---
lang: en
layout: doc
permalink: /doc/windows/
ref: 129
title: Windows qubes
---

Like any other unmodified OSes, Windows can be installed in Qubes as an [HVM](/doc/standalone-and-hvm/) domain.

Qubes Windows Tools are then usually installed to provide integration with the rest of the Qubes system; they also include Xen's paravirtualized (PV) drivers to increase performance compared to qemu emulated devices. Alternatively, only Xen's PV drivers can be installed if integration with Qubes isn't required or if the tools aren't supported on a given version of Windows. In the latter case, one would have to [enable inter-VM networking](/doc/firewall/#enabling-networking-between-two-qubes) to be able to exchange files with HVMs.

For more information about Windows VMs in Qubes OS, please see the following external resources:

* [Installing and Using Windows-based VMs in Qubes R4.0 and earlier](https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows-vm.md)
* [Installing and Using Qubes Windows Tools in Qubes R4.0 and earlier](https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows-tools.md)
* [Installing and Using Windows-based VMs in Qubes R4.1](https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows-vm41.md)
* [Installing and Using Qubes Windows Tools in Qubes R4.1](https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows-tools41.md)
* [Migrate backups of Windows VMs created under Qubes R4.0 to R4.1](https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows-migrate41.md)
