---
layout: doc
title: Building Non-Fedora Template
permalink: /doc/building-non-fedora-template/
redirect_from:
- /en/doc/building-non-fedora-template/
- /doc/BuildingNonFedoraTemplate/
- /wiki/BuildingNonFedoraTemplate/
---

Building a TemplateVM for a new OS
==============================================================

If you don't like using one of the existing templates because of specific administration, package management or other building needs, you can build a TemplateVM for your distribution of choice.

This article shows how to go about building a template for a different OS.

Qubes builder scripts
=====================

One way to start is by creating Qubes builder scripts for your new OS.
Note that this will probably make your testing process harder than trying to build the package directly in an HVM on which you have already installed the new OS.

chroot initialization
---------------------

You need to customize some scripts that will be used to build all the Qubes tools.
Create a new directory to hold the files for the new os.
You can start from the Fedora scripts in `builder-rpm/template-scripts`, and see how they have been changed for Debian and Archlinux.
The scripts you need are in :

~~~
builder-archlinux/scripts
builder-debian/template-debian
builder-rpm/template-scripts
~~~

### 00\_prepare.sh

The goal of the first script `00_prepare.sh` is to download and verify the signature of the installation CD and tools, or the native tools for building an OS.
You can use the `$CACHEDIR` directory variable to store files that could be reused (such as downloaded scripts or iso files).

### 01\_install\_core.sh

The goal of this script is to install a base environment of your target OS inside the `$INSTALLDIR` directory variable.
Generally you need to bootstrap/install your package manager inside the `$INSTALLDIR` directory and install the base packages.

### Testing the installation process

Edit the file `builder.conf` to change the variable `$DISTS_VM` to your OS name (`DISTS_VM=your_os_name`).
Then try to create (make) the template to check that at least these first two scripts are working correctly:

~~~
make linux-template-builder
~~~

Qubes builder Makefiles
-----------------------

Now you need to create Makefiles specific to your OS.
You will find the required scripts to adapt in the `builder-*` folders:

~~~
prepare-chroot-yourOSname
Makefile.yourOSname
~~~

### prepare-chroot-yourOSname

The goal of this file is to prepare a development environment of your target OS inside a chroot.
You will reuse the `00_prepare.sh` and `01_install_core.sh` scripts.
Additionally, the following things have to be done in this Makefile:

-   the `$1` variable will contain the installation directory (`$INSTALLDIR` should contain the same value as `$1` when you run `00_prepare.sh` or `01_install_core.sh`)
-   after your base system is installed, you should install development tools and libraries (gcc, make, ...)
-   create a user called 'user' inside your chroot, and give them enough rights to run the command sudo without any password
-   register all the repositories that will be necessary and synchronize the package database
-   register a custom repository that will be used to store Qubes packages

### Makefile.yourOSname

This file will be used to define the action required when installing a custom package.
The most important one are:

-   `dist-prepare-chroot`: that's where you will call `prepare-chroot-yourOSname` if the chroot has not been initialized.
-   `dist-package`: that's where you will chroot the development environment and run the command used to build a package.
-   `dist-build-dep`: that's where you will create the custom repository for your target OS based on already compiled packages.

These additional targets need to exist once you have created your first packages:

-   `dist-copy-out`: that's where you will retrieve the package you just built and put it with all the other packages you prepared.
-   `update-repo`: that's where you will retrieve the package that has been built and add it to the custom repository.

### Testing the development chroot

You will be able to test these scripts when making the first Qubes packages.
Don't forget that the first things that run when running `make somecomponent-vm` will be these two scripts, and that you will need to debug it at this point.

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

Again you need to create new scripts based on the existing scripts in these folders:


~~~
builder-archlinux/scripts
builder-debian/template-debian
builder-rpm/template-scripts
~~~

### 02\_install\_groups.sh

The goal of this script is to install all the packages that you want to use in your template (eg: firefox, thunderbird, a file manager, Xorg...).

### 04\_install\_qubes.sh

The goal of this script is to install in your template all the packages you built previously.
Also you need to edit the fstab file of your template to mount Qubes virtual hard drives.

### 09\_cleanup.sh

This script is used to finalize and to remove unnecessary things from your template, such as cached packages, unused development packages ...

Starting with an HVM
====================

If no Qubes packages are available for your selected OS you could start by installing your OS in an HVM.
Your goals will be:

-   to identify how to install the OS using command lines
-   to create required Qubes packages
-   to identify potential issues, making sure all Qubes agents and scripts work correctly.

As soon as you manage to get `qrexec` and `qubes-gui-agent` working, you will be ready to start preparing a template VM.

### Xen libraries

Several Xen libraries are required for Qubes to work correctly.
In fact, you need to make `xenstore` commands working before anything else.
For this, Qubes git can be used as several patches have been selected by Qubes developers that could impact the activity inside a VM.
Start by retrieving a recent git and identify how you can build a package from it: `git clone https://github.com/QubesOS/qubes-vmm-xen.git`.

Find the .spec file in the git repository (this is the file used to build rpm packages), and try to adapt it to your OS in order to build a package similar to the target 'vmm-xen'.
For example, a PKGBUILD has been created for [ArchLinux](/doc/templates/archlinux/) which can be found in the vmm-xen repository.

Don't be afraid of the complexity of the PKGBUILD: most of the code is almost a copy/paste of required sources and patches found in the .spec file provided in the git repository.

Note once the package has been successfully compiled and installed, you need to setup XEN filesystem.
Add the following line to your fstab (you can create this line in your package install script):  
`xen                     /proc/xen               xenfs   defaults        0 0`.

Now install the package you built and mount `/proc/xen`.
Verify that xenstore-read works by running: `xenstore-read name`. That should give you the current qube name.
