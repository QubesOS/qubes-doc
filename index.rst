=============
Documentation
=============

=================
Table of contents
=================


.. _introduction:

.. toctree::
   :maxdepth: 1
   :caption: Introduction

   introduction/intro
   introduction/screenshots
   Introduction/video-tours
   introduction/security_architecture
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
   Community-recommended hardware <https://forum.qubes-os.org/t/community-recommended-computers/5560>
   Hardware compatibility list (HCL) <https://www.qubes-os.org/hcl/>
   user/hardware/how-to-use-the-hcl


.. _downloading-installing-and-upgrading-qubes:

.. toctree::
   :maxdepth: 1
   :caption: Downloading, Installing, and Upgrading Qubes

   Download Qubes OS <https://www.qubes-os.org/downloads/>
   user/downloading-installing-upgrading/download-mirrors
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
   user/how-to-guides/how-to-set-a-wallpaper
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
   user/how-to-guides/how-to-edit-a-policy
   user/how-to-guides/how-to-enable-a-service


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
   user/templates/windows/index


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
   Split GPG-1 <user/security-in-qubes/split-gpg>
   user/security-in-qubes/split-gpg-2
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
   developer/system/vm-sudo.rst


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

   Template: CentOS <https://forum.qubes-os.org/t/centos-rhel-clone-8-templatevm/19006>
   Template: Gentoo <https://forum.qubes-os.org/t/gentoo-templatevm/19007>
   Pentesting: BlackArch <https://forum.qubes-os.org/t/blackarch-templatevm/19010>
   Pentesting: Kali <https://forum.qubes-os.org/t/creating-a-kali-linux-templatevm/19071>
   Pentesting: PTF <https://forum.qubes-os.org/t/penetration-testers-framework-ptf-templatevm/19011>
   Tips for Using Linux in an HVM <https://forum.qubes-os.org/t/tips-for-linux-hvms/19008>
   Creating a NetBSD VM <https://forum.qubes-os.org/t/netbsd-qube/19009>


.. _external-security-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Security Guides

   Security Guidelines <https://forum.qubes-os.org/t/general-security-guidelines/19075>
   Using Multi-factor Authentication with Qubes <https://forum.qubes-os.org/t/using-multi-factor-authentication/19016>
   How to Set Up a Split Bitcoin Wallet in Qubes <https://forum.qubes-os.org/t/how-to-set-up-a-split-bitcoin-wallet/19017>
   Split dm-crypt <https://github.com/rustybird/qubes-split-dm-crypt>
   Split SSH <https://forum.qubes-os.org/t/split-ssh/19060>
   Using OnlyKey with Qubes OS <https://docs.crp.to/qubes.html>


.. _external-privacy-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Privacy Guides

   Whonix for Privacy & Anonymity <https://forum.qubes-os.org/t/whonix-for-privacy-anonymity/19014>
   Running Tails in Qubes <https://forum.qubes-os.org/t/tails-hvm/19012>
   Anonymizing your MAC Address <https://forum.qubes-os.org/t/anonymizing-your-mac-address/19072>
   Signal <https://forum.qubes-os.org/t/signal-messenger/19073>
   Reducing the fingerprint of the text-based web browser w3m <https://forum.qubes-os.org/t/reducing-the-fingerprint-of-the-text-based-web-browser-w3m/18993>


.. _external-configuration-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Configuration Guides

   How to set up a ProxyVM as a VPN Gateway <https://forum.qubes-os.org/t/configuring-a-proxyvm-vpn-gateway/19061>
   Multibooting <https://forum.qubes-os.org/t/multibooting-qubes/18988>
   Changing your Time Zone <https://forum.qubes-os.org/t/changing-your-time-zone/18983>
   Installing ZFS in Qubes <https://forum.qubes-os.org/t/zfs-in-qubes-os/18994>
   Mutt Guide <https://forum.qubes-os.org/t/mutt-mail-user-agent/18989>
   Postfix Guide <https://forum.qubes-os.org/t/postfix-mta/18991>
   Fetchmail Guide <https://forum.qubes-os.org/t/fetchmail/18985>
   Creating Custom NetVMs and ProxyVMs <https://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html>
   How to make proxy for individual tcp connection from networkless VM <https://groups.google.com/group/qubes-devel/msg/4ca950ab6d7cd11a>
   Adding Bridge Support to the NetVM (EXPERIMENTAL) <https://forum.qubes-os.org/t/network-bridge-support-experimental-and-unsupported/18990>
   Screen Sharing <https://forum.qubes-os.org/t/sharing-a-screen-across-qubes/19059>
   Enabling TRIM for SSD disks <https://forum.qubes-os.org/t/disk-trimming/19054>
   Configuring a Network Printer <https://forum.qubes-os.org/t/configuring-a-network-printer/19056>
   Using External Audio Devices <https://forum.qubes-os.org/t/using-external-audio-devices/18984>
   Rxvt Guide <https://forum.qubes-os.org/t/rxvt-terminal/18992>
   Adding SSD storage cache <https://groups.google.com/d/msgid/qubes-users/a08359c9-9eb0-4d1a-ad92-a8a9bc676ea6%40googlegroups.com>
   How to Make a Multimedia TemplateVM <https://forum.qubes-os.org/t/configuring-a-multimedia-templatevm/19055>
   How to install an Nvidia driver in dom0 <https://forum.qubes-os.org/t/nvidia-proprietary-driver-installation/18987>


.. _external-customization-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Customization Guides

   Customizing Fedora minimal templates <https://forum.qubes-os.org/t/fedora-packages-recommendations/18999>
   Customizing Windows 7 templates <https://forum.qubes-os.org/t/disable-uninstall-unnecessary-features-in-windows-qubes/19005>
   Language Localization <https://forum.qubes-os.org/t/language-localization/19001>
   Dark Theme in Dom0 and DomU <https://forum.qubes-os.org/t/dark-theme-in-dom0/18997>
   Safely Removing TemplateVM Packages (Example: Thunderbird) <https://forum.qubes-os.org/t/safely-uninstalling-packages-in-templatevms/19002>


.. _external-troubleshooting:

.. toctree::
   :maxdepth: 1
   :caption: External - Troubleshooting

   Nvidia troubleshooting guide <https://forum.qubes-os.org/t/nvidia-troubleshooting-guide/19021>
   Lenovo ThinkPad Troubleshooting <https://forum.qubes-os.org/t/lenovo-thinkpad-troubleshooting/19024>
   Apple MacBook Troubleshooting <https://forum.qubes-os.org/t/apple-macbook-troubleshooting/19020>
   Sony Vaio Troubleshooting <https://forum.qubes-os.org/t/sony-vaio-z-laptop-troubleshooting/19022>
   Intel Integrated Graphics Troubleshooting <https://forum.qubes-os.org/t/intel-integrated-graphics-troubleshooting/19081>
   Multiboot Troubleshooting <https://forum.qubes-os.org/t/multibooting-qubes/18988#troubleshooting-5>
   Application Troubleshooting <https://forum.qubes-os.org/t/troubleshooting-default-applications/19019>
   Tails Troubleshooting <https://forum.qubes-os.org/t/tails-troubleshooting-guide/19023>


.. _external-building-guides:

.. toctree::
   :maxdepth: 1
   :caption: External - Building Guides

   Building a TemplateVM based on a new OS (ArchLinux example) <https://forum.qubes-os.org/t/building-a-templatevm-for-a-new-os/18972>
   Building the Archlinux Template <https://forum.qubes-os.org/t/archlinux-minimal-template/19052>
   Building the Whonix Templates <https://forum.qubes-os.org/t/building-whonix-templates/18981>
   How to compile kernels for dom0 <https://groups.google.com/d/topic/qubes-users/yBeUJPwKwHM/discussion>

