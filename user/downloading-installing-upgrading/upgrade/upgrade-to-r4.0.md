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
   Go back and repeat the backup steps, review the documentation or search the qubes-users mailing list, or ask for assistance on the [qubes-users mailing list](/support/#qubes-users) or IRC.


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
   Ask for assistance on the [qubes-users mailing list](/support/#qubes-users) if you run into trouble.

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
   We recommend that you restore only your [TemplateBasedVMs](/doc/glossary/#templatebasedvm) and [StandaloneVMs](/doc/glossary/#standalonevm) from R3.2.
   Using [TemplateVMs](/doc/templates/) and [SystemVMs](/doc/glossary/#systemvm) from R3.2 is not fully supported (see [#3514](https://github.com/QubesOS/qubes-issues/issues/3514)).
   Instead, we recommend using the TemplateVMs that were created specifically for R4.0, which you can [customize](/doc/software-update-vm/) according to your needs.
   For the TemplateVM OS versions supported in R4.0, see [Supported Versions](/doc/supported-versions/#templatevms).
   If the restore tool complains about missing templates, you can select the option to restore the AppVMs anyway, then change them afterward to use one of the default R4.0 templates.

Note about additional disp-* qubes created during restore
---------------------------------------------------------

One of differences between R3.2 and R4.0 is the handling of DisposableVMs.
In R3.2, a DisposableVM inherited its network settings (NetVM and firewall rules) from the calling qube.
In R4.0, this is no longer the case.
Instead, in R4.0 it's possible to create multiple DisposableVM Templates and choose which one should be used by each qube.
It's even possible to use different DisposableVM Templates for different operations from the same qube.
This allows much more flexibility, since it allows you to differentiate not only network settings, but all of a qube's properties (including its template, memory settings, etc.).

Restoring a backup from R3.2 preserves the old behavior by creating separate DisposableVM Template for each network-providing qube (and also `disp-no-netvm` for network-isolated qubes).
Then, each restored qube is configured to use the appropriate DisposableVM Template according to its `netvm` or `dispvm_netvm` property from R3.2.
This way, DisposableVMs started on R4.0 by qubes restored from a R3.2 backup have the same NetVM settings as they had on R3.2.

If you find this behavior undesirable and want to configure it differently, you can remove those `disp-*` DisposableVM Templates.
But, to do so, you must first make sure they are not set as the value for the `default_dispvm` property on any other qube.
Both Qubes Manager and the `qvm-remove` tool will show you where a DisposableVM Template is being used, so you can go there and change the setting.

Upgrade all Template and Standalone VM(s)
-----------------------------------------

We strongly recommend that you update **all** TemplateVMs and StandaloneVMs before use so that you have the latest security patches from upstream distributions.
In addition, if the default templates have reached EOL (end-of-life) by the time you install R4.0, we strongly recommend that you upgrade them before use.
Please see [Supported Versions](/doc/supported-versions/) for information on supported OS versions and consult the guides below for specific upgrade instructions:

 * [Upgrading Fedora TemplateVMs](/doc/templates/fedora/#upgrading)
 * [Upgrading Debian TemplateVMs](/doc/templates/debian/#upgrading)
 * [Updating Whonix TemplateVMs](https://www.whonix.org/wiki/Qubes/Update)

