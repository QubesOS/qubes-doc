---
layout: doc
title: The Debian TemplateVM
redirect_from:
- /doc/templates/debian/
- /doc/debian/
- /en/doc/templates/debian/
- /doc/Templates/Debian/
- /wiki/Templates/Debian/
---

# The Debian TemplateVM

The Debian [TemplateVM] is an officially [supported] TemplateVM in Qubes OS.
This page is about the standard (or "full") Debian TemplateVM.
For the minimal version, please see the [Minimal TemplateVMs] page.
There is also a [Qubes page on the Debian Wiki].


## Installing

To [install] a specific Debian TemplateVM that is not currently installed in your system, use the following command in dom0:

    $ sudo qubes-dom0-update qubes-template-debian-XX

   (Replace `XX` with the Debian version number of the template you wish to install.)

To reinstall a Debian TemplateVM that is already installed in your system, see [How to Reinstall a TemplateVM].


## After Installing

After installing a fresh Debian TemplateVM, we recommend performing the following steps:

1. [Update the TemplateVM].

2. [Switch any TemplateBasedVMs that are based on the old TemplateVM to the new one][switch].

3. If desired, [uninstall the old TemplateVM].


## Updating

Please see [Updating software in TemplateVMs].


## Upgrading

Please see [Upgrading Debian TemplateVMs].


## Release-specific notes

This section contains notes about specific Debian releases.


### Debian 10

Debian 10 templates are currently available from the testing repository.

Debian 10 (buster) - minimal:

    [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-itl-testing qubes-template-debian-10-minimal

Because this template was built *before* buster became stable, it cannot be updated without [manually accepting the change in status][5149].
Also, to install additional Qubes packages you will have to enable the qubes-testing repository.


Debian 10 (buster) - stable:

    [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-itl-testing qubes-template-debian-10

Because this template was built *before* buster became stable, it cannot be updated without [manually accepting the change in status][5149].


### Starting services

The Debian way (generally) is to start daemons if they are installed.
This means that if you install (say) ssh-server in a template, *all* the qubes that use that template will run a ssh server when they start. (They will, naturally, all have the same server key.) This may not be what you want.

So be very careful when installing software in Templates - if the daemon spawns outbound connections then there is a serious security risk.

In general, a reasonable approach would be, (using ssh as example):
- Install the ssh service.
- systemctl stop ssh
- systemctl disable ssh
- systemctl mask ssh
- Close down template

Now the ssh service will **NOT** start in qubes based on this template.

Where you **DO** want the service to run, put this in /rw/config/rc.local:

    systemctl unmask ssh
    systemctl start ssh

Don't forget to make the file executable.


### Unattended Upgrades

Some users have noticed that on upgrading to Stretch, the unattended-upgrade package is installed.

This package is pulled in as part of a Recommend chain, and can be purged.

The lesson is that you should carefully look at what is being installed to your system, particularly if you run dist-upgrade. 


### Package installation errors in Qubes 4.0

By default, templates in 4.0 only have a loopback interface.

Some packages will throw an error on installation in this situation.
For example, Samba expects to be configured using a network interface post installation.

One solution is to add a dummy interface to allow the package to install correctly:

    ip link add d0 type dummy
    ip addr add 192.168.0.1/24 dev d0
    ip link set d0 up


[TemplateVM]: /doc/templates/
[Minimal TemplateVMs]: /doc/templates/minimal/
[Qubes page on the Debian Wiki]: https://wiki.debian.org/Qubes
[end-of-life]: https://wiki.debian.org/DebianReleases#Production_Releases
[supported]: /doc/supported-versions/#templatevms
[How to Reinstall a TemplateVM]: /doc/reinstall-template/
[Update the TemplateVM]: /doc/software-update-vm/
[switch]: /doc/templates/#switching
[uninstall the old TemplateVM]: /doc/templates/#uninstalling
[Updating software in TemplateVMs]: /doc/software-update-domu/#updating-software-in-templatevms
[Upgrading Debian TemplateVMs]: /doc/template/debian/upgrade/
[5149]: https://github.com/QubesOS/qubes-issues/issues/5149
[install]: /doc/templates/#installing

