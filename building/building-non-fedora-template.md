---
layout: doc
title: Building Non-Fedora Template
permalink: /doc/building-non-fedora-template/
redirect_from:
- /en/doc/building-non-fedora-template/
- /doc/BuildingNonFedoraTemplate/
- /wiki/BuildingNonFedoraTemplate/
---

Building a TemplateVM for ArchLinux (or another non Fedora OS)
==============================================================

If you don't like using Fedora because of specific administration, package management or other building needs, you could build a TemplateVM for your distribution of choice.

This article shows how to build a template for a different OS, taking ArchLinux as an example.

Qubes builder scripts
=====================

You can start creating Qubes builder scripts for your new OS. Just note that it will probably make your testing process harder than trying to build the package directly in an HVM on which you already installed this new OS.

chroot initialization
---------------------

You need to customize some scripts that will be used to build all the Qubes tools.

The scripts you will be interested in will be inside the `qubes-src/linux-template-builder` folder:

~~~
scripts_fedora
scripts_archlinux
scripts_yourOSname
~~~

### 00\_prepare.sh

The goal of the first script `00_prepare.sh` is to download and verify the signature of the installation CD and tools. You can use the `$CACHEDIR` directory variable to store files that could be reused (such as downloaded scripts or iso files).

### 01\_install\_core.sh

The goal of this script is to install a base environment of your target OS inside the `$INSTALLDIR` directory variable. Generally you need to bootstrap/install your package manager inside the `$INSTALLDIR` directory and install the base packages.

### Testing the installation process

Edit the file `builder.conf` to change the variable `$DISTS_VM` to your OS name (`DISTS_VM=your_os_name`). The try to create (make) the template to check that at least these first two scripts are working correctly:

~~~
make linux-template-builder
~~~

Qubes builder Makefiles
-----------------------

Now you need to create Makefiles specific to your OS. You will find the required scripts directly inside the `qubes-builder` folder:

~~~
prepare-chroot-yourOSname
Makefile.yourOSname
~~~

### prepare-chroot-yourOSname

The goal of this file is to prepare a development environment of your target OS inside a chroot. You will reuse the `00_prepare.sh` and `01_install_core.sh` scripts. Additionally, the following things will be necessary to put in this Makefile:

-   the `$1` variable will contain the installation directory (`$INSTALLDIR` should contain the same value as `$1` when you run `00_prepare.sh` or `01_install_core.sh`)
-   after your base system is installed, you should install development tools and libraries (gcc, make, ...)
-   create a user called 'user' inside your chroot, and give him enough rights to run the command sudo without any password
-   register all the repositories that are be necessary and synchronize the package database
-   register a custom repository that will be used to store Qubes packages

### Makefile.yourOSname

This file will be used to define the action required when installing a custom package. The most important one are:

-   `dist-prepare-chroot`: that's where you will call `prepare-chroot-yourOSname` if the chroot has not been initialized.
-   `dist-package`: that's where you will chroot the development environment and run the command used to build a package.
-   `dist-build-dep`: that's where you will create the custom repository for your target OS based on already compiled packages.

These additional target need to exist once you created your first packages:

-   `dist-copy-out`: that's where you will retrieve the package you just built and put it with all the other packages you prepared.
-   `update-repo`: that's where you will retrieve the package that have been built and add it to the custom repository.

### Testing the development chroot

You will be able to test these scripts when making the first Qubes packages. Don't forget that the first things that run when running `make somcomponent-vm` will be these two scripts, and that you will need to debug it at this point.

Qubes packages
--------------

* [vmm-xen](https://github.com/QubesOS/qubes-vmm-xen)
* [core-vchan-xen](https://github.com/QubesOS/qubes-core-vchan-xen)
* [linux-utils](https://github.com/QubesOS/qubes-linux-utils)
* [core-agent-linux](https://github.com/QubesOS/qubes-core-agent-linux)
* [gui-common](https://github.com/QubesOS/qubes-gui-common)
* [gui-agent-linux](https://github.com/QubesOS/qubes-gui-agent-linux)

Additional Installation scripts
-------------------------------

Again you need to work on scripts inside the `qubes-src/linux-template-builder` folder:

~~~
scripts_fedora
scripts_archlinux
scripts_yourOSname
~~~

### 02\_install\_groups.sh

The goal of this script is to install all the packages that you want to use in your template (eg: firefox, thunderbird, a file manager, Xorg...).

### 04\_install\_qubes.sh

The goal of this script is to install in your template all the packages you built previously. Also you need to edit the fstab file of your template to mount Qubes virtual hard drives.

### 09\_cleanup.sh

This script is use to finalize and to remove unnecessary things from your template, such as cached packages, unused development packages ...

Starting with an HVM
====================

If no Qubes packages are available for your selected OS. You could start to install an HVM with your OS. Your goals will be:

-   to identify how to install the OS using command lines
-   to create required Qubes packages
-   to identify potential issue making all Qubes agents and scripts working correctly.

As soon as you manage to make `qrexec` and `qubes-gui-agent` working, it should be sufficient to start preparing a template VM.

### Xen libraries

Several Xen libraries are required for Qubes to work correctly. In fact, you need to make `xenstore` commands working before anything else. For this, Qubes git can be used as several patches have been selected by Qubes developers that could impact the activity inside a VM. Start be retrieving a recent git and identify how you can build a package from it: `git clone https://github.com/QubesOS/qubes-vmm-xen.git`.

Find the .spec file in the git repository (this is the file being used to build rpm packages), and try to adapt it to your OS in order to build a package similar to the target 'vmm-xen'. For example, a PKGBUILD has been created for [ArchLinux](/doc/templates/archlinux/) and can be found in the vmm-xen repository.

Don't be afraid with the complexity of the PKGBUILD, most of the code is almost a copy/paste of required sources and patches found in the .spec file provided in the git repository.

Note once the package has been successfully compiled and installed, you need to setup XEN filesystem. Add the following line to your fstab (you can create this line in your package install script): `xen                     /proc/xen               xenfs   defaults        0 0`.

Now install the package you built and mount `/proc/xen`. Verify that xenstore-read works by running: `xenstore-read name`. That should give you the current name.

### ArchLinux example PKGBUILDs

Qubes OS core agent (qrexec...) - [https://aur.archlinux.org/packages/qu/qubes-vm-core/PKGBUILD](https://aur.archlinux.org/packages/qu/qubes-vm-core/PKGBUILD)

Qubes OS kernel modules - [https://aur.archlinux.org/packages/qu/qubes-vm-kernel-modules/PKGBUILD](https://aur.archlinux.org/packages/qu/qubes-vm-kernel-modules/PKGBUILD)

Qubes OS GUI agent - [https://aur.archlinux.org/packages/qu/qubes-vm-gui/PKGBUILD](https://aur.archlinux.org/packages/qu/qubes-vm-gui/PKGBUILD)
