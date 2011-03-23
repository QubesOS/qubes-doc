---
layout: wiki
title: InstallationIsoBuilding
permalink: /wiki/InstallationIsoBuilding/
---

How to build Qubes installation ISO
===================================

Qubes uses [FedoraUnity?](/wiki/FedoraUnity) [​Revisor](http://revisor.fedoraunity.org/) to build the installation ISO.

So, get [​Qubes version of Revisor](http://git.qubes-os.org/?p=smoku/revisor) build it (`cd package; rpmbuild -bb revisor.spec`) and install all built revisor packages.

Build ISO
---------

All configuration files for Qubes Revisor assume that the working directory is `/Devel/Qubes`. So either modify the configuration files to your needs, or just symlink your working directory as `/Devel/Qubes`.

You will need to put all additional packages, not present in Fedora and Qubes repos to local repository `file:///Devel/Qubes/rpmbuild/RPMS/` and `cd /Devel/Qubes/rpmbuild/RPMS && createrepo .` to create repository metadata.

Next just run:

``` {.wiki}
revisor --cli --config=qubes-install-respin.conf --model=qubes1-x86_64 --install-dvd
```

and wait... (You may add `-d 99` to get a ton of debugging information.)
