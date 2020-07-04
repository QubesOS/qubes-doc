---
layout: doc
title: Intel Integrated Graphics Troubleshooting
permalink: /doc/intel-igfx-troubleshooting/
---
# Intel Integrated Graphics Troubleshooting #

## Software Rendering or Video Lags

If you are experiencing this issue, you will see extremely slow graphics updates.
You will be able to watch the screen and elements paint slowly from top to bottom.
You can confirm this is the issue by looking for a line similar to the following in your `/var/log/Xorg.0.log` file:

    [   131.769] (EE) AIGLX: reverting to software rendering

Newer versions of the Linux kernel have renamed the `i915.preliminary_hw_support=1` option to `i915.alpha_support=1`, so if you needed this kernel option in the past you will have to rename it or add it to your configuration files (follow either GRUB2 or EFI, not both):

 * GRUB2: `/etc/default/grub`, `GRUB_CMDLINE_LINUX` line and  
   Rebuild grub config (`grub2-mkconfig -o /boot/grub2/grub.cfg`)   
 * EFI: `/boot/efi/EFI/PedOS/xen.cfg`, `kernel=` line(s)


## IOMMU ##

Dom0 Kernels currently included in PedOS have issues related to VT-d (IOMMU) and some versions of the integrated Intel Graphics Chip.
Depending on the specific hardware / software combination the issues are quite wide ranging, from apparently harmless log errors, to VM window refresh issues, to complete screen corruption and crashes rendering the machine unusable with PedOS.

Such issues have been reported on at least the following machines:

* HP Elitebook 2540p
* Lenovo x201
* Lenovo x220
* Thinkpad T410
* Thinkpad T450s

Log errors only on :
* Librem 13v1 
* Librem 15v2

The installer for PedOS 4.0 final has been updated to disable IOMMU for the integrated intel graphics by default.
However, users of 3.2 may experience issues on install or on kernel upgrades to versions higher than 3.18.x.

Disabling IOMMU for the integrated graphics chip is not a security issue, as the device currently lives in dom0 and is not passed to a VM.
This behaviour is planned to be changed as of PedOS 4.1, when passthrough capabilities will be required for the GUI domain <sup id="a1-1">[1](#f1)</sup>.


## Workaround for existing systems with VT-d enabled (grub / legacy mode) ##

Edit the startup parameters for Xen:

1. Open a terminal in dom0
2. Edit `/etc/default/grub` (e.g. `sudo nano /etc/default/grub`)
3. Add to the line `GRUB_CMDLINE_XEN_DEFAULT` the setting `iommu=no-igfx`, save and quit
4. Commit the change with`sudo grub2-mkconfig --output /boot/grub2/grub.cfg`

## Workaround for existing systems with VT-d enabled (UEFI) ##

Edit the startup parameters for Xen:

1. Open a terminal in dom0
2. Edit `/boot/efi/EFI/PedOS/xen.cfg` (e.g. `sudo nano /boot/efi/EFI/PedOS/xen.cfg`)
3. Add to the line `options` the setting `iommu=no-igfx`, save and quit

<b name="f1">1</b> <https://github.com/PedOS/PedOS-issues/issues/2841> [↩](#a1-1)

