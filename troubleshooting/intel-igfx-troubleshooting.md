---
layout: doc
title: Intel Integrated Graphics Troubleshooting
permalink: /doc/intel-igfx-troubleshooting/
---
# Intel Integrated Graphics Troubleshooting #

Dom0 Kernels currently included in Qubes have issues related to VT-d (IOMMU) and some versions of the
integrated Intel Graphics Chip. Depending on the specific hardware / software combination the issues are quite wide ranging, from apparently harmless log errors, to VM window refresh issues,
to complete screen corruption and crashes rendering the machine unusable with Qubes.

Such issues have been reported on at least the following machines:

* HP Elitebook 2540p
* Lenovo x201
* Lenovo x220
* Thinkpad T410
* Thinkpad T450s

Log errors only on :
* Librem 13v1 
* Librem 15v2

The installer for Qubes 4.0 final has been updated to disable IOMMU for the integrated intel graphics by default. However, users of 3.2 may experience
issues on install or on kernel upgrades to versions higher than 3.18.x 

Disabling of IOMMU for the integrated graphics chip is not a security issue, as the
device currently lives in dom0 and is not passed to a VM. This behaviour is planned to be changed as of Qubes 4.1, when passthrough capabilities will be required for the GUI domain <sup id="a1-1">[1](#f1)</sup>


## Workaround for existing systems with VT-d enabled (grub / legacy mode) ##

Edit the startup parameters for Xen:

1. Open a terminal in dom0
2. Edit `/etc/default/grub` (e.g. `sudo nano /etc/default/grub`)
3. Add to the line `GRUB_CMDLINE_XEN_DEFAULT` the setting `iommu=no-igfx`, save and quit
4. Commit the change with`sudo grub2-mkconfig --output /boot/grub2/grub.cfg`

## Workaround for existing systems with VT-d enabled (UEFI) ##

Edit the startup parameters for Xen:

1. Open a terminal in dom0
2. Edit `/boot/efi/EFI/qubes/xen.cfg` (e.g. `sudo nano /boot/efi/EFI/qubes/xen.cfg`)
3. Add to the line `options` the setting `iommu=no-igfx`, save and quit

<b name="f1">1</b> https://github.com/QubesOS/qubes-issues/issues/2841 [↩](#a1-1)

