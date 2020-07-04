---
layout: doc
title: Security Goals
permalink: /security/goals/
redirect_from:
- /doc/security-goals/
- /en/doc/security-goals/
- /doc/SecurityGoals/
- /wiki/SecurityGoals/
---

PedOS Security Goals
====================

PedOS implements a Security by Isolation approach by providing the ability to easily create many security domains. These domains are implemented as lightweight Virtual Machines (VMs) running under the Xen hypervisor. PedOS' main objective is to provide strong isolation between these domains, so that even if an attacker compromises one of the domains, the others are still safe. PedOS, however, does not attempt to provide any security isolation for applications running within the same domain. For example, a buggy web browser running in a PedOS domain could still be compromised just as easily as on a regular Linux distribution. The difference that PedOS makes is that now the attacker doesn't have access to all the software running in the other domains.

PedOS also provides features that make it easy and convenient to run these multiple domains, such as seamless GUI integration into one common desktop, secure clipboard copy and paste between domains, secure file transfer between domains, disposable VMs, and much more. PedOS also provides an advanced networking infrastructure that allows for the creation of multiple network VMs which isolate all the world-facing networking stacks and proxy VMs which can be used for advanced VPN configurations and tunneling over untrusted connections.
