---
lang: en
layout: doc
permalink: /doc/qubes-builder/
redirect_from:
- /en/doc/qubes-builder/
- /doc/QubesBuilder/
- /wiki/QubesBuilder/
ref: 64
title: Qubes builder
---

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Note:</b> These instructions concern the older Qubes builder (v1). It supports
  only building Qubes 4.1 or earlier. For building Qubes R4.2 or later and related
  components, please see instead [qubes-builderv2](https://github.com/QubesOS/qubes-builderv2/).
</div>

**Note: See [ISO building instructions](/doc/qubes-iso-building/) for a streamlined overview on how to use the build system.**


We have a fully automated build system for Qubes, that downloads, builds and
packages all the Qubes components, and finally should spit out a ready-to-use
installation ISO, all in a [secure](/news/2016/05/30/build-security/) way.

In order to use it, you should use an rpm-based distro, like Fedora :), and should ensure the following packages are installed:

- sudo
- gnupg
- git
- createrepo
- rpm-build
- dnf-plugins-core
- make
- wget
- rpmdevtools
- python3-sh
- dialog
- rpm-sign
- dpkg-dev
- debootstrap
- python3-pyyaml
- devscripts
- perl-Digest-MD5
- perl-Digest-SHA

Usually you can install those packages by just issuing:

```shell
sudo dnf install gnupg git createrepo rpm-build make wget rpmdevtools python3-sh dialog rpm-sign dpkg-dev debootstrap python3-pyyaml devscripts perl-Digest-MD5 perl-Digest-SHA
```

The build system creates build environments in chroots and so no other packages are needed on the host.
All files created by the build system are contained within the qubes-builder directory.
The full build requires some 25GB of free space, so keep that in mind when deciding where to place this directory.

The build system is configured via builder.conf file.
You can use the setup.sh script to create and modify this file.
Alternatively, you can copy the provided default builder.conf, and modify it as needed, e.g.:

```shell
cp example-configs/qubes-os-master.conf builder.conf
# edit the builder.conf file and set the following variables:
NO_SIGN=1
```

One additional useful requirement is that 'sudo root' must work without any prompt, which is default on most distros (e.g. 'sudo bash' brings you the root shell without asking for any password).
This is important as the builder needs to switch to root and then back to user several times during the build process.

Additionally, if building with signing enabled (NO\_SIGN is not set), you must adjust `\~/.rpmmacros` file so that it points to the GPG key used for package signing, e.g.:

```bash
%_signature gpg
%_gpg_path /home/user/.gnupg
%_gpg_name AC1BF9B3  # <-- Key ID used for signing
```

It is also recommended that you use an empty passphrase for the private key used for signing.
Contrary to a popular belief, this doesn't affect your key or sources security -- if somebody compromised your system, then the game is over anyway, whether you have used an additional passphrase for the key or not.

So, to build Qubes you would do:

```shell
# Import the Qubes master key
gpg --recv-keys 0xDDFA1A3E36879494

# Verify its fingerprint, set as 'trusted'.
# This is described here:
# https://www.qubes-os.org/doc/VerifyingSignatures

wget https://keys.qubes-os.org/keys/qubes-developers-keys.asc
gpg --import qubes-developers-keys.asc

git clone https://github.com/QubesOS/qubes-builder.git qubes-builder
cd qubes-builder

# Verify its integrity:
git tag -v `git describe`

cp example-configs/qubes-os-master.conf builder.conf
# edit the builder.conf file and set the following variables:
# NO_SIGN="1"

# Download all components:

make get-sources

# And now to build all Qubes RPMs (this will take a few hours):

make qubes

# ... and then to build the ISO

make iso
```

And this should produce a shiny new ISO.

You can also build selected component separately. Eg. to compile only gui virtualization agent/daemon:

```shell
make gui-daemon
```

You can get a full list from make help.

## Making customized build

### Manual source modification

You can also modify sources somehow if you wish.
Here are some basic steps:

1. Download qubes-builder as described above (if you want to use marmarek's branches, you should also download qubes-builder from his repo - replace 'QubesOS' with 'marmarek' in above git clone command)
2. Edit builder.conf (still the same as above), some useful additions:
  - You can also set GIT\_PREFIX="marmarek/qubes-" to use marmarek's repo instead of "mainstream" - it contains newer (but less tested) versions
3. Download unmodified sources

    ```shell
    make get-sources
    ```

4. **Make your modifications here**

5. Build the Qubes
     `make qubes` actually is just meta target which builds all required
     components in correct order. The list of components is configured in
     builder.conf. You can also check the current value at the end of `make
     help`, or using `make build-info`.

6. `get-sources` is already done, so continue with the next one. You can skip `sign-all` if you've disabled signing

    ```shell
    make vmm-xen core-admin linux-kernel gui-daemon template desktop-linux-kde installer-qubes-os manager linux-dom0-updates
    ```

7. build iso installation image

    ```shell
    make iso
    ```

### Use pre-built Qubes packages

For building just a few selected packages, it's very useful to download pre-built qubes-specific dependencies from `{yum,deb}.qubes-os.org`.
This is especially true for `gcc`, which takes several hours to build.

Before creating the `chroot`, add this to your `builder.conf`:

```
USE_QUBES_REPO_VERSION = $(RELEASE)
```

It will add the 'current' Qubes repository to your `chroot` environment.
Next, specify which components (`gcc`, for example) you want to download instead of compiling:

```
COMPONENTS := $(filter-out gcc,$(COMPONENTS))
```

Alternatively, edit the actual COMPONENTS list which is defined in the included version-dependent config from example-configs (see series of include directives near the beginning of `builder.conf`).
This way, you can build only the packages in which you are interested.

If you also want to use the 'current-testing' repository, add this to your configuration:

```
USE_QUBES_REPO_TESTING = 1
```

In the case of an existing `chroot`, for mock-enabled builds, this works immediately because `chroot` is constructed each time separately.
For legacy builds, it will not add the necessary configuration into the build environment unless a specific builder change or configuration would force rebuilding chroot.

Also, once enabled, disabling this setting will not disable repositories in relevant chroots.
And even if it did, there could be some leftover packages installed from those repos (which may or may not be desirable).

**Note**
If you are building Ubuntu templates, you cannot use this option.
This is because Qubes does not provide official packages for Ubuntu templates.

## Code verification keys management

[QubesBuilder](/doc/qubes-builder/) by default verifies signed tags on every downloaded code.
Public keys used for that are stored in `keyrings/git`.
By default Qubes developers' keys are imported automatically, but if you need some additional keys (for example your own), you can add them using:

```shell
GNUPGHOME=$PWD/keyrings/git gpg --import /path/to/key.asc
GNUPGHOME=$PWD/keyrings/git gpg --edit-key ID_OF_JUST_IMPORTED_KEY
# here use "trust" command to set key fully or ultimately trusted - only those keys are accepted by QubesBuilder
```

All Qubes developers' keys are signed by the Qubes Master Signing Key (which is set as ultimately trusted key), so are trusted automatically.

If you are the owner of Master key and want to revoke such signature, use the `revsig` gpg key edit command and update the key in qubes-developers-keys.asc - now the key will be no longer trusted (unless manually set as such).

## Further information

For advanced [QubesBuilder](/doc/qubes-builder/) use, and preparing sources, take a look at [QubesBuilderDetails](/doc/qubes-builder-details/) page, or [QubesBuilder's doc directory](https://github.com/marmarek/qubes-builder/tree/master/doc).
