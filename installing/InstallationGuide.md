---
layout: doc
title: Installation Guide
permalink: /doc/InstallationGuide/
redirect_from:
- /wiki/InstallationGuide/
- /doc/InstallationGuideR1/
- /doc/InstallationGuideR2B1/
- /doc/InstallationGuideR2B2/
- /doc/InstallationGuideR2B3/
- /doc/InstallationGuideR2rc1/
- /doc/InstallationGuideR2rc2/
- /doc/InstallationGuideR3.0rc1/
- /doc/InstallationGuideR3.0rc2/
---

Installation Guide
========================================

1.  [Hardware Requirements](#hardware-requirements)
2.  [Download installer ISO](#download-installer-iso)
3.  [Burning the ISO onto a DVD or USB stick](#burning-the-iso-onto-a-dvd-or-usb-stick)
4.  [Upgrading](#upgrading)
5.  [Troubleshooting problems with the installer](#troubleshooting-problems-with-the-installer)
6.  [Getting Help](#getting-help)

Hardware Requirements
---------------------

Please see the [Hardware Compatibility List](/hcl/) page for more information on required and recommended hardware.

Note: We don't recommend installing Qubes in a virtual machine! It will likely not work. Don't send emails asking about it. However, you can install it on an external USB hard drive and run from it, at least for testing (normally such disks are *orders* of magnitude slower than even the slowest internal hard drives).

Download installer ISO
----------------------

See [this page](/doc/QubesDownloads/) for ISO downloads. Remember, we have absolutely no control over those servers, and so you should be assuming that they might be compromised, or just be serving a compromised ISOs because their operators decided so, for whatever reason. Always verify the digital signature on the downloaded ISO. See this [page](/doc/VerifyingSignatures/) for more info about how to download and verify our GPG keys, and then verify the downloaded ISO:

    gpg -v Qubes-R2-x86_64-DVD.iso.asc

Adjust filename to the version you're installing.

Burning the ISO onto a DVD or USB stick
---------------------------------------

Once you verify this is an authentic ISO, you should burn it on a DVD.

If you prefer to use USB as a source for installation, then you just need to copy the ISO onto the USB device, e.g. using dd:

    dd if=Qubes-R2-x86_64-DVD.iso of=/dev/sdX

Adjust filename to the version you're installing. **Be sure to use a correct device as the target in the dd command above (instead of sdX)'''**

On windows you can use [Rufus](http://rufus.akeo.ie/) tool. Be sure to select "DD image" mode (you need to do that **after** selecting Qubes iso image):

<img src="/attachment/wiki/InstallationGuide/rufus-main-boxed.png" height="350">

Before proceeding with the installation, you are encouraged to first read all the information on this page, especially the *Known Issues* paragraph.

Then, when finally ready, boot your system from the installer DVD and follow the instructions on screen. The installer is very simple and asks very few questions -- it's actually easier to install Qubes right now than most other Linux distributions!

The installer loads Xen right at the beginning, so chances are high that if you can see the installer's graphical screen, Qubes will work on your system :)

Upgrading
---------

See [release notes](/doc/releases/) of appropriate version.



Getting Help
------------

-   **User manuals are [here](/doc/UserDoc/).** (Strongly recommended!)

-   Developers documentation (normally not needed by users) is [here](/doc/SystemDoc/)

-   If you don't find answer in the sources given above, write to the *qubes-users* mailing list (you don't need to be subscribed to the list, just send email to the address given below):
    -   [https://groups.google.com/group/qubes-users](https://groups.google.com/group/qubes-users)
    -   `qubes-users@googlegroups.com`

-   Please do not write email to individual developers (Marek, Joanna, etc) asking questions about installation or other problems. Please send all such questions to the mailing list.
