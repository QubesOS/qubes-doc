---
lang: en
release: 4.0
reviewed: yes
layout: doc
permalink: /doc/qubes-iso-building/
redirect_from:
- /doc/qubes-r3-building/
- /en/doc/qubes-r3-building/
- /en/doc/qubes-iso-building/
- /doc/QubesR3Building/
- /wiki/QubesR3Building/
ref: 63
title: Qubes ISO building
---

Build Environment
-----------------

Fedora 32 has been successfully used to build Qubes R4.0 with the below steps.
Other rpm-based operating systems may also work.
Travis-CI uses Ubuntu 18.04 to perform test builds, except it can not test the `./setup` script.

In `dom0`, install the Fedora 32 template if you don't already have it.

~~~
sudo qubes-dom0-update qubes-template-fedora-32
~~~

Create a standalone AppVM from the Fedora 32 template.
Set private storage to at least 60 GB if you will be building only the default templates; 100 GB or more if you plan on additional.
It's not required, but if you allocate additional CPU cores, the build process can utilize them at some steps such as the kernel build.
Likewise, more memory (up to 16 GB) can help.
Last, you may want to disable memory balancing, but keep in mind the impact on your other qubes.

Once you've built the development AppVM, open a Terminal window to it and install the necessary dependencies (see [QubesBuilder](/doc/qubes-builder/) for more info):

~~~
$ sudo dnf install git createrepo rpm-build rpm-sign make python3-sh rpmdevtools rpm-sign dialog perl-open python3-pyyaml perl-Digest-MD5 perl-Digest-SHA
~~~

Get the necessary keys to verify the sources (run these and other commands below as a regular user, not root):

~~~
wget https://keys.qubes-os.org/keys/qubes-master-signing-key.asc
gpg --import qubes-master-signing-key.asc
gpg --edit-key 36879494
fpr
# Verify fingerprint! See Note below!
# Once verified, set trust to *ultimate*
# (Typical sequence is trust, 5, q)
wget https://keys.qubes-os.org/keys/qubes-developers-keys.asc
gpg --import qubes-developers-keys.asc
~~~

**Note** In the above process, we do *not* rely on the security of our server (keys.qubes-os.org) nor the connection (ssl, cert) -- we only rely on you getting the Qubes Master Signing Key fingerprint *somehow* and ensuring they match!
See [verifying signatures](/security/verifying-signatures/#how-to-import-and-authenticate-the-qubes-master-signing-key) for verification sources.

Now let's bootstrap the builder. Unfortunately, the builder cannot verify itself (the classic Chicken and Egg problem), so we need to verify the signature manually:

~~~
git clone git://github.com/QubesOS/qubes-builder.git
cd qubes-builder
git tag -v `git describe`
~~~

**Note** It's very important to check if the verification message contains "Good signature from ..." and does not contain "WARNING: This key is not certified with a trusted signature!".

Assuming the verification went fine, we're good to go with all the rest without ever thinking more about verifying digital signatures on all the rest of the components, apart from an additional step if doing a non-scripted build.
The builder will do that for us for each component, every time we build, even for all auxiliary files (e.g. Xen or Linux kernel sources).

Build using setup script
-----------------

Let's configure the builder first (see [procedure](/doc/qubes-iso-building/#build-using-manual-steps) at bottom if you would prefer to manually configure):

~~~
cd ~/qubes-builder
./setup
# Select Yes to add Qubes Master Signing Key
# Select Yes to add Qubes OS Signing Key
# Select 4.0 for version
# Stable
# Select Yes for fast Git cloning
# Select Current (if you want the option to use pre-built packages)
# Select No (we want a full build)
# Select fc30 and buster (for the currently shipping templates)
# Select builder-rpm, builder-debian, template-whonix, mgmt-salt
# Select Yes to add adrelanos's third party key
# Select Yes (to download)
~~~

Once it completes downloading, re-run `setup` to add the Whonix templates:

~~~
./setup
# Choose the same options as above, except at templates select:
# fc30, buster, whonix-gateway-15, whonix-workstation-15
~~~

Continue the build process with:

~~~
make install-deps
make get-sources
~~~

When building the Whonix templates, you will often need to add/update the `WHONIX_TBB_VERSION` variable in `builder.conf` at this stage to specify the currently shipping Tor Browser version.
See the related note under [Extra Whonix Build Options](/doc/building-whonix-template/).

You may also want to add `COMPONENTS := $(filter-out gcc,$(COMPONENTS))` to bypass a multiple hour compile step.
See [QubesBuilder](/doc/qubes-builder/#use-pre-built-qubes-packages) for more detail.

Finally, if you are making a test build, use:

~~~
make qubes
make iso
~~~

Or for a fully signed build (this requires setting `SIGN_KEY` in `builder.conf`):

~~~
make qubes
make sign-all
make iso
~~~

Enjoy your new ISO!

Build using manual steps
-----------------

Instead of using `./setup`, you can manually configure the build.
The script takes care of a lot of the keyring preparation for us, so we first need to set that up.

If you will be building Whonix templates:

~~~
cd ~
gpg --keyserver pgp.mit.edu --recv-keys 916B8D99C38EAF5E8ADC7A2A8D66066A2EEACCDA
gpg --fingerprint 916B8D99C38EAF5E8ADC7A2A8D66066A2EEACCDA
~~~

**Note:** It's very important to check the fingerprint displayed against multiple sources such as the [Whonix web site](https://www.whonix.org/wiki/Whonix_Signing_Key), etc.
It should look something like this:

~~~
pub   4096R/2EEACCDA 2014-01-16 [expires: 2021-04-17]
      Key fingerprint = 916B 8D99 C38E AF5E 8ADC  7A2A 8D66 066A 2EEA CCDA
uid                  Patrick Schleizer <adrelanos@riseup.net>
sub   4096R/CE998547 2014-01-16 [expires: 2021-04-17]
sub   4096R/119B3FD6 2014-01-16 [expires: 2021-04-17]
sub   4096R/77BB3C48 2014-01-16 [expires: 2021-04-17]
~~~

Next, prepare the Git keyring directory and copy them in:

~~~
export GNUPGHOME=~/qubes-builder/keyrings/git
mkdir --parents "$GNUPGHOME"
cp ~/.gnupg/pubring.gpg "$GNUPGHOME"
cp ~/.gnupg/trustdb.gpg "$GNUPGHOME"
chmod --recursive 700 "$GNUPGHOME"
~~~

Copy one of the example configurations:

~~~
cd ~/qubes-builder
cp example-configs/qubes-os-master.conf builder.conf
~~~

Edit `builder.conf`, referring to `doc/Configuration.md` for a description of all available options.

Continue the build process with:

~~~
make install-deps
make get-sources
unset GNUPGHOME
~~~

When building the Whonix templates, you will often need to add/update the `WHONIX_TBB_VERSION` variable at this stage to specify the currently shipping Tor Browser version.
See the related note under [Extra Whonix Build Options](/doc/building-whonix-template/).

Finally, if you are making a test build, use:

~~~
make qubes
make iso
~~~

Or for a fully signed build (this requires setting `SIGN_KEY` in `builder.conf`):

~~~
make qubes
make sign-all
make iso
~~~

Enjoy your new ISO!
