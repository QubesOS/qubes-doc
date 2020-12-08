---
layout: doc
title: Sony Vaio Tinkering
redirect_to: https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/sony-vaio-tinkering.md
redirect_from:
- /doc/sony-vaio-tinkering/
- /en/doc/sony-vaio-tinkering/
- /doc/SonyVaioTinkering/
- /wiki/SonyVaioTinkering/
---

Instructions for getting your Sony Vaio Z laptop working with Qubes/Linux
=========================================================================

The following issues were reported on Qubes 3.2 and may not be prevalent on Qubes 4.0. 

Graphics card does not work
---------------------------

Newer models of Sony Vaio Z come with an "intelligent" GPU switch, that automatically chooses either Intel Integrated GPU (IGD) or the discrete NVIDIA GPU. This confuses the Linux graphics so much, that in most cases, it won't even be able to install a regular Linux on such a machine. Unfortunately, moving the switch into the "Stamina" position apparently doesn't work, and the automatic GPU switching is still active.

One solution that actually worked for me was to reflash the BIOS (I know, I know, this is scary) and to enable the so called "Advanced Menu" in the BIOS. This Advanced Menu allows you to choose the desired behaviour of the GPU switch, which in our case would be to set it to "Static" and then move the mechanical switch to the "Stamina" position, that enabled the Intel IGD (which is much better supported on Linux).

If you think you are ready to reflash you BIOS, you can follow [these instructions](http://forum.notebookreview.com/sony/473226-insyde-hacking-new-vaio-z-advanced-menu-bios.html).

**WARNING**: We take absolutely no responsibility that the BIOS reflashing instructions given at the referenced forum are 1) valid, 2) non-malicious, and 3) work at all. Do this step at your own risk. Keep in mind that reflashing your BIOS might yield your system unusable. If you don't feel like taking this risk (which is a reasonable state of mind), look for a different notebook, or ask Sony Support to enable this option for you.

In practice I have downloaded the BIOS-patching tools, run them in a VM on a BIOS image I extracted from my laptop, diffed the two versions, and concluded that it doesn't *seem* malicious, and then bravely applied the patched image. If you don't know what are you doing, just get a different laptop, really!

On a side note, we should note that allowing anybody to reflash the BIOS is really a bad idea from a security point of view (Hello Evil Maids!). Shame on you, Sony!

Touchpad does not work during installation 
------------------------------------------

In order to get the touchpad working during installation you should pass the `i8042.nopnp=1` option to the kernel before the installer starts:

~~~
sudo nano /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="i8042.nopnp=1"
~~~

Applying other fixes
--------------------

There are a few more fixes needed for Sony Vaio Z, and we have prepared a special package that you can install in dom0 that applies them all. After the installation is complete, open a console in dom0 and do the following:

~~~
$ sudo bash
# qvm-dom0-networking up
# yum install qubes-core-dom0-vaio-fixes
# reboot
~~~

This script takes care about the following:

-   Setting i8042.nopnp for your installed system
-   Adding special option for the sound module (so you can get sound)
-   Adding pm-suspend scripts that take care about restoring your screen after resume

