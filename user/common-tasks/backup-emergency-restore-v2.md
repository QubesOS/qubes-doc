---
lang: en
layout: doc
redirect_from:
- /doc/backup-emergency-restore-v2/
- /en/doc/backup-emergency-restore-v2/
- /doc/BackupEmergencyRestoreV2/
ref: 207
title: Emergency Backup Recovery (v2)
---

============================================

This page describes how to perform emergency restore of backup created on Qubes
R2 Beta3 or earlier (which uses backup format 2).

The Qubes backup system has been designed with emergency disaster recovery in
mind. No special Qubes-specific tools are required to access data backed up by
Qubes. In the event a Qubes system is unavailable, you can access your data on
any GNU/Linux system with the following procedure.

**Note:** In the following example, the backup file is assumed to be both
encrypted and compressed.

1. Untar the main backup file.

    ~~~
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
    ~~~

2. Verify the integrity of the `private.img` file which houses your data.

    ~~~
    [user@restore ~]$ cd vm1/
    [user@restore vm1]$ openssl dgst -sha512 -hmac "your_passphrase" private.img.000
    HMAC-SHA512(private.img.000)= cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
    [user@restore vm1]$ cat private.img.000.hmac
    (stdin)= cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
    ~~~

  **Note:** The hash values should match. If they do not match, then the backup
  file may have been tampered with, or there may have been a storage error.

  **Note:** If your backup was hashed with a message digest algorithm other
  than `sha512`, you must substitute the correct message digest command. A
  complete list of supported message digest algorithms can be found with
  `openssl list-message-digest-algorithms`.

3. Decrypt the `private.img` file.

    ~~~
    [user@restore vm1]$ openssl enc -d -pass pass:your_passphrase -aes-256-cbc -in private.img.000 -out private.img.dec.000
    ~~~

  **Note:** For multi-part files, a loop can be used:

  ~~~
  find -name 'private.img.*' | sort -V | while read f; do
    openssl enc -d -pass pass:your_passphrase -aes-256-cbc -in $f -out
  ${f/.img/.img.dec}
  done
  ~~~

  **Note:** If your backup was encrypted with a cipher algorithm other than
  `aes-256-cbc`, you must substitute the correct cipher command. A complete
  list of supported cipher algorithms can be found with `openssl
  list-cipher-algorithms`.

4. Decompress the decrypted `private.img` file.

    ~~~
    [user@restore vm1]$ zforce private.img.dec.*
    [user@restore vm1]$ gunzip private.img.dec.000.gz
    ~~~

  **Note:** If your backup was compressed with a program other than `gzip`, you
  must substitute the correct compression program.

5. Untar the decrypted and decompressed `private.img` file.

    ~~~
    [user@restore vm1]$ tar -M -xvf private.img.dec.000
    vm1/private.img
    ~~~

    **Note:** For multi-part files, a script is required:

    1. Create a `new-volume-script`:

        ~~~
        #!/bin/sh
        name=`expr $TAR_ARCHIVE : '\(.*\)\..*'`
        suffix=`printf %03d $[ $TAR_VOLUME - 1 ]`
        echo $name.$suffix >&$TAR_FD
        ~~~

    2. `chmod +x new-volume-script`.
    3. `tar --new-volume-script=./new-volume-script -xvf private.img.dec.000`.
        (The `--new-volume-script` option enables multi-volume untaring.)

6. Mount the private.img file and access your data.

    ~~~
    [user@restore vm1]$ sudo mkdir /mnt/img
    [user@restore vm1]$ sudo mount -o loop vm1/private.img /mnt/img/
    [user@restore vm1]$ cat /mnt/img/home/user/your_data.txt
    This data has been successfully recovered!
    ~~~

  **Note:** You may wish to store a plain text copy of these instructions with
  your Qubes backups in the event that you fail to recall the above procedure
  while this web page is inaccessible. You may obtain a plaintext version of
  this file in Git repository housing all the documentation on [Github](https://github.com/QubesOS/qubes-doc.git)
