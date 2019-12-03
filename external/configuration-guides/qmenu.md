---
layout: doc
title: Manage Qubes via dmenu
permalink: /doc/qmenu/
---


Manage Qubes via dmenu
==============================

qmenu
-----

[qmenu](https://github.com/sine3o14nnae/qmenu/) is a collection of tools that utilize
[dmenu](https://tools.suckless.org/dmenu/), a dynamic menu for X, to provide you with a drop down menu for Qubes specific tasks.

When configured to execute these tools via hotkeys, you are able to list, start and stop your qubes, attach and detach your connected devices,
adjust your qube preferences, firewall rules, per-qube keyboard layouts, and launch applications very quickly with only the keyboard.

List of qmenu tools:

- qmenu-al - Launch domU applications.

- qmenu-dm - List and manage your connected devices.

- qmenu-vm - List, manage and configure your qubes.

Warning
-------

qmenu is **not** included in the Qubes dom0 repositories. This page will show you how to install qmenu by cloning its repository
to a disposable qube and [copying its contents to dom0](https://www.qubes-os.org/doc/copy-from-dom0/#copying-to-dom0).
**However, this way of installing software in dom0 is not advised and can compromise the security of your system!**

**Furthermore, qmenu is unreviewed third party software and is in no way endorsed by the Qubes team. You have to trust its maintainers
to not act maliciously and to protect it from malicious and unsafe contributions. Keep in mind that you are
installing these tools in _dom0_, so judge accordingly.**

Installation
------------

- Install dmenu:

       [user@dom0]$ sudo qubes-dom0-update dmenu

- Start a disposable qube that is able to connect to the internet. **Do not use this qube for anything else!**
Then inside this qube; clone the qmenu repository with git:

       [user@dispXXXX ~]$ git clone https://github.com/sine3o14nnae/qmenu/

- Import the authors public key:

       [user@dispXXXX ~]$ gpg2 --keyserver pool.sks-keyservers.net --recv-keys 0xCBE6 0BC2 811F FE14 333F EE05 3435 0BCA 3DDE 9AD9

- Check the validity of the signed commit:

       [user@dispXXXX ~/qmenu/]$ git show --show-signature

- Finally, decide what qmenu tools you want to use, replace 'XX' accordingly, then copy them to dom0, place them
inside your path and change their mode bits.

       [user@dom0 ~]$ qvm-run --pass-io dispXXXX 'cat /home/user/qmenu/qmenu-XX' > /tmp/qmenu-XX

       [user@dom0 ~]$ sudo cp /tmp/qmenu-XX /usr/bin/

       [user@dom0 ~]$ sudo chmod 755 /usr/bin/qmenu-XX

- _Optionally_, copy the default config file:

       [user@dom0 ~]$ qvm-run --pass-io dispXXXX 'cat /home/user/qmenu/qmenu.conf' > /home/user/.config/qmenu.conf

Customization
-------------

### qmenu ###

The colors that correspond to the qube label can be adjusted by creating a text file called
`qmenu.conf` in `/home/user/.config/` with the following contents:

~~~
[LABEL 1]=#[HEX TRIPLET]
[LABEL 2]=#[HEX TRIPLET]
...
[LABEL 8]=#[HEX TRIPLET]
~~~    
    
### dmenu ###

In order to customize and configure dmenu, instead of downloading it from the repositories,
you have to get it from [suckless](https://tools.suckless.org/dmenu/patches/), compile it yourself
and [copy it to dom0](https://www.qubes-os.org/doc/copy-from-dom0/#copying-to-dom0).
**However, this way of installing software in dom0 is not advised and can compromise the security of your system!**
