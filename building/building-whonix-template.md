---
layout: doc
title: Building Whonix Templates
permalink: /doc/building-whonix-template/
redirect_from:
- /en/doc/building-whonix-template/
---

## Building Whonix Templates

The Whonix templates are easily downloaded and installed by following the [procedure here](doc/whonix/install/).
However, they are integrated into `qubes-builder` so they are easy to build yourself if you prefer.
Note that you will need to create `anon-whonix` yourself if you do so, but see [this issue](qubes-issues/issues/3601).

First, create the [Build Environment](doc/qubes-r3-building/) (follow the build environment section only).

Next, configure the builder:

~~~
cd ~/qubes-builder
./setup
# Select Yes to add Qubes Master Signing Key
# Select Yes to add Qubes OS Signing Key
# Select 3.2 or 4.0 for version
# Stable
# Yes (we want to build only templates)
# Select builder-fedora, builder-debian, template-whonix, mgmt-salt (builder will complain if you don't include builder-fedora, but we don't actually use it)
# Choose Yes to add adrelanos@riseup.net third party key
# Yes (to download)
# Select whonix-gateway, whonix-workstation (for the currently shipping templates)
~~~

Continue the build process with:

~~~
make install-deps
make get-sources
~~~

Finally, use:

~~~
make qubes-vm
make template
~~~
 
