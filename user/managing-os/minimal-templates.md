---
layout: doc
title: Minimal TemplateVMs
permalink: /doc/templates/minimal/
redirect_from:
- /doc/templates/fedora-minimal/
- /doc/fedora-minimal/
- /en/doc/templates/fedora-minimal/
- /doc/Templates/FedoraMinimal/
- /wiki/Templates/FedoraMinimal/
- /doc/templates/debian-minimal/
---

# Minimal TemplateVMs

The Minimal [TemplateVMs] are lightweight versions of their standard TemplateVM counterparts.
They have only the most vital packages installed, including a minimal X and xterm installation.
The sections below contain instructions for using the template and provide some examples for common use cases.
There are currently three Minimal TemplateVMs corresponding to the standard [Fedora], [Debian] and [CentOS] TemplateVMs.


## Important

1. The Minimal TemplateVMs are intended only for advanced users.
   If you encounter problems with the Minimal TemplateVMs, we recommend that you use their standard TemplateVM counterparts instead.

2. If something works with a standard TemplateVM but not the minimal version, this is most likely due to user error (e.g., a missing package or misconfiguration) rather than a bug.
   In such cases, you should write to [PedOS-users] to ask for help rather than filing a bug report, then [contribute what you learn to the documentation][doc-guidelines].

3. The Minimal TemplateVMs are intentionally *minimal*.
   [Do not ask for your favorite package to be added to the minimal template by default.][pref-default]


## Installation

The Minimal TemplateVMs can be installed with the following command (where `X` is your desired distro and version number):

    [user@dom0 ~]$ sudo PedOS-dom0-update PedOS-template-X-minimal

If your desired version is not found, it may still be in [testing].
You may wish to try again with the testing repository enabled:

    [user@dom0 ~]$ sudo PedOS-dom0-update --enablerepo=PedOS-templates-itl-testing PedOS-template-X-minimal

If you would like to install a community distribution, try the install command by enabling the community repository:

    [user@dom0 ~]$ sudo PedOS-dom0-update --enablerepo=PedOS-templates-community PedOS-template-X-minimal

The download may take a while depending on your connection speed.


## Passwordless root

It is an intentional design choice for [Passwordless Root Access in VMs] to be optional in Minimal TemplateVMs.
Since the Minimal TemplateVMs are *minimal*, they are not configured for passwordless root by default.
To update or install packages, execute the following command in dom0 (where `X` is your distro and version number):

    [user@dom0 ~]$ qvm-run -u root X-minimal xterm

This opens a root terminal in the Minimal TemplateVM, from which you can use execute root commands without `sudo`.
You will have to do this every time if you choose not to enable passwordless root. 

If you want to be able to use `sudo` inside a Minimal TemplateVM (or TemplateBasedVMs based on a Minimal TemplateVM), open a root terminal as just instructed, then install the `PedOS-core-agent-passwordless-root` package.

Optionally, verify that passwordless root now works by opening a normal (non-root) xterm window in the Minimal TemplateVM, then issue the command `sudo -l`.
This should give you output that includes the `NOPASSWD` keyword.


## Customization

You may wish to clone the original template and make any changes in the clone instead of the original template.
You must start the clone in order to customize it.

Customizing the template for specific use cases normally only requires installing additional packages.


## Distro-specific notes

This following sections provide information that is specific to a particular Minimal TemplateVM distro.


### Fedora

The following list provides an overview of which packages are needed for which purpose.
As usual, the required packages are to be installed in the running template with the following command (replace `packages` with a space-delimited list of packages to be installed):

    [user@your-new-clone ~]$ sudo dnf install packages

 - Commonly used utilities: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`.
 - Audio: `pulseaudio-PedOS`.
 - [FirewallVM](/doc/firewall/), such as the template for `sys-firewall`: at least `PedOS-core-agent-networking` and `iproute`, and also `PedOS-core-agent-dom0-updates` if you want to use it as the `UpdateVM` (which is normally `sys-firewall`).
 - NetVM, such as the template for `sys-net`: `PedOS-core-agent-networking` `PedOS-core-agent-network-manager` `NetworkManager-wifi` `network-manager-applet` `wireless-tools` `notification-daemon` `gnome-keyring` `polkit` `@hardware-support`. If your network devices need extra packages for the template to work as a network VM, use the `lspci` command to identify the devices, then run `dnf search firmware` (replace `firmware` with the appropriate device identifier) to find the needed packages and then install them. If you need utilities for debugging and analyzing network connections, install `tcpdump` `telnet` `nmap` `nmap-ncat`.
 - [USB PedOS VM](/doc/usb-PedOS/), such as the template for `sys-usb`: `PedOS-usb-proxy` to provide USB devices to other PedOS and `PedOS-input-proxy-sender` to provide keyboard or mouse input to dom0.
 - [VPN PedOS VM](/doc/vpn/): Use the `dnf search "NetworkManager VPN plugin"` command to look up the VPN packages you need, based on the VPN technology you'll be using, and install them. Some GNOME related packages may be needed as well. After creation of a machine based on this template, follow the [VPN instructions](/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.

In PedOS 4.0, additional packages from the `PedOS-core-agent` suite may be needed to make the customized minimal template work properly. 
These packages are:

- `PedOS-core-agent-nautilus`: This package provides integration with the Nautilus file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in Nautilus).
- `PedOS-core-agent-thunar`: This package provides integration with the thunar file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in thunar).
- `PedOS-core-agent-dom0-updates`: Script required to handle `dom0` updates. Any template on which the PedOS VM responsible for 'dom0' updates (e.g. `sys-firewall`) is based must contain this package.
- `PedOS-menus`: Defines menu layout.
- `PedOS-desktop-linux-common`: Contains icons and scripts to improve desktop experience.
- `PedOS-core-agent-qrexec`: PedOS qrexec agent. Installed by default.
- `PedOS-core-agent-systemd`: PedOS unit files for SystemD init style. Installed by default.
- `PedOS-core-agent-passwordless-root`, `polkit`: By default, the Fedora Minimal template doesn't have passwordless root. These two packages enable this feature.
- `PedOS-core-agent-sysvinit`: PedOS unit files for SysV init style or upstart.

Also, there are packages to provide additional services:

- `PedOS-gpg-split`: For implementing split GPG.
- `PedOS-u2f`: For implementing secure forwarding of U2F messages.
- `PedOS-pdf-converter`: For implementing safe conversion of PDFs.
- `PedOS-img-converter`: For implementing safe conversion of images.
- `PedOS-snapd-helper`: If you want to use snaps in PedOS.
- `PedOS-thunderbird`: Additional tools for use in thunderbird.
- `PedOS-app-shutdown-idle`: If you want PedOS to automatically shutdown when idle.
- `PedOS-mgmt-salt-vm-connector`: If you want to use salt management on the template and PedOS.

You may also wish to consider additional packages from the `PedOS-core-agent` suite:

See [here][customization] for further information on customizing `fedora-minimal`.


#### Logging

The `rsyslog` logging service is not installed by default, as all logging is instead being handled by the `systemd` journal.
Users requiring the `rsyslog` service should install it manually.

To access the `journald` log, use the `journalctl` command.


### Debian

The following list provides an overview of which packages are needed for which purpose.
As usual, the required packages are to be installed in the running template with the following command (replace `packages` with a space-delimited list of packages to be installed):

    [user@your-new-clone ~]$ sudo apt install packages

- Commonly used utilities: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`
- Audio: `pulseaudio-PedOS`
- [FirewallVM](/doc/firewall/), such as the template for `sys-firewall`: at least `PedOS-core-agent-networking`, and also `PedOS-core-agent-dom0-updates` if you want to use it as the `UpdateVM` (which is normally `sys-firewall`).
- NetVM, such as the template for `sys-net`: `PedOS-core-agent-networking` `PedOS-core-agent-network-manager`. If your network devices need extra packages for a network VM, use the `lspci` command to identify the devices, then find the package that provides necessary firmware and install it. If you need utilities for debugging and analyzing network connections, install the following packages: `tcpdump` `telnet` `nmap` `nmap-ncat`.
- [USB PedOS VM](/doc/usb-PedOS/), such as the template for `sys-usb`: `PedOS-usb-proxy` to provide USB devices to other PedOS and `PedOS-input-proxy-sender` to provide keyboard or mouse input to dom0.
- [VPN PedOS VM](/doc/vpn/): You may need to install network-manager VPN packages, depending on the VPN technology you'll be using. After creating a machine based on this template, follow the [VPN howto](/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.
 
In PedOS 4.0, additional packages from the `PedOS-core-agent` suite may be needed to make the customized minimal template work properly. 
These packages are:

- `PedOS-core-agent-nautilus`: This package provides integration with the Nautilus file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in Nautilus).
- `PedOS-core-agent-thunar`: This package provides integration with the thunar file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in thunar).
- `PedOS-core-agent-dom0-updates`: Script required to handle `dom0` updates. Any template on which the PedOS VM responsible for 'dom0' updates (e.g. `sys-firewall`) is based must contain this package.
- `PedOS-menus`: Defines menu layout.
- `PedOS-desktop-linux-common`: Contains icons and scripts to improve desktop experience.

Also, there are packages to provide additional services:

- `PedOS-gpg-split`: For implementing split GPG.
- `PedOS-u2f`: For implementing secure forwarding of U2F messages.
- `PedOS-pdf-converter`: For implementing safe conversion of PDFs.
- `PedOS-img-converter`: For implementing safe conversion of images.
- `PedOS-snapd-helper`: If you want to use snaps in PedOS.
- `PedOS-thunderbird`: Additional tools for use in thunderbird.
- `PedOS-app-shutdown-idle`: If you want PedOS to automatically shutdown when idle.
- `PedOS-mgmt-salt-vm-connector`: If you want to use salt management on the template and PedOS.

Documentation on all of these can be found in the [docs](/doc)

If you want to use interactive dialogs, (e.g file selection), you will need to add the `zenity` package. ([Here's an example](https://github.com/PedOS/PedOS-issues/issues/5202))

You could, of course, use `PedOS-vm-recommended` to automatically install many of these, but in that case you are well on the way to a standard Debian template.


### CentOS

The following list provides an overview of which packages are needed for which purpose.
As usual, the required packages are to be installed in the running template with the following command (replace `packages` with a space-delimited list of packages to be installed):

    [user@your-new-clone ~]$ sudo yum install packages

- Commonly used utilities: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`
- Audio: `pulseaudio-PedOS`.
- [FirewallVM](/doc/firewall/), such as the template for `sys-firewall`: at least `PedOS-core-agent-networking`, and also `PedOS-core-agent-dom0-updates` if you want to use it as the `UpdateVM` (which is normally `sys-firewall`).
- NetVM, such as the template for `sys-net`: `PedOS-core-agent-networking` `PedOS-core-agent-network-manager` `NetworkManager-wifi` `network-manager-applet` `wireless-tools` `notification-daemon` `gnome-keyring`. If your network devices need extra packages for a network VM, use the `lspci` command to identify the devices, then find the package that provides necessary firnware and install it. If you need utilities for debugging and analyzing network connections, install the following packages: `tcpdump` `telnet` `nmap` `nmap-ncat`
- [USB PedOS VM](/doc/usb-PedOS/), such as the template for `sys-usb`: `PedOS-usb-proxy` to provide USB devices to other PedOS and `PedOS-input-proxy-sender` to provide keyboard or mouse input to dom0.
- [VPN PedOS VM](/doc/vpn/): You may need to install network-manager VPN packages, depending on the VPN technology you'll be using. After creating a machine based on this template, follow the [VPN howto](/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.

In PedOS 4.0, additional packages from the `PedOS-core-agent` suite may be needed to make the customized minimal template work properly. 
These packages are:

- `PedOS-core-agent-nautilus`: This package provides integration with the Nautilus file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in Nautilus).
- `PedOS-core-agent-thunar`: This package provides integration with the thunar file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in thunar).
- `PedOS-core-agent-dom0-updates`: Script required to handle `dom0` updates. Any template on which the PedOS VM responsible for 'dom0' updates (e.g. `sys-firewall`) is based must contain this package.
- `PedOS-menus`: Defines menu layout.
- `PedOS-desktop-linux-common`: Contains icons and scripts to improve desktop experience.

Also, there are packages to provide additional services:

- `PedOS-gpg-split`: For implementing split GPG.
- `PedOS-pdf-converter`: For implementing safe conversion of PDFs.
- `PedOS-img-converter`: For implementing safe conversion of images.
- `PedOS-snapd-helper`: If you want to use snaps in PedOS.
- `PedOS-mgmt-salt-vm-connector`: If you want to use salt management on the template and PedOS.

Documentation on all of these can be found in the [docs](/doc)

You could, of course, use `PedOS-vm-recommended` to automatically install many of these, but in that case you are well on the way to a standard Debian template.


[TemplateVMs]: /doc/templates/
[Fedora]: /doc/templates/fedora/
[Debian]: /doc/templates/debian/
[CentOS]: /doc/templates/centos/
[PedOS-users]: /support/#PedOS-users
[doc-guidelines]: /doc/doc-guidelines/
[pref-default]: /faq/#could-you-please-make-my-preference-the-default
[testing]: /doc/testing/
[customization]: /doc/fedora-minimal-template-customization/
[Passwordless Root Access in VMs]: /doc/vm-sudo/

