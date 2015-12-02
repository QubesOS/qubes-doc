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

-   64-bit Intel or AMD processor (x86\_64 aka x64 aka AMD64)
-   4 GB RAM
-   32 GB disk space
-   legacy boot mode ([UEFI not supported yet](https://github.com/QubesOS/qubes-issues/issues/794))

Recommended
-----------

-   Fast SSD (strongly recommended)
-   Intel GPU (strongly preferred)
    -   Nvidia GPUs may require significant [troubleshooting](/doc/install-nvidia-driver/).
    -   ATI GPUs have not been formally tested (but see the [Hardware Compatibility List](/hcl/)).
-   Intel VT-x or AMD-v technology (required for running HVM domains, such as Windows-based AppVMs)
-   Intel VT-d or AMD IOMMU technology (required for effective isolation of network VMs)
-   TPM with proper BIOS support (required for [Anti Evil Maid](http://theinvisiblethings.blogspot.com/2011/09/anti-evil-maid.html))

Important Notes
---------------

-   Qubes **can** be installed on systems which do not meet the recommended requirements. Such systems will still offer significant security improvements over traditional operating systems, since things like GUI isolation and kernel protection do not require special hardware.
-   Qubes **can** be installed on a USB flash drive or external disk, and testing has shown that this works very well. A fast USB 3.0 flash drive is recommended for this. (As a reminder, its capacity must be at least 32 GB.) Simply plug the flash drive into the computer before booting into the Qubes installer from a separate installation medium, choose the flash drive as the target installation disk, and proceed with the installation normally. After Qubes has been installed on the flash drive, it can then be plugged into other computers in order to boot into Qubes. In addition to the convenience of having a portable copy of Qubes, this allows users to test for hardware compatibility on multiple machines (e.g., at a brick-and-mortar computer store) before deciding on which computer to purchase. (See [here](/doc/HCL/#generating-and-submitting-new-reports) for advice on hardware compatibility testing.) Keep in mind to also change assigned devices for your netvm and usbvm, if you move between different machines.
-   Installing Qubes in a virtual machine is not recommended, as it uses its own bare-metal hypervisor (Xen).
-   Macintosh PCs are not currently supported due to keyboard and mouse problems - details in \#230. (Patches welcome!)
-   [Advice on finding a VT-d capable notebook](https://groups.google.com/d/msg/qubes-users/Sz0Nuhi4N0o/ZtpJdoc0OY8J).

