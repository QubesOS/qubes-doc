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

Hardware Compatibility List (HCL) for All Qubes OS Releases
===========================================================

The [HCL](/hcl) is a compilation of reports generated and submitted by users across various Qubes versions.
 **Note:**
 Except in the case of developer-reported entries, the Qubes team has not independently verified the accuracy of these reports.
 Please first consult the data sheets (CPU, chipset, motherboard) prior to buying new hardware for Qubes.
 Meet the [System Requirements](/doc/system-requirements/) and search particular for support of:

-   HVM ("AMD virtualization (AMD-V)", "Intel virtualization (VT-x)", "VIA virtualization (VIA VT)")
-   IOMMU ("AMD I/O Virtualization Technology (AMD-Vi)", "Intel Virtualization Technology for Directed I/O (VT-d)")
-   TPM ("Trusted Platform Module (TPM)" connected to a "20-pin TPM header" on motherboards.)

Test the hardware yourself, if possible.
 If using the list to make a purchasing decision, we recommend that you choose hardware with:

-   the best achievable Qubes security level (green columns in HVM, IOMMU, TPM)
-   and general machine compatibility (green columns in Qubes version, dom0 kernel, remarks).

Generating and Submitting New Reports
-------------------------------------

In order to generate a HCL report in Qubes, simply open a terminal in dom0 (KDE: start-menu -\> System Tools -\> Konsole or Terminal Emulator)
 and run `qubes-hcl-report <vm-name>`, where `<vm-name>` is the name of the VM to which the generated HCL files will be saved.
 (Note: If you are working with a new Qubes installation, you may need to update your system in order to download this script.)

You are encouraged to submit your HCL report for the benefit of further Qubes development and other users.
 If you would like to submit your HCL report, please send the **HCL Info** `.txt` file to [\`qubes-users@googlegroups.com\`](/doc/mailing-lists/) with the subject `HCL - <your machine model name>`.
 Please include any useful information about any Qubes features you may have tested (see the legend below), as well as general machine compatibility (video, networking, sleep, etc.).
 If you have problems with your hardware try a different kernel in the [Troubleshooting menu](/doc/InstallationGuideR2rc1/#troubleshooting-problems-with-the-installer).
 Please consider sending the **HCL Support Files** `.cpio.gz` file as well.

**Please note:**
 The **HCL Support Files** may contain numerous hardware details, including serial numbers. If, for privacy or security reasons, you do not wish to make this information public, please **do not** send the `.cpio.gz` file to the public mailing list.
