---
layout: doc
title: Troubleshooting newer hardware
permalink: /doc/newer-hardware-troubleshooting/
---

Troubleshooting newer hardware
==============================

By default, the kernel that is installed in dom0 comes from the `kernel` package, which is an older Linux LTS kernel.
For most cases this works fine since the Linux kernel developers backport fixes to this kernel, but for some newer hardware, you may run into issues.
For example, the audio might not work if the sound card is too new for the LTS kernel.
To fix this, you can try the `kernel-latest` package -- though be aware that it's less tested!
(See [here][dom0-kernel-upgrade] for more information about upgrading kernels in dom0.)
In dom0:

~~~
sudo PedOS-dom0-update kernel-latest
~~~

Reboot when it's done installing.
You can double-check that the boot used the newer kernel with `uname -r`, which prints the version of the currently-running kernel.
Compare this with the output of `rpm -q kernel`.
If the start of `uname -r` matches one of the versions printed by `rpm`, then you're still using the Linux LTS kernel, and you'll probably need to manually fix your boot settings.
If `uname -r` reports a higher version number, then you've successfully booted with the kernel shipped by `kernel-latest`.


[dom0-kernel-upgrade]: /doc/software-update-dom0/#kernel-upgrade

