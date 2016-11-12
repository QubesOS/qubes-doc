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

The template only weighs about 300 MB and has only the most vital packages installed, including a minimal X and xterm installation. It is not thought to be usable in its original form.
The minimal template, however, can be easily extended to fit your requirements. The sections below contain the instructions on duplicating the template and provide some examples for commonly desired use cases.

Installation
-------

The Fedora minimal template can be installed with the following command:

~~~
[user@dom0 ~]$ sudo qubes-dom0-update qubes-template-fedora-23-minimal
~~~

The download and installation process may take some time. 

Cloning the template
-----

It is higly recommended to clone the original template, and make any changes in the clone instead of the original template. The following command clones the template. Replace "your-new-clone" with your desired name.

~~~
[user@dom0 ~]$ qvm-clone fedora-23-minimal your-new-clone
~~~

First steps
-----

You must start the template machine in order to customize it.
A recommended first step is to install the `sudo` package, which is not installed by default in the minimal template:

~~~
[user@your-new-clone ~]$ su -
[user@your-new-clone ~]$ dnf install sudo
~~~

The rsyslog logging service is not installed by default. All logging is now being handled by the systemd journal. Users requiring the rsyslog service should install it manually.

To access the journald log, use the `journalctl` command.

### as a NetVM

If you want to use this template to for standard NetVMs you should install some more packeges:

~~~
[user@F21-Minimal ~]$ sudo dnf install NetworkManager NetworkManager-wifi network-manager-applet  wireless-tools dbus-x11 dejavu-sans-fonts tinyproxy
~~~

And maybe some more optional but useful packages as well:

~~~
[user@F21-Minimal ~]$ sudo dnf install pciutils vim-minimal less tcpdump telnet psmisc nmap nmap-ncat gnome-keyring
~~~

If your network device needs some firmware then you should also install the corresponding packages as well. The `lspci` and `dnf search firmware` command will help to choose the right one :)

### as a ProxyVM

If you want to use this template as a ProxyVM you may want to install even more packages

#### Firewall

This template is now ready to use for a standard firewall VM.

#### VPN

The needed packages depend on the VPN technology. The `dnf search "NetworkManager VPN plugin"` command may help you to choose the right one. You should also install the corresponding GNOME related packages as well.

[More details about setting up a VPN Gateway](/doc/vpn/#proxyvm)

#### TOR

[UserDoc/TorVM](/wiki/UserDoc/TorVM)
