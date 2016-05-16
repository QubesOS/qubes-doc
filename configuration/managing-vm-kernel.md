---
layout: doc
title: Managing VM kernel
permalink: /doc/managing-vm-kernel/
redirect_from:
- /en/doc/managing-vm-kernel/
---

VM kernel managed by dom0
-------------------------

By default VMs kernels are provided by dom0. This means that:

1. You can select kernel version in VM settings;
2. You can modify kernel options in VM settings;
3. You can **not** modify any of above from inside of VM;
4. Installing additional kernel modules is cumbersome.

To select which kernel a given VM will use, you can use either use Qubes Manager (VM settings, advanced tab), or `qvm-prefs` tool:

~~~
[user@dom0 ~]$ qvm-prefs my-appvm -s kernel
Missing kernel version argument!
Possible values:
1) default
2) none (kernels subdir in VM)
3) <kernel version>, one of:
  - 3.18.16-3
  - 3.18.17-4
  - 3.19.fc20
  - 3.18.10-2
[user@dom0 ~]$ qvm-prefs my-appvm -s kernel 3.18.17-4
[user@dom0 ~]$ qvm-prefs my-appvm -s kernel default
~~~

To check/change the default kernel you can go either to "Global settings" in Qubes Manager, or use `qubes-prefs` tool:

~~~
[user@dom0 ~]$ qubes-prefs
clockvm           : sys-net
default-fw-netvm  : sys-net
default-kernel    : 3.18.17-4
default-netvm     : sys-firewall
default-template  : fedora-21
updatevm          : sys-firewall
[user@dom0 ~]$ qubes-prefs -s default-kernel 3.19.fc20
~~~

Installing different kernel using Qubes kernel package
==================================

VM kernels are packages by Qubes team in `kernel-qubes-vm` packages. Generally system will keep the 3 newest available versions. You can list them with the `rpm` command:

~~~
[user@dom0 ~]$ rpm -qa 'kernel-qubes-vm*'
kernel-qubes-vm-3.18.10-2.pvops.qubes.x86_64
kernel-qubes-vm-3.18.16-3.pvops.qubes.x86_64
kernel-qubes-vm-3.18.17-4.pvops.qubes.x86_64
~~~

If you want more recent version, you can check `qubes-dom0-unstable` repository. As the name suggest, keep in
mind that those packages may be less stable than the default ones.

Checking available versions in `qubes-dom0-unstable` repository:

~~~
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-dom0-unstable --action=list kernel-qubes-vm
Using sys-firewall as UpdateVM to download updates for Dom0; this may take some time...
Running command on VM: 'sys-firewall'...
Loaded plugins: langpacks, post-transaction-actions, yum-qubes-hooks
Installed Packages
kernel-qubes-vm.x86_64      1000:3.18.10-2.pvops.qubes       installed
kernel-qubes-vm.x86_64      1000:3.18.16-3.pvops.qubes       installed
kernel-qubes-vm.x86_64      1000:3.18.17-4.pvops.qubes       installed
Available Packages
kernel-qubes-vm.x86_64      1000:4.1.12-6.pvops.qubes        qubes-dom0-unstable
No packages downloaded
Installed Packages
kernel-qubes-vm.x86_64 1000:3.18.10-2.pvops.qubes @anaconda/R3.0
kernel-qubes-vm.x86_64 1000:3.18.16-3.pvops.qubes @/kernel-qubes-vm-3.18.16-3.pvops.qubes.x86_64
kernel-qubes-vm.x86_64 1000:3.18.17-4.pvops.qubes @qubes-dom0-cached

~~~

Installing new version from `qubes-dom0-unstable` repository:

~~~
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-dom0-unstable kernel-qubes-vm
Using sys-firewall as UpdateVM to download updates for Dom0; this may take some time...
Running command on VM: 'sys-firewall'...
Loaded plugins: langpacks, post-transaction-actions, yum-qubes-hooks
Resolving Dependencies
(...)

===========================================================================================
 Package             Arch       Version                        Repository             Size
===========================================================================================
Installing:
 kernel-qubes-vm     x86_64     1000:4.1.12-6.pvops.qubes      qubes-dom0-cached      40 M
Removing:
 kernel-qubes-vm     x86_64     1000:3.18.10-2.pvops.qubes     @anaconda/R3.0        134 M

Transaction Summary
===========================================================================================
Install  1 Package
Remove   1 Package

Total download size: 40 M
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction (shutdown inhibited)
  Installing : 1000:kernel-qubes-vm-4.1.12-6.pvops.qubes.x86_64                        1/2
mke2fs 1.42.12 (29-Aug-2014)
This kernel version is used by at least one VM, cannot remove
error: %preun(kernel-qubes-vm-1000:3.18.10-2.pvops.qubes.x86_64) scriptlet failed, exit status 1
Error in PREUN scriptlet in rpm package 1000:kernel-qubes-vm-3.18.10-2.pvops.qubes.x86_64
  Verifying  : 1000:kernel-qubes-vm-4.1.12-6.pvops.qubes.x86_64                        1/2
  Verifying  : 1000:kernel-qubes-vm-3.18.10-2.pvops.qubes.x86_64                       2/2

Installed:
  kernel-qubes-vm.x86_64 1000:4.1.12-6.pvops.qubes

Failed:
  kernel-qubes-vm.x86_64 1000:3.18.10-2.pvops.qubes

Complete!
[marmarek@dom0 ~]$
~~~

In the above example, it tries to remove 3.18.10-2.pvops.qubes kernel (to keep only 3 installed), but since some VM uses it, it fails. Installation of new package is unaffected by this event.

The newly installed package is set as default VM kernel.

Installing different VM kernel based on dom0 kernel
===================================================

It is possible to package kernel installed in dom0 as VM kernel. This makes it
possible to use VM kernel, which is not packaged by Qubes team. This includes:
 * using Fedora kernel package
 * using manually compiled kernel

To prepare such VM kernel, you need to install `qubes-kernel-vm-support`
package in dom0 and also have matching kernel headers installed (`kernel-devel`
package in case of Fedora kernel package). You can install required stuff using `qubes-dom0-update`:

~~~
[user@dom0 ~]$ sudo qubes-dom0-update qubes-kernel-vm-support kernel-devel
Using sys-firewall as UpdateVM to download updates for Dom0; this may take some time...
Running command on VM: 'sys-firewall'...
Loaded plugins: langpacks, post-transaction-actions, yum-qubes-hooks
Package 1000:kernel-devel-4.1.9-6.pvops.qubes.x86_64 already installed and latest version
Resolving Dependencies
(...)

================================================================================
 Package                      Arch        Version        Repository        Size
================================================================================
Installing:
 qubes-kernel-vm-support      x86_64      3.1.2-1.fc20   qubes-dom0-cached 9.2 k

Transaction Summary
================================================================================
Install  1 Package

Total download size: 9.2 k
Installed size: 13 k
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction (shutdown inhibited)
  Installing : qubes-kernel-vm-support-3.1.2-1.fc20.x86_64                  1/1

Creating symlink /var/lib/dkms/u2mfn/3.1.2/source ->
                 /usr/src/u2mfn-3.1.2

DKMS: add completed.
  Verifying  : qubes-kernel-vm-support-3.1.2-1.fc20.x86_64                  1/1

Installed:
  qubes-kernel-vm-support.x86_64 0:3.1.2-1.fc20

Complete!
~~~

Then you can call `qubes-prepare-vm-kernel` tool to actually package the
kernel. The first parameter is kernel version (exactly as seen by the kernel),
the second one (optional) is short name being visible in Qubes Manager and
`qvm-prefs` tool.

~~~
[user@dom0 ~]$ sudo qubes-prepare-vm-kernel 4.1.9-6.pvops.qubes.x86_64 4.1.qubes
--> Building files for 4.1.9-6.pvops.qubes.x86_64 in /var/lib/qubes/vm-kernels/4.1.qubes
---> Recompiling kernel module (u2mfn)
---> Generating modules.img
mke2fs 1.42.12 (29-Aug-2014)
---> Generating initramfs
--> Done.
~~~

Using kernel installed in the VM
================================

**This option is available only in Qubes R3.1 or newer**

It is possible to use kernel installed in the VM (in most cases - TemplateVM).
This is possible thanks to PV GRUB2 - GRUB2 running in the VM. To make it happen, you need to:

1. Install PV GRUB2 in dom0 - package is named `grub2-xen`.
2. Install kernel in the VM. As with all VM software installation - this needs to be done in TemplateVM (of StandaloneVM if you are using one).
3. Set VM kernel to `pvgrub2` value. You can use `pvgrub2` in selected VMs, not necessary all of them, even when it's template has kernel installed. You can still use dom0-provided kernel for selected VMs.

**WARNING: When using kernel from within VM, `kernelopts` parameter is ignored.**

### Installing PV GRUB2

Simply execute:

~~~
sudo qubes-dom0-update grub2-xen
~~~

### Installing kernel in Fedora VM

In Fedora based VM, you need to install `qubes-kernel-vm-support` package. This
package include required additional kernel module and initramfs addition
required to start Qubes VM (for details see
[template implementation](/doc/template-implementation/)). Additionally you
need some GRUB tools to create it's configuration. Note: you don't need actual
grub bootloader as it is provided by dom0. But having one also shouldn't harm.

~~~
sudo yum install qubes-kernel-vm-support grub2-tools
~~~

Then install whatever kernel you want. If you are using distribution kernel
package (`kernel` package), initramfs and kernel module should be handled
automatically. If you are using manually build kernel, you need to handle this
on your own. Take a look at `dkms` and `dracut` documentation.

When kernel is installed, you need to create GRUB configuration. 
You may want to adjust some settings in `/etc/default/grub`, for example lower
`GRUB_TIMEOUT` to speed up VM startup. Then you need to generate actual configuration:
In Fedora it can be done using `grub2-mkconfig` tool:

~~~
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
~~~

You can safely ignore this error message:

~~~
grub2-probe: error: cannot find a GRUB drive for /dev/mapper/dmroot. Check your device.map
~~~

Then shutdown the VM. From now you can set `pvgrub2` as VM kernel and it will
start kernel configured within VM. 

### Installing kernel in Debian VM

In Debian based VM, you need to install `qubes-kernel-vm-support` package. This
package include required additional kernel module and initramfs addition
required to start Qubes VM (for details see
[template implementation](/doc/template-implementation/)). Additionally you
need some GRUB tools to create it's configuration. Note: you don't need actual
grub bootloader as it is provided by dom0. But having one also shouldn't harm.

~~~
sudo apt-get update
sudo apt-get install qubes-kernel-vm-support grub2-common
~~~

Ignore warnings about `version '...' has bad syntax`.

Then install whatever kernel you want. If you are using distribution kernel
package (`linux-image-amd64` package), initramfs and kernel module should be
handled automatically. If you are using manually build kernel, you need to
handle this on your own. Take a look at `dkms` and `initramfs-tools` documentation.

When kernel is installed, you need to create GRUB configuration. 
You may want to adjust some settings in `/etc/default/grub`, for example lower
`GRUB_TIMEOUT` to speed up VM startup. Then you need to generate actual configuration:
In Fedora it can be done using `update-grub2` tool:

~~~
sudo mkdir /boot/grub
sudo update-grub2
~~~

You can safely ignore this error message:

~~~
grub2-probe: error: cannot find a GRUB drive for /dev/mapper/dmroot. Check your device.map
~~~

Then shutdown the VM. From now you can set `pvgrub2` as VM kernel and it will
start kernel configured within VM. 

### Troubleshooting

In case of problems, you can access VM console (using `sudo xl console VMNAME` in dom0) to access
GRUB menu. You need to call it just after starting VM (until `GRUB_TIMEOUT`
expires) - for example in separate dom0 terminal window.

In any case you can later access VM logs (especially VM console log (`guest-VMNAME.log`). 

You can always set kernel back to some dom0-provided value to fix VM kernel installation.
