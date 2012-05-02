---
layout: wiki
title: HCL
permalink: /wiki/HCL/
---

Hardware Compatibility List for Qubes OS
========================================

The following is a list of systems that have been tested and seem to work fine with Qubes OS (or mostly fine). Unless otherwise noted, all the systems have support for Intel VT-d, which is needed to properly secure driver domains in Qubes OS (netvm, usbvm, etc). Systems without VT-d are still usable, but you don't get an extra protection from driver domain separation (you still get lots of security benefit from AppVM separation though).

General system requirements
---------------------------

Minimum:

-   4GB of RAM
-   64-bit Intel or AMD processor (x86\_64 aka x64 aka AMD64)
-   Intel GPU strongly preferred (if you have Nvidia GPU, prepare for some [troubleshooting](/wiki/InstallNvidiaDriver); we haven't tested ATI hardware)
-   At least 20GB of disk (Note that **it is possible to install Qubes on an external USB disk**, so that you can try it without sacrificing your current system. Mind, however, that USB disks are usually SLOW!)
-   Fast SSD disk strongly recommended

Additional requirements:

-   Intel VT-d or AMD IOMMU technology (this is needed for effective isolation of your network VMs)
-   TPM with proper BIOS support if you want to use option [​Anti Evil Maid](http://theinvisiblethings.blogspot.com/2011/09/anti-evil-maid.html)

If you don't meet the additional criteria, you can still install and use Qubes. It still offers significant security improvement over traditional OSes, because things such as GUI isolation, or kernel protection do not require special hardware.

**Note:** We don't recommend installing Qubes in a virtual machine! **Note:** There is a problem with supporting keyboard and mouse on Mac, and so Mac hardware is currently unsupported (patches welcomed!)

Specific systems tested by Qubes core developers
------------------------------------------------

-   Lenovo Thinkpad T420 w/ Intel graphics
-   Lenovo Thinkpad T420s w/ Intel graphics (requires 2.3.7 kernel to handle the panel screen correctly)
-   Lenovo Thinkpad T61 w/ Nvidia graphics (Quadro NVS 140M) - works well (using xenlinux 2.6.38 kernel), better stability with [nvidia binary drivers](/wiki/InstallNvidiaDriver) - especially when using external monitor

-   Samsung X460 - works well on both xenlinux 2.6.38 and pvops 3.2.7 kernel; after resume ethernet driver (sky2) need to be reloaded in netvm to start working again

-   Sony Vaio Z 12 -- works well, but some [tinkering required](/wiki/SonyVaioTinkering)

Specific systems tested by the Qubes community
----------------------------------------------

TODO
