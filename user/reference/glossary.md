---
lang: en
layout: doc
permalink: /doc/glossary/
redirect_from:
- /en/doc/glossary/
- /doc/Glossary/
- /wiki/Glossary/
ref: 140
title: Glossary
---

## admin qube

A type of [qube](#qube) used for administering Qubes OS.

* Currently, the only admin qube is [dom0](#dom0).

## app qube

Any [qube](#qube) that does not have a root filesystem of its own. Every app
qube is based on a [template](#template) from which it borrows the root
filesystem.

* Previously known as: `AppVM`, `TemplateBasedVM`.

* Historical note: This term originally meant "a qube intended for running user
  software applications" (hence the name "app").

## disposable

A type of temporary [app qube](#app-qube) that self-destructs when its
originating window closes. Each disposable is based on a [disposable
template](#disposable-template).

See [How to Use Dispoables](/doc/how-to-use-disposables/).

* Previously known as: `DisposableVM`, `DispVM`.

## disposable template

Any [app qube](#app-qube) on which [disposables](#disposable) are based. A
disposable template shares its user directories (and, indirectly, the root
filesystem of the regular [template](#template) on which it is based) with all
[disposables](#disposable) based on it.

* Not to be confused with the concept of a regular [template](#template) that
  is itself disposable, which does not exist in Qubes OS.

* Disposable templates must be app qubes. They cannot be regular
  [templates](#template).

* Every [disposable](#disposable) is based on a disposable template, which is
  in turn based on a regular [template](#template).

* Unlike [disposables](#disposable), disposable templates have the persistence
  properties of normal [app qubes](#app-qube).

* Previously known as: `DisposableVM Template`, `DVM Template`, `DVM`.

## dom0

[Domain](#domain) zero. A type of [admin qube](#admin-qube). Also known as the
**host** domain, dom0 is the initial qube started by the Xen hypervisor on
boot. Dom0 runs the Xen management toolstack and has special privileges
relative to other domains, such as direct access to most hardware.

* The term "dom0" is a common noun and should follow the capitalization rules
  of common nouns.

## domain

In Xen, a synonym for [VM](#vm).

See ["domain" on the Xen Wiki](https://wiki.xenproject.org/wiki/Domain).

* This term has no official meaning in Qubes OS.

## domU

Unprivileged [domain](#domain). Also known as **guest** domains, domUs are the
counterparts to dom0. In Xen, all VMs except dom0 are domUs. By default, most
domUs lack direct hardware access.

* The term "domU" is a common noun and should follow the capitalization rules
  of common nouns.

* Sometimes the term [VM](#vm) is used as a synonym for domU. This is
  technically inaccurate, as [dom0](#dom0) is also a VM in Xen.

## firmware

Software that runs outside the control of the operating system.
Some firmware executes on the same CPU cores as Qubes OS does, but
all computers have many additional processors that the operating system
does not run on, and these computers also run firmware.

## HVM

Hardware-assisted Virtual Machine. Any fully virtualized, or hardware-assisted,
[VM](#vm) utilizing the virtualization extensions of the host CPU. Although
HVMs are typically slower than paravirtualized qubes due to the required
emulation, HVMs allow the user to create domains based on any operating system.

See [Standalones and HVM](/doc/standalones-and-hvms/).

## management qube

A [qube](#qube) used for automated management of a Qubes OS installation via
[Salt](/doc/salt/).

## named disposable

A type of [disposable](#disposable) given a permanent name that continues to
exist even after it is shut down and can be restarted again. Like a regular
[disposable](#disposable), a named disposable has no persistent state: Any
changes made are lost when it is shut down.

* Only one instance of a named disposable can run at a time.

* Like a regular [disposable](#disposable), a named disposable always has the
  same state when it starts, namely that of the [disposable
  template](#disposable-template) on which it is based.

* Technical note: Named disposables are useful for certain [service
  qubes](#service-qube), where the combination of persistent device assignment
  and ephemeral qube state is desirable.

## net qube

Internally known as `netvm`. The property of a [qube](#qube) that specifies
from which qube, if any, it receives network access. Despite the name, "net
qube" (or `netvm`) is a *property* of a qube, not a *type* of qube. For
example, it is common for the net qube of an [app qube](#app-qube) to be the
[service qube](#service-qube) `sys-firewall`, which in turn uses `sys-net` as
its net qube. 

* If a qube does not have a net qube (i.e., its `netvm` is set to `None`), then
  that qube is offline. It is disconnected from all networking.

* The name `netvm` derives from "Networking Virtual Machine." Before Qubes 4.0,
  there was a type of [service qube](#service-qube) called a "NetVM." The name
  of the `netvm` property is a holdover from that era.

## policies

In Qubes OS, "policies" govern interactions between qubes, powered by [Qubes' qrexec system](/doc/qrexec/).
A single policy is a rule applied to a qube or set of qubes, that governs how and when information or assets may be shared with other qubes.  
An example is the rules governing how files can be copied between qubes.  
Policy rules are grouped together in files under `/etc/qubes/policy.d`  
Policies are an important part of what makes Qubes OS special.


## qube

A secure compartment in Qubes OS. Currently, qubes are implemented as Xen
[VMs](#vm), but Qubes OS is independent of its underlying compartmentalization
technology. VMs could be replaced with a different technology, and qubes would
still be called "qubes."

* **Important:** The term "qube" is a common noun and should follow the
  capitalization rules of common nouns. For example, "I have three qubes" is
  correct, while "I have three Qubes" is incorrect.

* Note that starting a sentence with the plural of "qube" (i.e., "Qubes...")
  can be ambiguous, since it may not be clear whether the referent is a
  plurality of qubes or [Qubes OS](#qubes-os).

* Example usage: "In Qubes OS, you do your banking in your 'banking' qube and
  your web surfing in your 'untrusted' qube. That way, if your 'untrusted' qube
  is compromised, your banking activities will remain secure."

* Historical note: The term "qube" was originally invented as an alternative to
  "VM" intended to make it easier for less technical users to understand Qubes
  OS and learn how to use it.

## Qubes OS

A security-oriented operating system (OS). The main principle of Qubes OS is
security by compartmentalization (or isolation), in which activities are
compartmentalized (or isolated) in separate [qubes](#qube).

* **Important:** The official name is "Qubes OS" (note the capitalization and
  the space between "Qubes" and "OS"). In casual conversation, this is often
  shortened to "Qubes." Only in technical contexts where spaces are not
  permitted (e.g., in usernames) may the space be omitted, as in `@QubesOS`.

## Qubes Windows Tools (QWT)

A set of programs and drivers that provide integration of Windows qubes with
the rest of the Qubes OS system.

See [Qubes Windows Tools](/doc/windows-tools/) and [Windows](/doc/windows/).

## service qube

Any [app qube](#app-qube) the primary purpose of which is to provide services
to other qubes. `sys-net` and `sys-firewall` are examples of service qubes.

## standalone

Any [qube](#qube) that has its own root filesystem and does not share it with
another qube. Distinct from both [templates](#template) and [app
qubes](#app-qube).

See [Standalones and HVMs](/doc/standalones-and-hvms/).

* Previously known as: `StandaloneVM`.

## template

Any [qube](#qube) that shares its root filesystem with another qube. A qube
that is borrowing a template's root filesystem is known as an [app
qube](#app-qube) and is said to be "based on" the template. Templates are
intended for installing and updating software applications, but not for running
them.

See [Templates](/doc/templates/).

* No template is an [app qube](#app-qube).

* A template cannot be based on another template.

* Regular templates cannot function as [disposable
  templates](#disposable-template). (Disposable templates must be app qubes.)

* Previously known as: `TemplateVM`.

## VM

An abbreviation for "virtual machine." A software implementation of a computer
that provides the functionality of a physical machine.
