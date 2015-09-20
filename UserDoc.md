---
layout: doc
title: UserDoc
permalink: /doc/UserDoc/
redirect_from: /wiki/UserDoc/
---

Qubes User Documentation
========================

The Basics
----------
 *  [A Simple Introduction to Qubes](/doc/SimpleIntro/)
 *  [Getting Started](/doc/GettingStarted/)
 *  [Further reading: How is Qubes different from...?](http://blog.invisiblethings.org/2012/09/12/how-is-qubes-os-different-from.html)
 *  [Further reading: Why Qubes is more than a collection of VMs](http://www.invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf)


Choosing Your Hardware
----------------------
 *  [System Requirements](/doc/SystemRequirements/)
 *  [Hardware Compatibility List (HCL)](/hcl)
 *  Qubes Certified Laptops (coming soon!)


Installing Qubes
----------------
 *  [Use Qubes without installing: Qubes Live USB (alpha)](https://groups.google.com/d/msg/qubes-users/IQdCEpkooto/iyMh3LuzCAAJ)
 *  [How to Install Qubes](/doc/InstallationGuide/)
 *  [Qubes Downloads](/doc/Downloads/)
 *  [Why and How to Verify Signatures](/doc/VerifyingSignatures/)
 *  [Security Considerations when Installing](/doc/InstallSecurity/)


Common Tasks
------------
 *  [Copying and Pasting Text Between Domains](/doc/CopyPaste/)
 *  [Copying and Moving Files Between Domains](/doc/CopyingFiles/)
 *  [Copying Files to and from dom0](/doc/CopyToDomZero/)
 *  [Mounting USB Drives to AppVMs](/doc/StickMounting/)
 *  [Updating Software in dom0](/doc/SoftwareUpdateDom0/)
 *  [Updating and Installing Software in VMs](/doc/SoftwareUpdateVM/)
 *  [Backup, Restoration, and Migration](/doc/BackupRestore/)
 *  [Disposable VMs](/doc/DisposableVms/)
 *  [Managing Application Shortcuts](/doc/ManagingAppVmShortcuts/)
 *  [Enabling Fullscreen Mode](/doc/FullScreenMode/)


Managing Operating Systems within Qubes
---------------------------------------
 *  [TemplateVMs](/doc/Templates/)
 *  [Upgrading the Fedora 18 Template](/doc/FedoraTemplateUpgrade18/)
 *  [Upgrading the Fedora 20 Template](/doc/FedoraTemplateUpgrade20/)
 *  [Templates: Fedora - minimal](/doc/Templates/FedoraMinimal/)
 *  [Templates: Debian](/doc/Templates/Debian/)
 *  [Templates: Archlinux](/doc/Templates/Archlinux/)
 *  [Templates: Ubuntu](/doc/Templates/Ubuntu/)
 *  [Installing and Using Windows-based AppVMs (Qubes R2 Beta 3 and later)](/doc/WindowsAppVms/)
 *  [Creating and Using HVM and Windows Domains (Qubes R2+)](/doc/HvmCreate/)
 *  [Advanced options and troubleshooting of Qubes Tools for Windows (R3)](/doc/WindowsTools3/)
 *  [Advanced options and troubleshooting of Qubes Tools for Windows (R2)](/doc/WindowsTools2/)
 *  [Uninstalling Qubes Tools for Windows 2.x](/doc/UninstallingWindowsTools2/)
 *  [Tips for Using Linux in an HVM](/doc/LinuxHVMTips/)
 *  [Creating Whonix HVMs in Qubes](https://www.whonix.org/wiki/Qubes)
 *  [Creating NetBSD VM](https://groups.google.com/group/qubes-devel/msg/4015c8900a813985)


Security Guides
---------------
 *  [General Security Guidelines](/doc/SecurityGuidelines/)
 *  [Understanding Qubes Firewall](/doc/QubesFirewall/)
 *  [Understanding and Preventing Data Leaks](/doc/DataLeaks/)
 *  [Installing Anti Evil Maid](/doc/AntiEvilMaid/)
 *  [Using GPG more securely in Qubes: Split GPG](/doc/UserDoc/SplitGpg/)
 *  [Configuring YubiKey for user authentication](/doc/YubiKey/)
 *  [Note regarding password-less root access in VM](/doc/VMSudo/)


Configuration Guides
--------------------
 *  [Configuration Files](/doc/UserDoc/ConfigFiles/)
 *  [How to Install a Transparent Tor ProxyVM (TorVM)](/doc/UserDoc/TorVM/)
 *  [How to set up a ProxyVM as a VPN Gateway](/doc/VPN/)
 *  [Storing AppVMs on Secondary Drives](/doc/SecondaryStorage/)
 *  [Where are my external storage devices mounted?](/doc/ExternalDeviceMountPoint/)
 *  [Resizing AppVM and HVM Disk Images](/doc/ResizeDiskImage/)
 *  [Extending \`root.img\` Size](/doc/ResizeRootDiskImage/)
 *  [Installing ZFS in Qubes](/doc/ZFS/)
 *  [Creating Custom NetVMs and ProxyVMs](http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html)
 *  [How to make proxy for individual tcp connection from networkless VM](https://groups.google.com/group/qubes-devel/msg/4ca950ab6d7cd11a)
 *  [HTTP filtering proxy in Qubes firewall VM](https://groups.google.com/group/qubes-devel/browse_thread/thread/5252bc3f6ed4b43e/d881deb5afaa2a6c#39c95d63fccca12b)
 *  [Adding Bridge Support to the NetVM (EXPERIMENTAL)](/doc/NetworkBridgeSupport/)
 *  [Assigning PCI Devices to AppVMs](/doc/AssigningDevices/)
 *  [Enabling TRIM for SSD disks](/doc/DiskTRIM/)
 *  [Configuring a Network Printer](/doc/NetworkPrinter/)
 *  [Using External Audio Devices](/doc/ExternalAudio/)
 *  [Booting with GRUB2 and GPT](https://groups.google.com/group/qubes-devel/browse_thread/thread/e4ac093cabd37d2b/d5090c20d92c4128#d5090c20d92c4128)
 *  [Installing on system with new AMD GPU (missing firmware problem)](https://groups.google.com/group/qubes-devel/browse_thread/thread/e27a57b0eda62f76)
 *  [How to install an Nvidia driver in dom0](/doc/InstallNvidiaDriver/)
 *  [Solving problems with Macbook Air 2012](https://groups.google.com/group/qubes-devel/browse_thread/thread/b8b0d819d2a4fc39/d50a72449107ab21#8a9268c09d105e69)
 *  [Getting Sony Vaio Z laptop to work with Qubes](/doc/SonyVaioTinkering/)
 *  [Getting Lenovo 450 to work with Qubes](/doc/Lenovo450Tinkering/)


Customization Guides
--------------------
 *  [DispVM Customization](/doc/UserDoc/DispVMCustomization/)
 *  [XFCE Installation in dom0](/doc/UserDoc/XFCE/)
 *  [Customizing the GUI experience with KDE](https://groups.google.com/d/topic/qubes-users/KhfzF19NG1s/discussion)
 *  [Language Localization](/doc/LanguageLocalization/)


Reference Pages
---------------
 *  [Dom0 Command-Line Tools](/doc/DomZeroTools/)
 *  [DomU Command-Line Tools](/doc/VmTools/)
 *  [Glossary of Qubes Terminology](/doc/Glossary/)
 *  [Qubes Service Framework](/doc/QubesService/)
 *  [Command Execution in VMs (and Qubes RPC)](/doc/Qrexec/)
