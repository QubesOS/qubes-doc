---
layout: doc
title: Emergency Backup Recovery (v4)
redirect_from:
- /doc/backup-emergency-restore-v4/
- /en/doc/backup-emergency-restore-v4/
- /doc/BackupEmergencyRestoreV4/
---

Emergency Backup Recovery without Qubes (v4)
============================================

This page describes how to perform an emergency restore of a backup created on
Qubes R4.X (which uses backup format version 4).

The Qubes backup system has been designed with emergency disaster recovery in
mind. No special Qubes-specific tools are required to access data backed up by
Qubes. In the event a Qubes system is unavailable, you can access your data on
any GNU/Linux system with the following procedure.


Required `scrypt` Utility
-------------------------

In Qubes 4.X, backups are encrypted and integrity-protected with [scrypt]. You
will need a copy of this utility in order to access your data.  Since `scrypt`
is not pre-installed on every GNU/Linux system, it is strongly recommended that
you store a copy of it with your backups. If your distribution has `scrypt`
packaged (e.g., Debian), you can install the package in the standard way using
your distribution's package manager. Otherwise, you'll need to obtain a
compiled binary (instructions below) or compile the program from source
yourself. (Don't forget to [verify signatures] first!) Note that versions of
`scrypt` up to 1.2.0 (inclusive) do not support the `-P` option for easier
scripting, which means you'll need to enter the passphrase for each file
separately, instead of using `echo ... | scrypt`.

Here are instructions for obtaining a compiled `scrypt` binary. This example
uses an RPM-based system (Fedora), but the same general procedure should work on
any GNU/Linux system.

 1. If you're not on Qubes 4.X, [get and verify the Release 4 Signing Key].
 2. If you're not on Qubes 4.X, import the Release 4 Signing Key.

        [user@restore ~]$ sudo rpm --import qubes-release-4-signing-key.asc

 3. Download the `scrypt` RPM.

        [user@restore ~]$ dnf download scrypt

    or, if that doesn't work:

        [user@restore ~]$ curl -O https://yum.qubes-os.org/r4.0/current/vm/fc28/rpm/scrypt-1.2.1-1.fc28.x86_64.rpm

 4. Verify the signature on the `scrypt` RPM.

        [user@restore ~]$ rpm -K scrypt-*.rpm 
        scrypt-*.rpm: digests signatures OK

    The message `digests signatures OK` means that both the digest (i.e., the
    output of a hash function) and PGP signature verification were successful.

 5. Install `rpmdevtools`.

        [user@restore ~]$ sudo dnf install rpmdevtools

 6. Extract the `scrypt` binary from the RPM.

        [user@restore ~]$ rpmdev-extract scrypt-*.rpm

 7. (Optional) Create an alias for the new binary.

        [user@restore ~]$ alias scrypt="scrypt-*/usr/bin/scrypt"


Emergency Recovery Instructions
-------------------------------

**Note:** In the following example, the backup file is both *encrypted* and
*compressed*.

 1. Untar the main backup file.

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

    **To extract only specific VMs:** Each VM in the backup file has its path
    listed in `qubes.xml.000.enc`. Decrypt it. (In this example, the password is
    `password`.)

        [user@restore ~]$ cat backup-header | grep backup-id
        backup-id=20190128T123456-1234
        [user@restore ~]$ scrypt dec -P qubes.xml.000.enc qubes.xml.000
        Please enter passphrase: 20190128T123456-1234!qubes.xml.000!password
        [user@restore ~]$ tar -i -xvf qubes.xml.000

    Now that you have the decrypted `qubes.xml.000` file, search for the
    `backup-path` property inside of it. With the `backup-path`, extract only
    the files necessary for your VM (`vmX`).

        [user@restore ~]$ tar -i -xvf qubes-backup-2015-06-05T123456 \
            backup-header backup-header.hmac vmX/

 2. Set the backup passphrase environment variable. While this isn't strictly
    required, it will be handy later and will avoid saving the passphrase in
    the shell's history.

        [user@restore ~]$ read backup_pass

 3. Verify the integrity of `backup-header`. For compatibility reasons,
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
    - [Emergency Backup Recovery without Qubes (v2)]
    - [Emergency Backup Recovery without Qubes (v3)]

 4. Read `backup-header`:

        [user@restore ~]$ cat backup-header
        version=4
        encrypted=True
        compressed=True
        compression-filter=gzip
        backup_id=20161020T123455-1234

 5. Set `backup_id` to the value in the last line of `backup-header`:

        [user@restore ~]$ backup_id=20161020T123455-1234

 6. Verify the integrity of and decrypt the `private.img` file that houses your
    data.

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
    contained in `backup-header` (see step 4). For example, if you used `bzip2`,
    then you should do this:

        [user@restore vm1]$ mv private.img.dec private.img.dec.bz2
        [user@restore vm1]$ bunzip2 private.img.dec.bz2

 8. Mount `private.img` and access your data.

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

[scrypt]: https://www.tarsnap.com/scrypt.html
[verify signatures]: https://www.qubes-os.org/security/verifying-signatures
[get and verify the Release 4 Signing Key]: https://www.qubes-os.org/security/verifying-signatures/#2-get-the-release-signing-key
[Emergency Backup Recovery without Qubes (v2)]: https://www.qubes-os.org/doc/backup-emergency-restore-v2/
[Emergency Backup Recovery without Qubes (v3)]: https://www.qubes-os.org/doc/backup-emergency-restore-v3/

