---
lang: en
layout: doc
permalink: /doc/security-design-goals/
redirect_from:
- /security/goals/
- /doc/security-goals/
- /en/doc/security-goals/
- /doc/SecurityGoals/
- /wiki/SecurityGoals/
ref: 210
title: Security Design Goals
---

Qubes OS implements a security-by-isolation (or security-by-compartmentalization) approach by providing the ability to easily create many security domains. These domains are implemented as lightweight Virtual Machines (VMs) running under the Xen hypervisor. Qubes' main objective is to provide strong isolation between these domains, so that even if an attacker compromises one of the domains, the others are still safe. Qubes, however, does not attempt to provide any security isolation for applications running within the same domain. For example, a buggy web browser running in a Qubes domain could still be compromised just as easily as on a regular Linux distribution. The difference that Qubes makes is that now the attacker doesn't have access to all the software running in the other domains.

Qubes also provides features that make it easy and convenient to run these multiple domains, such as seamless GUI integration into one common desktop, secure clipboard copy and paste between domains, secure file transfer between domains, disposable VMs, and much more. Qubes also provides an advanced networking infrastructure that allows for the creation of multiple network VMs which isolate all the world-facing networking stacks and proxy VMs which can be used for advanced VPN configurations and tunneling over untrusted connections.
