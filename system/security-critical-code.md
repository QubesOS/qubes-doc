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

Below is a list of security-critical (or "trusted") code in Qubes OS.
A successful attack against any of these components of the codebase might compromise the system's security.
This code can be thought of as a Trusted Computing Base (TCB) of Qubes OS.
The goal of the project has been to keep the amount of this trusted code to an absolute minimum.
The size of the current TCB is of an order of hundreds thousands of lines of C code, which is several orders of magnitude less than in other OSes.
(In Windows, Linux, or Mac, the amount of trusted code can be in the order of tens of millions of lines of C code.)

For more information about the security goals of Qubes OS, see [this page](/security/goals/).

Security-Critical Qubes-Specific Components
-------------------------------------------

The following Qubes OS–produced code is security-critical:

-   Dom0-side of the libvchan library
-   Dom0-side of the GUI virtualization code (*qubes-guid*)
-   Dom0-side of the sound virtualization code (*pacat-simple-vchan*)
-   Dom0-side in qrexec-related code (*qrexec\_daemon*)
-   VM memory manager (*qmemman*) that runs in Dom0
-   select Qubes RPC servers that run in Dom0: qubes.ReceiveUpdates and qubes.SyncAppMenus
-   The qubes.Filecopy RPC server that runs in a VM (critical because it might allow one VM to compromise another if the user allows file copy operation to be performed between them)

Security-Critical Third-Party Components
----------------------------------------

These components have not been written or designed by the Qubes project, yet we still rely on them.
At the current project stage, we cannot afford to spend time to thoroughly review and audit them, so we more or less "blindly" trust they are secure.

-   Xen hypervisor
-   The Xen's xenstore backend running in Dom0
-   The Xen's block backend running in Dom0 kernel
-   The rpm program used in Dom0 for verifying signatures of Dom0 updates
-   Somehow optional: log viewing software in dom0 that parses VM-influenced logs

Attacks that originate through a compromised network domain and its connected VMs do not apply to domains connected to other network domains (Qubes allows more than one network domain), or those with networking disabled.
(Dom0 is not connected to any network by default).
These attacks might include:

-   Xen network PV frontends
-   VM's core networking stacks (core TCP/IP code)

Buggy Code vs. Back-doored Code Distinction
-------------------------------------------

There is an important distinction between the buggy code and maliciously trojaned code.
We could have the most secure architecture and the most bulletproof TCB that perfectly isolates all domains from each other, but it still would be pretty useless if all the code used within domains, e.g. the actual email clients, word processors, etc, was somehow trojaned.
In that case only network-isolated domains could be somewhat trusted, while all others could not.

The above means that we must trust at least some of the vendors (not all, of course, but at least those few that provide the apps that we use in the most critical domains).
In practice, we trust the software provided by Fedora project.
This software is signed by Fedora distribution keys, so it is also critical that the tools used in domains for software updates (yum and rpm) be trusted.

Cooperative Covert Channels Between Domains
-------------------------------------------

Qubes does not attempt to eliminate all possible *cooperative* covert channels between domains, i.e. such channels that could be established between two *compromised* domains.
We don't believe this is possible to achieve on x86 hardware, and we also doubt it makes any sense in practice for most users -- after all if the two domains are compromised, then it's already (almost) all lost anyway.
