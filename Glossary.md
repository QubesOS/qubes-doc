---
layout: doc
title: Glossary
permalink: /doc/Glossary/
redirect_from: /wiki/Glossary/
---

Glossary of Qubes Terminology
=============================

**Domain**  
A **virtual machine (VM)**, i.e., a software implementation of a machine (for example, a computer) that executes programs like a physical machine.

**Dom0**  
Domain Zero. Also known as the **host** domain, dom0 is the initial domain started by the Xen hypervisor on boot. Dom0 runs the Xen management toolstack and has special privileges relative to other domains, such as direct access to most hardware.

**DomU**  
Unprivileged Domain. Also known as **guest** domains, domUs are the counterparts to dom0. All domains except dom0 are domUs. By default, most domUs lack direct hardware access.

**AppVM**  
Application Virtual Machine. Any VM which depends on a TemplateVM for its root filesystem. In contrast to TemplateVMs, AppVMs are intended for running software applications.

**TemplateVM**  
Template Virtual Machine. Any standalone VM which supplies its root filesystem to other VMs, known as AppVMs. In contrast to AppVMs, TemplateVMs are intended for installing and updating software applications.

**Standalone(VM)**  
Standalone (Virtual Machine). In general terms, a VM is described as **standalone** if and only if it does not depend on any other VM for its root filesystem. (In other words, a VM is standalone if and only if it is not an AppVM.) More specifically, a **StandaloneVM** is a type of VM in Qubes which is created by cloning a TemplateVM. Unlike TemplateVMs, however, StandaloneVMs cannot supply their root filesystems to other VMs. (Therefore, while a TemplateVM is a standalone VM, it is not a StandaloneVM.)

**NetVM**  
Network Virtual Machine. A type of VM which connects directly to a network and provides access to that network to other VMs which connect to the NetVM. A NetVM called `netvm` is created by default in most Qubes installations.

**ProxyVM**  
Proxy Virtual Machine. A type of VM which proxies network access for other VMs. Typically, a ProxyVM sits between a NetVM and a domU which requires network access.

**FirewallVM**  
Firewall Virtual Machine. A type of ProxyVM which is used to enforce network-level policies (a.k.a. "firewall rules"). A FirewallVM called `firewallvm` is created by default in most Qubes installations.

**DispVM**  
Disposable Virtual Machine. A temporary AppVM which can quickly be created, used, and destroyed.

**PV**  
Paravirtualization. An efficient and lightweight virtualization technique originally introduced by the Xen Project and later adopted by other virtualization platforms. Unlike HVMs, paravirtualized VMs do not require virtualization extensions from the host CPU. However, paravirtualized VMs require a PV-enabled kernel and PV drivers, so the guests are aware of the hypervisor and can run efficiently without emulation or virtual emulated hardware.

**HVM**  
Hardware Virtual Machine. Any fully virtualized, or hardware-assisted, VM utilizing the virtualization extensions of the host CPU. Although HVMs are typically slower than paravirtualized VMs due to the required emulation, HVMs allow the user to create domains based on any operating system.

**StandaloneHVM**  
Any HVM which is standalone (i.e., does not depend on any other VM for its root filesystem). In Qubes, StandaloneHVMs are referred to simply as **HVMs**.

**TemplateHVM**  
Any HVM which functions as a TemplateVM by supplying its root filesystem to other VMs. In Qubes, TemplateHVMs are referred to as **HVM templates**.

**PVH**  
PV on HVM. To boost performance, fully virtualized HVM guests can use special paravirtual device drivers (PVHVM or PV-on-HVM drivers). These drivers are optimized PV drivers for HVM environments and bypass the emulation for disk and network IO, thus providing PV like (or better) performance on HVM systems. This allows for optimal performance on guest operating systems such as Windows.


