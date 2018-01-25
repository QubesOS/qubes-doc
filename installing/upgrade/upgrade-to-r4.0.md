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
======================================

**Before attempting either an in-place upgrade or a clean installation, we
strongly recommend that users [back up their systems](/doc/backup-restore/).**

Current Qubes R3.2 systems cannot be upgraded in place to R4.0. A full backup,
re-install, and restore is required. This can be done by following the procedure below.

Preparation
--------------

1.  Go to [downloads](/downloads/) and prepare a USB drive or DVD with the R4.0 installer.

2.  If this is your only computer and you have misplaced your R3.2 installer, you should also create a separate R3.2 USB drive or DVD installer at this time.

Backup R3.2
--------------

1.  Attach the backup drive you will be using. These steps assume it is a USB drive.

2.  Create an AppVM to be used for testing (in **Qubes VM Manager**, select the **VM -> Create New VM** menu item). It will be deleted later so just accept the defaults.

3.  Shutdown all non-essential VMs. Typically, `sys-usb` will be the only VM you need to leave running.

4.  Follow the **Creating a Backup** section in the [Backup, Restoration, and Migration](/doc/backup-restore) guide to back up **all VMs** except sys-usb. 

5.  Delete the VM created in step #2 (right-click it from the list of VMs, choose **Delete VM**, and enter the name).

6.  Follow the **Restoring from a Backup** section in the [Backup, Restoration, and Migration](/doc/backup-restore) guide **for the test VM only**.

7.  If your test VM restored correctly and is listed in **Qubes VM Manager**, great! Proceed to the next section. If it did not, **STOP**! Go back and repeat the backup steps, review the documentation or search the qubes-users mailing list, or ask for assistance from the qubes-users mailing list or IRC.

Install R4.0
--------------

1.  Shutdown R3.2 and boot the R4.0 installer.

2.  Follow the installation prompts, except when you get to the drive selection screen choose **I want to make additional space available**. Put a checkmark on the top of the list to select all partitions. **THIS WILL ERASE THE ENTIRE DRIVE**, so only do this if Qubes is the only OS installed on your computer. If you did not test restoring a VM in the previous section, cancel the install, go back and do that now. 

3.  Complete the R4.0 installation. Consult the same resources if you run into trouble.

4.  If you are unable to successfully install R4.0 on your system, all is not lost. Use the R3.2 installer to go back to R3.2, then proceed with the next section.

Restore
--------------

1.  Welcome to Qubes R4.0! The first thing you might notice is **Qubes Manager** is not started by default. We won't need it for the next step, but will be starting it later.

2.  Since patches may have been added since the installation image was created, update Qubes R4.0 by going to the dom0 command line (**Qubes menu -> Terminal Emulator**) then:

        sudo qubes-dom0-update

3.  Reboot.

4.  Go to **Qubes menu -> System Tools -> Qubes Manager** to start it.

5.  Follow the **Restoring from a Backup** section in the [Backup, Restoration, and Migration](/doc/backup-restore) guide. It is cleanest to restore only the App and Standalone VMs from R3.2, so don't select any **sys-** or templates to restore unless you've heavily customized them. If it complains about missing templates, check the box to allow you to restore the AppVMs anyways, then change them after restore to use one of the default R4.0 templates.

Upgrade all Template and Standalone VM(s)
-----------------------------------------

By default, in Qubes R4.0, there are few TemplateVMs and no StandaloneVMs.
However, users are free to create StandaloneVMs. More information on using
multiple TemplateVMs, as well as StandaloneVMs, can be found
[here](/doc/software-update-vm/). The steps described in this section should be
repeated in **all** the user's Template and Standalone VMs.

### Upgrade Fedora templates: ###

TBD

### Upgrade Debian (and Whonix) templates: ###

TBD

