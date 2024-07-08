---
lang: en
layout: doc
permalink: /doc/templates/xfce/
redirect_from:
- /doc/xfce/
- /doc/templates/fedora-xfce/
- /en/doc/templates/xfce/
- /doc/Templates/Xfce/
- /wiki/Templates/Xfce/
ref: 222
title: Xfce templates
---

If you would like to use Xfce (more lightweight compared to GNOME desktop environment) Linux distribution in your qubes,
you can install one of the available Xfce templates for [Fedora](/doc/templates/fedora/), [Debian](/doc/templates/debian/), [CentOS](/doc/templates/centos/), or [Gentoo](/doc/templates/gentoo/).

## Installation

The Fedora Xfce templates can be installed with the following command (where `X` is your desired distro and version number):

```
[user@dom0 ~]$ sudo qubes-dom0-update qubes-template-X-xfce
```

If your desired version is not found, it may still be in [testing](/doc/testing/).
You may wish to try again with the testing repository enabled:

```
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-itl-testing qubes-template-X-xfce
```

If you would like to install a community distribution, like CentOS or Gentoo, try the install command by enabling the community repository:

```
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community qubes-template-X-xfce
```

If your desired version is not found, it may still be in [testing](/doc/testing/).
You may wish to try again with the testing repository enabled:

```
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community-testing qubes-template-X-xfce
```

The download may take a while depending on your connection speed.

To reinstall a Xfce template that is already installed in your system, see [How to Reinstall a template](/doc/reinstall-template/).
