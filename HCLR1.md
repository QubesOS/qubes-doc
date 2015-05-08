---
layout: doc
title: HCLR1
permalink: /doc/HCLR1/
redirect_from: /wiki/HCLR1/
---

Hardware Compatibility List for Qubes OS R1
===========================================

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
-   TPM with proper BIOS support if you want to use option [Anti Evil Maid](http://theinvisiblethings.blogspot.com/2011/09/anti-evil-maid.html)

If you don't meet the additional criteria, you can still install and use Qubes. It still offers significant security improvement over traditional OSes, because things such as GUI isolation, or kernel protection do not require special hardware.

**Note:** We don't recommend installing Qubes in a virtual machine!

**Note:** There is a problem with supporting keyboard and mouse on Mac, and so Mac hardware is currently unsupported (patches welcomed!)

Specific systems known to work tested by Qubes core developers
--------------------------------------------------------------

-   Lenovo Thinkpad T420 w/ Intel graphics
-   Lenovo Thinkpad T420s w/ Intel graphics (requires 3.2.7 kernel to handle the panel screen correctly)
-   Lenovo Thinkpad T61 w/ Nvidia graphics (Quadro NVS 140M) - works well. This system doesn't support VT-d!

-   Samsung X460 - works well on both xenlinux 2.6.38 and pvops 3.2.7 kernel; after resume ethernet driver (sky2) need to be reloaded in netvm to start working again. Even though the chipset suppors VT-d, the BIOS is broken, and so the VT-d is not picked up by Xen, so it effectively doesn't work.

-   Sony Vaio Z 12 (2010 edition) -- works well, but some [tinkering required](/wiki/SonyVaioTinkering)

-   Dell Latitude E6420 w/ Intel graphics (Sandy Bridge), i5-2520M CPU - works well on 3.4.18 (haven't tested default 3.2.30 kernel)

Specific systems known to work tested by the Qubes community
------------------------------------------------------------

-   Fujitsu S751 seems to work well, but requires BIOS update to get VT-d working. Reported by [Zrubecz Laszlo](https://groups.google.com/forum/#!msg/qubes-devel/xoyNCigBvFE/ER61L6TbVpwJ).
-   Sony Vaio Z2 (2011 edition) works fine but requires some BIOS mod to enable VT-d. Reported by [Danny Fullerton](https://groups.google.com/d/msg/qubes-devel/xoyNCigBvFE/fkC6em-Wqd0J).
-   Lenovo Thinkpad W510 with core I7 Q820, with proprietary Nvidia driver works fine. Reported by [Sebastian Hültenschmidt](https://groups.google.com/forum/#!msg/qubes-devel/TgDWwBs36yA/IUFZPHs716cJ).
-   Lenovo Thinkpad x220 8GB RAM, Intel graphics (core i5), VT-d is working. Reported by [Stefan Boresch](https://groups.google.com/group/qubes-devel/msg/f41578eef913446a)
-   Dell Latitude 5520, requires some minor fixes for networking to work. Reported by [Erik Edin](https://groups.google.com/group/qubes-devel/msg/7418e7084c2de99f?hl=en).
-   Dell Latitude E6520 with i7-2760QM CPU. VT-d works fine. nVidia graphics not working, but integrated Intel does. Reported by [Steven Collins](https://groups.google.com/group/qubes-devel/msg/340afc6fc2d06d0e)
-   Dell [PowerEdge?](/wiki/PowerEdge) T110 II, onboard Matrox graphics (Intel Xeon E3-1230), VT-d is working. Reported by [Geoff](https://groups.google.com/group/qubes-devel/msg/8a894915909eeaee)
-   Toshiba Tecra S11. Requires [some tinkering](https://groups.google.com/group/qubes-devel/browse_thread/thread/fdec0ec165a87726) to enable 3G modem. Reported by Jan Beerden
-   Toshiba M780 S7240, requires latest BIOS to have VT-d working, [some problems](https://groups.google.com/group/qubes-devel/browse_thread/thread/2b89d2dc5f999ab7) with card reader. Reported by [Franz](https://groups.google.com/group/qubes-devel/browse_thread/thread/66e97c990a08d8e2)
-   Dell Precision M4600 Intel Core i7-2860QM, 16GB ram, NVIDIA Quadro 1000M, EMEA Intel Pro Wireless 6300. Reported by [nqe](https://groups.google.com/group/qubes-devel/browse_thread/thread/ddf35d12a35f96a3)
-   Tecra A11-15X: RAM 8GB CPU I7 M620 2.67 ghz. Reported by [PirBoazo](https://groups.google.com/group/qubes-devel/browse_thread/thread/c0d5f6a33d672b62)

Specific systems known to not work well with Qubes
--------------------------------------------------

-   All systems based on Ivy Bridge processors with the Intel integrated GPU used as the primary display. Currently our Xorg drivers in Dom0 do not support the latest Intel integrated GPUs from Ivy Bridge line. For instructions on possible workarounds see [this message](https://groups.google.com/d/msg/qubes-devel/XN6JrEXVOVA/GMTjUM2J6QEJ).
    -   Specific system in above category: Lenovo x230 reported by [Chris](https://groups.google.com/d/msg/qubes-devel/XN6JrEXVOVA/lkxGRA00EqgJ) - with detailed list of working and not working components

