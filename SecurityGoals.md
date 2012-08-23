---
layout: wiki
title: SecurityGoals
permalink: /wiki/SecurityGoals/
---

Qubes Security Goals
====================

Qubes implements Security by Isolation approach by providing a user with ability to easily create many security domains. Those domains are implemented as lightweight Virtual Machines (VMs) running under the Xen hypervisor. Qubes' main objective is to provide strong isolation between these domains, so that even if the attacker compromise one of the domains, the others are still safe. Qubes, however, does not attempt to provide any security isolation for applications that run within the same domain. E.g. a buggy web browser running in one of the Qubes domains could still be compromised just as easily as on regular Linux OS. The difference that Qubes makes, is that now the attacker doesn't have access to all the other software running in the other domains.

Qubes also provides a number of mechanisms that make it easy and convenient for the user to run multiply domains, such as seamless GUI integration onto one common desktop, secure clipboard copy and paste between domains, secure file transfer between domains, disposable VMs, etc. Qubes also provides advanced networking infrastructure that allows for creation of multiple network VMs (that isolate all the world-facing networking stacks) and proxy VMs that could be used for advanced VPN and tunnelling over untrusted connections.
