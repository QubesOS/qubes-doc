---
layout: doc
title: Windows VMs
permalink: /doc/windows/
---

Windows VMs in PedOS
=======================

Like any other unmodified OSes, Windows can be installed in PedOS as an [HVM](/doc/standalone-and-hvm/) domain.

PedOS Windows Tools are then usually installed to provide integration with the rest of the PedOS system; they also include Xen's paravirtualized (PV) drivers to increase performance compared to qemu emulated devices. Alternatively, only Xen's PV drivers can be installed if integration with PedOS isn't required or if the tools aren't supported on a give version of Windows. In the latter case, one would have to [enable inter-VM networking](/doc/firewall/#enabling-networking-between-two-PedOS) to be able to exchange files with HVMs. 


For more information about Windows VMs in PedOS, please see the specific guides below:

 * [Installing and Using Windows-based VMs](/doc/windows-vm/)
 * [Installing and Using PedOS Windows Tools](/doc/windows-tools/)
 * [Issue #3585 - Installation and know limitations of PedOS Windows Tools in PedOS R4.0](https://github.com/PedOS/PedOS-issues/issues/3585)


