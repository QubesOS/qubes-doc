---
layout: wiki
title: UsbInstallation
permalink: /wiki/UsbInstallation/
---

How to create a bootable USB stick from Qubes ISO
=================================================

Qubes ISO image is already prepared to boot from USB disk, you just need to copy the ISO onto the USB device, e.g. using dd:

``` {.wiki}
dd if=Qubes-R2-Beta2-x86_64-DVD.iso of=/dev/sdX
```

**Be sure to use a correct device as the target in the dd command above (instead of sdX)**
