---
layout: wiki
title: UserFaq
permalink: /wiki/UserFaq/
---

Qubes User's FAQ
================

1.  [General Questions](#GeneralQuestions)
    1.  [Is Qubes just another Linux distribution?](#IsQubesjustanotherLinuxdistribution)
    2.  [How is Qubes different from other security solutions?](#HowisQubesdifferentfromothersecuritysolutions)
    3.  [What is the main concept behind Qubes?](#WhatisthemainconceptbehindQubes)
    4.  [What about other approaches to security?](#Whataboutotherapproachestosecurity)
    5.  [What about safe languages and formally verified microkernels?](#Whataboutsafelanguagesandformallyverifiedmicrokernels)
    6.  [Why does Qubes use virtualization?](#WhydoesQubesusevirtualization)
    7.  [Does Qubes run every app in a separate VM?](#DoesQubesruneveryappinaseparateVM)
    8.  [Why does Qubes use Xen instead of KVM or some other hypervisor?](#WhydoesQubesuseXeninsteadofKVMorsomeotherhypervisor)
    9.  [What's so special about Qubes' GUI virtualization?](#WhatssospecialaboutQubesGUIvirtualization)
    10. [Can I watch YouTube videos in AppVMs?](#CanIwatchYouTubevideosinAppVMs)
    11. [Can I run applications, like games, which require 3D support?](#CanIrunapplicationslikegameswhichrequire3Dsupport)
    12. [Is Qubes a multi-user system?](#IsQubesamulti-usersystem)

2.  [Installation & Hardware Compatibility](#InstallationHardwareCompatibility)
    1.  [How much disk space does each AppVM require?](#HowmuchdiskspacedoeseachAppVMrequire)
    2.  [How much memory is recommended for Qubes?](#HowmuchmemoryisrecommendedforQubes)
    3.  [Can I install Qubes on a system without VT-x?](#CanIinstallQubesonasystemwithoutVT-x)
    4.  [Can I install Qubes on a system without VT-d?](#CanIinstallQubesonasystemwithoutVT-d)
    5.  [Can I use AMD-v instead of VT-x?](#CanIuseAMD-vinsteadofVT-x)
    6.  [Can I install Qubes in a virtual machine (e.g., on VMWare)?](#CanIinstallQubesinavirtualmachinee.g.onVMWare)

General Questions
-----------------

### Is Qubes just another Linux distribution?

If you really want to call it a distribution, then it's more of a "Xen distribution" than a Linux one. But Qubes is much more than just Xen packaging. It has its own VM management infrastructure, with support for template VMs, centralized VM updating, etc. It also has a very unique GUI virtualization infrastructure.

### How is Qubes different from other security solutions?

Please see [​this article](http://theinvisiblethings.blogspot.com/2012/09/how-is-qubes-os-different-from.html) for a thorough discussion.

### What is the main concept behind Qubes?

To build security on the “Security by Isolation” principle.

### What about other approaches to security?

The other two popular [​approaches](http://theinvisiblethings.blogspot.com/2008/09/three-approaches-to-computer-security.html) are “Security by Correctness” and “Security by Obscurity.” We don't believe either of these approaches are capable of providing reasonable security today, nor do we believe that they will be capable of doing so in the foreseeable future.

### What about safe languages and formally verified microkernels?

In short: these are non-realistic solutions today. We discuss this in further depth in our [​Architecture Specification document](http://files.qubes-os.org/files/doc/arch-spec-0.3.pdf).

### Why does Qubes use virtualization?

We believe that this is currently the only practically viable approach to implementing strong isolation while simultaneously providing compatibility with existing applications and drivers.

### Does Qubes run every app in a separate VM?

No! This would not make much sense. Qubes uses lightweight VMs to create security domains (e.g., "work," "personal," and "banking,"). A typical user would likely need around five domains. Very paranoid users, or those who are high-profile targets, might use a dozen or more domains.

### Why does Qubes use Xen instead of KVM or some other hypervisor?

In short: we believe the Xen architecture allows for the creation of more secure systems (i.e. with a much smaller TCB, which translates to a smaller attack surface). We discuss this in much greater depth in our [​Architecture Specification document](http://files.qubes-os.org/files/doc/arch-spec-0.3.pdf).

### What's so special about Qubes' GUI virtualization?

We have designed the GUI virtualization subsystem with two primary goals: security and performance. Our GUI infrastructure introduces only about 2,500 lines of C code (LOC) into the privileged domain (Dom0), which is very little, and thus leaves little space for bugs and potential attacks. At the same time, due to the smart use of Xen shared memory, our GUI implementation is very efficient, so most virtualized applications really feel as if they were executed natively.

### Can I watch YouTube videos in AppVMs?

Absolutely.

### Can I run applications, like games, which require 3D support?

Those won’t fly. We do not provide OpenGL virtualization for AppVMs. This is mostly a security decision, as implementing such a feature would most likely introduce a great deal of complexity into the GUI virtualization infrastructure. However, Qubes does allow for the use of accelerated graphics (OpenGL) in Dom0’s Window Manager, so all the fancy desktop effects should still work.

For further discussion about the potential for GPU passthorugh on Xen/Qubes, please see the following threads:

-   [​GPU passing to HVM](https://groups.google.com/group/qubes-devel/browse_frm/thread/31f1f2da39978573?scoring=d&q=GPU&)
-   [​Clarifications on GPU security](https://groups.google.com/group/qubes-devel/browse_frm/thread/31e2d8a47c8b4474?scoring=d&q=GPU&)

### Is Qubes a multi-user system?

No. Qubes does not pretend to be a multi-user system. Qubes assumes that the user who controls Dom0 controls the whole system. It would be very difficult to **securely** implement multi-user support. See [​here](https://groups.google.com/group/qubes-devel/msg/899f6f3efc4d9a06) for details.]

Installation & Hardware Compatibility
-------------------------------------

(See also: [System Requirements](/wiki/SystemRequirements) and [Hardware Compatibility List](/wiki/HCL).)

### How much disk space does each AppVM require?

Each AppVM is created from a TemplateVM and shares the root filesystem with this TemplateVM (in a read-only manner). This means that each AppVM needs only as much disk space as is necessary to store its own private data. This also means that it is possible to update the software for several AppVMs simultaneously by running a single update process in the TemplateVM upon which those AppVMs are based. (These AppVMs will then have to be restarted in order for the update to take effect in them.)

### How much memory is recommended for Qubes?

At least 4 GB. It is possible to install Qubes on a system with 2 GB of RAM, but the system would probably not be able to run more than three AppVMs at a time.

### Can I install Qubes on a system without VT-x?

Yes. Xen doesn't use VT-x (or AMD-v) for PV guest virtualization. (It uses ring0/3 separation instead.) However, without VT-x, you won't be able to use fully virtualized VMs (e.g., Windows-based AppVMs), which were introduced in Qubes 2. In addition, if your system lacks VT-x, then it also lacks VT-d. (See next question.)

### Can I install Qubes on a system without VT-d?

Yes. You can even run a NetVM, but you will not benefit from DMA protection for driver domains. On a system without VT-d, everything should work in the same way, except there will be no real security benefit to having a separate NetVM, as an attacker could always use a simple DMA attack to go from the NetVM to Dom0. **Nonetheless, all of Qubes' other security mechanisms, such as AppVM separation, work without VT-d. Therefore, a system running Qubes will still be significantly more secure than one running Windows, Mac, or Linux, even if it lacks VT-d.**

### Can I use AMD-v instead of VT-x?

See [​this message](http://groups.google.com/group/qubes-devel/msg/6412170cfbcb4cc5).

### Can I install Qubes in a virtual machine (e.g., on VMWare)?

Some users have been able to do this, but it is neither recommended nor supported. Qubes should be installed bare-metal. (After all, it uses its own bare-metal hypervisor!)
