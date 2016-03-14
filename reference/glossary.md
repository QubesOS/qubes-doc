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

**Qubes OS**  
A security-oriented operating system (OS). The main principle of Qubes OS is
security by compartmentalization (or isolation), in which activities are
compartmentalized (or isolated) in separate **qubes**.

 * The official name is `Qubes OS` (note the capitalization and spacing).
   However, in casual conversation this is often shortened to `Qubes`, and in
   technical contexts where spaces are not permitted, (e.g., usernames), the
   space may be omitted, as in `QubesOS`.

**Qube**  
A user-friendly term for a **domain** (i.e., a VM) in Qubes OS.

 * Example: "In Qubes OS, you do your banking in your 'banking' qube and your
   web surfing in your 'untrusted' qube. That way, if your 'untrusted' qube is
   compromised, your banking activities will remain secure."

 * "Qube" is an informal term intended to make it easier for less technical
   users to understand Qubes OS and learn how to use it. In technical
   discussions, the other, more precise terms defined on this page are to be
   preferred.

 * The term "qube" should be lowercase unless it is the first word in a
   sentence. Note that starting a sentence with the plural of "qube" (i.e.,
   "Qubes...") can be ambiguous, since it may not be clear whether the referent
   is a collection of qubes or Qubes OS.

**Domain**  
A synonym for **virtual machine (VM)**. A software implementation of a machine
(for example, a computer) which executes programs like a physical machine.

**Dom0**  
Domain Zero. Also known as the **host** domain, dom0 is the initial domain
started by the Xen hypervisor on boot. Dom0 runs the Xen management toolstack
and has special privileges relative to other domains, such as direct access to
most hardware.

**DomU**  
Unprivileged Domain. Also known as **guest** domains, domUs are the counterparts
to dom0. All domains except dom0 are domUs. By default, most domUs lack direct
hardware access.

**TemplateVM**  
Template Virtual Machine. Any VM which supplies its root filesystem to another
VM. TemplateVMs are intended for installing and updating software applications,
but not for running them.

 * Colloquially, TemplateVMs are often referred to as "templates."

**TemplateBasedVM**
Any VM which depends on a TemplateVM for its root filesystem.

**Standalone(VM)**  
Standalone (Virtual Machine). In general terms, a VM is described as
**standalone** if and only if it does not depend on any other VM for its root
filesystem. (In other words, a VM is standalone if and only if it is not a
TemplateBasedVM.) More specifically, a **StandaloneVM** is a type of VM in Qubes
which is created by cloning a TemplateVM. Unlike TemplateVMs, however,
StandaloneVMs do not supply their root filesystems to other VMs. (Therefore,
while a TemplateVM is a type of standalone VM, it is not a StandaloneVM.)

**AppVM**  
Application Virtual Machine. A VM which is intended for running software
applications. Typically a TemplateBasedVM, but may be a StandaloneVM. Never a
TemplateVM.

**NetVM**  
Network Virtual Machine. A type of VM which connects directly to a network and
provides access to that network to other VMs which connect to the NetVM. A NetVM
called `sys-net` is created by default in most Qubes installations.

Alternatively, "NetVM" may refer to whichever VM is directly connected to a VM
for networking purposes. For example, if `untrusted` is directly connected to
`sys-firewall` for network access, then it is accurate to say, "`sys-firewall`
is `untrusted`'s NetVM," even though `sys-firewall` is a ProxyVM.

**ProxyVM**  
Proxy Virtual Machine. A type of VM which proxies network access for other VMs.
Typically, a ProxyVM sits between a NetVM and another VM (such as an AppVM or a
TemplateVM) which requires network access.

**FirewallVM**  
Firewall Virtual Machine. A type of ProxyVM which is used to enforce
network-level policies (a.k.a. "firewall rules"). A FirewallVM called
`sys-firewall` is created by default in most Qubes installations.

**DispVM**  
Disposable Virtual Machine. A temporary AppVM which can quickly be created,
used, and destroyed.

**DVM**  
An abbreviation of **DispVM**, typically used to refer to the TemplateVM on
which DispVMs are based. By default, a VM named `fedora-XX-dvm` is created on
most Qubes installations (where `XX` is the current Fedora version).

**PV**  
Paravirtualization. An efficient and lightweight virtualization technique
originally introduced by the Xen Project and later adopted by other
virtualization platforms. Unlike HVMs, paravirtualized VMs do not require
virtualization extensions from the host CPU. However, paravirtualized VMs
require a PV-enabled kernel and PV drivers, so the guests are aware of the
hypervisor and can run efficiently without emulation or virtual emulated
hardware.

**HVM**  
Hardware Virtual Machine. Any fully virtualized, or hardware-assisted, VM
utilizing the virtualization extensions of the host CPU. Although HVMs are
typically slower than paravirtualized VMs due to the required emulation, HVMs
allow the user to create domains based on any operating system.

**StandaloneHVM**  
Any HVM which is standalone (i.e., does not depend on any other VM for its root
filesystem). In Qubes, StandaloneHVMs are referred to simply as **HVMs**.

**TemplateHVM**  
Any HVM which functions as a TemplateVM by supplying its root filesystem to
other VMs. In Qubes, TemplateHVMs are referred to as **HVM templates**.

**PVH**  
PV on HVM. To boost performance, fully virtualized HVM guests can use special
paravirtual device drivers (PVHVM or PV-on-HVM drivers). These drivers are
optimized PV drivers for HVM environments and bypass the emulation for disk and
network I/O, thus providing PV-like (or better) performance on HVM systems. This
allows for optimal performance on guest operating systems such as Windows.

