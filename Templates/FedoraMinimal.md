---
layout: doc
title: FedoraMinimal
permalink: /doc/Templates/FedoraMinimal/
redirect_from: /wiki/Templates/FedoraMinimal/
---

Fedora - minimal
================

We have uploaded a new "minimal" template to our templates-itl repo. The template weighs only 150MB and has most of the stuff cut off, except for minimal X and xterm.

More into in ticket \#828

Install
-------

It can be installed via the following command:

{% highlight trac-wiki %}
[user@dom0 ~]$ sudo qubes-dom0-update qubes-template-fedora-21-minimal
{% endhighlight %}

Usage
-----

It is a good idea to clone the original template, and make any changes in the new clone instead:

{% highlight trac-wiki %}
[user@dom0 ~]$ qvm-clone fedora-21-minimal <your new template name>
{% endhighlight %}

The sudo package is not installed by default, so let's install it:

{% highlight trac-wiki %}
[user@F21-Minimal ~]$ su - 
[user@F21-Minimal ~]$ yum install sudo
{% endhighlight %}

The rsyslog logging service is not installed by default. All logging is now being handled by the systemd journal. Users requiring the rsyslog service should install it manually.

To access the journald log, use the `journalctl` command.

### as a NetVM

If you want to use this template to for standard NetVMs you should install some more packeges:

{% highlight trac-wiki %}
[user@F21-Minimal ~]$ sudo yum install NetworkManager NetworkManager-wifi network-manager-applet  wireless-tools dbus-x11 dejavu-sans-fonts tar tinyproxy
{% endhighlight %}

And maybe some more optional but useful packages as well:

{% highlight trac-wiki %}
[user@F21-Minimal ~]$ sudo yum install pciutils vim-minimal less tcpdump telnet psmisc nmap nmap-ncat gnome-keyring
{% endhighlight %}

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
