---
layout: doc
title: Qubes OS 4.2 release notes
permalink: /doc/releases/4.2/release-notes/
---

## New features and improvements since Qubes 4.1

- Dom0 upgraded to Fedora 37 ([#6982](https://github.com/QubesOS/qubes-issues/issues/6982))
- Xen upgraded to version 4.17
- Default Debian template upgraded to Debian 12
- Default Fedora and Debian templates use Xfce instead of GNOME ([#7784](https://github.com/QubesOS/qubes-issues/issues/7784))
- SELinux support in Fedora templates ([#4239](https://github.com/QubesOS/qubes-issues/issues/4239))
- Several GUI applications rewritten (screenshots below), including:
  - Applications Menu (also available as preview in R4.1) ([#6665](https://github.com/QubesOS/qubes-issues/issues/6665)), ([#5677](https://github.com/QubesOS/qubes-issues/issues/5677))
  - Qubes Global Settings ([#6898](https://github.com/QubesOS/qubes-issues/issues/6898))
  - Create New Qube
  - Qubes Update ([#7443](https://github.com/QubesOS/qubes-issues/issues/7443))
- Unified `grub.cfg` location for both UEFI and legacy boot ([#7985](https://github.com/QubesOS/qubes-issues/issues/7985))
- PipeWire support ([#6358](https://github.com/QubesOS/qubes-issues/issues/6358))
- fwupd integration for firmware updates ([#4855](https://github.com/QubesOS/qubes-issues/issues/4855))
- Optional automatic clipboard clearing ([#3415](https://github.com/QubesOS/qubes-issues/issues/3415))
- Official packages built using Qubes Builder v2 ([#6486](https://github.com/QubesOS/qubes-issues/issues/6486))
- Split GPG management in Qubes Global Settings
- Qrexec services use new qrexec policy format by default (but old format is still supported) ([#8000](https://github.com/QubesOS/qubes-issues/issues/8000))
- Improved keyboard layout switching

For a full list, including more detailed descriptions, please see [here](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+4.2%22+label%3A%22release+notes%22+is%3Aclosed). Below are some screenshots of the new and improved Qubes GUI tools.

The new Qubes OS Update tool:

[![Screenshot of the Qubes OS Update tool](/attachment/site/4-2_update.png)](/attachment/site/4-2_update.png)

The new Qubes OS Global Config tool:

[![Screenshot of the Qubes OS Global Config tool](/attachment/site/4-2_global-config_1.png)](/attachment/site/4-2_global-config_1.png)
[![Screenshot of the Qubes OS Global Config tool](/attachment/site/4-2_global-config_2.png)](/attachment/site/4-2_global-config_2.png)

The new Qubes OS Policy Editor tool:

[![Screenshot of the Qubes OS Policy Editor tool](/attachment/site/4-2_policy-editor.png)](/attachment/site/4-2_policy-editor.png)

## Known issues

- DomU firewalls have completely switched to nftables. Users should add their custom rules to the `custom-input` and `custom-forward` chains. (For more information, see issues [#5031](https://github.com/QubesOS/qubes-issues/issues/5031) and [#6062](https://github.com/QubesOS/qubes-issues/issues/6062).)

- Templates restored in 4.2 from a pre-4.2 backup continue to target their original Qubes OS release repos. If you are using fresh templates on a clean 4.2 installation, or if you performed an [in-place upgrade from 4.1 to 4.2](/doc/upgrade/4.2/#in-place-upgrade), then this does not affect you. (For more information, see issue [#8701](https://github.com/QubesOS/qubes-issues/issues/8701).)

Also see the [full list of open bug reports affecting Qubes 4.2](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+label%3Aaffects-4.2+label%3A%22T%3A+bug%22+is%3Aopen).

We strongly recommend [updating Qubes OS](/doc/how-to-update/) immediately after installation in order to apply all available bug fixes.

## Notes

- Qubes 4.2 does not support Debian 11 templates (see [supported template releases](/doc/supported-releases/#templates)). Please [upgrade your Debian templates](/doc/templates/debian/#upgrading) to Debian 12.

## Download

All Qubes ISOs and associated [verification files](/security/verifying-signatures/) are available on the [downloads](/downloads/) page.

## Installation instructions

See the [installation guide](/doc/installation-guide/).

## Upgrading

Please see [how to upgrade to Qubes 4.2](/doc/upgrade/4.2/).
