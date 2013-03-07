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

The private disk image of a AppVM can be grown with [qubes-grow-private](/wiki/Dom0Tools/QvmGrowPrivate):

``` {.wiki}
qvm-grow-private <vm-name> <size>
```

### HVM disk image

A disk image for a HVM for can be grown using following command:

``` {.wiki}
truncate -s <size> root.img
```

The root.img is found in /var/lib/qubes/appvm/hvmname.

Be aware, that the HVM should be stopped during this operation. The partition table and file-system must be adjusted after this change.

#### Windows

Go to Storage management and click on "Extend Volume"

#### FreeBSD

``` {.wiki}
gpart recover ada0
sysctl kern.geom.debugflags=0x10
gpart resize -i index ada0
zpool online -e poolname ada0
```
