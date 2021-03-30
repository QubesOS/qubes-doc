---
lang: en
layout: doc
permalink: /doc/hcl/
redirect_from:
- /en/doc/hcl/
- /doc/HCL/
- /wiki/HCL/
- /wiki/HCLR1/
- /wiki/HCL-R2B2/
ref: 146
title: Hardware Compatibility List (HCL)
---

Hardware Compatibility List (HCL) for All Qubes OS Releases
===========================================================

The [HCL](/hcl) is a compilation of reports generated and submitted by users across various Qubes versions about their hardware's compatibility with Qubes.

 **Note:**
 Except in the case of developer-reported entries, the Qubes team has not independently verified the accuracy of these reports.
 Please first consult the data sheets (CPU, chipset, motherboard) prior to buying new hardware for Qubes.
 Make sure it meets the [System Requirements](/doc/system-requirements/) and search in particular for support of:

-   HVM ("AMD virtualization (AMD-V)", "Intel virtualization (VT-x)", "VIA virtualization (VIA VT)")
-   IOMMU ("AMD I/O Virtualization Technology (AMD-Vi)", "Intel Virtualization Technology for Directed I/O (VT-d)")
-   TPM ("Trusted Platform Module (TPM)" connected to a "20-pin TPM header" on motherboards.)

If using the list to make a purchasing decision, we recommend that you choose hardware with:

-   the best achievable Qubes security level (green columns in HVM, IOMMU, TPM)
-   and general machine compatibility (green columns in Qubes version, dom0 kernel, remarks).

Also see [Certified Hardware] and [Hardware Testing].

Generating and Submitting New Reports
-------------------------------------

In order to generate an HCL report in Qubes, simply open a terminal in dom0 (KDE: start-menu -\> System Tools -\> Konsole or Terminal Emulator)
and run `qubes-hcl-report <vm-name>`, where `<vm-name>` is the name of the VM to which the generated HCL files will be saved.
(Note: If you are working with a new Qubes installation, you may need to update your system in order to download this script.)

You are encouraged to submit your HCL report for the benefit of further Qubes development and other users.
When submitting reports, test the hardware yourself, if possible.
If you would like to submit your HCL report, please send the **HCL Info** `.yml` file to [\`qubes-users@googlegroups.com\`](/support/#qubes-users) with the subject `HCL - <your machine model name>`. Alternatively you can also create a post in the [HCL Reports category](https://qubes-os.discourse.group/c/user-support/hcl-reports/23) of the forum.
Please include any useful information about any Qubes features you may have tested (see the legend below), as well as general machine compatibility (video, networking, sleep, etc.).
Please consider sending the **HCL Support Files** `.cpio.gz` file as well. To generate these add the `-s` or `--support` command line option.

**Please note:**
 The **HCL Support Files** may contain numerous hardware details, including serial numbers. If, for privacy or security reasons, you do not wish to make this information public, please **do not** send the `.cpio.gz` file to the public mailing list.


[Certified Hardware]: /doc/certified-hardware/
[Hardware Testing]: /doc/hardware-testing/
