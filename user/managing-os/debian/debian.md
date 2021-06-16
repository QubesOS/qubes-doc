---
lang: en
layout: doc
permalink: /doc/templates/debian/
redirect_from:
- /doc/debian/
- /en/doc/templates/debian/
- /doc/Templates/Debian/
- /wiki/Templates/Debian/
ref: 134
title: The Debian TemplateVM
---

# The Debian TemplateVM

The Debian [TemplateVM](/doc/templates/) is an officially [supported](/doc/supported-versions/#templatevms) TemplateVM in Qubes OS.
This page is about the standard (or "full") Debian TemplateVM.
For the minimal version, please see the [Minimal TemplateVMs](/doc/templates/minimal/) page.
There is also a [Qubes page on the Debian Wiki](https://wiki.debian.org/Qubes).

## Installing

To [install](/doc/templates/#installing) a specific Debian TemplateVM that is not currently installed in your system, use the following command in dom0:

```
$ sudo qubes-dom0-update qubes-template-debian-XX
```

   (Replace `XX` with the Debian version number of the template you wish to install.)

To reinstall a Debian TemplateVM that is already installed in your system, see [How to Reinstall a TemplateVM](/doc/reinstall-template/).

## After Installing

After installing a fresh Debian TemplateVM, we recommend performing the following steps:

1. [Update the TemplateVM](/doc/software-update-vm/).

2. [Switch any TemplateBasedVMs that are based on the old TemplateVM to the new one](/doc/templates/#switching).

3. If desired, [uninstall the old TemplateVM](/doc/templates/#uninstalling).

## Updating

For routine daily TemplateVM updates within a given Debian release, see [Updating software in TemplateVMs](/doc/software-update-domu/#updating-software-in-templatevms).

## Upgrading

There are two ways to upgrade your TemplateVM to a new Debian release:

- [Install a fresh template to replace the existing one.](#installing) **This option may be simpler for less experienced users.** After you install the new template, redo all desired template modifications and [switch everything that was set to the old template to the new template](/doc/templates/#switching). You may want to write down the modifications you make to your templates so that you remember what to redo on each fresh install. In the old Debian template, see `/var/log/dpkg.log` and `/var/log/apt/history.log` for logs of package manager actions.

- [Perform an in-place upgrade of an existing Debian template.](/doc/template/debian/upgrade/) This option will preserve any modifications you've made to the template, **but it may be more complicated for less experienced users.**

## Release-specific notes

This section contains notes about specific Debian releases.

### Debian 10

Debian 10 (buster) - minimal:

```
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-itl qubes-template-debian-10-minimal
```

Debian 10 (buster) - stable:

```
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-itl qubes-template-debian-10
```

### Starting services

The Debian way (generally) is to start daemons if they are installed.
This means that if you install (say) ssh-server in a template, *all* the qubes that use that template will run a ssh server when they start. (They will, naturally, all have the same server key.) This may not be what you want.

So be very careful when installing software in Templates - if the daemon spawns outbound connections then there is a serious security risk.

In general, a reasonable approach would be, (using ssh as example):

- Install the ssh service.
- `systemctl stop ssh`
- `systemctl disable ssh`
- `systemctl mask ssh`
- Close down template

Now the ssh service will **NOT** start in qubes based on this template.

Where you **DO** want the service to run, put this in `/rw/config/rc.local`:

```
systemctl unmask ssh
systemctl start ssh
```

Don't forget to make the file executable.

### Unattended Upgrades

Some users have noticed that on upgrading to Stretch, the `unattended-upgrade` package is installed.

This package is pulled in as part of a Recommend chain, and can be purged.

The lesson is that you should carefully look at what is being installed to your system, particularly if you run `dist-upgrade`.

### Package installation errors in Qubes 4.0

If some packages throw installation errors, see [this guide.](/doc/vm-troubleshooting/#fixing-package-installation-errors)

