---
layout: doc
title: Emergency Backup Recovery (v3)
permalink: /doc/backup-emergency-restore-v3/
redirect_from:
- /en/doc/backup-emergency-restore-v3/
- /doc/BackupEmergencyRestoreV3/
---

Emergency Backup Recovery without Qubes (v3)
============================================

This page describes how to perform an emergency restore of a backup created on
Qubes R2 or later (which uses backup format version 3).

The Qubes backup system has been designed with emergency disaster recovery in
mind. No special Qubes-specific tools are required to access data backed up by
Qubes. In the event a Qubes system is unavailable, you can access your data on
any GNU/Linux system with the following procedure.

**Note:** In the following example, the backup file is both *encrypted* and
*compressed*.

 1. Untar the main backup file.

        [user@restore ~]$ tar -i -xvf qubes-backup-2015-06-05T123456
        backup-header
        backup-header.hmac
        qubes.xml.000
        qubes.xml.000.hmac
        vm1/private.img.000
        vm1/private.img.000.hmac
        vm1/icon.png.000
        vm1/icon.png.000.hmac
        vm1/firewall.xml.000
        vm1/firewall.xml.000.hmac
        vm1/whitelisted-appmenus.list.000
        vm1/whitelisted-appmenus.list.000.hmac
        dom0-home/dom0user.000
        dom0-home/dom0user.000.hmac

 2. Verify the integrity of the `backup-header` file, which contains basic
    information about your backup.

        [user@restore ~]$ openssl dgst -sha512 -hmac "your_passphrase" backup-header
        HMAC-SHA512(backup-header)= 5b266783e116fe3b2601a54c249ca5f5f96d421dfe6828eeaeb2dcd014e9e945c27b3d7b0f952f5d55c927318906d9c360f387b0e1f069bb8195e96543e2969c
        [user@restore ~]$ cat backup-header.hmac
        (stdin)= 5b266783e116fe3b2601a54c249ca5f5f96d421dfe6828eeaeb2dcd014e9e945c27b3d7b0f952f5d55c927318906d9c360f387b0e1f069bb8195e96543e2969c

    **Note:** The hash values should match. If they do not match, then the
    backup file may have been tampered with, or there may have been a storage
    error.

    **Note:** If your backup was hashed with a message digest algorithm other
    than `sha512`, you must substitute the correct message digest command. This
    information is contained in the `backup-header` file (see step 3), however
    it is not recommended to open this file until its integrity and
    authenticity has been verified (the current step). A complete list of
    supported message digest algorithms can be found with `openssl
    list-message-digest-algorithms`.

 3. Read the `backup-header`. You'll need some of this information later. The
    file will look similar to this:

        [user@restore ~]$ cat backup-header
        version=3
        hmac-algorithm=SHA512
        crypto-algorithm=aes-256-cbc
        encrypted=True
        compressed=True
        compression-filter=gzip

    **Note:** If you see `version=2` here, go to [Emergency Backup Recovery -
    format version 2](/doc/backup-emergency-restore-v2/) instead.

 4. Verify the integrity of the `private.img` file which houses your data.

        [user@restore ~]$ cd vm1/
        [user@restore vm1]$ openssl dgst -sha512 -hmac "your_passphrase" private.img.000
        HMAC-SHA512(private.img.000)= cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
        [user@restore vm1]$ cat private.img.000.hmac
        (stdin)= cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e

    **Note:** The hash values should match. If they do not match, then the
    backup file may have been tampered with, or there may have been a storage
    error.

    **Note:** If your backup was hashed with a message digest algorithm other
    than `sha512`, you must substitute the correct message digest command. This
    information is contained in the `backup-header` file (see step 3). A
    complete list of supported message digest algorithms can be found with
    `openssl list-message-digest-algorithms`.

 5. Decrypt the `private.img` file.

        [user@restore vm1]$ find -name 'private.img.*[0-9]' | sort -V | xargs cat | openssl enc -d -pass pass:your_passphrase -aes-256-cbc -out private.img.dec

    **Note:** If your backup was encrypted with a cipher algorithm other than
    `aes-256-cbc`, you must substitute the correct cipher command. This
    information is contained in the `backup-header` file (see step 3). A
    complete list of supported cipher algorithms can be found with `openssl
    list-cipher-algorithms`.

 6. Decompress the decrypted `private.img` file.

        [user@restore vm1]$ zforce private.img.dec
        private.img.dec -- replaced with private.img.dec.gz
        [user@restore vm1]$ gunzip private.img.dec.gz

    **Note:** If your backup was compressed with a program other than `gzip`,
    you must substitute the correct compression program. This information is
    contained in the `backup-header` file (see step 3). For example, if you
    used `bzip2`, then you should do this:

        [user@restore vm1]$ mv private.img.dec private.img.dec.bz2
        [user@restore vm1]$ bunzip2 private.img.dec.bz2

 7. Untar the decrypted and decompressed `private.img` file.

        [user@restore vm1]$ tar -xvf private.img.dec
        vm1/private.img

 8. Mount the private.img file and access your data.

        [user@restore vm1]$ sudo mkdir /mnt/img
        [user@restore vm1]$ sudo mount -o loop vm1/private.img /mnt/img/
        [user@restore vm1]$ cat /mnt/img/home/user/your_data.txt
        This data has been successfully recovered!

 9. Success! If you wish to recover data from more than one VM in your backup,
    simply repeat steps 4--8 for each additional VM.

    **Note:** You may wish to store a copy of these instructions with your
    Qubes backups in the event that you fail to recall the above procedure
    while this web page is inaccessible. All Qubes documentation, including
    this page, is available in plain text format in the following Git
    repository:

        https://github.com/QubesOS/qubes-doc.git
