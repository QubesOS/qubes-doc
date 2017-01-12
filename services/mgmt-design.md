---
layout: doc-full
title: Management API
permalink: /doc/mgmt-architecture/
---

# Qubes OS Management Architecture

*(This page is the current draft of the proposal. It is not implemented yet.)*

## Goals

The goals of the management system is to provide a way for the user to manage
the domains without direct access to dom0.

Foreseen benefits include:

- Ability to remotely manage the Qubes OS.
- Possibility to create multi-user system, where different users are able to use
  different sets of domains, possibly overlapping. This would also require to
  have separate GUI domain.

The API would be used by:

- Qubes OS Manager (or any tools that would replace it)
- CLI tools, when run from another VM (and possibly also from dom0)
- remote management tools
- any custom tools

## Threat model

TBD

## Components

![Management Architecture][mgmt-architecture]

A central entity in the Qubes management system is a `qubesd` daemon, which
holds information about all domains in the system and mediates all actions (like
starting and stopping a qube) with `libvirtd`. The `qubesd` daemon also manages
the `qubes.xml` file, which stores all persistent state information and
dispatches events to extensions. Last but not least, `qubesd` is responsible for
querying the RPC policy for qrexec daemon.

The `qubesd` daemon may be accessed from other domains through a set of qrexec
API calls called the [management API][mgmt1]. This API is the intended
management interface supported by the Qubes OS. The API is stable. When called,
the RPC handler performs basic validation and forwards the request to the
`qubesd` via UNIX domain socket. The socket API is private and unstable. It is
documented [FIXME currently it isn't -- woju 20161221] in the developer's
documentation of the source code.

[mgmt1]: ../mgmt1/

[mgmt-architecture]: /attachment/wiki/mgmt/mgmt-architecture.svg
