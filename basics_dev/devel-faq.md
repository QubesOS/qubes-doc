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

Since 2013 [Xen has not supported 32-bit x86 architecture](http://wiki.xenproject.org/wiki/Xen_Project_Release_Features) and Intel VT-d, which Qubes uses to isolate devices and drivers, is available on Intel 64-bit processors only.

In addition, the included ASLR in x64 linux often makes it more difficult to exploit a bug. While we designed Qubes with an emphasis on limiting any potential attack vectors in the first place, we still realize that some of the code running in Dom0 like our GUI daemon or xen-store daemon, however simple, may contain bugs. We also haven't yet implemented a separate storage domain, which means disk backends are in Dom0. This makes those backends "reachable" from the VMs, which aexpands the potential attack surface. Because of all this, having faced a choice between a 32-bit OS and a 64-bit OS for Dom0, our decision was almost a no-brainer. The 64-bit option provides some (little perhaps, but some) more protection against some classes of attacks, and doesn't have any disadvantages. As a result Qubes OS requires 64-bit processors, but systems that run Qubes OS should have at least 3-4GBs of ram, and those have 64-bit CPUs anyway.

What is the recommended build environment?
------------------------------------------

Any rpm-based, 64-bit. Preferred Fedora.

How can I build Qubes from sources?
--------------------------------

See [these instructions](/doc/qubes-builder/)

How do I submit a patch?
------------------------

See [Qubes Source Code Repositories](/doc/source-code/).

What is Qubes' attitude toward changing guest distros?
------------------------------------------------------

We try to respect each distro's culture, where possible. See the discussion on
issue [#1014](https://github.com/QubesOS/qubes-issues/issues/1014) for an
example.

The policy is there mostly to ease maintenance, on several levels:

 * Less modifications means easier migration to new upstream distribution
   releases
 * Upstream documentation matching the distribution running in Qubes VM
 * Less likely to introduce Qubes-specific issues
 * Each officially supported distribution (ideally) should offer the same set of
   Qubes-specific features - a change in one supported distribution should be
   followed also in others (including some new in the future)

Is QEMU part of the TCB?
------------------------

No. Unlike many other virtualization systems, Qubes takes special effort to keep
the I/O emulation component (QEMU) _outside_ of the TCB. This has been achieved
thanks to the careful use of Xen's stub domain feature. For more details about
how we improved on Xen's native stub domain use, see
[here](https://blog.invisiblethings.org/2012/03/03/windows-support-coming-to-qubes.html).

