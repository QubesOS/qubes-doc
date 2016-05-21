---
layout: doc
title: Debian Template
permalink: /doc/templates/debian/
redirect_from:
- /en/doc/templates/debian/
- /doc/Templates/Debian/
- /wiki/Templates/Debian/
---

Debian template(s)
===============

If you like to use Debian Linux distribution in your AppVMs, you can install one of available Debian templates.

Updates for this template are provided by ITL and are signed by this key:

    pub   4096R/47FD92FA 2014-07-27
          Key fingerprint = 2D43 E932 54EE EA7C B31B  6A77 5E58 18AB 47FD 92FA
    uid                  Qubes OS Debian Packages Signing Key

The key is already installed when you install (signed) template package. You
can also obtain the key from [git
repository](https://github.com/QubesOS/qubes-core-agent-linux/blob/master/misc/qubes-archive-keyring.gpg),
which is also integrity-protected using signed git tags.

Install
-------

It can be installed via the following command:

Debian 7 (wheezy) - old stable:

    [user@dom0 ~]$ sudo qubes-dom0-update qubes-template-debian-7

(The download will take a while, and there will be no progress indicator.)

Debian 8 (jessie) - stable:

    [user@dom0 ~]$ sudo qubes-dom0-update qubes-template-debian-8

(The download will take a while, and there will be no progress indicator.)

Debian 9 (stretch) - testing:

A prebuilt template is not yet available, but there are two options for
achieving a stretch template:

* Build an experimental stretch template from source.

* Clone a `debian-8` template and then modify `/etc/apt/sources.list` and 
`/etc/apt/sources.list.d/qubes-r3.list` to pull from stretch repos rather 
than jessie repos. After that, an `apt-get dist-upgrade` followed by a 
reboot should "just work."


Known issues
------------

If you want to help in improving the template, feel free to [contribute](/wiki/ContributingHowto).
