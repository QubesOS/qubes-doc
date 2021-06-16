---
lang: en
layout: doc
redirect_from:
- /doc/system-requirements/
- /system-requirements/
- /en/doc/system-requirements/
- /doc/SystemRequirements/
- /wiki/SystemRequirements/
ref: 142
title: System Requirements
---

# System Requirements

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Notice:</b>
  The system requirements on this page are <em>necessary, but not sufficient,</em> for Qubes compatibility at a minimal or recommended level.
  In other words, just because a computer satisfies these requirements doesn't mean that Qubes will successfully install and run on it.
  We strongly recommend consulting the <a href="/hcl/">Hardware Compatibility List</a> to verify that Qubes can install and run on your specific model in the ways you need it to.
</div>

## Minimum

- **CPU:** 64-bit Intel or AMD processor (also known as `x86_64`, `x64`, and `AMD64`)
  - [Intel VT-x](https://en.wikipedia.org/wiki/X86_virtualization#Intel_virtualization_.28VT-x.29) with [EPT](https://en.wikipedia.org/wiki/Second_Level_Address_Translation#Extended_Page_Tables) or [AMD-V](https://en.wikipedia.org/wiki/X86_virtualization#AMD_virtualization_.28AMD-V.29) with [RVI](https://en.wikipedia.org/wiki/Second_Level_Address_Translation#Rapid_Virtualization_Indexing)
  - [Intel VT-d](https://en.wikipedia.org/wiki/X86_virtualization#Intel-VT-d) or [AMD-Vi (also known as AMD IOMMU)](https://en.wikipedia.org/wiki/X86_virtualization#I.2FO_MMU_virtualization_.28AMD-Vi_and_Intel_VT-d.29)
- **Memory:** 6 GB RAM
- **Storage:** 32 GB free space

## Recommended

- **CPU:** 64-bit Intel or AMD processor (also known as `x86_64`, `x64`, and `AMD64`)
  - [Intel VT-x](https://en.wikipedia.org/wiki/X86_virtualization#Intel_virtualization_.28VT-x.29) with [EPT](https://en.wikipedia.org/wiki/Second_Level_Address_Translation#Extended_Page_Tables) or [AMD-V](https://en.wikipedia.org/wiki/X86_virtualization#AMD_virtualization_.28AMD-V.29) with [RVI](https://en.wikipedia.org/wiki/Second_Level_Address_Translation#Rapid_Virtualization_Indexing)
  - [Intel VT-d](https://en.wikipedia.org/wiki/X86_virtualization#Intel-VT-d) or [AMD-Vi (also known as AMD IOMMU)](https://en.wikipedia.org/wiki/X86_virtualization#I.2FO_MMU_virtualization_.28AMD-Vi_and_Intel_VT-d.29)
- **Memory:** 16 GB RAM
- **Storage:** 128 GB free space
  - High-speed solid-state drive strongly recommended
- **Graphics:** Intel integrated graphics processor (IGP) strongly recommended
  - Nvidia GPUs may require significant [troubleshooting](/doc/install-nvidia-driver/)
  - AMD GPUs have not been formally tested, but Radeons (especially RX580 and earlier) generally work well
- **Peripherals:** A non-USB keyboard or multiple USB controllers
- **TPM:** Trusted Platform Module (TPM) with proper BIOS support (required for [Anti Evil Maid](/doc/anti-evil-maid/))
- **Other:** Satisfaction of all [hardware certification requirements for Qubes 4.x](/news/2016/07/21/new-hw-certification-for-q4/)

## Choosing Hardware

- Please see the [Hardware Compatibility List](/hcl/) for a compilation of hardware reports generated and submitted by users across various Qubes versions.
  (For more information about the HCL itself, see [here](/doc/hcl/).)
- See the [Certified Hardware](/doc/certified-hardware/) page.
- See the [Hardware Testing](/doc/hardware-testing/) page.

## Important Notes

- **Installing Qubes in a virtual machine is not recommended, as it uses its own bare-metal hypervisor (Xen).**
- Qubes **can** be installed on systems which do not meet the recommended requirements.
  Such systems will still offer significant security improvements over traditional operating systems, since things like GUI isolation and kernel protection do not require special hardware.
- Qubes **can** be installed on a USB flash drive or external disk, and testing has shown that this works very well. A fast USB 3.0 flash drive is recommended for this.
  (As a reminder, its capacity must be at least 32 GiB.)
  Simply plug the flash drive into the computer before booting into the Qubes installer from a separate installation medium, choose the flash drive as the target installation disk, and proceed with the installation normally.
  After Qubes has been installed on the flash drive, it can then be plugged into other computers in order to boot into Qubes.
  In addition to the convenience of having a portable copy of Qubes, this allows users to test for hardware compatibility on multiple machines (e.g., at a brick-and-mortar computer
  store) before deciding on which computer to purchase.
  (See [hcl-report](/doc/hcl/#generating-and-submitting-new-reports) for advice on hardware compatibility testing.)
  Remember to change the devices assigned to your NetVM and USB VM if you move between different machines.
- [Advice on finding a VT-d capable notebook](https://groups.google.com/d/msg/qubes-users/Sz0Nuhi4N0o/ZtpJdoc0OY8J).
- You can check whether an Intel processor has VT-x and VT-d on [ark.intel.com](https://ark.intel.com/content/www/us/en/ark.html#@Processors).

