---
layout: wiki
title: BackupRestore
permalink: /wiki/BackupRestore/
---

Qubes Backup, Restoration, and Migration
========================================

1.  [Qubes Backup, Restoration, and Migration](#QubesBackupRestorationandMigration)
    1.  [Creating a Backup](#CreatingaBackup)
    2.  [Restoring from a Backup](#RestoringfromaBackup)
    3.  [Emergency Backup Recovery without Qubes](#EmergencyBackupRecoverywithoutQubes)
    4.  [Migrating Between Two Physical Machines](#MigratingBetweenTwoPhysicalMachines)
    5.  [Troubleshooting and Technical Details](#TroubleshootingandTechnicalDetails)

With Qubes, it's easy to back up and restore your whole system, as well as to migrate between two physical machines.

As of Qubes R2B3, these functions are integrated into the Qubes VM Manager GUI. There are also two command-line tools available which perform the same functions: [qvm-backup](/wiki/Dom0Tools/QvmBackup) and [qvm-backup-restore](/wiki/Dom0Tools/QvmBackupRestore).

Creating a Backup
-----------------

1.  In **Qubes VM Manager**, click **System** on the menu bar, then click **Backup VMs** in the dropdown list. This brings up the **Qubes Backup VMs** window.

1.  Move the AppVMs which you desire to back up to the right-hand **Selected** column. AppVMs in the left-hand **Available** column will not be backed up.

> **Note:** An AppVM must be shut down in order to be backed up. Currently running AppVMs appear in red.

> Once you have selected all desired AppVMs, click **Next**.

1.  Select the destination for the backup:

-   If you wish to send your backup to a [USB mass storage device](/wiki/StickMounting), select the device in the dropdown box next to **Device**.
-   If you wish to send your backup to a (currently running) AppVM, select the AppVM in the dropdown box next to **Target AppVM**.

> You must also specify a directory on the device or in the AppVM, or a command to be executed in the AppVM as a destination for your backup. For example, if you wish to send your backup to the `~/backups` folder in the target AppVM, you would simply type `backups` in this field. This destination directory must already exist. If it does not exist, you must create it manually prior to backing up.

> By specifying the appropriate directory as the destination in an AppVM, it is possible to send the backup directly to, e.g., a USB mass storage device attached to the AppVM. Likewise, it is possible to enter any command as a backup target by specifying the command as the destination in the AppVM. This can be used to send your backup directly to, e.g., a remote server using SSH.

> At this point, you must also choose whether to encrypt your backup by checking or unchecking the **Encrypt backup** box.

> **Note:** It is strongly recommended that you opt to encrypt all backups which will be sent to untrusted destinations!

> **Note:** The supplied passphrase is used for **both** encryption/decryption and integrity verification. If you decide not to encrypt your backup (by unchecking the **Encrypt backup** box), the passphrase you supply will be used **only** for integrity verification. If you supply a passphrase but do not check the **Encrypt backup** box, your backup will **not** be encrypted!

1.  When you are ready, click **Next**. Qubes will proceed to create your backup. Once the progress bar has completed, you may click **Finish**.

Restoring from a Backup
-----------------------

1.  In **Qubes VM Manager**, click **System** on the menu bar, then click **Restore VMs from backup** in the dropdown list. This brings up the **Qubes Restore VMs** window.

1.  Select the source location of the backup to be restored:

-   If your backup is located on a [USB mass storage device](/wiki/StickMounting), select the device in the dropdown box next to **Device**.
-   If your backup is located in a (currently running) AppVM, select the AppVM in the dropdown box next to **AppVM**.

> You must also specify the directory in which the backup resides (or a command to be executed in an AppVM). If you followed the instructions in the previous section, "Creating a Backup," then your backup is most likely in the location you chose as the destination in step 3. For example, if you had chosen the `~/backups` directory of an AppVM as your destination in step 3, you would now select the same AppVM and again type `backups` into the **Backup directory** field.

> **Note:** After you have typed the directory location of the backup in the **Backup directory** field, click the ellipsis button `...` to the right of the field.

1.  There are three options you may select when restoring from a backup:
    1.  **ignore missing**: If any of the AppVMs in your backup depended upon a NetVM, ProxyVM, or TemplateVM which is not present in (i.e., "missing from") the current system, checking this box will ignore the fact that they are missing and restore the AppVMs anyway.
    2.  **ignore username mismatch**: This option applies only to the restoration of dom0's home directory. If your backup was created on a Qubes system which had a different dom0 username than the dom0 username of the current system, then checking this box will ignore the mismatch between the two usernames and proceed to restore the home directory anyway.
    3.  **skip dom0**: If this box is checked, dom0's home directory will not be restored from your backup.

1.  If your backup is encrypted, you must check the **Encrypted backup** box. If a passphrase was supplied during the creation of your backup (regardless of whether it is encrypted), then you must supply it here.

> **Note:** The passphrase which was supplied when the backup was created was used for **both** encryption/decryption and integrity verification. If the backup was not encrypted, the supplied passphrase is used only for integrity verification.

> **Note:** An AppVM cannot be restored from a backup if an AppVM with the same name already exists on the current system. You must first remove or change the name of any AppVM with the same name in order to restore such an AppVM.

1.  When you are ready, click **Next**. Qubes will proceed to restore from your backup. Once the progress bar has completed, you may click **Finish**.

Emergency Backup Recovery without Qubes
---------------------------------------

The Qubes backup system has been designed with emergency disaster recovery in mind. No special Qubes-specific tools are required to access data backed up by Qubes. In the event a Qubes system is unavailable, you can access your data on any GNU/Linux system with the following procedure.

> **Note:** In the following example, the backup file is assumed to be both encrypted and compressed.

1.  Untar the main backup file.

    ``` {.wiki}
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
    ```

1.  Verify the integrity of the `private.img` file which houses your data.

    ``` {.wiki}
    [user@restore ~]$ cd vm1/
    [user@restore vm1]$ openssl dgst -sha512 -hmac "your_passphrase" private.img.000
    HMAC-SHA512(private.img.000)= cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
    [user@restore vm1]$ cat private.img.000.hmac 
    (stdin)= cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
    ```

> **Note:** The hash values should match. If they do not match, then the backup file may have been tampered with, or there may have been a storage error.

> **Note:** If your backup was hashed with a message digest algorithm other than `sha512`, you must substitute the correct message digest command. A complete list of supported message digest algorithms can be found with `openssl list-message-digest-algorithms`.

1.  Decrypt the `private.img` file.

    ``` {.wiki}
    [user@restore vm1]$ openssl enc -d -pass pass:your_passphrase -aes-256-cbc -in private.img.000 -out private.img.dec.000
    ```

> **Note:** For multi-part files, a loop can be used:
>
> ``` {.wiki}
> for f in private.img.*; do
>   openssl enc -d -pass pass:your_passphrase -aes-256-cbc -in $f -out
> ${f/.img/.img.dec}
> done
> ```

> **Note:** If your backup was encrypted with a cipher algorithm other than `aes-256-cbc`, you must substitute the correct cipher command. A complete list of supported cipher algorithms can be found with `openssl list-cipher-algorithms`.

1.  Decompress the decrypted `private.img` file.

    ``` {.wiki}
    [user@restore vm1]$ zforce private.img.dec.*
    [user@restore vm1]$ gunzip private.img.dec.000.gz
    ```

> **Note:** If your backup was compressed with a program other than `gzip`, you must substitute the correct compression program.

1.  Untar the decrypted and decompressed `private.img` file.

    ``` {.wiki}
    [user@restore vm1]$ tar -M -xvf private.img.dec.000
    vm1/private.img
    ```

    **Note:** For multi-part files, a script is required:

    1.  Create a `new-volume-script`:

        ``` {.wiki}
        #!/bin/sh
        name=`expr $TAR_ARCHIVE : '\(.*\)\..*'`
        suffix=`printf %03d $[ $TAR_VOLUME - 1 ]`
        echo $name.$suffix >&$TAR_FD
        ```

    2.  `chmod +x new-volume-script`.
    3.  `tar --new-volume-script=./new-volume-script -xvf private.img.dec.000`. (The `--new-volume-script` option enables multi-volume untaring.)

1.  Mount the private.img file and access your data.

    ``` {.wiki}
    [user@restore vm1]$ sudo mkdir /mnt/img
    [user@restore vm1]$ sudo mount -o loop vm1/private.img /mnt/img/
    [user@restore vm1]$ cat /mnt/img/home/user/your_data.txt
    This data has been successfully recovered!
    ```

> **Note:** You may wish to store a plain text copy of these instructions with your Qubes backups in the event that you fail to recall the above procedure while this web page is inaccessible. You may download a plain text copy of this page by clicking the `Plain Text` link at the bottom of this page (as with every page on this wiki). In addition, the whole wiki is synced hourly with a public Git repo at:
>
> ``` {.wiki}
> git://gitorious.org/qubes-os/wiki.git
> ```

Migrating Between Two Physical Machines
---------------------------------------

In order to migrate your Qubes system from one physical machine to another, simply follow the backup procedure on the old machine, [install Qubes](/wiki/QubesDownloads) on the new machine, and follow the restoration procedure on the new machine. All of your settings and data will be preserved!

Troubleshooting and Technical Details
-------------------------------------

-   For troubleshooting (especially if you encounter a bug or error message during the backup or restore process), please refer to [​this thread](https://groups.google.com/d/topic/qubes-users/XfyJHSCD4_U/discussion).

-   For the technical details of the backup system, please refer to [​this thread](https://groups.google.com/d/topic/qubes-devel/TQr_QcXIVww/discussion).

