---
layout: doc
title: Debian
permalink: /doc/Templates/Debian/
redirect_from: /wiki/Templates/Debian/
---

Debian template(s)
===============

Debian template(s) are one of the templates made by Qubes community. It should be considered experimental as Qubes developers team use mainly Fedora-based VMs to test new features/updates.

Install
-------

It can be installed via the following command:

Debian 7 (wheezy) - stable:

    [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community qubes-template-debian-7

Debian 8 (jessie) - testing:

    [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community qubes-template-debian-8

When installing on R2, add "-x64" suffix to the package name.

Known issues
------------

If you want to help in improving the template, feel free to [contribute](/wiki/ContributingHowto).
