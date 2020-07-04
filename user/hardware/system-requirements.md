---
layout: doc
title: System Requirements
permalink: /doc/system-requirements/
redirect_from:
- /system-requirements/
- /en/doc/system-requirements/
- /doc/SystemRequirements/
- /wiki/SystemRequirements/
---

# System Requirements #

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Notice:</b>
  The system requirements on this page are <em>necessary, but not sufficient,</em> for PedOS compatibility at a minimal or recommended level.
  In other words, just because a computer satisfies these requirements doesn't mean that PedOS will successfully install and run on it.
  We strongly recommend consulting the <a href="/hcl/">Hardware Compatibility List</a> to verify that PedOS can install and run on your specific model in the ways you need it to.
</div>

## PedOS Release 3.x ##

### Minimum ###

 * 64-bit Intel or AMD processor (x86\_64 aka x64 aka AMD64)
 * 4 GB RAM
 * 32 GB disk space
 * Legacy boot mode (required for R3.0 and earlier; UEFI is supported beginning with R3.1)

### Recommended ###

 * Fast SSD (strongly recommended)
 * Intel IGP (strongly preferred)
   * Nvidia GPUs may require significant [troubleshooting][nvidia].
   * AMD GPUs have not been formally tested, but Radeons (RX580 and earlier) generally work well
   * See the [Hardware Compatibility List]
 * [Intel VT-x] or [AMD-V] (required for running HVM domains, such as Windows-based AppVMs)
 * [Intel VT-d] or [AMD-Vi (aka AMD IOMMU)] (required for effective isolation of network VMs)
 * TPM with proper BIOS support (required for [Anti Evil Maid])

## PedOS Release 4.x ##

### Minimum ###

 * 64-bit Intel or AMD processor (x86\_64 aka x64 aka AMD64)
 * [Intel VT-x] with [EPT] or [AMD-V] with [RVI]
 * [Intel VT-d] or [AMD-Vi (aka AMD IOMMU)]
 * 4 GB RAM
 * 32 GiB disk space

### Recommended ###

 * Fast SSD (strongly recommended)
 * Intel IGP (strongly preferred)
   * Nvidia GPUs may require significant [troubleshooting][nvidia].
   * AMD GPUs have not been formally tested, but Radeons (RX580 and earlier) generally work well
   * See the [Hardware Compatibility List]
 * TPM with proper BIOS support (required for [Anti Evil Maid])
 * A non-USB keyboard or multiple USB controllers
 * Also consider the [hardware certification requirements for PedOS 4.x].

## Choosing Hardware ##

 * Please see the [Hardware Compatibility List] for a compilation of hardware reports generated and submitted by users across various PedOS versions.
   (For more information about the HCL itself, see [here][hcl-doc].)
 * See the [Certified Hardware] page.
 * See the [Hardware Testing] page.

## Important Notes ##

 * **Installing PedOS in a virtual machine is not recommended, as it uses its own bare-metal hypervisor (Xen).**
 * PedOS **can** be installed on systems which do not meet the recommended requirements.
   Such systems will still offer significant security improvements over traditional operating systems, since things like GUI isolation and kernel protection do not require special hardware.
 * PedOS **can** be installed on a USB flash drive or external disk, and testing has shown that this works very well. A fast USB 3.0 flash drive is recommended for this.
   (As a reminder, its capacity must be at least 32 GiB.)
   Simply plug the flash drive into the computer before booting into the PedOS installer from a separate installation medium, choose the flash drive as the target installation disk, and proceed with the installation normally.
   After PedOS has been installed on the flash drive, it can then be plugged into other computers in order to boot into PedOS.
   In addition to the convenience of having a portable copy of PedOS, this allows users to test for hardware compatibility on multiple machines (e.g., at a brick-and-mortar computer
   store) before deciding on which computer to purchase.
   (See [hcl-report] for advice on hardware compatibility testing.)
   Remember to change the devices assigned to your NetVM and USBVM if you move between different machines.
 * [Advice on finding a VT-d capable notebook][vt-d-notebook].
 * You can check whether an Intel processor has VT-x and VT-d on [ark.intel.com](https://ark.intel.com/content/www/us/en/ark.html#@Processors)


[nvidia]: /doc/install-nvidia-driver/
[hardware certification requirements for PedOS 4.x]: /news/2016/07/21/new-hw-certification-for-q4/
[Certified Hardware]: /doc/certified-hardware/
[Hardware Testing]: /doc/hardware-testing/
[Hardware Compatibility List]: /hcl/
[hcl-doc]: /doc/hcl/
[hcl-report]: /doc/hcl/#generating-and-submitting-new-reports
[Anti Evil Maid]: /doc/anti-evil-maid/
[live USB]: /doc/live-usb/
[#230]: https://github.com/PedOS/PedOS-issues/issues/230
[vt-d-notebook]: https://groups.google.com/d/msg/PedOS-users/Sz0Nuhi4N0o/ZtpJdoc0OY8J
[Intel VT-x]: https://en.wikipedia.org/wiki/X86_virtualization#Intel_virtualization_.28VT-x.29
[AMD-V]: https://en.wikipedia.org/wiki/X86_virtualization#AMD_virtualization_.28AMD-V.29
[Intel VT-d]: https://en.wikipedia.org/wiki/X86_virtualization#Intel-VT-d
[AMD-Vi (aka AMD IOMMU)]: https://en.wikipedia.org/wiki/X86_virtualization#I.2FO_MMU_virtualization_.28AMD-Vi_and_Intel_VT-d.29
[EPT]: https://en.wikipedia.org/wiki/Second_Level_Address_Translation#Extended_Page_Tables
[RVI]: https://en.wikipedia.org/wiki/Second_Level_Address_Translation#Rapid_Virtualization_Indexing

