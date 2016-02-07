---
layout: doc
title: Building Archlinux Template
permalink: /doc/building-archlinux-template/
redirect_from:
- /en/doc/building-archlinux-template/
- /doc/BuildingArchlinuxTemplate/
- /wiki/BuildingArchlinuxTemplate/
---

Template building
=================

The archlinux VM is now almost working as a NetVM. Based on qubes-builder code, you could find below how to build it and problem that could arise from template building to using archlinux as a netvm:

Download qubes-builder git code
-------------------------------

Prefer the [marmarek git repository](https://github.com/marmarek/qubes-builder) as it is the most recent one.

~~~
git clone https://github.com/marmarek/qubes-builder.git
~~~

Change your builder.conf
------------------------

Change the following variables / add the following lines (as appropriate):

~~~
BUILDER_PLUGINS += builder-archlinux
GIT_PREFIX := marmarek/qubes-
DISTS_VM += archlinux
~~~

If you don't already have a `builder.conf` in the root of your qubes-builder
directory, a basic Archlinux template build may be achieved by copying
`example-configs/debian.conf` and making the above changes (don't forget to
also comment out any Debian-related `DISTS_VM += ` lines).

Get all required sources
------------------------

~~~
make get-sources
~~~

Note that make get-sources sometimes fails because it didn't download packages that are not used by archlinux such as xfce or kde packages.

You can ignore the repositories that are failing by adding the following line to your builder.conf:

~~~
COMPONENTS:=$(filter-out desktop-linux-kde desktop-linux-xfce,$(COMPONENTS))
~~~

Just don't forget that you need to comment this line again if you want to build the whole Qubes-OS install CD.

Make all required Qubes components
----------------------------------

The first use of the builder can take several hours depending on your bandwidth as it will install an archlinux chroot:

~~~
make qubes-vm
~~~

Now build the template itself
-----------------------------

This can take again several hours, especially the first time you built and archlinux template:

~~~
make linux-template-builder
~~~

Retrieve your template
----------------------

You can now find your template in qubes-src/linux-template-builder/rpm/noarch. Install it in dom0 (just take care as it will replace your current archlinux-x64 template)

* * * * *

Known problems during building or when running the VM
=====================================================

Build fails when fetching qubes-mgmt-salt
-----------------------------------------

The `qubes-mgmt-salt` repo is not currently forked under the marmarek user on
GitHub, to whom the above instructions set the `GIT_PREFIX`.  As Archlinux is
not yet supported by mgmt-salt, simply leave it out of the build (when building
the Archlinux template on it's own) by appending the following to your
`builder.conf`:

~~~
BUILDER_PLUGINS := $(filter-out mgmt-salt,$(BUILDER_PLUGINS))
~~~

The nm-applet (network manager icon) fails to start when archlinux is defined as a template-vm:
-----------------------------------------------------------------------------------------------

In fact /etc/dbus-1/system.d/org.freedesktop.NetworkManager.conf does not allow a standard user to run network manager clients. To allow this, one need to change inside \<policy context="default"\>:

~~~
<deny send_destination="org.freedesktop.NetworkManager"/>
~~~

to

~~~
<allow send_destination="org.freedesktop.NetworkManager"/>
~~~

DispVM, Yum proxy and most Qubes addons (thunderbird ...) have not been tested at all.
--------------------------------------------------------------------------------------

The sound does not work in AppVMs and there are messages related to pulse segfault in glibc when running dmesg (FIXED)
----------------------------------------------------------------------------------------------------------------------

This is apparently a bug in Archlinux between glibc and pulseaudio package 4.0-6. The packages pulseaudio-4.0-2 and libpulse-4.0-2 are known to work and can be downloaded and reinstalled manually.

Error when building the gui-agent-linux with pulsecore error
------------------------------------------------------------

~~~
module-vchan-sink.c:62:34: fatal error: pulsecore/core-error.h: No such file or directory
 #include <pulsecore/core-error.h>
~~~

This error is because Archlinux update package too quickly. Probably, a new version of pulseaudio has been released, but the qubes team has not imported the new development headers yet.

You can create fake new headers just by copying the old headers:

~~~
cd qubes-builder/qubes-src/gui-agent-linux/pulse
ls
cp -r pulsecore-#lastversion pulsecore-#archlinuxversion
~~~

You can check the current archlinux pulseaudio version like this:

~~~
sudo chroot chroot-archlinux/ pacman -Qi pulseaudio
~~~

chroot-archlinux/dev/pts has not been unmounted
-----------------------------------------------

This is a known problem when there are errors during building. Check what is mounted using the command mount (with no parameters). Just unmount what you can (or reboot your vm if you are too lazy :) )

Known problems in Qubes R2-B2
=============================

xen-vmm-vm fail to build with a PARSETUPLE related error (FIXED):
-----------------------------------------------------------------

Commenting out "\#define HAVE\_ATTRIBUTE\_FORMAT\_PARSETUPLE" from chroot\_archlinux/usr/include/python2.7/pyconfig.h fixes the problem, but it isn't the right solution [1]...

A better fix is planned for the next python release (the bug is considered release blocking), and will be updated in archlinux chroot as soon as available.

[1] [http://bugs.python.org/issue17547](http://bugs.python.org/issue17547)

The boot process fails without visible errors in the logs, but spawn a recovery shell
-------------------------------------------------------------------------------------

The problem is a new conflict between systemd and the old sysvinit style. To fix this, you can change the master xen template in dom0 to remove sysvinit remains: Edit **INSIDE DOM0** /usr/share/qubes/vm-template.conf, and change the variable 'extra' that contains the kernel variables: from:

~~~
extra="ro nomodeset 3 console=hvc0 rd_NO_PLYMOUTH {kernelopts}"
~~~

to:

~~~
extra="ro nomodeset console=hvc0 rd_NO_PLYMOUTH {kernelopts}"
~~~

Qubes-OS is now using different xenstore variable names, which makes to archlinux VM failing to boot
----------------------------------------------------------------------------------------------------

Apply the following fix in the template to revert the variable name to the old Qubes version.

You can edit the template the following way:

~~~
sudo mkdir /mnt/vm
sudo mount /var/lib/qubes/vm-templates/archlinux-x64/root.img /mnt/vm
sudo chroot /mnt/vm
~~~

Then apply the fix:

~~~
sudo sed 's:qubes-keyboard:qubes_keyboard:g' -i /etc/X11/xinit/xinitrc.d/qubes-keymap.sh

sudo sed 's:qubes-netvm-domid:qubes_netvm_domid:g' -i /etc/NetworkManager/dispatcher.d/30-qubes-external-ip
sudo sed 's:qubes-netvm-external-ip:qubes_netvm_external_ip:g' -i /etc/NetworkManager/dispatcher.d/30-qubes-external-ip

sudo sed 's:qubes-netvm-network:qubes_netvm_network:g' -i /usr/lib/qubes/init/network-proxy-setup.sh
sudo sed 's:qubes-netvm-gateway:qubes_netvm_gateway:g' -i /usr/lib/qubes/init/network-proxy-setup.sh
sudo sed 's:qubes-netvm-netmask:qubes_netvm_netmask:g' -i /usr/lib/qubes/init/network-proxy-setup.sh
sudo sed 's:qubes-netvm-secondary-dns:qubes_netvm_secondary_dns:g' -i /usr/lib/qubes/init/network-proxy-setup.sh

sudo sed 's:qubes-vm-type:qubes_vm_type:g' -i /usr/lib/qubes/init/qubes-sysinit.sh

sudo sed 's:qubes-ip:qubes_ip:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-netmask:qubes_netmask:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-gateway:qubes_gateway:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-secondary-dns:qubes_secondary_dns:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-netvm-network:qubes_netvm_network:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-netvm-gateway:qubes_netvm_gateway:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-netvm-netmask:qubes_netvm_netmask:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-netvm-secondary-dns:qubes_netvm_secondary_dns:g' -i /usr/lib/qubes/setup-ip

sudo sed 's:qubes-iptables-domainrules:qubes_iptables_domainrules:g' -i /usr/bin/qubes-firewall
sudo sed 's:qubes-iptables-header:qubes_iptables_header:g' -i /usr/bin/qubes-firewall
sudo sed 's:qubes-iptables-error:qubes_iptables_error:g' -i /usr/bin/qubes-firewall
sudo sed 's:qubes-iptables:qubes_iptables:g' -i /usr/bin/qubes-firewall

sudo sed 's:qubes-netvm-domid:qubes_netvm_domid:g' -i /usr/bin/qubes-netwatcher
sudo sed 's:qubes-netvm-external-ip:qubes_netvm_external_ip:g' -i /usr/bin/qubes-netwatcher
sudo sed 's:qubes-vm-updateable:qubes_vm_updateable:g' -i /usr/lib/qubes/qubes_trigger_sync_appmenus.sh

sudo sed 's:qubes-vm-type:qubes_vm_type:g' -i /usr/bin/qubes-session
sudo sed 's:qubes-vm-updateable:qubes_vm_updateable:g' -i /usr/bin/qubes-session
~~~

Do not forgot to:

~~~
umount /mnt/vm
~~~

Installing the template in dom0 fails because of a missing dependency (qubes-core-dom0-linux)
---------------------------------------------------------------------------------------------

Again you built a template based on a recent Qubes API which has not been released yet. So skip the dependency for now:

~~~
sudo rpm -U --nodeps yourpackage.rpm
~~~
