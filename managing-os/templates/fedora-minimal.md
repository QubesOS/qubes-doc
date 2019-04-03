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

The template only weighs about 600 MB compressed (1.6 GB on disk) and has only the most vital packages installed, including a minimal X and xterm installation.
The minimal template, however, can be easily extended to fit your requirements.
The sections below contain the instructions on duplicating the template and provide some examples for commonly desired use cases.

Important
---------

1. The Fedora minimal template is intended only for advanced users.
   If you encounter problems with the Fedora minimal template, we recommend that you use the [default Fedora template] instead.

2. If something works with the default Fedora template but not the minimal template, this is most likely due to user error (e.g., a missing package or misconfiguration) rather than a bug.
   In such cases, you should write to [qubes-users] to ask for help rather than filing a bug report, then [contribute what you learn to the documentation][doc-guidelines].

3. The Fedora minimal template is intentionally *minimal*.
   [Do not ask for your favorite package to be added to the minimal template by default.][pref-default]

Installation
------------

The Fedora minimal template can be installed with the following command:

~~~
[user@dom0 ~]$ sudo qubes-dom0-update qubes-template-fedora-29-minimal
~~~

The download may take a while depending on your connection speed.

Duplication and first steps
---------------------------

It is highly recommended to clone the original template, and make any changes in the clone instead of the original template. The following command clones the template. Replace `your-new-clone` with your desired name.

~~~
[user@dom0 ~]$ qvm-clone fedora-29-minimal your-new-clone
~~~

You must start the template in order to customize it.

Customization
-------------

Customizing the template for specific use cases normally only requires installing additional packages.
The following table provides an overview of which packages are needed for which purpose.

As expected, the required packages are to be installed in the running template with the following command. Replace "packages` with a space-delimited list of packages to be installed.

~~~
[user@your-new-clone ~]$ sudo dnf install packages
~~~

### Package table for Qubes 3.2

Use case | Description | Required steps
--- | --- | ---
**Standard utilities** | If you need the commonly used utilities | Install the following packages: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`
**FirewallVM** | You can use the minimal template as a [FirewallVM](/doc/firewall/), such as the basis template for `sys-firewall` | No extra packages are needed for the template to work as a firewall.
**NetVM** | You can use this template as the basis for a NetVM such as `sys-net` | Install the following packages:  `NetworkManager-wifi` `wireless-tools` `dejavu-sans-fonts` `notification-daemon`.
**NetVM (extra firmware)** | If your network devices need extra packages for the template to work as a network VM | Use the `lspci` command to identify the devices, then run `dnf search firmware` (replace `firmware` with the appropriate device identifier) to find the needed packages and then install them.
**Network utilities** | If you need utilities for debugging and analyzing network connections | Install the following packages: `tcpdump` `telnet` `nmap` `nmap-ncat`
**USB** | If you want USB input forwarding to use this template as the basis for a [USB](/doc/usb/) qube such as `sys-usb` | Install `qubes-input-proxy-sender`
**VPN** | You can use this template as basis for a [VPN](/doc/vpn/) qube | Use the `dnf search "NetworkManager VPN plugin"` command to look up the VPN packages you need, based on the VPN technology you'll be using, and install them. Some GNOME related packages may be needed as well. After creation of a machine based on this template, follow the [VPN howto](/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.
**DisposableVM Template** | If you want to use this VM as a [DisposableVM Template](/doc/glossary/#disposablevm-template) | Install `perl-Encode`

### Package table for Qubes 4.0

Use case | Description | Required steps
--- | --- | ---
**Standard utilities** | If you need the commonly used utilities | Install the following packages: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`
**Audio** | If you want sound from your VM | Install `pulseaudio-qubes`
**FirewallVM** | You can use the minimal template as a [FirewallVM](/doc/firewall/), such as the basis template for `sys-firewall` | Install at least `qubes-core-agent-networking` and `iproute`, and also `qubes-core-agent-dom0-updates` if you want to use it as the updatevm (which is normally sys-firewall).
**NetVM** | You can use this template as the basis for a NetVM such as `sys-net` | Install the following packages:  `qubes-core-agent-networking` `qubes-core-agent-network-manager` `NetworkManager-wifi` `network-manager-applet` `wireless-tools` `dejavu-sans-fonts` `notification-daemon` `gnome-keyring` `polkit` `@hardware-support`.
**NetVM (extra firmware)** | If your network devices need extra packages for the template to work as a network VM | Use the `lspci` command to identify the devices, then run `dnf search firmware` (replace `firmware` with the appropriate device identifier) to find the needed packages and then install them.
**Network utilities** | If you need utilities for debugging and analyzing network connections | Install the following packages: `tcpdump` `telnet` `nmap` `nmap-ncat`
**USB** | If you want USB input forwarding to use this template as the basis for a [USB](/doc/usb/) qube such as `sys-usb` | Install `qubes-input-proxy-sender`
**VPN** | You can use this template as basis for a [VPN](/doc/vpn/) qube | Use the `dnf search "NetworkManager VPN plugin"` command to look up the VPN packages you need, based on the VPN technology you'll be using, and install them. Some GNOME related packages may be needed as well. After creation of a machine based on this template, follow the [VPN howto](/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.
 
A comprehensive guide to customizing the minimal template is available [here][GUIDE]


Qubes 4.0
---------

In Qubes R4.0 the minimal template is not configured for passwordless root.  To update or install packages to it, from a dom0 terminal window:

~~~
[user@dom0 ~]$ qvm-run -u root fedora-29-minimal xterm
~~~
to open a root terminal in the template, from which you can use dnf without sudo. You will have to do this every time if you choose not to enable passwordless root. 

If you want the usual qubes `sudo dnf ...` commands, open the root terminal just this once using the above command, and in the root xterm window enter

~~~
bash-4.4# dnf install qubes-core-agent-passwordless-root polkit
~~~

Optionally check this worked: from the gui open the minimal template's xterm and give the command

~~~
[user@fed-min-clone ~]$ sudo -l
~~~

which should give you output that includes the NOPASSWD keyword.


In Qubes 4.0, additional packages from the `qubes-core-agent` suite may be needed to make the customized minimal template work properly. These packages are:

- `qubes-core-agent-qrexec`: Qubes qrexec agent. Installed by default.
- `qubes-core-agent-systemd`: Qubes unit files for SystemD init style. Installed by default.
- `qubes-core-agent-passwordless-root`, `polkit`: By default the 'fedora-29-minimal' template doesn't have passwordless root. These two packages enable this feature. (Note from R4.0 a design choice was made that passwordless should be optional, so is left out of the minimal templates)
- `qubes-core-agent-nautilus`: This package provides integration with the Nautilus file manager (without it things like "copy to VM/open in disposable VM" will not be shown in Nautilus).
- `qubes-core-agent-sysvinit`: Qubes unit files for SysV init style or upstart.
- `qubes-core-agent-networking`: Networking support. Required for general network access and particularly if the template is to be used for a `sys-net` or `sys-firewall` VM.
- `qubes-core-agent-network-manager`: Integration for NetworkManager. Useful if the template is to be used for a `sys-net` VM.
- `network-manager-applet`: Useful (together with `dejavu-sans-fonts` and `notification-daemon`) to have a system tray icon if the template is to be used for a `sys-net` VM.
- `qubes-core-agent-dom0-updates`: Script required to handle `dom0` updates. Any template which the VM responsible for 'dom0' updates (e.g. `sys-firewall`) is based on must contain this package.
- `qubes-usb-proxy`: Required if the template is to be used for a USB qube (`sys-usb`) or for any destination qube to which USB devices are to be attached (e.g `sys-net` if using USB network adapter).
- `pulseaudio-qubes`: Needed to have audio on the template VM.


Logging
-------

The `rsyslog` logging service is not installed by default, as all logging is instead being handled by the `systemd` journal.
Users requiring the `rsyslog` service should install it manually.

To access the `journald` log, use the `journalctl` command.


[default Fedora template]: /doc/templates/fedora/
[qubes-users]: /support/#qubes-users
[doc-guidelines]: /doc/doc-guidelines/
[pref-default]: /faq/#could-you-please-make-my-preference-the-default
[GUIDE]: /doc/fedora-minimal-template-customization/

