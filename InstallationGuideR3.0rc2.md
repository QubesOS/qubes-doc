---
layout: doc
title: Installation Guide for Qubes 3.0 rc2
permalink: /doc/InstallationGuideR3.0rc2/
---

Installation Guide for Qubes Release 3.0 rc2
============================================

1.  [Hardware Requirements](#hardware-requirements)
2.  [Download installer ISO](#download-installer-iso)
3.  [Burning the ISO onto a DVD or USB stick](#burning-the-iso-onto-a-dvd-or-usb-stick)
4.  [Upgrading](#upgrading)
5.  [Troubleshooting problems with the installer](#troubleshooting-problems-with-the-installer)
6.  [Known Issues](#known-issues)
7.  [Getting Help](#getting-help)

Hardware Requirements
---------------------

Please see the [Hardware Compatibility List](/hcl/) page for more information on required and recommended hardware.

Note: We don't recommend installing Qubes in a virtual machine! It will likely not work. Don't send emails asking about it. However, you can install it on an external USB hard drive and run from it, at least for testing (normally such disks are *orders* of magnitude slower than even the slowest internal hard drives).

Download installer ISO
----------------------

See [this page](/doc/QubesDownloads/) for ISO downloads. Remember, we have absolutely no control over those servers, and so you should be assuming that they might be compromised, or just be serving a compromised ISOs because their operators decided so, for whatever reason. Always verify the digital signature on the downloaded ISO. See this [page](/doc/VerifyingSignatures/) for more info about how to download and verify our GPG keys, and then verify the downloaded ISO:

    gpg -v Qubes-R3.0-rc2-x86_64-DVD.iso.asc

Burning the ISO onto a DVD or USB stick
---------------------------------------

Once you verify this is an authentic ISO, you should burn it on a DVD.

If you prefer to use USB as a source for installation, then you just need to copy the ISO onto the USB device, e.g. using dd:

    dd if=Qubes-R3.0-rc2-x86_64-DVD.iso of=/dev/sdX

On windows you can use [this](http://www.chrysocome.net/dd) tool. Example command would be (as Administrator):

    dd if=Qubes-R3.0-rc2-x86_64-DVD.iso of=\\?\Device\Harddisk1\Partition0 bs=1M --size --progress

**Be sure to use a correct device as the target in the dd command above (instead of sdX or Harddisk1)**

Before proceeding with the installation, you are encouraged to first read all the information on this page, especially the *Known Issues* paragraph.

Then, when finally ready, boot your system from the installer DVD and follow the instructions on screen. The installer is very simple and asks very few questions -- it's actually easier to install Qubes right now than most other Linux distributions!

The installer loads Xen right at the beginning, so chances are high that if you can see the installer's graphical screen, Qubes will work on your system :)

Upgrading from R3.0rc1
-----------------------

If you are using Qubes R3.0rc1, just install system updates, there is no special steps required.

Upgrading
---------

If you are using Qubes R2, follow instructions below.

The easiest and safest way to upgrade to Qubes R3.0rc2 is to install it from scratch and use [qubes backup and restore tools](/doc/BackupRestore/) for migrating of all of the user VMs.

Users of Qubes R2 can upgrade using [experimental procedure](/doc/UpgradeToR3.0rc1/) (the same as for R3.0rc1).

Troubleshooting problems with the installer
-------------------------------------------

If the installer fails for some reason, typically because of the graphics card not being correctly supported, it is possible to try booting the installer with a different kernel -- to do that, choose Troubleshooting menu in the Installer Welcome screen, and later choose an option to proceed with one of the kernels provided.

The installer ships with 4 different kernels (3.12, 3.11, 3.9 and 3.7) and all those kernel will be installed (regardless of which is selected to run the installer) so it is later always possible to boot the Qubes OS using any of those kernels.

Known Issues
------------

- UEFI is not supported, you need to enable "legacy boot" in BIOS before installing Qubes OS

- Some icons in the Qubes Manager application might not be drawn correctly when using the Xfce4 environment in Dom0. If this bothers you, please use the KDE environment instead.

- If your GPU is not correctly supported by the Dom0 kernel (e.g. the 3D desktop effects do not run smoothly) then you might experience "heaviness" with Windows 7-based AppVMs. In that case, please solve the problem with your GPU support in Dom0 in the first place (by using a different kernel), or install Qubes OS on a different system.

- For other known issues take a look at [our tickets](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Release+3.0%22+label%3Abug)

It is advised to install updates just after system installation to apply bug fixes for (some of) the above problems.

Getting Help
------------

-   **User manuals are [here](/doc/UserDoc/).** (Strongly recommended!)

-   Developers documentation (normally not needed by users) is [here](/doc/SystemDoc/)

-   If you don't find answer in the sources given above, write to the *qubes-users* mailing list (you don't need to be subscribed to the list, just send email to the address given below):
    -   [https://groups.google.com/group/qubes-users](https://groups.google.com/group/qubes-users)
    -   `qubes-users@googlegroups.com`

-   Please do not write email to individual developers (Marek, Joanna, etc) asking questions about installation or other problems. Please send all such questions to the mailing list.
