---
layout: wiki
title: ResizeDiskImage
permalink: /wiki/ResizeDiskImage/
---

Resizing Disk Image
-------------------

There are several disk images which can be easily extended.
 But pay attention to the overall consumed space of your sparse disk images.

### Private disk image

1048576 MB is the maximum size which can be assigned to a private storage through qubes-manager.

To grow the private disk image of a AppVM beyond this limit [qubes-grow-private](/wiki/Dom0Tools/QvmGrowPrivate) can be used:

``` {.wiki}
qvm-grow-private <vm-name> <size>
```

### HVM disk image

In this example we will grow the disk image of an HVM to 30GB.

First, stop/shutdown the HVM.

Then, from a Dom0 terminal (in KDE: System Tools -\> Terminal Emulator) do the following:

``` {.wiki}
cd /var/lib/qubes/appvms/<yourHVM>/
ls -lh root.img  (<--verify current size of disk image)
truncate -s 30GB root.img
ls -lh root.img  (<--verify new size of disk image)
```

The partition table and file-system must be adjusted after this change:

#### Windows 7

1.  Click Start
2.  type "diskmgmt.msc" - this takes you to Disk Management
3.  Right-click on your existing volume, select "Extend Volume..."
4.  Click through the wizard.

No reboot required.

#### FreeBSD

``` {.wiki}
gpart recover ada0
sysctl kern.geom.debugflags=0x10
gpart resize -i index ada0
zpool online -e poolname ada0
```
