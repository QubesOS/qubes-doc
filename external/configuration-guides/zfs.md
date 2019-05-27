---
layout: doc
title: ZFS
permalink: /doc/zfs/
redirect_from:
- /en/doc/zfs/
- /doc/ZFS/
- /wiki/ZFS/
---

ZFS in Qubes
============

**Use at your own risk**!

Beware: Dragons might eat your precious data!

Install ZFS in Dom0
===================

Install DKMS style packages for Fedora <sup>(defunct in 0.6.2 due to spl/issues/284)</sup>
----------------------------------------------------------------------------------------------------

Fetch and install repository for DKMS style packages for your Dom0 Fedora version [http://zfsonlinux.org/fedora.html](http://zfsonlinux.org/fedora.html):

~~~
disp1# wget http://archive.zfsonlinux.org/fedora/zfs-release-1-1$(rpm -E %dist).noarch.rpm
dom0# qvm-run --pass-io disp1 'cat /home/user/zfs-release-1-1.fc18.noarch.rpm' > /home/user/zfs-release-1-1.fc18.noarch.rpm
dom0# sudo yum localinstall /home/user/zfs-release-1-1.fc18.noarch.rpm
dom0# sudo sed -i 's/$releasever/18/g' /etc/yum.repo.d/zfs.repo
dom0# sudo qubes-dom0-update @development-tools
dom0# sudo qubes-dom0-update zfs
~~~

Install DKMS style packages from git-repository
-----------------------------------------------

Build and install your DKMS or KMOD packages as described in [http://zfsonlinux.org/generic-rpm.html](http://zfsonlinux.org/generic-rpm.html).

### Prerequisites steps in AppVM <sup>(i.e. disp1)</sup>

Checkout repositories for SPL and ZFS:

~~~
mkdir ~/repositories && cd ~/repositories
git clone https://github.com/zfsonlinux/spl.git
git clone https://github.com/zfsonlinux/zfs.git
~~~

Revert changes in SPL repository due to this bug: [https://github.com/zfsonlinux/spl/issues/284](https://github.com/zfsonlinux/spl/issues/284)

~~~
cd ~/repositories/spl
git config --global user.email "user@example.com"
git config --global user.name "user"
git revert e3c4d44886a8564e84aa697477b0e37211d634cd
~~~

### Installation steps in Dom0

Copy repositories over to Dom0:

~~~
mkdir ~/repositories
qvm-run --pass-io disp1 'tar -cf - -C ~/repositories/ {spl,zfs}' | tar -xpf - -C ~/repositories/
~~~

Installing build requirements for SPL and ZFS DKMS modules:

~~~
sudo qubes-dom0-update dkms kernel-devel zlib-devel libuuid-devel libblkid-devel lsscsi bc autoconf automake binutils bison flex gcc gcc-c++ gdb gettext libtool make pkgconfig redhat-rpm-config rpm-build strace 
~~~

Configure and build SPL DKMS packages:

~~~
cd ~/repositories/spl
./autogen.sh
./configure --with-config=user
make rpm-utils rpm-dkms
~~~

Configure and build ZFS DKMS packages:

~~~
cd ~/repositories/zfs
./autogen.sh
./configure --with-config=user
make rpm-utils rpm-dkms
~~~

Install SPL and ZFS packages (i.e. version 0.6.2):

~~~
sudo yum localinstall \
    ~/repositories/spl/spl-0.6.2-1.qbs2.x86_64.rpm \
    ~/repositories/spl/spl-dkms-0.6.2-1.qbs2.noarch.rpm \
    ~/repositories/zfs/zfs-0.6.2-1.qbs2.x86_64.rpm \
    ~/repositories/zfs/zfs-dkms-0.6.2-1.qbs2.noarch.rpm \
    ~/repositories/zfs/zfs-dracut-0.6.2-1.qbs2.x86_64.rpm \
    ~/repositories/zfs/zfs-test-0.6.2-1.qbs2.x86_64.rpm
~~~

Configure ZFS
=============

Automatically load modules
--------------------------

/etc/sysconfig/modules/zfs.modules

~~~
#!/bin/sh

for module in spl zfs; do
    modprobe ${module} >/dev/null 2>&1
done
~~~

Make this file executable.

Tuning
------

Tame the memory-eating dragon (i.e. 512 Mb zfs\_arc\_max):

/etc/modprobe.d/zfs.conf

~~~
options zfs zfs_arc_max=536870912
~~~

Setup a zpool with ZFS datasets
-------------------------------

You can create a ZFS dataset for each AppVM, ServiceVM, HVM or TemplateVM or just use a pool as your backup location.

Move your existing directory to a temporary location, or the ZFS mount will overlay your directory.

Beware: VMs on a ZFS dataset aren't working, if your ZFS installation deserts you.

So keep netvm, firewallvm and your templates on your root file-system (preferably on a SSD).

~~~
zpool create -m none -o ashift=12 -O atime=off -O compression=lz4 qubes mirror /dev/mapper/<cryptname1> /dev/mapper/<cryptname2>
zfs create -p qubes/appvms
zfs create -m /var/lib/qubes/backup-zfs qubes/backup
zfs create -m /var/lib/qubes/appvms/banking qubes/appvms/banking
zfs create -m /var/lib/qubes/appvms/personal qubes/appvms/personal
zfs create -m /var/lib/qubes/appvms/untrusted qubes/appvms/untrusted
zfs create -m /var/lib/qubes/appvms/work qubes/appvms/work
~~~

Have fun with zpool and zfs.

Tips and Hints
==============

Backup your data
----------------

You're depending on an huge amount of code for this file system, keep this in mind and backup your precious data.

Encrypt underlying devices
--------------------------

~~~
dom0# cryptsetup -c aes-xts-plain64 luksFormat <device1>
dom0# cryptsetup luksOpen <device1> <cryptname1>
~~~

With the use of cryptsetup a keyfile can be specified to decrypt devices.

~~~
dom0# head -c 256 /dev/random > /root/keyfile1
dom0# chmod 0400 /root/keyfile1
dom0# cryptsetup luksAddKey <device1> /root/keyfile1
~~~

Decrypt devices on boot
-----------------------

Add your devices to /etc/crypttab.

~~~
<cryptname1> <device1> <keyfile1>
<cryptname2> <device2> none
~~~

Specifying a keyfile is especially useful, if ZFS should be ready during boot.

Further Reading
---------------

-   [http://www.open-zfs.org](http://www.open-zfs.org)
-   [http://zfsonlinux.org](http://zfsonlinux.org)

