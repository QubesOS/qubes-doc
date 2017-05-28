---
layout: doc
title: Security-critical Code
permalink: /doc/security-critical-code/
redirect_from:
- /en/doc/security-critical-code/
- /doc/SecurityCriticalCode/
- /wiki/SecurityCriticalCode/
- /trac/wiki/SecurityCriticalCode/
---

Security-Critical Code in Qubes OS
==================================

Below is a list of security-critical (AKA trusted) code in Qubes OS. 
A successful attack against any of these portions of the codebase might allow an attacker to compromise the Qubes OS security. This code can be thought of as the Trusted Computing Base (TCB) of Qubes OS. 
One of the major security goals of the project has been to minimize the amount of this trusted code to an absolute minimum. 
The size of the current TCB is of an order of hundreds thousands of lines of C code, which is several orders of magnitude less than in other OSes, such as Windows, Linux or Mac, where it comprises tens of millions of lines of C code. 
Keeping the TCB small reduces the operating system's attack surface and limits the points of entry for exploit hunters.

For more information about the security goals of Qubes OS, see [this page](/security/goals/).

Security-Critical Qubes-Specific Components
-------------------------------------------

The code produced by the Qubes project below is security-critical.

-   Dom0-side of the libvchan library
-   Dom0-side of the GUI virtualization code (*qubes-guid*)
-   Dom0-side of the sound virtualization code (*pacat-simple-vchan*)
-   Dom0-side in qrexec-related code (*qrexec\_daemon*)
-   VM memory manager (*qmemman*) that runs in Dom0
-   Select Qubes RPC servers that run in Dom0: qubes.ReceiveUpdates and qubes.SyncAppMenus
-   The qubes.Filecopy RPC server that runs in a VM -- this segment is critical because it might allow one VM to compromise another one if user allows file copy operation to be performed between them

Security-Critical 3rd-Party Components
--------------------------------------

These are the components that we haven't written or designed ourselves, yet we still rely on them. At the current project stage, we cannot afford to spend time to thoroughly review and audit them, so we just more or less "blindly" trust they are secure.

-   Xen hypervisor
-   The Xen's xenstore backend running in Dom0
-   The Xen's block backend running in Dom0 kernel
-   The rpm program used in Dom0 for verifying Dom0 updates' signatures
-   Somehow optional: log viewing software in dom0 that parses VM-influenced logs

Additionally when we consider attacks that originate through a compromised network domain and target the varying VMs connected to it, these parts must also be included. Those attacks do not apply to domains connected to other network domains (Qubes allows more than one network domains), or those with networking disabled (Dom0 is not connected to any network by default).

-   Xen network PV frontends
-   VM's core networking stacks (core TCP/IP code)

On "Non-Security-Critical" Components
-------------------------------------------

We could have finely audited architecture and a bulletproof TCB that perfectly isolates all domains from each other, but that security would be wasted if the actual email clients, word processors, and other apps used with Qubes OS were somehow trojaned. Treating the *security critical components* as the *only necessary components* means trusting solely the network-isolated domains.

The above means that we must also trust at least some of the vendors that provide the apps we use in critical domains. In practice, Qubes OS must trust the software provided by Fedora project. This software is signed by Fedora distribution keys and so it is also critical that the tools used in domains for software updates (yum and rpm) be trusted.
