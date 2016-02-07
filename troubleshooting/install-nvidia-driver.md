---
layout: doc
title: How to Install an Nvidia Driver
permalink: /doc/install-nvidia-driver/
redirect_from:
- /en/doc/install-nvidia-driver/
- /doc/InstallNvidiaDriver/
- /wiki/InstallNvidiaDriver/
---

#Nvidia proprietary driver installation

You can use rpm packages from rpmfusion, or you can build the driver yourself.

##RpmFusion packages

There are rpm packages with all necessary software on rpmfusion. The only package you have to compile is the kernel module (but there is a ready built src.rpm package).

###Download packages

You will need any Fedora 18 system to download and build packages. You can use Qubes AppVM for it, but it isn't necessary. To download packages from rpmfusion - add this repository to your yum configuration (instructions are on their website). Then download packages using yumdownloader:

~~~
yumdownloader --resolve xorg-x11-drv-nvidia
yumdownloader --source nvidia-kmod
~~~

###Build kernel package

You will need at least kernel-devel (matching your Qubes dom0 kernel), rpmbuild tool and kmodtool, and then you can use it to build package:

~~~
yum install kernel-devel rpm-build kmodtool
rpmbuild --nodeps -D "kernels `uname -r`" --rebuild nvidia-kmod-260.19.36-1.fc13.3.src.rpm
~~~

In above command replace `uname -r` with kernel version from your Qubes dom0. If everything went right, you have now complete packages with nvidia drivers for Qubes system. Transfer them to dom0 (e.g. using a USB stick) and install (using standard "yum install /path/to/file"). 

Then you need to disable nouveau (normally it is done by install scripts from nvidia package, but unfortunately it isn't compatible with Qubes...):

Edit /etc/default/grub:

    ~~~
    GRUB_CMDLINE_LINUX="quiet rhgb nouveau.modeset=0 rd.driver.blacklist=nouveau video=vesa:off"
    ~~~

Regenerate grub configuration:

    ~~~
    grub2-mkconfig -o /boot/grub2/grub.cfg
    ~~~

Reboot.



##Manual installation

This process is quite complicated: First - download the source from nvidia.com site. Here "NVIDIA-Linux-x86\_64-260.19.44.run" is used. Copy it to dom0. Every next step is done in dom0.

See [this page](/doc/copy-to-dom0/) for instructions on how to transfer files to Dom0 (where there is normally no networking).

**WARNING**: Nvidia doesn't sign their files. To make it worse, you are forced to download them over a plaintext connection. This means there are virtually dozens of possibilities for somebody to modify this file and provide you with a malicious/backdoored file. You should realize that installing untrusted files into your Dom0 is a bad idea. Perhaps it might be a better idea to just get a new laptop with integrated Intel GPU? You have been warned.



###Userspace components

Install libraries, Xorg driver, configuration utilities. This can by done by nvidia-installer:

~~~
./NVIDIA-Linux-x86_64-260.19.44.run --ui=none --no-x-check --keep --no-nouveau-check --no-kernel-module
~~~

###Kernel module

You will need:

-   nvidia kernel module sources (left from previous step)
-   kernel-devel package installed
-   gcc, make, etc

This installation must be done manually, because nvidia-installer refused to install it on Xen kernel. Firstly ensure that kernel-devel package installed all needed files. This should consists of:

-   */usr/src/kernels/2.6.34.1-12.xenlinux.qubes.x86\_64*
-   */lib/modules/2.6.34.1-12.xenlinux.qubes.x86\_64/build* symlinked to the above directory
-   */usr/src/kernels/2.6.34.1-12.xenlinux.qubes.x86\_64/arch/x64/include/mach-xen* should be present (if not - take it from kernel sources)

If all the files are not there correct the errors manually. To build kernel module, enter *NVIDIA-Linux-x86\_64-260.19.44/kernel* directory and execute:

~~~
make
IGNORE_XEN_PRESENCE=1 CC="gcc -DNV_VMAP_4_PRESENT -DNV_SIGNAL_STRUCT_RLIM" make -f Makefile.kbuild
mv /lib/modules/2.6.34.1-12.xenlinux.qubes.x86_64/kernel/drivers/video/nvidia.ko /lib/modules/2.6.34.1-12.xenlinux.qubes.x86_64/extra/
~~~

Ignore any errors while inserting nvidia.ko (at the end of make phase). 

###Disable nouveau:

~~~
cat /etc/modprobe.d/nouveau-disable.conf
# blacklist isn't enough...
install nouveau /bin/true
~~~

Add *rdblacklist=nouveau* option to /boot/grub/menu.lst (at the end of line containing *vmlinuz*).

###Configure Xorg

After all, you should configure Xorg to use nvidia driver. You can use *nvidia-xconfig* or do it manually:

~~~
X -configure
mv /root/xorg.conf.new /etc/X11/xorg.conf
# replace Driver in Device section by "nvidia"
~~~



Now you should reboot the system.
