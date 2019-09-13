---
layout: doc
title: Managing VM kernel
redirect_from:
- /doc/managing-vm-kernel/
- /en/doc/managing-vm-kernel/
---

VM kernel managed by dom0
=========================

By default, VMs kernels are provided by dom0.
(See [here][dom0-kernel-upgrade] for information about upgrading kernels in dom0.)
This means that:

1. You can select the kernel version (using GUI VM Settings tool or `qvm-prefs` commandline tool);
2. You can modify kernel options (using `qvm-prefs` commandline tool);
3. You can **not** modify any of the above from inside a VM;
4. Installing additional kernel modules is cumbersome.

*Note* In the examples below, although the specific version numbers might be old, the commands have been verified on R3.2 and R4.0 with debian-9 and fedora-26 templates.

To select which kernel a given VM will use, you can either use Qubes Manager (VM settings, advanced tab), or the `qvm-prefs` tool:

~~~
[user@dom0 ~]$ qvm-prefs -s my-appvm kernel
Missing kernel version argument!
Possible values:
1) default
2) none (kernels subdir in VM)
3) <kernel version>, one of:
  - 3.18.16-3
  - 3.18.17-4
  - 3.19.fc20
  - 3.18.10-2
[user@dom0 ~]$ qvm-prefs -s my-appvm kernel 3.18.17-4
[user@dom0 ~]$ qvm-prefs -s my-appvm kernel default
~~~

To check/change the default kernel you can either go to "Global settings" in Qubes Manager, or use the `qubes-prefs` tool:

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

To view kernel options, you can use the GUI VM Settings tool; to view and change them, use `qvm-prefs` commandline tool:

~~~
[user@dom0 ~]$ qvm-prefs -g work kernelopts
nopat
[user@dom0 ~]$ qvm-prefs -s work kernelopts "nopat apparmor=1 security=apparmor"
~~~

Installing different kernel using Qubes kernel package
----------------------------------

VM kernels are packages by Qubes team in `kernel-qubes-vm` packages.
Generally, the system will keep the three newest available versions.
You can list them with the `rpm` command:

~~~
[user@dom0 ~]$ rpm -qa 'kernel-qubes-vm*'
kernel-qubes-vm-3.18.10-2.pvops.qubes.x86_64
kernel-qubes-vm-3.18.16-3.pvops.qubes.x86_64
kernel-qubes-vm-3.18.17-4.pvops.qubes.x86_64
~~~

If you want a more recent version, you can check the `qubes-dom0-unstable` repository.
There is also the `kernel-latest-qubes-vm` package which should provide a more recent (non-LTS) kernel, but has received much less testing.
As the names suggest, keep in mind that those packages may be less stable than the default ones.

To check available versions in the `qubes-dom0-unstable` repository:

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

Installing a new version from `qubes-dom0-unstable` repository:

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
[user@dom0 ~]$
~~~

In the above example, it tries to remove the 3.18.10-2.pvops.qubes kernel (to keep only three installed), but since some VM uses it, it fails.
Installation of the new package is unaffected by this event.

The newly installed package is set as the default VM kernel.

Installing different VM kernel based on dom0 kernel
---------------------------------------------------

It is possible to package a kernel installed in dom0 as a VM kernel.
This makes it possible to use a VM kernel which is not packaged by Qubes team.
This includes:
 * using a Fedora kernel package
 * using a manually compiled kernel

To prepare such a VM kernel, you need to install the `qubes-kernel-vm-support` package in dom0 and also have matching kernel headers installed (`kernel-devel` package in the case of a Fedora kernel package).
You can install requirements using `qubes-dom0-update`:

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

Then you can call the `qubes-prepare-vm-kernel` tool to actually package the kernel.
The first parameter is kernel version (exactly as seen by the kernel), the second one (optional) is short name.
This is visible in Qubes Manager and the `qvm-prefs` tool.

~~~
[user@dom0 ~]$ sudo qubes-prepare-vm-kernel 4.1.9-6.pvops.qubes.x86_64 4.1.qubes
--> Building files for 4.1.9-6.pvops.qubes.x86_64 in /var/lib/qubes/vm-kernels/4.1.qubes
---> Recompiling kernel module (u2mfn)
---> Generating modules.img
mke2fs 1.42.12 (29-Aug-2014)
---> Generating initramfs
--> Done.
~~~

Kernel files structure
-----------------------

Kernel for a VM is stored in `/var/lib/qubes/vm-kernels/KERNEL_VERSION` directory (`KERNEL_VERSION` replaced with actual version). Qubes 4.x supports the following files there:

- `vmlinuz` - kernel binary (may not be a Linux kernel)
- `initramfs` - initramfs for the kernel to load
- `modules.img` - ext4 filesystem image containing Linux kernel modules (to be mounted at `/lib/modules`); additionally it should contain a copy of `vmlinuz` and `initramfs` in its root directory (for loading by qemu inside stubdomain)
- `default-kernelopts-common.txt` - default kernel options, in addition to those specified with `kernelopts` qube property (can be disabled with `no-default-kernelopts` feature)

All the files besides `vmlinuz` are optional.

Using kernel installed in the VM
--------------------------------

Both debian-9 and fedora-26 templates already have grub and related tools preinstalled so if you want to use one of the distribution kernels, all you need to do is clone either template to a new one, then:

~~~
qvm-prefs <clonetemplatename> virt_mode hvm
qvm-prefs <clonetemplatename> kernel ''
~~~

If you'd like to use a different kernel than default, continue reading.

### Installing kernel in Fedora VM

Install whatever kernel you want.
You need to also ensure you have the `kernel-devel` package for the same kernel version installed.

If you are using a distribution kernel package (`kernel` package), the initramfs and kernel modules may be handled automatically. 
If you are using a manually built kernel, you need to handle this on your own.
Take a look at the `dkms` documentation, especially the `dkms autoinstall` command may be useful.
If you did not see the `kernel` install rebuild your initramfs, or are using a manually built kernel, you will need to rebuild it yourself.
Replace the version numbers in the example below with the ones appropriate to the kernel you are installing:

~~~
sudo dracut -f /boot/initramfs-4.15.14-200.fc26.x86_64.img 4.15.14-200.fc26.x86_64
~~~

Once the kernel is installed, you need to create a GRUB configuration. 
You may want to adjust some settings in `/etc/default/grub`; for example, lower `GRUB_TIMEOUT` to speed up VM startup. 
Then, you need to generate the actual configuration:
In Fedora it can be done using the `grub2-mkconfig` tool:

~~~
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
~~~

You can safely ignore this error message:

~~~
grub2-probe: error: cannot find a GRUB drive for /dev/mapper/dmroot. Check your device.map
~~~

Then shutdown the VM.

**Note:** You may also use `PV` mode instead of `HVM` but this is not recommended for security purposes.
If you require `PV` mode, install `grub2-xen` in dom0 and change the template's kernel to `pvgrub2`.
Booting to a kernel inside the template is not supported under `PVH`.

### Installing kernel in Debian VM

Install whatever kernel you want, making sure to include the headers.
If you are using a distribution kernel package (`linux-image-amd64` package), the initramfs and kernel modules should be handled automatically.
If not, or you are building the kernel manually, do this using `dkms` and `initramfs-tools`:

    sudo dkms autoinstall -k <kernel-version> # replace this <kernel-version> with actual kernel version
    sudo update-initramfs -u

The output should look like this:

	$ sudo dkms autoinstall -k 3.16.0-4-amd64

	u2mfn:
	Running module version sanity check.
	 - Original module
	   - No original module exists within this kernel
	 - Installation
	   - Installing to /lib/modules/3.16.0-4-amd64/updates/dkms/

	depmod....

	DKMS: install completed.
	$ sudo update-initramfs -u
	update-initramfs: Generating /boot/initrd.img-3.16.0-4-amd64

When the kernel is installed, you need to create a GRUB configuration. 
You may want to adjust some settings in `/etc/default/grub`; for example, lower `GRUB_TIMEOUT` to speed up VM startup.
Then, you need to generate the actual configuration with the `update-grub2` tool:

~~~
sudo mkdir /boot/grub
sudo update-grub2
~~~

You can safely ignore this error message:

~~~
grub2-probe: error: cannot find a GRUB drive for /dev/mapper/dmroot. Check your device.map
~~~

Then shutdown the VM.

**Note:** You may also use `PV` mode instead of `HVM` but this is not recommended for security purposes.
If you require `PV` mode, install `grub2-xen` in dom0 and change the template's kernel to `pvgrub2`.
Booting to a kernel inside the template is not supported under `PVH`.

### Troubleshooting

In case of problems, you can access the VM console using `sudo xl console VMNAME` in dom0, then access the GRUB menu.
You need to call it just after starting the VM (until `GRUB_TIMEOUT` expires); for example, in a separate dom0 terminal window.

In any case you can later access the VM's logs (especially the VM console log `/var/log/xen/console/guest-VMNAME.log`).

You can always set the kernel back to some dom0-provided value to fix a VM kernel installation.


[dom0-kernel-upgrade]: /doc/software-update-dom0/#kernel-upgrade

