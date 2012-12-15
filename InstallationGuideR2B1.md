---
layout: wiki
title: InstallationGuideR2B1
permalink: /wiki/InstallationGuideR2B1/
---

Installation Guide (for Qubes Release 2 Beta 1)
===============================================

1.  [Hardware Requirements](#HardwareRequirements)
2.  [Download installer ISO](#DownloadinstallerISO)
3.  [Burning the ISO onto a DVD or USB stick](#BurningtheISOontoaDVDorUSBstick)
4.  [Upgrading from Qubes R1](#UpgradingfromQubesR1)
5.  [Installing Updates](#InstallingUpdates)
6.  [Known Issues](#KnownIssues)
7.  [Getting Help](#GettingHelp)

Hardware Requirements
---------------------

Please see the [Hardware Compatibility List?](/wiki/HCLR2) page for more information on required and recommended hardware.

Note: We don't recommend installing Qubes in a virtual machine! It will likely not work. Don't send emails asking about it. However, you can install it on an external USB hard drive and run from it, at least for testing (normally such disks are *orders* of magnitude slower than even the slowest internal hard drives).

Download installer ISO
----------------------

See [this page](/wiki/QubesDownloads) for ISO downloads. Remember, we have absolutely no control over those servers, and so you should be assuming that they might be compromised, or just be serving a compromised ISOs because their operators decided so, for whatever reason. Always verify the digital signature on the downloaded ISO. See this [page](/wiki/VerifyingSignatures) for more info about how to download and verify our GPG keys, and then verify the downloaded ISO:

``` {.wiki}
gpg -v <iso>.asc
```

Burning the ISO onto a DVD or USB stick
---------------------------------------

Once you verify this is an authentic ISO, you should burn it on a DVD.

If you prefer to use USB as a source for installation, then you just need to copy the ISO onto the USB device, e.g. using dd:

``` {.wiki}
dd if=Qubes-R2-Beta-1-x86_64-DVD.iso of=/dev/sdX
```

**Be sure to use a correct device as the target in the dd command above (instead of sdX)'''**

Before proceeding with the installation, you are encouraged to first read all the information on this page, especially the *Known Issues* paragraph.

Then, when finally ready, boot your system from the installer DVD and follow the instructions on screen. The installer is very simple and asks very few questions -- it's actually easier to install Qubes right now than most other Linux distributions!

The installer loads Xen right at the beginning, so chances are high that if you can see the installer's graphical screen, Qubes will work on your system :)

Upgrading from Qubes R1
-----------------------

If you're already running Qubes Release 1, you don't need to reinstall, it's just enough to update the packages in your Dom0 and the template VM(s). This procedure is described [here?](/wiki/UpgradeToR2).

Installing Updates
------------------

Installing updates is very easy and can be done using the "Update" button in the Qubes Manager. Alternatively it can also be done from command prompt -- see the following for more details:

-   For installing updates for Dom0 -- see instructions [here](/wiki/SoftwareUpdateDom0).
-   For installing updates for you domains (VMs) -- see instructions [here](/wiki/SoftwareUpdateVM).

Known Issues
------------

-   Installer might not support some USB keyboards (\#230). This seems to include all the Mac Book keyboards (most PC laptops have PS2 keyboards and are not affected).

-   If you don't enable Composition (System Setting -\> Desktop -\> Enable desktop effects), which you really should do, then the KDE task bar might get somehow ugly (e.g. half of it might be black). This is some KDE bug that we don't plan to fix.

-   Some keyboard layout set by KDE System Settings can cause [​keyboard not working at all](https://groups.google.com/group/qubes-devel/browse_thread/thread/77d076b65dda7226). If you hit this issue, you can switch to console (by console login option) and manually edit `/etc/X11/xorg.conf.d/00-system-setup-keyboard.conf` (and `/etc/sysconfig/keyboard`) and place correct keyboard layout settings (details in linked thread). You can check if specific keyboard layout settings are proper using `setxkbmap` tool.

-   On systems with more than 8GB of RAM there is problem with Disposable VM. To fix it, limit maximum memory allocation for DispVM to 3GB

    ``` {.wiki}
    qvm-prefs -s fedora-17-x64-dvm maxmem 3072
    qvm-create-default-dvm --default-template --default-script
    ```

-   Qubes installer/system won't boot from a USB3-attached disks due to missing modules in initramfs (\#691). Please use USB2 port/device instead for now.

Getting Help
------------

-   **User manuals are [here](/wiki/UserDoc).** (Strongly recommended!)

-   Developers documentation (normally not needed by users) is [here](/wiki/SystemDoc)

-   If you don't find answer in the sources given above, write to the *qubes-devel* mailing list (you don't need to be subscribed to the list, just send email to the address given below):
    -   [​http://groups.google.com/group/qubes-devel](http://groups.google.com/group/qubes-devel)
    -   `qubes-devel@googlegroups.com`

-   Please do not write email to individual developers (Marek, Joanna, etc) asking questions about installation or other problems. Please send all such questions to the mailing list.

