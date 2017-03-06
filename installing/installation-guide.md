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

**Note:** We don't recommend installing Qubes in a virtual machine! It probably
won't work. Please don't send emails asking about it. Rather than running Qubes within a virtual machine, 
you can install and run Qubes on a USB drive for testing. Keep in mind that USB drives are 
slower than even the slowest internal hard drives. We also have a [live USB]
option (currently in alpha).


Downloading the ISO
-------------------

See the [downloads] page for ISO downloads. WW have no control over the servers, so it's  safest to assume that they may be
compromised. Bee certain to verify the digital signature on the downloaded
ISO. Read our guide on [verifying signatures].


Copying the ISO onto the installation Medium
--------------------------------------------

After you verify your copy is an authentic ISO, you should copy it onto a DVD or a USB drive. There are important [security considerations] to keep in mind when choosing
an installation medium.

When copying to a USB drive using Linux use the `dd` command as follows: `dd`:

    dd if=Qubes-R3-x86_64.iso of=/dev/sdX

Change `Qubes-R3-x86_64.iso` to the filename of the version you're installing,
and change `/dev/sdX` to the correct target device (e.g., `/dev/sda`).
**Warning:** Choosing the wrong device could result in data loss. Make sure to
write to the entire device (e.g., `/dev/sda`) rather than just a single
partition (e.g., `/dev/sda1`).

On Windows, you can use the [Rufus] tool. Be sure to select "DD image" mode (you
need to do that **after** selecting the Qubes ISO):

<img src="/attachment/wiki/InstallationGuide/rufus-main-boxed.png" height="350">

Before proceeding with the installation, continue reading
the information on this page. When you're ready, boot your system from the
source you created and follow the on-screen instructions. The installer is very
simple and asks very few questions. It's actually easier to install Qubes right
now than most other Linux distributions!

The installer loads Xen right at the beginning, so chances are high that if you
can see the installer's graphical screen, Qubes will work on your system. :)


Installing to a USB Drive
-------------------------

Installing an operating system onto a USB drive can be a convenient and secure
method of ensuring that your data is protected. A minimum 32 GB is required on the USB drive. Installing on a USB takes longer than an installation on a standard hard disk but The installation process is identical with two exceptions:

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
   questions. Since the documentation is a community effort, we'd also greatly
   appreciate your help in [improving] it!

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

