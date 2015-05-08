---
layout: doc
title: LinuxHVMTips
permalink: /doc/LinuxHVMTips/
redirect_from: /wiki/LinuxHVMTips/
---

Tips for Linux in HVM domain
============================

Screen resolution
-----------------

Some kernel/Xorg combination use only 640x480 in HVM, which is quite small. To enable maximum resolution, some changes in Xorg configuration are needed:

1.  Force "vesa" video driver
2.  Provide wide horizontal synchronization range

To achieve it (all commands run as root):

1.  Generate XOrg configuratio (if you don't have it):

    {% highlight trac-wiki %}
    X -configure :1 && mv ~/xorg.conf.new /etc/X11/xorg.conf
    {% endhighlight %}

2.  Add [HorizSync?](/wiki/HorizSync) line to Monitor section, it should look something like:

    {% highlight trac-wiki %}
    Section "Monitor"
            Identifier   "Monitor0"
            VendorName   "Monitor Vendor"
            ModelName    "Monitor Model"
            HorizSync    30.0 - 60.0
    EndSection
    {% endhighlight %}

3.  Change driver to "vesa" in Device section:

    {% highlight trac-wiki %}
    Section "Device"
            # (...)
            Identifier  "Card0"
            Driver      "vesa"
            VendorName  "Technical Corp."
            BoardName   "Unknown Board"
            BusID       "PCI:0:2:0"
    EndSection
    {% endhighlight %}

Now you should get at least 1280x1024 and be able to choose other modes.

Qubes agents
------------

Linux Qubes agents are written with PV domain in mind, but it looks to be possible to run them also in HVM domain. However some work is required to achieve it. Check [this thread](https://groups.google.com/group/qubes-devel/browse_thread/thread/081df4a43e49e7a5).
