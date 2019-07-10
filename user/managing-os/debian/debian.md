---
layout: doc
title: Debian Template
permalink: /doc/templates/debian/
redirect_from:
- /doc/debian/
- /en/doc/templates/debian/
- /doc/Templates/Debian/
- /wiki/Templates/Debian/
---

Debian template(s)
===============

If you would like to use Debian Linux distribution in your qubes, you can install one of the available Debian templates.

Updates for these templates are provided by ITL and are signed by this key:

    pub   4096R/47FD92FA 2014-07-27
          Key fingerprint = 2D43 E932 54EE EA7C B31B  6A77 5E58 18AB 47FD 92FA
    uid                  Qubes OS Debian Packages Signing Key

The key is already installed when you install (signed) template package. You
can also obtain the key from [git
repository](https://github.com/QubesOS/qubes-core-agent-linux/blob/master/misc/qubes-archive-keyring.gpg),
which is also integrity-protected using signed git tags.

If you want a debian-minimal template, this can be built using [Qubes-builder](https://www.qubes-os.org/doc/qubes-builder/),by selecting a +minimal flavour in setup, and then               

    make qubes-vm && make template

Installing
----------

Templates can be installed with the following command:

Debian 7 (wheezy) - obsolete/archive:

    [user@dom0 ~]$ sudo qubes-dom0-update qubes-template-debian-7

Debian 8 (jessie) - oldoldstable:

    [user@dom0 ~]$ sudo qubes-dom0-update qubes-template-debian-8

Debian 9 (stretch) - oldstable:

    [user@dom0 ~]$ sudo qubes-dom0-update qubes-template-debian-9


A Debian-10 template is currently available from the testing repository.

Debian 10 (buster) - stable:

    [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-itl-testing qubes-template-debian-10

Because this template was built *before* buster became stable, it cannot be updated without [manually accepting the change in status][5149].



Upgrading
---------

To upgrade your Debian TemplateVM, please consult the guide that corresponds to your situation:

 * [Upgrading the Debian 8 Template to Debian 9](/doc/template/debian/upgrade-8-to-9/)


Known issues
------------

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

Some packages will throw an error on installation in this situation. For example, Samba expects to be configured using a network interface post installation.

One solution is to add a dummy interface to allow the package to install correctly:

    ip link add d0 type dummy
    ip addr add 192.168.0.1/24 dev d0
    ip link set d0 up



Contributing
----------------

If you want to help in improving the template, feel free to [contribute](/wiki/ContributingHowto).


More information
----------------

* [Debian wiki](https://wiki.debian.org/Qubes)


[stretch]: /doc/template/debian/upgrade-8-to-9/ 
[5149]: https://github.com/QubesOS/qubes-issues/issues/5149
