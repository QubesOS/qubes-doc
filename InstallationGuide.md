---
layout: wiki
title: InstallationGuide
permalink: /wiki/InstallationGuide/
---

Installation Guide (for Qubes 1.0 rc1)
======================================

Hardware Requirements
---------------------

Please see the [Hardware Compatibility List](/wiki/HCL) page for more information on required and recommended hardware.

Download installer ISO
----------------------

You can download the ISO and the digital signature for the ISO from here:

**Note:** Be sure that you use a modern, non-handicapped browser to access the links below (e.g. disable the NoScript and the likes extensions that try to turn your Web Browser essentially into the 90's Mosaic).

-   [​http://qubes-os.s3.amazonaws.com/iso/Qubes-R1-rc1-x86\_64-DVD.iso](http://qubes-os.s3.amazonaws.com/iso/Qubes-R1-rc1-x86_64-DVD.iso)
-   [​http://qubes-os.s3.amazonaws.com/iso/Qubes-R1-rc1-x86\_64-DVD.iso.asc](http://qubes-os.s3.amazonaws.com/iso/Qubes-R1-rc1-x86_64-DVD.iso.asc)

... or you might try to download the ISO via bit torrent:

-   [​http://qubes-os.s3.amazonaws.com/iso/Qubes-R1-rc1-x86\_64-DVD.iso?torrent](http://qubes-os.s3.amazonaws.com/iso/Qubes-R1-rc1-x86_64-DVD.iso?torrent)

See this [page](/wiki/VerifyingSignatures) for more info about how to download and verify our GPG keys. Then, verify the downloaded ISO:

``` {.wiki}
gpg -v <iso>.asc
```

Burning the ISO onto a DVD or USB stick
---------------------------------------

Once you verify this is an authentic ISO, you should burn it on a DVD.

If you prefer to use USB as a source for installation, then you just need to copy the ISO onto the USB device, e.g. using dd:

``` {.wiki}
dd if=Qubes-R1-rc1-x86_64-DVD.iso of=/dev/sdX
```

**Be sure to use a correct device as the target in the dd command above (instead of sdX)'''**

Before proceeding with the installation, you are encouraged to first read all the information on this page, especially the *Known Issues* paragraph.

Then, when finally ready, boot your system from the installer DVD and follow the instructions on screen. The installer is very simple and asks very few questions -- it's actually easier to install Qubes right now than most other Linux distributions!

The installer loads Xen right at the beginning, so chances are high that if you can see the installer's graphical screen, Qubes will work on your system :)

Migrating from Qubes Beta 3
---------------------------

If you have Qubes Beta 3 currently installed on your system, you must reinstall from scratch, as we offer no direct upgrade option in the installer (sorry). However, we do offer tools for smooth migration of your AppVMs. In order to do that, please backup your AppVMs using the ```qvm-backup``` tool [as usual](/wiki/BackupRestore). Then, after you install Qubes 1.0 rc1, you can restore them using ```qvm-backup-restore``` tool. However, because we have changed the default template in RC1, you should tell qvm-back-restore about that by passing ```--replace-template``` option:

``` {.wiki}
qvm-backup-restore <backup_dir> --replace-template=fedora-15-x64:fedora-17-x64 
```

Installing Updates
------------------

Installing updates is very easy and can be done using the "Update" button in the Qubes Manager. Alternatively it can also be done from command prompt -- see the following for more details:

-   For installing updates for Dom0 -- see instructions [here](/wiki/SoftwareUpdateDom0).
-   For installing updates for you domains (VMs) -- see instructions [here](/wiki/SoftwareUpdateVM).

Known Issues
------------

-   NVIDIA GPU will likely cause problems, especially if you use suspend-to-RAM. This mostly results from the general poor support for NVIDIA GPUs under Linux, which in turn is caused by the lack of open documentation for those GPUs. You might try to use the NVIDIA's proprietary driver (see the instructions [here](/wiki/InstallNvidiaDriver)), which apparently helps a lot.

-   Installer might not support some USB keyboards (\#230). This seems to include all the Mac Book keyboards (most PC laptops have PS2 keyboards and are not affected).

-   If you don't enable Composition (System Setting -\> Desktop -\> Enable desktop effects), which you really should do, then the KDE task bar might get somehow ugly (e.g. half of it might be black). This is some KDE bug that we don't plan to fix.

Getting Help
------------

-   **User manuals are [here](/wiki/UserDoc).** (Strongly recommended!)

-   Developers documentation (normally not needed by users) is [here](/wiki/SystemDoc)

-   If you don't find answer in the sources given above, write to the *qubes-devel* mailing list:
    -   [​http://groups.google.com/group/qubes-devel](http://groups.google.com/group/qubes-devel)
    -   ```qubes-devel@googlegroups.com```

