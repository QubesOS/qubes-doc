---
layout: doc
title: UserFaq
permalink: /doc/UserFaq/
redirect_from: /wiki/UserFaq/
---

Qubes Users' FAQ
================

1.  [General Questions](#general-questions)
    1.  [Is Qubes just another Linux distribution?](#is-qubes-just-another-linux-distribution)
    2.  [How is Qubes different from other security solutions?](#how-is-qubes-different-from-other-security-solutions)
    3.  [What is the main concept behind Qubes?](#what-is-the-main-concept-behind-qubes)
    4.  [What about other approaches to security?](#what-about-other-approaches-to-security)
    5.  [What about safe languages and formally verified microkernels?](#what-about-safe-languages-and-formally-verified-microkernels)
    6.  [Why does Qubes use virtualization?](#why-does-qubes-use-virtualization)
    7.  [Does Qubes run every app in a separate VM?](#does-qubes-run-every-app-in-a-separate-vm)
    8.  [Why does Qubes use Xen instead of KVM or some other hypervisor?](#why-does-qubes-use-xen-instead-of-kvm-or-some-other-hypervisor)
    9.  [What about this other/new (micro)kernel/hypervisor?](#what-about-this-othernew-microkernelhypervisor)
    10. [What's so special about Qubes' GUI virtualization?](#whats-so-special-about-qubes-gui-virtualization)
    11. [Can I watch YouTube videos in AppVMs?](#can-i-watch-youtube-videos-in-appvms)
    12. [Can I run applications, like games, which require 3D support?](#can-i-run-applications-like-games-which-require-3d-support)
    13. [Is Qubes a multi-user system?](#is-qubes-a-multi-user-system)
    14. [Why passwordless sudo?](#why-passwordless-sudo)
    15. [How should I report documentation issues?](#how-should-i-report-documentation-issues)

2.  [Installation & Hardware Compatibility](#installation--hardware-compatibility)
    1.  [How much disk space does each AppVM require?](#how-much-disk-space-does-each-appvm-require)
    2.  [How much memory is recommended for Qubes?](#how-much-memory-is-recommended-for-qubes)
    3.  [Can I install Qubes on a system without VT-x?](#can-i-install-qubes-on-a-system-without-vt-x)
    4.  [Can I install Qubes on a system without VT-d?](#can-i-install-qubes-on-a-system-without-vt-d)
    5.  [Can I use AMD-v instead of VT-x?](#can-i-use-amd-v-instead-of-vt-x)
    6.  [Can I install Qubes in a virtual machine (e.g., on VMWare)?](#can-i-install-qubes-in-a-virtual-machine-eg-on-vmware)
    7.  [Why does my network adapter not work?](#why-does-my-network-adapter-not-work)

3.  [Common Problems](#common-problems)
    1.  [My AppVMs lost Internet access after a TemplateVM update. What should I do?](#my-appvms-lost-internet-access-after-a-templatevm-update-what-should-i-do)
    2.  [My keyboard layout settings are not behaving correctly. What should I do?](#my-keyboard-layout-settings-are-not-behaving-correctly-what-should-i-do)
    3.  [My dom0 and/or TemplateVM update stalls when attempting to update via …](#my-dom0-andor-templatevm-update-stalls-when-attempting-to-update-via-the-gui-tool-what-should-i-do)
    4.  [How do I run a Windows HVM in non-seamless mode (i.e., as a single window)?](#how-do-i-run-a-windows-hvm-in-non-seamless-mode-ie-as-a-single-window)
    5.  [I created a usbVM and assigned usb controllers to it. Now the usbVM wont boot.](#i-created-a-usbvm-and-assigned-usb-controllers-to-it-now-the-usbvm-wont-boot)
    6.  [I assigned a PCI device to an AppVM, then unassigned it/shut down the …](#i-assigned-a-pci-device-to-an-appvm-then-unassigned-itshut-down-the-appvm-why-isnt-the-device-available-in-dom0)

General Questions
-----------------

### Is Qubes just another Linux distribution?

If you really want to call it a distribution, then it's more of a "Xen distribution" than a Linux one. But Qubes is much more than just Xen packaging. It has its own VM management infrastructure, with support for template VMs, centralized VM updating, etc. It also has a very unique GUI virtualization infrastructure.

### How is Qubes different from other security solutions?

Please see [this article](http://theinvisiblethings.blogspot.com/2012/09/how-is-qubes-os-different-from.html) for a thorough discussion.

### What is the main concept behind Qubes?

To build security on the “Security by Isolation” principle.

### What about other approaches to security?

The other two popular [approaches](http://theinvisiblethings.blogspot.com/2008/09/three-approaches-to-computer-security.html) are “Security by Correctness” and “Security by Obscurity.” We don't believe either of these approaches are capable of providing reasonable security today, nor do we believe that they will be capable of doing so in the foreseeable future.

### What about safe languages and formally verified microkernels?

In short: these are non-realistic solutions today. We discuss this in further depth in our [Architecture Specification document](/attachment/wiki/QubesArchitecture/arch-spec-0.3.pdf).

### Why does Qubes use virtualization?

We believe that this is currently the only practically viable approach to implementing strong isolation while simultaneously providing compatibility with existing applications and drivers.

### Does Qubes run every app in a separate VM?

No! This would not make much sense. Qubes uses lightweight VMs to create security domains (e.g., "work," "personal," and "banking,"). A typical user would likely need around five domains. Very paranoid users, or those who are high-profile targets, might use a dozen or more domains.

### Why does Qubes use Xen instead of KVM or some other hypervisor?

In short: we believe the Xen architecture allows for the creation of more secure systems (i.e. with a much smaller TCB, which translates to a smaller attack surface). We discuss this in much greater depth in our [Architecture Specification document](/attachment/wiki/QubesArchitecture/arch-spec-0.3.pdf).

### What about this other/new (micro)kernel/hypervisor?

Whenever starting a discussion about another (micro)kernel or hypervisor in relation to Qubes, we strongly suggest including answers to the following questions first:

1.  What kinds of containers does it use for isolation? Processes? PV VMs? Fully virtualized VMs (HVMs)? And what underlying h/w technology is used (ring0/3, VT-x)?
2.  Does it require specially written/built applications (e.g. patched Firefox)?
3.  Does it require custom drivers, or can it use Linux/Windows ones?
4.  Does it support VT-d, and does it allow for the creation of untrusted driver domains?
5.  Does it support S3 sleep?
6.  Does it work on multiple CPUs/Chipsets?
7.  What are the performance costs, more or less? (e.g. "XYZ prevents concurrent execution of two domains/processes on shared cores of a single processor", etc.)
8.  Other special features? E.g. eliminates cooperative covert channels between VMs?

Here are the answers for Xen 4.1 (which we use as of 2014-04-28):

1.  PV and HVM Virtual Machines (ring0/3 for PV domains, VT-x/AMD-v for HVMs).
2.  Runs unmodified usermode apps (binaries).
3.  Runs unmodified Linux drivers (dom0 and driver domains). PV VMs require special written pvdrivers.
4.  Full VT-d support including untrusted driver domains.
5.  S3 sleep supported well.
6.  Works on most modern CPUs/Chipsets.
7.  Biggest performance hit on disk operations (especially in Qubes when complex 2-layer mapping used for Linux AppVMs). No GPU virtualization.
8.  Mostly Works<sup>TM</sup> :)

### What's so special about Qubes' GUI virtualization?

We have designed the GUI virtualization subsystem with two primary goals: security and performance. Our GUI infrastructure introduces only about 2,500 lines of C code (LOC) into the privileged domain (Dom0), which is very little, and thus leaves little space for bugs and potential attacks. At the same time, due to the smart use of Xen shared memory, our GUI implementation is very efficient, so most virtualized applications really feel as if they were executed natively.

### Can I watch YouTube videos in AppVMs?

Absolutely.

### Can I run applications, like games, which require 3D support?

Those won’t fly. We do not provide OpenGL virtualization for AppVMs. This is mostly a security decision, as implementing such a feature would most likely introduce a great deal of complexity into the GUI virtualization infrastructure. However, Qubes does allow for the use of accelerated graphics (OpenGL) in Dom0’s Window Manager, so all the fancy desktop effects should still work.

For further discussion about the potential for GPU passthorugh on Xen/Qubes, please see the following threads:

-   [GPU passing to HVM](https://groups.google.com/group/qubes-devel/browse_frm/thread/31f1f2da39978573?scoring=d&q=GPU&)
-   [Clarifications on GPU security](https://groups.google.com/group/qubes-devel/browse_frm/thread/31e2d8a47c8b4474?scoring=d&q=GPU&)

### Is Qubes a multi-user system?

No. Qubes does not pretend to be a multi-user system. Qubes assumes that the user who controls Dom0 controls the whole system. It would be very difficult to **securely** implement multi-user support. See [here](https://groups.google.com/group/qubes-devel/msg/899f6f3efc4d9a06) for details.

### Why passwordless sudo?

Please refer to [this page](https://www.qubes-os.org/doc/VMSudo/).

### How should I report documentation issues?

Create an issue in [qubes-issues](https://github.com/QubesOS/qubes-issues/issues), but **please make sure your issue does not already exist**. Documentation-related issues will be assigned the `doc` label. Issues which have been created in `qubes-issues` are significantly more likely to be addressed than those sent in emails to the mailing lists.

Installation & Hardware Compatibility
-------------------------------------

(See also: [System Requirements](/doc/SystemRequirements/) and [Hardware Compatibility List](/hcl/).)

### How much disk space does each AppVM require?

Each AppVM is created from a TemplateVM and shares the root filesystem with this TemplateVM (in a read-only manner). This means that each AppVM needs only as much disk space as is necessary to store its own private data. This also means that it is possible to update the software for several AppVMs simultaneously by running a single update process in the TemplateVM upon which those AppVMs are based. (These AppVMs will then have to be restarted in order for the update to take effect in them.)

### How much memory is recommended for Qubes?

At least 4 GB. It is possible to install Qubes on a system with 2 GB of RAM, but the system would probably not be able to run more than three AppVMs at a time.

### Can I install Qubes on a system without VT-x?

Yes. Xen doesn't use VT-x (or AMD-v) for PV guest virtualization. (It uses ring0/3 separation instead.) However, without VT-x, you won't be able to use fully virtualized VMs (e.g., Windows-based AppVMs), which were introduced in Qubes 2. In addition, if your system lacks VT-x, then it also lacks VT-d. (See next question.)

### Can I install Qubes on a system without VT-d?

Yes. You can even run a NetVM, but you will not benefit from DMA protection for driver domains. On a system without VT-d, everything should work in the same way, except there will be no real security benefit to having a separate NetVM, as an attacker could always use a simple DMA attack to go from the NetVM to Dom0. **Nonetheless, all of Qubes' other security mechanisms, such as AppVM separation, work without VT-d. Therefore, a system running Qubes will still be significantly more secure than one running Windows, Mac, or Linux, even if it lacks VT-d.**

### Can I use AMD-v instead of VT-x?

See [this message](http://groups.google.com/group/qubes-devel/msg/6412170cfbcb4cc5).

### Can I install Qubes in a virtual machine (e.g., on VMWare)?

Some users have been able to do this, but it is neither recommended nor supported. Qubes should be installed bare-metal. (After all, it uses its own bare-metal hypervisor!)

### Why does my network adapter not work?

You may have an adapter (wired, wireless), that is not compatible with open-source drivers shipped by Qubes. There may be a binary blob, which provides drivers in the linux-firmware package.

Open a terminal and run `sudo yum install linux-firmware` in the TemplateVM upon which your NetVM is based. You have to restart the NetVM after the TemplateVM has been shut down.

Common Problems
---------------

### My AppVMs lost Internet access after a TemplateVM update. What should I do?

Run `systemctl enable NetworkManager-dispatcher.service` in the TemplateVM upon which your NetVM is based. You may have to reboot afterward for the change to take effect. (Note: This is an upstream problem. See [here](https://bugzilla.redhat.com/show_bug.cgi?id=974811). For details, see the qubes-users mailing list threads [here](https://groups.google.com/d/topic/qubes-users/xPLGsAJiDW4/discussion) and [here](https://groups.google.com/d/topic/qubes-users/uN9G8hjKrGI/discussion).)

### My keyboard layout settings are not behaving correctly. What should I do?

Please read [this disccusion](https://groups.google.com/d/topic/qubes-devel/d8ZQ_62asKI/discussion).

### My dom0 and/or TemplateVM update stalls when attempting to update via the GUI tool. What should I do?

This can usually be fixed by updating via the command line.

In dom0, open a terminal and run `sudo qubes-dom0-update`.

In your TemplateVMs, open a terminal and run `sudo yum upgrade`.

### How do I run a Windows HVM in non-seamless mode (i.e., as a single window)?

Enable "debug mode" in the AppVM's settings, either by checking the box labelled "Run in debug mode" in the Qubes VM Manager AppVM settings menu or by running the [qvm-prefs command](/doc/Dom0Tools/QvmPrefs/).)


### I created a usbVM and assigned usb controllers to it. Now the usbVM wont boot.


This is probably because one of the controllers does not support reset. In Qubes R2 any such errors were ignored but in Qubes R3.0 they are not.
A device that does not support reset is not safe and generally should not be assigned to a VM.

Most likely the offending controller is a USB3.0 device. You can remove this controller from the usbVM, and see if this allows the VM to boot.
Alternatively you may be able to disable USB 3.0 in the BIOS.

Another solution would be to set the pci_strictreset option using qvm-prefs in dom0:

`qvm-prefs usbVM -s pci_strictreset false`

This option allows the VM to ignore the error and the VM will start.
Please review the note on [this page](https://www.qubes-os.org/doc/Dom0Tools/QvmPrefs/) and be aware of the potential risk.





### I assigned a PCI device to an AppVM, then unassigned it/shut down the AppVM. Why isn't the device available in dom0?

This is an intended feature. A device which was previously assigned to a less trusted AppVM could attack dom0 if it were automatically reassigned there. In order to re-enable the device in dom0, either:

1.  Reboot the physical machine.

or

1.  Go to the sysfs (`/sys/bus/pci`), find the right device, detach it from the pciback driver and attach back to the original driver. Replace `<BDF>` with your device, for example `00:1c.2`:
        
        echo 0000:<BDF> > /sys/bus/pci/drivers/pciback/unbind
        MODALIAS=`cat /sys/bus/pci/devices/0000:<BDF>/modalias`
        MOD=`modprobe -R $MODALIAS | head -n 1`
        echo <BDF> > /sys/bus/pci/drivers/$MOD/bind 
