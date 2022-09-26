---
lang: en
layout: doc
permalink: /doc/system-requirements/
redirect_from:
- /system-requirements/
- /en/doc/system-requirements/
- /doc/SystemRequirements/
- /wiki/SystemRequirements/
ref: 142
title: System requirements
---

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Notice:</b> The system requirements on this page are <em>necessary, but
  not sufficient,</em> for Qubes compatibility at a minimal or recommended
  level. In other words, just because a computer satisfies these requirements
  doesn't mean that Qubes will successfully install and run on it. We strongly
  recommend consulting the <a href="#choosing-hardware">resources below</a>
  when selecting hardware for Qubes.
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
  - Nvidia GPUs may require significant
    [troubleshooting](/doc/install-nvidia-driver/)
  - AMD GPUs have not been formally tested, but Radeons (especially RX580 and
    earlier) generally work well

- **Peripherals:** A non-USB keyboard or multiple USB controllers

- **TPM:** Trusted Platform Module (TPM) with proper BIOS support (required for
  [Anti Evil Maid](/doc/anti-evil-maid/))

The following are *required* for [Qubes-certified hardware
devices](/doc/certified-hardware/) but *merely recommended* for *non-certified*
hardware (see the [hardware certification
requirements](/doc/certified-hardware/#hardware-certification-requirements) for
details).

- Open-source boot firmware (e.g., [coreboot](https://www.coreboot.org/))

- Hardware switches for all built-in USB-connected microphones (if any)

- Either support for non-USB input devices (e.g., via PS/2, which most laptops
  already use internally) or a separate USB controller only for input devices

## Choosing Hardware

We recommend consulting these resources when selecting hardware for Qubes OS:

- [Certified hardware](/doc/certified-hardware/) --- Qubes developer certified,
  officially recommended
- [Community-recommended hardware](https://forum.qubes-os.org/t/5560)
  --- list curated and maintained by the community, unofficially recommended
- [Hardware compatibility list (HCL)](/hcl/) --- community test results,
  neither recommended nor disrecommended

## Important Notes

- **Installing Qubes in a virtual machine is not recommended, as it uses its
  own bare-metal hypervisor (Xen).**

- Qubes **can** be installed on many systems that do not meet the recommended
  requirements. Such systems will still offer significant security improvements
  over traditional operating systems, since things like GUI isolation and
  kernel protection do not require special hardware.

- Qubes **can** be installed on a USB flash drive or external disk, and testing
  has shown that this works very well. A fast USB 3.0 flash drive is
  recommended for this. (As a reminder, its capacity must be at least 32 GiB.)
  Simply plug the flash drive into the computer before booting into the Qubes
  installer from a separate installation medium, choose the flash drive as the
  target installation disk, and proceed with the installation normally. After
  Qubes has been installed on the flash drive, it can then be plugged into
  other computers in order to boot into Qubes. In addition to the convenience
  of having a portable copy of Qubes, this allows users to test for hardware
  compatibility on multiple machines (e.g., at a brick-and-mortar computer
  store) before deciding on which computer to purchase. (See [generating and
  submitting HCL
  reports](/doc/how-to-use-the-hcl/#generating-and-submitting-new-reports) for
  advice on hardware compatibility testing.) Remember to change the devices
  assigned to your NetVM and USB VM if you move between different machines.

- You can check whether an Intel processor has VT-x and VT-d on
  [ark.intel.com](https://ark.intel.com/content/www/us/en/ark.html#@Processors).
