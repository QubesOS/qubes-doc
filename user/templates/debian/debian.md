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
title: Debian templates
---

The Debian [template](/doc/templates/) is an officially [supported](/doc/supported-releases/#templates) template in Qubes OS.  
This page is about the standard (or "full") Debian template.
For the minimal version, please see the [Minimal templates](/doc/templates/minimal/) page.
There is also a [Qubes page on the Debian Wiki](https://wiki.debian.org/Qubes).

Building a template in Qubes OS is not a trivial process. Below is a (tally?) of known Debian releases, and the status of their Qubes OS templates. Release-specific installation notes, are at the bottom of the page below the general installation notes. 

| Release Version        |  Initial Release Date & Status*       |  Does a Qubes OS "full" Template yet exist for this? |  Does a Qubes OS "minimal" Template yet exist for this? |
| :---                   |  :---                                 |  :---                                                |  :---                                                  |
| Debian 11 "bullseye"   | 14 Aug 2021, current stable           |  No                                                  |  No                                                     |
| Debian 10 "buster"     | 06 Jul 2019, current oldstable            |  Yes                                             |  Yes                                                    |
| Debian 9 "stretch"     | 27 Jun 2017, oldoldstable under LTS       |  Decomissioned                                   | Decomissioned                                           |
| Debian 8 "jessie"      | 26 Apr 2015, archived under Extended LTS  |  Decomissioned                                   | Decomissioned                                           |
| Debian 7 "wheezy"      | 04 May 2013, obsolete stable              |  Decomissioned                                   | Decomissioned

## Installing

To [install](/doc/templates/#installing) a specific Debian template that is not currently installed in your system, use the following command in dom0:

```
$ sudo qubes-dom0-update qubes-template-debian-XX
```

   (Replace `XX` with the Debian version number of the template you wish to install.)

To reinstall a Debian template that is already installed in your system, see [How to Reinstall a template](/doc/reinstall-template/).

## After Installing

After installing a fresh Debian template, we recommend performing the following steps:

1. [Update the template](/doc/software-update-vm/).

2. [Switch any app qubes that are based on the old template to the new one](/doc/templates/#switching).

3. If desired, [uninstall the old template](/doc/templates/#uninstalling).

## Installing software

See [How to Install Software](/doc/how-to-install-software/).

## Updating

For routine daily updates within a given release, see [How to Update](/doc/how-to-update/).

## Upgrading

There are two ways to upgrade your template to a new Debian release:

- **Recommended:** [Install a fresh template to replace the existing one.](#installing) **This option may be simpler for less experienced users.** After you install the new template, redo all desired template modifications and [switch everything that was set to the old template to the new template](/doc/templates/#switching). You may want to write down the modifications you make to your templates so that you remember what to redo on each fresh install. In the old Debian template, see `/var/log/dpkg.log` and `/var/log/apt/history.log` for logs of package manager actions.

- **Advanced:** [Perform an in-place upgrade of an existing Debian template.](/doc/template/debian/upgrade/) This option will preserve any modifications you've made to the template, **but it may be more complicated for less experienced users.**

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
