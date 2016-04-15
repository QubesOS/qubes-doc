---
layout: doc
title: System Requirements
permalink: /doc/system-requirements/
redirect_from:
- /en/doc/system-requirements/
- /doc/SystemRequirements/
- /wiki/SystemRequirements/
---

System Requirements
===================

Minimum
-------

 * 64-bit Intel or AMD processor (x86\_64 aka x64 aka AMD64)
 * 4 GB RAM
 * 32 GB disk space
 * Legacy boot mode ([UEFI is not supported yet][UEFI])


Recommended
-----------

 * Fast SSD (strongly recommended)
 * Intel GPU (strongly preferred)
   * Nvidia GPUs may require significant [troubleshooting][nvidia].
   * ATI GPUs have not been formally tested (but see the [Hardware Compatibility
     List]).
 * Intel VT-x or AMD-v technology (required for running HVM domains, such as
   Windows-based AppVMs)
 * Intel VT-d or AMD IOMMU technology (required for effective isolation of
   network VMs)
 * TPM with proper BIOS support (required for [Anti Evil Maid])


Choosing Hardware
-----------------

 * Please see the [Hardware Compatibility List] for a compilation of
   hardware reports generated and submitted by users across various Qubes
   versions. (For more information about the HCL itself, see [here][hcl-doc]).
 * For more certain hardware compatibility, you may wish to consider a
   [Qubes-certified laptop].


Important Notes
---------------

 * Qubes **can** be installed on systems which do not meet the recommended
   requirements. Such systems will still offer significant security
   improvements over traditional operating systems, since things like GUI
   isolation and kernel protection do not require special hardware.
 * Qubes **can** be installed on a USB flash drive or external disk, and testing
   has shown that this works very well. A fast USB 3.0 flash drive is
   recommended for this. (As a reminder, its capacity must be at least 32 GB.)
   Simply plug the flash drive into the computer before booting into the Qubes
   installer from a separate installation medium, choose the flash drive as the
   target installation disk, and proceed with the installation normally. After
   Qubes has been installed on the flash drive, it can then be plugged into
   other computers in order to boot into Qubes. In addition to the convenience
   of having a portable copy of Qubes, this allows users to test for hardware
   compatibility on multiple machines (e.g., at a brick-and-mortar computer
   store) before deciding on which computer to purchase. (See [hcl-report] for
   advice on hardware compatibility testing.) Keep in mind to also change
   assigned devices for your netvm and usbvm, if you move between different
   machines.
 * There is also a [live USB] option available, which may be even easier for
   testing.
 * Installing Qubes in a virtual machine is not recommended, as it uses its own
   bare-metal hypervisor (Xen).
 * Macintosh PCs are not currently supported due to keyboard and mouse problems.
   (See [#230] for details. Patches welcome!)
 * [Advice on finding a VT-d capable notebook][vt-d-notebook].


[UEFI]: https://github.com/QubesOS/qubes-issues/issues/794
[nvidia]: /doc/install-nvidia-driver/
[Hardware Compatibility List]: /hcl/
[hcl-doc]: /doc/hcl/
[hcl-report]: /doc/HCL/#generating-and-submitting-new-reports
[Anti Evil Maid]: /doc/anti-evil-maid/
[Qubes-certified laptop]: /doc/certified-laptops/
[live USB]: /doc/live-usb/
[#230]: https://github.com/QubesOS/qubes-issues/issues/230
[vt-d-notebook]: https://groups.google.com/d/msg/qubes-users/Sz0Nuhi4N0o/ZtpJdoc0OY8J

