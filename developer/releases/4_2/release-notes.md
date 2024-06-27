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

- Qubes 4.2.2 includes a fix for [#8332: File-copy qrexec service is overly restrictive](https://github.com/QubesOS/qubes-issues/issues/8332). As explained in the issue comments, we introduced a change in Qubes 4.2.0 that caused inter-qube file-copy/move actions to reject filenames containing, e.g., non-Latin characters and certain symbols. The rationale for this change was to mitigate the security risks associated with unusual unicode characters and invalid encoding in filenames, which some software might handle in an unsafe manner and which might cause confusion for users. Such a change represents a trade-off between security and usability.
  
  After the change went live, we received several user reports indicating more severe usability problems than we had anticipated. Moreover, these problems were prompting users to resort to dangerous workarounds (such as packing files into an archive format prior to copying) that carry far more risk than the original risk posed by the unrestricted filenames. In addition, we realized that this was a backward-incompatible change that should not have been introduced in a minor release in the first place.
  
  Therefore, we have decided, for the time being, to restore the original (pre-4.2) behavior by introducing a new `allow-all-names` argument for the `qubes.Filecopy` service. By default, `qvm-copy` and similar tools will use this less restrictive service (`qubes.Filecopy+allow-all-names`) whenever they detect any files that would be have been blocked by the more restrictive service (`qubes.Filecopy+`). If no such files are detected, they will use the more restrictive service.
  
  Users who wish to opt for the more restrictive 4.2.0 and 4.2.1 behavior can do so by modifying their RPC policy rules. To switch a single rule to the more restrictive behavior, change `*` in the argument column to `+` (i.e., change "any argument" to "only empty"). To use the more restrictive behavior globally, add a "deny" rule for `qubes.Filecopy+allow-all-names` before all other relevant rules. For more information, see [RPC policies](/doc/rpc-policy/) and [Qube configuration interface](/doc/vm-interface/#qubes-rpc).

## Download

All Qubes ISOs and associated [verification files](/security/verifying-signatures/) are available on the [downloads](/downloads/) page.

## Installation instructions

See the [installation guide](/doc/installation-guide/).

## Upgrading

Please see [how to upgrade to Qubes 4.2](/doc/upgrade/4.2/).
