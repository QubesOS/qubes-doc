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

This page describes how to perform an emergency restore of a backup created on Qubes R4.0 or later (which uses backup format version 4).

The Qubes backup system has been designed with emergency disaster recovery in mind. No special Qubes-specific tools are required to access data backed up by Qubes. In the event a Qubes system is unavailable, you can access your data on any GNU/Linux system with the following procedure.

**Note:** In the following example, the backup file is both *encrypted* and *compressed*.

 1. Backup content is encrypted and integrity protected using [scrypt
    utility](https://www.tarsnap.com/scrypt.html). You need to obtain it to
    restore your data.  If your distribution have it packaged (like on Debian),
    install the package standard way, otherwise you need to compile it yourself
    (verify its signature first!). 
    Versions up to 1.2.0 (inclusive) do not support `-P` option for easier
    scripting - which means you'll need to enter the passphrase for each file
    separately, instead of using `echo ... | scrypt`.

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

 3. Set backup passhprase environment variable. While this isn't strictly required, it will be handy later and will avoid saving the passphrase into shell history.

        read backup_pass

 4. Verify integrity of `backup-header`. For compatibility reasons `backup-header.hmac` is in fact is an encrypted *and integrity protected* version of `backup-header`.

        [user@restore ~]$ set +H
        [user@restore ~]$ echo "backup-header!$backup_pass" |\
            scrypt dec -P backup-header.hmac backup-header.verified && \
            diff -qs backup-header backup-header.verified
        Files backup-header and backup-header.verified are identical

    **Note:** If the above fail, it may be either mean that backup was tampered
with, or it is in different format (see point 3 above). In that case, look into
`backup-header`, at `version` field. If it contains anything else than
`version=4`, go to other version of instruction: [Emergency Backup Recovery -
format version 2](/doc/backup-emergency-restore-v2/), [Emergency Backup
Recovery - format version 3](/doc/backup-emergency-restore-v3/)

 5. Read the `backup-header`. You'll need some of this information later. The file will look similar to this:

        [user@restore ~]$ cat backup-header
        version=4
        encrypted=True
        compressed=True
        compression-filter=gzip
        backup_id=20161020T123455-1234
  
 6. Verify the integrity and decrypt the `private.img` file which houses your data.

        [user@restore ~]$ backup_id=20161020T123455-1234 # see backup-header above
        [user@restore ~]$ for f_enc in vm1/private.img.???.enc; do \
            f_dec=${f_enc%.enc}; \
            echo "$backup_id!$f_dec!$backup_pass" | scrypt dec -P $f_enc $f_dec || break; \
            done

    **Note:** If the above fail, most likely your backup is corrupted, or been tampered with.

 7. Decompress and untar the decrypted `private.img` file.

        [user@restore ~]$ cat vm1/private.img.??? | gzip -d | tar -xv
        vm1/private.img

    **Note:** If your backup was compressed with a program other than `gzip`, you must substitute the correct compression program. This information is contained in the `backup-header` file (see step 3).

 8. Mount the private.img file and access your data.

        [user@restore vm1]$ sudo mkdir /mnt/img
        [user@restore vm1]$ sudo mount -o loop vm1/private.img /mnt/img/
        [user@restore vm1]$ cat /mnt/img/home/user/your_data.txt
        This data has been successfully recovered!

 9. Success! If you wish to recover data from more than one VM in your backup, simply repeat steps 5--8 for each additional VM.

    **Note:** You may wish to store a copy of these instructions with your Qubes backups in the event that you fail to recall the above procedure while this web page is inaccessible. All Qubes documentation, including this page, is available in plain text format in the following Git repository:

        https://github.com/QubesOS/qubes-doc.git

