---
layout: doc
title: Glossary
permalink: /doc/glossary/
redirect_from:
- /en/doc/glossary/
- /doc/Glossary/
- /wiki/Glossary/
---

Glossary of Qubes Terminology
=============================

Qubes OS
--------

A security-oriented operating system (OS).
The main principle of Qubes OS is security by compartmentalization (or isolation), in which activities are compartmentalized (or isolated) in separate **qubes**.

* The official name is `Qubes OS` (note the capitalization and spacing).
  However, in casual conversation this is often shortened to `Qubes`, and in technical contexts where spaces are not permitted, (e.g., usernames), the space may be omitted, as in `QubesOS`.

VM
--

An abbreviation for "virtual machine."
A software implementation of a machine (for example, a computer) that executes programs like a physical machine.

Qube
----

A user-friendly term for a [VM](#vm) in Qubes OS.

* Example: "In Qubes OS, you do your banking in your 'banking' qube and your web surfing in your 'untrusted' qube. That way, if your 'untrusted' qube is compromised, your banking activities will remain secure."

* "Qube" is an informal term intended to make it easier for less technical users to understand Qubes OS and learn how to use it. In technical discussions, the other, more precise terms defined on this page are to be preferred.

* The term "qube" should be lowercase unless it is the first word in a sentence. Note that starting a sentence with the plural of "qube" (i.e., "Qubes...") can be ambiguous, since it may not be clear whether the referent is a collection of qubes or [Qubes OS](#qubes-os).

Domain
------

**In Qubes OS:** An area or set of activities in one's digital life that has certain security requirements and therefore involves the use of certain [qubes](#qube).
For example, suppose your "email" domain encompasses the activity of sending PGP-encrypted email.
This domain may include your email qube and your [Split GPG](/doc/split-gpg) qube.
Note that domains and qubes are not the same thing.
In this example, your "email" domain includes the use of two qubes.
Furthermore, a qube can fall under multiple domains simultaneously.
For example, your Split GPG qube may also be part of your "software development" domain if you PGP-sign your Git commits.

**In Xen:** A synonym for [VM](#vm). See [Domain on the Xen Wiki](https://wiki.xenproject.org/wiki/Domain).

dom0
----

Domain Zero.
Also known as the **host** domain, dom0 is the initial VM started by the Xen hypervisor on boot.
Dom0 runs the Xen management toolstack and has special privileges relative to other domains, such as direct access to most hardware.
(Note that the use of [domain](#domain) for a synonym for [VM](#vm) is specific to Xen. Qubes diverges from this practice. See: [domain](#domain).)

domU
----

Unprivileged Domain.
Also known as **guest** domains, domUs are the counterparts to dom0.
All VMs except dom0 are domUs.
By default, most domUs lack direct hardware access.
(Note that the use of [domain](#domain) for a synonym for [VM](#vm) is specific to Xen. Qubes diverges from this practice. See: [domain](#domain).)

TemplateVM
----------

[Template Virtual Machine](/doc/templates/).
Any [VM](#vm) that supplies its root filesystem to another VM.
TemplateVMs are intended for installing and updating software applications, but not for running them.

* Colloquially, TemplateVMs are often referred to as "templates."
* Since every TemplateVM supplies its *own* root filesystem to at least one other VM, no TemplateVM can be based on another TemplateVM.
  In other words, no TemplateVM is a [TemplateBasedVM](#templatebasedvm).
* Since every TemplateVM supplies its *root* filesystem to at least one other VM, no [DisposableVM Template](#disposablevm-template) is a TemplateVM.

TemplateBasedVM
---------------

Any [VM](#vm) that depends on a [TemplateVM](#templatevm) for its root filesystem.

Standalone(VM)
--------------

[Standalone (Virtual Machine)](/doc/standalone-and-hvm/).
In general terms, a [VM](#vm) is described as **standalone** if and only if it does not depend on any other VM for its root filesystem.
(In other words, a VM is standalone if and only if it is not a TemplateBasedVM.)
More specifically, a **StandaloneVM** is a type of VM in Qubes that is created by cloning a TemplateVM.
Unlike TemplateVMs, however, StandaloneVMs do not supply their root filesystems to other VMs.
(Therefore, while a TemplateVM is a type of standalone VM, it is not a StandaloneVM.)

AppVM
-----

Application Virtual Machine.
A [VM](#vm) class.
Synonymous with [TemplateBasedVM](#templatebasedvm).

NetVM
-----

*This is an old definition from before Qubes 4.0.
NetVMs, as defined here, no longer exist in Qubes 4.0 or later (see [here][pr-748] for technical details).*

Network Virtual Machine.
A type of [VM](#vm) that connects directly to a network.
Other VMs gain access to a network by connecting to a NetVM (usually indirectly, via a [FirewallVM](#firewallvm)).
A NetVM called `sys-net` is created by default in most Qubes installations.

Alternatively, "NetVM" may refer to whichever VM is directly connected to a VM for networking purposes.
For example, if `untrusted` is directly connected to `sys-firewall` for network access, then it is accurate to say, "`sys-firewall` is `untrusted`'s NetVM," even though `sys-firewall` is a ProxyVM.

ProxyVM
-------

*This is an old definition from before Qubes 4.0.
ProxyVMs, as defined here, no longer exist in Qubes 4.0 or later (see [here][pr-748] for technical details).*

Proxy Virtual Machine.
A type of [VM](#vm) that proxies network access for other VMs.
Typically, a ProxyVM sits between a NetVM and another VM (such as an AppVM or a TemplateVM) that requires network access.

FirewallVM
----------

*This is an old definition from before Qubes 4.0.
FirewallVMs, as defined here, no longer exist in Qubes 4.0 or later (see [here][pr-748] for technical details).*

Firewall Virtual Machine.
A type of [ProxyVM](#proxyvm) that is used to enforce network-level policies (a.k.a. "firewall rules").
A FirewallVM called `sys-firewall` is created by default in most Qubes installations.
Also see [Qubes Firewall](/doc/firewall/).

DisposableVM
------------

[Disposable Virtual Machine](/doc/disposablevm/).
A temporary [AppVM](#appvm) based on a [DisposableVM Template](#disposablevm-template) that can quickly be created, used, and destroyed.

DispVM
------

An older term for [DisposableVM](#disposablevm).

DVM
---

An abbreviation of [DisposableVM](#disposablevm), typically used to refer to [DisposableVM Templates](#disposablevm-template).

DisposableVM Template
---------------------

(Formerly known as a "DVM Template".)
A type of [TemplateBasedVM](#templatebasedvm) on which [DisposableVMs](#disposablevm) are based.
By default, a DisposableVM Template named `fedora-XX-dvm` is created on most Qubes installations (where `XX` is the Fedora version of the default TemplateVM).
DisposableVM Templates are not [TemplateVMs](#templatevm), since (being TemplateBasedVMs) they do not have root filesystems of their own to provide to other VMs.
Rather, DisposableVM Templates are complementary to TemplateVMs insofar as DisposableVM Templates provide their own user filesystems to the DisposableVMs based on them.

PV
--

Paravirtualization.
An efficient and lightweight virtualization technique originally introduced by the Xen Project and later adopted by other virtualization platforms.
Unlike HVMs, paravirtualized [VMs](#vm) do not require virtualization extensions from the host CPU.
However, paravirtualized VMs require a PV-enabled kernel and PV drivers, so the guests are aware of the hypervisor and can run efficiently without emulation or virtual emulated hardware.

HVM
---

[Hardware-assisted Virtual Machine](/doc/standalone-and-hvm/).
Any fully virtualized, or hardware-assisted, [VM](#vm) utilizing the virtualization extensions of the host CPU.
Although HVMs are typically slower than paravirtualized VMs due to the required emulation, HVMs allow the user to create domains based on any operating system.

StandaloneHVM
-------------

Any [HVM](#hvm) that is standalone (i.e., does not depend on any other VM for its root filesystem).
In Qubes, StandaloneHVMs are referred to simply as **HVMs**.

TemplateHVM
-----------

Any [HVM](#hvm) that functions as a [TemplateVM](#templatevm) by supplying its root filesystem to other VMs.
In Qubes, TemplateHVMs are referred to as **HVM templates**.

TemplateBasedHVM
----------------

Any [HVM](#hvm) that depends on a [TemplateVM](#templatevm) for its root filesystem.

ServiceVM
---------

Service Virtual Machine.
A [VM](#vm) the primary purpose of which is to provide a service or services to other VMs.
NetVMs and ProxyVMs are examples of ServiceVMs.

SystemVM
--------

System Virtual Machine.
A synonym for [ServiceVM](#servicevm).
SystemVMs usually have the prefix `sys-`.

PVHVM
-----

[PV](#pv) on [HVM](#hvm).
To boost performance, fully virtualized HVM guests can use special paravirtual device drivers (PVHVM or PV-on-HVM drivers).
These drivers are optimized PV drivers for HVM environments and bypass the emulation for disk and network I/O, thus providing PV-like (or better) performance on HVM systems.
This allows for optimal performance on guest operating systems such as Windows.

Windows Tools
-----

[Qubes Windows Tools](/doc/windows-tools/) (QWT) are a set of programs and drivers that provide integration of Windows [AppVMs](#appvm) with the rest of the Qubes system.
Also see [Windows](/doc/windows/).

QWT
----

An abbreviation of Qubes [Windows Tools](#windows-tools).

[pr-748]: https://github.com/QubesOS/qubes-doc/pull/748
