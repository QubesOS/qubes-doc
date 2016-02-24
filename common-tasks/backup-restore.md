---
layout: doc
title: Backup, Restoration, and Migration
permalink: /doc/backup-restore/
redirect_from:
- /en/doc/backup-restore/
- /doc/BackupRestore/
- /wiki/BackupRestore/
---

Qubes Backup, Restoration, and Migration
========================================

**Caution:** The Qubes backup system currently relies on a [weak key derivation scheme](https://github.com/QubesOS/qubes-issues/issues/971). It is *strongly recommended* that users select a *high-entropy* passphrase for use with Qubes backups.

 * [Creating a Backup](#creating-a-backup)
 * [Restoring from a Backup](#restoring-from-a-backup)
 * [Emergency Backup Recovery without Qubes](#emergency-backup-recovery-without-qubes)
 * [Migrating Between Two Physical Machines](#migrating-between-two-physical-machines)
 * [Notes](#notes)

With Qubes, it's easy to back up and restore your whole system, as well as to migrate between two physical machines.

As of Qubes R2B3, these functions are integrated into the Qubes VM Manager GUI. There are also two command-line tools available which perform the same functions: [qvm-backup](/doc/dom0-tools/qvm-backup/) and [qvm-backup-restore](/doc/dom0-tools/qvm-backup-restore/).


Creating a Backup
-----------------

1. In **Qubes VM Manager**, click **System** on the menu bar, then click **Backup VMs** in the drop-down list. This brings up the **Qubes Backup VMs** window.

2. Move the AppVMs which you desire to back up to the right-hand **Selected** column. AppVMs in the left-hand **Available** column will not be backed up.

   **Note:** An AppVM must be shut down in order to be backed up. Currently running AppVMs appear in red.

   Once you have selected all desired AppVMs, click **Next**.

3. Select the destination for the backup:

   - If you wish to send your backup to a [USB mass storage device](/doc/stick-mounting/), select the device in the drop-down box next to **Device** (feature removed in R3, select appropriate **Target AppVM** and mount the stick with one click in file selection dialog).
   - If you wish to send your backup to a (currently running) AppVM, select the AppVM in the drop-down box next to **Target AppVM**.

   You must also specify a directory on the device or in the AppVM, or a command to be executed in the AppVM as a destination for your backup. For example, if you wish to send your backup to the `~/backups` folder in the target AppVM, you would simply type `backups` in this field. This destination directory must already exist. If it does not exist, you must create it manually prior to backing up.

   By specifying the appropriate directory as the destination in an AppVM, it is possible to send the backup directly to, e.g., a USB mass storage device attached to the AppVM. Likewise, it is possible to enter any command as a backup target by specifying the command as the destination in the AppVM. This can be used to send your backup directly to, e.g., a remote server using SSH.

   At this point, you must also choose whether to encrypt your backup by checking or unchecking the **Encrypt backup** box.

   **Note:** It is strongly recommended that you opt to encrypt all backups which will be sent to untrusted destinations!

   **Note:** The supplied passphrase is used for **both** encryption/decryption and integrity verification. If you decide not to encrypt your backup (by unchecking the **Encrypt backup** box), the passphrase you supply will be used **only** for integrity verification. If you supply a passphrase but do not check the **Encrypt backup** box, your backup will **not** be encrypted!

4. When you are ready, click **Next**. Qubes will proceed to create your backup. Once the progress bar has completed, you may click **Finish**.


Restoring from a Backup
-----------------------

1. In **Qubes VM Manager**, click **System** on the menu bar, then click **Restore VMs from backup** in the drop-down list. This brings up the **Qubes Restore VMs** window.

2. Select the source location of the backup to be restored:

   - If your backup is located on a [USB mass storage device](/doc/stick-mounting/), select the device in the drop-down box next to **Device**.
   - If your backup is located in a (currently running) AppVM, select the AppVM in the drop-down box next to **AppVM**.

   You must also specify the directory in which the backup resides (or a command to be executed in an AppVM). If you followed the instructions in the previous section, "Creating a Backup," then your backup is most likely in the location you chose as the destination in step 3. For example, if you had chosen the `~/backups` directory of an AppVM as your destination in step 3, you would now select the same AppVM and again type `backups` into the **Backup directory** field.

   **Note:** After you have typed the directory location of the backup in the **Backup directory** field, click the ellipsis button `...` to the right of the field.

3. There are three options you may select when restoring from a backup:
   1.  **ignore missing**: If any of the AppVMs in your backup depended upon a NetVM, ProxyVM, or TemplateVM which is not present in (i.e., "missing from") the current system, checking this box will ignore the fact that they are missing and restore the AppVMs anyway.
   2.  **ignore username mismatch**: This option applies only to the restoration of dom0's home directory. If your backup was created on a Qubes system which had a different dom0 username than the dom0 username of the current system, then checking this box will ignore the mismatch between the two usernames and proceed to restore the home directory anyway.
   3.  **skip dom0**: If this box is checked, dom0's home directory will not be restored from your backup.

4. If your backup is encrypted, you must check the **Encrypted backup** box. If a passphrase was supplied during the creation of your backup (regardless of whether it is encrypted), then you must supply it here.

   **Note:** The passphrase which was supplied when the backup was created was used for **both** encryption/decryption and integrity verification. If the backup was not encrypted, the supplied passphrase is used only for integrity verification.

   **Note:** An AppVM cannot be restored from a backup if an AppVM with the same name already exists on the current system. You must first remove or change the name of any AppVM with the same name in order to restore such an AppVM.

5. When you are ready, click **Next**. Qubes will proceed to restore from your backup. Once the progress bar has completed, you may click **Finish**.


Emergency Backup Recovery without Qubes
---------------------------------------

The Qubes backup system has been designed with emergency disaster recovery in mind. No special Qubes-specific tools are required to access data backed up by Qubes. In the event a Qubes system is unavailable, you can access your data on any GNU/Linux system with the following procedure.

For emergency restore of backup created on Qubes R2 or newer take a look [here](/doc/backup-emergency-restore-v3/). For backups created on earlier Qubes version, take a look [here](/doc/backup-emergency-restore-v2/).


Migrating Between Two Physical Machines
---------------------------------------

In order to migrate your Qubes system from one physical machine to another, simply follow the backup procedure on the old machine, [install Qubes](/doc/downloads/) on the new machine, and follow the restoration procedure on the new machine. All of your settings and data will be preserved!


Notes
-----

 * The Qubes backup system relies on `openssl enc`, which is known to use a very weak key derivation scheme. The Qubes backup system also uses the same passphrase for authentication and for encryption, which is problematic from a security perspective. Users are advised to use a very high entropy passphrase for Qubes backups. For a full discussion, see [this thread](https://groups.google.com/d/msg/qubes-devel/CZ7WRwLXcnk/u_rZPoVxL5IJ).
 * For the technical details of the backup system, please refer to [this thread](https://groups.google.com/d/topic/qubes-devel/TQr_QcXIVww/discussion).
 * If working with symlinks, note the issues described in [this thread](https://groups.google.com/d/topic/qubes-users/EITd1kBHD30/discussion).
