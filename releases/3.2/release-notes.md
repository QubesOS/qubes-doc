---
layout: doc
title: Qubes R3.2 release notes
permalink: /doc/releases/3.2/release-notes/
---

Qubes R3.2 release notes
========================

*this page is a draft for yet unreleased version*

New features since 3.1
----------------------

* Management Stack extended to support in-VM configuration - [documentation][salt-doc]
* PV USB - [documentation][usb]
* Dom0 update to Fedora 23 for better hardware support
* Kernel 4.4.x
* KDE 5 support
* Tiling window managers support: awesome, [i3][i3]
* More flexible Qubes RPC services - [related ticket][qrexec-argument], [documentation][qrexec-doc]

You can get detailed description in [completed github issues][github-release-notes]

Known issues
------------

* Installation image does not fit on DVD, requires either DVD DL, or USB stick (5GB or more)

* Windows Tools: `qvm-block` does not work

* Some icons in the Qubes Manager application might not be drawn correctly when using the Xfce4 environment in Dom0. If this bothers you, please use the KDE environment instead.

* For other known issues take a look at [our tickets](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Release+3.2%22+label%3Abug)

It is advised to install updates just after system installation to apply bug fixes for (some of) the above problems.

Downloads
---------

See [Qubes Downloads](/downloads/).

Installation instructions
-------------------------

See [Installation Guide](/doc/installation-guide/).

Upgrading
---------

### From R3.1

The easiest and safest way to upgrade to Qubes R3.2 is to install it from
scratch and use [qubes backup and restore tools][backup] for
migrating of all of the user VMs.

Users of Qubes R3.1 can also upgrade using [this
procedure][upgrade].

### From R3.0 or earlier

When upgrading from earlier versions the easiest and safest way is to install
it from scratch and use [qubes backup and restore tools][backup]
for migrating of all of the user VMs.

Alternatively you can [upgrade to R3.1 using][upgrade-r3.1] first, then follow
the instructions above. This will be time consuming process.

[salt-doc]: /doc/salt/
[usb]: /doc/usb/
[i3]: /doc/i3/
[upgrade]: /doc/upgrade-to-r3.2/
[upgrade-r3.1]: /doc/releases/3.1/release-notes/#upgrading
[backup]: /doc/backup-restore/
[qrexec-argument]: https://github.com/QubesOS/qubes-issues/issues/1876
[qrexec-doc]: /doc/qrexec3/#service-argument-in-policy
[github-release-notes]: https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+3.2%22+label%3Arelease-notes+is%3Aclosed
