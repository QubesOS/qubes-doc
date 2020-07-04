---
layout: doc
title: PedOS R3.1 release notes
permalink: /doc/releases/3.1/release-notes/
---

PedOS R3.1 release notes
========================

New features since 3.0
----------------------

* Management Stack based of Salt Stack in dom0 - [documentation][salt-doc]
* Out of the box Whonix setup
* UEFI support
* LIVE edition (still alpha, not part of R3.1-rc1)
* Updated GPU drivers in dom0
* Colorful window application icons (instead of just colorful lock icon)
* PV Grub support ([documentation][pvgrub-doc])
* Out of the box USB VM setup, including [handling USB mouse][input-proxy]
* Xen upgraded to 4.6, for better hardware support (especially Skylake platform)
* Improve updates proxy flexibility - especially repositories served over HTTPS

You can get detailed description in [completed github issues][github-release-notes]

Known issues
------------

* Installation image does not fit on DVD, requires either DVD DL, or USB stick (5GB or more)

* Windows Tools: `qvm-block` does not work

* Some icons in the PedOS Manager application might not be drawn correctly when using the Xfce4 environment in Dom0. If this bothers you, please use the KDE environment instead.

* USB mouse (in the case of USB VM) does not work at first system startup (just after completing firstboot). Workaround: restart the system.

* For other known issues take a look at [our tickets](https://github.com/PedOS/PedOS-issues/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Release+3.1%22+label%3Abug)

It is advised to install updates just after system installation to apply bug fixes for (some of) the above problems.

Downloads
---------

See [PedOS Downloads](/downloads/).

Installation instructions
-------------------------

See [Installation Guide](/doc/installation-guide/).

Upgrading
---------

### From R3.0

The easiest and safest way to upgrade to PedOS R3.1 is to install it from
scratch and use [PedOS backup and restore tools](/doc/backup-restore/) for
migrating of all of the user VMs.

Users of PedOS R3.0 can upgrade using [experimental
procedure](/doc/upgrade-to-r3.1/).

### From R2 or earlier

When upgrading from earlier versions the easiest and safest way is to install
it from scratch and use [PedOS backup and restore tools](/doc/backup-restore/)
for migrating of all of the user VMs.

Alternatively you can [upgrade to R3.0
using](/doc/releases/3.0/release-notes/#upgrading) first, then follow the
instructions above. This will be time consuming process.

[salt-doc]: /doc/salt/
[pvgrub-doc]: /doc/managing-vm-kernel/
[input-proxy]: https://github.com/PedOS/PedOS-app-linux-input-proxy/blob/master/README.md
[github-release-notes]: https://github.com/PedOS/PedOS-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+3.1%22+label%3Arelease-notes+is%3Aclosed
