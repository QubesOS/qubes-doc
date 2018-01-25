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

### What is the main concept behind Qubes?

To build security on the "Security by Compartmentalization (or Isolation)" principle.

### What about other approaches to security?

The other two popular [approaches](https://blog.invisiblethings.org/2008/09/02/three-approaches-to-computer-security.html) are “Security by Correctness” and “Security by Obscurity.” 
We don't believe either of these approaches are capable of providing reasonable security today, nor do we believe that they will be capable of doing so in the foreseeable future.

### How is Qubes different from other security solutions?

Please see [this article](https://blog.invisiblethings.org/2012/09/12/how-is-qubes-os-different-from.html) for a thorough discussion.

### Is Qubes just another Linux distribution?

If you really want to call it a distribution, then it's more of a "Xen distribution" than a Linux one. 
But Qubes is much more than just Xen packaging. 
It has its own VM management infrastructure, with support for template VMs, centralized VM updating, etc. It also has a very unique GUI virtualization infrastructure.

### What about safe languages and formally verified microkernels?

In short: these are non-realistic solutions today. We discuss this in further depth in our [Architecture Specification document](/attachment/wiki/QubesArchitecture/arch-spec-0.3.pdf).

### Why does Qubes use virtualization?

We believe that this is currently the only practically viable approach to implementing strong isolation while simultaneously providing compatibility with existing applications and drivers.

### Does Qubes use full disk encryption (FDE)?

Yes, of course! 
Full disk encryption is enabled by default. 
Specifically, we use [`LUKS`](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup)/[`dm-crypt`](https://en.wikipedia.org/wiki/Dm-crypt). 
You can even [manually configure your encryption parameters](/doc/encryption-config/), if you like!

### What do all these terms mean?

All Qubes-specific terms are defined in the [glossary](/doc/glossary/).

### Does Qubes run every app in a separate VM?

No! This would not make much sense. Qubes uses lightweight VMs to create security qubes (e.g., "work," "personal," and "banking,"). 
A typical user would likely need around five qubes. Very paranoid users, or those who are high-profile targets, might use a dozen or more qubes.

### Why does Qubes use Xen instead of KVM or some other hypervisor?

In short: we believe the Xen architecture allows for the creation of more secure systems (i.e. with a much smaller TCB, which translates to a smaller attack surface). 
We discuss this in much greater depth in our [Architecture Specification document](/attachment/wiki/QubesArchitecture/arch-spec-0.3.pdf).

### How is Qubes affected by Xen Security Advisories (XSAs)?

See the [XSA Tracker](/security/xsa/).

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

Here is an overview of the VM virtualization modes that correspond to each Qubes OS version (as of 2018-01-13):

VM Type \ Qubes OS version         | 3.2 | 3.2+ | 4.0-rc1-3 | 4.0-rc4 |
---------------------------------- | --- | ---- | --------- | ------- |
Default VMs without PCI devices    | PV  | PVH  |    HVM    |   PVH   |
Default VMs with PCI devices       | PV  | PV   |    HVM    |   HVM   |
Stub domains - Default VMs w/o PCI | N/A | N/A  |    PV     |   N/A   |
Stub domains - Default VMs w/ PCI  | N/A | N/A  |    PV     |   PV    |
Stub domains - HVMs                | PV  | PV   |    PV     |   PV    |

("3.2+" denotes Qubes 3.2 after applying the update discussed in [QSB #37](/news/2018/01/11/qsb-37/), which will result in most VMs running in PVH mode. "N/A" means "not applicable," since PV and PVH VMs do not require stub domains.)

### What's so special about Qubes' GUI virtualization?

We have designed the GUI virtualization subsystem with two primary goals: security and performance. 
Our GUI infrastructure introduces only about 2,500 lines of C code (LOC) into the privileged domain (Dom0), which is very little, and thus leaves little space for bugs and potential attacks. 
At the same time, due to the smart use of Xen shared memory, our GUI implementation is very efficient, so most virtualized applications really feel as if they were executed natively.

### Why passwordless sudo?

Please refer to [this page](https://www.qubes-os.org/doc/vm-sudo/).

### How should I report documentation issues?

Please see the [documentation guidelines](/doc/doc-guidelines).

### Will Qubes seek to get certified under the GNU Free System Distribution Guidelines (GNU FSDG)?

Not currently, for the same reasons that [Debian is not certified](https://www.gnu.org/distros/common-distros.en.html).

### Should I trust this website?

This website is hosted via GitHub Pages behind Cloudflare ([why?](#why-does-this-website-use-cloudflare)).
Therefore, it is largely outside of our control.
We don't consider this a problem, however, since we explicitly [distrust the infrastructure](#what-does-it-mean-to-distrust-the-infrastructure).
For this reason, we don't think that anyone should place undue trust in the live version of this site on the Web.
Instead, if you want to obtain your own, trustworthy copy of this website in a secure way, you should clone our [website repo](https://github.com/QubesOS/qubesos.github.io), [verify the PGP signatures on the commits and/or tags](/security/verifying-signatures/#verifying-qubes-code) (signed by the [doc-signing keys](https://github.com/QubesOS/qubes-secpack/tree/master/keys/doc-signing)), then either [render the site on your local machine](https://github.com/QubesOS/qubesos.github.io/blob/master/README.md#instructions) or simply read the source, the vast majority of which was [intentionally written in Markdown so as to be readable as plain text for this very reason](/doc/doc-guidelines/#markdown-conventions).
We've gone to special effort to set all of this up so that no one has to trust the infrastructure and so that the contents of this website are maximally available and accessible.

### What does it mean to "distrust the infrastructure"?

A core tenet of the Qubes philosophy is "distrust the infrastructure," where "the infrastructure" refers to things like hosting providers, CDNs, DNS services, package repositories, email servers, PGP keyservers, etc. 
As a project, we focus on securing endpoints instead of attempting to secure "the middle" (i.e., the infrastructure), since one of our primary goals is to free users from being forced to entrust their security to unknown third parties.
Instead, our aim is for users to be required to trust as few entities as possible (ideally, only themselves and any known persons whom they voluntarily decide to trust).

Users can never fully control all the infrastructure they rely upon, and they can never fully trust all the entities who do control it. 
Therefore, we believe the best solution is not to attempt to make the infrastructure trustworthy, but instead to concentrate on solutions that obviate the need to do so. 
We believe that many attempts to make the infrastructure appear trustworthy actually provide only the illusion of security and are ultimately a disservice to real users. 
Since we don't want to encourage or endorse this, we make our distrust of the infrastructure explicit.

Also see: [Should I trust this website?](#should-i-trust-this-website)

### Why does this website use Cloudflare?

Three main reasons:

1. We [distrust the infrastructure](#what-does-it-mean-to-distrust-the-infrastructure), including Cloudflare.
2. It's free (as in beer). We'd have to spend either time or money to implement a solution ourselves or pay someone to do so, and we can't spare either one right now.
3. It has low admin/overhead requirements, which is very important, given how little time we have to spare.

Also see: [Should I trust this website?](#should-i-trust-this-website)

### Why doesn't this website have security feature X?

Although we caution users against [placing undue trust in this website](#should-i-trust-this-website) because we [distrust the infrastructure](#what-does-it-mean-to-distrust-the-infrastructure), we have no objection to enabling website security features when doing so is relatively costless and provides some marginal benefit to website visitors (e.g., HTTPS via Cloudflare page rules).
So, if feature X isn't enabled, it's most likely for one of three reasons:

1. Our GitHub Pages + Cloudflare platform doesn't support it.
2. Our platform supports it, but we've decided not to enable it.
3. Our platform supports it, but we're not aware that we can enable it or have forgotten to do so.
   (If it seems like this is the case, let us know!)

----------

## Users

### Can I watch YouTube videos in qubes?

Absolutely.

### Can I run applications, like games, which require 3D support?

Those won’t fly. 
We do not provide OpenGL virtualization for Qubes. 
This is mostly a security decision, as implementing such a feature would most likely introduce a great deal of complexity into the GUI virtualization infrastructure. 
However, Qubes does allow for the use of accelerated graphics (OpenGL) in Dom0’s Window Manager, so all the fancy desktop effects should still work.

For further discussion about the potential for GPU passthrough on Xen/Qubes, please see the following threads:

-   [GPU passing to HVM](https://groups.google.com/group/qubes-devel/browse_frm/thread/31f1f2da39978573?scoring=d&q=GPU&)
-   [Clarifications on GPU security](https://groups.google.com/group/qubes-devel/browse_frm/thread/31e2d8a47c8b4474?scoring=d&q=GPU&)

### Is Qubes a multi-user system?

No. 
Qubes does not pretend to be a multi-user system. 
Qubes assumes that the user who controls Dom0 controls the whole system. 
It is very difficult to **securely** implement multi-user support. 
See [here](https://groups.google.com/group/qubes-devel/msg/899f6f3efc4d9a06) for details.

However, in Qubes 4.x we will be implementing management functionality. See [Admin API](https://www.qubes-os.org/news/2017/06/27/qubes-admin-api/) and [Core Stack](https://www.qubes-os.org/news/2017/10/03/core3/) for more details.


### What are the system requirements for Qubes OS?

See the [System Requirements](/doc/system-requirements/).

### Is there a list of hardware that is compatible with Qubes OS?

See the [Hardware Compatibility List](/hcl/).

### Is there any certified hardware for Qubes OS?

See [Certified Hardware](/doc/certified-hardware/).

### How much disk space does each qube require?

Each qube is created from a TemplateVM and shares the root filesystem with this TemplateVM (in a read-only manner). 
This means that each qube needs only as much disk space as is necessary to store its own private data. 
This also means that it is possible to update the software for several qubes simultaneously by running a single update process in the TemplateVM upon which those qubes are based. 
(These qubes will then have to be restarted in order for the update to take effect in them.)

### How much memory is recommended for Qubes?

At least 4 GB, but 8 GB is more realistic. 
It is possible to install Qubes on a system with 2 GB of RAM, but the system would probably not be able to run more than three qubes at a time.

### Can I install Qubes 4.x on a system without VT-x or VT-d?

Qubes 4.x requires Intel VT-x with EPT / AMD-V with RVI (SLAT) and Intel VT-d / AMD-Vi (aka AMD IOMMU) for proper functionality (see the [4.x System Requirements](/doc/system-requirements/#qubes-release-4x)). You may be able to install it without the required CPU features for testing purposes only, but VMs may not function correctly and there will be no security isolation. For more information, see our post on [updated requirements for Qubes-certified hardware](/news/2016/07/21/new-hw-certification-for-q4/).

### Can I install Qubes 3.2 on a system without VT-x?

Yes. 
Xen doesn't use VT-x (or AMD-v) for PV guest virtualization. 
(It uses ring0/3 separation instead.) 
However, without VT-x, you won't be able to use fully virtualized VMs (e.g., Windows-based qubes), which were introduced in Qubes 2. 
In addition, if your system lacks VT-x, then it also lacks VT-d. (See next question.)

### Can I install Qubes 3.2 on a system without VT-d?

Yes. 
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
Most attacks on NetVM / UsbVM (but not all!) require being somewhat close to the target system - for example connected to the same WiFi network, or in the case of a UsbVM, having physical acccess to a USB port.

### Can I use AMD-v instead of VT-x?

Yes, and see [this message](http://groups.google.com/group/qubes-devel/msg/6412170cfbcb4cc5).

### Can I install Qubes in a virtual machine (e.g., on VMware)?

Some users have been able to do this, but it is neither recommended nor supported. Qubes should be installed bare-metal. (After all, it uses its own bare-metal hypervisor!)

### Why does my network adapter not work?

You may have an adapter (wired, wireless), that is not compatible with open-source drivers shipped by Qubes. There may be a binary blob, which provides drivers in the linux-firmware package.

Open a terminal and run `sudo dnf install linux-firmware` (or `sudo yum install linux-firmware` in Qubes versions prior to 3.2.1) in the TemplateVM upon which your NetVM is based. You have to restart the NetVM after the TemplateVM has been shut down.

### Can I install Qubes OS together with other operating system (dual-boot/multi-boot)?

You shouldn't do that, because it poses a security risk for your Qubes OS installation. 
But if you understand the risk and accept it, read [documentation on multibooting](/doc/multiboot/), 
it begins with an explanation of the risks with such a setup.

### Which version of Qubes am I running?

See [here](/doc/version-scheme/#check-installed-version).

### My qubes lost Internet access after a TemplateVM update. What should I do?

Run `systemctl enable NetworkManager-dispatcher.service` in the TemplateVM upon which your NetVM is based. 
You may have to reboot afterward for the change to take effect. 
(Note: This is an upstream problem. See [here](https://bugzilla.redhat.com/show_bug.cgi?id=974811)). 
For details, see the qubes-users mailing list threads [here](https://groups.google.com/d/topic/qubes-users/xPLGsAJiDW4/discussion) and [here](https://groups.google.com/d/topic/qubes-users/uN9G8hjKrGI/discussion).)

### My keyboard layout settings are not behaving correctly. What should I do?

The best approach is to choose the right keyboard layout during the installation process. But if you want to change things afterwards, you can try this workaround.

Assuming XFCE desktop: in `Q` → `System Tools` → `Keyboard` → `Layout`, leave the checkbox "`Use system defaults`" checked. Do not customize the keyboard layout here.

Set the system-wide layout and options for `xorg` with the `localectl` command in `dom0`. You can use `localectl --help` as a starting point.

Example: `localectl set-x11-keymap us dell ,qwerty compose:caps`.

This generates the appropriate configuration in `/etc/X11/xorg.conf.d/00-keyboard.conf`. This file is auto-generated. Do not edit it by hand, unless you know what you are doing.

Restarting `xorg` is required. The most straightforward way is to reboot the system.

More information in [this discussion](https://groups.google.com/d/topic/qubes-devel/d8ZQ_62asKI/discussion) and [this issue](https://github.com/QubesOS/qubes-issues/issues/1396).

### My dom0 and/or TemplateVM update stalls when attempting to update via the GUI tool. What should I do?

This can usually be fixed by updating via the command line.

In dom0, open a terminal and run `sudo qubes-dom0-update`.

In your TemplateVMs, open a terminal and run `sudo dnf upgrade` (or `sudo yum upgrade` for Qubes older than 3.2.1).

### How do I run a Windows HVM in non-seamless mode (i.e., as a single window)?

Enable "debug mode" in the qube's settings, either by checking the box labeled "Run in debug mode" in the Qubes VM Manager qube settings menu or by running the [qvm-prefs command](/doc/dom0-tools/qvm-prefs/).)

### I created a usbVM and assigned usb controllers to it. Now the usbVM wont boot.

This is probably because one of the controllers does not support reset. 
In Qubes R2 any such errors were ignored. In Qubes R3.x they are not. In R4.x, devices that are automatically added to sys-net and sys-usb on install but do not support FLR will be attached with the no-strict-reset option, but see the related warning in the last sentence in this answer.

A device that does not support reset is not ideal and generally should not be assigned to a VM.

Most likely the offending controller is a USB 3.0 device. 
You can remove this controller from the usbVM, and see if this allows the VM to boot.
Alternatively you may be able to disable USB 3.0 in the BIOS.  
If the BIOS does not have the option to disable USB 3.0, try running the following command in dom0 to [force USB 2.0 modes for the USB ports][force_usb2]:

        lspci -nn | grep USB | cut -d '[' -f3 | cut -d ']' -f1 | xargs -I@ setpci -H1 -d @ d0.l=0


Errors suggesting this issue:

 - in `xl dmesg` output:

        (XEN) [VT-D] It's disallowed to assign 0000:00:1a.0 with shared RMRR at dbe9a000 for Dom19.
        (XEN) XEN_DOMCTL_assign_device: assign 0000:00:1a.0 to dom19 failed (-1)

 - during `qvm-start sys-usb`:

        internal error: Unable to reset PCI device [...]  no FLR, PM reset or bus reset available.


Another solution would be to set the pci_strictreset option in dom0:

 - In Qubes R4.x, when attaching the PCI device to the VM (where <BDF> can be obtained from running [qvm-pci](/doc/dom0-tools/qvm-pci/)):

        qvm-pci attach -persistent -option no-strict-reset=true usbVM dom0:<BDF>

 - In Qubes R3.x, by modifying the VM's properties:

        qvm-prefs usbVM -s pci_strictreset false

These options allow the VM to ignore the error and the VM will start.
Please review the note on [this page](https://www.qubes-os.org/doc/Dom0Tools/QvmPrefs/) and be aware of the potential risk.

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

### How do I install Flash in a Debian qube?

The Debian way is to install the flashplugin-nonfree package. 
Do this in a Debian template. You will have to allow Full access in the firewall prior to installation. 
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

3. Use VLC to play your video files

For Fedora:

1. (Recommended) Clone an existing Fedora TemplateVM
2. [Enable the appropriate RPMFusion repos in the desired Fedora TemplateVM.](/doc/software-update-vm/#rpmfusion-for-a-fedora-templatevm)
3. Install VLC in that TemplateVM:

       $ sudo dnf install vlc

4. Use VLC to play your video files.

### How do I access my external drive?

The recommended approach is to pass only the specific partition you intend to use from [`sys-usb`](/doc/usb/) to another qube via [qvm-block](/doc/dom0-tools/qvm-block/). They will show up in the destination qube as `/dev/xvd*` and must be mounted manually. Another approach is to use the Qubes VM Manager. Simply insert your USB drive, right-click on the desired qube in the Qubes VM Manager list, click Attach/detach block devices, and select your desired action and device.
Although external media such as external hard drives or flash drives plugged in via USB are available in the USB qube, it is recommended not to access them directly from inside the USB qube.
See ["How to attach USB drives"](/doc/usb/#how-to-attach-usb-drives) for more information.

### My encrypted drive doesn't appear in Debian qube.

This is an issue that affects qubes based on Debian Jessie. 
The problem is fixed in Stretch, and does not affect Fedora-based qubes.

A mixed drive with some encrypted partitions appears correctly in Nautilus. 
The encrypted partitions are identified and the user is prompted for password on attempting to mount the partition.

A fully encrypted drive does not appear in Nautilus.

The work round is to manually decrypt and mount the drive:

1. attach usb device to qube - it should be attached as /dev/xvdi or similar.
2. sudo cryptsetup open /dev/xvdi bk --type luks
3. sudo cryptsetup status /dev/mapper/bk [Shows useful status]
4. sudo mount /dev/mapper/bk /mnt

The decrypted device is now available at `/mnt` - when you have finished using it unmount and close the drive.

1. sudo umount /mnt
2. sudo cryptsetup close bk --type luks
3. remove usb from qube

### Windows Update is stuck.

This has nothing to do with Qubes. 
[It's a longstanding Windows bug.](https://superuser.com/questions/951960/windows-7-sp1-windows-update-stuck-checking-for-updates)

### Fullscreen Firefox is frozen.

Press `F11` twice.

### I have weird graphics glitches like the screen turning partially black.

If it seems like the issue described in [this thread](https://github.com/QubesOS/qubes-issues/issues/2399), try disabling the window compositor:

- Q → System Tools → Window Manager Tweaks → Compositor → uncheck "Enable display compositing"

Please report (via the mailing lists) if you experience this issue, and whether disabling the compositor fixes it for you or not.

----------

## Developers

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

### Is I/O emulation component (QEMU) part of the Trusted Computing Base (TCB)?

No. Unlike many other virtualization systems, Qubes takes special effort to keep QEMU _outside_ of the TCB. 
This has been achieved thanks to the careful use of Xen's stub domain feature. 
For more details about how we improved on Xen's native stub domain use, see [here](https://blog.invisiblethings.org/2012/03/03/windows-support-coming-to-qubes.html).

[force_usb2]: https://www.systutorials.com/qa/1908/how-to-force-a-usb-3-0-port-to-work-in-usb-2-0-mode-in-linux
