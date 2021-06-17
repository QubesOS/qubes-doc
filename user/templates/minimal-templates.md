---
lang: en
layout: doc
permalink: /doc/templates/minimal/
redirect_from:
- /doc/templates/fedora-minimal/
- /doc/fedora-minimal/
- /en/doc/templates/fedora-minimal/
- /doc/Templates/FedoraMinimal/
- /wiki/Templates/FedoraMinimal/
- /doc/templates/debian-minimal/
ref: 132
title: Minimal Templates
---

The Minimal [TemplateVMs](/doc/templates/) are lightweight versions of their standard TemplateVM counterparts.
They have only the most vital packages installed, including a minimal X and xterm installation.
The sections below contain instructions for using the template and provide some examples for common use cases.
There are currently three Minimal TemplateVMs corresponding to the standard [Fedora](/doc/templates/fedora/), [Debian](/doc/templates/debian/), [CentOS](/doc/templates/centos/) and [Gentoo](/doc/templates/gentoo/) TemplateVMs.

## Important

1. The Minimal TemplateVMs are intended only for advanced users.
   If you encounter problems with the Minimal TemplateVMs, we recommend that you use their standard TemplateVM counterparts instead.

2. If something works with a standard TemplateVM but not the minimal version, this is most likely due to user error (e.g., a missing package or misconfiguration) rather than a bug.
   In such cases, please do *not* file a bug report.
   Instead, please see [Help, Support, Mailing Lists, and Forum](/support/) for the appropriate place to ask for help.
   Once you have learned how to solve your problem, please [contribute what you learned to the documentation](/doc/doc-guidelines/).

3. The Minimal TemplateVMs are intentionally *minimal*.
   [Do not ask for your favorite package to be added to the minimal template by default.](/faq/#could-you-please-make-my-preference-the-default)

4. In order to reduce unnecessary risk, unused repositories have been disabled by default.
   If you wish to install or update any packages from those repositories, you must enable them.

## Installation

The Minimal TemplateVMs can be installed with the following command (where `X` is your desired distro and version number):

```
[user@dom0 ~]$ sudo qubes-dom0-update qubes-template-X-minimal
```

If your desired version is not found, it may still be in [testing](/doc/testing/).
You may wish to try again with the testing repository enabled:

```
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-itl-testing qubes-template-X-minimal
```

If you would like to install a community distribution, try the install command by enabling the community repository:

```
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community qubes-template-X-minimal
```

The download may take a while depending on your connection speed.

## Passwordless root

It is an intentional design choice for [Passwordless Root Access in VMs](/doc/vm-sudo/) to be optional in Minimal TemplateVMs.
Since the Minimal TemplateVMs are *minimal*, they are not configured for passwordless root by default.
To update or install packages, execute the following command in dom0 (where `X` is your distro and version number):

```
[user@dom0 ~]$ qvm-run -u root X-minimal xterm
```

This opens a root terminal in the Minimal TemplateVM, from which you can use execute root commands without `sudo`.
You will have to do this every time if you choose not to enable passwordless root.

If you want to be able to use `sudo` inside a Minimal TemplateVM (or TemplateBasedVMs based on a Minimal TemplateVM), open a root terminal as just instructed, then install the `qubes-core-agent-passwordless-root` package.

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

```
[user@your-new-clone ~]$ sudo dnf install packages
```

- Commonly used utilities: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`.
- Audio: `pulseaudio-qubes`.
- [FirewallVM](/doc/firewall/), such as the template for `sys-firewall`: at least `qubes-core-agent-networking` and `iproute`, and also `qubes-core-agent-dom0-updates` if you want to use it as the `UpdateVM` (which is normally `sys-firewall`).
- NetVM, such as the template for `sys-net`: `qubes-core-agent-networking` `qubes-core-agent-network-manager` `NetworkManager-wifi` `network-manager-applet` `wireless-tools` `notification-daemon` `gnome-keyring` `polkit` `@hardware-support`. If your network devices need extra packages for the template to work as a network VM, use the `lspci` command to identify the devices, then run `dnf search firmware` (replace `firmware` with the appropriate device identifier) to find the needed packages and then install them. If you need utilities for debugging and analyzing network connections, install `tcpdump` `telnet` `nmap` `nmap-ncat`.
- [USB qube](/doc/usb-qubes/), such as the template for `sys-usb`: `qubes-usb-proxy` to provide USB devices to other Qubes and `qubes-input-proxy-sender` to provide keyboard or mouse input to dom0.
- [VPN qube](https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md): Use the `dnf search "NetworkManager VPN plugin"` command to look up the VPN packages you need, based on the VPN technology you'll be using, and install them. Some GNOME related packages may be needed as well. After creation of a machine based on this template, follow the [VPN instructions](https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.
- `default-mgmt-dvm`: requires `qubes-core-agent-passwordless-root` and `qubes-mgmt-salt-vm-connector`.

In Qubes 4.0, additional packages from the `qubes-core-agent` suite may be needed to make the customized minimal template work properly.
These packages are:

- `qubes-core-agent-nautilus`: This package provides integration with the Nautilus file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in Nautilus).
- `qubes-core-agent-thunar`: This package provides integration with the thunar file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in thunar).
- `qubes-core-agent-dom0-updates`: Script required to handle `dom0` updates. Any template on which the qube responsible for 'dom0' updates (e.g. `sys-firewall`) is based must contain this package.
- `qubes-menus`: Defines menu layout.
- `qubes-desktop-linux-common`: Contains icons and scripts to improve desktop experience.
- `qubes-core-agent-qrexec`: Qubes qrexec agent. Installed by default.
- `qubes-core-agent-systemd`: Qubes unit files for SystemD init style. Installed by default.
- `qubes-core-agent-passwordless-root`, `polkit`: By default, the Fedora Minimal template doesn't have passwordless root. These two packages enable this feature.
- `qubes-core-agent-sysvinit`: Qubes unit files for SysV init style or upstart.

Also, there are packages to provide additional services:

- `qubes-gpg-split`: For implementing split GPG.
- `qubes-u2f`: For implementing secure forwarding of U2F messages.
- `qubes-pdf-converter`: For implementing safe conversion of PDFs.
- `qubes-img-converter`: For implementing safe conversion of images.
- `qubes-snapd-helper`: If you want to use snaps in qubes.
- `thunderbird-qubes`: Additional tools for use in thunderbird.
- `qubes-app-shutdown-idle`: If you want qubes to automatically shutdown when idle.
- `qubes-mgmt-salt-vm-connector`: If you want to use salt management on the template and qubes.

You may also wish to consider additional packages from the `qubes-core-agent` suite:

See [here](https://github.com/Qubes-Community/Contents/blob/master/docs/customization/fedora-minimal-template-customization.md) for further information on customizing `fedora-minimal`.

#### Logging

The `rsyslog` logging service is not installed by default, as all logging is instead being handled by the `systemd` journal.
Users requiring the `rsyslog` service should install it manually.

To access the `journald` log, use the `journalctl` command.

### Debian

The following list provides an overview of which packages are needed for which purpose.
As usual, the required packages are to be installed in the running template with the following command (replace `packages` with a space-delimited list of packages to be installed):

```
[user@your-new-clone ~]$ sudo apt install packages
```

- Commonly used utilities: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`
- Audio: `pulseaudio-qubes`
- [FirewallVM](/doc/firewall/), such as the template for `sys-firewall`: at least `qubes-core-agent-networking`, and also `qubes-core-agent-dom0-updates` if you want to use it as the `UpdateVM` (which is normally `sys-firewall`).
- NetVM, such as the template for `sys-net`: `qubes-core-agent-networking` `qubes-core-agent-network-manager`. If your network devices need extra packages for a network VM, use the `lspci` command to identify the devices, then find the package that provides necessary firmware and install it. If you need utilities for debugging and analyzing network connections, install the following packages: `tcpdump` `telnet` `nmap` `nmap-ncat`.
- [USB qube](/doc/usb-qubes/), such as the template for `sys-usb`: `qubes-usb-proxy` to provide USB devices to other Qubes and `qubes-input-proxy-sender` to provide keyboard or mouse input to dom0.
- [VPN qube](https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md): You may need to install network-manager VPN packages, depending on the VPN technology you'll be using. After creating a machine based on this template, follow the [VPN howto](https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.
- `default-mgmt-dvm`: requires `qubes-core-agent-passwordless-root` and `qubes-mgmt-salt-vm-connector`.

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
- `qubes-img-converter`: For implementing safe conversion of images.
- `qubes-snapd-helper`: If you want to use snaps in qubes.
- `qubes-thunderbird`: Additional tools for use in thunderbird.
- `qubes-app-shutdown-idle`: If you want qubes to automatically shutdown when idle.
- `qubes-mgmt-salt-vm-connector`: If you want to use salt management on the template and qubes.

Documentation on all of these can be found in the [docs](/doc)

If you want to use interactive dialogs, (e.g file selection), you will need to add the `zenity` package. ([Here's an example](https://github.com/QubesOS/qubes-issues/issues/5202))

You could, of course, use `qubes-vm-recommended` to automatically install many of these, but in that case you are well on the way to a standard Debian template.

### CentOS

The following list provides an overview of which packages are needed for which purpose.
As usual, the required packages are to be installed in the running template with the following command (replace `packages` with a space-delimited list of packages to be installed):

```
[user@your-new-clone ~]$ sudo yum install packages
```

- Commonly used utilities: `pciutils` `vim-minimal` `less` `psmisc` `gnome-keyring`
- Audio: `pulseaudio-qubes`.
- [FirewallVM](/doc/firewall/), such as the template for `sys-firewall`: at least `qubes-core-agent-networking`, and also `qubes-core-agent-dom0-updates` if you want to use it as the `UpdateVM` (which is normally `sys-firewall`).
- NetVM, such as the template for `sys-net`: `qubes-core-agent-networking` `qubes-core-agent-network-manager` `NetworkManager-wifi` `network-manager-applet` `wireless-tools` `notification-daemon` `gnome-keyring`. If your network devices need extra packages for a network VM, use the `lspci` command to identify the devices, then find the package that provides necessary firnware and install it. If you need utilities for debugging and analyzing network connections, install the following packages: `tcpdump` `telnet` `nmap` `nmap-ncat`
- [USB qube](/doc/usb-qubes/), such as the template for `sys-usb`: `qubes-usb-proxy` to provide USB devices to other Qubes and `qubes-input-proxy-sender` to provide keyboard or mouse input to dom0.
- [VPN qube](https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md): You may need to install network-manager VPN packages, depending on the VPN technology you'll be using. After creating a machine based on this template, follow the [VPN howto](https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager) to configure it.
- `default-mgmt-dvm`: requires `qubes-core-agent-passwordless-root` and `qubes-mgmt-salt-vm-connector`.

In Qubes 4.0, additional packages from the `qubes-core-agent` suite may be needed to make the customized minimal template work properly.
These packages are:

- `qubes-core-agent-nautilus`: This package provides integration with the Nautilus file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in Nautilus).
- `qubes-core-agent-thunar`: This package provides integration with the thunar file manager (without it, items like "copy to VM/open in disposable VM" will not be shown in thunar).
- `qubes-core-agent-dom0-updates`: Script required to handle `dom0` updates. Any template on which the qube responsible for 'dom0' updates (e.g. `sys-firewall`) is based must contain this package.
- `qubes-menus`: Defines menu layout.
- `qubes-desktop-linux-common`: Contains icons and scripts to improve desktop experience.

Also, there are packages to provide additional services:

- `qubes-gpg-split`: For implementing split GPG.
- `qubes-pdf-converter`: For implementing safe conversion of PDFs.
- `qubes-img-converter`: For implementing safe conversion of images.
- `qubes-snapd-helper`: If you want to use snaps in qubes.
- `qubes-mgmt-salt-vm-connector`: If you want to use salt management on the template and qubes.

Documentation on all of these can be found in the [docs](/doc)

You could, of course, use `qubes-vm-recommended` to automatically install many of these, but in that case you are well on the way to a standard Debian template.

