---
layout: doc
title: Fedora Minimal Template
permalink: /doc/templates/fedora-minimal/
redirect_from:
- /doc/fedora-minimal/
- /en/doc/templates/fedora-minimal/
- /doc/Templates/FedoraMinimal/
- /wiki/Templates/FedoraMinimal/
---

Fedora - minimal
================

The template only weighs about 300 MB and has only the most vital packages installed, including a minimal X and xterm installation.
The minimal template, however, can be easily extended to fit your requirements. The sections below contain the instructions on duplicating the template and provide some examples for commonly desired use cases.

Installation
------------

The Fedora minimal template can be installed with the following command:

~~~
[user@dom0 ~]$ sudo qubes-dom0-update qubes-template-fedora-25-minimal
~~~

The download may take a while depending on your connection speed.

Duplication and first steps
---------------------------

It is higly recommended to clone the original template, and make any changes in the clone instead of the original template. The following command clones the template. Replace `your-new-clone` with your desired name.

~~~
[user@dom0 ~]$ qvm-clone fedora-25-minimal your-new-clone
~~~

You must start the template in order to customize it.
A recommended first step is to install the `sudo` package, which is not installed by default in the minimal template:

~~~
[user@your-new-clone ~]$ su -
[user@your-new-clone ~]$ dnf install sudo
~~~

Customization
-------------

Customizing the template for specific use cases normally only requires installing additional packages.
The following table provides an overview of which packages are needed for which purpose.

As expected, the required packages are to be installed in the running template with the following command. Replace "packages` with a space-delimited list of packages to be installed.

~~~
[user@your-new-clone ~]$ sudo dnf install packages
~~~

Use case | Description | Required steps
--- | --- | ---
**Standard utilities** | If you need the commonly used utilities | Install the following packages: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`
**FirewallVM** | You can use the minimal template as a [FirewallVM](/doc/firewall/), such as the basis template for `sys-firewall` | No extra packages are needed for the template to work as a firewall.
**NetVM** | You can use this template as the basis for a NetVM such as `sys-net` | Install the following packages: `NetworkManager` `NetworkManager-wifi` `network-manager-applet` `wireless-tools` `dbus-x11 dejavu-sans-fonts` `tinyproxy`  `notification-daemon` `gnome-keyring`.
**NetVM (extra firmware)** | If your network devices need extra packages for the template to work as a network VM | Use the `lspci` command to identify the devices, then run `dnf search firmware` (replace `firmware` with the appropriate device identifier) to find the needed packages and then install them.
**Network utilities** | If you need utilities for debugging and analyzing network connections | Install the following packages: `tcpdump` `telnet` `nmap` `nmap-ncat`
**USB** | If you want USB input forwarding to use this template as the basis for a [USB](/doc/usb/) qube such as `sys-usb` | Install `qubes-input-proxy-sender`
**VPN** | You can use this template as basis for a [VPN](/doc/vpn/) qube | Use the `dnf search "NetworkManager VPN plugin"` command to look up the VPN packages you need, based on the VPN technology you'll be using, and install them. GNOME related packages are needed as well in order to edit your VPN connections through the Network Applet. After creation of a machine based on this template, follow the [VPN howto](/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.
**3G Modems**| If you want to use this template as a NetVM using a 3G Modem connection| Install the following packages: `ModemManager` `NetworkManager-wwan` `usb_modeswitch`. Additionnally, `modem-manager-gui` can help troubleshooting your 3g modem [1].
**DVM Template** | If you want to use this VM as a [DVM Template](/doc/glossary/#dvm-template) | Install `perl-Encode`

Locales
--------
Several bugs can be encountered because locales for your language are not necessarily generated on the system.

Generating new locales on the template can help fixing such bugs.

First install the package `glibc-locale-source`

New locales can be generated using the following commands (as root). Change to the language you want (eg: fr_FR for french language):
`# localedef -v -c -i en_US -f UTF-8 en_US.UFT-8`

Logging
-------

The `rsyslog` logging service is not installed by default, as all logging is instead being handled by the `systemd` journal.
Users requiring the `rsyslog` service should install it manually.

To access the `journald` log, use the `journalctl` command.

GUI Tips and Tricks
---------

Installing GUI tools in a minimal template often ends with a bad user experiences as good fonts, icons or GTK/QT themes are missing.

This paragraph regroups tips and tricks to increase user friendlyness of GUI tools while using a minimal template.

### Tools ###

The following table shows example of tools that can be installed with minimum dependencies.

Use case | Description | Package
--- | --- | ---
**File manager** |  Thunar is xfce file manager and has limited xfce dependencies. It has support for automount, and shared folders. | `thunar` `thunar-volman` `ntfs-3g` `cifs-utils`
**Notepad** | Scite has limited dependencies but support indentiation and syntax highlighting | `scite`
**Terminal** | lxterminal has limited dependencie and support tabs | `lxterminal`
**Printing** | Cups and some configuration apples need to be installed to support printing (see notes below) | `system-config-printer` `system-config-printer-applet` `cups`

### Fonts ###

You need to install sans-mono fonts for terminals to be readable (to avoid overlapping characters....).

Sans fonts are also needed to get nicer GUI menus.

For example it is possible to install sans and mono variants of nice fonts such as bitstream-vera or dejavu fonts.
`dnf install bitstream-vera-sans-fonts bitstream-vera-sans-mono-fonts dejavu-sans-fonts dejavu-sans-mono-fonts`

### Printing ###

To tools above depends on python3 + python3 additionnal libraries which takes more than 40 M once installed. Cups also depends on ghostscript and require installing additionnal printing fonts (not documented here), so it can takes several dozen of MB.

1. If you want to instal a network printer inside a template, you first need to identify the printer IP address.
2. Once the printer is identified, open temporarily firewall access to the printer, as qubes firewall is filtering all outbound trafic by default in templates
3. Run system-config-printer GUI to install your printer
4/ Eventually, install printer drivers if the driver cannot be found automatically by search for driver packages `dnf search printername` eg: `dnf search photosmart`


References
----------
[1] https://www.codeenigma.com/community/blog/installing-3g-usb-modems-linux
