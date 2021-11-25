---
layout: doc
title: Qubes OS 4.1 release notes
permalink: /doc/releases/4.1/release-notes/
---

## New features and improvements since Qubes 4.0

- Optional qubes-remote-support package now available from repositories
  (strictly opt-in, no package installed by default; no new ports or network
  connections open by default; requires explicit connection initiation by the
  user, then requires sharing a code word with the remote party before a
  connection can be established; see
  [#6364](https://github.com/QubesOS/qubes-issues/issues/6364) for more
  information)
- Qubes firewall reworked to be more defensive (see
  [#5540](https://github.com/QubesOS/qubes-issues/issues/5540) for details)
- Xen upgraded to version 4.14
- Dom0 operating system upgraded to Fedora 32
- Default desktop environment upgraded to Xfce 4.14
- Upgraded default template releases
- Experimental support for GUI running outside of dom0 (hybrid mode GUI domain
  without real GPU passthrough; see
  [#5662](https://github.com/QubesOS/qubes-issues/issues/5662) for details)
- Experimental support for audio server running outside of dom0 ("Audio domain")
- sys-firewall and sys-usb are now disposables by default
- UEFI boot now loads GRUB, which in turn loads Xen, making the boot path
  similar to legacy boot and allowing the user to modify boot parameters or
  choose an alternate boot menu entry
- New qrexec policy format (see
  [#4370](https://github.com/QubesOS/qubes-issues/issues/4370) for details)
- qrexec protocol improvements (see
  [#4909](https://github.com/QubesOS/qubes-issues/issues/4909) for details)
- New qrexec-policy daemon
- Simplified using in-qube kernels
- Clarified disposable-related terminology and properties
- Default kernelopts can now be specified by a kernel package
- Improved support for high-resolution displays
- Improved notifications when a system drive runs out of free space
- Support for different cursor shapes
- "Paranoid mode" backup restore option now properly supported using
  disposables
- Users can now choose between Debian and Fedora in the installer
- Certain files and applications are now opened in disposables, e.g.,
  Thunderbird email attachments
- New graphical interface for managing testing repository updates
- New "Cute Qube" icon family (replaces padlock icons)
- Disposable qube types now use the disposable icon
- New Template Manager tool for installing, removing, and updating templates
  (meanwhile, the tool previously known as the "Template Manager," which was
  for mass template switching, has been integrated into the Qube Manager)
- The "file" storage driver has been deprecated in Qubes 4.1 and will be
  removed in Qubes 4.2
- `property-del` event renamed to `property-reset` to avoid confusion
- qrexec no longer supports non-executable files in `/etc/qubes-rpc`
- qrexec components have been reorganized into the core-qrexec repository
- The `qvm-pool` argument parser has been rewritten and improved
- Removed the need for the out-of-tree u2mfn kernel module
- Qrexec services can now run as a socket server
- Improved template distribution mechanism
- Now possible to restart qrexec-agent
- The term "VM" has largely been replaced by "qube"
- GUI daemon is now configured using `qvm-features` tool,
  `/etc/qubes/guid.conf` file is no longer used
- `qvm-run` tool got `--no-shell` option to run a single command without using
  a shell inside the qube

For a full list, including more detailed descriptions, please see
[here](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+4.1%22+label%3A%22release+notes%22+is%3Aclosed).

## Known issues

For a full list of known 4.1 issues with open bug reports, please see
[here](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Release+4.1%22+label%3A%22T%3A+bug%22).
We strongly recommend [updating Qubes OS](/doc/how-to-update/) immediately
after installation in order to apply any and all available bug fixes.

## Download

See [downloads](/downloads/).

## Installation instructions

See the [installation guide](/doc/installation-guide/).

## Upgrading

Please see [how to upgrade to Qubes 4.1](/doc/upgrade/4.1/).
