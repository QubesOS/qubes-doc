---
layout: doc
title: Emergency Backup Recovery - format version 4
permalink: /doc/backup-emergency-restore-v4/
redirect_from:
- /en/doc/backup-emergency-restore-v4/
- /doc/BackupEmergencyRestoreV4/
---

Emergency Backup Recovery without Qubes - format version 4
==========================================================

This page describes how to perform an emergency restore of a backup created on
Qubes R4.0 or later (which uses backup format version 4).

The Qubes backup system has been designed with emergency disaster recovery in
mind. No special Qubes-specific tools are required to access data backed up by
Qubes. In the event a Qubes system is unavailable, you can access your data on
any GNU/Linux system with the following procedure.

**Note:** The backup content is encrypted and integrity-protected with the
[`scrypt` utility](https://www.tarsnap.com/scrypt.html). You will need a copy
of this utility in order to access your data. For this reason, it is strongly
recommended that you store a copy of this utility with your backups. If your
distribution has `scrypt` packaged (e.g., Debian), you can install the package
in the standard way using your distribution's package manager. Otherwise,
you'll need to download a compiled binary or compile the program from source
yourself. (Don't forget to [verify signatures](/security/verifying-signatures)
first!) Note that versions of `scrypt` up to 1.2.0 (inclusive) do not support
the `-P` option for easier scripting, which means you'll need to enter the
passphrase for each file separately, instead of using `echo ... | scrypt`.

**Note:** In the following example, the backup file is both *encrypted* and
*compressed*.

 2. Untar the main backup file.

        [user@restore ~]$ tar -i -xvf qubes-backup-2015-06-05T123456
        backup-header
        backup-header.hmac
        qubes.xml.000.enc
        vm1/private.img.000.enc
        vm1/private.img.001.enc
        vm1/private.img.002.enc
        vm1/icon.png.000.enc
        vm1/firewall.xml.000.enc
        vm1/whitelisted-appmenus.list.000.enc
        dom0-home/dom0user.000.enc

    **Note:** Each VM in the backup file has its path listed in
    `qubes.xml.000.enc` (search for the `backup-path` property). You can
    extract only the files necessary for your VM (`vmX`) with `tar -i -xvf
    qubes-backup-2015-06-05T123456 backup-header backup-header.hmac vmX/`.

 3. Set the backup passhprase environment variable. While this isn't strictly
    required, it will be handy later and will avoid saving the passphrase in
    the shell's history.

        read backup_pass

 4. Verify the integrity of `backup-header`. For compatibility reasons,
    `backup-header.hmac` is an encrypted *and integrity protected*
    version of `backup-header`.

        [user@restore ~]$ set +H
        [user@restore ~]$ echo "backup-header!$backup_pass" |\
            scrypt dec -P backup-header.hmac backup-header.verified && \
            diff -qs backup-header backup-header.verified
        Files backup-header and backup-header.verified are identical

    **Note:** If this command fails, it may be that the backup was tampered
    with or is in a different format. In the latter case, look inside
    `backup-header` at the `version` field. If it contains a value other than
    `version=4`, go to the instructions for that format version:
    - [Emergency Backup Recovery - format version 2](/doc/backup-emergency-restore-v2/)
    - [Emergency Backup Recovery - format version 3](/doc/backup-emergency-restore-v3/)

 5. Read `backup-header`. You'll need some of this information later. The
    file will look similar to this:

        [user@restore ~]$ cat backup-header
        version=4
        encrypted=True
        compressed=True
        compression-filter=gzip
        backup_id=20161020T123455-1234
  
 6. Verify the integrity of and decrypt the `private.img` file that houses your
    data.

        [user@restore ~]$ backup_id=20161020T123455-1234 # see backup-header above
        [user@restore ~]$ for f_enc in vm1/private.img.???.enc; do \
            f_dec=${f_enc%.enc}; \
            echo "$backup_id!$f_dec!$backup_pass" | scrypt dec -P $f_enc $f_dec || break; \
            done

    **Note:** If this command fails, it is likely that the backup is corrupted
    or has been tampered with.

 7. Decompress and untar the decrypted `private.img` file.

        [user@restore ~]$ cat vm1/private.img.??? | gzip -d | tar -xv
        vm1/private.img

    **Note:** If your backup was compressed with a program other than `gzip`,
    you must substitute the correct compression program. This information is
    contained in the `backup-header` file (see step 3). For example, if you
    used `bzip2`, then you should do this:

        [user@restore vm1]$ mv private.img.dec private.img.dec.bz2
        [user@restore vm1]$ bunzip2 private.img.dec.bz2

 8. Mount the private.img file and access your data.

        [user@restore vm1]$ sudo mkdir /mnt/img
        [user@restore vm1]$ sudo mount -o loop vm1/private.img /mnt/img/
        [user@restore vm1]$ cat /mnt/img/home/user/your_data.txt
        This data has been successfully recovered!

 9. Success! If you wish to recover data from more than one VM in your backup,
    simply repeat steps 6--8 for each additional VM.

    **Note:** You may wish to store a copy of these instructions with your
    Qubes backups in the event that you fail to recall the above procedure
    while this web page is inaccessible. All Qubes documentation, including
    this page, is available in plain text format in the following Git
    repository:

        https://github.com/QubesOS/qubes-doc.git

