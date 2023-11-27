---
layout: doc
title: Qubes OS 4.2.0 release notes
permalink: /doc/releases/4.2/release-notes/
---

_**Please note:** This page is still an unfinished draft in progress. It is being updated as Qubes 4.2 development and testing continues._

## New features and improvements since Qubes 4.1

- Dom0 upgraded to Fedora 37 ([#6982](https://github.com/QubesOS/qubes-issues/issues/6982))
- Xen upgraded to version 4.17
- Default Debian template upgraded to Debian 12
- Default Fedora and Debian templates use Xfce instead of GNOME ([#7784](https://github.com/QubesOS/qubes-issues/issues/7784))
- SELinux support in Fedora templates ([#4239](https://github.com/QubesOS/qubes-issues/issues/4239))
- Several GUI applications rewritten, including:
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

For a full list, including more detailed descriptions, please see
[here](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+4.2%22+label%3A%22release+notes%22+is%3Aclosed).

## Known issues

- DomU firewalls have completely switched to nftables. Users should add their custom rules to the `custom-input` and `custom-forward` chains. ([#5031](https://github.com/QubesOS/qubes-issues/issues/5031), [#6062](https://github.com/QubesOS/qubes-issues/issues/6062))

For a full list of open bug reports affecting 4.2, please see [here](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+label%3Aaffects-4.2+label%3A%22T%3A+bug%22+is%3Aopen). We strongly recommend [updating Qubes OS](/doc/how-to-update/) immediately after installation in order to apply any and all available bug fixes.

## Download

All Qubes ISOs and associated [verification files](/security/verifying-signatures/) are available on the [downloads](/downloads/) page.

## Installation instructions

See the [installation guide](/doc/installation-guide/).

## Upgrading

Please see [how to upgrade to Qubes 4.2](/doc/upgrade/4.2/).
