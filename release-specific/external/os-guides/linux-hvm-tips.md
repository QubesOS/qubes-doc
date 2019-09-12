---
layout: doc
title: Linux HVM Tips
redirect_from:
- /doc/linux-hvm-tips/
- /en/doc/linux-hvm-tips/
- /doc/LinuxHVMTips/
- /wiki/LinuxHVMTips/
---

Tips for Linux in HVM domain
============================

How to fix bootup kernel error 
-------------------------------

The HVM may pause on boot, showing a fixed cursor.
After a while a series of warnings may be shown similar to this:

    BUG: soft lockup - CPU#0 stuck for 23s! [systemd-udevd:244]

To fix this:

1.  Kill the HVM.
1.  Start the HVM
1.  Press "e" at the grub screen to edit the boot parameters
1.  Find the /vmlinuz line, and edit it to replace "rhgb" with "modprobe.blacklist=bochs_drm"
1.  Press "Ctrl-x" to start the HVM

If this solves the problem then you will want to make the change permanent:

1.  Edit the file `/etc/default/grub`.
1.  Find the line which starts:
    ~~~
    GRUB_CMDLINE_LINUX=
    ~~~
1.  Remove this text from that line:
    ~~~
    rhgb
    ~~~
1.  Add this text to that line:
    ~~~
    modprobe.blacklist=bochs_drm
    ~~~
1.  Run this command:
    ~~~
    grub2-mkconfig --output=/boot/grub2/grub.cfg
    ~~~

The HVM should now start normally.


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
