---
layout: wiki
title: QubesArchitecture
permalink: /wiki/QubesArchitecture/
---

Qubes Architecture Overview
===========================

Qubes implements Security by Isolation approach. To do this, Qubes utilizes virtualization technology, to be able to isolate various programs from each other, and even sandbox many system-level components, like networking or storage subsystem, so that their compromise don’t affect the integrity of the rest of the system.

Qubes lets the user define many security domains implemented as lightweight Virtual Machines (VMs), or “AppVMs”. E.g. user can have “personal”, “work”, “shopping”, “bank”, and “random” AppVMs and can use the applications from within those VMs just like if they were executing on the local machine, but at the same time they are well isolated from each other. Qubes supports secure copy-and-paste and file sharing between the AppVMs, of course.

[![](http://www.qubes-os.org/Architecture_files/droppedImage.png "http://www.qubes-os.org/Architecture_files/droppedImage.png")](http://www.qubes-os.org/Architecture_files/droppedImage.png)

Key Architecture features
-------------------------

-   Based on a secure bare-metal hypervisor (Xen)
-   Networking code sand-boxed in an unprivileged VM (using IOMMU/VT-d)
-   USB stacks and drivers sand-boxed in an unprivileged VM (currently experimental feature)
-   No networking code in the privileged domain (dom0)
-   All user applications run in “AppVMs”, lightweight VMs based on Linux
-   Centralized updates of all AppVMs based on the same template
-   Qubes GUI virtualization presents applications like if they were running locally
-   Qubes GUI provides isolation between apps sharing the same desktop
-   Secure system boot based (optional)

