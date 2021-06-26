---
lang: en
layout: doc
permalink: /doc/skip-qubes-autostart/
title: Skip Qubes OS autostart
---

The following instructions are valid for Qubes OS R4.0 *legacy mode* only and Qubes OS R4.1 *legacy* and *UEFI* modes. For Qubes OS R4.0 in UEFI mode, we don't have GRUB so manual boot from another operating system is needed.

In several cases, it is needed to prevent `autostart=True` for qubes on boot. For example:

* `sys-usb` was enabled but the only keyboard is on USB and qubes.InputKeyboard service is disabled,
* Some PCI device assigned to autostart VM crashes the system (e.g. GPU or RAID controller cards).

For that, there exists `qubes.skip_autostart` option on kernel command line. In order to use it, at the grub boot menu,

[![grub1.png](/attachment/doc/grub1.png)](/attachment/doc/grub1.png)

press `e` on the first entry (or any of your usual/custom entry). Then, press down key multiple times to reach the line starting by `module2`.

[![grub2.png](/attachment/doc/grub2.png)](/attachment/doc/grub2.png)

Append to the end of this line (generally after `rhgb quiet` options) `qubes.skip_autostart`

[![grub3.png](/attachment/doc/grub3.png)](/attachment/doc/grub3.png)

and press `Control-x` to boot the edited GRUB entry. The boot proceeds as usual with LUKS password prompt and then boot only the Qubes services without starting any qube.
