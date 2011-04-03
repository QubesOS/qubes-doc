---
layout: wiki
title: InstallNvidiaDriver
permalink: /wiki/InstallNvidiaDriver/
---

Nvidia proprietary driver installation
======================================

The NVIDIA proprietary driver works **much** more stable than nouveau, so it's good idea to install it. But this is somehow complicated: First - download it from nvidia.com site. Here "NVIDIA-Linux-x86\_64-260.19.44.run" is used. Copy it to dom0. Every next step is done in dom0.

Userspace components
--------------------

Install libraries, Xorg driver, configuration utilities. This can by done by nvidia-installer:

``` {.wiki}
./NVIDIA-Linux-x86_64-260.19.44.run --ui=none --no-x-check --keep --no-nouveau-check
```

Kernel module
-------------

You will need:

-   nvidia kernel module sources (left from previous step)
-   kernel-devel package installed
-   gcc, make, etc

This installation must be done manually, because nvidia-installer refused to install it on Xen kernel. Firstly ensure that kernel-devel package installed all needed files. This should consists of:

-   */usr/src/kernels/2.6.34.1-12.xenlinux.qubes.x86\_64*
-   */lib/modules/2.6.34.1-12.xenlinux.qubes.x86\_64/build* symlinked to the above directory
-   */usr/src/kernels/2.6.34.1-12.xenlinux.qubes.x86\_64/arch/x64/include/mach-xen* should be present (if not - take it from kernel sources)

If it is not true - correct it manually. To build kernel module, enter *NVIDIA-Linux-x86\_64-260.19.44/kernel* directory and execute:

``` {.wiki}
IGNORE_XEN_PRESENCE=1 CC="gcc -DNV_VMAP_4_PRESENT -DNV_SIGNAL_STRUCT_RLIM" make -f Makefile.kbuild
mv /lib/modules/2.6.34.1-12.xenlinux.qubes.x86_64/kernel/drivers/video/nvidia.ko /lib/modules/2.6.34.1-12.xenlinux.qubes.x86_64/extra/
```

Ignore error while inserting nvidia.ko (at the end of make phase). Now you should disable nouveau:

``` {.wiki}
cat /etc/modprobe.d/nouveau-disable.conf
# blacklist isn't enough...
install nouveau /bin/true
```

Configure Xorg
--------------

After all, you should configure Xorg to use nvidia driver. You can use *nvidia-xconfig* or do it manually:

``` {.wiki}
X -configure
mv /root/xorg.conf.new /etc/X11/xorg.conf
# replace Driver in Device section by "nvidia"
```
