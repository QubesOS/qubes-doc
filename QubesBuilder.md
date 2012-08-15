---
layout: wiki
title: QubesBuilder
permalink: /wiki/QubesBuilder/
---

Building Qubes from scratch
===========================

We have recently created a fully automated build system for Qubes, that downloads, builds and packages all the Qubes components, and finally should spit out a ready-to-use installation ISO.

In order to use it one should use an rpm-based distro, like Fedora :) and should ensure the following packages are installed:

-   git
-   createrepo
-   rpm-build
-   make

Unusually one can install those packages by just issuing:

``` {.wiki}
sudo yum install git createrepo rpm-build make wget
```

The build system creates build environments in chroots and so no other packages are needed on the host. All files created by the build system are contained within the qubes-builder directory. The full build requires some 25GB of free space, so keep that in mind when deciding where to place this directory.

The build system is configured via builder.conf file -- one should copy the attached builder.conf.default, and modify it as needed, e.g.:

``` {.wiki}
cp builder.conf.default builder.conf 
# edit the builder.conf file and set the following variables: 
# (make sure to leave no spaces around '=' sign!) 
# NO_SIGN="1"
```

One additional useful requirement is that 'sudo root' work without any prompt, which is default on most distros (e.g. 'sudo bash' brings you the root shell without asking for any password). This is important as the builder needs to switch to root and then back to user several times during the build process.

Additionally, if building with signing enabled (so NO\_SIGN is not set), one must adjust \~/.rpmmacro file so that it point to the GPG key used for package signing, e.g.:

``` {.wiki}
%_signature gpg
%_gpg_path /home/user/.gnupg
%_gpg_name AC1BF9B3  # <-- Key ID used for signing
```

It is also recommended to use an empty passphrase for the private key used for signing. Contrary to a popular belief, this doesn't affect your key or sources security -- if somebody compromised your system, then the game is over, whether you use additional passphrase for the key or not.

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

Making customized build
-----------------------

You can use above tool to build Qubes with some components modified. Described here procedure will build Qubes with:

-   non-default kernel
-   newer Intel display driver

The instruction:

1.  Download qubes-builder as described above
2.  Edit builder.conf (still the same as above), some useful additions:
    -   As time of writing this, the default is fc15, but latest supported is fc17, so switch to newer one

        ``` {.wiki}
        DISTS_VM="fc17"
        ```

    -   You can also set GIT\_SUBDIR="marmarek" to use my repo instead of "mainstream" - it contains newer (but less tested) versions

1.  Download unmodified sources

    ``` {.wiki}
    make get-sources
    ```

1.  Make your modifications here

-   The kernel

    ``` {.wiki}
    cd qubes-src/kernel
    git fetch git://git.qubes-os.org/marmarek/kernel.git devel-3.4:devel-3.4
    git checkout devel-3.4
    # need to download sources again, as the first time the default (older) kernel source was downloaded
    # note that this is run from kernel subdir, not main qubes-builder directory
    make BUILD_FLAVOR=pvops get-sources

    cd ../../
    ```

-   Xorg driver

    ``` {.wiki}
    cd qubes-src/dom0-updates
    rm xorg-x11-driver-intel*fc15.src.rpm
    yumdownloader --releasever=17 --source xorg-x11-driver-intel

    cd ../../
    ```

> If you want to install any other package in newer version than in fc13 (on which dom0 is based), you can place it here. Remember to update also Makefile to include its build and add its build requires to *build-pkgs-dom0-updates.list* in qubes-builder dir.

1.  Build the Qubes
     `make qubes` actually is just meta target which build all required components in correct order

    ``` {.wiki}
    grep ^qubes: Makefile
    qubes: get-sources xen core kernel gui addons docs template kde-dom0 installer qubes-manager dom0-updates sign-all
    ```

> `get-sources` is already done, so continue with the next one. You can skip `sign-all` if you've disabled signing
>
> ``` {.wiki}
> make xen core kernel gui addons docs template kde-dom0 installer qubes-manager dom0-updates
> ```

1.  build iso installation image

    ``` {.wiki}
    make iso
    ```


