===================
System requirements
===================


.. warning::

      Notice: The system requirements on this page are *necessary, but not sufficient*, for Qubes compatibility at a minimal or recommended level. In other words, just because a computer satisfies these requirements doesn’t mean that Qubes will successfully install and run on it. We strongly recommend consulting :ref:`user/hardware/system-requirements:choosing hardware` when selecting hardware for Qubes.

Minimum
-------


- **CPU:** 64-bit Intel or AMD processor (also known as ``x86_64``, ``x64``, and ``AMD64``)

  - `Intel VT-x <https://en.wikipedia.org/wiki/X86_virtualization#Intel_virtualization_.28VT-x.29>`__ with `EPT <https://en.wikipedia.org/wiki/Second_Level_Address_Translation#Extended_Page_Tables>`__ or `AMD-V <https://en.wikipedia.org/wiki/X86_virtualization#AMD_virtualization_.28AMD-V.29>`__ with `RVI <https://en.wikipedia.org/wiki/Second_Level_Address_Translation#Rapid_Virtualization_Indexing>`__

  - `Intel VT-d <https://en.wikipedia.org/wiki/X86_virtualization#Intel-VT-d>`__ or `AMD-Vi (also known as AMD IOMMU) <https://en.wikipedia.org/wiki/X86_virtualization#I.2FO_MMU_virtualization_.28AMD-Vi_and_Intel_VT-d.29>`__



- **Memory:** 6 GB RAM

- **Storage:** 32 GB free space



Recommended
-----------


- **CPU:** 64-bit Intel processor (also known as ``x86_64``, ``x64``, and ``Intel 64``)

  - `Intel VT-x <https://en.wikipedia.org/wiki/X86_virtualization#Intel_virtualization_.28VT-x.29>`__ with `EPT <https://en.wikipedia.org/wiki/Second_Level_Address_Translation#Extended_Page_Tables>`__

  - `Intel VT-d <https://en.wikipedia.org/wiki/X86_virtualization#Intel-VT-d>`__

  - For security, we recommend processors that are recent enough to still be receiving microcode updates (see :ref:`user/hardware/system-requirements:important notes` for details).

  - AMD processors are not recommended due to inconsistent security support on client platforms (see :ref:`user/hardware/system-requirements:important notes` for details).



- **Memory:** 16 GB RAM

- **Storage:** 128 GB free space

  - High-speed solid-state drive strongly recommended



- **Graphics:** Intel integrated graphics processor (IGP) strongly recommended

  - Nvidia GPUs may require significant `troubleshooting <https://forum.qubes-os.org/t/18987>`__.

  - AMD GPUs have not been formally tested, but Radeons (especially RX580 and earlier) generally work well.



- **Peripherals:** A non-USB keyboard or multiple USB controllers

- **TPM:** Trusted Platform Module (TPM) with proper BIOS support (required for :doc:`Anti Evil Maid </user/security-in-qubes/anti-evil-maid>`)



Qubes-certified hardware
^^^^^^^^^^^^^^^^^^^^^^^^


The following are *required* for :doc:`Qubes-certified hardware devices </user/hardware/certified-hardware/certified-hardware>` but *merely recommended* for *non-certified* hardware (see the :ref:`hardware certification requirements <user/hardware/certified-hardware/certified-hardware:hardware certification requirements>` for details).

- Open-source boot firmware (e.g., `coreboot <https://www.coreboot.org/>`__)

- Hardware switches for all built-in USB-connected microphones (if any)

- Either support for non-USB input devices (e.g., via PS/2, which most laptops already use internally) or a separate USB controller only for input devices



Choosing Hardware
-----------------


We recommend consulting these resources when selecting hardware for Qubes OS:

- :doc:`Certified hardware </user/hardware/certified-hardware/certified-hardware>` — Qubes developer certified, officially recommended

- `Community-recommended hardware <https://forum.qubes-os.org/t/5560>`__ — list curated and maintained by the community, unofficially recommended

- `Hardware compatibility list (HCL) <https://www.qubes-os.org/hcl/>`__ — community test results, neither recommended nor disrecommended



Important Notes
---------------


- **Installing Qubes in a virtual machine is not recommended, as it uses its own bare-metal hypervisor (Xen).**

- There is a class of security vulnerabilities that can be fixed only by microcode updates. If your computer or the CPU in it no longer receives microcode updates (e.g., because it is too old), it may not be possible for some of these vulnerabilities to be mitigated on your system, leaving you vulnerable. For this reason, we recommend using Qubes OS on systems that are still receiving microcode updates. Nonetheless, Qubes OS **can** run on systems that no longer receive microcode updates, and such systems will still offer significant security advantages over conventional operating systems on the same hardware.

  - Intel maintains a `list <https://www.intel.com/content/www/us/en/support/articles/000022396/processors.html>`__ of end-of-support dates for its processors. However, this list seems to include only processors that are no longer supported or will soon no longer be supported. Many newer Intel processors are missing from this list. To our knowledge, Intel does not announce end-of-support dates for its newer processors in advance, nor does it have a public policy governing how long support will last.



- Intel and AMD handle microcode updates differently, which has significant security implications. On Intel platforms, microcode updates can typically be loaded from the operating system. This allows the Qubes security team to respond rapidly to new vulnerabilities by shipping microcode updates alongside other security updates directly to users. By contrast, on AMD client (as opposed to server) platforms, microcode updates are typically shipped only as part of system firmware and generally cannot be loaded from the operating system  [1]_. This means that AMD users typically must wait for:

  1. AMD to distribute microcode updates to original equipment manufacturers (OEMs), original design manufacturers (ODMs), and motherboard manufacturers (MB); and

  2. The user’s OEM, ODM, or MB to provide a suitable BIOS or (U)EFI update for the user’s system.



  - Historically, AMD has often been slow to complete step (1), at least for its client (as opposed to server) platforms  [2]_. In some cases, AMD has made fixes available for its server platforms very shortly after a security embargo was lifted, but it did not make fixes available for client platforms facing the same vulnerability until weeks or months later. (A “security embargo” is the practice of avoiding public disclosure of a security vulnerability prior to a designated date.) By contrast, Intel has consistently made fixes available for new CPU vulnerabilities across its supported platforms very shortly after security embargoes have been lifted.

  - Step (2) varies by vendor. Many vendors fail to complete step (2) at all, while some others take a very long time to complete it.

  - The bottom line is that Qubes OS **can** run on AMD systems, and the Qubes and Xen security teams do their best to provide security support for AMD systems. However, without the ability to ship microcode updates, there is only so much they can do.



- Qubes **can** be installed on many systems that do not meet the recommended requirements. Such systems will still offer significant security improvements over traditional operating systems, since things like GUI isolation and kernel protection do not require special hardware.

- Qubes **can** be installed on a USB flash drive or external disk, and testing has shown that this works very well. A fast USB 3.0 flash drive is recommended for this. (As a reminder, its capacity must be at least 32 GiB.) Simply plug the flash drive into the computer before booting into the Qubes installer from a separate installation medium, choose the flash drive as the target installation disk, and proceed with the installation normally. After Qubes has been installed on the flash drive, it can then be plugged into other computers in order to boot into Qubes. In addition to the convenience of having a portable copy of Qubes, this allows users to test for hardware compatibility on multiple machines (e.g., at a brick-and-mortar computer store) before deciding on which computer to purchase. (See :ref:`generating and submitting HCL reports <user/hardware/how-to-use-the-hcl:generating and submitting new reports>` for advice on hardware compatibility testing.) Remember to change the devices assigned to your NetVM and USB VM if you move between different machines.

- You can check whether an Intel processor has VT-x and VT-d on `ark.intel.com <https://ark.intel.com/content/www/us/en/ark.html#@Processors>`__.


.. [1]
   There is an ``amd-ucode-firmware`` package, but it only contains microcode for servers and outdated microcode for Chromebooks. Also, the `AMD security website <https://www.amd.com/en/resources/product-security.html>`__ only lists microcode as a mitigation for data center CPUs.
.. [2]
   As shown on `the AMD page for Speculative Return Stack Overflow <https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7005.html>`__, updated AGESA™ firmware for AMD Ryzen™ Threadripper™ 5000WX Processors was not available until 2024-01-11, even though the vulnerability became public on 2023-08-08. AMD did not provide updated firmware for other client processors until a date between 2023-08-22 to 2023-08-25.

   For Zenbleed, firmware was not available until 2024 for most client parts, even though server parts got microcode on 2023-06-06.
