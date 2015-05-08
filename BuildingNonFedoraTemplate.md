---
layout: doc
title: BuildingNonFedoraTemplate
permalink: /doc/BuildingNonFedoraTemplate/
redirect_from: /wiki/BuildingNonFedoraTemplate/
---

Building a TemplateVM for [ArchLinux?](/wiki/ArchLinux) (or another non fedora OS)
==================================================================================

If you don't like using Fedora because of specific administration or package management / building needs, you could build a VM Template for your Distribution of choice.

This article shows how to build a template for a different OS, taking [ArchLinux?](/wiki/ArchLinux) as an example.

Qubes builder scripts
=====================

You can start creating Qubes builder scripts for your new OS. Just note that it will probably make your testing process harder than trying to build the package directly in an HVM on which you already installed this new OS.

chroot initialization
---------------------

You need to install your OS inside a chroot that will be used to build all the required qubes agents of tools.

The scripts you will be interested in will be inside the qubes-src/linux-template-builder project:

{% highlight trac-wiki %}
scripts_fedora
scripts_archlinux
scripts_yourOSname
{% endhighlight %}

### 00\_prepare.sh

The goal of the first script 00\_prepare.sh is to download and verify the signature of the installation cd and tools. You can use the \$CACHEDIR directory variable to store files that could be reused (such as downloaded scripts or iso files)

### 01\_install\_core.sh

The goal of this script is to install a base environment of your target OS inside the \$INSTALLDIR directory variable. Generally you need to bootstrap/install your package manager inside the \$INSTALLDIR directory and install the base packages.

### Testing the installation process

Edit the builder.conf file to change the variable DISTS\_VM to your OS name (DISTS\_VM=your\_os\_name). The try to make the template to check that at least these to first scripts are working correctly:

{% highlight trac-wiki %}
make linux-template-builder
{% endhighlight %}

Qubes builder Makefiles
-----------------------

Now you need to create Makefiles specific to your OS. You will find the required scripts directly inside qubes-builder:

{% highlight trac-wiki %}
prepare-chroot-yourOSname
Makefile.yourOSname
{% endhighlight %}

### prepare-chroot-yourOSname

The goal of this file is to prepare a development environment of your target OS inside a chroot. You will reuse there the 00\_prepare.sh and 01\_install\_core.sh scripts. Additionally, the following things will be necessary to use to chroot environment:

-   the \$1 variable will contain the installation directory (INSTALLDIR should contain the same value than \$1 when you run 00\_prepare or 01\_install\_core)
-   after your base system is installed, you should install development tools and libraries (gcc, make, ...)
-   create a user called 'user' inside your chroot, and give him enought right to run the command sudo without any password
-   register all the repository that could be necessary and synchronize the package database
-   register a custom repository that will be used to store qubes packages

### Makefile.yourOSname

This file will be used to define the action required when installing a package. The most important one are:

-   dist-prepare-chroot: that's where you will call prepare-chroot-yourOSname if the chroot has not been initialized
-   dist-package: that's where you will chroot the development environment and run the command used to build a package.
-   dist-build-dep: that's where you will create the custom repository for your target OS based on already compiled packages.

These additional target need to exist once you created your first packages:

-   dist-copy-out: that's where you will retrieve the package you just built and put it with all the other package you prepared.
-   update-repo: that's where you will retrieve the package that have been built and that need to be installed inside the template

### Testing the development chroot

You will be able to test these script when making the first qubes packages. Don't forget that the first things that run when running 'make somcomponent-vm' will be these two scripts, and that you will need to debug it at this point.

Qubes packages
--------------

### vmm-xen-vm

### core-vchan-xen-vm

### linux-utils-vm

### core-agent-linux-vm

### gui-common-vm

### gui-agent-linux-vm

Additional Installation scripts
-------------------------------

Again you need to work on scripts inside the qubes-src/linux-template-builder project:

{% highlight trac-wiki %}
scripts_fedora
scripts_archlinux
scripts_yourOSname
{% endhighlight %}

### 02\_install\_groups.sh

The goal of this script is to install all the package that you want to use in your template (eg: firefox, thunderbird, a file manager, Xorg...)

### 04\_install\_qubes.sh

The goal of this script is to install in your template all the packages you built previously. Also you need to edit the fstab file of your template to mount qubes virtual hard drives.

### 09\_cleanup.sh

This script is use to finalize and to remove unnecessary things from your template, such as cached packages, unused development packages ...

Starting with an HVM
====================

If no Qubes packages are available for your selected OS. You could start to install an HVM with your OS. Your goals will be:

-   to identify how to install the OS using command lines
-   to create required Qubes packages
-   to identify potential issue making all Qubes agents and scripts working correctly.

As soon as you manage to make qrexec and qubes-gui-agent working, it should be sufficient to start preparing a template VM.

### Xen libraries

Several XEN libraries are required for Qubes to work correctly. In fact, you need to make xenstore commands working before anything else. For this, Qubes git can be used as several patches have been selected by Qubes developpers that could impact the activity inside a VM. Start be retrieving a recent git and identify how you can build a package from it: `git clone git://git.qubes-os.org/marmarek/xen`

Find the .spec file in the git repository (this is the file being used to build rpm packages), and try to adapt it to your OS in order to build a package similar to the target 'xen-vm'. For example, a PKGBUILD has been created for [ArchLinux?](/wiki/ArchLinux) and can be found on [http://aur.archlinux.org/packages/qu/qubes-vm-xen/PKGBUILD](http://aur.archlinux.org/packages/qu/qubes-vm-xen/PKGBUILD).

Don't be afraid with the complexity of the PKGBUILD, most of the code is almost a copy/paste of required sources and patches found in the .spec file provided in the git repository.

Note once the package has been successfully compiled and installed, you need to setup XEN filesystem. Add the folowing line to your fstab (you can create this line in your package install script): `xen                     /proc/xen               xenfs   defaults        0 0`

Now install the package you built and mount /proc/xen. Verify that xenstore-read works by running: `xenstore-read qubes_vm_type` That should give you the current VM type such as HVM or AppVM.

### Qubes-OS core agents (qrexec...)

[https://aur.archlinux.org/packages/qu/qubes-vm-core/PKGBUILD](https://aur.archlinux.org/packages/qu/qubes-vm-core/PKGBUILD)

### Qubes-OS kernel modules

[https://aur.archlinux.org/packages/qu/qubes-vm-kernel-modules/PKGBUILD](https://aur.archlinux.org/packages/qu/qubes-vm-kernel-modules/PKGBUILD)

### Qubes-OS gui agents

[https://aur.archlinux.org/packages/qu/qubes-vm-gui/PKGBUILD](https://aur.archlinux.org/packages/qu/qubes-vm-gui/PKGBUILD)
