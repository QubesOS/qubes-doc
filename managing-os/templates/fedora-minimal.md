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

The template only weighs about 2.3 GB and has only the most vital packages installed, including a minimal X and xterm installation.
The minimal template, however, can be easily extended to fit your requirements. The sections below contain the instructions on duplicating the template and provide some examples for commonly desired use cases.

Installation
------------

The Fedora minimal template can be installed with the following command:

~~~
[user@dom0 ~]$ sudo qubes-dom0-update qubes-template-fedora-26-minimal
~~~

The download may take a while depending on your connection speed.

Duplication and first steps
---------------------------

It is higly recommended to clone the original template, and make any changes in the clone instead of the original template. The following command clones the template. Replace `your-new-clone` with your desired name.

~~~
[user@dom0 ~]$ qvm-clone fedora-26-minimal your-new-clone
~~~

You must start the template in order to customize it.

For Qubes R4.0, sudo is not installed by default in the minimal template.  To update or install packages, from a dom0 terminal window:

~~~
[user@dom0 ~]$ qvm-run -u root fedora-26-minimal xterm
~~~

If you would like to skip this step in future, please install the `sudo` package:

~~~
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
**NetVM** | You can use this template as the basis for a NetVM such as `sys-net` | Install the following packages:  `NetworkManager-wifi` `wireless-tools` `dejavu-sans-fonts` `notification-daemon`.
**NetVM (extra firmware)** | If your network devices need extra packages for the template to work as a network VM | Use the `lspci` command to identify the devices, then run `dnf search firmware` (replace `firmware` with the appropriate device identifier) to find the needed packages and then install them.
**Network utilities** | If you need utilities for debugging and analyzing network connections | Install the following packages: `tcpdump` `telnet` `nmap` `nmap-ncat`
**USB** | If you want USB input forwarding to use this template as the basis for a [USB](/doc/usb/) qube such as `sys-usb` | Install `qubes-input-proxy-sender`
**VPN** | You can use this template as basis for a [VPN](/doc/vpn/) qube | Use the `dnf search "NetworkManager VPN plugin"` command to look up the VPN packages you need, based on the VPN technology you'll be using, and install them. Some GNOME related packages may be needed as well. After creation of a machine based on this template, follow the [VPN howto](/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.
**DVM Template** | If you want to use this VM as a [DVM Template](/doc/glossary/#dvm-template) | Install `perl-Encode`
  
  

A comprehensive guide to customizing the minimal template is available [here][GUIDE]

Logging
-------

The `rsyslog` logging service is not installed by default, as all logging is instead being handled by the `systemd` journal.
Users requiring the `rsyslog` service should install it manually.

To access the `journald` log, use the `journalctl` command.

[GUIDE]: /doc/fedora-minimal-template-customization/
