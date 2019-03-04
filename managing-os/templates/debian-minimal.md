---
layout: doc
title: Debian Minimal Template
permalink: /doc/templates/debian-minimal/
---

Debian - minimal
================

The template weighs about 200 MB compressed (0.75 GB on disk) and has only the most vital packages installed, including a minimal X and xterm installation.
The minimal template, however, can be easily extended to fit your requirements.
The sections below contain instructions on cloning the template and provide some examples for commonly desired use cases.

Note that use of the minimal template requires some familiarity with the command line and basics of Qubes.

Installation
------------

The Debian minimal template can be installed with the following command:

~~~
[user@dom0 ~]$ sudo qubes-dom0-update --enable-repo qubes-templates-itl-testing qubes-template-debian-9-minimal
~~~

The download may take a while depending on your connection speed.

Duplication and first steps
---------------------------

It is highly recommended that you clone the original template, and make any changes in the clone instead of the original template. 
The following command clones the template. 
(Replace `your-new-clone` with your desired name.)

~~~
[user@dom0 ~]$ qvm-clone debian-9-minimal your-new-clone
~~~

You must start the template in order to customize it.

Customization
-------------

Customizing the template for specific use cases normally only requires installing additional packages.
The following table provides an overview of which packages are needed for which purpose.

As you would expect, the required packages can be installed in the running template with any apt-based command. 
For example : (Replace "packages` with a space-delimited list of packages to be installed.)

~~~
[user@your-new-clone ~]$ sudo apt install packages
~~~

Qubes 4.0
---------

In Qubes R4.0 the minimal template is not configured for passwordless root.  
To update or install packages to it, from a dom0 terminal window run:

~~~
[user@dom0 ~]$ qvm-run -u root debian-9-minimal xterm
~~~
to open a root terminal in the template, from which you can use apt tools without sudo. 
You will have to do this every time you want root access if you choose not to enable passwordless root. 

If you want the usual qubes `sudo ...` commands, open the root terminal using the above command, and in the root xterm window enter

~~~
bash-4.4# apt install qubes-core-agent-passwordless-root polkit
~~~

Optionally check this worked: from the gui open the minimal template's xterm and give the command:

~~~
[user@debian-9-minimal ~]$ sudo -l
~~~

which should give you output that includes the NOPASSWD keyword.

### Package table for Qubes 4.0

Use case | Description | Required steps
--- | --- | ---
**Standard utilities** | If you need the commonly used utilities | Install the following packages: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`
**Networking** | If you want networking | Install qubes-core-agent-networking
**Audio** | If you want sound from your VM... | Install `pulseaudio-qubes`
**FirewallVM** | You can use the minimal template as a template for a [FirewallVM](/doc/firewall/), like `sys-firewall` | Install `qubes-core-agent-networking`, and `nftables`.  Also install `qubes-core-agent-dom0-updates` if you want to use a qube based on the template as an updateVM (normally sys-firewall).
**NetVM** | You can use this template as the basis for a NetVM such as `sys-net` | Install the following packages:  `qubes-core-agent-networking`, `qubes-core-agent-network-manager`, and `nftables`.  
**NetVM (extra firmware)** | If your network devices need extra packages for a network VM | Use the `lspci` command to identify the devices, then find the package that provides necessary firnware and install it.
**Network utilities** | If you need utilities for debugging and analyzing network connections | Install the following packages: `tcpdump` `telnet` `nmap` `nmap-ncat`
**USB** | If you want to use this template as the basis for a [USB](/doc/usb/) qube such as `sys-usb` | Install `qubes-usb-proxy`. To use USB mouse or keyboard install `qubes-input-proxy-sender`.
**VPN** | You can use this template as basis for a [VPN](/doc/vpn/) qube | You may need to install network-manager VPN packages, depending on the VPN technology you'll be using. After creating a machine based on this template, follow the [VPN howto](/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.
 

In Qubes 4.0, additional packages from the `qubes-core-agent` suite may be needed to make the customized minimal template work properly. 
These packages are:

- `qubes-core-agent-nautilus`: This package provides integration with the Nautilus file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in Nautilus).
- `qubes-core-agent-thunar`: This package provides integration with the thunar file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in thunar).
- `qubes-core-agent-dom0-updates`: Script required to handle `dom0` updates. Any template on which the qube responsible for 'dom0' updates (e.g. `sys-firewall`) is based must contain this package.
- `qubes-menus`: Defines menu layout.
- `qubes-desktop-linux-common`: Contains icons and scripts to improve desktop experience.

Also, there are packages to provide additional services:
- `qubes-gpg-split`: For implementing split GPG.
- `qubes-u2f`: For implementing secure forwarding of U2F messages.
- `qubes-pdf-converter`: For implementing safe conversion of PDFs.
- `qubes-image-converter`: For implementing safe conversion of images.
- `qubes-snapd-helper`: If you want to use snaps in qubes.
- `qubes-thunderbird`: Additional tools for use in thunderbird.
- `qubes-app-shutdown-idle`: If you want qubes to automatically shutdown when idle.
- `qubes-mgmt-\*`: If you want to use salt management on the template and qubes.

Documentation on all of these can be found in the [docs](/doc)

You could, of course, use qubes-vm-recommended to automatically install many of these, but in that case you are well on the way to a standard Debian template.
