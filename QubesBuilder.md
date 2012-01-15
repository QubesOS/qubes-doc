---
layout: wiki
title: QubesBuilder
permalink: /wiki/QubesBuilder/
---

Building Qubes from scratch
===========================

(based on [​this post](https://groups.google.com/group/qubes-devel/browse_thread/thread/588399cdd43da28c/496e9eb9ccf31abb))

We have recently created a fully automated build system for Qubes, that downloads, builds and packages all the Qubes components, and finally should spit out a ready-to-use installation ISO.

In order to use it one should use an rpm-based distro, like Fedora :) and should ensure the following packages are installed:

-   git
-   createrepo
-   rpm-build
-   make

Unusually one can install those packages by just issuing:

``` {.wiki}
sudo yum install git createrepo rpm-build make 
```

The build system creates build environments in chroots and so no other packages are needed on the host. All files created by the build system are contained within the qubes-builder directory. The full build requires some 25GB of free space, so keep that in mind when deciding where to place this directory.

One additional useful requirement is that 'sudo root' work without any prompt, which is default on most distros (e.g. 'sudo bash' brings you the root shell without asking for any password). This is important as the builder needs to switch to root and then back to user several times during the build process.

So, to build Qubes one would do:

``` {.wiki}
# Import the Qubes master key 
gpg --recv-keys 0x36879494 

# Verify its fingerprint, set as 'trusted'. 
# This is described here: 
# https://wiki.qubes-os.org/trac/wiki/VerifyingSignatures 

wget http://keys.qubes-os.org/keys/qubes-developers-keys.asc 
gpg --import qubes-developers-keys.asc 

git clone git://git.qubes-os.org/joanna/qubes-builder.git qubes-builder 
cd qubes-builder 

cp builder.conf.default builder.conf 
# edit the builder.conf file and set the following variables: 
# (make sure to leave no spaces around '=' sign!) 
# GIT_SUBDIR="joanna" 
# NO_SIGN="1"

# And now to build all Qubes rpms (this will take a few hours): 

make qubes 

# ... and then to build the ISO 

make iso 
```

And this should produce a shiny new ISO.

You can also build selected component separately. Eg. to compile only gui virtualization agent/daemon:

``` {.wiki}
make gui
```

Full list you can get from make help.
