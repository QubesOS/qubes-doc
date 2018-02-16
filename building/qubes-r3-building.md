---
layout: doc
title: Qubes ISO Building
permalink: /doc/qubes-r3-building/
redirect_from:
- /en/doc/qubes-r3-building/
- /doc/QubesR3Building/
- /wiki/QubesR3Building/
---

Building Qubes OS ISO
=========================

In `dom0`, install the Fedora 26 template if you don't already have it.
Other rpm-based operating systems may also work, but Fedora 26 has been successfully used to build Qubes R3.2 and R4.0 with the below steps.

~~~
sudo qubes-dom0-update qubes-template-fedora-26
~~~

Create a standalone appVM from the Fedora 26 template.
You may choose your own name, but this document will refer to it as `dev26`.
Set private storage to at least 60 GB if you will be building only the default templates; 100 GB if you plan on additional.
It's not required, but if you allocate additional CPU cores, the build process can utilize them at some steps such as the kernel build.
Likewise, more memory (up to 16 GB) can help.
Last, you may want to disable memory balancing on `dev26` but keep in mind the impact on your other qubes.

Once you've built `dev26`, open a Terminal window to it and install the necessary dependencies (see [QubesBuilder](/doc/qubes-builder/) for more info):

~~~
$ sudo dnf install git createrepo rpm-build make wget rpmdevtools dialog rpm-sign gnupg dpkg-dev debootstrap python2-sh
~~~

Get the necessary keys to verify the sources:

~~~
$ wget https://keys.qubes-os.org/keys/qubes-master-signing-key.asc
$ gpg --import qubes-master-signing-key.asc 
$ gpg --edit-key 36879494
# Verify fingerprint!, set trust to *ultimate*
# (Typical sequence is fpr, trust, 5, q)
$ wget https://keys.qubes-os.org/keys/qubes-developers-keys.asc
$ gpg --import qubes-developers-keys.asc
~~~

And if you will be building the Whonix templates:

~~~
$ wget https://github.com/QubesOS/qubes-builder-debian/blob/master/keys/whonix-developer-patrick.asc
$ gpg --import whonix-developer-patrick.asc
~~~

**Note** In the above process, we do *not* rely on the security of our server (keys.qubes-os.org) nor the connection (ssl, cert) -- we only rely on you getting the Qubes Master Signing Key fingerprint *somehow* and ensuring they match!
Likewise, the Whonix signing key is available from multiple sources.

Now let's bootstrap the builder. Unfortunately, the builder cannot verify itself (the classic Chicken and Egg problem), so we need to verify the signature manually:

~~~
$ git clone git://github.com/QubesOS/qubes-builder.git
$ mkdir qubes-builder/keyrings
$ mkdir qubes-builder/keyrings/git
$ cp .gnupg/pubring.gpg qubes-builder/keyrings/git/
$ cp .gnupg/trustdb.gpg qubes-builder/keyrings/git/
$ cd qubes-builder
$ git tag -v `git describe`
~~~

Assuming the verification went fine, we're good to go with all the rest without ever thinking more about verifying digital signatures on all the rest of the components.
The builder will do that for us for each component, every time we build, even for all auxiliary files (e.g. Xen or Linux kernel sources).

Let's configure the builder first (see Note at bottom if you would prefer to manually configure):

~~~
$ ./setup
# Select 3.2 or 4.0 for version
# Stable
# No (we want a full build)
# Select builder-fedora, builder-debian, template-whonix, mgmt-salt
# Yes (to download)
# Select fc26, stretch, whonix-gateway, whonix-workstation (for the currently shipping templates)
~~~

Once the download is complete, continue the build process with:

~~~
$ make install-deps
$ make get-sources
~~~

Finally, if you are making a test build, use:

~~~
$ make qubes
$ make iso
~~~

Or for a fully signed build (this requires setting SIGN_KEY in the builder.conf):

~~~
$ make sign-all
$ make iso
~~~

Enjoy your new ISO!


**Note** Instead of using `./setup`, you can manually configure the build by doing `cp example-configs/qubes-os-master.conf builder.conf` and editing `builder.conf`.
Take a look at `builder.conf.default` for a description of all available options.
On manually configured builds, you may also need to:

~~~
export GNUPGHOME=~/qubes-builder/keyrings/git
mkdir --parents "$GNUPGHOME"
chmod --recursive 700 "$GNUPGHOME"
echo '427F11FD0FAA4B080123F01CDDFA1A3E36879494:6:' | gpg --import-ownertrust
~~~
And for the Whonix templates:
~~~
echo '916B8D99C38EAF5E8ADC7A2A8D66066A2EEACCDA:6:' | gpg --import-ownertrust
~~~

