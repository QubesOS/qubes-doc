---
layout: wiki
title: HCL
permalink: /wiki/HCL/
---

Hardware Compatibility List (HCL) for All Qubes OS Releases
===========================================================

This list contains information about the [latest stable release](/wiki/HCL#LatestStableRelease) (**R1**) and the [latest development release](/wiki/HCL#LatestDevelopmentRelease) (**R2B3**). You can also find information about the [previous releases](/wiki/HCL#PreviousReleases) here.

Generating and Submitting New Reports
-------------------------------------

In order to generate an HCL report in Qubes, simply open a terminal in dom0 and run `qubes-hcl-report <vm-name>`, where `<vm-name>` is the name of the VM to which the generated HCL files will be saved.
 (Note: If you are working with a new Qubes installation, you may need to update your system in order to download this script.)

Users are encouraged to submit their HCL reports for the benefit of further Qubes development and other users. If you would like to submit your HCL report, please send the **HCL Info** `.txt` file to `qubes-users@googlegroups.com` (see [here](/wiki/QubesLists) information about the mailing lists) with the subject `HCL - <your machine model name>`.
 Please include any useful information about any Qubes features you may have tested (see the legend above), as well as general machine compatibility (video, networking, sleep, etc.).
 If you have problems with your hardware, please send the **HCL Support Files** `.cpio.gz` file as well.

**Please note:** The **HCL Support Files** may contain numerous hardware details, including serial numbers. If, for privacy or security reasons, you do not wish to make this information public, please **do not** send the `.cpio.gz` file to the public mailing list.

Reports
-------

**Note:** The HCL is a compilation of reports generated and submitted by users. Except in the case of developer-reported entries, the Qubes team has not independently verified the accuracy of these reports. If using the list to make a purchasing decision, we recommend that you first test the hardware yourself, if possible.

**Legend**

**Background colors**

White

We have not received a sufficient report yet

Green

The reporter has sent an HCL Info output which indicates everything is OK.

Yellow

Some non-required feature is missing (e.g., VT-d), or manual tweaking is required in order to get some components to work.

Red

Some primary feature is not working. These are usually machines with poor or nonexistent Linux support in general.

**Marks**

Yes,OK

The feature is working correctly.

No,X

The feature does not work or is not present.

\*

An asterisk (\*) indicates that some kind of tweaking is needed.

 

A blank cell indicates that we lack information about a feature.

Latest Development Release
--------------------------

Qubes R2 Beta3
==============

Device

Runs out of the box

Kernel
3.11

Kernel
3.9

Kernel
3.7

VT-x
(HVM)

VT-d

Remarks

Reported by

**Laptop Devices**

Apple MacBookPro
 (i7 M620; GeForce GT 330M)

Yes

No

No Network, Chipset doesn't support VT-d! [​read more](https://groups.google.com/d/topic/qubes-devel/hag-MQDH_Vs/discussion)

[​Alex Dubois](https://groups.google.com/d/msg/qubes-devel/hag-MQDH_Vs/pmJ7TIWUWAsJ)

Apple MacBookPro
 (i5-3210M; Ivy Bridge; HD4000)

Yes

Yes

No CPU VT-d support!? [​read more](https://groups.google.com/d/topic/qubes-users/ZbjrseLxuPQ/discussion)

[​ph145h](https://groups.google.com/d/msg/qubes-users/ZbjrseLxuPQ/5Jx5DvpnwMMJ)

ASUS X55A

No

No

[​read more](https://groups.google.com/d/topic/qubes-devel/2csjvHia9Rw/discussion)

[​Zrubi](https://groups.google.com/d/msg/qubes-devel/2csjvHia9Rw/NRsqR0g6wIMJ)

ASUS Zenbook UX31A
 (i7-3517U; Ivy Bridge; HD4000; BIOS UX31A.212)

Yes

Yes

Yes

Yes

Backlight keyboard keys not working. Only 4GB ram, but works.

[jeff](https://groups.google.com/d/msg/qubes-users/jlvKvKtEiWk/axMMx8St8xIJ)

Clevo P150EM (Sager NP9150)
 (i7-3720QM; HD4000; BIOS 4.6.5)

\*

\*

Yes

\*

Yes

Yes

Most features work on 3.7 and 3.11, but for best results use 3.9.

[​AndrewX192](https://groups.google.com/d/msg/qubes-users/Ol6v6xSla4Y/vFgIHeObF-8J)

Dell Latitude E4300
 (P9600; GM45; GMA 4500MHD, BIOS A24)

\*

No

Yes

No

Yes

Yes

Runs only with kernel 3.9 [​read more](https://groups.google.com/d/topic/qubes-devel/LNJqSbH0cOQ/discussion)

[​Pablo Costa](https://groups.google.com/d/msg/qubes-devel/LNJqSbH0cOQ/VC9EwEDrXMQJ)

Dell Latitude E6420
 (i5-2520M; Sandy Bridge; Intel HD graphics; BIOS A17)

Yes

Yes

Yes

Yes

Yes

Yes

[marmarek (Qubes core developer)](https://groups.google.com/d/msg/qubes-devel/S-leNH8AYsU/WL_XdNAhBkQJ)

Dell Latitude E6430
 (i5-3340M; Ivy Bridge; Intel HD graphics; BIOS A11)

\*

Yes

Yes

Yes

[​Zrubi](https://groups.google.com/d/msg/qubes-users/pAVGe04ZC48/AJwY6yd7LeIJ)

Fujitsu S751
 (i5-2520M; QM67; HD3000; BIOS 1.18)

\*

Yes

Yes

Yes

[​Zrubi](https://groups.google.com/forum/#!msg/qubes-devel/xoyNCigBvFE/ER61L6TbVpwJ)

Lenovo Thinkpad T61
 (Nvidia Quadro NVS 140M)

Yes

Yes

Yes

No

Qubes core developers

Lenovo Thinkpad T410
 (i7-620M; Arrandale; HD graphics, BIOS 6IET74WW (1.34 ))

\*

No

Yes

Yes

Yes

[​Vincent Penquerc'h](https://groups.google.com/d/msg/qubes-users/WsHQ_GqXdT4/63xtC0iqXXEJ)

Lenovo Thinkpad T420s
 (i5-2520M; Sandy Bridge; Intel HD graphics)

Yes

Yes

Yes

Yes

Qubes core developers

Lenovo Thinkpad T430s (2352CTO)
 (i5-3320M; Ivy Bridge; Intel HD graphics; BIOS 2.05)

Yes

Yes

Yes

Yes

[​cprise](https://groups.google.com/d/msg/qubes-users/Ll_pPP7glwI/jtRbKtQO_rMJ)

Lenovo Thinkpad T500
 (P8400; GM45; GMA 4500MHD; BIOS 6FET92WW 3.22)

Yes

Yes

Yes

\*

activated VT-d BIOS option not recognized in Qubes

[​Jens Porup](https://groups.google.com/d/msg/qubes-users/EoG4VffajRw/-oeSfNCA-KIJ)

Lenovo Thinkpad T510
 (i5-520M; Arrandale; Intel HD Graphics; BIOS 6MET92WW 1.52)

\*

No

Yes

No

Yes

Yes

[​pete](https://groups.google.com/d/msg/qubes-users/UP9BK_yn-Pk/DR6PBVF4GlgJ)

Lenovo ThinkPad X220 (4290-W3W)
 (i5-2520M; QM67; HD3000; BIOS 1.39)

Yes

Yes

Yes

Yes

[​Matt Tracy](https://groups.google.com/d/msg/qubes-users/5tNavg4MhT4/dFXsYHXOgu4J)

Lenovo X1 Carbon Gen 2
 (i5-4300U; Haswell-ULT; HD4000; BIOS 1.07)

Yes

Yes

No

No

needs iwl7260-firmware in netvm

[​Patrick Schless](https://groups.google.com/d/msg/qubes-users/cu_mJa4iDHk/v1FdT3ZGofEJ)

Lenovo X1 Carbon Gen 2
 (i7-4600U; Haswell-ULT; HD4000; BIOS 1.11)

Yes

Yes

Yes

Yes

needs iwl7260-firmware in netvm

[​Jean-François Rioux](https://groups.google.com/d/msg/qubes-users/cu_mJa4iDHk/v1FdT3ZGofEJ)

MSI GX660
 (i5-460M; PM55; Radeon HD5870; BIOS E16F1IMS VER1.0L)

Yes

Yes

Yes

No

[​Avant Garden](https://groups.google.com/d/msg/qubes-users/UrWYjkHwon8/TPE0XSBiPDQJ)

Samsung NP300E7A
 (i3-2330M; HM65; HD3000)

Yes

Yes

Yes

No

[​Marc](https://groups.google.com/d/msg/qubes-users/dzYwiYzvWYM/iOyq3V2y5L4J)

Samsung X460
 (P8600; PM45; GeForce 9200M GS; BIOS 06LY.M038.20091110.JIP)

Yes

Yes

Yes

Yes

Yes

No

[marmarek (Qubes core developer)](https://groups.google.com/d/msg/qubes-devel/S-leNH8AYsU/WL_XdNAhBkQJ)

Sony VAIO series Z2 - VPCZ2190S
 (i5-2540M; Sandy Bridge; HD3000; BIOS R0170H5)

Yes

Yes

Yes

\*

BIOS has to be patched to activate VT-d, external Radeon HD 6700M

[​Danny Fullerton](https://groups.google.com/d/msg/qubes-users/8urk8ZNeblg/jCD2iQyQQZwJ)

Sony Vaio Z 12
 (2010 edition)

\*

Yes

Yes

[​read more](/trac/wiki/SonyVaioTinkering)

Qubes core developers

**Desktop, Workstation and Server**

HP Compaq dc7900 Convertible Minitower
 (E8400; Q45/Q43; BIOS 1.16)

\*

No

Yes

No

Yes

Yes

Problem with graphics on 3.11,3.7, only 2GB RAM.

[​Nukama](https://groups.google.com/d/msg/qubes-users/RYzkSFoMsxQ/ukXhBW4ybqQJ)

HP ProLiant DL360 G5
 (E5440; 5000P; ATI ES1000; BIOS P58)

Yes

Yes

Yes

Yes

Yes

No

Some video glitches, no audio hardware.

[​Nukama](https://groups.google.com/d/msg/qubes-users/1CyVEStoVCI/RTRw8-aalsUJ)

Lenovo ThinkCentre M71e
 (G620; H61; HD2000; BIOS 9QKT29AUS)

Yes

Yes

Yes

Yes

Yes

No

[​Nukama](https://groups.google.com/d/msg/qubes-users/YcqMDcVYQh8/pk0B_9RfGQMJ)

**Motherboards**

ASRock Q87M Vpro
 (LGA1150; Q87; BIOS P1.50)

\*

Yes

Yes

Yes

Problems with Power Saving, Audio and USB3

[​suricabile](https://groups.google.com/d/msg/qubes-users/oExJBIDsAwQ/lwAzNNe7OcYJ)

Biostar A880GZ
 (AM3+; 880G/SB850)

\*

\*

Yes

Yes

[\#762](/trac/ticket/762)

[​clewis](https://groups.google.com/d/msg/qubes-users/YcqMDcVYQh8/pk0B_9RfGQMJ)

Biostar TA790GX A3+
 (AM3; 790GX/SB750; BIOS 78DAA420)

\*

\*

Yes

Yes

Yes

No

[\#762](/trac/ticket/762)

EVGA\_E685
 (LGA1150; Z68; BIOS 4.6.4)

\*

Yes

Yes

No

Problems with Audio

[​jeff](https://groups.google.com/d/msg/qubes-users/wSCL-4VL2Ew/cU8-2qyT008J)

Gigabyte GA-X79S-UP5 Wi-Fi
 (LGA2011; C606; BIOS 1.0)

Yes

Yes

VT-d option in BIOS according to [manual](http://download.gigabyte.eu/FileList/Manual/mb-manual_ga-x79s-up5_e.pdf)

Latest Stable Release
---------------------

Qubes R1
========

Device

Standard features

VT-d

Remarks

Reported by

**Developer Reported Machines**

Lenovo Thinkpad T420

OK

OK

Qubes core developers

Lenovo Thinkpad T420s
 (Intel HD graphics; Sandy Bridge; i5-2520M)

OK

OK

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

Qubes core developers

Dell Latitude E6420
 (Intel HD graphics; Sandy Bridge; i5-2520M)

OK

OK

needs kernel 3.4.17+

Qubes core developers

**User Reported Laptops**

ASUS UX-31

\*

[​Stephen Boyd](https://groups.google.com/d/topic/qubes-devel/6I07Bbzn5M4/discussion)

ASUS X55A

X

X

[​read more](https://groups.google.com/d/topic/qubes-devel/2csjvHia9Rw/discussion)

[​Zrubi](https://groups.google.com/d/msg/qubes-devel/2csjvHia9Rw/NRsqR0g6wIMJ)

Dell Latitude 5520

OK

OK

[​read more](https://groups.google.com/group/qubes-devel/msg/7418e7084c2de99f?hl=en)

[​Erik Edin](https://groups.google.com/group/qubes-devel/msg/7418e7084c2de99f?hl=en)

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

[​j](https://groups.google.com/d/msg/qubes-devel/7JumqdldVJM/n9TiDVxc2jkJ)

Fujitsu S751
 (HD3000; QM67; i5-2520M; BIOS 1.18)

OK

OK

[​Zrubi](https://groups.google.com/forum/#!msg/qubes-devel/xoyNCigBvFE/ER61L6TbVpwJ)

Lenovo Thinkpad W510
 (nVidia; i7-Q820)

OK

OK

[​read more](https://groups.google.com/forum/#!msg/qubes-devel/TgDWwBs36yA/IUFZPHs716cJ)

[​Sebastian Hültenschmidt](https://groups.google.com/forum/#!msg/qubes-devel/TgDWwBs36yA/IUFZPHs716cJ)

Lenovo Thinkpad x220
 (Sandy Bridge; HD Graphics; i5-2520M; BIOS: 1.39)

OK

OK

[​Stefan Boresch](https://groups.google.com/group/qubes-devel/msg/f41578eef913446a)

Lenovo Thinkpad x230
 (Ivy Bridge; HD Graphics; i5-3320M; BIOS:2.51)

\*

OK

[​read more](https://groups.google.com/d/msg/qubes-devel/XN6JrEXVOVA/lkxGRA00EqgJ)

[​Chris](https://groups.google.com/d/msg/qubes-devel/XN6JrEXVOVA/lkxGRA00EqgJ)

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

[​read more](https://groups.google.com/d/msg/qubes-devel/0xBeX8NZFiU/bUqxGdn6KOMJ)

[​Outback Dingo](https://groups.google.com/d/msg/qubes-devel/0xBeX8NZFiU/bUqxGdn6KOMJ)

Sony Vaio Z2
 (2011 edition)

OK

OK

[​read more](https://groups.google.com/d/msg/qubes-devel/xoyNCigBvFE/fkC6em-Wqd0J)

[​Danny Fullerton](https://groups.google.com/d/msg/qubes-devel/xoyNCigBvFE/fkC6em-Wqd0J)

**User Reported Desktops and Workstations**

Supermicro X10SAE
 (Haswell; Radeon HD 5700; Xeon E3-1245; BIOS: 1.0)

X

X

[read more](https://groups.google.com/d/topic/qubes-users/V9BLpdf4xCs/discussion)

[Qubes Fan](https://groups.google.com/d/msg/qubes-users/V9BLpdf4xCs/v4XcOjLT6uUJ)

Previous Releases
-----------------

Qubes R2 Beta2
==============

Device

Standard features

VT-x
(HVM)

VT-d

Remarks

Reported by

**Developer Reported Machines**

Lenovo Thinkpad T420s
 (Intel HD graphics; Sandy Bridge; i5-2520M)

OK

OK

OK

Requires kernel 3.2.30 to support S3 sleep (the default kernel S3 sleep causes system reboot)

Qubes core developers

Sony Vaio Z 12
 (2010 edition)

OK

OK

OK

[read more](/trac/wiki/SonyVaioTinkering)

Qubes core developers

Dell Latitude E6420
 (Intel HD graphics; Sandy Bridge; i5-2520M)

OK

OK

OK

Suspend doesn't work on 3.7.6 kernel, but work on 3.7.4

Qubes core developers

**User Reported Laptops**

Apple MacBookPro
 (i7 M620)

X

OK

X

[​read more](https://groups.google.com/d/topic/qubes-devel/hag-MQDH_Vs/discussion)

[​Alex Dubois](https://groups.google.com/d/msg/qubes-devel/hag-MQDH_Vs/pmJ7TIWUWAsJ)

Apple MacBookPro
 (Intel HD Graphics, Ivy Bridge, i5-3210M)

X

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-users/ZbjrseLxuPQ/discussion)

[​ph145h](https://groups.google.com/d/msg/qubes-users/ZbjrseLxuPQ/5Jx5DvpnwMMJ)

ASUS X55A

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

Dell XPS 13
 (i5; intel HD; sandy bridge; BIOS A03)

OK

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

needs kernel downgrade to 3.7.4

[​Zrubi](https://groups.google.com/forum/#!msg/qubes-devel/xoyNCigBvFE/ER61L6TbVpwJ)

HP EliteBook 8540p
 (Arrandale; NVIDIA GT216; i5-2540M; BIOS:F.0C)

OK

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-users/o_FTsPW6GD8/discussion)

[Olivier Médoc](https://groups.google.com/d/msg/qubes-users/o_FTsPW6GD8/bjAD-CSpRKsJ)

HP EliteBook 8560p
 (Sandy Bridge; ATI Caicos; i5-2540M; BIOS: F.08)

\*

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-users/o_FTsPW6GD8/discussion)

[Olivier Médoc](https://groups.google.com/d/msg/qubes-users/o_FTsPW6GD8/bjAD-CSpRKsJ)

HP Pavilion Sleekbook 14-B030TU
 (Ivy Bridge; Intel HD Graphics; i5-3317; BIOS F.06)

OK

OK

OK

[Stephen Boyd](https://groups.google.com/d/msg/qubes-devel/ZC_SQJhXVOM/4aLjEc7GIsUJ)

Lenovo Thinkpad Edge E130
 (Ivy Bridge; HD Graphics i3-3217U; BIOS: 2.05)

OK

OK

OK

[Danny Cautaert](https://groups.google.com/d/msg/qubes-devel/kGnZKZ9ILKA/2vpzltNW3K4J)

Lenovo Thinkpad T430
 (Ivy Bridge; HD Graphics; i5-3360M; BIOS: 2.51)

OK

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-devel/LSVluAZ9Udo/discussion)

[Alex Dubois](https://groups.google.com/d/msg/qubes-devel/LSVluAZ9Udo/Fl3jmt4tWssJ)

Lenovo Thinkpad T430s
 (i5-3320M)

OK

OK

OK

[read more](https://groups.google.com/d/topic/qubes-users/V4PQYEBuoSg/discussion)

[cprise](https://groups.google.com/d/msg/qubes-users/V4PQYEBuoSg/udLCHyR6RUUJ)

Lenovo Thinkpad T430U
 (Ivy Bridge; HD Graphics +GT 620M; i7-3517M; BIOS: 2.08)

OK

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-devel/Z9M_k3i6dxU/discussion)

[tigerbeard](https://groups.google.com/d/msg/qubes-devel/Z9M_k3i6dxU/09CqBppyMnsJ)

Lenovo Thinkpad X1 Carbon (LENOVO 3444CTO)
 (i5-3427U)

OK

OK

[Ulrich Pfeifer](https://groups.google.com/d/msg/qubes-users/UCuF41rq758/BRhc7lTecsMJ)

Lenovo Thinkpad x220
 (Sandy Bridge; HD Graphics; i5-2520M; BIOS: 1.39)

OK

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-users/-b8b9fpo0UU/discussion)

[​Stefan Boresch](https://groups.google.com/group/qubes-devel/msg/f41578eef913446a)
 [​Matt Tracy](https://groups.google.com/d/msg/qubes-users/-b8b9fpo0UU/RFh6HiWqt5oJ)

Lenovo Thinkpad x230
 (Ivy Bridge; HD Graphics; i5-3320M; BIOS:2.51)

\*

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-users/hf0vkL3TE7k/discussion)

[​Chris](https://groups.google.com/d/msg/qubes-devel/XN6JrEXVOVA/lkxGRA00EqgJ)
 [​mgflax](https://groups.google.com/d/msg/qubes-users/hf0vkL3TE7k/VOtrW3wEbtMJ)

Samsung Series 7 Chronos NP700Z5C
 (nVidia Optimus; i7-3635QM; BIOS P04ABJ)

OK

OK

X

[​read more](https://groups.google.com/d/topic/qubes-devel/Wu1mn9f1qgM/discussion)

[​Outback Dingo](https://groups.google.com/d/msg/qubes-devel/0xBeX8NZFiU/bUqxGdn6KOMJ)

Zareason Ultra Lap 420
 (Ivy Bridge; HD Graphics; i5-3317U)

OK

OK

[​Ant](https://groups.google.com/d/msg/qubes-users/uKI-VBtKWxg/uKjsdGNSpSQJ)

**User Reported Desktops and Workstations**

ASRock Z77 Pro4
 (Ivy Bridge; Xeon E3-1200 Graphics; i7-3770; BIOS: P1.40)

OK

OK

OK

[read more](https://groups.google.com/d/topic/qubes-users/lycnE-LcJBo/discussion)

[gorka](https://groups.google.com/d/msg/qubes-users/lycnE-LcJBo/0u10xl7AMrIJ)

Dell Inspiron 660
 (Xeon E3-1200 Graphics; i5-3330; BIOS: A09)

OK

OK

OK

[read more](https://groups.google.com/d/topic/qubes-users/Nq7T0l4A2b0/discussion)

[KR](https://groups.google.com/d/msg/qubes-users/Nq7T0l4A2b0/IP_pwZMn9LYJ)

Dell Precision T3400 Workstation
 (NVIDIA Quadro NVS 290; Intel Q6600; BIOS: A09)

OK

OK

X

[Andrew Sorensen](https://groups.google.com/d/msg/qubes-devel/D16dM3rg8Iw/zOEZmjTJkRIJ)

GA-fxa990-ud3 (rev 3.0)
 (AMD FX-8350; GTX 470)

OK

OK

X

[m astroj](https://groups.google.com/d/msg/qubes-devel/oox94EsIduQ/7w4xUoK5pxwJ)

MSI Big Bang
 (i7-950; Radeon HD 6770)

OK

[read more](https://groups.google.com/d/topic/qubes-devel/TxzaoodB02o/discussion)

[Andrew Sorensen](https://groups.google.com/d/msg/qubes-devel/TxzaoodB02o/NxVHjaPoRYoJ)

Supermicro X10SAE
 (Haswell; Radeon HD 5700; Xeon E3-1245; BIOS: 1.0)

OK

OK

X

[read more](https://groups.google.com/d/topic/qubes-users/V9BLpdf4xCs/discussion)

[Qubes Fan](https://groups.google.com/d/msg/qubes-users/V9BLpdf4xCs/v4XcOjLT6uUJ)

Qubes R2 Beta1
==============

Device

Standard features

VT-x
(HVM)

VT-d

Remarks

Reported by

**Developer Reported Machines**

Lenovo Thinkpad T420

OK

OK

OK

AEM works

Qubes core developers

Lenovo Thinkpad T420s

OK

OK

OK

AEM works

Qubes core developers

Lenovo Thinkpad T61
 (Nvidia Quadro NVS 140M)

OK

OK

X

Qubes core developers

Samsung X460

OK

OK

X

Qubes core developers

Sony Vaio Z 12
 (2010 edition)

OK

OK

OK

[​read more](/trac/wiki/SonyVaioTinkering)

Qubes core developers

Dell Latitude E6420
 (Intel HD graphics; Sandy Bridge; i5-2520M)

OK

OK

OK

needs kernel 3.4.17+

Qubes core developers

**User Reported Machines**

ASUS UX-31

\*

[​read more](https://groups.google.com/d/topic/qubes-devel/6I07Bbzn5M4/discussion)

[​Stephen Boyd](https://groups.google.com/d/topic/qubes-devel/6I07Bbzn5M4/discussion)

Dell XPS 13
 (i5; intel HD; sandy bridge; BIOS A03)

OK

[​read more](https://groups.google.com/d/msg/qubes-devel/7JumqdldVJM/n9TiDVxc2jkJ)

[​j](https://groups.google.com/d/msg/qubes-devel/7JumqdldVJM/n9TiDVxc2jkJ)

Fujitsu S751
 (HD3000; QM67; i5-2520M; BIOS 1.18)

OK

OK

OK

[​Zrubi](https://groups.google.com/forum/#!msg/qubes-devel/xoyNCigBvFE/ER61L6TbVpwJ)

HP Pavilion Sleekbook 14-B030TU
 (i5-3317U; BIOS F.06)

OK

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-devel/ZC_SQJhXVOM/discussion)

[​Stephen Boyd](https://groups.google.com/d/msg/qubes-devel/ZC_SQJhXVOM/4aLjEc7GIsUJ)

Lenovo Thinkpad T430
 (i5-3320)

OK

OK

OK

[​Tunguuz](https://groups.google.com/d/msg/qubes-devel/S_VG_jgtpBo/VngCPK2W5FcJ)

Lenovo Thinkpad T430s
 (i5-3320M; HD4000; QM77; BIOS 2.05)

OK

OK

OK

[​read more](https://groups.google.com/d/topic/qubes-devel/Z9seyOT46Ro/discussion)

[​cprise](https://groups.google.com/d/msg/qubes-devel/Z9seyOT46Ro/wX6tsrxE84sJ)

Lenovo Thinkpad X61t

OK

[​George Walker](https://groups.google.com/d/msg/qubes-devel/4IrF1A6sa3U/QIQe-dNc4tEJ)

Samsung Series 7 Chronos NP700Z5C
 (nVidia Optimus; i7-3635QM; BIOS P04ABJ)

OK

OK

OK

[​read more](https://groups.google.com/d/msg/qubes-devel/0xBeX8NZFiU/bUqxGdn6KOMJ)

[​Outback Dingo](https://groups.google.com/d/msg/qubes-devel/0xBeX8NZFiU/bUqxGdn6KOMJ)


