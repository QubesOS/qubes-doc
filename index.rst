=============
Documentation
=============

:doc:`core-admin:index`

=================
Table of contents
=================


.. _introduction:

.. toctree::
   :maxdepth: 1
   :caption: Introduction

   introduction/intro
   introduction/screenshots
   introduction/video-tours
   introduction/getting-started
   introduction/faq
   introduction/issue-tracking
   introduction/support
   introduction/contributing
   introduction/statistics
   introduction/code-of-conduct
   introduction/privacy


==================
User Documentation
==================


Core documentation for Qubes users.


.. _choosing-your-hardware:

.. toctree::
   :maxdepth: 1
   :caption: Choosing Your Hardware

   user/hardware/system-requirements
   user/hardware/certified-hardware/certified-hardware
   Community-recommended hardware <https://forum.qubes-os.org/t/5560>
   Hardware compatibility list (HCL) <https://www.qubes-os.org/hcl/>
   user/hardware/how-to-use-the-hcl


.. _downloading-installing-and-upgrading-qubes:

.. toctree::
   :maxdepth: 1
   :caption: Downloading, Installing, and Upgrading Qubes

   Download Qubes OS <https://www.qubes-os.org/downloads/>
   Download mirrors <https://www.qubes-os.org/downloads/mirrors/>
   user/downloading-installing-upgrading/installation-guide
   user/downloading-installing-upgrading/install-security
   user/downloading-installing-upgrading/upgrade/upgrade
   user/downloading-installing-upgrading/supported-releases
   user/downloading-installing-upgrading/testing


.. _how-to-guides:

.. toctree::
   :maxdepth: 1
   :caption: How-to guides

   user/how-to-guides/how-to-organize-your-qubes
   user/how-to-guides/how-to-update
   user/how-to-guides/how-to-back-up-restore-and-migrate
   user/how-to-guides/how-to-copy-and-paste-text
   user/how-to-guides/how-to-copy-and-move-files
   user/how-to-guides/how-to-copy-from-dom0
   user/how-to-guides/how-to-install-software
   user/how-to-guides/how-to-use-disposables
   user/how-to-guides/how-to-enter-fullscreen-mode
   user/how-to-guides/how-to-use-devices
   user/how-to-guides/how-to-use-block-storage-devices
   user/how-to-guides/how-to-use-usb-devices
   user/how-to-guides/how-to-use-pci-devices
   user/how-to-guides/how-to-use-optical-discs
   user/how-to-guides/how-to-reinstall-a-template


.. _templates:

.. toctree::
   :maxdepth: 1
   :caption: Templates

   user/templates/templates
   user/templates/fedora/fedora
   user/templates/fedora/fedora-upgrade
   user/templates/debian/debian
   user/templates/debian/debian-upgrade
   user/templates/minimal-templates
   user/templates/xfce-templates
   user/templates/windows/windows


.. _troubleshooting:

.. toctree::
   :maxdepth: 1
   :caption: Troubleshooting

   user/troubleshooting/installation-troubleshooting
   user/troubleshooting/update-troubleshooting
   user/troubleshooting/debian-and-whonix-update-troubleshooting
   user/troubleshooting/hardware-troubleshooting
   user/troubleshooting/uefi-troubleshooting
   user/troubleshooting/autostart-troubleshooting
   user/troubleshooting/resume-suspend-troubleshooting
   user/troubleshooting/app-menu-shortcut-troubleshooting
   user/troubleshooting/vm-troubleshooting
   user/troubleshooting/hvm-troubleshooting
   user/troubleshooting/disk-troubleshooting
   user/troubleshooting/pci-troubleshooting
   user/troubleshooting/usb-troubleshooting
   user/troubleshooting/gui-troubleshooting
   user/troubleshooting/media-troubleshooting
   user/troubleshooting/vpn-troubleshooting


.. _security:
.. _security-in-qubes:

.. toctree::
   :maxdepth: 1
   :caption: Security in Qubes

   user/security-in-qubes/firewall
   user/security-in-qubes/data-leaks
   user/security-in-qubes/vm-sudo
   user/security-in-qubes/device-handling-security
   user/security-in-qubes/anti-evil-maid
   user/security-in-qubes/split-gpg
   user/security-in-qubes/mfa
   user/security-in-qubes/ctap-proxy


.. _advanced-topics:

.. toctree::
   :maxdepth: 1
   :caption: Advanced topics

   user/advanced-topics/how-to-install-software-in-dom0
   user/advanced-topics/volume-backup-revert
   user/advanced-topics/standalones-and-hvms
   user/advanced-topics/config-files
   user/advanced-topics/secondary-storage
   user/advanced-topics/rpc-policy
   user/advanced-topics/usb-qubes
   user/advanced-topics/managing-vm-kernels
   user/advanced-topics/salt
   user/advanced-topics/gui-domain
   user/advanced-topics/disposable-customization
   user/advanced-topics/installing-contributed-packages
   user/advanced-topics/bind-dirs
   user/advanced-topics/gui-configuration
   user/advanced-topics/resize-disk-image
   user/advanced-topics/qubes-service
   user/advanced-topics/mount-from-other-os
   user/advanced-topics/kde
   user/advanced-topics/i3
   user/advanced-topics/awesomewm


.. _reference:

.. toctree::
   :maxdepth: 1
   :caption: Reference

   user/reference/tools
   user/reference/glossary


.. _project-security:

.. toctree::
   :maxdepth: 1
   :caption: Project Security

   project-security/security
   project-security/security-pack
   project-security/verifying-signatures


=======================
Developer Documentation
=======================


Core documentation for Qubes developers and advanced users.

.. _general:

.. toctree::
   :maxdepth: 1
   :caption: Developers - general

   developer/general/package-contributions
   developer/general/gsoc
   developer/general/gsod
   developer/general/how-to-edit-the-rst-documentation
   developer/general/rst-documentation-style-guide
   developer/general/how-to-edit-the-website
   developer/general/website-style-guide
   developer/general/continuous-integration
   developer/general/usability-ux
   developer/general/developing-gui-applications
   Visual style guide <https://www.qubes-os.org/doc/visual-style-guide/>
   developer/general/research
   developer/general/devel-books


.. _code:

.. toctree::
   :maxdepth: 1
   :caption: Developers - code

   developer/code/source-code
   developer/code/license
   developer/code/coding-style
   developer/code/code-signing


.. _system:

.. toctree::
   :maxdepth: 1
   :caption: Developers - system

   developer/system/architecture
   developer/system/security-design-goals
   developer/system/security-critical-code
   Qubes core admin <https://dev.qubes-os.org/projects/core-admin/>
   Qubes core admin client <https://dev.qubes-os.org/projects/core-admin-client/>
   Qubes core stack <https://www.qubes-os.org/news/2017/10/03/core3/>
   developer/system/gui
   developer/system/networking
   developer/system/template-implementation
   developer/system/audio
   developer/system/template-manager


.. _services:

.. toctree::
   :maxdepth: 1
   :caption: Developers - services

   developer/services/qfilecopy
   developer/services/qmemman
   developer/services/disposablevm-implementation
   developer/services/dom0-secure-updates
   developer/services/qrexec
   developer/services/qrexec2
   developer/services/qrexec-internals
   developer/services/qrexec-socket-services
   developer/services/admin-api
   developer/services/qfileexchgd


.. _debugging:

.. toctree::
   :maxdepth: 1
   :caption: Developers - debugging

   developer/debugging/test-bench
   developer/debugging/automated-tests
   developer/debugging/vm-interface
   developer/debugging/windows-debugging
   developer/debugging/safe-remote-ttys
   developer/debugging/mount-lvm-image


.. _building:

.. toctree::
   :maxdepth: 1
   :caption: Developers - building

   developer/building/qubes-builder-v2
   developer/building/qubes-builder-details
   developer/building/development-workflow
   developer/building/qubes-iso-building
   Qubes template configs <https://github.com/QubesOS/qubes-template-configs>


.. _releases:

.. toctree::
   :maxdepth: 1
   :caption: Developers - releases

   developer/releases/notes
   developer/releases/schedules
   developer/releases/todo
   developer/releases/version-scheme


======================
External Documentation
======================

Unofficial, third-party documentation from the Qubes community and
others.

.. _external-operating-system-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Operating System Guides

   Template: Ubuntu <https://github.com/Qubes-Community/Contents/blob/master/docs/os/ubuntu.md>
   Template: Whonix <https://github.com/Qubes-Community/Contents/blob/master/docs/privacy/whonix.md>
   Template: CentOS <https://github.com/Qubes-Community/Contents/blob/master/docs/os/centos.md>
   Template: Gentoo <https://github.com/Qubes-Community/Contents/blob/master/docs/os/gentoo.md>
   Pentesting <https://github.com/Qubes-Community/Contents/blob/master/docs/os/pentesting.md>
   Pentesting: BlackArch <https://github.com/Qubes-Community/Contents/blob/master/docs/os/pentesting/blackarch.md>
   Pentesting: Kali <https://github.com/Qubes-Community/Contents/blob/master/docs/os/pentesting/kali.md>
   Pentesting: PTF <https://github.com/Qubes-Community/Contents/blob/master/docs/os/pentesting/ptf.md>
   Tips for Using Linux in an HVM <https://github.com/Qubes-Community/Contents/blob/master/docs/os/linux-hvm-tips.md>
   Creating a NetBSD VM <https://github.com/Qubes-Community/Contents/blob/master/docs/os/netbsd.md>


.. _exteranl-security-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Security Guides

   Security Guidelines <https://github.com/Qubes-Community/Contents/blob/master/docs/security/security-guidelines.md>
   Using Multi-factor Authentication with Qubes <https://github.com/Qubes-Community/Contents/blob/master/docs/security/multifactor-authentication.md>
   How to Set Up a Split Bitcoin Wallet in Qubes <https://github.com/Qubes-Community/Contents/blob/master/docs/security/split-bitcoin.md>
   Split dm-crypt <https://github.com/rustybird/qubes-split-dm-crypt>
   Split SSH <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/split-ssh.md>
   Using OnlyKey with Qubes OS <https://docs.crp.to/qubes.html>


.. _external-privacy-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Privacy Guides

   Whonix for Privacy & Anonymity <https://github.com/Qubes-Community/Contents/blob/master/docs/privacy/whonix.md>
   Running Tails in Qubes <https://github.com/Qubes-Community/Contents/blob/master/docs/privacy/tails.md>
   Anonymizing your MAC Address <https://github.com/Qubes-Community/Contents/blob/master/docs/privacy/anonymizing-your-mac-address.md>
   Signal <https://github.com/Qubes-Community/Contents/blob/master/docs/privacy/signal.md>
   Reducing the fingerprint of the text-based web browser w3m <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/w3m.md>


.. _external-configuration-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Configuration Guides

   Qubes Tips and Tricks <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/tips-and-tricks.md>
   How to set up a ProxyVM as a VPN Gateway <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md>
   Multibooting <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/multiboot.md>
   Changing your Time Zone <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/change-time-zone.md>
   Installing ZFS in Qubes <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/zfs.md>
   Mutt Guide <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/mutt.md>
   Postfix Guide <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/postfix.md>
   Fetchmail Guide <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/fetchmail.md>
   Creating Custom NetVMs and ProxyVMs <https://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html>
   How to make proxy for individual tcp connection from networkless VM <https://groups.google.com/group/qubes-devel/msg/4ca950ab6d7cd11a>
   Adding Bridge Support to the NetVM (EXPERIMENTAL) <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/network-bridge-support.md>
   Screen Sharing <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/screen-share.md>
   Enabling TRIM for SSD disks <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/disk-trim.md>
   Configuring a Network Printer <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/network-printer.md>
   Using External Audio Devices <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/external-audio.md>
   Rxvt Guide <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/rxvt.md>
   Adding SSD storage cache <https://groups.google.com/d/msgid/qubes-users/a08359c9-9eb0-4d1a-ad92-a8a9bc676ea6%40googlegroups.com>
   How to Make a Multimedia TemplateVM <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/multimedia.md>
   How to install an Nvidia driver in dom0 <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/install-nvidia-driver.md>


.. _external-customization-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Customization Guides

   Customizing Fedora minimal templates <https://github.com/Qubes-Community/Contents/blob/master/docs/customization/fedora-minimal-template-customization.md>
   Customizing Windows 7 templates <https://github.com/Qubes-Community/Contents/blob/master/docs/customization/windows-template-customization.md>
   Language Localization <https://github.com/Qubes-Community/Contents/blob/master/docs/customization/language-localization.md>
   Dark Theme in Dom0 and DomU <https://github.com/Qubes-Community/Contents/blob/master/docs/customization/dark-theme.md>
   Safely Removing TemplateVM Packages (Example: Thunderbird) <https://github.com/Qubes-Community/Contents/blob/master/docs/customization/removing-templatevm-packages.md>


.. _external-troubleshooting:

.. toctree::
   :maxdepth: 1
   :caption: External - Troubleshooting

   Nvidia troubleshooting guide <https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/nvidia-troubleshooting.md>
   Lenovo ThinkPad Troubleshooting <https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/thinkpad-troubleshooting.md>
   Apple MacBook Troubleshooting <https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/macbook-troubleshooting.md>
   Sony Vaio Troubleshooting <https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/sony-vaio-tinkering.md>
   Intel Integrated Graphics Troubleshooting <https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/intel-igfx-troubleshooting.md>
   Multiboot Troubleshooting <https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/multiboot.md#troubleshooting>
   Application Troubleshooting <https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/application-troubleshooting.md>
   Tails Troubleshooting <https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/tails-troubleshooting.md>


.. _external-building-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Building Guides

   Building a TemplateVM based on a new OS (ArchLinux example) <https://github.com/Qubes-Community/Contents/blob/master/docs/building/building-non-fedora-template.md>
   Building the Archlinux Template <https://github.com/Qubes-Community/Contents/blob/master/docs/building/building-archlinux-template.md>
   Building the Whonix Templates <https://github.com/Qubes-Community/Contents/blob/master/docs/building/building-whonix-template.md>
   How to compile kernels for dom0 <https://groups.google.com/d/topic/qubes-users/yBeUJPwKwHM/discussion>

