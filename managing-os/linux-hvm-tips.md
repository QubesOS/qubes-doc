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

Screen resolution
-----------------

Some kernel/Xorg combination use only 640x480 in HVM, which is quite small. To enable maximum resolution, some changes in Xorg configuration are needed:

1.  Force "vesa" video driver
2.  Provide wide horizontal synchronization range

To achieve it (all commands run as root):

1.  Generate XOrg configuration (if you don't have it):

    ~~~
    X -configure :1 && mv ~/xorg.conf.new /etc/X11/xorg.conf
    ~~~

2.  Add HorizSync line to Monitor section, it should look something like:

    ~~~
    Section "Monitor"
            Identifier   "Monitor0"
            VendorName   "Monitor Vendor"
            ModelName    "Monitor Model"
            HorizSync    30.0 - 60.0
    EndSection
    ~~~

3.  Change driver to "vesa" in Device section:

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

Now you should get at least 1280x1024 and be able to choose other modes.

Qubes agents
------------

Linux Qubes agents are written with PV domain in mind, but it looks to be possible to run them also in HVM domain. However some work is required to achieve it. Check [this thread](https://groups.google.com/group/qubes-devel/browse_thread/thread/081df4a43e49e7a5).
