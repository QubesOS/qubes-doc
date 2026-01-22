============================
Google Summer of Code (GSoC)
============================


Information for Students
------------------------


Thank you for your interest in participating in the `Google Summer of Code program <https://summerofcode.withgoogle.com/>`__ with the `Qubes OS team <https://www.qubes-os.org/team/>`__. You can read more about the Google Summer of Code program at the `official website <https://summerofcode.withgoogle.com/>`__ and the `official FAQ <https://developers.google.com/open-source/gsoc/faq>`__.

Being accepted as a Google Summer of Code contributor is quite competitive. If you are interested in participating in the Summer of Code please be aware that you must be able to produce code for Qubes OS for 3-5 months. Your mentors, Qubes developers, will dedicate a portion of their time towards mentoring you. Therefore, we seek candidates who are committed to helping Qubes long-term and are willing to do quality work and be proactive in communicating with your mentor.

You don’t have to be a proven developer – in fact, this whole program is meant to facilitate joining Qubes and other free and open source communities. The Qubes community maintains information about :ref:`contributing to Qubes development <introduction/contributing:contributing code>` and :ref:`how to send patches <developer/code/source-code:how to send patches>`. In order to contribute code to the Qubes project, you must be able to :doc:`sign your code </developer/code/code-signing>`.

You should start learning the components that you plan on working on before the start date. Qubes developers are available on the :ref:`mailing lists <introduction/support:qubes-devel>` for help. The GSoC timeline reserves a lot of time for bonding with the project – use that time wisely. Good communication is key, you should plan to communicate with your team daily and formally report progress and plans weekly. Students who neglect active communication will be failed.

Overview of Steps
^^^^^^^^^^^^^^^^^


- Join the :ref:`qubes-devel list <introduction/support:qubes-devel>` and introduce yourself, and meet your fellow developers

- Read `Google’s instructions for participating <https://developers.google.com/open-source/gsoc/>`__ and the `GSoC Student Manual <https://google.github.io/gsocguides/student/>`__

- Take a look at the list of ideas below

- Come up with a project that you are interested in (and feel free to propose your own! Don’t feel limited by the list below.)

- Read the Contributor Proposal guidelines below

- Write a first draft proposal and send it to the qubes-devel mailing list for review

- Submit proposal using `Google’s web interface <https://summerofcode.withgoogle.com/>`__ ahead of the deadline (this requires a Google Account!)

- Submit proof of enrollment well ahead of the deadline



Coming up with an interesting idea that you can realistically achieve in the time available to you (one summer) is probably the most difficult part. We strongly recommend getting involved in advance of the beginning of GSoC, and we will look favorably on applications from prospective contributors who have already started to act like free and open source developers.

Before the summer starts, there are some preparatory tasks which are highly encouraged. First, if you aren’t already, definitely start using Qubes as your primary OS as soon as possible! Also, it is encouraged that you become familiar and comfortable with the Qubes development workflow sooner than later. A good way to do this (and also a great way to stand out as an awesome applicant and make us want to accept you!) might be to pick up some issues from `qubes-issues <https://github.com/QubesOS/qubes-issues/issues>`__ (our issue-tracking repo) and submit some patches addressing them. Some suitable issues might be those with tags `“help wanted” and “P: minor” <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22P%3A%20minor%22%20label%3A%22help%20wanted%22>`__ (although more significant things are also welcome, of course). Doing this will get you some practice with :doc:`qubes-builder </developer/building/qubes-builder-v2>`, our code-signing policies, and some familiarity with our code base in general so you are ready to hit the ground running come summer.

Contributor proposal guidelines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


A project proposal is what you will be judged upon. Write a clear proposal on what you plan to do, the scope of your project, and why we should choose you to do it. Proposals are the basis of the GSoC projects and therefore one of the most important things to do well.

Below is the application template:

.. code:: markdown

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



Project Ideas
-------------


These project ideas were contributed by our developers and may be incomplete. If you are interested in submitting a proposal based on these ideas, you should contact the :ref:`qubes-devel mailing list <introduction/support:qubes-devel>` and associated GitHub issue to learn more about the idea.

.. code:: markdown

      ### Adding a Proposal

      **Project**: Something that you're totally excited about

      **Brief explanation**: What is the project, where does the code live?

      **Expected results**: What is the expected result in the timeframe given

      **Difficulty**: easy / medium / hard

      **Knowledge prerequisite**: Pre-requisites for working on the project. What coding language and knowledge is needed?
      If applicable, links to more information or discussions

      **Size of the project**: either 175 hours (medium) or 350 hours (large)

      **Mentor**: Name and email address.



Qubes as a Vagrant provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Qubes as a Vagrant provider

**Brief explanation**: Currently using Vagrant on Qubes requires finding an image that uses Docker as isolation provider and running Docker in a qube, or downloading the Vagrantfile and manually setting up a qube according to the Vagrantfile. This project aims at simplifying this workflow. Since introduction of Admin API, it’s possible for a qube to provision another qube - which is exactly what is needed for Vagrant. `Related discussion <https://groups.google.com/d/msgid/qubes-devel/535299ca-d16a-4a70-8223-a4ac6be4be41%40googlegroups.com>`__

**Expected results**:

- Design how Vagrant Qubes provider should look like, including:

  - `box format <https://www.vagrantup.com/docs/plugins/providers.html#box-format>`__

  - method for running commands inside (ssh vs qvm-run)



- Write a Vagrant provider able to create/start/stop/etc a VM

- Document how to configure and use the provider, including required qrexec policy changes and possibly firewall rules

- Write integration tests



**Difficulty**: medium

**Knowledge prerequisite**:

- Ruby

- Vagrant concepts



**Size of the project**: 350 hours

**Mentor**: `Wojtek Porczyk <https://www.qubes-os.org/team/>`__, `Marek Marczykowski-Górecki <https://www.qubes-os.org/team/>`__

System health monitor
^^^^^^^^^^^^^^^^^^^^^


**Project**: System health monitor

**Brief explanation**: A tool that informs the user about common system and configuration issues. Some of this is already available, but scattered across different places. See related issues: `6663 <https://github.com/QubesOS/qubes-issues/issues/6663>`__, `2134 <https://github.com/QubesOS/qubes-issues/issues/2134>`__ (see issues linked to it).

**Expected results**:

- a tool / service that checks for common issues and things needing user attention, for example:

  - some updates to be applied (separate widget already exists)

  - running out of disk space (separate widget already exists)

  - running out of memory

  - insecure USB configuration (USB in dom0)

  - some system VM crashed

  - …



- a GUI that provides terse overview of the system state, and notifies the user if something bad happens



**Difficulty**: medium

**Knowledge prerequisite**:

- Python

- basic knowledge about systemd services

- PyGTK (optional)



**Size of the project**: 350 hours

**Mentor**: `Marta Marczykowska-Górecka <https://www.qubes-os.org/team/>`__, `Benjamin Grande <https://www.qubes-os.org/team/>`__

Mechanism for maintaining in-VM configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Mechanism for maintaining in-VM configuration

**Brief explanation**: Large number of VMs is hard to maintain. Templates helps with keeping them updated, but many applications have configuration in user home directory, which is not synchronized.

**Expected results**:

- Design a mechanism how to *safely* synchronize application configuration living in user home directory (``~/.config``, some other “dotfiles”). Mechanism should be resistant against malicious VM forcing its configuration on other VMs. Some approach could be a strict control which VM can send what changes (whitelist approach, not blacklist).

- Implementation of the above mechanism.

- Documentation how to configure it securely.



**Difficulty**: medium

**Knowledge prerequisite**:

- shell and/or python scripting

- Qubes OS qrexec services



**Size of the project**: 175 hours

**Mentor**: `Frédéric Pierret <https://www.qubes-os.org/team/>`__

Qubes Live USB
^^^^^^^^^^^^^^


**Project**: Revive Qubes Live USB, integrate it with installer

**Brief explanation**: Qubes Live USB is based on Fedora tools to build live distributions. But for Qubes we need some adjustments: starting Xen instead of Linux kernel, smarter copy-on-write handling (we run there multiple VMs, so a lot more data to save) and few more. Additionally in Qubes 3.2 we have so many default VMs that default installation does not fit in 16GB image (default value) - some subset of those VMs should be chosen. Ideally we’d like to have just one image being both live system and installation image. More details: `#1552 <https://github.com/QubesOS/qubes-issues/issues/1552>`__, `#1965 <https://github.com/QubesOS/qubes-issues/issues/1965>`__.

**Expected results**:

- Adjust set of VMs and templates included in live edition.

- Update and fix build scripts for recent Qubes OS version.

- Update startup script to mount appropriate directories as either copy-on-write (device-mapper snapshot), or tmpfs.

- Optimize memory usage: should be possible to run sys-net, sys-firewall, and at least two more VMs on 4GB machine. This include minimizing writes to copy-on-write layer and tmpfs (disable logging etc).

- Research option to install the system from live image. If feasible add this option.



**Difficulty**: hard

**Knowledge prerequisite**:

- System startup sequence: bootloaders (isolinux, syslinux, grub, UEFI), initramfs, systemd.

- Python and Bash scripting

- Filesystems and block devices: loop devices, device-mapper, tmpfs, overlayfs, sparse files.



**Size of the project**: 350 hours

**Mentor**: `Frédéric Pierret <https://www.qubes-os.org/team/>`__

LogVM(s)
^^^^^^^^


**Project**: LogVM(s)

**Brief explanation**: Qubes AppVMs do not have persistent /var (on purpose). It would be useful to send logs generated by various VMs to a dedicated log-collecting VM. This way logs will not only survive VM shutdown, but also be immune to altering past entries. See `#830 <https://github.com/QubesOS/qubes-issues/issues/830>`__ for details.

**Expected results**:

- Design a *simple* protocol for transferring logs. The less metadata (parsed in log-collecting VM) the better.

- Implement log collecting service. Besides logs itself, should save information about logs origin (VM name) and timestamp. The service should *not* trust sending VM in any of those.

- Implement log forwarder compatible with systemd-journald and rsyslog. A mechanism (service/plugin) fetching logs in real time from those and sending to log-collecting VM over qrexec service.

- Document the protocol.

- Write unit tests and integration tests.



**Difficulty**: easy

**Knowledge prerequisite**:

- syslog

- systemd

- Python/Bash scripting



**Size of the project**: 175 hours

**Mentor**: `Frédéric Pierret <https://www.qubes-os.org/team/>`__

Whonix IPv6 and nftables support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Whonix IPv6 and nftables support

**Brief explanation**: `T509 <https://phabricator.whonix.org/T509>`__

**Expected results**:

- Work at upstream Tor: An older version of `TransparentProxy <https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy>`__ page was the origin of Whonix. Update that page for nftables / IPv6 support without mentioning Whonix. Then discuss that on the tor-talk mailing list for wider input. `here <https://trac.torproject.org/projects/tor/ticket/21397>`__

- implement corridor feature request add IPv6 support / port to nftables - `issue <https://github.com/rustybird/corridor/issues/39>`__

- port `whonix-firewall <https://github.com/Whonix/whonix-firewall>`__ to nftables

- make connections to IPv6 Tor relays work

- make connections to IPv6 destinations work



**Difficulty**: medium

**Knowledge prerequisite**:

- nftables

- iptables

- IPv6



**Size of the project**: 175 hours

**Mentor**: `Patrick Schleizer <https://www.qubes-os.org/team/>`__

GUI agent for Windows 8/10
^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: GUI agent for Windows 8/10

**Brief explanation**: Add support for Windows 8+ to the Qubes GUI agent and video driver. Starting from Windows 8, Microsoft requires all video drivers to conform to the WDDM display driver model which is incompatible with the current Qubes video driver. Unfortunately the WDDM model is much more complex than the old XPDM one and officially *requires* a physical GPU device (which may be emulated). Some progress has been made to create a full WDDM driver that *doesn’t* require a GPU device, but the driver isn’t working correctly yet. Alternatively, WDDM model supports display-only drivers which are much simpler but don’t have access to system video memory and rendering surfaces (a key feature that would simplify seamless GUI mode). `#1861 <https://github.com/QubesOS/qubes-issues/issues/1861>`__

**Expected results**: Working display-only WDDM video driver or significant progress towards making the full WDDM driver work correctly.

**Difficulty**: hard

**Knowledge prerequisite**: C/C++ languages, familiarity with Windows API, familiarity with the core Windows WDM driver model. Ideally familiarity with the WDDM display driver model.

**Size of the project**: 175 hours

**Mentor**: `Rafał Wojdyła <https://www.qubes-os.org/team/>`__

GNOME support in dom0 / GUI VM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: GNOME support in dom0

**Brief explanation**: Integrating GNOME into Qubes dom0. This include:

- patching window manager to add colorful borders

- removing stuff not needed in dom0 (file manager(s), indexing services etc)

- adjusting menu for easy navigation (same applications in different VMs and such problems, dom0-related entries in one place)

- More info: `#1806 <https://github.com/QubesOS/qubes-issues/issues/1806>`__



**Expected results**:

- Review existing support for other desktop environments (KDE, Xfce4, i3, awesome).

- Patch window manager to draw colorful borders (we use only server-side decorations), there is already very similar patch in `Cappsule project <https://github.com/cappsule/cappsule-gui>`__.

- Configure GNOME to not make use of dom0 user home in visible way (no search in files there, no file manager, etc).

- Configure GNOME to not look into external devices plugged in (no auto mounting, device notifications etc).

- Package above modifications as RPMs, preferably as extra configuration files and/or plugins than overwriting existing files. Exceptions to this rule may apply if no other option.

- Adjust comps.xml (in installer-qubes-os repo) to define package group with all required packages.

- Document installation procedure.



**Difficulty**: hard

**Knowledge prerequisite**:

- GNOME architecture

- C language (patching metacity)

- Probably also javascript - for modifying GNOME shell extensions



**Size of the project**: 175 hours

**Mentor**: `Frédéric Pierret <https://www.qubes-os.org/team/>`__, `Marek Marczykowski-Górecki <https://www.qubes-os.org/team/>`__

Generalize the Qubes PDF Converter to other types of files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Qubes Converters

**Brief explanation**: One of the pioneering ideas of Qubes is to use disposable virtual machines to convert untrustworthy files (such as documents given to journalists by unknown and potentially malicious whistleblowers) into trustworthy files. See `Joanna’s blog on the Qubes PDF Convert <https://theinvisiblethings.blogspot.co.uk/2013/02/converting-untrusted-pdfs-into-trusted.html>`__ for details of the idea. Joanna has implemented a prototype for PDF documents. The goal of this project would be to generalize beyond the simple prototype to accommodate a wide variety of file formats, including Word documents, audio files, video files, spreadsheets, and so on. The converters should prioritise safety over faithful conversion. For example the Qubes PDF converter typically leads to lower quality PDFs (e.g. cut and paste is no longer possible), because this makes the conversion process safer.

**Expected results**: We expect that in the timeframe, it will be possible to implement many converters for many file formats. However, if any unexpected difficulties arise, we would prioritise a small number of safe and high quality converters over a large number of unsafe or unuseful converters.

**Difficulty**: easy

**Knowledge prerequisite**: Most of the coding will probably be implemented as shell scripts to interface with pre-existing converters (such as ImageMagick in the Qubes PDF converter). However, shell scripts are not safe for processing untrusted data, so any extra processing will need to be implemented in another language – probably Python.

**Size of the project**: 175 hours

**Mentors**: Andrew Clausen and Jean-Philippe Ouellet

Progress towards reproducible builds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Progress towards reproducible builds

**Brief explanation**: A long-term goal is to be able to build the entire OS and installation media in a completely bit-wise deterministic manner, but there are many baby steps to be taken along that path. See:

- “`Security challenges for the Qubes build process <https://www.qubes-os.org/news/2016/05/30/build-security/>`__”

- `This mailing list post <https://groups.google.com/d/msg/qubes-devel/gq-wb9wTQV8/mdliS4P2BQAJ>`__

- and `reproducible-builds.org <https://reproducible-builds.org/>`__



for more information and qubes-specific background.

**Expected results**: Significant progress towards making the Qubes build process deterministic. This would likely involve cooperation with and hacking on several upstream build tools to eliminate sources of variability.

**Difficulty**: medium

**Knowledge prerequisite**: qubes-builder :doc:`[1] </developer/building/qubes-builder-v2>` `[2] <https://github.com/QubesOS/qubes-builderv2>`__, and efficient at introspecting complex systems: comfortable with tracing and debugging tools, ability to quickly identify and locate issues within a large codebase (upstream build tools), etc.

**Size of the project**: 350 hours

**Mentor**: `Marek Marczykowski-Górecki <https://www.qubes-os.org/team/>`__

Porting Qubes to ARM/aarch64
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Porting Qubes to ARM/aarch64

**Brief explanation**:

Qubes currently only supports the x86_64 CPU architecture. Xen currently has additional support for ARM32/ARM64 processors, however work needs to be done to integrate this into the Qubes build process, as well as work in integrating this with the Qubes toolstack and security model. This may also be beneficial in simplifying the process of porting to other architectures.

Some related discussion:

- `#4318 <https://github.com/QubesOS/qubes-issues/issues/4318>`__ on porting to ppc64.

- `#3894 <https://github.com/QubesOS/qubes-issues/issues/3894>`__ on porting to L4 microkernel.



**Expected results**:

- Add cross-compilation support to qubes-builder and related components.

- Make aarch64 specific adjustments to Qubes toolstacks/manager (including passthrough of devices from device tree to guest domains).

- Aarch64 specific integration and unit tests.

- Production of generic u-boot or uefi capable image/iso for target hardware.



**Difficulty**: hard

**Knowledge prerequisite**:

- Libvirt and Qubes toolstacks (C and python languages).

- Xen debugging.

- General ARM architecture knowledge.



**Size of the project**: 350 hours

**Mentor**: `Marek Marczykowski-Górecki <https://www.qubes-os.org/team/>`__

Android development in Qubes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Research running Android in Qubes VM (probably HVM) and connecting it to Android Studio

**Brief explanation**: The goal is to enable Android development (and testing!) on Qubes OS. Currently it’s only possible using qemu-emulated Android for ARM. Since it’s software emulation it’s rather slow. Details, reference: `#2233 <https://github.com/QubesOS/qubes-issues/issues/2233>`__

**Expected results**:

- a simple way of setting up Android qubes with hardware emulation (distributed as a template or as a salt, handling various modern Android versions)

- figuring out and implementing an easy and secure way to connect an Android qube to a development qube with Android studio

- documentation and tests



**Difficulty**: hard

**Knowledge prerequisite**:

**Size of the project**: 350 hours

**Mentor**: Inquire on :ref:`qubes-devel <introduction/support:qubes-devel>`.

Admin API Fuzzer
^^^^^^^^^^^^^^^^


**Project**: Develop a `Fuzzer <https://en.wikipedia.org/wiki/Fuzzing>`__ for the :doc:`Qubes OS Admin API </developer/services/admin-api>`.

**Brief explanation**: The :doc:`Qubes OS Admin API </developer/services/admin-api>` enables VMs to execute privileged actions on other VMs or dom0 - if allowed by the Qubes OS RPC policy. Programming errors in the Admin API however may cause these access rights to be more permissive than anticipated by the programmer. If the there is a client error and the API response is too restrictive, it won't reveal any information making it difficult to debug and handle errors, as it is a general error. More details:

- `QSB-038: Qrexec policy bypass and possible information leak <https://www.qubes-os.org/news/2018/02/20/qsb-38/>`__
- `QSB-087: Qrexec: Injection of unsanitized data into log output <https://www.qubes-os.org/news/2022/11/23/qsb-087/>`__ (related to Qrexec rather than the Admin API, but helps understand dangers of unsanitized data in logs/output)
- `QSB-089: Qrexec: Memory corruption in service request handling <https://www.qubes-os.org/news/2023/05/11/qsb-089/>`__ (related to Qrexec rather than the Admin API, but helps understand dangers of unsanitized data length that could be passed to other applications that may cause memory corruption on a faulty application)
- `QSB-099: Qrexec policy leak via policy.RegisterArgument service <https://www.qubes-os.org/news/2024/01/19/qsb-099/>`__
- `#5316: qvm-create error message unhelpful on missing template <https://github.com/QubesOS/qubes-issues/issues/5316>`__
- `#6739: Improve “Got empty response from qubesd” message <https://github.com/QubesOS/qubes-issues/issues/6739>`__
- `#10345: Specific exception against PermissionDenied when API argument is invalid <https://github.com/QubesOS/qubes-issues/issues/10345>`__

Since the Admin API is continuously growing and changing, continuous security assessments are required. A `Fuzzer <https://en.wikipedia.org/wiki/Fuzzing>`__ would help to automate part of these assessments.

**Expected results**:

- fully automated & extensible Fuzzer for parts of the Admin API

- user & developer documentation



**Difficulty**: medium

**Prerequisites**:

- basic Python understanding

- some knowledge about fuzzing & existing fuzzing frameworks (e.g. `oss-fuzz <https://github.com/google/oss-fuzz/tree/master/projects/qubes-os>`__)

- a hacker’s curiosity



**Size of the project**: 175 hours

**Mentor**: Inquire on :ref:`qubes-devel <introduction/support:qubes-devel>`.

Secure Boot support
^^^^^^^^^^^^^^^^^^^


**Project**: Add support for protecting boot binaries with Secure Boot technology, using user-generated keys.

**Brief explanation**: Since recently, Xen supports “unified EFI boot” which allows to sign not only Xen binary itself, but also dom0 kernel and their parameters. While the base technology is there, enabling it is a painful and complex process. The goal of this project is to integrate configuration of this feature into Qubes, automating as much as possible. See discussion in `issue #4371 <https://github.com/QubesOS/qubes-issues/issues/4371>`__

**Expected results**:

- a tool to prepare relevant boot files for unified Xen EFI boot - this includes collecting Xen, dom0 kernel, initramfs, config file, and possibly few more (ucode update?); the tool should then sign the file with user provided key (preferably propose to generate it too)

- integrate it with updates mechanism, so new Xen or dom0 kernel will be picked up automatically

- include a fallback configuration that can be used for troubleshooting (main unified Xen EFI intentionally does not allow to manipulate parameters at boot time)



**Difficulty**: hard

**Knowledge prerequisite**:

- basic understanding of Secure Boot

- Bash and Python scripting



**Size of the project**: 175 hours

**Mentor**: `Marek Marczykowski-Górecki <https://www.qubes-os.org/team/>`__

Reduce logging of Disposable VMs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Reduce logging of Disposable VMs

**Brief explanation**: Partial metadata of a DisposableVM is stored in the dom0 filesystem. This applies to various logs, GUI status files etc. There should be an option to hide as much of that as possible - including bypassing some logging, and removing various state files, or at the very least obfuscating any hints what is running inside DisposableVM. More details at `issue #4972 <https://github.com/QubesOS/qubes-issues/issues/4972>`__

**Expected results**: A DisposableVM should not leave logs hinting what was running inside.

**Difficulty**: medium

**Knowledge prerequisite**:

- Python scripting

- Basic knowledge of Linux system services management (systemd, syslog etc)



**Size of the project**: 350 hours

**Mentor**: `Marek Marczykowski-Górecki <https://www.qubes-os.org/team/>`__

Past Projects
-------------


You can view the projects we had in 2017 in the `GSoC 2017 archive <https://summerofcode.withgoogle.com/archive/2017/organizations/5074771758809088/>`__. We also participated in GSoC 2020 and GSoC 2021, and you can see the project in the `GSoC 2020 archive <https://summerofcode.withgoogle.com/archive/2020/organizations/4924517870206976/>`__ and `GSoC 2021 archive <https://summerofcode.withgoogle.com/archive/2021/organizations/5682513023860736>`__.

Here are some successful projects which have been implemented in the past by Google Summer of Code participants.

Template manager, new template distribution mechanism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Project**: Template manager, new template distribution mechanism

**Brief explanation**: Template VMs currently are distributed using RPM packages. There are multiple problems with that, mostly related to static nature of RPM package (what files belong to the package). This means such Template VM cannot be renamed, migrated to another storage (like LVM), etc. Also we don’t want RPM to automatically update template package itself (which would override all the user changes there). More details: `#2064 <https://github.com/QubesOS/qubes-issues/issues/2064>`__, `#2534 <https://github.com/QubesOS/qubes-issues/issues/2534>`__, `#3573 <https://github.com/QubesOS/qubes-issues/issues/3573>`__.

**Expected results**:

- Design new mechanism for distributing templates (possibly including some package format - either reuse something already existing, or design new one). The mechanism needs to handle:

  - integrity protection (digital signatures), not parsing any data in dom0 prior to signature verification

  - efficient handling of large sparse files

  - ability to deploy the template into various storage mechanisms (sparse files, LVM thin volumes etc).

  - template metadata, templates repository - enable the user to browse available templates (probably should be done in dedicated VM, or DisposableVM)

  - manual template removal by users (without it, see problems such as `#5509 <https://github.com/QubesOS/qubes-issues/issues/5509>`__



- Implement the above mechanism:

  - tool to download named template - should perform download operation in some VM (as dom0 have no network access), then transfer the data to dom0, verify its integrity and then create Template VM and feed it’s root filesystem image with downloaded data.

  - tool to browse templates repository - both CLI and GUI (preferably integrated with existing Template Manager tool)

  - integrate both tools - user should be able to choose some template to be installed from repository browsing tool - see `#1705 <https://github.com/QubesOS/qubes-issues/issues/1705>`__ for some idea (this one lacks integrity verification, but a similar service could be developed with that added)



- If new “package” format is developed, add support for it into `linux-template-builder <https://github.com/QubesOS/qubes-linux-template-builder>`__.

- Document the mechanism.

- Write unit tests and integration tests.



**Knowledge prerequisite**:

- Large files (disk images) handling (sparse files, archive formats)

- Bash and Python scripting

- Data integrity handling - digital signatures (gpg2, gpgv2)

- PyGTK

- RPM package format, (yum) repository basics



**Mentor**: `Marek Marczykowski-Górecki <https://www.qubes-os.org/team/>`__


----


We adapted some of the language here about GSoC from the `KDE GSoC page <https://community.kde.org/GSoC>`__.
