---
layout: wiki
title: InstallationIsoBuilding
permalink: /wiki/InstallationIsoBuilding/
---

How to build Qubes installation ISO
===================================

Qubes uses [FedoraUnity?](/wiki/FedoraUnity) [​Revisor](http://revisor.fedoraunity.org/) to build the installation ISO.

You may want to get familiar with [​Revisor documentation](http://revisor.fedoraunity.org/documentation).

Build installer packages
------------------------

Get [​Qubes Installer repository](http://git.qubes-os.org/?p=smoku/installer) and build its packages:

``` {.wiki}
cd installer
make rpms
```

Packages will be in `rpm/noarch` and `rpm/x86_64`.

Install Revisor
---------------

Next install the freshly built revisor:

``` {.wiki}
yum install rpm/noarch/revisor*.rpm
```

Prepare configuration files
---------------------------

All configuration files for Qubes Revisor assume that the working directory is `/Devel/Qubes`. So either modify the configuration files to your needs, or just symlink your working directory as `/Devel/Qubes`.

See the end of this document for description of the configuration files purpose.

Create local repository
-----------------------

Revisor fetches all RPM packages from YUM repositories. You will need to put all additional packages not present in Fedora and Qubes repos (like the ones you've built in the first step) to local repository. By default it is `file:///Devel/Qubes/yum/r1/installer/rpm/`.

Copy or link all `installer/rpm/*/*.rpm` packages to `/evel/Qubes/yum/r1/installer/rpm`. Then create repository metadata.

``` {.wiki}
mkdir -p /Devel/Qubes/yum/r1/installer/rpm
cd /Devel/Qubes/installer
make update-repo
cd /Devel/Qubes/yum/r1/installer/rpm
createrepo .
```

Build ISO
---------

Now you're finally ready to build the ISO image:

``` {.wiki}
revisor --cli --config=/conf/qubes-install-respin.conf --model=qubes1-x86_64 --install-dvd
```

and wait...

You may add `-d 99` to get a ton of debugging information.

Revisor configuration files
---------------------------

**conf/qubes-install-respin.conf** - Main Revisor configuration file. This configures Revisor to build Qubes Installation image based on Fedora 13. All other configuration files and working directories are pointed here.

**conf/qubes1-x86\_64-respin.conf** - As said Revisor gets all packages it uses form YUM repositories. This file describes all repositories needed to build Qubes R1 for x86\_64 architecture. This file also points the local repository you created before.

**conf/qubes-1-respin.cfg** - Fedora Kickstart formatted file describing which packages should land in the ISO `/Packages` repository. This describes basically what will be available for installation. The packages list built using this file will be further filtered by the comps file.

**conf/comps-qubes1.xml** - Repository Comps file for ISO `/Packages` repository, describing packages and package groups of the installer repository. Package groups are used to select which of the packages are mandatory to install, which are optional and which are to be just available on the ISO but not installed by default. Package groups may also be optional - this allows them to be selected during installation in Anaconda interface.
