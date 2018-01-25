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

Warning
-------

There is a set of known upstream bugs in the Fedora installer that affect Qubes 3.2 ([Bug 1170803], [Bug 1374983], and [Bug 1268700]; tracked in Qubes issue [#2835]).
This issue is fixed in Qubes 4.0.
On Qubes 3.2, because of these bugs, the installer will try to access all existing disk partitions, run fsck on them, and mount them.
Therefore, we *strongly* recommended that, prior to starting the Qubes installer, you physically disconnect all disks that you do not want to be modified.
Furthermore, if you are installing Qubes on a potentially compromised system, we *strongly* recommended that you wipe your target installation disk before starting the installer.


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

    dd if=Qubes-R3-x86_64.iso of=/dev/sdX bs=1M && sync

Change `Qubes-R3-x86_64.iso` to the filename of the version you're installing,
and change `/dev/sdX` to the correct target device (e.g., `/dev/sda`).
**Warning:** Choosing the wrong device could result in data loss. Make sure to
write to the entire device (e.g., `/dev/sda`) rather than just a single
partition (e.g., `/dev/sda1`).

On Windows, you can use the [Rufus] tool. Be sure to select "DD image" mode (you
need to do that **after** selecting the Qubes ISO):

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

 * Please do not email individual developers (Marek, Joanna, etc.) with
   questions about installation or other problems. Please send all such
   questions to the appropriate mailing list.


[Bug 1170803]: https://bugzilla.redhat.com/show_bug.cgi?id=1170803
[Bug 1374983]: https://bugzilla.redhat.com/show_bug.cgi?id=1374983
[Bug 1268700]: https://bugzilla.redhat.com/show_bug.cgi?id=1268700
[#2835]: https://github.com/QubesOS/qubes-issues/issues/2835
[system requirements]: /doc/system-requirements/
[Hardware Compatibility List]: /hcl/
[live USB]: /doc/live-usb/
[downloads]: /downloads/
[verifying signatures]: /security/verifying-signatures/
[security considerations]: /doc/install-security/
[Rufus]: https://rufus.akeo.ie/
[documentation]: /doc/
[improving]: /doc/doc-guidelines/
[mailing lists]: /doc/mailing-lists/
[help]: /help/

