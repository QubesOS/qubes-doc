---
layout: doc
permalink: /doc/hardware-troubleshooting/
redirect_from:
- /doc/newer-hardware-troubleshooting/
title: Hardware Troubleshooting
---

# Troubleshooting hardware-related issues

## Audio doesn't work / Troubleshooting newer hardware

By default, the kernel that is installed in dom0 comes from the `kernel` package, which is an older Linux LTS kernel.
For most cases this works fine since the Linux kernel developers backport fixes to this kernel, but for some newer hardware, you may run into issues.
For example, the audio might not work if the sound card is too new for the LTS kernel.
To fix this, you can try the `kernel-latest` package -- though be aware that it's less tested!
(See [here][dom0-kernel-upgrade] for more information about upgrading kernels in dom0).
In dom0:

~~~
sudo qubes-dom0-update kernel-latest
~~~

Reboot when it's done installing.
You can double-check that the boot used the newer kernel with `uname -r`, which prints the version of the currently-running kernel.
Compare this with the output of `rpm -q kernel`.
If the start of `uname -r` matches one of the versions printed by `rpm`, then you're still using the Linux LTS kernel, and you'll probably need to manually fix your boot settings.
If `uname -r` reports a higher version number, then you've successfully booted with the kernel shipped by `kernel-latest`.

## "Unsupported Hardware Detected" error

See [Installation Troubleshooting](/doc/installation-troubleshooting/#unsupported-hardware-detected-error).

## Keyboard layout settings not behaving correctly

The best approach is to choose the right keyboard layout during the installation process.
But if you want to change things afterwards, you can try this workaround.

Assuming XFCE desktop: in `Q` → `System Tools` → `Keyboard` → `Layout`, leave the checkbox "`Use system defaults`" checked. Do not customize the keyboard layout here.

Set the system-wide layout and options for `xorg` with the `localectl` command in `dom0`. You can use `localectl --help` as a starting point.

Example: `localectl set-x11-keymap us dell ,qwerty compose:caps`.

This generates the appropriate configuration in `/etc/X11/xorg.conf.d/00-keyboard.conf`.
This file is auto-generated.
Do not edit it by hand, unless you know what you are doing.

Restarting `xorg` is required.
The most straightforward way is to reboot the system.

More information in [this discussion][layout_discussion] and [this GitHub issue][layout_issue].


[dom0-kernel-upgrade]: /doc/software-update-dom0/#kernel-upgrade
[hardware-reqs]: /doc/installation-guide/#hardware-requirements
[layout_discussion]: https://groups.google.com/d/topic/qubes-devel/d8ZQ_62asKI/discussion
[layout_issue]: https://github.com/QubesOS/qubes-issues/issues/1396
