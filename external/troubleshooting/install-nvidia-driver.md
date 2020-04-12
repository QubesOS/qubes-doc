---
layout: doc
title: How to Install an Nvidia Driver
permalink: /doc/install-nvidia-driver/
redirect_from:
- /en/doc/install-nvidia-driver/
- /doc/InstallNvidiaDriver/
- /wiki/InstallNvidiaDriver/
---

# Nvidia proprietary driver installation

You can use rpm packages from rpmfusion, or you can build the driver yourself.

## Word of Caution 

Proprietary (NVIDIA/AMD) drivers are known to be sometimes highly problematic, or completely unsupported. 
Radeon driver support is prebaked in the Qubes kernel (v4.4.14-11) but only versions 4000-9000 give or take.
Support for newer cards is limited until AMDGPU support in the 4.5+ kernel, which isn't released yet for Qubes. 

Built in Intel graphics, Radeon graphics (between that 4000-9000 range), and perhaps some prebaked NVIDIA card support that I don't know about. Those are your best bet for great Qubes support.

If you do happen to get proprietary drivers working on your Qubes system (via installing them), please take the time to go to the 
[Hardware Compatibility List (HCL)](/doc/hcl/#generating-and-submitting-new-reports )
Add your computer, graphics card, and installation steps you did to get everything working.

Before continuing, you may wish to try the `kernel-latest` package from the `current` repository. This kernel may better support your card and if so, you would not have to rely on proprietary drivers. This can be installed from dom0 with:
~~~
sudo qubes-dom0-update kernel-latest
~~~

## RpmFusion packages

There are rpm packages with all necessary software on rpmfusion. The only package you have to compile is the kernel module (but there is a ready built src.rpm package).

### Download packages

You will need any Fedora 18 system to download and build packages. You can use Qubes AppVM for it, but it isn't necessary. To download packages from rpmfusion - add this repository to your yum configuration (instructions are on their website). Then download packages using yumdownloader:

~~~
yumdownloader --resolve xorg-x11-drv-nvidia
yumdownloader --source nvidia-kmod
~~~

### Build kernel package

You will need at least kernel-devel (matching your Qubes dom0 kernel), rpmbuild tool and kmodtool, and then you can use it to build the package:

~~~
yum install kernel-devel rpm-build kmodtool
rpmbuild --nodeps -D "kernels `uname -r`" --rebuild nvidia-kmod-260.19.36-1.fc13.3.src.rpm
~~~

In the above command, replace `uname -r` with kernel version from your Qubes dom0. If everything went right, you have now complete packages with nvidia drivers for the Qubes system. Transfer them to dom0 (e.g. using a USB stick) and install (using standard "yum install /path/to/file").

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



## Manual installation

This process is quite complicated: First - download the source from nvidia.com site. Here "NVIDIA-Linux-x86\_64-260.19.44.run" is used. Copy it to dom0. Every next step is done in dom0.

See [this page](/doc/copy-to-dom0/) for instructions on how to transfer files to Dom0 (where there is normally no networking).

**WARNING**: Nvidia doesn't sign their files. To make it worse, you are forced to download them over a plaintext connection. This means there are virtually dozens of possibilities for somebody to modify this file and provide you with a malicious/backdoored file. You should realize that installing untrusted files into your Dom0 is a bad idea. Perhaps it might be a better idea to just get a new laptop with integrated Intel GPU? You have been warned.



### Userspace components

Install libraries, Xorg driver, configuration utilities. This can by done by nvidia-installer:

~~~
./NVIDIA-Linux-x86_64-260.19.44.run --ui=none --no-x-check --keep --no-nouveau-check --no-kernel-module
~~~

### Kernel module

You will need:

-   nvidia kernel module sources (left from previous step)
-   kernel-devel package installed
-   gcc, make, etc

This installation must be done manually, because nvidia-installer refused to install it on Xen kernel. Firstly ensure that kernel-devel package installed all needed files. This should consist of:

-   */usr/src/kernels/2.6.34.1-12.xenlinux.qubes.x86\_64*
-   */lib/modules/2.6.34.1-12.xenlinux.qubes.x86\_64/build* symlinked to the above directory
-   */usr/src/kernels/2.6.34.1-12.xenlinux.qubes.x86\_64/arch/x64/include/mach-xen* should be present (if not - take it from kernel sources)

If all the files are not there correct the errors manually. To build the kernel module, enter *NVIDIA-Linux-x86\_64-260.19.44/kernel* directory and execute:

~~~
make
IGNORE_XEN_PRESENCE=1 CC="gcc -DNV_VMAP_4_PRESENT -DNV_SIGNAL_STRUCT_RLIM" make -f Makefile.kbuild
mv /lib/modules/2.6.34.1-12.xenlinux.qubes.x86_64/kernel/drivers/video/nvidia.ko /lib/modules/2.6.34.1-12.xenlinux.qubes.x86_64/extra/
~~~

Ignore any errors while inserting nvidia.ko (at the end of make phase). 

### Disable nouveau:

~~~
cat /etc/modprobe.d/nouveau-disable.conf
# blacklist isn't enough...
install nouveau /bin/true
~~~

Add *rdblacklist=nouveau* option to /boot/grub/menu.lst (at the end of line containing *vmlinuz*).

### Configure Xorg

Finally, you should configure Xorg to use nvidia driver. You can use *nvidia-xconfig* or do it manually:

~~~
X -configure
mv /root/xorg.conf.new /etc/X11/xorg.conf
# replace Driver in Device section by "nvidia"
~~~

Reboot to verify all this works.

# Troubleshooting lack of video output during installation

Specifically, the notes below are aimed to help when the GRUB menu shows up fine, the installation environment starts loading, and then the display(s) go into standby mode. This is, typically, related to some sort of an issue with the kernel's KMS/video card modules.

## Initial setup.
*Note*: The steps below do *not* produce a fully-functional Qubes OS install. Rather, only a dom0 instance is functional, and there is no networking there. However, they can be used to gather data in order to troubleshoot video card issues and/or possible other basic kernel module issues.

1. Append `nomodeset ip=dhcp inst.nokill inst.vnc` to the kernel command line. Remove `rhgb` and `quiet` to see the kernel messages scroll by, which may help in further diagnostics.
   * If DHCP is not available on the installation network, the syntax becomes a bit more involved. The full list of variants is documented in the [Dracut Command-line parameters] (http://man7.org/linux/man-pages/man7/dracut.cmdline.7.html)
2. The VGA console should switch into the installer's multi-virtual-terminal display. VNC may take a number of minutes to start, please be patient.
   * Using the anaconda installer interface, switch to the "shell" TTY (ALT-F2), and use `ip a` command to display the IP addresses.
3. Using the Connect to the IP (remember the :1) using a VNC viewer.
4. Follow the installation UI. 
   * Since this won't be a usable install, skipping LUKS encryption is an option which will simplify this troubleshooting process.
   * Do *not* reboot at the end of the installation.
5. Once the installation completes, use the local VGA console switch to TTY2 via ALT-F2
   * Switch to the chroot of the newly-installed system via `chroot /mnt/sysinstall`
   * Set the root password (this will also enable the root account login)
   * Double-check that `/boot/grub2/grub.cfg` contains a `nomodeset` kernel parameter.
   * Exit out of the chroot environment (`exit` or CTRL-D)
6. Reboot

*Note* If the kernel parameters do *not* include `quiet` and `rhgb`, the kernel messages can easily obscure the LUKS passphrase prompt. Additionally, each character entered will cause the LUKS passphrase prompt to repeat onto next line. Both of these are cosmetic. The trade-off between kernel messages and the easy-to-spot LUKS passphrase prompt is left as an exercise to the user.

## Gather initial `dmesg` output
If all is well, the newly-installed Qubes OS instance should allow for user root to log in. 
Run `dmesg > dmesg.nomodeset.out` to gather an initial dmesg output.

## Gather the 'video no worky' `dmesg` output
1. Reboot and interrupt the Grub2's process, modifying the kernel parameters to no longer contain `nomodeset`.
   * If the LUKS passphrase was set, blindly enter it.
2. Wait for the system to finish booting (about 5 minutes, typically).
3. Blindly switch to a TTY via CTRL-ALT-F2.
4. Blindly log in as user root
5. Blindly run `dmesg > dmesg.out`
6. Blindly run `reboot` (this will also serve to confirm that logging in as root, and running commands blindly is possible rather than, say, the kernel having hung or some such).
   * Should this step fail, perhaps by the time step #3 was undertaken, the OS hasn't finished coming up yet. Please retry, possibly with a different TTY (say, 3 or 4 - so CTRL-ALT-F3?)

## Exfiltrate the dmesg outputs
Allow the system to boot normally, log in as user root, and sneakernet the files off the system for analysis, review, bug logging, et cetera.
