---
layout: doc
title: USBVM
permalink: /doc/USBVM/
redirect_from: /wiki/USBVM/
---

USB Pass through: USBVM
-----------------------

**WARNING:** This is experimental and very broken.

Source: [https://groups.google.com/d/msg/qubes-devel/4AKulABh2Jc/\_R7SRSC4peYJ](https://groups.google.com/d/msg/qubes-devel/4AKulABh2Jc/_R7SRSC4peYJ)

You'll need the patch tagged abb\_e58b432 from [git://github.com/grwl/qubes-core.git](git://github.com/grwl/qubes-core.git).

The rest is in RPMs, yes. I roughly follow this procedure to have pvusb on Qubes 1.0:

-   rebuild kernel, core, and xen from marmarek's repo (devel-3.4 branch for kernel),
-   make dedicated usbvm domain, passthrough USB controller PCI devices there
-   in usbvm: "rpm -Uhv qubes-core-vm-2.1.1-1.fc17.x86\_64.rpm xen-libs-2000:4.1.3-18.fc17.x86\_64.rpm xen-qubes-vm-essentials-2000:4.1.3-18.fc17.x86\_64.rpm"
-   in appvm where you want to attach the device to: "rpm -Uhv qubes-core-vm-2.1.1-1.fc17.x86\_64.rpm"
-   in dom0 I think the following packages need to be updated, don't have exact list now.qubes-core-dom0 is actually important, the rest are dependencies:

> kernel-qubes-vm-3.4.18-1.pvops.qubes.x86\_64.rpm
>  qubes-core-dom0-2.1.1-1.fc13.x86\_64.rpm
>  xen-4.1.3-18.fc13.x86\_64.rpm
>  xen-hvm-4.1.3gui2.0.9-18.fc13.x86\_64.rpm
>  xen-hypervisor-4.1.3-18.fc13.x86\_64.rpm
>  xen-libs-4.1.3-18.fc13.x86\_64.rpm
>  xen-licenses-4.1.3-18.fc13.x86\_64.rpm
>  xen-runtime-4.1.3-18.fc13.x86\_64.rpm

-   plug or replug some USB device -- it will be picked up by usbvm, and in dom0 it will appear in the output of qvm-usb

