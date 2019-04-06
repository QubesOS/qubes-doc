---
layout: doc
title: Installation Guide
permalink: /doc/installation-guide/
redirect_from:
- /en/doc/installation-guide/
- /doc/InstallationGuide/
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
==================


Qubes 4.0.1 Warning
-------------------

Immediately after installing Qubes 4.0.1, please upgrade all of your Debian and Whonix TemplateVMs by executing the following commands in a dom0 terminal, as applicable for the templates you chose to install:

    $ sudo qubes-dom0-update --action=upgrade qubes-template-debian-9
    $ sudo qubes-dom0-update --enablerepo=qubes-templates-community --action=upgrade qubes-template-whonix-gw-14
    $ sudo qubes-dom0-update --enablerepo=qubes-templates-community --action=upgrade qubes-template-whonix-ws-14

These upgrades are required in order to be protected from the APT update mechanism vulnerability that was announced and patched in [QSB #46], which was after the release of Qubes 4.0.1.
This method is simpler than the method recommended in [QSB #46], but it is just as safe and effective so long as it is performed immediately after installing Qubes OS.


Hardware Requirements
---------------------

Please see the [system requirements] and [Hardware Compatibility List] pages for
more information on required and recommended hardware.

**Note:** We don't recommend installing Qubes in a virtual machine! It will
likely not work. Please don't send emails asking about it. You can, however,
install it on an external USB hard drive (at least 32 GB) and run from it,
at least for testing. Bear in mind, however, that such disks are typically
*orders* of magnitude slower than even the slowest internal hard drives.


Downloading the ISO
-------------------

See the [downloads] page for ISO downloads. Remember, we have absolutely
no control over those servers, so you should be assuming that they might be
compromised, or just be serving compromised ISOs because their operators decided
so, for whatever reason. Always verify the digital signature on the downloaded
ISO. Make sure to read our guide on [verifying signatures] for more info about
how to download and verify our PGP keys and verify the downloaded ISO.


Copying the ISO onto the installation medium
--------------------------------------------

Once you verify this is an authentic ISO, you should copy it onto the
installation medium of your choice, such as a DVD or a USB drive. (Please note
that there are important [security considerations] to keep in mind when choosing
an installation medium.)

If you prefer to use a USB drive, then you just need to copy the ISO onto the
USB device, e.g. using `dd`:

    dd if=Qubes-R3-x86_64.iso of=/dev/sdX bs=1048576 && sync

Change `Qubes-R3-x86_64.iso` to the filename of the version you're installing,
and change `/dev/sdX` to the correct target device (e.g., `/dev/sdc`).
**Warning:** Choosing the wrong device could result in data loss. Make sure to
write to the entire device (e.g., `/dev/sdc`) rather than just a single
partition (e.g., `/dev/sdc1`).

On Windows, you can use the [Rufus] tool. Be sure to select "DD image" mode (you
need to do that **after** selecting the Qubes ISO):

**Warning:** If you do that on Windows 10, you can only install Qubes without 
MediaTest, which isn't recommended. 

<img src="/attachment/wiki/InstallationGuide/rufus-main-boxed.png" height="350">

Before proceeding with the installation, you are encouraged to first read all
the information on this page. When you're ready, boot your system from the
installation source and follow the on-screen instructions. The installer is very
simple and asks very few questions. (It's actually easier to install Qubes right
now than most other Linux distributions!)

The installer loads Xen right at the beginning, so chances are high that if you
can see the installer's graphical screen and you pass the compatibility check that
runs immediately after that, Qubes will work on your system. :)


Installing to a USB drive
-------------------------

Installing an operating system onto a USB drive can be a convenient and secure
method of ensuring that your data is protected. Be advised that a minimum
storage of 32 GB is required on the USB drive. This installation process may
take longer than an installation on a standard hard disk. The installation
process is identical to using a hard disk in conjunction with two exceptions:

* Select the USB as the storage location for the OS. 

* Leave the option checked to “Automatically configure my Qubes installation to
the disk(s) I selected and return me to the main menu”.


Upgrading
---------

For instructions in upgrading an existing installation, please see the **Release
Notes** of the version to which you want to upgrade. All of these release notes
are available from the main [downloads] page.


Getting Help
------------

 * We work very hard on making the [documentation] accurate, comprehensive, and
   useful. We urge you to read it! It may very well contain the answers to your
   questions. (Since the documentation is a community effort, we'd also greatly
   appreciate your help in [improving] it!)

 * If you don't find your answer in the documentation, it may be time to consult
   the [mailing lists], as well as the many other available sources of [help].

 * Please do not email individual developers (Marek, etc.) with
   questions about installation or other problems. Please send all such
   questions to the appropriate mailing list.


[QSB #46]: /news/2019/01/23/qsb-46/
[system requirements]: /doc/system-requirements/
[Hardware Compatibility List]: /hcl/
[live USB]: /doc/live-usb/
[downloads]: /downloads/
[verifying signatures]: /security/verifying-signatures/
[security considerations]: /doc/install-security/
[Rufus]: https://rufus.akeo.ie/
[documentation]: /doc/
[improving]: /doc/doc-guidelines/
[mailing lists]: /support/
[help]: /help/

