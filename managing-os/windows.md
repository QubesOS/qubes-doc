---
layout: doc
title: Windows VMs
permalink: /doc/windows/
---

Windows VMs in Qubes OS
=======================

Like any other unmodified OSes, Windows can be installed in Qubes as an [HVM](/doc/hvm/) domain.

Qubes Windows Tools are then usually installed to provide integration with the rest of the Qubes system; they also include Xen's paravirtualized (PV) drivers to increase performance compared to qemu emulated devices. Alternatively, only Xen's PV drivers can be installed if integration with Qubes isn't required or if the tools aren't supported on a give version of Windows. In the latter case, one would have to [enable inter-VM networking](https://www.qubes-os.org/doc/firewall/#enabling-networking-between-two-qubes) to be able to exchange files with HVMs. 


For more information about Windows VMs in Qubes OS, please see the specific guides below:

 * [Installing and Using Windows-based VMs](/doc/windows-vm/)
 * [Installing and Using Qubes Windows Tools (Qubes R2 Beta 3 up to R3.2)](/doc/windows-tools/)
 * [Issue #3585 - Installation and know limitations of Qubes Windows Tools in Qubes R4.0](https://github.com/QubesOS/qubes-issues/issues/3585)
 * [Advanced options and troubleshooting of Qubes Tools for Windows (R3)](/doc/windows-tools-3/)
 * [Advanced options and troubleshooting of Qubes Tools for Windows (R2)](/doc/windows-tools-2/)
 * [Uninstalling Qubes Tools for Windows 2.x](/doc/uninstalling-windows-tools-2/)


