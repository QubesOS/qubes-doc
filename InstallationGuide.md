---
layout: wiki
title: InstallationGuide
permalink: /wiki/InstallationGuide/
---

Installation Guide (for Qubes Beta 3)
=====================================

Hardware Requirements
---------------------

Minimum:

-   4GB of RAM
-   64-bit Intel or AMD processor (x86\_64 aka x64 aka AMD64)
-   Intel GPU strongly preferred (if you have Nvidia GPU, prepare for some [troubleshooting](/wiki/InstallNvidiaDriver); we haven't tested ATI hardware)
-   20GB of disk (Note that **it is possible to install Qubes on an external USB disk**, so that you can try it without sacrificing your current system. Mind, however, that USB disks are usually SLOW!)
-   Fast SSD disk strongly recommended

Additional requirements:

-   Intel VT-d or AMD IOMMU technology (this is needed for effective isolation of your network VMs)

If you don't meet the additional criteria, you can still install and use Qubes. It still offers significant security improvement over traditional OSes, because things such as GUI isolation, or kernel protection do not require special hardware.

**Note:** We don't recommend installing Qubes in a virtual machine! **Note:** There is a problem with supporting keyboard and mouse on Mac, and so Mac hardware is currently unsupported (patches welcomed!)

Download installer ISO
----------------------

You can download the ISO and the digital signature for the ISO from here:

-   [​http://s3-eu-west-1.amazonaws.com/qubes-os/iso/Qubes-R1-Beta3-x86\_64-DVD.iso](http://s3-eu-west-1.amazonaws.com/qubes-os/iso/Qubes-R1-Beta3-x86_64-DVD.iso)
-   [​http://s3-eu-west-1.amazonaws.com/qubes-os/iso/Qubes-R1-Beta3-x86\_64-DVD.iso.asc](http://s3-eu-west-1.amazonaws.com/qubes-os/iso/Qubes-R1-Beta3-x86_64-DVD.iso.asc)

or you might try to download the ISO via bit torrent:

-   [​http://s3-eu-west-1.amazonaws.com/qubes-os/iso/Qubes-R1-Beta3-x86\_64-DVD.iso?torrent](http://s3-eu-west-1.amazonaws.com/qubes-os/iso/Qubes-R1-Beta3-x86_64-DVD.iso?torrent)

See this [page](/wiki/VerifyingSignatures) for more info about how to download and verify our GPG keys. Then, verify the downloaded ISO:

``` {.wiki}
gpg -v <iso>.asc
```

Burning the ISO onto a DVD or USB stick
---------------------------------------

Once you verify this is an authentic ISO, you should burn it on a DVD. For instructions on how to "burn" it on a USB stick, see [this page](/wiki/UsbInstallation). Before proceeding with the installation, you are encouraged to first read all the information on this page, especially the *Known Issues* paragraph.

Then, when finally ready, boot your system from the installer DVD and follow the instructions on screen. The installer is very simple and asks very few questions -- it's actually easier to install Qubes right now than most other Linux distributions!

The installer loads Xen right at the beginning, so chances are high that if you can see the installer's graphical screen, Qubes will work on your system :)

Migrating from Qubes Beta 2
---------------------------

If you have Qubes Beta 2 currently installed on your system, you must reinstall from scratch, as we offer no direct upgrade option in the installer (sorry). However, we do offer tools for smooth migration of your AppVMs. In order to do that, please backup your AppVMs using the ```qvm-backup``` tool [as usual](/wiki/BackupRestore). Then, after you install Qubes Beta 3, you can restore them using ```qvm-backup-restore``` tool that. Because we have changed the default template in Beta 3, you should tell qvm-back-restore about that by passing ```--replace-template``` option:

``` {.wiki}
qvm-backup-restore <backup_dir> --replace-template=fedora-14-x64:fedora-15-x64
```

Installing Updates
------------------

Currently the user must start the update process manually (in future versions we will make this automatic).

-   For installing updates for Dom0 -- see instructions [here](/wiki/SoftwareUpdateDom0).
-   For installing updates for you domains (VMs) -- see instructions [here](/wiki/SoftwareUpdateVM).

Known Issues
------------

-   NVIDIA GPU will likely cause problems, especially if you use suspend-to-RAM. This mostly results from the general poor support for NVIDIA GPUs under Linux, which in turn is caused by the lack of open documentation for those GPUs. You might try to use the NVIDIA's proprietary driver (see the instructions [here](/wiki/InstallNvidiaDriver)), which apparently helps a lot.

-   If you have Sony Vaio Z, you will need some tinkering before you would be able to fully use this machine with Qubes (and generally with non-Windows systems). See this [page](/wiki/SonyVaioTinkering) for instructions.

-   Installer might not support some USB keyboards (\#230). This seems to include all the Mac Book keyboards (most PC laptops have PS2 keyboards and are not affected).

Getting Help
------------

-   **User manuals are [here](/wiki/UserDoc).** (Strongly recommended!)

-   Developers documentation (normally not needed by users) is [here](/wiki/SystemDoc)

-   If you don't find answer in the sources given above, write to the *qubes-devel* mailing list:
    -   [​http://groups.google.com/group/qubes-devel](http://groups.google.com/group/qubes-devel)
    -   ```qubes-devel@googlegroups.com```

