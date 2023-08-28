---
layout: doc
title: Qubes OS 4.2 release notes
permalink: /doc/releases/4.2/release-notes/
---

_**Please note:** This page is still an unfinished draft in progress. It is being updated as Qubes 4.2 development and testing continues._

## New features and improvements since Qubes 4.1

- dom0 updated to Fedora 37 ([#6982](https://github.com/QubesOS/qubes-issues/issues/6982))
- Xen updated to 4.17
- SELinux support in Fedora templates ([#4239](https://github.com/QubesOS/qubes-issues/issues/4239))
- several GUI applications rewritten, including:
  - applications menu (available as preview in R4.1 too) ([#6665](https://github.com/QubesOS/qubes-issues/issues/6665)), ([#5677](https://github.com/QubesOS/qubes-issues/issues/5677))
  - global settings ([#6898](https://github.com/QubesOS/qubes-issues/issues/6898))
  - new qube dialog
  - system updater ([#7443](https://github.com/QubesOS/qubes-issues/issues/7443))
- grub.cfg stored in /boot/grub2/grub.cfg in UEFI boot to ([#7985](https://github.com/QubesOS/qubes-issues/issues/7985))
- pipewire support ([#6358](https://github.com/QubesOS/qubes-issues/issues/6358))
- fwupd integration to allow firmware updates ([#4855](https://github.com/QubesOS/qubes-issues/issues/4855))
- optional automatic clipboard clearing ([#3415](https://github.com/QubesOS/qubes-issues/issues/3415))
- official packages built using rewritten qubes-builder (qubes-builderv2) ([#6486](https://github.com/QubesOS/qubes-issues/issues/6486))
- Split GPG and Split SSH management in Qubes Global Settings

For a full list, including more detailed descriptions, please see
[here](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+4.2%22+label%3A%22release+notes%22+is%3Aclosed).

## Known issues

- DomU firewalls have completely switched to nftables. Users should add their custom rules to the `custom-input` and `custom-forward` chains. ([#5031](https://github.com/QubesOS/qubes-issues/issues/5031), [#6062](https://github.com/QubesOS/qubes-issues/issues/6062))

For a full list of known 4.2 issues with open bug reports, please see
[here](https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Release+4.2%22+label%3A%22T%3A+bug%22).
We strongly recommend [updating Qubes OS](/doc/how-to-update/) immediately
after installation in order to apply any and all available bug fixes.

## Download

See [downloads](/downloads/).

## Installation instructions

See the [installation guide](/doc/installation-guide/).

## Upgrading

Please see [how to upgrade to Qubes 4.2](/doc/upgrade/4.2/).
