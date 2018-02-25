---
layout: doc
title: Building Whonix Templates
permalink: /doc/building-whonix-template/
redirect_from:
- /en/doc/building-whonix-template/
---

## Building Whonix Templates

The Whonix templates are easily downloaded and installed by following the [procedure here](/doc/whonix/install/).
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
# Select 3.2 or 4.0 for version
# Stable
# Yes (we want to build only templates)
# Select builder-fedora, builder-debian, template-whonix, mgmt-salt (setup won't let you continue if you don't include builder-fedora, but we don't actually use it)
# Choose Yes to add adrelanos's third party key
# Yes (to download sources)
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
 
Once the build is complete, the install packages for your newly built templates will be located in `/qubes-builder/qubes-src/linux-template-builder/rpm/noarch`.
Copy them from there to dom0 and install:

~~~
qvm-run --pass-io <src-vm> 'cat ~/qubes-builder/qubes-src/linux-template-builder/rpm/noarch/qubes-template-whonix-gw-4.0.0-201802250036.noarch.rpm' > ~/qubes-template-whonix-gw-4.0.0-201802250036.noarch.rpm
qvm-run --pass-io <src-vm> 'cat ~/qubes-builder/qubes-src/linux-template-builder/rpm/noarch/qubes-template-whonix-ws-4.0.0-201802250145.noarch.rpm' > ~/qubes-template-whonix-ws-4.0.0-201802250145.noarch.rpm
sudo dnf install qubes-template-whonix-gw-4.0.0-201802250036.noarch.rpm
sudo dnf install qubes-template-whonix-ws-4.0.0-201802250145.noarch.rpm
~~~

And you are done!


