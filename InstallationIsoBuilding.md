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

Next install the freshly built revisor and anaconda:

``` {.wiki}
yum install rpm/noarch/revisor*.rpm
yum install rpm/x86_64/anaconda*.rpm
```

Review configuration files
--------------------------

All configuration files for Qubes Revisor are kept in the ```conf/``` directory:

-   ```conf/qubes-install-respin.conf``` - Main Revisor configuration file. This configures Revisor to build Qubes Installation image based on Fedora 13. All other configuration files and working directories are pointed here.

-   ```conf/qubes1-x86_64-respin.conf``` - As said Revisor gets all packages it uses form YUM repositories. This file describes all repositories needed to build Qubes R1 for x86\_64 architecture. This file also points the local repository you created before.

-   ```conf/qubes-1-respin.cfg``` - Fedora Kickstart formatted file describing which packages should land in the ISO `/Packages` repository. This describes basically what will be available for installation. The packages list built using this file will be further filtered by the comps file.

-   ```conf/comps-qubes1.xml``` - Repository Comps file for ISO `/Packages` repository, describing packages and package groups of the installer repository. Package groups are used to select which of the packages are mandatory to install, which are optional and which are to be just available on the ISO but not installed by default. Package groups may also be optional - this allows them to be selected during installation in Anaconda interface.

Create local repository
-----------------------

Revisor fetches all RPM packages from YUM repositories. We currently use 5 repositories:

-   ```build/yum/installer``` (installer-related rpms)
-   ```build/yum/qubes-dom0``` (all the Qubes stuff)
-   ```build/yum/dom0-updates``` (for select 3rd party packages, e.g. Xorg)
-   ```build/fedora13-repo``` (local fedora 13 repo, copy from DVD, we don't keep it uder build/yum, because we don't want our update script to process it every time)
-   remote fedora repo for extra packages (usually deps for qubes-dom0)

You need to manually copy the Fedora 13 installation DVD contents (```Packages/``` and ```repodata/``` directories) into ```build/fedora13-repo```.

Also, you need to copy all the qubes dom0 rpms into ```build/yum/qubes-dom0/rpm``` and run the ```yum/update_repo.sh``` script afterwards.

In order to fill the ```build/yum/installer``` repo one can just use ```make update-repo```.

The ```build/yum/dom0-updates``` is to be used for select rpms that should also be used instead of those from the fedora (loacal and remote) repos.

Build ISO
---------

Now you're finally ready to build the ISO image:

``` {.wiki}
make iso
```

and wait...

You may add `-d 1` (or `-d 99` if you're a masochist) in the Makefile at the end of the revisor command to get (a ton of) debugging information.
