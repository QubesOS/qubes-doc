---
layout: doc
title: Qubes Builder
permalink: /doc/qubes-builder/
redirect_from:
- /en/doc/qubes-builder/
- /doc/QubesBuilder/
- /wiki/QubesBuilder/
---

**Note: The build system has been improved since this how-to was last updated. The [ISO building instructions](/doc/qubes-r3-building/) contain more up-to-date information on how to use the build system.**

Building Qubes from scratch
===========================

We have a fully automated build system for Qubes, that downloads, builds and
packages all the Qubes components, and finally should spit out a ready-to-use
installation ISO.

In order to use it, one should use an rpm-based distro, like Fedora :), and should ensure the following packages are installed:

-   sudo
-   gnupg
-   git
-   createrepo
-   rpm-build
-   make
-   wget
-   rpmdevtools
-   python2-sh
-   dialog
-   rpm-sign
-   dpkg-dev
-   debootstrap
-   PyYAML
-   devscripts
-   perl-Digest-MD5
-   perl-Digest-SHA

Usually one can install those packages by just issuing:

    sudo dnf install gnupg git createrepo rpm-build make wget rpmdevtools python2-sh dialog rpm-sign dpkg-dev debootstrap PyYAML devscripts perl-Digest-MD5 perl-Digest-SHA

The build system creates build environments in chroots and so no other packages are needed on the host. All files created by the build system are contained within the qubes-builder directory. The full build requires some 25GB of free space, so keep that in mind when deciding where to place this directory.

The build system is configured via builder.conf file -- one should copy the provided default builder.conf, and modify it as needed, e.g.:

    cp example-configs/qubes-os-master.conf builder.conf 
    # edit the builder.conf file and set the following variables: 
    NO_SIGN=1

One additional useful requirement is that 'sudo root' must work without any prompt, which is default on most distros (e.g. 'sudo bash' brings you the root shell without asking for any password). This is important as the builder needs to switch to root and then back to user several times during the build process.

Additionally, if building with signing enabled (NO\_SIGN is not set), one must adjust \~/.rpmmacro file so that it points to the GPG key used for package signing, e.g.:

    %_signature gpg
    %_gpg_path /home/user/.gnupg
    %_gpg_name AC1BF9B3  # <-- Key ID used for signing

It is also recommended to use an empty passphrase for the private key used for signing. Contrary to a popular belief, this doesn't affect your key or sources security -- if somebody compromised your system, then the game is over anyway, whether you have used an additional passphrase for the key or not.

So, to build Qubes one would do:

    # Import the Qubes master key 
    gpg --recv-keys 0xDDFA1A3E36879494
    
    # Verify its fingerprint, set as 'trusted'. 
    # This is described here: 
    # https://www.qubes-os.org/doc/VerifyingSignatures
    
    wget https://keys.qubes-os.org/keys/qubes-developers-keys.asc
    gpg --import qubes-developers-keys.asc 
    
    git clone git://github.com/QubesOS/qubes-builder.git qubes-builder 
    cd qubes-builder 

    # Verify its integrity:
    git tag -v `git describe`
    
    cp example-configs/qubes-os-master.conf builder.conf 
    # edit the builder.conf file and set the following variables: 
    # NO_SIGN="1"
    
    # Download all components:
    
    make get-sources
    
    # And now to build all Qubes rpms (this will take a few hours): 
    
    make qubes 
    
    # ... and then to build the ISO 
    
    make iso 

And this should produce a shiny new ISO.

You can also build selected component separately. Eg. to compile only gui virtualization agent/daemon:

    make gui-daemon

You can get a full list from make help. For advanced use and preparing sources
for use with [QubesBuilder](/doc/qubes-builder/) take a look at [doc directory
in QubesBuilder](https://github.com/marmarek/qubes-builder/tree/master/doc) or 
[QubesBuilderDetails](/doc/qubes-builder-details/) page.

Making customized build
-----------------------

### Manual source modification

If you want to somehow modify sources, you can also do it, here are some basic steps:

1.  Download qubes-builder as described above (if you want to use marmarek's branches, you should also download qubes-builder from his repo - replace 'QubesOS' with 'marmarek' in above git clone command)
2.  Edit builder.conf (still the same as above), some useful additions:
    -   You can also set GIT\_PREFIX="marmarek/qubes-" to use my repo instead of "mainstream" - it contains newer (but less tested) versions

3.  Download unmodified sources

        make get-sources

4.  **Make your modifications here**

5.  Build the Qubes
     `make qubes` actually is just meta target which build all required
     components in correct order. List of components is configured in
     builder.conf. You can also check the current value at the end of `make
     help`, or using `make build-info`. 

6. `get-sources` is already done, so continue with the next one. You can skip `sign-all` if you've disabled signing

        make vmm-xen core-admin linux-kernel gui-daemon template desktop-linux-kde installer-qubes-os manager linux-dom0-updates

1.  build iso installation image

        make iso

### Use pre-built Qubes packages

For building just few selected packages, it's very useful to download pre-built qubes-specific dependencies from `{yum,deb}.qubes-os.org`.
This is especially true for `gcc`, which takes several hours to build.

Before creating the `chroot`, add this to your `builder.conf`:

    USE_QUBES_REPO_VERSION = $(RELEASE)

It will add the 'current' Qubes repository to your `chroot` environment.
This way, you can build only the packages you are interested in.
If you also want to use the 'current-testing' repository, add this to your configuration:

    USE_QUBES_REPO_TESTING = 1

In the case of an existing `chroot`, for mock-enabled builds, it works immediately because `chroot` is constructed each time separately.
For legacy builds, it will not add the necessary configuration into the build environment unless a specific builder change or configuration would force rebuilding chroot.

Also, once enabled, disabling this setting will not disable repositories in relevant chroots.
And even if it did, there could be leftover packages installed from those repos (which may or may not be desirable).

Code verification keys management
---------------------------------

[QubesBuilder](/doc/qubes-builder/) by default verifies signed tags on every downloaded code. Public keys used for that are stored in `keyrings/git`. By default Qubes developers' keys are imported automatically, but if you need some additional keys (for example your own), you can add them using:

    GNUPGHOME=$PWD/keyrings/git gpg --import /path/to/key.asc
    GNUPGHOME=$PWD/keyrings/git gpg --edit-key ID_OF_JUST_IMPORTED_KEY
    # here use "trust" command to set key fully or ultimately trusted - only those keys are accepted by QubesBuilder

All Qubes developers' keys are signed by the Qubes Master Signing Key (which is set as ultimately trusted key), so are trusted automatically.

If you are the owner of Master key and want to revoke such signature, use the `revsig` gpg key edit command and update the key in qubes-developers-keys.asc - now the key will be no longer trusted (unless manually set as such).
