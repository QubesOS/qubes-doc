---
layout: doc
title: Qubes R4.0 release notes
permalink: /doc/releases/4.0/release-notes/
---

Qubes R4.0 release notes
========================

New features since 3.2
----------------------

* Core management scripts rewrite with better structure and extensibility, [API documentation][api-doc]
* [Admin API][admin-api] allowing strictly controlled managing from non-dom0
* All `qvm-*` command-line tools rewritten, some options have changed
* Renaming VM directly is prohibited, there is GUI to clone under new name and remove old VM
* [Use HVM by default][hvm-switch] to lower [attack surface on Xen][qsb-24]
* Create USB VM by default
* [Multiple Disposable VMs templates support][dispvm-ticket]
* New [backup format][backup-format] using scrypt key-derivation function
* Non-encrypted backups no longer supported
* [split VM packages][packages-split], for better support minimal, specialized templates
* [Qubes Manager decomposition][manager-ticket] - domains and devices widgets instead of full Qubes Manager; devices widget support also USB
* [More flexible firewall interface][vm-interface] for ease unikernel integration
* Template VMs do not have network interface by default, [qrexec-based updates proxy][qrexec-proxy] is used instead
* More flexible IP addressing for VMs - [custom IP][custom-ip], [hidden from the IP][hide-ip]
* More flexible Qubes RPC policy - [related ticket][qrexec-policy-keywords], [documentation][qrexec-doc]
* [New Qubes RPC confirmation window][qrexec-confirm], including option to specify destination VM
* Dom0 update to Fedora 25 for better hardware support
* Kernel 4.9.x

You can get detailed description in [completed github issues][github-release-notes]

Note
----
* PV VMs restaured from R3.2 to R4.x will be automatically migrated to PVH from R4.rc4 to address [QSB 37 (Meltdown & Spectre)][qsb-37]. However PV VMs restaured from R4.x are not migrated.

Known issues
------------

* On some laptops (for example Librem 15v2), touchpad do not work directly after installation. Reboot the system to fix the issue.

* List of USB devices may contain device identifiers instead of name

* For other known issues take a look at [our tickets](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Release+4.0%22+label%3Abug)

* Until R4.rc3 included, PV VMs restaured from R3.x backup will not automatically be migrated to PVH mode and may be explosed to [QSB 37][qsb-37].

It is advised to install updates just after system installation to apply bug fixes for (some of) the above problems.

Downloads
---------

See [Qubes Downloads](/downloads/).

Installation instructions
-------------------------

See [Installation Guide](/doc/installation-guide/).

Upgrading
---------

There is no in-place upgrade path from earlier Qubes versions. The only
supported option to upgrade to Qubes R4.0 is to install it from scratch and use
[qubes backup and restore tools][backup] for migrating of all of the user VMs.
We also provide [detailed instruction][upgrade-to-r4.0] for this procedure.


[backup]: /doc/backup-restore/
[github-release-notes]: https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+4.0%22+label%3Arelease-notes+is%3Aclosed
[custom-ip]: https://github.com/QubesOS/qubes-issues/issues/1477
[hide-ip]: https://github.com/QubesOS/qubes-issues/issues/1143
[packages-split]: https://github.com/QubesOS/qubes-issues/issues/2771
[hvm-switch]: https://github.com/QubesOS/qubes-issues/issues/2185
[manager-ticket]: https://github.com/QubesOS/qubes-issues/issues/2132
[dispvm-ticket]: https://github.com/QubesOS/qubes-issues/issues/2253
[qrexec-proxy]: https://github.com/QubesOS/qubes-issues/issues/1854
[qrexec-policy-keywords]: https://github.com/QubesOS/qubes-issues/issues/865
[qrexec-confirm]: https://github.com/QubesOS/qubes-issues/issues/910
[qrexec-doc]: /doc/qrexec3/#extra-keywords-available-in-qubes-40-and-later
[vm-interface]: /doc/vm-interface/
[admin-api]: /news/2017/06/27/qubes-admin-api/
[qsb-24]: https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-024-2016.txt
[qsb-37]: https://www.qubes-os.org/news/2018/01/24/qsb-37-update/
[backup-format]: /doc/backup-emergency-restore-v4/
[api-doc]: https://dev.qubes-os.org/projects/qubes-core-admin/en/latest/
[upgrade-to-r4.0]: /doc/upgrade-to-r4.0/
