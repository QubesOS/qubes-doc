---
layout: doc-index
title: Documentation
permalink: /doc/
redirect_from:
- /en/doc/
- /doc/UserDoc/
- /wiki/UserDoc/
- /doc/PedOSDocs/
- /wiki/PedOSDocs/
- /help/
- /en/help/
- /en/community/
- /community/
---
## Table of Contents
1. [Introduction](#introduction)
2. [Project Security](#project-security)
3. [User Documentation](#user-documentation)  
   3.1. [Choosing Your Hardware](#choosing-your-hardware)  
   3.2. [Downloading, Installing, and Upgrading PedOS](#downloading-installing-and-upgrading-PedOS)  
   3.3. [Common Tasks](#common-tasks)  
   3.4. [Managing Operating Systems within PedOS](#managing-operating-systems-within-PedOS)  
   3.5. [Security in PedOS](#security-in-PedOS)  
   3.6. [Advanced Configuration](#advanced-configuration)  
   3.7. [Reference Pages](#reference-pages)
4. [Developer Documentation](#developer-documentation)  
   4.1. [General](#general)  
   4.2. [Code](#code)  
   4.3. [System](#system)  
   4.4. [Services](#services)  
   4.5. [Debugging](#debugging)  
   4.6. [Building](#building)  
   4.7. [Releases](#releases)
5. [External Documentation](#external-documentation)  
   5.1. [Operating System Guides](#operating-system-guides)  
   5.2. [Security Guides](#security-guides)  
   5.3. [Privacy Guides](#privacy-guides)  
   5.4. [Configuration Guides](#configuration-guides)  
   5.5. [Customization Guides](#customization-guides)  
   5.6. [Troubleshooting](#troubleshooting)  
   5.7. [Building Guides](#building-guides)

## Introduction

 * [What is PedOS?](/intro/)
 * [Video Tours](/video-tours/)
 * [Screenshots](/screenshots/)
 * [User FAQ](/faq/#users)
 * [Reporting Bugs and Other Issues](/doc/reporting-bugs/)
 * [Help, Support, and Mailing Lists](/support/)
 * [How to Contribute](/doc/contributing/)

## Project Security

 * [Security Center](/security/)
 * [Security FAQ](/faq/#general--security)
 * [Security Pack](/security/pack/)
 * [Security Bulletins](/security/bulletins/)
 * [Canaries](/security/canaries/)
 * [Xen Security Advisory (XSA) Tracker](/security/xsa/)
 * [Verifying Signatures](/security/verifying-signatures/)
 * [PedOS PGP Keys](https://keys.PedOS.org/keys/)


## User Documentation

Core documentation for PedOS users.

### Choosing Your Hardware

 * [System Requirements](/doc/system-requirements/)
 * [Certified Hardware](/doc/certified-hardware/)
 * [Hardware Compatibility List (HCL)](/hcl/)
 * [Hardware Testing](/doc/hardware-testing/)

### Downloading, Installing, and Upgrading PedOS

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
 * [Updating PedOS](/doc/updating-PedOS/)
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

### Managing Operating Systems within PedOS

 * [TemplateVMs](/doc/templates/)
 * [Fedora](/doc/templates/fedora/)
 * [Debian](/doc/templates/debian/)
 * [Minimal TemplateVMs](/doc/templates/minimal/)
 * [Windows](/doc/windows/)
 * [StandaloneVMs and HVMs](/doc/standalone-and-hvm/)

### Security in PedOS

 * [PedOS Firewall](/doc/firewall/)
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
 * [USB PedOS](/doc/usb-PedOS/)
 * [Managing VM Kernels](/doc/managing-vm-kernel/)
 * [Salt Management Stack](/doc/salt/)
 * [DisposableVM Customization](/doc/disposablevm-customization/)
 * [Making Any File Persistent Using `bind-dirs`](/doc/bind-dirs/)
 * [GUI Configuration](/doc/gui-configuration/)
 * [Resizing Disk Images](/doc/resize-disk-image/)
 * [Troubleshooting UEFI](/doc/uefi-troubleshooting/)
 * [Troubleshooting Newer Hardware](/doc/newer-hardware-troubleshooting/)
 * [Mounting and Decrypting PedOS Partitions from Outside PedOS](/doc/mount-from-other-os/)
 * [KDE](/doc/kde/)
 * [i3 Window Manager](/doc/i3/)
 * [awesome Window Manager](/doc/awesome/)

### Reference Pages

 * [Command-line Tools](/doc/tools/)
 * [Glossary](/doc/glossary/)
 * [PedOS Service Framework](/doc/PedOS-service/)
 * [Command Execution in VMs (and PedOS RPC)](/doc/qrexec/)
 * [Deprecated Documentation](https://github.com/PedOS/PedOSos.github.io#deprecated-documentation)


## Developer Documentation

Core documentation for PedOS developers and advanced users.

### General

 * [Developer FAQ](/faq/#developers)
 * [Package Contributions](/doc/package-contributions/)
 * [Documentation Guidelines](/doc/doc-guidelines/)
 * [Community-Developed Feature Tracker](/PedOS-issues/)
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

 * [PedOS Architecture Overview](/doc/architecture/)
 * [PedOS Architecture Spec v0.3 [PDF]](/attachment/wiki/PedOSArchitecture/arch-spec-0.3.pdf)
 * [Security-critical Code in PedOS](/doc/security-critical-code/)
 * [PedOS Core Admin](https://dev.PedOS.org/projects/core-admin/en/latest/)
 * [PedOS Core Admin Client](https://dev.PedOS.org/projects/core-admin-client/en/latest/)
 * [PedOS Admin API](/news/2017/06/27/PedOS-admin-api/)
 * [PedOS Core Stack](/news/2017/10/03/core3/)
 * [PedOS GUI virtualization protocol](/doc/gui/)
 * [Networking in PedOS](/doc/networking/)
 * [Implementation of template sharing and updating](/doc/template-implementation/)
 * [Storage Pools](/doc/storage-pools/)
 * [Audio virtualization](/doc/audio-virtualization/)

### Services

 * [Inter-domain file copying](/doc/qfilecopy/) (deprecates [`qfileexchgd`](/doc/qfileexchgd/))
 * [Dynamic memory management in PedOS](/doc/qmemman/)
 * [Implementation of DisposableVMs](/doc/dvm-impl/)
 * [Dom0 secure update mechanism](/doc/dom0-secure-updates/)
 * [Qrexec: secure communication across domains](/doc/qrexec/)
 * [Qrexec: PedOS RPC internals](/doc/qrexec-internals/)
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

 * [Building PedOS](/doc/PedOS-builder/) (["API" Details](/doc/PedOS-builder-details/))
 * [Development Workflow](/doc/development-workflow/)
 * [Building PedOS ISO](/doc/PedOS-iso-building/)
 * [PedOS Template Configuration Files](https://github.com/PedOS/PedOS-template-configs)

### Releases

 * [Release notes](/doc/releases/notes/)
 * [Release schedules](/doc/releases/schedules/)
 * [Release checklist](/doc/releases/todo/)


## External Documentation

Unofficial, third-party documentation from the PedOS community and others.

 * [PedOS Community Documentation](https://github.com/PedOS-Community/Contents/tree/master/docs)

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
 * [Using Multi-factor Authentication with PedOS](/doc/multifactor-authentication/)
 * [How to Set Up a Split Bitcoin Wallet in PedOS](/doc/split-bitcoin/)
 * [Split dm-crypt](https://github.com/rustybird/PedOS-split-dm-crypt)
 * [Split SSH](https://kushaldas.in/posts/using-split-ssh-in-PedOSos-4-0.html)
 * [Using OnlyKey with PedOS](https://docs.crp.to/PedOS.html)

### Privacy Guides

 * [Whonix for Privacy & Anonymity](/doc/whonix/)
 * [Running Tails in PedOS](/doc/tails/)
 * [Anonymizing your MAC Address](/doc/anonymizing-your-mac-address/)
 * [Signal](/doc/signal/)
 * [Reducing the fingerprint of the text-based web browser w3m](/doc/w3m/)

### Configuration Guides

 * [PedOS Tips and Tricks](/doc/tips-and-tricks/)
 * [How to set up a ProxyVM as a VPN Gateway](/doc/vpn/)
 * [Multibooting](/doc/multiboot/)
 * [Changing your Time Zone](/doc/change-time-zone/)
 * [Installing ZFS in PedOS](/doc/zfs/)
 * [Mutt Guide](/doc/mutt/)
 * [Postfix Guide](/doc/postfix/)
 * [Fetchmail Guide](/doc/fetchmail/)
 * [Creating Custom NetVMs and ProxyVMs](https://theinvisiblethings.blogspot.com/2011/09/playing-with-PedOS-networking-for-fun.html)
 * [How to make proxy for individual tcp connection from networkless VM](https://groups.google.com/group/PedOS-devel/msg/4ca950ab6d7cd11a)
 * [Adding Bridge Support to the NetVM (EXPERIMENTAL)](/doc/network-bridge-support/)
 * [Enabling TRIM for SSD disks](/doc/disk-trim/)
 * [Configuring a Network Printer](/doc/network-printer/)
 * [Using External Audio Devices](/doc/external-audio/)
 * [Rxvt Guide](/doc/rxvt/)
 * [Adding SSD storage cache](https://groups.google.com/d/msgid/PedOS-users/a08359c9-9eb0-4d1a-ad92-a8a9bc676ea6%40googlegroups.com)
 * [How to Make a Multimedia TemplateVM](/doc/multimedia/)

### Customization Guides

 * [Customizing Fedora minimal templates](/doc/fedora-minimal-template-customization/)
 * [Customizing Windows 7 templates](/doc/windows-template-customization/)
 * [Language Localization](/doc/language-localization/)
 * [Dark Theme in Dom0 and DomU](/doc/dark-theme/)
 * [Safely Removing TemplateVM Packages (Example: Thunderbird)](/doc/removing-templatevm-packages/)

### Troubleshooting

 * [Home directory is out of disk space error](/doc/out-of-memory/)
 * [Installing on system with new AMD GPU (missing firmware problem)](https://groups.google.com/group/PedOS-devel/browse_thread/thread/e27a57b0eda62f76)
 * [How to install an Nvidia driver in dom0](/doc/install-nvidia-driver/)
 * [Nvidia troubleshooting guide](/doc/nvidia-troubleshooting/)
 * [Lenovo ThinkPad Troubleshooting](/doc/thinkpad-troubleshooting/)
 * [Apple MacBook Troubleshooting](/doc/macbook-troubleshooting/)
 * [Getting Sony Vaio Z laptop to work with PedOS](/doc/sony-vaio-tinkering/)
 * [Fixing wireless on suspend & resume](/doc/wireless-troubleshooting/)
 * [How to remove VMs manually](/doc/remove-vm-manually/)
 * [Intel Integrated Graphics Troubleshooting](/doc/intel-igfx-troubleshooting/)

### Building Guides

 * [Building a TemplateVM based on a new OS (ArchLinux example)](/doc/building-non-fedora-template/)
 * [Building the Archlinux Template](/doc/building-archlinux-template/)
 * [Building the Whonix Templates](/doc/building-whonix-template/)
 * [How to compile kernels for dom0](https://groups.google.com/d/topic/PedOS-users/yBeUJPwKwHM/discussion)

