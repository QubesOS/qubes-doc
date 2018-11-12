---
layout: doc
title: Troubleshooting newer hardware
permalink: /doc/newer-hardware-troubleshooting/
---

Troubleshooting newer hardware
==============================

By default, the kernel that is installed in dom0 is the kernel shipped by Fedora 25.
For most cases this works fine since the Qubes OS developers backport fixes to this kernel, but for some newer hardware, you may run into issues.
For example, the audio might not work if the sound card is too new for the Fedora 25 kernel.

To fix this, you can try the `kernel-latest` package - though be aware that it's less tested!
In dom0:

~~~
sudo qubes-dom0-update kernel-latest
~~~

Reboot when it's done installing.
You can double-check that the boot used the newer kernel with `uname -r`, which prints the version of the currently-running kernel.
If it says `4.14` at the beginning, then you're still using the Fedora 25 kernel, and you'll probably need to manually fix your boot settings.
If it reports a higher version number, then you've successfully booted with the kernel shipped by `kernel-latest`.
