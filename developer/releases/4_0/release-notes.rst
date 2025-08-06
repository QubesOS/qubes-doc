---
lang: en
layout: doc
permalink: /doc/releases/4.0/release-notes/
ref: 23
title: Qubes R4.0 release notes
---

New features since 3.2
----------------------

* Core management scripts rewrite with better structure and extensibility, [current API documentation](https://dev.qubes-os.org/projects/core-admin/en/latest/) and the documentation API index as a [webarchive](https://web.archive.org/web/20230128102821/https://dev.qubes-os.org/projects/qubes-core-admin/en/latest/)
* [Admin API](/news/2017/06/27/qubes-admin-api/) allowing strictly controlled managing from non-dom0
* All `qvm-*` command-line tools rewritten, some options have changed
* Renaming VM directly is prohibited, there is GUI to clone under new name and remove old VM
* Use [PVH](https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-037-2018.txt) and [HVM](https://github.com/QubesOS/qubes-issues/issues/2185) by default to [mitigate Meltdown & Spectre](https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-037-2018.txt) and lower the [attack surface on Xen](https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-024-2016.txt)
* Create USB VM by default
* [Multiple DisposableVMs templates support](https://github.com/QubesOS/qubes-issues/issues/2253)
* New [backup format](/doc/backup-emergency-restore-v4/) using scrypt key-derivation function
* Non-encrypted backups no longer supported
* [split VM packages](https://github.com/QubesOS/qubes-issues/issues/2771), for better support minimal, specialized templates
* [Qubes Manager decomposition](https://github.com/QubesOS/qubes-issues/issues/2132) - domains and devices widgets instead of full Qubes Manager; devices widget support also USB
* [More flexible firewall interface](/doc/vm-interface/) for ease unikernel integration
* Template VMs do not have network interface by default, [qrexec-based updates proxy](https://github.com/QubesOS/qubes-issues/issues/1854) is used instead
* More flexible IP addressing for VMs - [custom IP](https://github.com/QubesOS/qubes-issues/issues/1477), [hidden from the IP](https://github.com/QubesOS/qubes-issues/issues/1143)
* More flexible Qubes RPC policy - [related ticket](https://github.com/QubesOS/qubes-issues/issues/865), [documentation](/doc/qrexec/#specifying-vms-tags-types-targets-etc)
* [New Qubes RPC confirmation window](https://github.com/QubesOS/qubes-issues/issues/910), including option to specify destination VM
* [New storage subsystem design](https://github.com/QubesOS/qubes-issues/issues/1842)
* Dom0 update to Fedora 25 for better hardware support
* Kernel 4.9.x

You can get detailed description in [completed github issues](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+4.0%22+label%3Arelease-notes+is%3Aclosed)

Security Notes
--------------

* PV VMs migrated from 3.2 to 4.0-rc4 or later are automatically set to PVH mode in order to protect against Meltdown (see [QSB #37](https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-037-2018.txt)).
  However, PV VMs migrated from any earlier 4.0 release candidate (RC1, RC2, or RC3) are not automatically set to PVH mode.
  These must be set manually.

* The following steps may need to be applied in dom0 and Fedora 26 TemplateVMs in order to receive updates (see [#3737](https://github.com/QubesOS/qubes-issues/issues/3737)).

  Steps for dom0 updates:

  1. Open the Qubes Menu by clicking on the "Q" icon in the top-left corner of the screen.
  2. Select `Terminal Emulator`.
  3. In the window that opens, enter this command:

     ```
     sudo nano /etc/yum.repos.d/qubes-dom0.repo
     ```

  4. This opens the nano text editor. Change all four instances of `http` to `https`.
  5. Press `CTRL+X`, then `Y`, then `ENTER` to save changes and exit.
  6. Check for updates normally.

  Steps for Fedora 26 TemplateVM updates:

  1. Open the Qubes Menu by clicking on the "Q" icon in the top-left corner of the screen.
  2. Select `Template: fedora-26`, then `fedora-26: Terminal`.
  3. In the window that opens, enter the command for your version:

     ```
     [Qubes 3.2] sudo gedit /etc/yum.repos.d/qubes-r3.repo
     [Qubes 4.0] sudo gedit /etc/yum.repos.d/qubes-r4.repo
     ```

  4. This opens the gedit text editor in a window. Change all four instances of `http` to `https`.
  5. Click the "Save" button in the top-right corner of the window.
  6. Close the window.
  7. Check for updates normally.
  8. Shut down the TemplateVM.

Known issues
------------

* Locale using coma as decimal separator [crashes qubesd](https://github.com/QubesOS/qubes-issues/issues/3753). Either install with different locale (English (United States) for example), or manually apply fix explained in that issue.

* In the middle of installation, [keyboard layout reset to US](https://github.com/QubesOS/qubes-issues/issues/3352). Be careful what is the current layout while setting default user password (see upper right screen corner).

* On some laptops (for example Librem 15v2), touchpad do not work directly after installation. Reboot the system to fix the issue.

* List of USB devices may contain device identifiers instead of name

* With R4.0.1, which ships kernel-4.19, you may never reach the anaconda startup and be block on an idle black screen with blinking cursor. You can try to add `plymouth.ignore-serial-consoles` in the grub installer boot menu right after `quiet rhgb`. With legacy mode, you can do it directly when booting the DVD or USB key. In UEFI mode, follow the same procedure described for [disabling](/doc/uefi-troubleshooting/#installation-freezes-before-displaying-installer) `nouveau` module (related [solved issue](https://github.com/QubesOS/qubes-issues/issues/3849) in further version of Qubes).

* For other known issues take a look at [our tickets](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Release+4.0%22+label%3Abug)

It is advised to install updates just after system installation to apply bug fixes for (some of) the above problems.

Downloads
---------

See [Qubes Downloads](/downloads/).

Installation instructions
-------------------------

See [Installation Guide](/doc/installation-guide/).

Upgrading
---------

There is no in-place upgrade path from earlier Qubes versions. The only
supported option to upgrade to Qubes R4.0 is to install it from scratch and use
[qubes backup and restore tools](/doc/backup-restore/) for migrating of all of the user VMs.
We also provide [detailed instruction](/doc/upgrade-to-r4.0/) for this procedure.
