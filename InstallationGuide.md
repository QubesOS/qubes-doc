---
layout: wiki
title: InstallationGuide
permalink: /wiki/InstallationGuide/
---

Installation Guide (for Qubes Beta 1)
=====================================

**Qubes Beta 1 is scheduled to be released on April 12th, stay tuned!**

**The instructions below are just a draft -- do not try to follow them now!**

Hardware Requirements
---------------------

Minimum:

-   4GB of RAM
-   64-bit Intel or AMD processor (x86\_64 aka x64 aka AMD64)
-   Intel GPU strongly preferred (if you have Nvidia GPU, prepare for some [troubleshooting](/wiki/InstallNvidiaDriver); we haven't tested ATI hardware)
-   10GB of disk (Note that **it is possible to install Qubes on an external USB disk**, so that you can try it without sacrificing your current system. Mind, however, that USB disks are usually SLOW!)

Additional requirements:

-   Intel VT-d or AMD IOMMU technology (this is needed for effective isolation of your network VMs)

If you don't meet the additional criteria, you can still install and use Qubes. It still offers significant security improvement over traditional OSes, because things such as GUI isolation, or kernel protection do not require special hardware.

Download installer ISO
----------------------

You can download the ISO and the digital signature for the ISO from here:

-   TODO (ISO link)
-   TODO (ISO sig link)

See this [page](/wiki/VerifyingSignatures) for more info about how to download and verify our GPG keys. Then, verify the downloaded ISO:

``` {.wiki}
gpg -v ISO.asc
```

Once you verify this is an authentic ISO, you should burn it on a DVD. For instructions on how to "burn" it on a USB stick, see [this page](/wiki/UsbInstallation). Before proceeding with the installation, you are encouraged to first read all the information on this page, especially the *Known Issues* paragraph.

Then, when finally ready, boot your system from the installer DVD and follow the instructions on screen. The installer is very simple and asks very few questions -- it's actually easier to install Qubes right now, then most other Linux distributions!

The installer loads Xen right at the beginning, so chances are high that if you can see the installer's graphical screen, Qubes will work on your system :)

Migrating from Qubes Alpha 3
----------------------------

If you have Qubes Alpha 3 currently installed on your system, you must reinstall from scratch, as we offer no direct upgrade option in the installer. However, we do offer tools for smooth migration of your AppVMs. In order to do that, please backup your AppVMs using the ```qvm-backup``` tool [as usual](/wiki/BackupRestore) (under Qubes Alpha 3). Then, after you install Qubes Beta 1, you will need to restore them using a special argument that would tell the restore tool to replace the old template name, used on Alpha 3, with the new one that we use on Qubes Beta 1:

``` {.wiki}
qvm-backup-restore /mnt/backup/<backup_dir> --replace-template=linux-x64:fedora-14-x64
```

As you can see we decided to name our default template in Beta 1 in a bit more descriptive way (*fedora-14-x64*), mostly because we might be providing more templates in the future (e.g. based on other Linux distros).

Enable VT-d/IOMMU
-----------------

In order to take advantage of NetVM isolation you should enable VT-d/IOMMU (if your system supports it). To do that you should add ```iommu=1``` boot option to Xen by editing your ```grub.conf``` file. This can be done in the following way:

1.  Open konsole in Dom0 (Start-\>Applications-\>System Tools-\>Terminal)
2.  Working now under console, switch to root first:

    ``` {.wiki}
    sudo bash
    ```

3.  Use your favourite editor such as vi or joe to open the /boot/grub/grub.conf and add **```iommu=1```** just after the ```/xen.gz``` string as shown in the example below (some fragments of the file omitted for clarity):

    ``` {.wiki}
    title Qubes (2.6.34.1-14.xenlinux.qubes.x86_64)
        root (hd0,0)
        kernel /xen.gz iommu=1
        module /vmlinuz-2.6.34.1-14.xenlinux.qubes.x86_64 (...)
        module /initramfs-2.6.34.1-14.xenlinux.qubes.x86_64.img
    ```

You should now reboot your system and examine Xen logs to see if VT-d has indeed been enabled (Xen can fail to enable VT-d on your system for various of reasons, lack of proper BIOS support being the most common one). To do that just grep the Xen system log for iommu and vtd strings (you need to open konsole in Dom0 again):

``` {.wiki}
xm dmesg | grep -i iommu
xm dmesg | grep -i vtd
```

Yes, we will make this procedure more user friendly in the next Beta :)

Known Issues
------------

-   NVIDIA GPU will likely cause problems, especially if you use suspend-to-RAM. This mostly results from the general poor support for NVIDIA GPUs under Linux, which in turn is caused by the lack of open documentation for those GPUs. You might try to use the NVIDIA's proprietary driver (see the instructions [here](/wiki/InstallNvidiaDriver)), which apparently helps a lot.

-   If you have Sony Vaio Z, you will need some tinkering before you would be able to fully use this machine with Qubes (and generally with non-Windows systems). See this [page](/wiki/SonyVaioTinkering) for instructions.

-   KDE taskbar might look ugly. This problem can be easily solved by turning composition on (it's called "Desktop Effects", and can be found in System [Settings/Desktop?](/wiki/Settings/Desktop) tab).

-   Currently there is no support for delegating single USB devices to NetVMs, which likely mean that you will not be able to use your 3G modem. The only option is to delegate the whole USB controller to a NetVM, which, however, might not always be desirable, because of the other devices that are connected to this USB controller.

-   KDE might break after resume from suspend-to-RAM -- this is a KDE-specific bug and applies to some GPUs only. The solution is to switch off composition (normally Alt-Shift-F12) before putting the computer into sleep.

-   It might take up to 1 minute after you log in for the NetVM's network icon to appear in the tray -- be patient!

-   Virtualized tray icons might look incorrectly directly for some apps. This problem seems to vanish whenever the app refreshes the icon.

-   If using a wired connection in netvm, it might not come up properly after suspend/resume. One may need to manually do ` ifconfig eth0 down; ifconfig eth0 up` in netvm after resume.

-   Under some circumstances, when you choose "Use All Space" during installation, the installer will not replace your boot partition but will create another one.

Getting Help
------------

-   **User manuals are [here](/wiki/UserDoc).** (Strongly recommended!)

-   Developers documentation (normally not needed by users) is [here](/wiki/SystemDoc)

-   If you don't find answer in the sources given above, write to the *qubes-devel* mailing list:
    -   [​http://groups.google.com/group/qubes-devel](http://groups.google.com/group/qubes-devel)
    -   ```qubes-devel@googlegroups.com```

