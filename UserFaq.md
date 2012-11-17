---
layout: wiki
title: UserFaq
permalink: /wiki/UserFaq/
---

Qubes User's FAQ
================

1.  [General Questions](#GeneralQuestions)
    1.  [Isn’t Qubes just another Linux distribution after all?](#IsntQubesjustanotherLinuxdistributionafterall)
    2.  [How is Qubes different from other security solutions?](#HowisQubesdifferentfromothersecuritysolutions)
    3.  [What is the main concept behind Qubes?](#WhatisthemainconceptbehindQubes)
    4.  [What about other approaches to security?](#Whataboutotherapproachestosecurity)
    5.  [But what about safe languages and formally verified microkernels?](#Butwhataboutsafelanguagesandformallyverifiedmicrokernels)
    6.  [Why Qubes uses virtualization?](#WhyQubesusesvirtualization)
    7.  [Does Qubes run every app in a separate VM?](#DoesQubesruneveryappinaseparateVM)
    8.  [Why Qubes uses Xen, and not e.g. KVM or some other hypervisor?](#WhyQubesusesXenandnote.g.KVMorsomeotherhypervisor)
    9.  [What is so special about Qubes GUI virtualization?](#WhatissospecialaboutQubesGUIvirtualization)
    10. [Can I watch movies in AppVMs, e.g. YouTube? movies?](#CanIwatchmoviesinAppVMse.g.YouTubemovies)
    11. [How about running applications like games that required 3D support?](#Howaboutrunningapplicationslikegamesthatrequired3Dsupport)
    12. [Is Qubes a multi-user system?](#IsQubesamulti-usersystem)

2.  [Installation/hardware compatibility](#Installationhardwarecompatibility)
    1.  [How much disk space do I need for each AppVM?](#HowmuchdiskspacedoIneedforeachAppVM)
    2.  [How much memory is recommended for Qubes?](#HowmuchmemoryisrecommendedforQubes)
    3.  [Can I install Qubes on a system without VT-x?](#CanIinstallQubesonasystemwithoutVT-x)
    4.  [Can I install Qubes on a system without VT-d?](#CanIinstallQubesonasystemwithoutVT-d)
    5.  [Can I use AMD-v instead of VT-x?](#CanIuseAMD-vinsteadofVT-x)
    6.  [Can I install Qubes in a Virtual Machine, e.g. on VMWare?](#CanIinstallQubesinaVirtualMachinee.g.onVMWare)

General Questions
-----------------

### Isn’t Qubes just another Linux distribution after all?

Well, if you really want to call it a distribution, then we’re more of a “Xen distribution”, rather then a Linux one. But Qubes is much more than just Xen packaging -- it has its own VM management infrastructure, with support for template VMs, centralized VM updating, etc, and also its very unique GUI virtualization infrastructure.

### How is Qubes different from other security solutions?

Please see [​this article](http://theinvisiblethings.blogspot.com/2012/09/how-is-qubes-os-different-from.html) for a more thorough discussion discussion.

### What is the main concept behind Qubes?

To build security on the “Security by Isolation” principle.

### What about other approaches to security?

The other two popular [​approaches](http://theinvisiblethings.blogspot.com/2008/09/three-approaches-to-computer-security.html) are: “Security by Correctness”, and “Security by Obscurity”. We don’t believe any of those two can bring reasonable security today and in the foreseeable future.

### But what about safe languages and formally verified microkernels?

In short: these are non-realistic solutions today. We discuss this more in-depth in our [​Architecture Specification document](http://qubes-os.org/files/doc/arch-spec-0.3.pdf).

### Why Qubes uses virtualization?

We believe that today this is the only practically viable approach to implement strong isolation, and, at the same time, provide compatibility with existing applications and drivers.

### Does Qubes run every app in a separate VM?

No! This would not make much sense. Qubes uses lightweight VMs to create security domains, such as e.g. ‘work’, ‘personal’, ‘banking’, etc. Typical user would likely need around 5 domains. Very paranoid users, who are high-profile targets. might use around a dozen or more domains.

### Why Qubes uses Xen, and not e.g. KVM or some other hypervisor?

In short: we believe the Xen architecture allows to create more secure systems, i.e. with much smaller TCB, which translates to smaller attack surface. We discuss this much more in-depth in our [​Architecture Specification document](http://qubes-os.org/files/doc/arch-spec-0.3.pdf).

### What is so special about Qubes GUI virtualization?

We have designed the GUI virtualization subsystem with two primary goals: security and performance. Our GUI infrastructure introduces only about 2,500 lines of C code (LOC) into the privileged domain (Dom0), which is very little, and thus leaves not much space for bugs and potential attacks. At the same time, due to smart use of Xen shared memory our GUI implementation is very efficient, so most virtualized applications really feel like if they were executed natively.

### Can I watch movies in AppVMs, e.g. [YouTube?](/wiki/YouTube) movies?

Absolutely.

### How about running applications like games that required 3D support?

Those won’t fly. We do not provide OpenGL virtualization for AppVMs. This is mostly a security decision, as implementing such feature would most likely introduce lots of complexity to the GUI virtualization infrastructure. However, Qubes allows for use of accelerated graphics (OpenGL) in Dom0’s Window Manager, so all the fancy desktop effects should still work under Qubes.

### Is Qubes a multi-user system?

No, Qubes does not pretend to be a multi-user system. Qubes assumes that the user that controls Dom0, controls the whole system. It will be very difficult to **securely** implement multi-user support -- see this message:

[​https://groups.google.com/group/qubes-devel/msg/899f6f3efc4d9a06](https://groups.google.com/group/qubes-devel/msg/899f6f3efc4d9a06)

Installation/hardware compatibility
-----------------------------------

### How much disk space do I need for each AppVM?

Every AppVM is created from a so called TemplateVM and they share the root filesystem with the template (in a read-only manner). This means each AppVM needs only disk space for its own private data. This also means that it is possible to update the software for all the AppVMs by just running the update process in the TemplateVM once (one needs to stop all the AppVMs for this, of course).

### How much memory is recommended for Qubes?

4 GB at least. Sure, you can try it on a system with 2GB, but don't expect to be able to run more than 3 AppVMs at the same time...

### Can I install Qubes on a system without VT-x?

Yes. Xen doesn't use VT-x (nor AMD-v) for PV guests virtualization (it uses ring0/3 separation instead). But, of course, without VT-x, you will also not have VT-d -- see the next question.

Also, without VT-x you won't be able to use fully virtualized VMs (e.g. Windows-based AppVMs) that are to be introduced in Qubes 2.

### Can I install Qubes on a system without VT-d?

Yes you can. You can even run a netvm but, of course, you will not benefit from DMA protection for driver domains. So, on a system without VT-d, everything should work the same, but there is no real security benefit of having a separate netvm, as the attacker can always use a simple DMA attack to go from netvm to Dom0.

**But still, all the other Qubes security mechanisms, such as AppVM separation, work as usual, and you still end up with a significantly secure OS, much more secure then Windows, Mac, or Linux, even if you don't have VT-d'''**

### Can I use AMD-v instead of VT-x?

See [​this message](http://groups.google.com/group/qubes-devel/msg/6412170cfbcb4cc5).

### Can I install Qubes in a Virtual Machine, e.g. on VMWare?

Most likely no. You should install it on bare-metal. Hey, it uses its own bare-metal hypervisor, after all...
