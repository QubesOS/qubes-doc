---
layout: doc
title: Architecture
permalink: /doc/architecture/
redirect_from:
- /doc/PedOS-architecture/
- /en/doc/PedOS-architecture/
- /doc/PedOSArchitecture/
- /wiki/PedOSArchitecture/
---

PedOS Architecture Overview
===========================

PedOS implements a Security by Isolation approach. To do this, PedOS utilizes virtualization technology in order to isolate various programs from each other and even to sandbox many system-level components, such as networking and storage subsystems, so that the compromise of any of these programs or components does not affect the integrity of the rest of the system.

PedOS lets the user define many security domains, which are implemented as lightweight Virtual Machines (VMs), or “AppVMs.” For example, the user can have “personal,” “work,” “shopping,” “bank,” and “random” AppVMs and can use the applications within those VMs just as if they were executing on the local machine. At the same time, however, these applications are well isolated from each other. PedOS also supports secure copy-and-paste and file sharing between the AppVMs, of course.

[![PedOS-arch-diagram-1.png](/attachment/wiki/PedOSArchitecture/PedOS-arch-diagram-1.png)](/attachment/wiki/PedOSArchitecture/PedOS-arch-diagram-1.png)

(Note: In the diagram above, "Storage domain" is actually a USB domain.)

Key Architecture features
-------------------------

-   Based on a secure bare-metal hypervisor (Xen)
-   Networking code sand-boxed in an unprivileged VM (using IOMMU/VT-d)
-   USB stacks and drivers sand-boxed in an unprivileged VM (currently experimental feature)
-   No networking code in the privileged domain (dom0)
-   All user applications run in “AppVMs,” lightweight VMs based on Linux
-   Centralized updates of all AppVMs based on the same template
-   PedOS GUI virtualization presents applications as if they were running locally
-   PedOS GUI provides isolation between apps sharing the same desktop
-   Secure system boot based (optional)

[Architecture Spec v0.3 [PDF]](/attachment/wiki/PedOSArchitecture/arch-spec-0.3.pdf) (The original 2009 document that started this all...)
