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

**Caution:** The Qubes R3.2 backup system currently relies on a [weak key derivation scheme](https://github.com/QubesOS/qubes-issues/issues/971). 
Although resolved in R4.0 and higher with the switch to scrypt, it is *strongly recommended* that users select a *high-entropy* passphrase for use with Qubes backups.


With Qubes, it's easy to back up and restore your whole system, as well as to migrate between two physical machines.

As of Qubes R2B3, these functions are integrated into the Qubes VM Manager GUI.
There are also two command-line tools available which perform the same functions: [qvm-backup](/doc/dom0-tools/qvm-backup/) and [qvm-backup-restore](/doc/dom0-tools/qvm-backup-restore/).


Creating a Backup (R4.0 and later)
-----------------

1. Go to **Applications menu -> System Tools -> Backup Qubes**.
This brings up the **Qubes Backup VMs** window.

2. Move the VMs that you want to back up to the right-hand **Selected** column.
VMs in the left-hand **Available** column will not be backed up.

   You may choose whether to compress backups by checking or unchecking the **Compress the backup** box.
   Normally this should be left on unless you have a specific reason otherwise.
   
   Once you have selected all desired VMs, click **Next**.

3. Select the destination for the backup:

   If you wish to send your backup to a (currently running) VM, select the VM in the drop-down box next to **Target AppVM**.
   If you wish to send your backup to a [USB mass storage device](/doc/usb/), you can use the directory selection widget to mount a connected device (under "Other locations" item on the left); or first mount the device in a VM, then select the mount point inside that VM as the backup destination.

   You must also specify a directory on the device or in the VM, or a command to be executed in the VM as a destination for your backup. 
   For example, if you wish to send your backup to the `~/backups` folder in the target VM, you would simply browse to it using the convenient directory selection dialog (`...`) at the right.
   This destination directory must already exist.
   If it does not exist, you must create it manually prior to backing up.

   By specifying the appropriate directory as the destination in a VM, it is possible to send the backup directly to, e.g., a USB mass storage device attached to the VM.
   Likewise, it is possible to enter any command as a backup target by specifying the command as the destination in the VM.
   This can be used to send your backup directly to, e.g., a remote server using SSH.

   **Note:** The supplied passphrase is used for **both** encryption/decryption and integrity verification.

   At this point, you may also choose whether to save your settings by checking or unchecking the **Save settings as default backup profile** box.
   
   **Warning: Saving the settings will result in your backup passphrase being saved in plaintext in dom0, so consider your threat model before checking this box.**

4. You will now see the summary of VMs to be backed up.
If there are any issues preventing the backup, they will be listed here and the **Next** button grayed out.

5. When you are ready, click **Next**.
Qubes will proceed to create your backup. 
Once the progress bar has completed, you may click **Finish**.

Creating a Backup (R3.2 and earlier)
-----------------

1. In **Qubes VM Manager**, click **System** on the menu bar, then click **Backup VMs** in the drop-down list.
This brings up the **Qubes Backup VMs** window.

2. Move the VMs that you want to back up to the right-hand **Selected** column. 
VMs in the left-hand **Available** column will not be backed up.

   **Note:** A VM must be shut down in order to be backed up. 
   Currently running VMs appear in red.

   Once you have selected all desired VMs, click **Next**.

3. Select the destination for the backup:

   If you wish to send your backup to a (currently running) VM, select the VM in the drop-down box next to **Target AppVM**.
   If you wish to send your backup to a [USB mass storage device](/doc/usb/), you can use the directory selection widget to mount a connected device (under "Other locations" item on the left); or first mount the device in a VM, then select the mount point inside that VM as the backup destination.

   You must also specify a directory on the device or in the VM, or a command to be executed in the VM as a destination for your backup. 
   For example, if you wish to send your backup to the `~/backups` folder in the target VM, you would simply browse to it using the convenient directory selection dialog (`...`) at the right.
   If it does not exist, you must create it manually prior to backing up.

   By specifying the appropriate directory as the destination in a VM, it is possible to send the backup directly to, e.g., a USB mass storage device attached to the VM. 
   Likewise, it is possible to enter any command as a backup target by specifying the command as the destination in the VM.
   This can be used to send your backup directly to, e.g., a remote server using SSH.

   At this point, you must also choose whether to encrypt your backup by checking or unchecking the **Encrypt backup** box.

   **Note:** It is strongly recommended that you opt to encrypt all backups which will be sent to untrusted destinations!

   **Note:** The supplied passphrase is used for **both** encryption/decryption and integrity verification.
   If you decide not to encrypt your backup (by unchecking the **Encrypt backup** box), the passphrase you supply will be used **only** for integrity verification.
   If you supply a passphrase but do not check the **Encrypt backup** box, your backup will **not** be encrypted!

4. You will now see the summary of VMs to be backed up. 
If there are any issues preventing the backup, they will be listed here and the **Next** button grayed out.

5. When you are ready, click **Next**.
Qubes will proceed to create your backup. 
Once the progress bar has completed, you may click **Finish**.


Restoring from a Backup (R4.0 and later)
-----------------------

1. Go to **Applications menu -> System Tools -> Restore Backup**.
This brings up the **Qubes Restore VMs** window.

2. Select the source location of the backup to be restored:

   - If your backup is located on a [USB mass storage device](/doc/usb/), attach it first to another VM or select `sys-usb` in the next item.
   - If your backup is located in a (currently running) VM, select the VM in the drop-down box next to **AppVM**.

   You must also specify the directory and filename of the backup (or a command to be executed in a VM) in the **Backup file** field. 
   If you followed the instructions in the previous section, "Creating a Backup," then your backup is most likely in the location you chose as the destination in step 3.
   For example, if you had chosen the `~/backups` directory of a VM as your destination in step 3, you would now select the same VM and again browse to (using `...`) the `backups` folder.
   Once you've located the backup file, double-click it or select it and hit **OK**.

3. There are three options you may select when restoring from a backup:
   1.  **ignore missing templates and net VMs**: If any of the VMs in your backup depended upon a NetVM or TemplateVM that is not present in (i.e., "missing from") the current system, checking this box will ignore the fact that they are missing and restore the VMs anyway and set them to use the default NetVM and system default template.
   2.  **ignore username mismatch**: This option applies only to the restoration of dom0's home directory.
   If your backup was created on a Qubes system which had a different dom0 username than the dom0 username of the current system, then checking this box will ignore the mismatch between the two usernames and proceed to restore the home directory anyway.
   3.  **Verify backup integrity, do not restore the data**: This will scan the backup file for corrupted data.
   However, it does not currently detect if it is missing data as long as it is a correctly structured, non-corrupted backup file.
   See [issue #3498](https://github.com/QubesOS/qubes-issues/issues/3498) for more details.

4. If your backup is encrypted, you must check the **Encrypted backup** box. 
If a passphrase was supplied during the creation of your backup (regardless of whether it is encrypted), then you must supply it here.

   **Note:** The passphrase which was supplied when the backup was created was used for **both** encryption/decryption and integrity verification. 
   If the backup was not encrypted, the supplied passphrase is used only for integrity verification.
   All backups made from a Qubes R4.0 system will be encrypted.

5. You will now see the summary of VMs to be restored. 
If there are any issues preventing the restore, they will be listed here and the **Next** button grayed out.

6. When you are ready, click **Next**. 
Qubes will proceed to restore from your backup. 
Once the progress bar has completed, you may click **Finish**.

Restoring from a Backup (R3.2 and earlier)
-----------------------

1. In **Qubes VM Manager**, click **System** on the menu bar, then click **Restore VMs from backup** in the drop-down list. 
This brings up the **Qubes Restore VMs** window.

2. Select the source location of the backup to be restored:

   - If your backup is located on a [USB mass storage device](/doc/usb/), attach it first to another VM or select `sys-usb` in the next item.
   - If your backup is located in a (currently running) VM, select the VM in the drop-down box next to **AppVM**.

   You must also specify the directory and filename of the backup (or a command to be executed in a VM) in the **Backup file** field.
   If you followed the instructions in the previous section, "Creating a Backup," then your backup is most likely in the location you chose as the destination in step 3.
   For example, if you had chosen the `~/backups` directory of a VM as your destination in step 3, you would now select the same VM and again browse to (using `...`) the `backups` folder. 
   Once you've located the backup file, double-click or select it and hit **OK**.

3. There are three options you may select when restoring from a backup:
   1.  **ignore missing**: If any of the VMs in your backup depended upon a NetVM, ProxyVM, or TemplateVM that is not present in (i.e., "missing from") the current system, checking this box will ignore the fact that they are missing and restore the VMs anyway and set them to use the default NetVM and system default template.
   2.  **ignore username mismatch**: This option applies only to the restoration of dom0's home directory.
   If your backup was created on a Qubes system which had a different dom0 username than the dom0 username of the current system, then checking this box will ignore the mismatch between the two usernames and proceed to restore the home directory anyway.
   3.  **Verify backup integrity, do not restore the data**: This will scan the backup file for corrupted data. 
   However, it does not currently detect if it is missing data as long as it is a correctly structured, non-corrupted backup file. See [issue #3498](https://github.com/QubesOS/qubes-issues/issues/3498) for more details.

4. If your backup is encrypted, you must check the **Encrypted backup** box. 
If a passphrase was supplied during the creation of your backup (regardless of whether it is encrypted), then you must supply it here.

   **Note:** The passphrase which was supplied when the backup was created was used for **both** encryption/decryption and integrity verification. 
   If the backup was not encrypted, the supplied passphrase is used only for integrity verification.

   **Note:** A VM cannot be restored from a backup if a VM with the same name already exists on the current system. 
   You must first remove or change the name of any VM with the same name in order to restore such a VM.

5. You will now see the summary of VMs to be restored. 
If there are any issues preventing the restore, they will be listed here and the **Next** button grayed out.

6. When you are ready, click **Next**. 
Qubes will proceed to restore from your backup.
Once the progress bar has completed, you may click **Finish**.


Emergency Backup Recovery without Qubes
---------------------------------------

The Qubes backup system has been designed with emergency disaster recovery in mind. 
No special Qubes-specific tools are required to access data backed up by Qubes.
In the event a Qubes system is unavailable, you can access your data on any GNU/Linux system with the following procedure.

Refer to the following for emergency restore of a backup created on:

 * [Qubes R4 or newer](/doc/backup-emergency-restore-v4/)
 * [Qubes R3](/doc/backup-emergency-restore-v3/)
 * [Qubes R2 or older](/doc/backup-emergency-restore-v2/)


Migrating Between Two Physical Machines
---------------------------------------

In order to migrate your Qubes system from one physical machine to another, simply follow the backup procedure on the old machine, [install Qubes](/downloads/) on the new machine, and follow the restoration procedure on the new machine.
All of your settings and data will be preserved!

Choosing a Backup Passphrase
----------------------------

Here are some things to consider when selecting a passphrase for your backups:

 * If you plan to store the backup for a long time or on third-party servers, you should make sure to use a very long, high-entropy passphrase. 
 (Depending on the decryption passphrase you use for your system drive, this may necessitate selecting a stronger passphrase. 
 If your system drive decryption passphrase is already sufficiently strong, it may not.)
 * An adversary who has access to your backups may try to substitute one backup for another. 
 For example, when you attempt to retrieve a recent backup, the adversary may instead give you a very old backup containing a compromised VM. 
 If you're concerned about this type of attack, you may wish to use a different passphrase for each backup, e.g., by appending a number or date to the passphrase.
 * If you're forced to enter your system drive decryption passphrase in plain view of others (where it can be shoulder-surfed), then you may want to use a different passphrase for your backups (even if your system drive decryption passphrase is already maximally strong).
 On the other hand, if you're careful to avoid shoulder-surfing and/or have a passphrase that's difficult to detect via shoulder-surfing, then this may not be a problem for you.

Notes
-----

 * The Qubes R3.2 and earlier backup system relies on `openssl enc`, which is known to use a very weak key derivation scheme.
 The Qubes backup system also uses the same passphrase for authentication and for encryption, which is problematic from a security perspective.
 Users are advised to use a very high entropy passphrase for Qubes backups.
 For a full discussion, see [this ticket](https://github.com/QubesOS/qubes-issues/issues/971) and [this thread](https://groups.google.com/d/msg/qubes-devel/CZ7WRwLXcnk/u_rZPoVxL5IJ).
 * For the technical details of the backup system, please refer to [this thread](https://groups.google.com/d/topic/qubes-devel/TQr_QcXIVww/discussion).
 * If working with symlinks, note the issues described in [this thread](https://groups.google.com/d/topic/qubes-users/EITd1kBHD30/discussion).
