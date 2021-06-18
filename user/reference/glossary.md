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

## app qube

Any [qube](#qube) that does not have a root filesystem of its own. Every app
qube is based on a [template](#template) from which it borrows the root
filesystem.

* Technical note: This is the preferred user-facing term replacing the
  deprecated terms "AppVM" and "TemplateBasedVM."

* Historical note: This term originally meant "a qube intended for running user
  software applications" (hence the name "app").

## disposable

See [How to Use Dispoables](/doc/how-to-use-disposables/). A type of temporary
[app qube](#app-qube) that can quickly be created, used, and destroyed. Each
disposable is based on a [disposable template](#disposable-template).

## disposable template

A type of [app qube](#app-qube) on which [disposables](#disposable) are based.
(Not to be confused with the concept of a regular [template](#template) that is
itself disposable, which does not exist in Qubes OS.)

* Disposable templates must be app qubes. They cannot be regular
  [templates](#template).

* Each [disposables](#disposable) is based on a disposable template, which is
  in turn based on a regular [templates](#template).

## dom0

[Domain](#domain) zero. Also known as the **host** domain, dom0 is the initial
qube started by the Xen hypervisor on boot. Dom0 runs the Xen management
toolstack and has special privileges relative to other domains, such as direct
access to most hardware.

* The term "dom0" is not a proper noun. It should follow the capitalization
  rules of common nouns.

## domain

In Xen, a synonym for [VM](#vm). See ["domain" on the Xen
Wiki](https://wiki.xenproject.org/wiki/Domain).

* This term has no official meaning in the context of Qubes OS.

## domU

Unprivileged [domain](#domain). Also known as **guest** domains, domUs are the
counterparts to dom0. In Xen, all VMs except dom0 are domUs. By default, most
domUs lack direct hardware access.

* The term "domU" is not a proper noun.  It should follow the capitalization
  rules of common nouns.

## HVM

[Hardware-assisted Virtual Machine](/doc/standalones-and-HVM/). Any fully
virtualized, or hardware-assisted, [VM](#vm) utilizing the virtualization
extensions of the host CPU. Although HVMs are typically slower than
paravirtualized qubes due to the required emulation, HVMs allow the user to
create domains based on any operating system.

## qube

A secure compartment in Qubes OS. Currently, qubes are implemented as Xen
[VMs](#vm), but Qubes OS is independent of its underlying compartmentalization
technology. VMs could be replaced with a different technology, and qubes would
still be called "qubes."

* **Important:** The term "qube" is not a proper noun.  It should follow the
  capitalization rules of common nouns. For example, "I have three qubes" is
  correct," while "I have three Qubes" is incorrect.

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

## Qubes Windows Tools

[Qubes Windows Tools (QWT)](/doc/windows-tools/) are a set of programs and
drivers that provide integration of Windows qubes with the rest of the Qubes OS
system. Also see [Windows](/doc/windows/).

## service qube

A type of [qube](#qube) the primary purpose of which is to provide a service or
services to other qubes. `sys-net` and `sys-firewall` are examples of service
qubes.

## standalone

See [Standalones and HVMs](/doc/standalones-and-hvm/). Any [qube](#qube) that
has its own root filesystem and does not share it with another qube.
Standalones are distinct from both templates and app qubes. A standalone is
created by cloning a template while selecting the option to make the clone
standalone.

## template

See [Templates](/doc/templates/). Any [qube](#qube) that shares its root
filesystem with another qube. A qube that is borrowing a template's root
filesystem is known as an [app qube](#app-qube) and is said to be "based on"
the template. Templates are intended for installing and updating software
applications, but not for running them.

* No template is an [app qube](#app-qube).

* A template cannot be based on another template.

* Regular templates cannot function as [disposable
  templates](#disposable-template). (Disposable templates must be app qubes.)

## VM

An abbreviation for "virtual machine." A software implementation of a machine
(for example, a computer) that executes programs like a physical machine.

