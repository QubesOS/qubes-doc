---
layout: doc
title: CentOS Template
permalink: /doc/templates/centos-minimal/
---

# CentOS Minimal Template

The minimal CentOS images use the standard CentOS installer with all of its regular features minus the selection of packages, thus keeping only the most essential ones, including the xterm terminal emulator. Yum is completed and can be used to add or remove packages, right after the Template installation.

The CentOS Minimal template is intended only for advanced users and requires some familiarity with the command line and basics of Qubes.

## Installation

The CentOS-7 Minimal Template can be installed with the following command:

    [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community-testing qubes-template-centos-7-minimal

To switch, reinstall and uninstall a CentOS TemplateVM that is already installed in your system, see  [How to switch, reinstall and uninstall](/doc/templates/#how-to-install-uninstall-reinstall-and-switch).

Customization
---------------------------

### Clone

It is highly recommended not to make any changes in the original template, but use a **clone** instead. The following command clones the template. (Replace your-new-clone with your desired name.)

~~~
[user@dom0 ~]$ qvm-clone centos-7-minimal your-new-clone
~~~

You must start the template in order to customize it.

**Customizing** the template for specific use cases normally requires installing additional packages. In the running template, use yum to install the required packages as follows(replace packages with a space-delimited list of packages to be installed):

~~~
[user@your-new-clone ~]$ sudo yum install packages
~~~

### Passwordless root

Before starting to install packages in your template, it is worthy of mention that in Qubes R4.0, the minimal template is not configured for passwordless root.
To update or install packages to it, from a dom0 terminal window run:

~~~
[user@dom0 ~]$ qvm-run -u root centos-7-minimal xterm
~~~

to open a root terminal in the template, from which you can use yum without sudo. You will have to do this every time if you choose not to enable passwordless root. 

If you want the usual CentoOS qubes `sudo yum ...` commands, open the root terminal just this once using the above command, and in the root xterm window enter

~~~
bash-4.4# yum install qubes-core-agent-passwordless-root polkit
~~~

Optionally check this worked: from the gui open the minimal template's xterm and give the command

~~~
[user@cent-min-clone ~]$ sudo -l
~~~

which should give you output that includes the NOPASSWD keyword.

From this point, your template is ready to be customized.

### Packages

The following table provides an overview of which packages are needed for which purpose.

Use case | Description | Required steps
--- | --- | ---
**Standard utilities** | If you need the commonly used utilities | Install the following packages: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`
**Networking** | If you want networking | Install qubes-core-agent-networking
**Audio** | If you want sound from your VM... | Install `pulseaudio-qubes`
**FirewallVM** | You can use the minimal template as a template for a [FirewallVM](/doc/firewall/), like `sys-firewall` | Install `qubes-core-agent-networking`, and `nftables`.  Also install `qubes-core-agent-dom0-updates`(script required to handle `dom0` updates), if you want to use a qube based on the template as an updateVM (normally sys-firewall).
**NetVM** | You can use this template as the basis for a NetVM such as `sys-net` | Install the following packages:  `qubes-core-agent-networking`, `qubes-core-agent-network-manager`, and `nftables`.
**NetVM (extra firmware)** | If your network devices need extra packages for a network VM | Use the `lspci` command to identify the devices, then find the package that provides necessary firnware and install it.
**Network utilities** | If you need utilities for debugging and analyzing network connections | Install the following packages: `tcpdump` `telnet` `nmap` `nmap-ncat`
**USB** | If you want to use this template as the basis for a [USB](/doc/usb/) qube such as `sys-usb` | Install `qubes-usb-proxy`. To use USB mouse or keyboard install `qubes-input-proxy-sender`.
**VPN** | You can use this template as basis for a [VPN](/doc/vpn/) qube | You may need to install network-manager VPN packages, depending on the VPN technology you'll be using. After creating a machine based on this template, follow the [VPN howto](/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.
**Desktop environment** | To improve desktop experience using additional packages from the `qubes-core-agent` | `qubes-menus `which defines menu layout, `qubes-desktop-linux-common` which contains icons and scripts to improve desktop experience. `qubes-core-agent-nautilus`/`qubes-core-agent-thunar`: packages providing integration with the Nautilus/Thunar file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in Nautilus/Thunar).

Also, there are packages to provide additional services:
- `qubes-gpg-split`: For implementing split GPG.
- `qubes-u2f`: For implementing secure forwarding of U2F messages.
- `qubes-pdf-converter`: For implementing safe conversion of PDFs.
- `qubes-img-converter`: For implementing safe conversion of images.
- `qubes-snapd-helper`: If you want to use snaps in qubes.
- `qubes-thunderbird`: Additional tools for use in thunderbird.
- `qubes-app-shutdown-idle`: If you want qubes to automatically shutdown when idle.
- `qubes-mgmt-\*`: If you want to use salt management on the template and qubes.

## Want to contribute?

*   [How can I contribute to the Qubes Project?](/doc/contributing/)

*   [Guidelines for Documentation Contributors](/doc/doc-guidelines/)
