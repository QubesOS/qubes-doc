---
layout: wiki
title: FedoraMinimal
permalink: /wiki/Templates/FedoraMinimal/
---

Fedora - minimal
================

We have uploaded a new "minimal" template to our templates-itl repo. The template weighs only 150MB and has most of the stuff cut off, except for minimal X and xterm.

More into in ticket \#828

Install
-------

It can be installed via the following command:

``` {.wiki}
[user@dom0 ~]$ sudo qubes-dom0-update qubes-template-fedora-20-x64-minimal
```

Usage
-----

It is a good idea to clone the original template, and make any changes in the new clone instead:

``` {.wiki}
[user@dom0 ~]$ qvm-clone fedora-20-x64-minimal <your new template name>
```

Not even the sudo package is installed by default, so lets install it:

``` {.wiki}
[user@F20-Minimal ~]$ su - 
[user@F20-Minimal ~]$ yum install sudo
```

### NetVM

If You want to use this template to for standard NetVMs You should install some more packeges:

``` {.wiki}
[user@F20-Minimal ~]$ sudo yum install NetworkManager network-manager-applet  wireless-tools dbus-x11 dejavu-sans-fonts tar tinyproxy
```

And maybe some more optional but useful packages as well:

``` {.wiki}
[user@F20-Minimal ~]$ sudo yum install pci-tools vim-minimal less tcpdump
```

If Your network device needs some firmware then you should also install the correspondong packages as well. The `lspci; yum search firmware` command will help to choose the right one :)

### ProxyVM

FIXME
