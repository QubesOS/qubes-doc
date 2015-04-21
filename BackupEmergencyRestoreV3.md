---
layout: doc
title: Emergency Backup Recovery - format version 3
permalink: /doc/BackupEmergencyRestoreV3/
---

Emergency Backup Recovery without Qubes - format version 3
==========================================================

This page describes how to perform emergency restore of backup created on Qubes R2 or later (which uses backup format 3).

The Qubes backup system has been designed with emergency disaster recovery in mind. No special Qubes-specific tools are required to access data backed up by Qubes. In the event a Qubes system is unavailable, you can access your data on any GNU/Linux system with the following procedure.

**Note:** In the following example, the backup file is assumed to be both encrypted and compressed.

1.  Untar the main backup file.

    [user@restore ~]$ tar -i -xvf qubes-backup-2013-12-26-123456
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

1. Verify the integrity of the `backup-header` file contains basic information about your backup.
    [user@restore ~]$ cd vm1/
    [user@restore ~]$ openssl dgst -sha512 -hmac "your_passphrase" backup-header
    HMAC-SHA512(backup-header)= 5b266783e116fe3b2601a54c249ca5f5f96d421dfe6828eeaeb2dcd014e9e945c27b3d7b0f952f5d55c927318906d9c360f387b0e1f069bb8195e96543e2969c
    [user@restore ~]$ cat backup-header.hmac 
    (stdin)= 5b266783e116fe3b2601a54c249ca5f5f96d421dfe6828eeaeb2dcd014e9e945c27b3d7b0f952f5d55c927318906d9c360f387b0e1f069bb8195e96543e2969c

  **Note:** The hash values should match. If they do not match, then the backup file may have been tampered with, or there may have been a storage error.

  **Note:** If your backup was hashed with a message digest algorithm other than `sha512`, you must substitute the correct message digest command. A complete list of supported message digest algorithms can be found with `openssl list-message-digest-algorithms`.

1. Read the `backup-header`. You'll need some of this information later. The file will look similar to this:
    version=3
    hmac-algorithm=SHA512
    crypto-algorithm=aes-256-cbc
    encrypted=True
    compressed=True
  
  If you see `version=2` here, go to [Emergency Backup Recovery - format version 2](/doc/BackupEmergencyRestoreV2/) page instead.

1. Verify the integrity of the `private.img` file which houses your data.

    [user@restore ~]$ cd vm1/
    [user@restore vm1]$ openssl dgst -sha512 -hmac "your_passphrase" private.img.000
    HMAC-SHA512(private.img.000)= cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
    [user@restore vm1]$ cat private.img.000.hmac 
    (stdin)= cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e

  **Note:** The hash values should match. If they do not match, then the backup file may have been tampered with, or there may have been a storage error.

  **Note:** If your backup was hashed with a message digest algorithm other than `sha512`, you must substitute the correct message digest command. A complete list of supported message digest algorithms can be found with `openssl list-message-digest-algorithms`. You can check `backup-header` file for the hash used to create the backup.

1. Decrypt the `private.img` file.

    cat private.img.??? | openssl enc -d -pass pass:your_passphrase -aes-256-cbc -out private.img.dec

  **Note:** If your backup was encrypted with a cipher algorithm other than `aes-256-cbc`, you must substitute the correct cipher command. A complete list of supported cipher algorithms can be found with `openssl list-cipher-algorithms`. You can check `backup-header` file to get that information.

1. Decompress the decrypted `private.img` file.

    [user@restore vm1]$ zforce private.img.dec
    [user@restore vm1]$ gunzip private.img.dec.gz

  **Note:** If your backup was compressed with a program other than `gzip`, you must substitute the correct compression program. `backup-header` file contains name of program used to compress the data.

1. Untar the decrypted and decompressed `private.img` file.

    [user@restore vm1]$ tar -xvf private.img.dec
    vm1/private.img

1.  Mount the private.img file and access your data.

    [user@restore vm1]$ sudo mkdir /mnt/img
    [user@restore vm1]$ sudo mount -o loop vm1/private.img /mnt/img/
    [user@restore vm1]$ cat /mnt/img/home/user/your_data.txt
    This data has been successfully recovered!

  **Note:** You may wish to store a plain text copy of these instructions with your Qubes backups in the event that you fail to recall the above procedure while this web page is inaccessible. You may obtain a plaintext version of this file in Git repository housing all the documentation at:

    https://github.com/QubesOS/qubes-doc.git

