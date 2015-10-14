---
layout: doc
title: Lenovo450Tinkering
permalink: /en/doc/lenovo450-tinkering/
redirect_from:
- /doc/Lenovo450Tinkering/
- /wiki/Lenovo450Tinkering/
---

Instructions for getting your Lenovo 450 laptop working with Qubes/Linux
=========================================================================

Lenovo 450 uses UEFI, so some settings are needed to get Qubes (or Fedora) to boot, otherwise Qubes install USB stick will reboot right after boot selector screen and not continue install.

Setting UEFI options to get Qubes install to boot
-------------------------------------------------

1.  Enable Legacy USB mode
2.  Disable all Secure Boot and UEFI options, but leave this enabled: Config / USB / USB UEFI BIOS SUPPORT
3.  Save settings and reboot
5.  Install Qubes

... and now enjoy :) These settings may be needed also in other UEFI computers.
