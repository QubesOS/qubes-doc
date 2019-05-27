---
layout: doc
title: The Fedora Minimal TemplateVM
permalink: /doc/templates/fedora-minimal/
redirect_from:
- /doc/fedora-minimal/
- /en/doc/templates/fedora-minimal/
- /doc/Templates/FedoraMinimal/
- /wiki/Templates/FedoraMinimal/
---

The Fedora Minimal TemplateVM
=============================

The Fedora Minimal TemplateVM (`fedora-minimal`) only weighs about 600 MB compressed (1.6 GB on disk) and has only the most vital packages installed, including a minimal X and xterm installation.
The sections below contain instructions for using the template and provide some examples for common use cases.


Important
---------

1. The Fedora Minimal template is intended only for advanced users.
   If you encounter problems with the Fedora Minimal template, we recommend that you use the [default Fedora template] instead.

2. If something works with the default Fedora template but not the Fedora Minimal template, this is most likely due to user error (e.g., a missing package or misconfiguration) rather than a bug.
   In such cases, you should write to [qubes-users] to ask for help rather than filing a bug report, then [contribute what you learn to the documentation][doc-guidelines].

3. The Fedora Minimal template is intentionally *minimal*.
   [Do not ask for your favorite package to be added to the minimal template by default.][pref-default]


Installation
------------

The Fedora Minimal template can be installed with the following command (where `XX` is your desired version number):

~~~
[user@dom0 ~]$ sudo qubes-dom0-update qubes-template-fedora-XX-minimal
~~~

The download may take a while depending on your connection speed.


Customization
-------------

It is highly recommended to clone the original template and make any changes in the clone instead of the original template.
The following command clones the template.
Replace `XX` with your installed Fedora Minimal version number and `your-new-clone` with your desired clone name.

~~~
[user@dom0 ~]$ qvm-clone fedora-XX-minimal your-new-clone
~~~

You must start the clone in order to customize it.

Customizing the template for specific use cases normally only requires installing additional packages.
The following list provides an overview of which packages are needed for which purpose.
As usual, the required packages are to be installed in the running template with the following command (replace `packages` with a space-delimited list of packages to be installed):

~~~
[user@your-new-clone ~]$ sudo dnf install packages
~~~

 - Commonly used utilities: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`.
 - Audio: `pulseaudio-qubes`.
 - [FirewallVM](/doc/firewall/), such as the template for `sys-firewall`: at least `qubes-core-agent-networking` and `iproute`, and also `qubes-core-agent-dom0-updates` if you want to use it as the `UpdateVM` (which is normally `sys-firewall`).
 - NetVM, such as the template for `sys-net`: `qubes-core-agent-networking` `qubes-core-agent-network-manager` `NetworkManager-wifi` `network-manager-applet` `wireless-tools` `dejavu-sans-fonts` `notification-daemon` `gnome-keyring` `polkit` `@hardware-support`.
   If your network devices need extra packages for the template to work as a network VM, use the `lspci` command to identify the devices, then run `dnf search firmware` (replace `firmware` with the appropriate device identifier) to find the needed packages and then install them.
   If you need utilities for debugging and analyzing network connections, install `tcpdump` `telnet` `nmap` `nmap-ncat`.
 - [USB qube](/doc/usb-qubes/), such as the template for `sys-usb`: `qubes-input-proxy-sender`.
 - [VPN qube](/doc/vpn/): Use the `dnf search "NetworkManager VPN plugin"` command to look up the VPN packages you need, based on the VPN technology you'll be using, and install them.
   Some GNOME related packages may be needed as well.
   After creation of a machine based on this template, follow the [VPN instructions](/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.

You may also wish to consider additional packages from the `qubes-core-agent` suite:

 - `qubes-core-agent-qrexec`: Qubes qrexec agent. Installed by default.
 - `qubes-core-agent-systemd`: Qubes unit files for SystemD init style. Installed by default.
 - `qubes-core-agent-passwordless-root`, `polkit`: By default, the Fedora Minimal template doesn't have passwordless root. These two packages enable this feature.
 - `qubes-core-agent-nautilus`: This package provides integration with the Nautilus file manager (without it things like "copy to VM/open in disposable VM" will not be shown in Nautilus).
 - `qubes-core-agent-sysvinit`: Qubes unit files for SysV init style or upstart.
 - `qubes-core-agent-networking`: Networking support. Required for general network access and particularly if the template is to be used for a `sys-net` or `sys-firewall` VM.
 - `qubes-core-agent-network-manager`: Integration for NetworkManager. Useful if the template is to be used for a `sys-net` VM.
 - `network-manager-applet`: Useful (together with `dejavu-sans-fonts` and `notification-daemon`) to have a system tray icon if the template is to be used for a `sys-net` VM.
 - `qubes-core-agent-dom0-updates`: Script required to handle `dom0` updates. Any template which the VM responsible for 'dom0' updates (e.g. `sys-firewall`) is based on must contain this package.
 - `qubes-usb-proxy`: Required if the template is to be used for a USB qube (`sys-usb`) or for any destination qube to which USB devices are to be attached (e.g `sys-net` if using USB network adapter).
 - `pulseaudio-qubes`: Needed to have audio on the template VM.

See [here][customization] for further information on customizing `fedora-minimal`.


Passwordless root
-----------------

It is an intentional design choice for passwordless to be optional.
Since the Fedora Minimal template is *minimal*, it is not configured for passwordless root by default.
To update or install packages to it, from a dom0 terminal window:

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


Logging
-------

The `rsyslog` logging service is not installed by default, as all logging is instead being handled by the `systemd` journal.
Users requiring the `rsyslog` service should install it manually.

To access the `journald` log, use the `journalctl` command.


[default Fedora template]: /doc/templates/fedora/
[qubes-users]: /support/#qubes-users
[doc-guidelines]: /doc/doc-guidelines/
[pref-default]: /faq/#could-you-please-make-my-preference-the-default
[customization]: /doc/fedora-minimal-template-customization/

