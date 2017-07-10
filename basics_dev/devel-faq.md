---
layout: doc
title: Developers' FAQ
permalink: /doc/devel-faq/
redirect_from:
- /en/doc/devel-faq/
- /doc/DevelFaq/
- /wiki/DevelFaq/
---

Qubes Developers' FAQ
=====================

Why does dom0 need to be 64-bit?
--------------------------------

Since 2013 [Xen has not supported 32-bit x86 architecture](https://wiki.xenproject.org/wiki/Xen_Project_Release_Features) and Intel VT-d, which Qubes uses to isolate devices and drivers, is available on Intel 64-bit processors only.

In addition, with features like improved ASLR, it is often more difficult to exploit a bug on x64 Linux than x86 Linux. 
While we designed Qubes from the beginning to limit potential attack vectors, we still realize that some of the code running in Dom0, e.g. our GUI daemon or xen-store daemon, however simple, might contain some bugs. 
Plus since we haven't implemented a separate storage domain, the disk backends are in Dom0 and are "reachable" from the VMs, which adds up to the potential attack surface. 
So, having faced a choice between 32-bit and 64-bit OS for Dom0, it was almost a no-brainer. 
The 64-bit option provides some (little perhaps, but some) more protection against some classes of attacks, and at the same time does not have any disadvantages except the extra requirement of a 64 bit processor. 
And even though Qubes now "needs" a 64 bit processor, it didn't make sense to run Qubes on a system without 3-4GB of memory, and those have 64-bit CPUs anyway.

What is the recommended build environment for Qubes OS?
------------------------------------------

Any rpm-based, 64-bit environment, the preferred OS being Fedora.

How do I build Qubes from sources?
--------------------------------

See [these instructions](/doc/qubes-builder/).

How do I submit a patch?
------------------------

See the [Qubes Source Code Repositories](/doc/source-code/) article.

What is Qubes' attitude toward changing guest distros?
------------------------------------------------------

We try to respect each distro's culture, where possible. 
See the discussion on issue [#1014](https://github.com/QubesOS/qubes-issues/issues/1014) for an example.

The policy is there mostly to ease maintenance, on several levels:

 * Less modifications means easier migration to new upstream distribution
   releases.
 * The upstream documentation matches the distribution running in the Qubes VM.
 * We're less likely to introduce Qubes-specific issues.
 * Each officially supported distribution (ideally) should offer the same set of
   Qubes-specific features - a change in one supported distribution should be
   followed also in others, including new future distributions.

Is I/O emulation component (QEMU) part of the Trusted Computing Base (TCB)?
------------------------

No. Unlike many other virtualization systems, Qubes takes special effort to keep QEMU _outside_ of the TCB. 
This has been achieved thanks to the careful use of Xen's stub domain feature. 
For more details about how we improved on Xen's native stub domain use, see [here](https://blog.invisiblethings.org/2012/03/03/windows-support-coming-to-qubes.html).
