---
layout: doc
title: Qubes R3.0 release notes
permalink: /en/doc/releases/3.0/release-notes/
redirect_from: /doc/releases/3.0/release-notes/
---

Qubes R3.0 release notes
========================

*this page is a draft for yet unreleased version*

New features since 2.0
----------------------

* Xen 4.4
* Qrexec 3
* Debian templates
* Whonix templates
* Build system improvements

Known issues
------------

* Windows Tools: `qvm-block` does not work

* UEFI is not supported, you need to enable "legacy boot" in BIOS before installing Qubes OS

* Some icons in the Qubes Manager application might not be drawn correctly when using the Xfce4 environment in Dom0. If this bothers you, please use the KDE environment instead.

* If your GPU is not correctly supported by the Dom0 kernel (e.g. the 3D desktop effects do not run smoothly) then you might experience "heaviness" with Windows 7-based AppVMs. In that case, please solve the problem with your GPU support in Dom0 in the first place (by using a different kernel), or install Qubes OS on a different system.

* For other known issues take a look at [our tickets](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Release+3%22+label%3Abug)

It is advised to install updates just after system installation to apply bug fixes for (some of) the above problems.

Downloads
---------

See [Qubes Downloads](/doc/QubesDownloads/).

Installation instructions
-------------------------

See [Installation Guide](/doc/InstallationGuide/).

Upgrading
---------

### From from R3.0rc1

If you are using Qubes R3.0rc1, just install system updates, there is no special steps required.

### From R2.0 or earlier

The easiest and safest way to upgrade to Qubes R3.0 is to install it from scratch and use [qubes backup and restore tools](/doc/BackupRestore/) for migrating of all of the user VMs.

Users of Qubes R2 can upgrade using [experimental procedure](/doc/UpgradeToR3.0/).

