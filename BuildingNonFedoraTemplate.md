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
