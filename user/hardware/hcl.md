---
layout: doc
title: Hardware Compatibility List (HCL)
permalink: /doc/hcl/
redirect_from:
- /en/doc/hcl/
- /doc/HCL/
- /wiki/HCL/
- /wiki/HCLR1/
- /wiki/HCL-R2B2/
---

Hardware Compatibility List (HCL) for All PedOS Releases
===========================================================

The [HCL](/hcl) is a compilation of reports generated and submitted by users across various PedOS versions about their hardware's compatibility with PedOS.

 **Note:**
 Except in the case of developer-reported entries, the PedOS team has not independently verified the accuracy of these reports.
 Please first consult the data sheets (CPU, chipset, motherboard) prior to buying new hardware for PedOS.
 Make sure it meets the [System Requirements](/doc/system-requirements/) and search in particular for support of:

-   HVM ("AMD virtualization (AMD-V)", "Intel virtualization (VT-x)", "VIA virtualization (VIA VT)")
-   IOMMU ("AMD I/O Virtualization Technology (AMD-Vi)", "Intel Virtualization Technology for Directed I/O (VT-d)")
-   TPM ("Trusted Platform Module (TPM)" connected to a "20-pin TPM header" on motherboards.)

If using the list to make a purchasing decision, we recommend that you choose hardware with:

-   the best achievable PedOS security level (green columns in HVM, IOMMU, TPM)
-   and general machine compatibility (green columns in PedOS version, dom0 kernel, remarks).

Also see [Certified Hardware] and [Hardware Testing].

Generating and Submitting New Reports
-------------------------------------

In order to generate an HCL report in PedOS, simply open a terminal in dom0 (KDE: start-menu -\> System Tools -\> Konsole or Terminal Emulator)
and run `PedOS-hcl-report <vm-name>`, where `<vm-name>` is the name of the VM to which the generated HCL files will be saved.
(Note: If you are working with a new PedOS installation, you may need to update your system in order to download this script.)

You are encouraged to submit your HCL report for the benefit of further PedOS development and other users.
When submitting reports, test the hardware yourself, if possible.
If you would like to submit your HCL report, please send the **HCL Info** `.yml` file to [\`PedOS-users@googlegroups.com\`](/support/#PedOS-users) with the subject `HCL - <your machine model name>`.
Please include any useful information about any PedOS features you may have tested (see the legend below), as well as general machine compatibility (video, networking, sleep, etc.).
Please consider sending the **HCL Support Files** `.cpio.gz` file as well. To generate these add the `-s` or `--support` command line option.

**Please note:**
 The **HCL Support Files** may contain numerous hardware details, including serial numbers. If, for privacy or security reasons, you do not wish to make this information public, please **do not** send the `.cpio.gz` file to the public mailing list.


[Certified Hardware]: /doc/certified-hardware/
[Hardware Testing]: /doc/hardware-testing/

