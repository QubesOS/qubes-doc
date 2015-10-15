---
layout: doc
title: Developers' FAQ
permalink: /en/doc/devel-faq/
redirect_from:
- /doc/DevelFaq/
- /wiki/DevelFaq/
---

Qubes Developers' FAQ
=====================

1.  1.  [Q: Why does dom0 need to be 64-bit?](#q-why-does-dom0-need-to-be-64-bit)
    2.  [Q: Why do you use KDE in Dom0? What is the roadmap for Gnome support?](#q-why-do-you-use-kde-in-dom0-what-is-the-roadmap-for-gnome-support)
    3.  [Q: What is the recommended build environment?](#q-what-is-the-recommended-build-environment)
    4.  [Q: How to build Qubes from sources?](#q-how-to-build-qubes-from-sources)
    5.  [Q: How do I submit a patch?](#q-how-do-i-submit-a-patch)

### Q: Why does dom0 need to be 64-bit?

Since 2013 [Xen has not supported 32-bit x86 architecture](http://wiki.xenproject.org/wiki/Xen_Project_Release_Features) and Intel VT-d, which Qubes uses to isolate devices and drivers, is available on Intel 64-bit processors only.

In addition, often it is more difficult to exploit a bug on the x64 Linux than it is on x86 Linux (e.g. ASLR is sometimes harder to get around). While we designed Qubes with the emphasis on limiting any potential attack vectors in the first place, still we realize that some of the code running in Dom0, e.g. our GUI daemon or xen-store daemon, even though it is very simple code, might contain some bugs. Plus currently we haven't implemented a separate storage domain, so also the disk backends are in Dom0 and are "reachable" from the VMs, which adds up to the potential attack surface. So, having faced a choice between 32-bit and 64-bit OS for Dom0, it was almost a no-brainer, as the 64-bit option provides some (little perhaps, but still) more protection against some classes of attacks, and at the same time does not have any disadvantages (except that it requires a 64-bit processor, but all systems on which it makes sense to run Qubes, e.g. that have at least 3-4GB memory, they do have 64-bit CPUs anyway).

### Q: Why do you use KDE in Dom0? What is the roadmap for Gnome support?

There are a few things that are KDE-specific, but generally it should not be a big problem to also add Gnome support to Qubes (in Dom0 of course). Those KDE-specific things are:

-   Qubes requires KDM (KDE Login Manager), rather than GDM, for the very simple reason that GDM doesn't obey standards and start `/usr/bin/Xorg` instead of `/usr/bin/X`. This is important for Qubes, because we need to load a special "X wrapper" (to make it possible to use Linux usermode shared memory to access Xen shared memory pages in our App Viewers -- see the sources [here](https://github.com/QubesOS/qubes-gui-daemon/tree/master/shmoverride)). So, Qubes makes the `/usr/bin/X` to be a symlink to the Qubes X Wrapper, which, in turn, executes the `/usr/bin/Xorg`. This works well with KDM (and would probably also work with other X login managers), but not with GDM. If somebody succeeded in makeing GDM to execute `/usr/bin/X` instead of `/usr/bin/Xorg`, we would love to hear about it!

-   We maintain a special [repository](/en/doc/kde-dom0/) for building packages specifically for Qubes Dom0.

-   We've patched the KDE's Window Manager (specifically [one of the decoration plugins](https://github.com/QubesOS/qubes-desktop-linux-kde/tree/master/plastik-for-qubes)) to draw window decorations in the color of the specific AppVM's label.

If you're interested in porting GNOME for Qubes Dom0 use, let us know -- we will most likely welcome patches in this area.

### Q: What is the recommended build environment?

Any rpm-based, 64-bit. Preferred Fedora.

### Q: How to build Qubes from sources?

See [the instruction](/en/doc/qubes-builder/)

### Q: How do I submit a patch?

See [Qubes Source Code Repositories](/en/doc/source-code/).
