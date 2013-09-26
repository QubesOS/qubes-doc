---
layout: wiki
title: HCL
permalink: /wiki/HCL/
---

Hardware Compatibility List for Qubes OS
========================================

General System Requirements
---------------------------

Minimum:

-   64-bit Intel or AMD processor (x86\_64 aka x64 aka AMD64)
-   4 GB RAM
-   32 GB disk space

Recommended:

-   Fast SSD (strongly recommended)
-   Intel GPU (strongly preferred)
    -   Nvidia GPUs may require significant [troubleshooting](/wiki/InstallNvidiaDriver).
    -   ATI GPUs have not been formally tested (but see the [Hardware Compatibility List](/wiki/HCL#HardwareCompatibilityList) below).
-   Intel VT-x or AMD-v technology (required for running HVM domains, such as Windows-based AppVMs)
-   Intel VT-d or AMD IOMMU technology (required for effective isolation of network VMs)
-   TPM with proper BIOS support (required for [​Anti Evil Maid](http://theinvisiblethings.blogspot.com/2011/09/anti-evil-maid.html))

Please note:

-   Qubes **can** be installed on systems which do not meet the recommended requirements. Such systems will still offer significant security improvements over traditional operating systems, since things like GUI isolation and kernel protection do not require special hardware.
-   Qubes **can** be installed on a USB flash drive or external disk, and testing has shown that this works very well. A fast USB 3.0 flash drive is recommended for this. (As a reminder, its capacity must be at least 32 GB.) Simply plug the flash drive into the computer before booting into the Qubes installer, choose the flash drive as the target installation disk, and proceed with the installation normally. After Qubes has been installed on the flash drive, it can then be plugged into other computers in order to boot from Qubes. In addition to the convenience of having a portable copy of Qubes, this allows users to test for hardware compatibility on multiple machines (e.g., at a brick-and-mortar computer store) before deciding on which computer to purchase. (For more on hardware compatibility testing, see below.)
-   Installing Qubes in a virtual machine is not recommended, as it uses its own bare-metal hypervisor (Xen).
-   Macintosh PCs are not currently supported due to keyboard and mouse problems. (Patches welcome!)
-   [​Advice on finding a VT-d capable notebook](https://groups.google.com/d/msg/qubes-users/Sz0Nuhi4N0o/ZtpJdoc0OY8J).

Hardware Compatibility List
---------------------------

**Device**

**Qubes R1**

**Qubes R2 Beta2**

**Reported by**

Standard feautures

VT-d

Remarks

Standard features

VT-x
(HVM)

VT-d

Remarks

Lenovo Thinkpad T420

OK

OK

Qubes core developers

Lenovo Thinkpad T420s
 (Intel HD graphics; Sandy Bridge; i5-2520M)

OK

OK

OK

OK

OK

Requires kernel 3.2.30 to support S3 sleep (the default kernel S3 sleep causes system reboot)

Qubes core developers

Lenovo Thinkpad T61
 (Nvidia Quadro NVS 140M)

OK

X

Qubes core developers

Samsung X460

OK

X

Qubes core developers

Sony Vaio Z 12
 (2010 edition)

OK

OK

[read more](/trac/wiki/SonyVaioTinkering)

OK

OK

OK

[read more](/trac/wiki/SonyVaioTinkering)

Qubes core developers

Dell Latitude E6420
 (Intel HD graphics; Sandy Bridge; i5-2520M)

OK

OK

needs kernel 3.4.17+

OK

OK

OK

Suspend doesn't work on 3.7.6 kernel, but work on 3.7.4

Qubes core developers

Apple MacBookPro
 (i7 M620)

?

?

X

OK

X

[​read more](https://groups.google.com/d/topic/qubes-devel/hag-MQDH_Vs/discussion)

[​Alex Dubois](https://groups.google.com/d/msg/qubes-devel/hag-MQDH_Vs/pmJ7TIWUWAsJ)

Apple MacBookPro
 (Intel HD Graphics, Ivy Bridge, i5-3210M)

?

?

X

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-users/ZbjrseLxuPQ/discussion)

[​ph145h](https://groups.google.com/d/msg/qubes-users/ZbjrseLxuPQ/5Jx5DvpnwMMJ)

ASUS UX-31

\*

?

[​Stephen Boyd](https://groups.google.com/d/topic/qubes-devel/6I07Bbzn5M4/discussion)

ASUS X55A

X

X

[​read more](https://groups.google.com/d/topic/qubes-devel/2csjvHia9Rw/discussion)

X

X

X

[​read more](https://groups.google.com/d/topic/qubes-devel/2csjvHia9Rw/discussion)

[​Zrubi](https://groups.google.com/d/msg/qubes-devel/2csjvHia9Rw/NRsqR0g6wIMJ)

Dell Latitude E4300
 (Intel GMA 4500M; Mobile 4 Series Chipset; Core2 Duo P9600)

X

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-devel/LNJqSbH0cOQ/discussion)

[​Pablo Costa](https://groups.google.com/d/msg/qubes-devel/LNJqSbH0cOQ/VC9EwEDrXMQJ)

Dell Latitude 5520

OK

OK

[​read more](https://groups.google.com/group/qubes-devel/msg/7418e7084c2de99f?hl=en)

[​Erik Edin](https://groups.google.com/group/qubes-devel/msg/7418e7084c2de99f?hl=en)

Dell Latitude E6320
 (Intel HD graphics; Sandy Bridge; i5-2540M; BIOS: A06)

OK

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-users/FyA7_Kzw1WA/discussion)

[Alex​](https://groups.google.com/d/msg/qubes-users/F-jVh62ANak/s57rqUWTY7kJ)

Dell Latitude E6430
 (Intel HD graphics; Ivy Bridge; i5-3340M, BIOS: A11)

OK

OK

OK

[​Zrubi](https://groups.google.com/d/msg/qubes-users/pAVGe04ZC48/AJwY6yd7LeIJ)

Dell Latitude E6520

OK

OK

[​read more](https://groups.google.com/group/qubes-devel/msg/340afc6fc2d06d0e)

[​Steven Collins](https://groups.google.com/group/qubes-devel/msg/340afc6fc2d06d0e)

Dell PowerEdge T110 II
 (onboard Matrox; Xeon E3-1230)

OK

OK

[​Geoff](https://groups.google.com/group/qubes-devel/msg/8a894915909eeaee)

Dell Precision M4600
 (i7-2860QM; NVIDIA Quadro 1000M)

OK

OK

[​nqe](https://groups.google.com/group/qubes-devel/browse_thread/thread/ddf35d12a35f96a3)

Dell XPS 13
 (i5; intel HD; sandy bridge; BIOS A03)

OK

?

OK

?

?

[​read more](https://groups.google.com/d/msg/qubes-devel/jamRkZJDC0g/KTniY0Y3dioJ)

[​j](https://groups.google.com/d/msg/qubes-devel/7JumqdldVJM/n9TiDVxc2jkJ)

Dell XPS 13 (L322X)
 (i7-3537U; intel HD; Ivy Bridge; BIOS A09)

\*

OK

X

[​read more](https://groups.google.com/d/topic/qubes-users/21kqNBzJLPw/discussion)

[​Brian J Smith-Sweeney](https://groups.google.com/d/msg/qubes-users/21kqNBzJLPw/e74SMRweTMsJ)

Fujitsu S751
 (HD3000; QM67; i5-2520M; BIOS 1.18)

OK

OK

OK

OK

OK

needs kernel downgrade to 3.7.4

[​Zrubi](https://groups.google.com/forum/#!msg/qubes-devel/xoyNCigBvFE/ER61L6TbVpwJ)

HP Pavilion Sleekbook 14-B030TU
 (Ivy Bridge; Intel HD Graphics; i5-3317; BIOS F.06)

?

?

OK

OK

OK

[Stephen Boyd](https://groups.google.com/d/msg/qubes-devel/ZC_SQJhXVOM/4aLjEc7GIsUJ)

Lenovo Thinkpad Edge E130
 (Ivy Bridge; HD Graphics i3-3217U; BIOS: 2.05)

?

?

OK

OK

OK

[Danny Cautaert](https://groups.google.com/d/msg/qubes-devel/kGnZKZ9ILKA/2vpzltNW3K4J)

Lenovo Thinkpad T430
 (Ivy Bridge; HD Graphics; i5-3360M; BIOS: 2.51)

?

?

OK

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-devel/LSVluAZ9Udo/discussion)

[Alex Dubois](https://groups.google.com/d/msg/qubes-devel/LSVluAZ9Udo/Fl3jmt4tWssJ)

Lenovo Thinkpad T430U
 (Ivy Bridge; HD Graphics +GT 620M; i7-3517M; BIOS: 2.08)

?

?

OK

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-devel/Z9M_k3i6dxU/discussion)

[tigerbeard](https://groups.google.com/d/msg/qubes-devel/Z9M_k3i6dxU/09CqBppyMnsJ)

Lenovo Thinkpad W510
 (nVidia; i7-Q820)

OK

OK

[​read more](https://groups.google.com/forum/#!msg/qubes-devel/TgDWwBs36yA/IUFZPHs716cJ)

[​Sebastian Hültenschmidt](https://groups.google.com/forum/#!msg/qubes-devel/TgDWwBs36yA/IUFZPHs716cJ)

Lenovo Thinkpad x220
 (HD?000; i5-?)

OK

OK

[​Stefan Boresch](https://groups.google.com/group/qubes-devel/msg/f41578eef913446a)

Lenovo Thinkpad x230
 (Ivy Bridge; HD Graphics; i5-3320M; BIOS:2.51)

\*

OK

[​read more](https://groups.google.com/d/msg/qubes-devel/XN6JrEXVOVA/lkxGRA00EqgJ)

\*

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-users/hf0vkL3TE7k/discussion)

[​Chris](https://groups.google.com/d/msg/qubes-devel/XN6JrEXVOVA/lkxGRA00EqgJ)
 [​mgflax](https://groups.google.com/d/msg/qubes-users/hf0vkL3TE7k/VOtrW3wEbtMJ)

Toshiba Tecra S11

OK

OK

[​read more](https://groups.google.com/group/qubes-devel/browse_thread/thread/fdec0ec165a87726)

[​Jan Beerden](https://groups.google.com/group/qubes-devel/browse_thread/thread/fdec0ec165a87726)

Toshiba Tecra A11-15X
 (i7-M620)

OK

OK

[​PirBoazo](https://groups.google.com/group/qubes-devel/browse_thread/thread/c0d5f6a33d672b62)

Toshiba M780 S7240
 (BIOS latest)

OK

OK

[​Franz](https://groups.google.com/group/qubes-devel/browse_thread/thread/66e97c990a08d8e2)

Samsung Series 7 Chronos NP700Z5C
 (nVidia Optimus; i7-3635QM; BIOS P04ABJ)

OK

?

[​read more](https://groups.google.com/d/msg/qubes-devel/0xBeX8NZFiU/bUqxGdn6KOMJ)

OK

OK

X

[​read more](https://groups.google.com/d/topic/qubes-devel/Wu1mn9f1qgM/discussion)

[​Outback Dingo](https://groups.google.com/d/msg/qubes-devel/0xBeX8NZFiU/bUqxGdn6KOMJ)

Sony Vaio Z2
 (2011 edition)

OK

OK

[​read more](https://groups.google.com/d/msg/qubes-devel/xoyNCigBvFE/fkC6em-Wqd0J)

[​Danny Fullerton](https://groups.google.com/d/msg/qubes-devel/xoyNCigBvFE/fkC6em-Wqd0J)

Zareason Ultra Lap 420
 (Ivy Bridge; HD Graphics; i5-3317U)

OK

OK

[​Ant](https://groups.google.com/d/msg/qubes-users/uKI-VBtKWxg/uKjsdGNSpSQJ)

ASRock Z77 Pro4
 (Ivy Bridge; Xeon E3-1200 Graphics; i7-3770; BIOS: P1.40)

OK

OK

OK

[read more](https://groups.google.com/d/topic/qubes-users/lycnE-LcJBo/discussion)

[gorka](https://groups.google.com/d/msg/qubes-users/lycnE-LcJBo/0u10xl7AMrIJ)

Dell Precision T3400 Workstation
 (NVIDIA Quadro NVS 290; Intel Q6600; BIOS: A09)

?

?

OK

OK

X

[Andrew Sorensen](https://groups.google.com/d/msg/qubes-devel/D16dM3rg8Iw/zOEZmjTJkRIJ)

GA-fxa990-ud3 (rev 3.0)
 (AMD FX-8350; GTX 470)

?

?

OK

OK

X

[m astroj](https://groups.google.com/d/msg/qubes-devel/oox94EsIduQ/7w4xUoK5pxwJ)

MSI Big Bang
 (i7-950; Radeon HD 6770)

?

?

OK

?

?

[read more](https://groups.google.com/d/topic/qubes-devel/TxzaoodB02o/discussion)

[Andrew Sorensen](https://groups.google.com/d/msg/qubes-devel/TxzaoodB02o/NxVHjaPoRYoJ)

Supermicro X10SAE
 (Haswell; Radeon HD 5700; Xeon E3-1245; BIOS: 1.0)

X

X

[read more](https://groups.google.com/d/topic/qubes-users/V9BLpdf4xCs/discussion)

OK

OK

X

[read more](https://groups.google.com/d/topic/qubes-users/V9BLpdf4xCs/discussion)

[Qubes Fan](https://groups.google.com/d/msg/qubes-users/V9BLpdf4xCs/v4XcOjLT6uUJ)

Generating and Submitting New Reports
-------------------------------------

In order to generate an HCL report in Qubes, simply open a terminal in dom0 and run `qubes-hcl-report <vm-name>`, where `<vm-name>` is the name of the VM to which the generated HCL files will be saved. (Note: If you are working with a new Qubes installation, you may need to update your system in order to download this script.)

Users are encouraged to submit their HCL reports for the benefit of further Qubes development and other users. If you would like to submit your HCL report, please send the **HCL Info** `.txt` file to `qubes-users@googlegroups.com` (see [here](/wiki/QubesLists) information about the mailing lists) with the subject `HCL - <your machine model name>`. Please feel free to include any useful information about any Qubes features you may have tested, as well as general machine compatibility (video, networking, sleep, etc.). If you have problems with your hardware, please send the **HCL Support Files** `.cpio.gz` file as well.

**Please note:** The **HCL Support Files** may contain numerous hardware details, including serial numbers. If, for privacy or security reasons, you do not wish to make this information public, please **do not** send them to the public mailing list.
