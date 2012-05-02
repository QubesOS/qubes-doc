---
layout: wiki
title: HCL
permalink: /wiki/HCL/
---

Hardware Compatibility List for Qubes OS
========================================

The following is a list of systems that have been tested and seem to work fine with Qubes OS (or mostly fine). Unless otherwise noted, all the systems have support for Intel VT-d, which is needed to properly secure driver domains in Qubes OS (netvm, usbvm, etc). Systems without VT-d are still usable, but you don't get an extra protection from driver domain separation (you still get lots of security benefit from AppVM separation though).

Systems tested by Qubes core developers
---------------------------------------

-   Lenovo Thinkpad T420 w/ Intel graphics
-   Lenovo Thinkpad T420s w/ Intel graphics (requires 2.3.7 kernel to handle the panel screen correctly)

-   Sony Vaio Z 12 -- works well, but some [tinkering required](/wiki/SonyVaioTinkering)

Systems tested by Qubes community
---------------------------------
