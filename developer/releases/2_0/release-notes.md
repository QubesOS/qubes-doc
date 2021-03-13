---
layout: doc
title: Qubes R2.0 Release Notes
permalink: /doc/releases/2.0/release-notes/
redirect_from:
- /en/doc/releases/2.0/release-notes/
---

Qubes R2.0 Release Notes
========================

Detailed release notes in [this blog post](https://blog.invisiblethings.org/2014/09/26/announcing-qubes-os-release-2.html)

New features since 1.0
----------------------

* Support for generic fully virtualized VMs (without qemu in the TCB!)
* Support for Windows-based AppVMs integration (clipboard, file exchange, qrexec, pv drivers)
* Secure audio input to select AppVMs (Hello Skype users!)
* Clipboard is now also controlled by central policies, unified with other qrexec policies.
* Out of the box TorVM support
* Experimental support for PVUSB
* Updated Xorg packages in Dom0 to support new GPUs
* DisposableVM customization support
* Introduced Xfce 4.10 environment for Dom0 as an alternative to KDE
* Advanced infrastructure for system backups
* Ability to autostart selected VM at system startup
* Support for dynamic screen resolution change
* Dom0 distribution upgraded to Fedora 20

Known issues
------------

-   On some graphics cards the Xfce4 Window Manager (one of the two supported Dom0 Windows Managers in Qubes R2, the other being KDE) might behave "strangely", e.g. decorations might not be drawn sometimes. Also the accompanying lightdm login manager might incorrectly display the wallpaper. If you're facing those problems, it's advisable to use the KDE Window Manager and kdm instead of Xfce4 and lightdm (this is default if one chooses the KDE only installation option in the installer).

-   Some icons in the Qubes Manager application might not be drawn correctly when using the Xfce4 environment in Dom0. If this bothers you, please use the KDE environment instead.

-   If your GPU is not correctly supported by the Dom0 kernel (e.g. the 3D desktop effects do not run smoothly) then you might experience "heaviness" with Windows 7-based AppVMs. In that case, please solve the problem with your GPU support in Dom0 in the first place (by using a different kernel), or install Qubes OS on a different system.

-   Under some circumstances, Qubes backup can create broken backup, without any visible message (\#902). It is advisable to verify a backup to spot the problem. If you encounter this problem, backup VM directory manually.

-   System shutdown sometimes is very slow (\#903). To mitigate the problem, shutdown all the VMs first.

-   For other known issues take a look at [our trac tickets](https://wiki.qubes-os.org/query?status=accepted&status=assigned&status=new&status=reopened&type=defect&milestone=Release+2.1+(post+R2)&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&order=priority)

It is advised to install updates just after system installation to apply bug fixes for (some of) the above problems.

Downloads
---------

See [Qubes Downloads](/doc/QubesDownloads/).

Installation instructions
-------------------------

See [Installation Guide](/doc/installation-guide/).

Upgrading
---------

### From Qubes R2 rc1

Upgrading from Qubes R2 rc1 should be a simple matter of installing updates for [dom0](/doc/software-update-dom0/) and [VMs](/doc/software-update-vm/).

### From Qubes R2 beta 3 and older

The easiest and safest way to upgrade to Qubes R2 (especially from older releases) is to install it from scratch and use [qubes backup and restore tools](/doc/backup-restore/) for migrating of all of the user VMs.

Users of R2 beta 3 can upgrade using procedure that has been described [here](/doc/upgrade-to-r2/).

Note: if the user has custom Template VMs (i.e. other than the default template, e.g. created from it by cloning), or Standalone VMs, then the user should perform manual upgrade from R2B3 to R2rc1, as described under the link given above.

### Migrating between beta releases

#### From Qubes R1 to R2 beta1

If you're already running Qubes Release 1, you don't need to reinstall, it's just enough to update the packages in your Dom0 and the template VM(s). This procedure is described [here?](/doc/upgrade-to-r2/).

#### From Qubes R1 or R2 Beta 1 to R2 beta2

Because of the distribution change in R2B2 (from fc13 to fc18) it's preferred that users reinstall Qubes R2B2 from scratch, and use [qubes backup and restore tools](/doc/backup-restore/) for migrating of all of the user VMs.

Advanced users (and advanced users only) can also try a manual upgrade procedure that has been described [here](/doc/upgrade-to-r2b2/). It's advisable to backup your VMs before proceeding anyway!

#### Upgrading from Qubes R1 or R2 Beta 2 to R2 beta 3

The easiest and safest way to upgrade to Qubes R2B3 is to install it from scratch and use [qubes backup and restore tools](/doc/backup-restore/) for migrating of all of the user VMs.

Users can also try a manual upgrade procedure that has been described [here](/doc/upgrade-to-r2b3/).

Note: if the user has custom Template VMs (i.e. other than the default template, e.g. created from it by cloning), or Standalone VMs, then the user should perform manual upgrade from R2B2 to R2B3, as described under the link given above.
