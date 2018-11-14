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

Security-critical Code in Qubes OS
==================================

Below is a list of security-critical (i.e., trusted) code components in Qubes OS.
A successful attack against any of these components could compromise the system's security.
This code can be thought of as the Trusted Computing Base (TCB) of Qubes OS.
One of the main goals of the project is to keep the TCB to an absolute minimum.
The size of the current TCB is on the order order of hundreds of thousands of lines of C code, which is several orders of magnitude less than other OSes.
(In Windows, Linux, and Mac OSes, the amount of trusted code is typically on the order of tens of *millions* of lines of C code.)

For more information, see [Qubes Security Goals].


Security-critical Qubes-specific Components
-------------------------------------------

The following code components are security-critical in Qubes OS:

 - Dom0-side of the libvchan library
 - Dom0-side of the GUI virtualization code (`qubes-guid`)
 - Dom0-side of the sound virtualization code (`pacat-simple-vchan`)
 - Dom0-side in qrexec-related code (`qrexec_daemon`)
 - VM memory manager (`qmemman`) that runs in Dom0
 - Select Qubes RPC servers that run in Dom0: `qubes.ReceiveUpdates` and `qubes.SyncAppMenus`
 - The `qubes.Filecopy` RPC server that runs in a VM (critical because it could allow one VM to compromise another if the user allows a file copy operation to be performed between them)


Security-critical Third-party Components
----------------------------------------

We did not create these components, but Qubes OS relies on them.
At the current stage of the project, we cannot afford to spend the time to thoroughly review and audit them, so we more or less "blindly" trust that they are secure.

 - The Xen hypervisor
 - Xen's xenstore backend running in Dom0
 - Xen's block backend running in Dom0's kernel
 - The RPM program used in Dom0 for verifying signatures on dom0 updates
 - Somewhat trusted: log viewing software in dom0 that parses VM-influenced logs


Attacks on Networking Components
--------------------------------

Here are two examples of networking components that an adversary might seek to attack (or in which to exploit a vulnerability as part of an attack):

 - Xen network PV frontends
 - VMs' core networking stacks (core TCP/IP code)

Hypothetically, an adversary could compromise a NetVM, `sys-net-1`, and try to use it to attack the VMs connected to that NetVM.
However, Qubes allows for the existence of more than one NetVM, so the adversary would not be able to use `sys-net-1` in order to attack VMs connected to a *different* NetVM, `sys-net-2` without also compromising `sys-net-2`.
In addition, the adversary would not be able to use `sys-net-1` (or, for that matter, `sys-net-2`) to attack VMs that have networking disabled (i.e., VMs that are not connected to any NetVM).


Buggy Code vs. Backdoored Code
------------------------------

There is an important distinction between buggy code and maliciously backdoored code.
We could have the most secure architecture and the most bulletproof TCB that perfectly isolates all domains from each other, but it would all be pretty useless if all the code we ran inside our domains (e.g. the code in our email clients, word processors, and web browsers) were backdoored.
In that case, only network-isolated domains would be somewhat trustworthy.

This means that we must trust at least some of the vendors that supply the code we run inside our domains.
(We don't have to trust *all* of them, but we at least have to trust the few that provide the apps we use in the most critical domains.)
In practice, we trust the software provided by the [Fedora Project].
This software is signed by Fedora distribution keys, so it is also critical that the tools used in domains for software updates (`dnf` and `rpm`) are trustworthy.


[Qubes Security Goals]: /security/goals/
[Fedora Project]: https://getfedora.org/
[Understanding and Preventing Data Leaks]: /doc/data-leaks/

