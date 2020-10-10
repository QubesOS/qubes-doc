---
layout: doc
title: Linux HVM Tips
permalink: /doc/linux-hvm-tips/
redirect_from:
- /en/doc/linux-hvm-tips/
- /doc/LinuxHVMTips/
- /wiki/LinuxHVMTips/
---

Tips for Linux in HVM domain
============================

How to fix bootup kernel error 
-------------------------------

If the HVM pauses on boot and shows a series of warnings, visit [HVM Troubleshooting](/doc/hvm-troubleshooting/#hvm-pauses-on-boot-followed-by-kernel-error) for a fix. 

Screen resolution
-----------------

Some kernel/Xorg combinations use only 640x480 in HVM, which is quite small. 
To enable maximum resolution, some changes in the Xorg configuration are needed:
1.  Force "vesa" video driver
2.  Provide wide horizontal synchronization range

To achieve it (all commands to be run as root):

1.  Generate XOrg configuration (if you don't have it):
    ~~~
    X -configure :1 && mv ~/xorg.conf.new /etc/X11/xorg.conf
    ~~~

1.  Add HorizSync line to Monitor section, it should look something like:
    ~~~
    Section "Monitor"
            Identifier   "Monitor0"
            VendorName   "Monitor Vendor"
            ModelName    "Monitor Model"
            HorizSync    30.0 - 60.0
    EndSection
    ~~~

1.  Change driver to "vesa" in Device section:
    ~~~
    Section "Device"
            # (...)
            Identifier  "Card0"
            Driver      "vesa"
            VendorName  "Technical Corp."
            BoardName   "Unknown Board"
            BusID       "PCI:0:2:0"
    EndSection
    ~~~

Now you should get resolution of at least 1280x1024 and should be able to choose other modes.

Qubes agents
------------

Linux Qubes agents are written primarily for PV qubes, but it is possible to run them also in a HVM qube.
However some work may be required to achieve this. Check [this thread](https://groups.google.com/group/qubes-devel/browse_thread/thread/081df4a43e49e7a5).
