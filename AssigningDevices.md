---
layout: wiki
title: AssigningDevices
permalink: /wiki/AssigningDevices/
---

In order to assign a whole PCI/e device to a VM one should use ```qvm-pci``` tool. E.g.

``` {.wiki}
lspci
```

Find the BDF address of the device you want to assign, and then:

``` {.wiki}
qvm-pci -a <vmname> <bdf>
```

E.g. assuming 00:1a.0 is a BDF of the device I want to assign to "personal" domain:

``` {.wiki}
qvm-pci -a personal 00:1a.0
```

Note that one can only assign full PCI or PCI Express devices. This means one cannot assign single USB devices -- only the whole USB controller with whatever USB devices connected to it. This limit is imposed by PC and VT-d architecture.

Using Qubes Manager
-------------------

TODO

\<screenshot\>

Possible issues
---------------

VM with PCI device in Qubes have allocated small buffer for DMA operations (called swiotlb). By default it is 2MB, but some devices needs a larger space. To change this allocation, edit VM kernel parameters (this is expressed in 512B chunks):

``` {.wiki}
# qvm-prefs netvm |grep kernelopts
kernelopts       : iommu=soft swiotlb=2048 (default)
# qvm-prefs -s netvm kernelopts "iommu=soft swiotlb=4096"
```

This is [​know to be needed](https://groups.google.com/group/qubes-devel/browse_thread/thread/631c4a3a9d1186e3) for Realtek RTL8111DL Gigabit Ethernet Controller.
