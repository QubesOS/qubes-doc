---
lang: en
layout: doc
permalink: /doc/templates/windows/
redirect_from:
- /doc/windows/
title: Windows qubes
---

Like any other unmodified OSes, Windows can be installed in Qubes as an [HVM](/doc/standalones-and-hvms/) domain.

Qubes Windows Tools (QWT) are then usually installed to provide integration with the rest of the Qubes system; they also include Xen's paravirtualized (PV) drivers to increase performance compared to qemu emulated devices. Alternatively, only Xen's PV drivers can be installed if integration with Qubes isn't required or if the tools aren't supported on a given version of Windows. In the latter case, one would have to [enable inter-VM networking](/doc/firewall/#enabling-networking-between-two-qubes) to be able to exchange files with HVMs.

For more information about Windows VMs in Qubes OS, please see the following external resources:

* [Installing and Using Windows-based VMs](/doc/templates/windows/windows-qubes-4-1/)
* [Installing and Using Qubes Windows Tools](/doc/templates/windows/qubes-windows-tools-4-1/)
* [Create a Gaming HVM in Qubes](https://forum.qubes-os.org/t/create-a-gaming-hvm/19000)
* [Migrate backups of Windows VMs created under Qubes R4.0 to R4.1](/doc/templates/windows/migrate-to-4-1/)
