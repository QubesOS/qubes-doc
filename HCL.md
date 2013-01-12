---
layout: wiki
title: HCL
permalink: /wiki/HCL/
---

Hardware Compatibility List for Qubes OS
========================================

The following is a list of systems that have been tested and seem to work fine with Qubes OS

General system requirements
---------------------------

Minimum:

-   4GB of RAM
-   64-bit Intel or AMD processor (x86\_64 aka x64 aka AMD64)
-   Intel GPU strongly preferred (if you have Nvidia GPU, prepare for some [troubleshooting](/wiki/InstallNvidiaDriver); we haven't tested ATI hardware)
-   At least 20GB of disk (Note that **it is possible to install Qubes on an external USB disk**, so that you can try it without sacrificing your current system. Mind, however, that USB disks are usually SLOW!)
-   Fast SSD disk strongly recommended

Additional requirements:

-   Intel VT-x or AMD-v technology (this is needed to run HVM domains only, such as Windows-based AppVMs)
-   Intel VT-d or AMD IOMMU technology (this is needed for effective isolation of your network VMs)
-   TPM with proper BIOS support if you want to use option [​Anti Evil Maid](http://theinvisiblethings.blogspot.com/2011/09/anti-evil-maid.html)

If you don't meet the additional criteria, you can still install and use Qubes. It still offers significant security improvement over traditional OSes, because things such as GUI isolation, or kernel protection do not require special hardware.

**Note:** We don't recommend installing Qubes in a virtual machine!

**Note:** There is a problem with supporting keyboard and mouse on Mac, and so Mac hardware is currently unsupported (patches welcomed!)

Hardware Compatibility List
---------------------------

Device

Qubes R1

Qubes R2 Beta1

Standard feautures

VT-d

TPM

Remarks

Standard features

VT-x

VT-d

TPM

Remarks

Lenovo Thinkpad T420

OK

OK

?

OK

OK

OK

?

Lenovo Thinkpad T420s

OK

OK

?

OK

OK

OK

?

Lenovo Thinkpad T61
 (Nvidia Quadro NVS 140M)

OK

X

?

OK

OK

X

?

Samsung X460

OK

X

?

OK

OK

X

?

Sony Vaio Z 12
 (2010 edition)

OK

OK

?

[link](https://qubes-os.org/trac/wiki/SonyVaioTinkering)

OK

OK

OK

?

[link](https://qubes-os.org/trac/wiki/SonyVaioTinkering)

Dell Latitude E6420
 (Intel HD graphics; Sandy Bridge; i5-2520M)

OK

OK

?

needs kernel 3.4.17+

OK

OK

OK

?

needs kernel 3.4.17+

Fujitsu S751
 (HD3000; QM67; i5-2520M; BIOS 1.18)

OK

OK

?

OK

OK

OK

?

Sony Vaio Z2
 (2011 edition)

OK

OK

?

[link](https://groups.google.com/d/msg/qubes-devel/xoyNCigBvFE/fkC6em-Wqd0J)

?

?

?

?

Lenovo Thinkpad W510
 (nVidia; i7-Q820)

OK

OK

?

[link](https://groups.google.com/forum/#!msg/qubes-devel/TgDWwBs36yA/IUFZPHs716cJ)

?

?

?

?

Lenovo Thinkpad x220
 (HD?000; i5-?)

OK

OK

?

?

?

?

?

Lenovo Thinkpad x230

\*

OK

?

[link](https://groups.google.com/d/msg/qubes-devel/XN6JrEXVOVA/lkxGRA00EqgJ)

?

?

?

?

Dell Latitude 5520

OK

OK

?

[link](https://groups.google.com/group/qubes-devel/msg/7418e7084c2de99f?hl=en)

?

?

?

?

Dell Latitude E6520

OK

OK

?

[link](https://groups.google.com/group/qubes-devel/msg/340afc6fc2d06d0e)

?

?

?

?

Dell PowerEdge T110 II
 (onboard Matrox; Xeon E3-1230)

OK

OK

?

?

?

?

?

Dell Precision M4600
 (i7-2860QM; NVIDIA Quadro 1000M)

OK

OK

?

?

?

?

?

Toshiba Tecra S11

OK

OK

?

[link](https://groups.google.com/group/qubes-devel/browse_thread/thread/fdec0ec165a87726)

?

?

?

?

Toshiba Tecra A11-15X
 (i7-M620)

OK

OK

?

?

?

?

?

Toshiba M780 S7240
 (BIOS latest)

OK

OK

?

?

?

?

?
