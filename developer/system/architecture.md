---
layout: doc
title: Architecture
permalink: /doc/architecture/
redirect_from:
- /doc/qubes-architecture/
- /en/doc/qubes-architecture/
- /doc/QubesArchitecture/
- /wiki/QubesArchitecture/
---

Qubes Architecture Overview
===========================

Qubes implements a Security by Isolation approach. To do this, Qubes utilizes virtualization technology in order to isolate various programs from each other and even to sandbox many system-level components, such as networking and storage subsystems, so that the compromise of any of these programs or components does not affect the integrity of the rest of the system.

[![qubes-schema-v2.png](/attachment/wiki/QubesArchitecture/qubes-schema-v2.png)](/attachment/wiki/QubesArchitecture/qubes-schema-v2.png)

Qubes lets the user define many security domains, which are implemented as lightweight Virtual Machines (VMs), or “AppVMs.” For example, the user can have “personal,” “work,” “shopping,” “bank,” and “random” AppVMs and can use the applications within those VMs just as if they were executing on the local machine. At the same time, however, these applications are well isolated from each other. Qubes also supports secure copy-and-paste and file sharing between the AppVMs, of course.


Key Architecture features
-------------------------

-   Based on a secure bare-metal hypervisor (Xen)
-   Networking code sand-boxed in an unprivileged VM (using IOMMU/VT-d)
-   USB stacks and drivers sand-boxed in an unprivileged VM (currently experimental feature)
-   No networking code in the privileged domain (dom0)
-   All user applications run in “AppVMs,” lightweight VMs based on Linux
-   Centralized updates of all AppVMs based on the same template
-   Qubes GUI virtualization presents applications as if they were running locally
-   Qubes GUI provides isolation between apps sharing the same desktop
-   Secure system boot based (optional)

(For those interested in the history of the project, [Architecture Spec v0.3 [PDF]](/attachment/wiki/QubesArchitecture/arch-spec-0.3.pdf) is the original 2009 document that started this all.)


Qubes Core Stack
----------------

Qubes Core Stack is, as the name implies, the core component of Qubes OS. It's
the glue that connects all the other components together, and which allows users
and admins to interact with and configure the system. The other components of
the Qubes system include:

 - VM-located core agents (implementing e.g. qrexec endpoints used by various
   Qubes services)
 - VM-customizations (making the VMs lightweight and working well with seamless
   GUI virtualization)
 - Qubes GUI virtualization (the protocol, VM-located agents, and daemons
   located in the GUI domain which, for now, happens to be the same as dom0),
 - GUI domain customizations (Desktop Environment customizations, decoration
   coloring plugin, etc)
 - The AdminVM distribution (various customizations, special services, such as
   for receiving and verifying updates, in the future: custom distro)
 - The Xen hypervisor (with a bunch of customization patches, occasional
   hardening) or - in the future - some other virtualising or containerizing
   software or technology
 - Multiple "Qubes Apps" (various services built on top of Qubes qrexec
   infrastructure, such as: trusted PDF and Image converters, Split GPG, safe
   USB proxies for HID devices, USB proxy for offering USB devices (exposed via
   qvm-usb), Yubikey support, USB Armory support, etc)
 - Various ready-to-use templates (e.g. Debian-, Whonix-based), which are used
   to create actual VMs, i.e. provide the root filesystem to the VMs
 - Salt Stack integration

And all these components are "glued together" by the Qubes Core Stack.

[![Qubes system components](/attachment/wiki/QubesArchitecture/qubes-components.png)](/attachment/wiki/QubesArchitecture/qubes-components.png)

This diagram illustrates the location of all these components in the overall
system architecture. Unlike the other Qubes architecture diagram above, this one
takes an AppVM-centric approach.

