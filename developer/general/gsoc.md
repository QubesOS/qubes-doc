---
layout: sidebar
title: Google Summer of Code
permalink: /gsoc/
redirect_from: /GSoC/
---

2020 Google Summer of Code
================
## Information for Students

Thank you for your interest in participating in the [Google Summer of Code program][gsoc-qubes] with the [Qubes OS team][team]. You can read more about the Google Summer of Code program at the [official website][gsoc] and the [official FAQ][gsoc-faq].

Being accepted as a Google Summer of Code student is quite competitive. Students wishing to participate in the Summer of Code must be aware that you will be required to produce code for Qubes OS for 3 months. Your mentors, Qubes developers, will dedicate a portion of their time towards mentoring you. Therefore, we seek candidates who are committed to helping Qubes long-term and are willing to do quality work and be proactive in communicating with your mentor.

You don't have to be a proven developer -- in fact, this whole program is meant to facilitate joining Qubes and other free and open source communities. The Qubes community maintains information about [contributing to Qubes development][contributing] and [how to send patches][patches]. In order to contribute code to the Qubes project, you must be able to [sign your code][code-signing].

You should start learning the components that you plan on working on before the start date. Qubes developers are available on the [mailing lists][ml-devel] for help. The GSoC timeline reserves a lot of time for bonding with the project -- use that time wisely. Good communication is key, you should plan to communicate with your team daily and formally report progress and plans weekly. Students who neglect active communication will be failed.

You can view the projects we had in 2017 in the [GSoC archive here][2017-archive].

### Overview of Steps

- Join the [qubes-devel list][ml-devel] and introduce yourself, and meet your fellow developers
- Read [Google's instructions for participating][gsoc-participate] and the [GSoC Student Manual][gsoc-student]
- Take a look at the list of ideas below
- Come up with a project that you are interested in (and feel free to propose your own! Don't feel limited by the list below.)
- Read the Student Proposal guidelines below
- Write a first draft proposal and send it to the qubes-devel mailing list for review
- Submit proposal using [Google's web interface][gsoc-submit] ahead of the deadline (this requires a Google Account!)
- Submit proof of enrollment well ahead of the deadline

Coming up with an interesting idea that you can realistically achieve in the time available to you (one summer) is probably the most difficult part. We strongly recommend getting involved in advance of the beginning of GSoC, and we will look favorably on applications from students who have already started to act like free and open source developers.

Before the summer starts, there are some preparatory tasks which are highly encouraged. First, if you aren't already, definitely start using Qubes as your primary OS as soon as possible! Also, it is encouraged that you become familiar and comfortable with the Qubes development workflow sooner than later. A good way to do this (and also a great way to stand out as an awesome applicant and make us want to accept you!) might be to pick up some issues from [qubes-issues][qubes-issues] (our issue-tracking repo) and submit some patches addressing them. Some suitable issues might be those with tags ["help wanted" and "P: minor"][qubes-issues-suggested] (although more significant things are also welcome, of course). Doing this will get you some practice with [qubes-builder][qubes-builder], our code-signing policies, and some familiarity with our code base in general so you are ready to hit the ground running come summer.

### Student proposal guidelines

A project proposal is what you will be judged upon. Write a clear proposal on what you plan to do, the scope of your project, and why we should choose you to do it. Proposals are the basis of the GSoC projects and therefore one of the most important things to do well. The proposal is not only the basis of our decision of which student to choose, it has also an effect on Google's decision as to how many student slots are assigned to Qubes.

Below is the application template:

```
# Introduction

Every software project should solve a problem. Before offering the solution (your Google Summer of Code project), you should first define the problem. What’s the current state of things? What’s the issue you wish to solve and why? Then you should conclude with a sentence or two about your solution. Include links to discussions, features, or bugs that describe the problem further if necessary.

# Project goals

Be short and to the point, and perhaps format it as a list. Propose a clear list of deliverables, explaining exactly what you promise to do and what you do not plan to do. “Future developments” can be mentioned, but your promise for the Google Summer of Code term is what counts.

# Implementation

Be detailed. Describe what you plan to do as a solution for the problem you defined above. Include technical details, showing that you understand the technology. Illustrate key technical elements of your proposed solution in reasonable detail.

# Timeline

Show that you understand the problem, have a solution, have also broken it down into manageable parts, and that you have a realistic plan on how to accomplish your goal. Here you set expectations, so don’t make promises you can’t keep. A modest, realistic and detailed timeline is better than promising the impossible.

If you have other commitments during GSoC, such as a job, vacation, exams, internship, seminars, or papers to write, disclose them here. GSoC should be treated like a full-time job, and we will expect approximately 40 hours of work per week. If you have conflicts, explain how you will work around them. If you are found to have conflicts which you did not disclose, you may be failed.

Open and clear communication is of utmost importance. Include your plans for communication in your proposal; daily if possible. You will need to initiate weekly formal communications such as a detailed email to the qubes-devel mailing list. Lack of communication will result in you being failed.

# About me

Provide your contact information and write a few sentences about you and why you think you are the best for this job. Prior contributions to Qubes are helpful; list your commits. Name people (other developers, students, professors) who can act as a reference for you. Mention your field of study if necessary. Now is the time to join the relevant mailing lists. We want you to be a part of our community, not just contribute your code.

Tell us if you are submitting proposals to other organizations, and whether or not you would choose Qubes if given the choice.

Other things to think about:
* Are you comfortable working independently under a supervisor or mentor who is several thousand miles away, and perhaps 12 time zones away? How will you work with your mentor to track your work? Have you worked in this style before?
* If your native language is not English, are you comfortable working closely with a supervisor whose native language is English? What is your native language, as that may help us find a mentor who has the same native language?
* After you have written your proposal, you should get it reviewed. Do not rely on the Qubes mentors to do it for you via the web interface, although we will try to comment on every proposal. It is wise to ask a colleague or a developer to critique your proposal. Clarity and completeness are important.
```

## Project Ideas

These project ideas were contributed by our developers and may be incomplete. If you are interested in submitting a proposal based on these ideas, you should contact the [qubes-devel mailing list][ml-devel] and associated GitHub issue to learn more about the idea.

```
### Adding a Proposal

**Project**: Something that you're totally excited about

**Brief explanation**: What is the project, where does the code live?

**Expected results**: What is the expected result in the timeframe given

**Knowledge prerequisite**: Pre-requisites for working on the project. What coding language and knowledge is needed?
If applicable, links to more information or discussions

**Mentor**: Name and email address.
```

### Template manager, new template distribution mechanism

**Project**: Template manager, new template distribution mechanism

**Brief explanation**: Template VMs currently are distributed using RPM
packages. There are multiple problems with that, mostly related to static
nature of RPM package (what files belong to the package). This means such
Template VM cannot be renamed, migrated to another storage (like LVM), etc.
Also we don't want RPM to automatically update template package itself (which
would override all the user changes there). More details:
[#2064](https://github.com/QubesOS/qubes-issues/issues/2064),
[#2534](https://github.com/QubesOS/qubes-issues/issues/2534),
[#3573](https://github.com/QubesOS/qubes-issues/issues/3573).

**Expected results**:

 - Design new mechanism for distributing templates (possibly including some
   package format - either reuse something already existing, or design
   new one). The mechanism needs to handle:
   - integrity protection (digital signatures), not parsing any data in dom0
     prior to signature verification
   - efficient handling of large sparse files
   - ability to deploy the template into various storage mechanisms (sparse
     files, LVM thin volumes etc).
   - template metadata, templates repository - enable the user to browse
     available templates (probably should be done in dedicated VM, or DisposableVM)
   - manual template removal by users (without it, see problems such 
     as [#5509](https://github.com/QubesOS/qubes-issues/issues/5509)
 - Implement the above mechanism:
   - tool to download named template - should perform download operation in
     some VM (as dom0 have no network access), then transfer the data to dom0,
     verify its integrity and then create Template VM and feed it's root
     filesystem image with downloaded data.
   - tool to browse templates repository - both CLI and GUI (preferably integrated 
     with existing Template Manager tool)
   - integrate both tools - user should be able to choose some template to be
     installed from repository browsing tool - see
     [#1705](https://github.com/QubesOS/qubes-issues/issues/1705) for some idea
     (this one lacks integrity verification, but a similar service could
     be developed with that added)
 - If new "package" format is developed, add support for it into
   [linux-template-builder](https://github.com/QubesOS/qubes-linux-template-builder).
 - Document the mechanism.
 - Write unit tests and integration tests.

**Knowledge prerequisite**:

 - Large files (disk images) handling (sparse files, archive formats)
 - Bash and Python scripting
 - Data integrity handling - digital signatures (gpg2, gpgv2)
 - PyGTK
 - RPM package format, (yum) repository basics

**Mentor**: [Marek Marczykowski-Górecki](/team/)

### USB passthrough to Windows qubes

**Project**: USB passthrough to Windows qubes

**Brief explanation**: Add ability to use individual USB devices in Windows qubes. Right now the only option to do that, is to assign the whole USB controller (PCI device), which applies to all the devices connected to it. USB passthrough on Qubes is based on USBIP project, with transport over qrexec instead of TCP/IP.

**Expected results**:

 - Evaluate possible approaches (including flexibility, compatibility and performance), suggested ideas:
   - use [USBIP for Windows](https://github.com/cezuni/usbip-win) and make it work with qrexec - similar as done for Linux
   - use qrexec+USBIP in Linux-based stubdomain and plug it into USB emulation in qemu
 - Choose one approach, write (very simple) design documentation
 - Write relevant new code (applies mostly for usbip-win case)
 - Plug the mechanism into Qubes core toolstack ([Devices API](https://dev.qubes-os.org/projects/core-admin/en/latest/qubes-devices.html))

**Knowledge prerequisite**:

- basic USB architecture knowledge (buses, devices, interfaces, functions)
- Python and Bash scripting
- C
- Windows USB stack and/or qemu USB stack

**Mentor**: [Marek Marczykowski-Górecki](/team/)

### Dedicated Audio qube

**Project**: Dedicated Audio qube

**Brief explanation**: Moving audio subsystem from dom0 to a dedicated AudioVM and/or a preexisting VM (e.g sys-usb with attached usb audio device). This would allow using USB audio devices system-wide, without leaving a USB controller in dom0. [Relevant github issue](https://github.com/QubesOS/qubes-issues/issues/1590).

**Expected results**:

- Make audio virtualization components work with non-dom0 backend (in short: add configuration option for the backend, instead of assuming "dom0")
- Possibly per-qube setting what should be used as an AudioVM
- Make other audio-related tools (including GUI tools) work with the new setup, especially enabling/disabling microphone (`qvm-device mic`) and volume control

**Knowledge prerequisite**:

- Pulseaudio
- C
- Python

**Mentor**: [Marek Marczykowski-Górecki](/team/)

### Qubes as a Vagrant provider

**Project**: Qubes as a Vagrant provider

**Brief explanation**: Currently using Vagrant on Qubes requires finding an image that uses Docker as isolation provider and running Docker in a qube, or downloading the Vagrantfile and manually setting up a qube according to the Vagrantfile. This project aims at simplifying this workflow. Since introduction of Admin API, it's possible for a qube to provision another qube - which is exactly what is needed for Vagrant. [Related discussion](https://groups.google.com/d/msgid/qubes-devel/535299ca-d16a-4a70-8223-a4ac6be4be41%40googlegroups.com)

**Expected results**:

 - Design how Vagrant Qubes provider should look like, including:
   - [box format](https://www.vagrantup.com/docs/plugins/providers.html#box-format)
   - method for running commands inside (ssh vs qvm-run)
 - Write a Vagrant provider able to create/start/stop/etc a VM
 - Document how to configure and use the provider, including required qrexec policy changes and possibly firewall rules
 - Write integration tests

**Knowledge prerequisite**:

 - Ruby
 - Vagrant concepts

**Mentor**: [Wojtek Porczyk](/team/), [Marek Marczykowski-Górecki](/team/)

### Mechanism for maintaining in-VM configuration

**Project**: Mechanism for maintaining in-VM configuration

**Brief explanation**: Large number of VMs is hard to maintain. Templates helps with keeping them updated, but many applications have configuration in user home directory, which is not synchronized.

**Expected results**:

- Design a mechanism how to _safely_ synchronize application configuration living in user home directory (`~/.config`, some other "dotfiles"). Mechanism should be resistant against malicious VM forcing its configuration on other VMs. Some approach could be a strict control which VM can send what changes (whitelist approach, not blacklist).
- Implementation of the above mechanism.
- Documentation how to configure it securely.


**Knowledge prerequisite**:

- shell and/or python scripting
- Qubes OS qrexec services

**Mentor**: [Frédéric Pierret](/team/)

### Wayland support in GUI agent and/or GUI daemon

**Project**: Wayland support in GUI agent and/or GUI daemon

**Brief explanation**: Currently both GUI agent (VM side of the GUI virtualization) and GUI daemon (dom0 side of GUI virtualization) support X11 protocol only. It may be useful to add support for Wayland there. Note that those are in fact two independent projects:

1. GUI agent - make it work as Wayland compositor, instead of extracting window's composition buffers using custom X11 driver
2. GUI daemon - act as Wayland application, showing windows retrieved from VMs, keeping zero-copy display path (window content is directly mapped from application running in VM, not copied)

**Expected results**:

Choose either of GUI agent, GUI daemon. Both are of similar complexity and each separately looks like a good task for GSoC time period.

- design relevant GUI agent/daemon changes, the GUI protocol should not be affected
- consider window decoration handling - VM should have no way of spoofing those, so it must be enforced by GUI daemon (either client-side - by GUI daemon itself, or server-side, based on hints given by GUI daemon)
- implement relevant GUI agent/daemon changes
- implement tests for new GUI handling, similar to existing tests for X11 based GUI

Relevant links:
 - [Low level GUI documentation](/doc/gui/)
 - [qubes-gui-agent-linux](https://github.com/qubesos/qubes-gui-agent-linux)
 - [qubes-gui-daemon](https://github.com/qubesos/qubes-gui-daemon)
 - [Use Wayland instead of X11 to increase performance](https://github.com/qubesos/qubes-issues/issues/3366)

**Knowledge prerequisite**:

- Wayland architecture
- basics of X11 (for understanding existing code)
- C language
- using shared memory (synchronization methods etc)

**Mentor**: [Marek Marczykowski-Górecki](/team/).

### Qubes Live USB

**Project**: Revive Qubes Live USB, integrate it with installer

**Brief explanation**: Qubes Live USB is based on Fedora tools to build live
distributions. But for Qubes we need some adjustments: starting Xen instead of
Linux kernel, smarter copy-on-write handling (we run there multiple VMs, so a
lot more data to save) and few more. Additionally in Qubes 3.2 we have
so many default VMs that default installation does not fit in 16GB image
(default value) - some subset of those VMs should be chosen. Ideally we'd like
to have just one image being both live system and installation image. More
details: [#1552](https://github.com/QubesOS/qubes-issues/issues/1552),
[#1965](https://github.com/QubesOS/qubes-issues/issues/1965).

**Expected results**:

 - Adjust set of VMs and templates included in live edition.
 - Update and fix build scripts for recent Qubes OS version.
 - Update startup script to mount appropriate directories as either
   copy-on-write (device-mapper snapshot), or tmpfs.
 - Optimize memory usage: should be possible to run sys-net, sys-firewall, and
   at least two more VMs on 4GB machine. This include minimizing writes to
   copy-on-write layer and tmpfs (disable logging etc).
 - Research option to install the system from live image. If feasible add
   this option.

**Knowledge prerequisite**:

 - System startup sequence: bootloaders (isolinux, syslinux, grub, UEFI), initramfs, systemd.
 - Python and Bash scripting
 - Filesystems and block devices: loop devices, device-mapper, tmpfs, overlayfs, sparse files.

**Mentor**: [Frédéric Pierret](/team/)

<!--
### Unikernel-based firewallvm with Qubes firewall settings support

REMOVED as of January 2020: work is being done on this

**Project**: Unikernel based firewallvm with Qubes firewall settings support

**Brief explanation**: [blog post](http://roscidus.com/blog/blog/2016/01/01/a-unikernel-firewall-for-qubesos/), [repo](https://github.com/talex5/qubes-mirage-firewall)

**Expected results**: A firewall implemented as a unikernel which supports all the networking-related functionality as the default sys-firewall VM, including configuration via Qubes Manager. Other duties currently assigned to sys-firewall such as the update proxy may need to be appropriately migrated first.

**Knowledge prerequisite**:

- [OCaml](https://ocaml.org/) + [MirageOS](https://mirage.io/) or other unikernel framework,
- Xen network stack,
- Qubes networking model & firewall semantics.

**Mentor**: [Thomas Leonard](mailto:talex5@gmail.com), [Marek Marczykowski-Górecki](/team/)
-->


### LogVM(s)

**Project**: LogVM(s)

**Brief explanation**: Qubes AppVMs do not have persistent /var (on purpose).
It would be useful to send logs generated by various VMs to a dedicated
log-collecting VM. This way logs will not only survive VM shutdown, but also be
immune to altering past entries. See
[#830](https://github.com/QubesOS/qubes-issues/issues/830) for details.

**Expected results**:

 - Design a _simple_ protocol for transferring logs. The less metadata (parsed
   in log-collecting VM) the better.
 - Implement log collecting service. Besides logs itself, should save
   information about logs origin (VM name) and timestamp. The service should
   _not_ trust sending VM in any of those.
 - Implement log forwarder compatible with systemd-journald and rsyslog. A
   mechanism (service/plugin) fetching logs in real time from those and sending
   to log-collecting VM over qrexec service.
 - Document the protocol.
 - Write unit tests and integration tests.

**Knowledge prerequisite**:

 - syslog
 - systemd
 - Python/Bash scripting

**Mentor**: [Frédéric Pierret](/team/)

<!--

Removed as of January 2020: work done by MIM UW students

### Xen GPU passthrough for Intel integrated GPUs
**Project**: Xen GPU passthrough for Intel integrated GPUs (largely independent of Qubes)

**Brief explanation**: This project is prerequisite to full GUI domain support,
where all desktop environment is running in dedicated VM, isolated from
dom0. There is already some support for GPU passthrough in Xen, but needs to be
integrated in to Qubes and probably really make working, even when using qemu
in stubdomain. GUI domain should be a HVM domain (not PV).
This should be done without compromising Qubes security features, especially:
using VT-d for protection against DMA attacks, using stubdomain for sandboxing
qemu process (if needed) - qemu running in dom0 is not acceptable.  More
details in [#2618](https://github.com/QubesOS/qubes-issues/issues/2618).

**Expected results**:

 - Ability to start a VM with GPU connected. VM should be able to handle video
   output (both laptop internal display, and external monitors if apply). That
   VM also should be able to use hardware acceleration.
 - This project may require patching any/all of Xen hypervisor, Libvirt, Qemu,
   Linux. In such a case, patches should be submitted to appropriate upstream
   project.
 - It's ok to focus on a specific, relatively new Intel-based system with Intel
   integrated GPU.

**Knowledge prerequisite**:

 - C language
 - Kernel/hypervisor debugging
 - Basics of x86_64 architecture, PCIe devices handling (DMA, MMIO, interrupts), IOMMU (aka VT-d)
 - Xen hypervisor architecture

**Mentor**: [Marek Marczykowski-Górecki](/team/)
-->

### Whonix IPv6 and nftables support
**Project**: Whonix IPv6 and nftables support

**Brief explanation**: [T509](https://phabricator.whonix.org/T509)

**Expected results**:

- Work at upstream Tor: An older version of https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy page was the origin of Whonix. Update that page for nftables / IPv6 support without mentioning Whonix. Then discuss that on the tor-talk mailing list for wider input. - https://trac.torproject.org/projects/tor/ticket/21397
- implement corridor feature request add IPv6 support / port to nftables - https://github.com/rustybird/corridor/issues/39
- port [whonix-firewall](https://github.com/Whonix/whonix-firewall) to nftables
- make connections to IPv6 Tor relays work
- make connections to IPv6 destinations work

**Knowledge prerequisite**:

- nftables
- iptables
- IPv6

**Mentor**: [Patrick Schleizer](/team/)

### Audio support for Qubes Windows Tools
**Project**: Audio support for Qubes Windows Tools

**Brief explanation**: Add audio support for Windows HVMs via Qubes Windows Tools. [#2624](https://github.com/QubesOS/qubes-issues/issues/2624)

**Expected results**: Windows HVMs should have an audio device that supports playback and recording.

**Knowledge prerequisite**: C/C++ languages, familiarity with Windows API, possibly familiarity with Windows audio stack on the driver level.

**Mentor**: [Rafał Wojdyła](/team/)

### Improve Windows GUI agent performance and stability
**Project**: Improve Windows GUI agent performance and stability

**Brief explanation**: Previous profiling has shown that the Windows GUI agent uses significant portion of VM's CPU time for mouse input simulation. This can be improved, as well as agent's stability in some cases (desktop/user switching, logon/logoff, domain-joined VMs, multiple monitors). Seamless GUI experience can be significantly improved, but that may require changes in the Qubes video driver. [#1044](https://github.com/QubesOS/qubes-issues/issues/1044) [#1045](https://github.com/QubesOS/qubes-issues/issues/1045) [#1500](https://github.com/QubesOS/qubes-issues/issues/1500) [#2138](https://github.com/QubesOS/qubes-issues/issues/2138) [#2487](https://github.com/QubesOS/qubes-issues/issues/2487) [#2589](https://github.com/QubesOS/qubes-issues/issues/2589)

**Expected results**: Reduction of agent's CPU usage, improved stability.

**Knowledge prerequisite**: C language, Familiarity with Windows API, especially the windowing stack. Familiarity with profiling and debugging tools for Windows.

**Mentor**: [Rafał Wojdyła](/team/)

### GUI agent for Windows 8/10
**Project**: GUI agent for Windows 8/10

**Brief explanation**: Add support for Windows 8+ to the Qubes GUI agent and video driver. Starting from Windows 8, Microsoft requires all video drivers to conform to the WDDM display driver model which is incompatible with the current Qubes video driver. Unfortunately the WDDM model is much more complex than the old XPDM one and officially *requires* a physical GPU device (which may be emulated). Some progress has been made to create a full WDDM driver that *doesn't* require a GPU device, but the driver isn't working correctly yet. Alternatively, WDDM model supports display-only drivers which are much simpler but don't have access to system video memory and rendering surfaces (a key feature that would simplify seamless GUI mode). [#1861](https://github.com/QubesOS/qubes-issues/issues/1861)

**Expected results**: Working display-only WDDM video driver or significant progress towards making the full WDDM driver work correctly.

**Knowledge prerequisite**: C/C++ languages, familiarity with Windows API, familiarity with the core Windows WDM driver model. Ideally familiarity with the WDDM display driver model.

**Mentor**: [Rafał Wojdyła](/team/)

### Unattended Windows installation

**Project**: Unattended Windows installation

**Brief explanation**: Simplify Windows usage by providing a tool that perform unattended installation given required input data (installation image, license key, user name, etc). Similar feature is already supported in other virtualization solutions, including VMWare Workstation and VirtualBox. [Related github issue](https://github.com/QubesOS/qubes-issues/issues/4688).

**Expected results**:

 - A template for `autounattended.xml` file for Windows installer - the template should have placeholders for settings that need to be provided by the user.
 - A tool for generating actual `autounattended.xml` file based on the template and user settings.
 - A tool for launching Windows installation, given installation image and `autounattended.xml` file (can be the same as in the above point).
 - (Optional) Unattended installation should also include Qubes Windows Tools.
 - (Optional) A tool should be able to use Windows license embedded in ACPI tables - [related discussion](https://groups.google.com/d/msgid/qubes-devel/0b7fabae-f843-e7ce-40cf-193326cecdb0%40zrubi.hu)
 - User documentation
 - Automated tests (unit tests, integration tests)

**Knowledge prerequisite**:

 - Python scripting
 - Linux administration, including handling loop devices, partition tables, filesystems etc
 - For optional features, C language and x86 architecture (ACPI tables)

**Mentor**: [Rafał Wojdyła](/team/), [Marek Marczykowski-Górecki](/team/)

### GNOME support in dom0 / GUI VM

**Project**: GNOME support in dom0

**Brief explanation**: Integrating GNOME into Qubes dom0. This include:

 - patching window manager to add colorful borders
 - removing stuff not needed in dom0 (file manager(s), indexing services etc)
 - adjusting menu for easy navigation (same applications in different VMs and such problems, dom0-related entries in one place)
 - More info: [#1806](https://github.com/QubesOS/qubes-issues/issues/1806)

**Expected results**:

 - Review existing support for other desktop environments (KDE, Xfce4, i3, awesome).
 - Patch window manager to draw colorful borders (we use only server-side
   decorations), there is already very similar patch in
   [Cappsule project](https://github.com/cappsule/cappsule-gui).
 - Configure GNOME to not make use of dom0 user home in visible way (no search
   in files there, no file manager, etc).
 - Configure GNOME to not look into external devices plugged in (no auto
   mounting, device notifications etc).
 - Package above modifications as rpms, preferably as extra configuration files
   and/or plugins than overwriting existing files. Exceptions to this rule may
   apply if no other option.
 - Adjust comps.xml (in installer-qubes-os repo) to define package group with
   all required packages.
 - Document installation procedure.

**Knowledge prerequisite**:

 - GNOME architecture
 - C language (patching metacity)
 - Probably also javascript - for modifying GNOME shell extensions

**Mentor**: [Frédéric Pierret](/team/), [Marek Marczykowski-Górecki](/team/)

### Generalize the Qubes PDF Converter to other types of files

**Project**: Qubes Converters

**Brief explanation**: One of the pioneering ideas of Qubes is to use disposable virtual machines to convert untrustworthy files (such as documents given to journalists by unknown and potentially malicious whistleblowers) into trustworthy files.  See [Joanna's blog on the Qubes PDF Convert](http://theinvisiblethings.blogspot.co.uk/2013/02/converting-untrusted-pdfs-into-trusted.html) for details of the idea.  Joanna has implemented a prototype for PDF documents.  The goal of this project would be to generalize beyond the simple prototype to accommodate a wide variety of file formats, including Word documents, audio files, video files, spreadsheets, and so on.  The converters should prioritise safety over faithful conversion.  For example the Qubes PDF converter typically leads to lower quality PDFs (e.g. cut and paste is no longer possible), because this makes the conversion process safer.

**Expected results**: We expect that in the timeframe, it will be possible to implement many converters for many file formats.  However, if any unexpected difficulties arise, we would prioritise a small number of safe and high quality converters over a large number of unsafe or unuseful converters.

**Knowledge prerequisite**: Most of the coding will probably be implemented as shell scripts to interface with pre-existing converters (such as ImageMagick in the Qubes PDF converter).  However, shell scripts are not safe for processing untrusted data, so any extra processing will need to be implemented in another language -- probably Python.

**Mentors**: Andrew Clausen and Jean-Philippe Ouellet

### Progress towards reproducible builds
**Project**: Progress towards reproducible builds

**Brief explanation**: A long-term goal is to be able to build the entire OS and installation media in a completely bit-wise deterministic manner, but there are many baby steps to be taken along that path. See:

- "[Security challenges for the Qubes build process](/news/2016/05/30/build-security/)"
- [This mailing list post](https://groups.google.com/d/msg/qubes-devel/gq-wb9wTQV8/mdliS4P2BQAJ)
- and [reproducible-builds.org](https://reproducible-builds.org/)

for more information and qubes-specific background.

**Expected results**: Significant progress towards making the Qubes build process deterministic. This would likely involve cooperation with and hacking on several upstream build tools to eliminate sources of variability.

**Knowledge prerequisite**: qubes-builder [[1]](/doc/qubes-builder/) [[2]](/doc/qubes-builder-details/) [[3]](https://github.com/QubesOS/qubes-builder/tree/master/doc), and efficient at introspecting complex systems: comfortable with tracing and debugging tools, ability to quickly identify and locate issues within a large codebase (upstream build tools), etc.

**Mentor**: [Marek Marczykowski-Górecki](/team/)

### Porting Qubes to ARM/aarch64

**Project**: Porting Qubes to ARM/aarch64

**Brief explanation**:

Qubes currently only supports the x86_64 CPU architecture. Xen currently has additional support for ARM32/ARM64 processors, however work needs to be done to integrate this into the Qubes build process, as well as work in integrating this with the Qubes toolstack and security model. This may also be beneficial in simplifying the process of porting to other architectures.

Some related discussion:

 - [#4318](https://github.com/QubesOS/qubes-issues/issues/4318) on porting to ppc64.
 - [#3894](https://github.com/QubesOS/qubes-issues/issues/3894) on porting to L4 microkernel.

**Expected results**:

 - Add cross-compilation support to qubes-builder and related components.
 - Make aarch64 specific adjustments to Qubes toolstacks/manager (including passthrough of devices from device tree to guest domains).
 - Aarch64 specific integration and unit tests.
 - Production of generic u-boot or uefi capable image/iso for target hardware.

**Knowledge prerequisite**:

 - Libvirt and Qubes toolstacks (C and python languages).
 - Xen debugging.
 - General ARM architecture knowledge.
 
**Mentor**: [Marek Marczykowski-Górecki](/team/)

### Porting Qubes to POWER9/PPC64

**Project**: Porting Qubes to POWER9/ppc64

**Brief explanation**:

Qubes currently supports the x86_64 CPU architecture. PowerPC is desirable for security purposes as it is the only architecture where one can get performant hardware with entirely open source firmware. Xen has **deprecated** support for Power9/PPC64 processors. Here are two directions to tackle this project from:

- Port Qubes to KVM then work on ppc64 specifics
  - Implement some missing functionality in KVM then implement KVM support in the Qubes Hypervisor Abstraction Layer and build process. Improving the HAL will also be beneficial for simplifying the process of porting to further architectures and hypervisors.

- Port Xen to ppc64 then work on Qubes specifics
  - For more information on porting Xen see [this thread](https://markmail.org/message/vuk7atnyqfq52epp).

More information and further links can be found in the related issue:
[#4318](https://github.com/QubesOS/qubes-issues/issues/4318).

**Expected results**:

 - Add cross-compilation support to qubes-builder and related components.
 - Make ppc64 specific adjustments to Qubes toolstacks/manager (including passthrough of devices from device tree to guest domains).
 - ppc64 specific integration and unit tests.
 - Production of generic u-boot or uefi capable image/iso for target hardware.

**Knowledge prerequisite**:

 - Libvirt and Qubes toolstacks (C and python languages).
 - KVM or XEN internals
 - General ppc64 architecture knowledge.
 
**Mentor**: [Marek Marczykowski-Górecki](/team/)

### Android development in Qubes

**Project**: Research running Android in Qubes VM (probably HVM) and connecting it to Android Studio

**Brief explanation**: The goal is to enable Android development (and testing!)
on Qubes OS. Currently it's only possible using qemu-emulated Android for ARM.
Since it's software emulation it's rather slow.
Details, reference: [#2233](https://github.com/QubesOS/qubes-issues/issues/2233)

**Expected results**:
  - a simple way of setting up Android qubes with hardware emulation
  (distributed as a template or as a salt, handling various modern Android versions)
  - figuring out and implementing an easy and secure way to connect an Android 
  qube to a development qube with Android studio
  - documentation and tests

**Knowledge prerequisite**:

**Mentor**: Inquire on [qubes-devel][ml-devel].

----

We adapted some of the language here about GSoC from the [KDE GSoC page](https://community.kde.org/GSoC).

[2017-archive]: https://summerofcode.withgoogle.com/archive/2017/organizations/5074771758809088/
[gsoc-qubes]: https://summerofcode.withgoogle.com/organizations/6239659689508864/
[gsoc]: https://summerofcode.withgoogle.com/
[team]: /team/
[gsoc-faq]: https://developers.google.com/open-source/gsoc/faq
[contributing]: /doc/contributing/#contributing-code
[patches]: /doc/source-code/#how-to-send-patches
[code-signing]: /doc/code-signing/
[ml-devel]: /support/#qubes-devel
[gsoc-participate]: https://developers.google.com/open-source/gsoc/
[gsoc-student]: https://developers.google.com/open-source/gsoc/resources/manual#student_manual
[how-to-gsoc]: http://teom.org/blog/kde/how-to-write-a-kick-ass-proposal-for-google-summer-of-code/
[gsoc-submit]: https://summerofcode.withgoogle.com/
[mailing-lists]: /support/
[qubes-issues]: https://github.com/QubesOS/qubes-issues/issues
[qubes-issues-suggested]: https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22P%3A%20minor%22%20label%3A%22help%20wanted%22
[qubes-builder]: /doc/qubes-builder/
