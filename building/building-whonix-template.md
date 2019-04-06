---
layout: doc
title: Building Whonix Templates
permalink: /doc/building-whonix-template/
redirect_from:
- /en/doc/building-whonix-template/
---

## Building Whonix Templates

The Whonix templates are easily downloaded and installed by following the [procedure here](https://www.whonix.org/wiki/Qubes/Install).
However, they are integrated into `qubes-builder` so they are straight-forward to build yourself if you prefer.

Many other Qubes templates can also be built by following this procedure.
Simply choose the appropriate builder(s) and template(s) you wish to build in the `./setup` procedure below.
Always include the `mgmt-salt` builder.

First, set up the [Build Environment](/doc/qubes-r3-building/#build-environment) (follow the build environment section only).

Next, configure the builder:

~~~
cd ~/qubes-builder
./setup
# Select Yes to add Qubes Master Signing Key
# Select Yes to add Qubes OS Signing Key
# Select 4.0 for version
# Stable
# Select Current (if you want to use pre-built packages instead of compiling for hours)
# Yes (we want to build only templates)
# Select fc29 and stretch (for the currently shipping templates)
# Select builder-rpm, builder-debian, template-whonix, mgmt-salt
# Yes (to download)
~~~

Once it completes downloading, re-run `setup` to add the Whonix templates:

~~~
./setup
# Choose the same options as above, except at templates select:
# whonix-gateway-14, whonix-workstation-14
# If prompted, choose Yes to add adrelanos's third party key
~~~
Continue the build process with:

~~~
make install-deps
make get-sources
~~~

You will often need to edit/update `qubes-src/template-whonix/builder.conf` at this stage to specify the currently shipping Tor Browser version.
Open it in your favorite editor, then look for "Extra Whonix Build Options" and add/edit the `WHONIX_TBB_VERSION` variable to specify the current version.
For example:

```
################################################################################
# Extra Whonix Build Options
################################################################################

# Whonix repository.
WHONIX_APT_REPOSITORY_OPTS ?= stable
#WHONIX_APT_REPOSITORY_OPTS = off

# Use turbo mode to build template
BUILDER_TURBO_MODE ?= 1

# Enable Tor by default (0: disable; 1: enable)
WHONIX_ENABLE_TOR ?= 0

WHONIX_TBB_VERSION ?= 7.5.2
```

You can add/edit the `WHONIX_TBB_VERSION` variable in `~/qubes-builder/builder.conf` instead of this file if preferred.

Finally, use:

~~~
make qubes-vm
make template
~~~
 
Once the build is complete, the install packages for your newly built templates will be located in `~/qubes-builder/qubes-src/linux-template-builder/rpm/noarch`.
Copy them from there to dom0 and install:

~~~
qvm-run --pass-io <src-vm> 'cat ~/qubes-builder/qubes-src/linux-template-builder/rpm/noarch/qubes-template-whonix-gw-4.0.0-201802250036.noarch.rpm' > ~/qubes-template-whonix-gw-4.0.0-201802250036.noarch.rpm
qvm-run --pass-io <src-vm> 'cat ~/qubes-builder/qubes-src/linux-template-builder/rpm/noarch/qubes-template-whonix-ws-4.0.0-201802250145.noarch.rpm' > ~/qubes-template-whonix-ws-4.0.0-201802250145.noarch.rpm
sudo dnf install qubes-template-whonix-gw-4.0.0-201802250036.noarch.rpm
sudo dnf install qubes-template-whonix-ws-4.0.0-201802250145.noarch.rpm
~~~

And you are done!


