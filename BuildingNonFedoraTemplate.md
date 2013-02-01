---
layout: wiki
title: BuildingNonFedoraTemplate
permalink: /wiki/BuildingNonFedoraTemplate/
---

Building a TemplateVM for [ArchLinux?](/wiki/ArchLinux) (or another non fedora OS)
==================================================================================

If you don't like using Fedora because of specific administration or package management / building needs, you could build a VM Template for your Distribution of choice.

This article shows how to build a template for a different OS, taking [ArchLinux?](/wiki/ArchLinux) as an example.

Starting with HVM
-----------------

If no Qubes packages are available for your selected OS. You should start to install an HVM with your OS. Your goals will be:

-   to create required Qubes packages
-   to identify potential issue making all Qubes agents and scripts working correctly.

As soon as you manage to make qrexec and qubes-gui-agent working, it should be sufficient to start preparing a template VM.

### Xen libraries

Several XEN libraries are required for Qubes to work correctly. In fact, you need to make xenstore commands working before anything else. For this, Qubes git can be used as several patches have been selected by Qubes developpers that could impact the activity inside a VM. Start be retrieving a recent git and identify how you can build a package from it: `git clone git://git.qubes-os.org/marmarek/xen`

Find the .spec file in the git repository (this is the file being used to build rpm packages), and try to adapt it to your OS in order to build a package similar to the target 'xen-vm'. For example, a PKGBUILD has been created for [ArchLinux?](/wiki/ArchLinux) and can be found on [​http://aur.archlinux.org/packages/qu/qubes-vm-xen/PKGBUILD](http://aur.archlinux.org/packages/qu/qubes-vm-xen/PKGBUILD).

Don't be afraid with the complexity of the PKGBUILD, most of the code is almost a copy/paste of required sources and patches found in the .spec file provided in the git repository.

Note once the package has been successfully compiled and installed, you need to setup XEN filesystem. Add the folowing line to your fstab (you can create this line in your package install script): `xen                     /proc/xen               xenfs   defaults        0 0`

Now install the package you built and mount /proc/xen. Verify that xenstore-read works by running: `xenstore-read qubes_vm_type` That should give you the current VM type such as HVM or AppVM.

### Qubes-OS core agents (qrexec...)

[​https://aur.archlinux.org/packages/qu/qubes-vm-core/PKGBUILD](https://aur.archlinux.org/packages/qu/qubes-vm-core/PKGBUILD)

### Qubes-OS kernel modules

[​https://aur.archlinux.org/packages/qu/qubes-vm-kernel-modules/PKGBUILD](https://aur.archlinux.org/packages/qu/qubes-vm-kernel-modules/PKGBUILD)

### Qubes-OS gui agents

[​https://aur.archlinux.org/packages/qu/qubes-vm-gui/PKGBUILD](https://aur.archlinux.org/packages/qu/qubes-vm-gui/PKGBUILD)

Creating a template builder
---------------------------

### 00\_prepare.sh

``` {.wiki}
#!/bin/sh

echo "Downloading Archlinux dvd..."
wget -O "archlinux.iso" "http://mir.archlinux.fr/iso/latest/arch/x86_64/root-image.fs.sfs" --continue

echo "Extracting squash filesystem from DVD..."
mkdir archlinux_dvd
sudo mount -o loop archlinux.iso archlinux_dvd
cp archlinux_dvd/root-image.fs .
sudo umount archlinux_dvd
```

### 01\_install\_core.sh

``` {.wiki}
#!/bin/sh

echo "Mounting archlinux install system into archlinux_dvd..."
sudo mount root-image.fs archlinux_dvd

echo "Creating chroot bootstrap environment"

sudo mount --bind $INSTALLDIR archlinux_dvd/mnt
sudo cp /etc/resolv.conf archlinux_dvd/etc

echo "-> Initializing pacman keychain"
sudo ./archlinux_dvd/usr/bin/arch-chroot archlinux_dvd/ pacman-key --init
sudo ./archlinux_dvd/usr/bin/arch-chroot archlinux_dvd/ pacman-key --populate

echo "-> Installing core pacman packages..."
sudo ./archlinux_dvd/usr/bin/arch-chroot archlinux_dvd/ sh -c 'pacstrap /mnt base'

echo "-> Cleaning up bootstrap environment"
sudo umount archlinux_dvd/mnt

sudo umount archlinux_dvd

cp scripts_"${DIST}"/resolv.conf $INSTALLDIR/etc
```

### 02\_install\_groups.sh

``` {.wiki}
echo "Mounting archlinux install system into archlinux_dvd..."
sudo mount root-image.fs archlinux_dvd

echo "-> Installing archlinux package groups..."
echo "-> Selected packages:"
echo "$PKGGROUPS"
sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR pacman --needed --noconfirm -S $PKGGROUPS

sudo umount archlinux_dvd
```

### 04\_install\_qubes.sh

``` {.wiki}
#!/bin/sh

echo "Mounting archlinux install system into archlinux_dvd..."
sudo mount root-image.fs archlinux_dvd

echo $INSTALLDIR

echo "--> Installing yaourt..."
sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR sh -c 'cd tmp && wget https://aur.archlinux.org/packages/pa/package-query/package-query.tar.gz && tar xzvf package-query.tar.gz && cd package-query && makepkg --asroot && pacman --noconfirm -U package-query-*.pkg.tar.xz'
sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR sh -c 'cd tmp && wget https://aur.archlinux.org/packages/ya/yaourt/yaourt.tar.gz && tar xzvf yaourt.tar.gz && cd yaourt && makepkg --asroot && pacman --noconfirm -U yaourt-*.pkg.tar.xz'

echo "--> Preparing build environment inside the chroot..."
# Notes for qubes-vm-xen
# Note: we need more ram for /tmp (at least 700M of disk space for compiling XEN because of the sources...)
sudo sed 's:-t tmpfs -o mode=1777,strictatime,nodev,:-t tmpfs -o size=700M,mode=1777,strictatime,nodev,:' -i ./archlinux_dvd/usr/bin/arch-chroot

# Note: Enable x86 repos
su -c "echo '[multilib]' >> $INSTALLDIR/etc/pacman.conf"
su -c "echo 'SigLevel = PackageRequired' >> $INSTALLDIR/etc/pacman.conf"
su -c "echo 'Include = /etc/pacman.d/mirrorlist' >> $INSTALLDIR/etc/pacman.conf"
sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR sh -c "pacman -Sy"

echo "--> Compiling and installing qubes-packages..."
sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR sh -c "yaourt --noconfirm -S qubes-vm-xen"
sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR sh -c "yaourt --noconfirm -S qubes-vm-core"
sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR sh -c "yaourt --noconfirm -S qubes-vm-gui"

sudo umount archlinux_dvd
```

### 09\_cleanup.sh

``` {.wiki}
#!/bin/sh

echo "Mounting archlinux install system into archlinux_dvd..."
sudo mount root-image.fs archlinux_dvd

echo "--> Starting cleanup actions"
# Remove unused packages and their dependencies (make dependencies)
cleanuppkgs=`sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR pacman -Qdt | cut -d " " -f 1`
sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR pacman --noconfirm -Rsc $cleanuppkgs

# Remove yaourt dependencies
sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR pacman --noconfirm -Rsc binutils yajl gcc make

# Clean pacman cache
sudo ./archlinux_dvd/usr/bin/arch-chroot $INSTALLDIR pacman --noconfirm -Scc

sudo umount archlinux_dvd
```

Building a template
-------------------

``` {.wiki}
export DIST=archlinux
make rpms
```

Testing a template
------------------

Extracting a kernel
-------------------

### Qubes boot scripts (dracut/initramfs)

### Modules image
