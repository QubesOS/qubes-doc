---
layout: sidebar
title: Frequently Asked Questions
permalink: /faq/
redirect_from:
- /doc/user-faq/
- /en/doc/user-faq/
- /doc/UserFaq/
- /wiki/UserFaq/
- /doc/devel-faq/
- /en/doc/devel-faq/
- /doc/DevelFaq/
- /wiki/DevelFaq/
---

# Frequently Asked Questions

## General & Security

### What is Qubes OS?

Qubes OS is a security-oriented operating system (OS).
The OS is the software that runs all the other programs on a computer. 
Some examples of popular OSes are Microsoft Windows, Mac OS X, Android, and iOS.
Qubes is free and open-source software (FOSS).
This means that everyone is free to use, copy, and change the software in any way.
It also means that the source code is openly available so others can contribute to and audit it.

### Why is OS security important?

Most people use an operating system like Windows or OS X on their desktop and laptop computers.
These OSes are popular because they tend to be easy to use and usually come pre-installed on the computers people buy.
However, they present problems when it comes to security.
For example, you might open an innocent-looking email attachment or website, not realizing that you're actually allowing malware (malicious software) to run on your computer.
Depending on what kind of malware it is, it might do anything from showing you unwanted advertisements to logging your keystrokes to taking over your entire computer.
This could jeopardize all the information stored on or accessed by this computer, such as health records, confidential communications, or thoughts written in a private journal.
Malware can also interfere with the activities you perform with your computer.
For example, if you use your computer to conduct financial transactions, the malware might allow its creator to make fraudulent transactions in your name.

### Aren't antivirus programs and firewalls enough?

Unfortunately, conventional security approaches like antivirus programs and (software and/or hardware) firewalls are no longer enough to keep out sophisticated attackers.
For example, nowadays it's common for malware creators to check to see if their malware is recognized by any signature-based antivirus programs.
If it's recognized, they scramble their code until it's no longer recognizable by the antivirus programs, then send it out.
The best of these programs will subsequently get updated once the antivirus programmers discover the new threat, but this usually occurs at least a few days after the new attacks start to appear in the wild.
By then, it's too late for those who have already been compromised.
More advanced antivirus software may perform better in this regard, but it's still limited to a detection-based approach.
New zero-day vulnerabilities are constantly being discovered in the common software we all use, such as our web browsers, and no antivirus program or firewall can prevent all of these vulnerabilities from being exploited.

### How does Qubes OS provide security?

Qubes takes an approach called **security by compartmentalization**, which
allows you to compartmentalize the various parts of your digital life into
securely isolated compartments called *qubes*.

This approach allows you to keep the different things you do on your computer securely separated from each other in isolated qubes so that one qube getting compromised won't affect the others.
For example, you might have one qube for visiting untrusted websites and a different qube for doing online banking.
This way, if your untrusted browsing qube gets compromised by a malware-laden website, your online banking activities won't be at risk.
Similarly, if you're concerned about malicious email attachments, Qubes can make it so that every attachment gets opened in its own single-use [disposable qube].
In this way, Qubes allows you to do everything on the same physical computer without having to worry about a single successful cyberattack taking down your entire digital life in one fell swoop.

Moreover, all of these isolated qubes are integrated into a single, usable system.
Programs are isolated in their own separate qubes, but all windows are displayed in a single, unified desktop environment with unforgeable colored window borders so that you can easily identify windows from different security levels.
Common attack vectors like network cards and USB controllers are isolated in their own hardware qubes while their functionality is preserved through secure [networking][network], [firewalls], and [USB device management][USB].
Integrated [file] and [clipboard] copy and paste operations make it easy to work across various qubes without compromising security.
The innovative [Template] system separates software installation from software use, allowing qubes to share a root filesystem without sacrificing security (and saving disk space, to boot).
Qubes even allows you to sanitize PDFs and images in a few clicks.
Those concerned about physical hardware attacks will benefit from [Anti Evil Maid].

### How does Qubes OS provide privacy?

There can be no privacy without security, since security vulnerabilities allow privacy measures to be circumvented.
This makes Qubes exceptionally well-suited for implementing effective privacy tools.

Users concerned about privacy will appreciate the integration of [Whonix][Qubes-Whonix] into Qubes, which makes it easy to use [Tor] securely.
For more information about how to use this powerful tool correctly and safely, please see [Whonix][Qubes-Whonix].

### What about privacy in non-Whonix qubes?

Qubes OS does not claim to provide special privacy (as opposed to security) properties in non-[Whonix][Qubes-Whonix] qubes.
This includes [DisposableVMs][disposable].

For example, a standard [Fedora](/doc/templates/fedora/) qube is expected to have basically the same privacy properties as that upstream Fedora distribution, enhanced to some degree by the control Qubes provides over that qube.
For most users, this level of privacy may be good enough for many common activities.
However, users seeking more advanced privacy features should use [Whonix][Qubes-Whonix] qubes.

Privacy is far more difficult than is commonly understood.
In addition to the [web browser](https://www.torproject.org/projects/torbrowser/design/), there is also [VM fingerprinting](https://www.whonix.org/wiki/VM_Fingerprinting) and [advanced deanonymization attacks](https://www.whonix.org/wiki/Advanced_Deanonymization_Attacks) that most users have never considered (and this is just to mention a few examples).
The [Whonix Project](https://www.whonix.org/) specializes in [protecting against these risks](https://www.whonix.org/wiki/Protocol-Leak-Protection_and_Fingerprinting-Protection).

In order to achieve the same results in non-Whonix qubes (including DisposableVMs), one would have to reinvent Whonix.
Such duplication of effort makes no sense when Whonix already exists and is already integrated into Qubes OS.

Therefore, when you need privacy, you should use Whonix qubes.
Remember, though, that privacy is difficult to achieve and maintain.
Whonix is a powerful tool, but no tool is perfect.
Read the [documentation](https://www.whonix.org/wiki/Documentation) thoroughly and exercise care when using it.

### How does Qubes OS compare to using a "live CD" OS?

Booting your computer from a live CD (or DVD) when you need to perform sensitive activities can certainly be more secure than simply using your main OS, but this method still preserves many of the risks of conventional OSes.
For example, popular live OSes (such as [Tails] and other Linux distributions) are still **monolithic** in the sense that all software is still running in the same OS.
This means, once again, that if your session is compromised, then all the data and activities performed within that same session are also potentially compromised.


### How does Qubes OS compare to running VMs in a conventional OS?

Not all virtual machine software is equal when it comes to security.
You may have used or heard of VMs in relation to software like VirtualBox or VMware Workstation.
These are known as "Type 2" or "hosted" hypervisors.
(The **hypervisor** is the software, firmware, or hardware that creates and runs virtual machines.)
These programs are popular because they're designed primarily to be easy to use and run under popular OSes like Windows (which is called the **host** OS, since it "hosts" the VMs).
However, the fact that Type 2 hypervisors run under the host OS means that they're really only as secure as the host OS itself.
If the host OS is ever compromised, then any VMs it hosts are also effectively compromised.

By contrast, Qubes uses a "Type 1" or "bare metal" hypervisor called [Xen].
Instead of running inside an OS, Type 1 hypervisors run directly on the "bare metal" of the hardware.
This means that an attacker must be capable of subverting the hypervisor itself in order to compromise the entire system, which is vastly more difficult.

Qubes makes it so that multiple VMs running under a Type 1 hypervisor can be securely used as an integrated OS.
For example, it puts all of your application windows on the same desktop with special colored borders indicating the trust levels of their respective VMs.
It also allows for things like secure copy/paste operations between VMs, securely copying and transferring files between VMs, and secure networking between VMs and the Internet.


### How does Qubes OS compare to using a separate physical machine?

Using a separate physical computer for sensitive activities can certainly be more secure than using one computer with a conventional OS for everything, but there are still risks to consider.
Briefly, here are some of the main pros and cons of this approach relative to Qubes:

<div class="focus">
  <i class="fa fa-check"></i> <strong>Pros</strong>
</div>

 * Physical separation doesn't rely on a hypervisor. (It's very unlikely that an attacker will break out of Qubes' hypervisor, but if one were to manage to do so, one could potentially gain control over the entire system.)
 * Physical separation can be a natural complement to physical security.
	(For example, you might find it natural to lock your secure laptop in a safe when you take your unsecure laptop out with you.)

<div class="focus">
    <i class="fa fa-times"></i> <strong>Cons</strong>
</div>

 * Physical separation can be cumbersome and expensive, since we may have to obtain and set up a separate physical machine for each security level we need.
 * There's generally no secure way to transfer data between physically separate computers running conventional OSes.
	(Qubes has a secure inter-VM file transfer system to handle this.)
 * Physically separate computers running conventional OSes are still independently vulnerable to most conventional attacks due to their monolithic nature.
 * Malware which can bridge air gaps has existed for several years now and is becoming increasingly common.

(For more on this topic, please see the paper [Software compartmentalization vs. physical separation][paper-compart].)


### What is the main concept behind Qubes?

To build security on the "Security by Compartmentalization (or Isolation)" principle.

### What about other approaches to security?

The other two popular [approaches] are “Security by Correctness” and “Security by Obscurity.” 
We don't believe either of these approaches are capable of providing reasonable security today, nor do we believe that they will be capable of doing so in the foreseeable future.

### How is Qubes different from other security solutions?

Please see this [article] for a thorough discussion.

### Is Qubes just another Linux distribution?

If you really want to call it a distribution, then it's more of a "Xen distribution" than a Linux one. 
But Qubes is much more than just Xen packaging. 
It has its own VM management infrastructure, with support for template VMs, centralized VM updating, etc.
It also has a very unique GUI virtualization infrastructure.

### What about safe languages and formally verified microkernels?

In short: these are non-realistic solutions today.
We discuss this in further depth in our [Architecture Specification document].

### Why does Qubes use virtualization?

We believe that this is currently the only practically viable approach to implementing strong isolation while simultaneously providing compatibility with existing applications and drivers.

### Does Qubes use full disk encryption (FDE)?

Yes, of course! 
Full disk encryption is enabled by default. 
Specifically, we use [LUKS]/[dm-crypt]. 
You can even [manually configure your encryption parameters][custom_config] if you like!

### What do all these terms mean?

All Qubes-specific terms are defined in the [glossary]

### Does Qubes run every app in a separate VM?

No! This would not make much sense.
Qubes uses lightweight VMs to create security qubes (e.g., "work," "personal," and "banking,"). 
A typical user would likely need around five qubes.
Very paranoid users, or those who are high-profile targets, might use a dozen or more qubes.

### Why does Qubes use Xen instead of KVM or some other hypervisor?

In short: we believe the Xen architecture allows for the creation of more secure systems (i.e. with a much smaller TCB, which translates to a smaller attack surface). 
We discuss this in much greater depth in our [Architecture Specification document].

### How is Qubes affected by Xen Security Advisories (XSAs)?

See the [XSA Tracker].

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
7.  Biggest performance hit on disk operations (especially in Qubes when complex 2-layer mapping used for Linux qubes). No GPU virtualization.
8.  Mostly Works<sup>TM</sup> :)

### Which virtualization modes do VMs use?

Here is an overview of the VM virtualization modes:

VM type                                    | Mode |
------------------------------------------ | ---- |
Default VMs without PCI devices (most VMs) | PVH  |
Default VMs with PCI devices               | HVM  |
Stub domains - Default VMs w/o PCI devices | N/A  |
Stub domains - Default VMs w/ PCI devices  | PV   |
Stub domains - HVMs                        | PV   |

### What's so special about Qubes' GUI virtualization?

We have designed the GUI virtualization subsystem with two primary goals: security and performance. 
Our GUI infrastructure introduces only about 2,500 lines of C code (LOC) into the privileged domain (Dom0), which is very little, and thus leaves little space for bugs and potential attacks. 
At the same time, due to the smart use of Xen shared memory, our GUI implementation is very efficient, so most virtualized applications really feel as if they were executed natively.

### Why passwordless sudo?

Please refer to [this page].

### Why is dom0 so old?

Please see:
- [Installing and updating software in dom0]
- [Note on dom0 and EOL]

### Do you recommend coreboot as an alternative to vendor BIOS?

Yes, where it is possible to use it an open source boot firmware ought to be more trustable than a closed source implementation.
[coreboot] is as a result a requirement for [Qubes Certified Hardware].
The number of machines coreboot currently supports is limited and the use of some vendor supplied blobs is generally still required.
Where coreboot does support your machine and is not already installed, you will generally need additional hardware to flash it.
Please see the coreboot website / their IRC channel for further information.

### How should I report documentation issues?

Please see the [documentation guidelines].

### Will Qubes seek to get certified under the GNU Free System Distribution Guidelines (GNU FSDG)?

Not currently, for the same reasons that [Debian is not certified].

### Should I trust this website?

This website is hosted on [GitHub Pages][] ([why?][]).
Therefore, it is largely outside of our control.
We don't consider this a problem, however, since we explicitly [distrust the infrastructure].
For this reason, we don't think that anyone should place undue trust in the live version of this site on the Web.
Instead, if you want to obtain your own trustworthy copy of this website in a secure way, you should clone our [website repo], [verify the PGP signatures on the commits and/or tags] signed by the [doc-signing keys] (which indicates that the content has undergone review per our [documentation guidelines]), then either [render the site on your local machine][render] or simply read the source, the vast majority of which was [intentionally written in Markdown so as to be readable as plain text for this very reason][Markdown].
We've gone to special effort to set all of this up so that no one has to trust the infrastructure and so that the contents of this website are maximally available and accessible.

### What does it mean to "distrust the infrastructure"?

A core tenet of the Qubes philosophy is "distrust the infrastructure," where "the infrastructure" refers to things like hosting providers, CDNs, DNS services, package repositories, email servers, PGP keyservers, etc. 
As a project, we focus on securing endpoints instead of attempting to secure "the middle" (i.e., the infrastructure), since one of our primary goals is to free users from being forced to entrust their security to unknown third parties.
Instead, our aim is for users to be required to trust as few entities as possible (ideally, only themselves and any known persons whom they voluntarily decide to trust).

Users can never fully control all the infrastructure they rely upon, and they can never fully trust all the entities who do control it. 
Therefore, we believe the best solution is not to attempt to make the infrastructure trustworthy, but instead to concentrate on solutions that obviate the need to do so. 
We believe that many attempts to make the infrastructure appear trustworthy actually provide only the illusion of security and are ultimately a disservice to real users. 
Since we don't want to encourage or endorse this, we make our distrust of the infrastructure explicit.

Also see: [Should I trust this website?]

### Why do you use GitHub?

Three main reasons:

1. We [distrust the infrastructure] including GitHub (though there are aspects we're still [working on](https://github.com/QubesOS/qubes-issues/issues/3958)).
2. It's free (as in beer). We'd have to spend either time or money to implement a solution ourselves or pay someone to do so, and we can't spare either one right now.
3. It has low admin/overhead requirements, which is very important, given how little time we have to spare.

Also see: [Should I trust this website?]

### Why doesn't this website have security feature X?

Although we caution users against [placing undue trust in this website][Should I trust this website?] because we [distrust the infrastructure], we have no objection to enabling website security features when doing so is relatively costless and provides some marginal benefit to website visitors.
So, if feature X isn't enabled, it's most likely for one of three reasons:

1. Our GitHub Pages platform doesn't support it.
2. Our platform supports it, but we've decided not to enable it.
3. Our platform supports it, but we're not aware that we can enable it or have forgotten to do so.

If it seems like a feature that we can and should enable, please [let us know][reporting-bugs]!


## Users

### Can I watch YouTube videos in qubes?

Absolutely.

### Can I run applications, like games, which require 3D support?

Those won’t fly. 
We do not provide OpenGL virtualization for Qubes. 
This is mostly a security decision, as implementing such a feature would most likely introduce a great deal of complexity into the GUI virtualization infrastructure. 
However, Qubes does allow for the use of accelerated graphics (OpenGL) in Dom0’s Window Manager, so all the fancy desktop effects should still work.

For further discussion about the potential for GPU passthrough on Xen/Qubes, please see the following threads:

-   [GPU passing to HVM]
-   [Clarifications on GPU security]

### Is Qubes a multi-user system?

No. 
Qubes does not pretend to be a multi-user system. 
Qubes assumes that the user who controls Dom0 controls the whole system. 
It is very difficult to **securely** implement multi-user support. 
See [here] for details.

However, in Qubes 4.x we will be implementing management functionality.
See [Admin API] and [Core Stack] for more details.


### What are the system requirements for Qubes OS?

See the [System Requirements].

### Is there a list of hardware that is compatible with Qubes OS?

See the [Hardware Compatibility List].

### Is there any certified hardware for Qubes OS?

See [Certified Hardware].

### How much disk space does each qube require?

Each qube is created from a TemplateVM and shares the root filesystem with this TemplateVM (in a read-only manner). 
This means that each qube needs only as much disk space as is necessary to store its own private data. 
This also means that it is possible to update the software for several qubes simultaneously by running a single update process in the TemplateVM upon which those qubes are based. 
(These qubes will then have to be restarted in order for the update to take effect in them.)

### How much memory is recommended for Qubes?

At least 6 GB, but 8 GB is more realistic. 
It is possible to install Qubes on a system with 4 GB of RAM, but the system would probably not be able to run more than three qubes at a time.

### Can I install Qubes 4.x on a system without VT-x or VT-d?

Qubes 4.x requires Intel VT-x with EPT / AMD-V with RVI (SLAT) and Intel VT-d / AMD-Vi (aka AMD IOMMU) for proper functionality (see the [4.x System Requirements]).
If you are receiving an error message on install saying your "hardware lacks the features required to proceed", check to make sure the virtualization options are enabled in your BIOS/UEFI configuration.
You may be able to install without the required CPU features for testing purposes only, but VMs (in particular, sys-net) may not function correctly and there will be no security isolation. 
For more information, see our post on [updated requirements for Qubes-certified hardware](/news/2016/07/21/new-hw-certification-for-q4/).

### Can I install Qubes OS on a system without VT-x?

Yes, for releases 3.2.1 and below. 
Xen doesn't use VT-x (or AMD-v) for PV guest virtualization. 
(It uses ring0/3 separation instead.) 
However, without VT-x, you won't be able to use fully virtualized VMs (e.g., Windows-based qubes), which were introduced in Qubes 2. 
In addition, if your system lacks VT-x, then it also lacks VT-d. (See next question.)

### Can I install Qubes OS on a system without VT-d?

Yes, for releases 3.2.1 and below.  
You can even run a NetVM, but you will not benefit from DMA protection for driver domains. 
On a system without VT-d, everything should work in the same way, except there will be no real security benefit to having a separate NetVM, as an attacker could always use a simple DMA attack to go from the NetVM to Dom0. 
**Nonetheless, all of Qubes' other security mechanisms, such as qube separation, work without VT-d. 
Therefore, a system running Qubes will still be significantly more secure than one running Windows, Mac, or Linux, even if it lacks VT-d.**

### What is a DMA attack?

DMA is mechanism for PCI devices to access system memory (read/write).
Without VT-d, any PCI device can access all the memory, regardless to which VM it is assigned (or if it is left in dom0). 
Most PCI devices allow the driver to request an arbitrary DMA operation (like "put received network packets at this address in memory", or "get this memory area and send it to the network"). 
So, without VT-d, it gives unlimited access to the whole system. 
Now, it is only a matter of knowing where to read/write to take over the system, instead of just crashing. 
But since you can read the whole memory, it isn't that hard.

Now, how does this apply to Qubes OS? 
The above attack requires access to a PCI device, which means that it can be performed only from NetVM / UsbVM, so someone must first break into one of those VMs. 
But this isn't that hard, because there is a lot of complex code handling network traffic. 
Recent bugs include DHCP client, DNS client, etc. 
Most attacks on NetVM / UsbVM (but not all!) require being somewhat close to the target system - for example connected to the same WiFi network, or in the case of a UsbVM, having physical access to a USB port.

### Can I use AMD-v instead of VT-x?

Yes, and see [this message].

### Can I install Qubes in a virtual machine (e.g., on VMware)?

Some users have been able to do this, but it is neither recommended nor supported.
Qubes should be installed bare-metal.
(After all, it uses its own bare-metal hypervisor!)

### What is a terminal?

A [terminal emulator], nowadays often referred to as just a *terminal*, is a program which provides a text window.
Inside that window, a [shell] is typically running in it.
A shell provides a [command-line interface] where the user can enter and run [commands].

See introductions on Wikibooks: [here][intro1], [here][intro2] and [here][intro3].

### Why does my network adapter not work?

You may have an adapter (wired, wireless), that is not compatible with open-source drivers shipped by Qubes.
You may need to install a binary blob, which provides drivers, from the linux-firmware package.

Open a terminal and run `sudo dnf install linux-firmware` in the TemplateVM upon which your NetVM is based.
You have to restart the NetVM after the TemplateVM has been shut down.

### Can I install Qubes OS together with other operating system (dual-boot/multi-boot)?

You shouldn't do that, because it poses a security risk for your Qubes OS installation. 
But if you understand the risk and accept it, read [documentation on multibooting].
It begins with an explanation of the risks with such a setup.


### Which version of Qubes am I running?

See [here][version].

### My qubes lost internet access after a TemplateVM update. What should I do?

See [Update Troubleshooting](/doc/update-troubleshooting/#lost-internet-access-after-a-templatevm-update).

### My keyboard layout settings are not behaving correctly. What should I do?

The best approach is to choose the right keyboard layout during the installation process.
But if you want to change things afterwards, you can try this workaround.

Assuming XFCE desktop: in `Q` → `System Tools` → `Keyboard` → `Layout`, leave the checkbox "`Use system defaults`" checked. Do not customize the keyboard layout here.

Set the system-wide layout and options for `xorg` with the `localectl` command in `dom0`. You can use `localectl --help` as a starting point.

Example: `localectl set-x11-keymap us dell ,qwerty compose:caps`.

This generates the appropriate configuration in `/etc/X11/xorg.conf.d/00-keyboard.conf`.
This file is auto-generated.
Do not edit it by hand, unless you know what you are doing.

Restarting `xorg` is required.
The most straightforward way is to reboot the system.

More information in [this discussion][layout_discussion] and [this issue][layout_issue].

### My dom0 and/or TemplateVM update stalls when attempting to update via the GUI tool. What should I do?

This can usually be fixed by updating via the command line.

In dom0, open a terminal and run `sudo qubes-dom0-update`.

In your TemplateVMs, open a terminal and run `sudo dnf upgrade`.

### How do I run a Windows HVM in non-seamless mode (i.e., as a single window)?

Enable "debug mode" in the qube's settings, either by checking the box labeled "Run in debug mode" in the Qubes VM Manager qube settings menu or by running the `qvm-prefs` command.

### I created a usbVM and assigned usb controllers to it. Now the usbVM wont boot.

This is probably because one of the controllers does not support reset. 
See the [USB Troubleshooting guide](/doc/usb-troubleshooting/#usbvm-does-not-boot-after-creating-and-assigning-usb-controllers-to-it). 

### I assigned a PCI device to a qube, then unassigned it/shut down the qube. Why isn't the device available in dom0?

This is an intended feature. 
A device which was previously assigned to a less trusted qube could attack dom0 if it were automatically reassigned there. 
In order to re-enable the device in dom0, either:

 * Reboot the physical machine.

or

 * Go to the sysfs (`/sys/bus/pci`), find the right device, detach it from the pciback driver and attach back to the original driver. Replace `<BDF>` with your device, for example `00:1c.2`:

        echo 0000:<BDF> > /sys/bus/pci/drivers/pciback/unbind
        MODALIAS=`cat /sys/bus/pci/devices/0000:<BDF>/modalias`
        MOD=`modprobe -R $MODALIAS | head -n 1`
        echo 0000:<BDF> > /sys/bus/pci/drivers/$MOD/bind

See also [here][assign_devices].

### How do I install Flash in a Debian qube?

The Debian way is to install the flashplugin-nonfree package. 
Download this in a qubes, and copy it to a Debian template.
This will make Flash available to every qube using that template.

If you only want Flash available in one qube:

- download the Flash Player for linux (64 bit) .tar.gz from [Adobe](https://get.adobe.com/flashplayer/otherversions).
- untar the downloaded file ```tar xf install_flash_player_11_linux.x86_64.tar.gz```
- create `~/.mozilla/plugins` if it does not exist
- move `libflashhplayer.so` to `~/.mozilla/plugins`, and restart iceweasel.

### How do I play video files?

If you're having trouble playing a video file in a qube, you're probably missing the required codecs. 
The easiest way to resolve this is to install VLC Media Player and use that to play your video files. 
You can do this in multiple different TemplateVM distros (Fedora, Debian, etc.). 

For Debian:

1. (Recommended) Clone an existing Debian TemplateVM
2. Install VLC in that TemplateVM:

       $ sudo apt install vlc

3. Use VLC to play your video files.

For Fedora:

1. (Recommended) Clone an existing Fedora TemplateVM
2. [Enable the appropriate RPMFusion repos in the desired Fedora TemplateVM][Enable RPMFusion].
3. Install VLC in that TemplateVM:

       $ sudo dnf install vlc

4. Use VLC to play your video files.

### How do I access my external drive?

The recommended approach is to pass only the specific partition you intend to use from [`sys-usb`](/doc/usb/) to another qube via `qvm-block`.
They will show up in the destination qube as `/dev/xvd*` and must be mounted manually.
Another approach is to attach the entire USB drive to your destination qube. 
However, this could theoretically lead to an attack because it forces the destination qube to parse the device's partition table. 
If you believe your device is safe, you may proceed to attach it.

In Qubes 4.0, this is accomplished with the Devices Widget located in the tool tray (default top right corner, look for an icon with a yellow square). 
From the top part of the list, click on the drive you want to attach, then select the qube to attach it to. 
Although you can also attach the entire USB device to a qube by selecting it from the bottom part of the list, in general this approach should not be used because you are exposing the target qube to unnecessary additional attack surface.

Although external media such as external hard drives or flash drives plugged in via USB are available in the USB qube, it is not recommended to access them directly from inside the USB qube. 
See [Block (Storage) Devices][storage](/doc/block-devices/) for more information.

### My encrypted drive doesn't appear in Debian qube.

This is an issue that affects qubes based on Debian Jessie. 
The problem is fixed in Stretch, and does not affect Fedora-based qubes.

A mixed drive with some encrypted partitions appears correctly in Nautilus. 
The encrypted partitions are identified and the user is prompted for password on attempting to mount the partition.

A fully encrypted drive does not appear in Nautilus.

The workaround is to manually decrypt and mount the drive:

1. Attach usb device to qube - it should be attached as `/dev/xvdi` or similar.
2. `sudo cryptsetup open /dev/xvdi bk --type luks`
3. `sudo cryptsetup status /dev/mapper/bk` (Shows useful status info.)
4. `sudo mount /dev/mapper/bk /mnt`

The decrypted device is now available at `/mnt` - when you have finished using it unmount and close the drive.

1. `sudo umount /mnt`
2. `sudo cryptsetup close bk --type luks`
3. Remove usb from qube.

### Windows Update is stuck.

This has nothing to do with Qubes. 
[It's a longstanding Windows bug.](https://superuser.com/questions/951960/windows-7-sp1-windows-update-stuck-checking-for-updates)

### Fullscreen Firefox is frozen.

Press `F11` twice.

### I have weird graphics glitches like the screen turning partially black.

If it seems like the issue described in [this thread](https://github.com/QubesOS/qubes-issues/issues/2399), try disabling the window compositor:

- Q → System Tools → Window Manager Tweaks → Compositor → uncheck "Enable display compositing"

Please report (via the mailing lists) if you experience this issue, and whether disabling the compositor fixes it for you or not.

### My HVM in Qubes R4.0 won't let me start/install an OS

I see a screen popup with SeaBios and 4 lines, last one being `Probing EDD (edd=off to disable!... ok`.

From a `dom0` prompt, enter:

    qvm-prefs <HVMname> kernel ""

### When I try to install a TemplateVM, it says no match is found.

See [VM Troubleshooting](/doc/vm-troubleshooting/#no-match-found-when-trying-to-install-a-templatevm).

### I keep getting "Failed to synchronize cache for repo" errors when trying to update my Fedora templates

See [Update Troubleshooting](/doc/update-troubleshooting/#failed-to-synchronize-cache-for-repo-errors-when-updating-fedora-templates).

### I see a "Failed to start Load Kernel Modules" message on boot

The full message looks like:

```
[FAILED] Failed to start Load Kernel Modules.
See 'systemctl status systemd-modules-load.service' for details.
```
This is cosmetic only, and can safely be ignored.

### Why is Qubes so slow and how can I make it faster?

During boot, Qubes starts several virtual machines. 
Having so many qubes running at once inevitably strains the resources of your computer and causes slowness. 
The most effective way to speed up Qubes is to get more powerful hardware -- a fast CPU, a lot of memory and fast SSDs. 
Qubes is slower when reading from the disk because of the VM overhead, which is why we recommend installing it on a fast SSD.

### Could you please make my preference the default?

Wouldn't it be great if Qubes were configured just the way you like it by default with all of your favorite programs and settings?
Then you could just install Qubes without having to install any programs in it or adjust any settings!
You might even think that if a particular program or setting works so well for *you*, it would work well for *everyone*, so you'd actually be doing everyone a favor!
The problem is that Qubes has [tens of thousands of different users](/statistics/) with radically different needs and purposes.
There is no particular configuration that will be ideal for everyone (despite how much you might feel that your preference would be better for everyone), so the best we can do is to put power in the hands of users to configure their Qubes installations the way they like (subject to security constraints, of course).
Please don't ask for your favorite program to be installed by default or for some setting that obviously varies by user preference to be changed so that it matches *your* preference.
This is an incredibly selfish attitude that demonstrates a complete lack of consideration for the thousands of other Qubes users who don't happen to share your preferences.


## Developers

### Are there restrictions on the software that the Qubes developers are willing to use?

Yes.
In general, the Qubes developers will not use a piece of software unless there is an *easy* way to verify both its **integrity** and **authenticity**, preferably via PGP signatures (see [Verifying Signatures](/security/verifying-signatures/)).
Specifically:

 * If PGP signatures are used, the signing key(s) should have well-publicized fingerprint(s) verifiable via multiple independent channels or be accessible to the developers through a web of trust.
 * If the software is security-sensitive and requires communication with the outside world, a "split" implementation is highly preferred (for examples, see [Split GPG](/doc/split-gpg/) and [Split Bitcoin](/doc/split-bitcoin/)).
 * If the software has dependencies, these should be packaged and available in repos for a [current, Qubes-supported version](/doc/supported-versions/#templatevms) of Fedora (preferred) or Debian (unless all the insecure dependencies can run in an untrusted VM in a "split" implementation).
 * If the software must be built from source, the source code and any builders must be signed.
   (Practically speaking, the more cumbersome and time-consuming it is to build from source, the less likely the developers are to use it.)

### Why does dom0 need to be 64-bit?

Since 2013 [Xen has not supported 32-bit x86 architecture](https://wiki.xenproject.org/wiki/Xen_Project_Release_Features) and Intel VT-d, which Qubes uses to isolate devices and drivers, is available on Intel 64-bit processors only.

In addition, with features like improved ASLR, it is often more difficult to exploit a bug on x64 Linux than x86 Linux. 
While we designed Qubes from the beginning to limit potential attack vectors, we still realize that some of the code running in Dom0, e.g. our GUI daemon or xen-store daemon, however simple, might contain some bugs. 
Plus since we haven't implemented a separate storage domain, the disk backends are in Dom0 and are "reachable" from the VMs, which adds up to the potential attack surface. 
So, having faced a choice between 32-bit and 64-bit OS for Dom0, it was almost a no-brainer. 
The 64-bit option provides some (little perhaps, but some) more protection against some classes of attacks, and at the same time does not have any disadvantages except the extra requirement of a 64 bit processor. 
And even though Qubes now "needs" a 64 bit processor, it didn't make sense to run Qubes on a system without 3-4GB of memory, and those have 64-bit CPUs anyway.

### What is the recommended build environment for Qubes OS?

Any rpm-based, 64-bit environment, the preferred OS being Fedora.

### How do I build Qubes from sources?

See [these instructions](/doc/qubes-builder/).

### How do I submit a patch?

See the [Qubes Source Code Repositories](/doc/source-code/) article.

### What is Qubes' attitude toward changing guest distros?

We try to respect each distro's culture, where possible. 
See the discussion on issue [#1014](https://github.com/QubesOS/qubes-issues/issues/1014) for an example.

The policy is there mostly to ease maintenance, on several levels:

 * Less modifications means easier migration to new upstream distribution
   releases.
 * The upstream documentation matches the distribution running in the Qubes VM.
 * We're less likely to introduce Qubes-specific issues.
 * Each officially supported distribution (ideally) should offer the same set of
   Qubes-specific features - a change in one supported distribution should be
   followed also in others, including new future distributions.

### Is the I/O emulation component (QEMU) part of the Trusted Computing Base (TCB)?

No. Unlike many other virtualization systems, Qubes takes special effort to keep QEMU _outside_ of the TCB. 
This has been achieved thanks to the careful use of Xen's stub domain feature. 
For more details about how we improved on Xen's native stub domain use, see [here](https://blog.invisiblethings.org/2012/03/03/windows-support-coming-to-qubes.html).

[force_usb2]: https://www.systutorials.com/qa/1908/how-to-force-a-usb-3-0-port-to-work-in-usb-2-0-mode-in-linux

### Is Secure Boot supported?

UEFI Secure Boot is not supported out of the box as UEFI support in Xen is very basic.
Arguably secure boot reliance on UEFI integrity is not the best design.
The relevant binaries (shim.efi, xen.efi, kernel / initramfs) are not signed by the Qubes Team and secure boot has not been tested.
Intel TXT (used in [Anti Evil Maid](/doc/anti-evil-maid/)) at least tries to avoid or limit trust in BIOS.
See the Heads project [[1]](https://trmm.net/Heads) [[2]](http://osresearch.net/) for a better-designed non-UEFI-based secure boot scheme with very good support for Qubes.

### What is the canonical way to detect Qubes VM?

Check `/usr/share/qubes/marker-vm` file existence. Additionally, its last line contains Qubes release version (e.g., `4.0`).
The file was introduced after the initial Qubes 4.0 release.
If you need to support not-fully-updated systems, check for the existence of `/usr/bin/qrexec-client-vm`.

### Is there a way to automate tasks for continuous integration or DevOps?

Yes, Qubes natively supports automation via [Salt (SaltStack)][Salt].
There is also the unofficial [ansible-qubes toolkit][ansible].
(**Warning:** Since this is an external project that has not been reviewed or endorsed by the Qubes team, [allowing it to manage dom0 may be a security risk](/doc/security-guidelines/#dom0-precautions).)

[4.x System Requirements]: /doc/system-requirements/#qubes-release-4x 
[Admin API]: /news/2017/06/27/qubes-admin-api/
[ansible]: https://github.com/Rudd-O/ansible-qubes
[Anti Evil Maid]: /doc/anti-evil-maid/
[approaches]: https://blog.invisiblethings.org/2008/09/02/three-approaches-to-computer-security.html
[Architecture Specification document]: /attachment/wiki/QubesArchitecture/arch-spec-0.3.pdf
[article]: https://blog.invisiblethings.org/2012/09/12/how-is-qubes-os-different-from.html
[assign_devices]: /doc/assigning-devices/
[Certified Hardware]: /doc/certified-hardware/
[Clarifications on GPU security]: https://groups.google.com/group/qubes-devel/browse_frm/thread/31e2d8a47c8b4474?scoring=d&q=GPU&
[clipboard]: /doc/copy-paste
[command-line interface]: https://en.wikipedia.org/wiki/Command-line_interface
[commands]: https://en.wikipedia.org/wiki/Command_(computing)
[coreboot]: https://www.coreboot.org/ 
[Core Stack]: /news/2017/10/03/core3/
[custom_config]: /doc/custom-install/ 
[Debian is not certified]: https://www.gnu.org/distros/common-distros.en.html
[disposable]: /doc/disposablevm/
[disposable qube]: /doc/dispvm/
[distrust the infrastructure]: #what-does-it-mean-to-distrust-the-infrastructure
[dm-crypt]: https://en.wikipedia.org/wiki/Dm-crypt
[doc-signing keys]: https://github.com/QubesOS/qubes-secpack/tree/master/keys/doc-signing
[documentation guidelines]: /doc/doc-guidelines
[documentation on multibooting]: /doc/multiboot/ 
[Enable RPMFusion]: /doc/software-update-domu/#rpmfusion-for-fedora-templatevms
[file]: /doc/copying-files
[firewalls]: /doc/firewall
[GitHub Pages]: https://pages.github.com/
[glossary]: /doc/glossary/
[GPU passing to HVM]: https://groups.google.com/group/qubes-devel/browse_frm/thread/31f1f2da39978573?scoring=d&q=GPU&
[Hardware Compatibility List]: /hcl/
[here]: https://groups.google.com/group/qubes-devel/msg/899f6f3efc4d9a06
[Installing and updating software in dom0]: /doc/software-update-dom0/
[intro1]: https://en.wikibooks.org/wiki/Fedora_And_Red_Hat_System_Administration/Shell_Basics
[intro2]: https://en.wikibooks.org/wiki/A_Quick_Introduction_to_Unix
[intro3]: https://en.wikibooks.org/wiki/Bash_Shell_Scripting
[layout_discussion]: https://groups.google.com/d/topic/qubes-devel/d8ZQ_62asKI/discussion
[layout_issue]: https://github.com/QubesOS/qubes-issues/issues/1396
[LUKS]: https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup
[Markdown]: /doc/doc-guidelines/#markdown-conventions
[network]: /doc/networking/
[Note on dom0 and EOL]: /doc/supported-versions/#note-on-dom0-and-eol
[paper-compart]: https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf
[Qubes Certified Hardware]: https://www.qubes-os.org/news/2016/07/21/new-hw-certification-for-q4/
[Qubes-Whonix]: /doc/whonix/
[render]: https://github.com/QubesOS/qubesos.github.io/blob/master/README.md#instructions
[Salt]: /doc/salt/
[shell]: https://en.wikipedia.org/wiki/Shell_(computing)
[Should I trust this website?]: #should-i-trust-this-website
[storage]: /doc/block-devices/
[System Requirements]: /doc/system-requirements/
[Tails]: https://tails.boum.org/
[Template]: /doc/template-implementation 
[terminal emulator]: https://en.wikipedia.org/wiki/Terminal_emulator
[this message]: http://groups.google.com/group/qubes-devel/msg/6412170cfbcb4cc5
[this page]: /doc/vm-sudo/
[Tor]: https://www.torproject.org/
[USB]: /doc/usb-devices
[verify the PGP signatures on the commits and/or tags]: /security/verifying-signatures/#how-to-verify-qubes-repos
[version]: /doc/version-scheme/#check-installed-version
[website repo]: https://github.com/QubesOS/qubesos.github.io
[why?]: #why-do-you-use-github
[Xen]: https://www.xenproject.org/
[XSA Tracker]: /security/xsa/
[reporting-bugs]: /doc/reporting-bugs/
