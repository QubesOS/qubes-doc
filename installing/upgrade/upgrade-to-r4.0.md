---
layout: doc
title: Upgrading to R4.0
permalink: /doc/upgrade-to-r4.0/
redirect_from:
- /en/doc/upgrade-to-r4.0/
- /doc/UpgradeToR4.0/
- /doc/UpgradeToR4.0rc1/
---

Upgrading Qubes R3.2 to R4.0
============================

**Before attempting either an in-place upgrade or a clean installation, we strongly recommend that users [back up their systems](/doc/backup-restore/).**

Current Qubes R3.2 systems cannot be upgraded in-place to R4.0.
A full backup, clean 4.0 install, and restore is required.
This can be done by following the procedure below.


Preparation
-----------

1. Go to [downloads](/downloads/) and prepare a USB drive or DVD with the R4.0 installer.

2. If this is your only computer, and you do not have a R3.2 installer, you should also create a separate R3.2 USB drive or DVD installer at this time.


Backup R3.2
-----------

1. Attach the backup drive you will be using.
   These steps assume it is a USB drive.

2. Shutdown all non-essential VMs.
   Typically, `sys-usb` will be the only VM you need to leave running.

3. Follow the **Creating a Backup** section in the [Backup, Restoration, and Migration](/doc/backup-restore/) guide to back up **all VMs** except sys-usb. 

6. Verify the integrity of your backup by following the **Restoring from a Backup** section in the [Backup, Restoration, and Migration](/doc/backup-restore/) guide and:

   * If you're using Qubes Manager, check the box under "Restore options" that says, "Verify backup integrity, do not restore the data."
   * If you're using `qvm-backup-restore` from the command-line, use the `--verify-only` option.

7. If your backup verifies successfully, proceed to the next section.
   If it does not, **stop**.
   Go back and repeat the backup steps, review the documentation or search the qubes-users mailing list, or ask for assistance on the [qubes-users mailing list](/mailing-lists/#qubes-users) or IRC.


Install R4.0
------------

This section provides general guidance on installing R4.0 as part of migrating from R3.2.
For further details, please see the [installation guide](/doc/installation-guide/).

1. Shut down R3.2 and boot the R4.0 installer.

2. Follow the installation prompts until you get to the drive selection screen.
   Choose **I want to make additional space available**.
   Select the box at the top of the list in order to select all partitions.
   **This will erase the entire drive**, so do this only if Qubes is the only OS installed on your computer.
   If you did not successfully verify your backup in the previous section, cancel the installation, and go back to do that now. 

3. Complete the R4.0 installation.
   Ask for assistance on the [qubes-users mailing list](/mailing-lists/#qubes-users) if you run into trouble.

4. If you are unable to successfully install R4.0 on your system, all is not lost.
   Use the R3.2 installer to reinstall R3.2, then restore from your backup.


Restore from your backup
------------------------

1. Welcome to Qubes R4.0!
   The first thing you might notice is that **Qubes Manager** is not started by default.
   We won't need it for the next step, but we will be starting it later.

2. Since patches may have been released since your installation image was created, update Qubes R4.0 by going to the dom0 command line (**Qubes menu -> Terminal Emulator**) then running:

       sudo qubes-dom0-update

3. Reboot dom0.

4. Go to **Qubes menu -> System Tools -> Qubes Manager** to start it.

5. Follow the **Restoring from a Backup** section in the [Backup, Restoration, and Migration](/doc/backup-restore/) guide.
   It is cleanest to restore only the [AppVMs](/doc/glossary/#appvm) and [StandaloneVMs](/doc/glossary/#standalonevm) from R3.2, so it is recommended not to select any **sys-** or templates to restore unless you've heavily customized them.
   If the restore tool complains about missing templates, you can select the option to restore the AppVMs anyways, then change them after restore to use one of the default R4.0 templates.


Upgrade all Template and Standalone VM(s)
-----------------------------------------

By default, in Qubes R4.0, there are few [TemplateVMs](/doc/templates/) and no [StandaloneVMs](/doc/glossary/#standalonevm).
However, users are free to create StandaloneVMs.
More information on using multiple TemplateVMs, as well as StandaloneVMs, can be found [here](/doc/software-update-vm/).
We strongly recommend that you upgrade **all** TemplateVMs and StandaloneVMs.
Please consult the guides below for specific instructions:

 * [Upgrading Fedora TemplateVMs](/doc/templates/fedora/#upgrading)
 * [Upgrading Debian TemplateVMs](/doc/templates/debian/#upgrading)
 * [Updating Whonix TemplateVMs](/doc/whonix/update/)

