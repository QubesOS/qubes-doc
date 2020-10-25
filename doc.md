---
layout: doc
title: Documentation
permalink: /doc/
redirect_from:
- /en/doc/
- /doc/UserDoc/
- /wiki/UserDoc/
- /doc/QubesDocs/
- /wiki/QubesDocs/
- /help/
- /en/help/
- /en/community/
- /community/
---

# Qubes OS Documentation

Welcome to the Qubes OS documentation!

## Introduction

 * [What is Qubes OS?](/intro/)
 * [Video Tours](/video-tours/)
 * [Screenshots](/screenshots/)
 * [User FAQ](/faq/#users)
 * [Reporting Bugs and Other Issues](/doc/reporting-bugs/)
 * [Help, Support, Mailing Lists, and Forum](/support/)
 * [How to Contribute](/doc/contributing/)

## Project Security

 * [Security Center](/security/)
 * [Security FAQ](/faq/#general--security)
 * [Security Pack](/security/pack/)
 * [Security Bulletins](/security/bulletins/)
 * [Canaries](/security/canaries/)
 * [Xen Security Advisory (XSA) Tracker](/security/xsa/)
 * [Verifying Signatures](/security/verifying-signatures/)
 * [Qubes PGP Keys](https://keys.qubes-os.org/keys/)


## User Documentation

Core documentation for Qubes users.

### Choosing Your Hardware

 * [System Requirements](/doc/system-requirements/)
 * [Certified Hardware](/doc/certified-hardware/)
 * [Hardware Compatibility List (HCL)](/hcl/)
 * [Hardware Testing](/doc/hardware-testing/)

### Downloading, Installing, and Upgrading Qubes

 * [Downloads](/downloads/)
 * [Installation Guide](/doc/installation-guide/)
 * [Upgrade Guides](/doc/upgrade/)
 * [Supported Versions](/doc/supported-versions/)
 * [Version Scheme](/doc/version-scheme/)
 * [Testing New Releases and Updates](/doc/testing/)

### Common Tasks

 * [Getting Started](/getting-started/)
 * [Copying and Pasting Text Between Domains](/doc/copy-paste/)
 * [Copying and Moving Files Between Domains](/doc/copying-files/)
 * [Copying from (and to) Dom0](/doc/copy-from-dom0/)
 * [Updating Qubes OS](/doc/updating-qubes-os/)
 * [Installing and Updating Software in Dom0](/doc/software-update-dom0/)
 * [Installing and Updating Software in DomUs](/doc/software-update-domu/)
 * [Backup, Restoration, and Migration](/doc/backup-restore/)
 * [Volume Backup and Revert](/doc/volume-backup-revert/)
 * [DisposableVMs](/doc/disposablevm/)
 * [Block (or Storage) Devices](/doc/block-devices/)
 * [USB Devices](/doc/usb-devices)
 * [PCI Devices](/doc/pci-devices/)
 * [Device Handling](/doc/device-handling/)
 * [Optical Discs](/doc/optical-discs/)
 * [Application Shortcuts](/doc/managing-appvm-shortcuts/)
 * [Fullscreen Mode](/doc/full-screen-mode/)

### Managing Operating Systems within Qubes

 * [TemplateVMs](/doc/templates/)
 * [Fedora](/doc/templates/fedora/)
 * [Debian](/doc/templates/debian/)
 * [Minimal TemplateVMs](/doc/templates/minimal/)
 * [Windows](/doc/windows/)
 * [StandaloneVMs and HVMs](/doc/standalone-and-hvm/)

### Security in Qubes

 * [Qubes Firewall](/doc/firewall/)
 * [Understanding and Preventing Data Leaks](/doc/data-leaks/)
 * [Passwordless Root Access in VMs](/doc/vm-sudo/)
 * [Device Handling Security](/doc/device-handling-security/)
 * [Anti Evil Maid](/doc/anti-evil-maid/)
 * [Split GPG](/doc/split-gpg/)
 * [U2F Proxy](/doc/u2f-proxy/)
 * [YubiKey](/doc/yubi-key/)

### Advanced Configuration

 * [Configuration Files](/doc/config-files/)
 * [Storing AppVMs on Secondary Drives](/doc/secondary-storage/)
 * [RPC Policies](/doc/rpc-policy/)
 * [USB Qubes](/doc/usb-qubes/)
 * [Managing VM Kernels](/doc/managing-vm-kernel/)
 * [Salt Management Stack](/doc/salt/)
 * [DisposableVM Customization](/doc/disposablevm-customization/)
 * [Making Any File Persistent Using `bind-dirs`](/doc/bind-dirs/)
 * [GUI Configuration](/doc/gui-configuration/)
 * [Resizing Disk Images](/doc/resize-disk-image/)
 * [Troubleshooting Newer Hardware](/doc/newer-hardware-troubleshooting/)
 * [Mounting and Decrypting Qubes Partitions from Outside Qubes](/doc/mount-from-other-os/)
 * [KDE](/doc/kde/)
 * [i3 Window Manager](/doc/i3/)
 * [awesome Window Manager](/doc/awesome/)

### Troubleshooting

 * [Installation Troubleshooting](/doc/installation-troubleshooting)
 * [UEFI Troubleshooting](/doc/uefi-troubleshooting/)
 * [Suspend/Resume Troubleshooting](/doc/suspend-resume-troubleshooting/)
 * [VM Troubleshooting](/doc/vm-troubleshooting/)
 * [HVM Troubleshooting](/doc/hvm-troubleshooting/)
 * [Disk Troubleshooting](/doc/disk-troubleshooting/)
 * [PCI Troubleshooting](/doc/pci-troubleshooting/)
 * [USB Troubleshooting](/doc/usb-troubleshooting/)

### Reference Pages

 * [Command-line Tools](/doc/tools/)
 * [Glossary](/doc/glossary/)
 * [Qubes Service Framework](/doc/qubes-service/)
 * [Command Execution in VMs (and Qubes RPC)](/doc/qrexec/)
 * [Deprecated Documentation](https://github.com/QubesOS/qubesos.github.io#deprecated-documentation)


## Developer Documentation

Core documentation for Qubes developers and advanced users.

### General

 * [Developer FAQ](/faq/#developers)
 * [Package Contributions](/doc/package-contributions/)
 * [Documentation Guidelines](/doc/doc-guidelines/)
 * [Community-Developed Feature Tracker](/qubes-issues/)
 * [Google Summer of Code](/gsoc/)
 * [Google Season of Docs](/gsod/)
 * [Books for Developers](/doc/devel-books/)
 * [Style Guide](/doc/style-guide/)
 * [Usability & UX](/doc/usability-ux/)

### Code

 * [Source Code](/doc/source-code/)
 * [Software License](/doc/license/)
 * [Coding Guidelines](/doc/coding-style/)
 * [Code Signing](/doc/code-signing/)

### System

 * [Qubes OS Architecture Overview](/doc/architecture/)
 * [Security-critical Code in Qubes OS](/doc/security-critical-code/)
 * [Qubes Core Admin](https://dev.qubes-os.org/projects/core-admin/en/latest/)
 * [Qubes Core Admin Client](https://dev.qubes-os.org/projects/core-admin-client/en/latest/)
 * [Qubes Admin API](/news/2017/06/27/qubes-admin-api/)
 * [Qubes Core Stack](/news/2017/10/03/core3/)
 * [Qubes GUI virtualization protocol](/doc/gui/)
 * [Networking in Qubes](/doc/networking/)
 * [Implementation of template sharing and updating](/doc/template-implementation/)
 * [Storage Pools](/doc/storage-pools/)
 * [Audio virtualization](/doc/audio-virtualization/)

### Services

 * [Inter-domain file copying](/doc/qfilecopy/) (deprecates [`qfileexchgd`](/doc/qfileexchgd/))
 * [Dynamic memory management in Qubes](/doc/qmemman/)
 * [Implementation of DisposableVMs](/doc/dvm-impl/)
 * [Dom0 secure update mechanism](/doc/dom0-secure-updates/)
 * [Qrexec: secure communication across domains](/doc/qrexec/)
 * [Qrexec: Qubes RPC internals](/doc/qrexec-internals/)
 * [Qrexec: Socket-based services](/doc/qrexec-socket-services/)

### Debugging

 * [Profiling python code](/doc/profiling/)
 * [Test environment in separate machine for automatic tests](/doc/test-bench/)
 * [Automated tests](/doc/automated-tests/)
 * [VM-dom0 internal configuration interface](/doc/vm-interface/)
 * [Debugging Windows VMs](/doc/windows-debugging/)
 * [Safe Remote Dom0 Terminals](/doc/safe-remote-ttys/)
 * [Mount LVM Image](/doc/mount-lvm-image/)

### Building

 * [Building Qubes](/doc/qubes-builder/) (["API" Details](/doc/qubes-builder-details/))
 * [Development Workflow](/doc/development-workflow/)
 * [Building Qubes OS ISO](/doc/qubes-iso-building/)
 * [Qubes Template Configuration Files](https://github.com/QubesOS/qubes-template-configs)

### Releases

 * [Release notes](/doc/releases/notes/)
 * [Release schedules](/doc/releases/schedules/)
 * [Release checklist](/doc/releases/todo/)


## External Documentation

Unofficial, third-party documentation from the Qubes community and others.
For more, please see [Qubes Community Documentation](https://github.com/Qubes-Community/Contents/tree/master/docs).

### Operating System Guides

 * [Template: Ubuntu](/doc/templates/ubuntu/)
 * [Template: Whonix](/doc/whonix/)
 * [Pentesting](/doc/pentesting/)
 * [Pentesting: BlackArch](/doc/pentesting/blackarch/)
 * [Pentesting: Kali](/doc/pentesting/kali/)
 * [Pentesting: PTF](/doc/pentesting/ptf/)
 * [Tips for Using Linux in an HVM](/doc/linux-hvm-tips/)
 * [Creating a NetBSD VM](/doc/netbsd/)

### Security Guides

 * [Security Guidelines](/doc/security-guidelines/)
 * [Using Multi-factor Authentication with Qubes](/doc/multifactor-authentication/)
 * [How to Set Up a Split Bitcoin Wallet in Qubes](/doc/split-bitcoin/)
 * [Split dm-crypt](https://github.com/rustybird/qubes-split-dm-crypt)
 * [Split SSH](https://kushaldas.in/posts/using-split-ssh-in-qubesos-4-0.html)
 * [Using OnlyKey with Qubes OS](https://docs.crp.to/qubes.html)

### Privacy Guides

 * [Whonix for Privacy & Anonymity](/doc/whonix/)
 * [Running Tails in Qubes](/doc/tails/)
 * [Anonymizing your MAC Address](/doc/anonymizing-your-mac-address/)
 * [Signal](/doc/signal/)
 * [Reducing the fingerprint of the text-based web browser w3m](/doc/w3m/)

### Configuration Guides

 * [Qubes Tips and Tricks](/doc/tips-and-tricks/)
 * [How to set up a ProxyVM as a VPN Gateway](/doc/vpn/)
 * [Multibooting](/doc/multiboot/)
 * [Changing your Time Zone](/doc/change-time-zone/)
 * [Installing ZFS in Qubes](/doc/zfs/)
 * [Mutt Guide](/doc/mutt/)
 * [Postfix Guide](/doc/postfix/)
 * [Fetchmail Guide](/doc/fetchmail/)
 * [Creating Custom NetVMs and ProxyVMs](https://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html)
 * [How to make proxy for individual tcp connection from networkless VM](https://groups.google.com/group/qubes-devel/msg/4ca950ab6d7cd11a)
 * [Adding Bridge Support to the NetVM (EXPERIMENTAL)](/doc/network-bridge-support/)
 * [Enabling TRIM for SSD disks](/doc/disk-trim/)
 * [Configuring a Network Printer](/doc/network-printer/)
 * [Using External Audio Devices](/doc/external-audio/)
 * [Rxvt Guide](/doc/rxvt/)
 * [Adding SSD storage cache](https://groups.google.com/d/msgid/qubes-users/a08359c9-9eb0-4d1a-ad92-a8a9bc676ea6%40googlegroups.com)
 * [How to Make a Multimedia TemplateVM](/doc/multimedia/)

### Customization Guides

 * [Customizing Fedora minimal templates](/doc/fedora-minimal-template-customization/)
 * [Customizing Windows 7 templates](/doc/windows-template-customization/)
 * [Language Localization](/doc/language-localization/)
 * [Dark Theme in Dom0 and DomU](/doc/dark-theme/)
 * [Safely Removing TemplateVM Packages (Example: Thunderbird)](/doc/removing-templatevm-packages/)

### Troubleshooting

 * [Installing on system with new AMD GPU (missing firmware problem)](https://groups.google.com/group/qubes-devel/browse_thread/thread/e27a57b0eda62f76)
 * [How to install an Nvidia driver in dom0](/doc/install-nvidia-driver/)
 * [Nvidia troubleshooting guide](/doc/nvidia-troubleshooting/)
 * [Lenovo ThinkPad Troubleshooting](/doc/thinkpad-troubleshooting/)
 * [Apple MacBook Troubleshooting](/doc/macbook-troubleshooting/)
 * [Getting Sony Vaio Z laptop to work with Qubes](/doc/sony-vaio-tinkering/)
 * [Intel Integrated Graphics Troubleshooting](/doc/intel-igfx-troubleshooting/)

### Building Guides

 * [Building a TemplateVM based on a new OS (ArchLinux example)](/doc/building-non-fedora-template/)
 * [Building the Archlinux Template](/doc/building-archlinux-template/)
 * [Building the Whonix Templates](/doc/building-whonix-template/)
 * [How to compile kernels for dom0](https://groups.google.com/d/topic/qubes-users/yBeUJPwKwHM/discussion)

