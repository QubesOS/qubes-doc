---
layout: doc
title: Fedora Minimal Template
permalink: /doc/templates/fedora-minimal/
redirect_from:
- /en/doc/templates/fedora-minimal/
- /doc/Templates/FedoraMinimal/
- /wiki/Templates/FedoraMinimal/
---

Fedora - minimal
================

We have uploaded a new "minimal" template to our templates-itl repo. The template weighs only 150MB and has most of the stuff cut off, except for minimal X and xterm.

More into in ticket \#828

Install
-------

It can be installed via the following command:

~~~
[user@dom0 ~]$ sudo qubes-dom0-update qubes-template-fedora-21-minimal
~~~

Download will take a while and there will be no progress indicator.

Usage
-----

It is a good idea to clone the original template, and make any changes in the new clone instead:

~~~
[user@dom0 ~]$ qvm-clone fedora-21-minimal <your new template name>
~~~

The sudo package is not installed by default, so let's install it:

~~~
[user@F21-Minimal ~]$ su -
[user@F21-Minimal ~]$ yum install sudo
~~~

The rsyslog logging service is not installed by default. All logging is now being handled by the systemd journal. Users requiring the rsyslog service should install it manually.

To access the journald log, use the `journalctl` command.

### as a NetVM

If you want to use this template to for standard NetVMs you should install some more packeges:

~~~
[user@F21-Minimal ~]$ sudo yum install NetworkManager NetworkManager-wifi network-manager-applet  wireless-tools dbus-x11 dejavu-sans-fonts tar tinyproxy
~~~

And maybe some more optional but useful packages as well:

~~~
[user@F21-Minimal ~]$ sudo yum install pciutils vim-minimal less tcpdump telnet psmisc nmap nmap-ncat gnome-keyring
~~~

If your network device needs some firmware then you should also install the corresponding packages as well. The `lspci; yum search firmware` command will help to choose the right one :)

### as a ProxyVM

If you want to use this template as a ProxyVM you may want to install even more packages

#### Firewall

This template is ready to use for a standard firewall VM.

#### VPN

The needed packages depend on the VPN technology. The `yum search "NetworkManager VPN plugin"` command may help you to choose the right one.

[More details about setting up a VPN Gateway](/wiki/VPN#ProxyVM)

#### TOR

[UserDoc/TorVM](/wiki/UserDoc/TorVM)
