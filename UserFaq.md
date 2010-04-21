---
layout: wiki
title: UserFaq
permalink: /wiki/UserFaq/
---

Qubes User's FAQ
================

### Q: How much memory is recommended for Qubes?

4 GB at least. Sure, you can try it on a system with 2GB, but don't expect to be able to run more than 3 AppVMs at the same time.

### Q: Can I install Qubes on a system without VT-x?

Yes. Xen doesn't use VT-x (not AMD-v) for PV guests virtualization (it uses ring0/3 separation instead). But, of course, without VT-x, you will also not have VT-d -- see the next question.

### Q: Can I install Qubes on a system without VT-d?

Yes you can. You can even run a netvm but, of course, you will not benefit from DMA protection for driver domains. So, on a system without VT-d, everything should work the same, but there is no real security benefit of having a separate netvm, as the attacker can always use a simple DMA attack to go from netvm to Dom0.

The above is in theory -- in practice, if you have a broken network card driver and try to run it in a netvm on a system without VT-d, it might crash your system. This might happen e.g. if the driver is not properly using DMA-API.

### Q: Can I install Qubes in a Virtual Machine, e.g. on VMWare?

Most likely no. You should install it on bare-metal. Hey, it uses its own bare-metal hypervisor, after all...

### Q: Why is Fedora 12 "strongly" recommended as dom0?

As currently Qubes do not have its own installer, we need to rely on some other Linux distribution to bring all the software needed in Dom0. We made a more-or-less arbitrary decision to choose Fedora 12 as a base for our Dom0 and we have prepared all the RPMs and tested them with the assumption that the user has installed Dom0 based on F12 according to the specific instructions we gave in the [Installation Guide](/wiki/InstallationGuide). Qubes would most likely run on other RPM-based Linux distributions, although we have never tested it, and we'd rather focus our resources on implementing other Qubes features, than on testing other distros for Dom0 support. Especially that we plan to write custom installer for Qubes anyway -- see the next question.

### Q: Do you plan to "port" Qubes to other Linux distros?

Absolutely no. The plan for the near future (see the [Roadmap](https://www.qubes-os.org/trac/roadmap)) is to create a custom (and very simple to use) Qubes installer that would automatically take care about installing the minimal Dom0 system, all the Qubes packages in Dom0, and also the Qubes template and service VMs images. In other words Qubes will evolve into a true standalone system, not based on any specific Linux distribution (well, we still will probably use Fedora RPMs for most of the packages and probably the Anaconda installer, but this will be hidden from the user).

### Q: What is the recommended way update the template VM?

Shutdown all the running AppVMs that are based on this template (normally all your AppVMs are based on the same template):

``` {.wiki}
qvm-run --shutdown --wait --all --exclude netvm
```

(In the comming weeks we will provide a graphical VM manager where you will be able to do the above with just one or two mouse clicks :)

Next, start either console, e.g. Konsole, or KPackageKit application in your Template VM (normally it's called "linux-x64"), using the KDE menu, and proceed with the updates. If you use console then you will want to use yum (you must switch to root), e.g.:

``` {.wiki}
yum update
```

If you chose KPackageKit, then you should be able to update using just your mouse.

Once the Template VM got update, shut it down, and then any AppVM you start will already be using update software.

### Q: What is the root and user password for TemplateVM/AppVM?

-   ```user/userpass```
-   ```root/rootpass```

**NOTE:** This will be changed in the next Alpha (see the ticket:24)
