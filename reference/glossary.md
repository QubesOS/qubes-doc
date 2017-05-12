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
A software implementation of a machine (for example, a computer) which executes programs like a physical machine.

Qube
----
A user-friendly term for a [VM](#vm) in Qubes OS.

 * Example: "In Qubes OS, you do your banking in your 'banking' qube and your web surfing in your 'untrusted' qube. That way, if your 'untrusted' qube is compromised, your banking activities will remain secure."

 * "Qube" is an informal term intended to make it easier for less technical users to understand Qubes OS and learn how to use it. In technical discussions, the other, more precise terms defined on this page are to be preferred.

 * The term "qube" should be lowercase unless it is the first word in a sentence. Note that starting a sentence with the plural of "qube" (i.e., "Qubes...") can be ambiguous, since it may not be clear whether the reference is a collection of qubes or [Qubes OS](#qubes-os).

Domain
------
An area or set of activities in one's digital life that has certain security requirements and therefore involves the use of certain [qubes](#qube). 
For example, suppose your "email" domain encompasses the activity of sending PGP-encrypted email. 
This domain may include your email qube and your [Split GPG](/doc/split-gpg) qube. 
Note that domains and qubes are not the same thing.
In this example, your "email" domain includes the use of two qubes. 
Furthermore, a qube can fall under multiple domains simultaneously. 
For example, your Split GPG qube may also be part of your "software development" domain if you PGP-sign your Git commits.

Dom0
----
Domain Zero. 
Also known as the **host** domain, dom0 is the initial VM started by the Xen hypervisor on boot. 
Dom0 runs the Xen management toolstack and has special privileges relative to other domains, such as direct access to most hardware. 
(Note that the use of "domain" for a synonym for "VM" is specific to Xen. Qubes diverges from this practice. See: [domain](#domain).)

DomU
----
Unprivileged Domain. 
Also known as **guest** domains, domUs are the counterparts to dom0. 
All VMs except dom0 are domUs. 
By default, most domUs lack direct hardware access. 
(Note that the use of "domain" for a synonym for "VM" is specific to Xen. Qubes diverges from this practice. See: [domain](#domain).)

TemplateVM
----------
Template Virtual Machine. 
Any [VM](#vm) which supplies its root filesystem to another VM. 
TemplateVMs are intended for installing and updating software applications, but not for running them.

 * Colloquially, TemplateVMs are often referred to as "templates."

TemplateBasedVM
---------------
Any [VM](#vm) which depends on a [TemplateVM](#templatevm) for its root filesystem.

Standalone(VM)
--------------
Standalone (Virtual Machine). 
In general terms, a [VM](#vm) is described as **standalone** if and only if it does not depend on any other VM for its root filesystem. 
(In other words, a VM is standalone if and only if it is not a TemplateBasedVM.) 
More specifically, a **StandaloneVM** is a type of VM in Qubes which is created by cloning a TemplateVM. 
Unlike TemplateVMs, however, StandaloneVMs do not supply their root filesystems to other VMs. 
(Therefore, while a TemplateVM is a type of standalone VM, it is not a StandaloneVM.)

AppVM
-----
Application Virtual Machine. 
A [VM](#vm) which is intended for running software applications. 
Typically a TemplateBasedVM, but may be a StandaloneVM. Never a TemplateVM.

NetVM
-----
Network Virtual Machine. 
A type of [VM](#vm) which connects directly to a network and provides access to that network to other VMs which connect to the NetVM. 
A NetVM called `sys-net` is created by default in most Qubes installations.

Alternatively, "NetVM" may refer to whichever VM is directly connected to a VM for networking purposes. 
For example, if `untrusted` is directly connected to `sys-firewall` for network access, then it is accurate to say, "`sys-firewall` is `untrusted`'s NetVM," even though `sys-firewall` is a ProxyVM.

ProxyVM
-------
Proxy Virtual Machine. 
A type of [VM](#vm) which proxies network access for other VMs. 
Typically, a ProxyVM sits between a NetVM and another VM (such as an AppVM or a TemplateVM) which requires network access.

FirewallVM
----------
Firewall Virtual Machine. 
A type of [ProxyVM](#proxyvm) which is used to enforce network-level policies (a.k.a. "firewall rules"). 
A FirewallVM called `sys-firewall` is created by default in most Qubes installations.

DispVM
------
[Disposable Virtual Machine]. A temporary [AppVM](#appvm) based on a [DVM Template](#dvm-template) which can quickly be created, used, and destroyed.

DVM
---
An abbreviation of [DispVM](#dispvm), typically used to refer to [DVM Templates](#dvm-template).

DVM Template
------------
TemplateBasedVMs on which [DispVMs](#dispvm) are based. 
By default, a DVM Template named `fedora-XX-dvm` is created on most Qubes installations (where `XX` is the Fedora version of the default TemplateVM). 
DVM Templates are neither [TemplateVMs](#templatevm) nor [AppVMs](#appvm). 
They are intended neither for installing nor running software. 
Rather, they are intended for *customizing* or *configuring* software that has already been installed on the TemplateVM on which the DVM Template is based (see [DispVM Customization]). 
This software is then intended to be run (in its customized state) in DispVMs that are based on the DVM Template.

PV
--
Paravirtualization. 
An efficient and lightweight virtualization technique originally introduced by the Xen Project and later adopted by other virtualization platforms. 
Unlike HVMs, paravirtualized [VMs](#vm) do not require virtualization extensions from the host CPU. 
However, paravirtualized VMs require a PV-enabled kernel and PV drivers, so the guests are aware of the hypervisor and can run efficiently without emulation or virtual emulated hardware.

HVM
---
Hardware Virtual Machine. 
Any fully virtualized, or hardware-assisted, [VM](#vm) utilizing the virtualization extensions of the host CPU. 
Although HVMs are typically slower than paravirtualized VMs due to the required emulation, HVMs allow the user to create domains based on any operating system.

StandaloneHVM
-------------
Any [HVM](#hvm) which is standalone (i.e., does not depend on any other VM for its root filesystem). 
In Qubes, StandaloneHVMs are referred to simply as **HVMs**.

TemplateHVM
-----------
Any [HVM](#hvm) which functions as a [TemplateVM](#templatevm) by supplying its root filesystem to other VMs. 
In Qubes, TemplateHVMs are referred to as **HVM templates**.

TemplateBasedHVM
----------------
Any [HVM](#hvm) that depends on a [TemplateVM](#templatevm) for its root filesystem. 

ServiceVM
---------
Service Virtual Machine. 
A [VM](#vm) the primary purpose of which is to provide a service or services to other VMs. 
NetVMs and ProxyVMs are examples of ServiceVMs.

PVHVM
-----
[PV](#pv) on [HVM](#hvm). 
To boost performance, fully virtualized HVM guests can use special paravirtual device drivers (PVHVM or PV-on-HVM drivers). 
These drivers are optimized PV drivers for HVM environments and bypass the emulation for disk and network I/O, thus providing PV-like (or better) performance on HVM systems. 
This allows for optimal performance on guest operating systems such as Windows.

Windows Tools
-----
Qubes Windows Tools are a set of programs and drivers that provide integration of Windows [AppVMs](#appvm) with the rest of the Qubes system.

QWT
----
An abbreviation of Qubes [Windows Tools](#windows-tools).

[Disposable Virtual Machine]: /doc/dispvm/
[DispVM Customization]: /doc/dispvm-customization/

