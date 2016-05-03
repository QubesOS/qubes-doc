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

Hardware Requirements
---------------------

Please see the [system requirements] and [Hardware Compatibility List] pages for
more information on required and recommended hardware.

**Note:** We don't recommend installing Qubes in a virtual machine! It will
likely not work. Please don't send emails asking about it. You can, however,
install it on an external USB hard drive and run from it, at least for testing.
(Bear in mind, however, that such disks are typically *orders* of magnitude
slower than even the slowest internal hard drives). We also have a [live USB]
option (currently in alpha).


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

    dd if=Qubes-R3-x86_64.iso of=/dev/sdX

Adjust the filename to the version you're installing. Make sure to use the entire device (e.g. use **/dev/sda** and not **/dev/sda1**)
For example:

    dd mif=Qubes-R3-x86_64.iso of=/dev/sda

On Windows, you can use the [Rufus] tool. Be sure to select "DD image" mode (you
need to do that **after** selecting the Qubes ISO):

<img src="/attachment/wiki/InstallationGuide/rufus-main-boxed.png" height="350">

Before proceeding with the installation, you are encouraged to first read all
the information on this page. When you're ready, boot your system from the
installation source and follow the on-screen instructions. The installer is very
simple and asks very few questions. (It's actually easier to install Qubes right
now than most other Linux distributions!)

The installer loads Xen right at the beginning, so chances are high that if you
can see the installer's graphical screen, Qubes will work on your system. :)


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


[system requirements]: /doc/system-requirements/
[Hardware Compatibility List]: /hcl/
[live USB]: /doc/live-usb/
[downloads]: /downloads/
[verifying signatures]: /doc/verifying-signatures/
[security considerations]: /doc/install-security/
[Rufus]: http://rufus.akeo.ie/
[documentation]: /doc/
[improving]: /doc/doc-guidelines/
[mailing lists]: /doc/mailing-lists/
[help]: /help/

