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

app qube
--------

Any [qube](#qube) that depends on a [template](#template) for its root filesystem.

* Historical note: This term originally meant "a qube intended for running user software applications" (hence the name "app").

* Historical note: This is the preferred term replacing the deprecated term "app qube."

disposable
----------

See [Dispoables](/doc/how-to-use-disposables/).
A temporary [app qube](#app-qube) based on a [disposable template](#disposable-template) that can quickly be created, used, and destroyed.


disposable template
-------------------

A type of [app qube](#app-qube) on which [disposables](#disposable) are based.
(Not to be confused with the concept of a [template](#template) that is itself disposable, which does not exist in Qubes OS.)

Disposable templates are not [templates](#template), since (being app qubes) they do not have root filesystems of their own to provide to other qubes.
Rather, disposable templates are complementary to templates insofar as disposable templates provide their own user filesystems to the disposables based on them.

dom0
----

[Domain](#domain) Zero.
Also known as the **host** domain, dom0 is the initial qube started by the Xen hypervisor on boot.
Dom0 runs the Xen management toolstack and has special privileges relative to other domains, such as direct access to most hardware.

* The term "dom0" is not a proper noun and should not be capitalized (unless it's the first word in a sentence, for example).

* The use of [domain](#domain) as a synonym for [VM](#vm) is specific to Xen. Qubes diverges from this practice. See: [domain](#domain).

domain
------

_This term is deprecated in the context of Qubes OS._

In Xen, a synonym for [VM](#vm). See ["domain" on the Xen Wiki](https://wiki.xenproject.org/wiki/Domain).

domU
----

Unprivileged [domain](#domain).
Also known as **guest** domains, domUs are the counterparts to dom0.
In Xen, all VMs except dom0 are domUs.
By default, most domUs lack direct hardware access.

* The term "domU" is not a proper noun and should not be capitalized unless it is the first word in a sentence.

* The use of [domain](#domain) as a synonym for [VM](#vm) is specific to Xen. Qubes diverges from this practice. See: [domain](#domain).

HVM
---

[Hardware-assisted Virtual Machine](/doc/standalones-and-HVM/).
Any fully virtualized, or hardware-assisted, [VM](#vm) utilizing the virtualization extensions of the host CPU.
Although HVMs are typically slower than paravirtualized qubes due to the required emulation, HVMs allow the user to create domains based on any operating system.

qube
----

A secure compartment in Qubes OS.
Currently, qubes are implemented as Xen [VMs](#vm), but Qubes OS is independent of its underlying compartmentalization technology.
VMs could be replaced with a different technology, and qubes would still be called "qubes."

* **Important:** The term "qube" should be lowercase unless it is the first word in a sentence. Note that starting a sentence with the plural of "qube" (i.e., "Qubes...") can be ambiguous, since it may not be clear whether the referent is a collection of qubes or [Qubes OS](#qubes-os).

* Example usage: "In Qubes OS, you do your banking in your 'banking' qube and your web surfing in your 'untrusted' qube. That way, if your 'untrusted' qube is compromised, your banking activities will remain secure."

* Historical note: The term "qube" was originally invented as an alternative to "VM" intended to make it easier for less technical users to understand Qubes OS and learn how to use it.

Qubes OS
--------

A security-oriented operating system (OS).
The main principle of Qubes OS is security by compartmentalization (or isolation), in which activities are compartmentalized (or isolated) in separate [qubes](#qube).

* **Important:** The official name is "Qubes OS" (note the capitalization and the space between "Qubes" and "OS").
  However, in casual conversation this is often shortened to "Qubes."
  Only in technical contexts where spaces are not permitted (e.g., usernames) may the space be omitted, as in `@QubesOS`.

Qubes Windows Tools
-------------------

[Qubes Windows Tools (QWT)](/doc/windows-tools/) are a set of programs and drivers that provide integration of Windows qubes with the rest of the Qubes OS system.
Also see [Windows](/doc/windows/).

service qube
------------

A [qube](#qube) the primary purpose of which is to provide a service or services to other qubes.
`sys-net` and `sys-firewall` are examples of service qubes.

standalone
----------

See [Standalones and HVMs](/doc/standalone-and-hvm/).
A type of [qube](#qube) that does not depend on any other qube for its root filesystem.
The opposite of an app qube.
A standalone is created by cloning a template.
Unlike templates, however, standalones do not supply their root filesystems to other qubes.

template
--------

See [Templates](/doc/templates/).
Any [qube](#qube) that supplies its root filesystem to another qube.
Templates are intended for installing and updating software applications, but not for running them.

* Since every template supplies its *own* root filesystem to at least one other qube, no template can be based on another template.
  In other words, no template is an [app qube](#app-qube).

* Since every template supplies its *root* filesystem to at least one other qube, no [disposable template](#disposable-template) is a template.

VM
--

An abbreviation for "virtual machine."
A software implementation of a machine (for example, a computer) that executes programs like a physical machine.

