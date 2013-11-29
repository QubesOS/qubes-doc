---
layout: wiki
title: BuildingArchlinuxTemplate
permalink: /wiki/BuildingArchlinuxTemplate/
---

Template building
=================

The archlinux VM is now almost working as a NetVM. Based on qubes-builder code, you could find below how to build it and problem that could arise from template building to using archlinux as a netvm:

Download qubes-builder git code
-------------------------------

Prefer marmarek git repository as it is the most recent one

Change your builder.conf
------------------------

Change the following variables GIT\_SUBDIR=marmarek DISTS\_VM=archlinux

Get all required sources
------------------------

``` {.wiki}
make get-sources
```

Make all required qubes components
----------------------------------

The first use of the builder can take several hours depending on your bandwidth as it will install an archlinux chroot:

``` {.wiki}
make vmm-xen-vm
make core-vchan-xen-vm
make linux-utils-vm
make core-agent-linux-vm
make gui-common-vm
make gui-agent-linux-vm
```

Now build the template itself
-----------------------------

This can take again several hours, especially the first time you built and archlinux template:

``` {.wiki}
make linux-template-builder
```

Retrieve your template
----------------------

You can now find your template in qubes-src/linux-template-builder/rpm/noarch. Install it in dom0 (just take care as it will replace your current archlinux-x64 template)

* * * * *

Known problems during building or when running the VM
=====================================================

Can't open file archlinux-2013.02.01-dual.iso
---------------------------------------------

Archlinux ISO files are sometimes removed from mirrors. Check the last version available on the archlinux mirror (eg: [​http://mir.archlinux.fr/iso/](http://mir.archlinux.fr/iso/)), and update qubes-src/linux-template-builder/scripts\_archlinux/00\_prepare.sh accordingly:

``` {.wiki}
ISO_VERSION=2013.06.01
```

You will also need to download the signature matching this ISO version inside qubes-src/linux-template-builder/scripts\_archlinux/:

``` {.wiki}
wget http://mir.archlinux.fr/iso/2013.06.01/archlinux-2013.06.01-dual.iso.sig
```

xen-vmm-vm fail to build with a PARSETUPLE related error (FIXED):
-----------------------------------------------------------------

Commenting out "\#define HAVE\_ATTRIBUTE\_FORMAT\_PARSETUPLE" from chroot\_archlinux/usr/include/python2.7/pyconfig.h fixes the problem, but it isn't the right solution [1]...

A better fix is planned for the next python release (the bug is considered release blocking), and will be updated in archlinux chroot as soon as available.

[1] [​http://bugs.python.org/issue17547](http://bugs.python.org/issue17547)

The boot process fails without visible errors in the logs, but spawn a recovery shell
-------------------------------------------------------------------------------------

The problem is a new conflict between systemd and the old sysvinit style. To fix this, you can change the master xen template in dom0 to remove sysvinit remains: Edit **INSIDE DOM0** /usr/share/qubes/vm-template.conf, and change the variable 'extra' that contains the kernel variables: from:

``` {.wiki}
extra="ro nomodeset 3 console=hvc0 rd_NO_PLYMOUTH {kernelopts}"
```

to:

``` {.wiki}
extra="ro nomodeset console=hvc0 rd_NO_PLYMOUTH {kernelopts}"
```

Qubes-OS is now using different xenstore variable names, which makes to archlinux VM failing to boot
----------------------------------------------------------------------------------------------------

Apply the following fix in the template to revert the variable name to the old Qubes version.

You can edit the template the following way:

``` {.wiki}
sudo mkdir /mnt/vm
sudo mount /var/lib/qubes/vm-templates/archlinux-x64/root.img /mnt/vm
sudo chroot /mnt/vm
```

Then apply the fix:

``` {.wiki}
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
```

Do not forgot to:

``` {.wiki}
umount /mnt/vm
```

The nm-applet (network manager icon) fails to start when archlinux is defined as a template-vm:
-----------------------------------------------------------------------------------------------

In fact /etc/dbus-1/system.d/org.freedesktop.[NetworkManager?](/wiki/NetworkManager).conf does not allow a standard user to run network manager clients. To allow this, one need to change inside \<policy context="default"\>:

``` {.wiki}
<deny send_destination="org.freedesktop.NetworkManager"/>
```

to

``` {.wiki}
<allow send_destination="org.freedesktop.NetworkManager"/>
```

DispVM, Yum proxy and most Qubes addons (thunderbird ...) have not been tested at all.
--------------------------------------------------------------------------------------

Installing the template in dom0 fails because of a missing dependency (qubes-core-dom0-linux)
---------------------------------------------------------------------------------------------

Again you built a template based on a recent Qubes API which has not been released yet. So skip the dependency for now:

``` {.wiki}
sudo rpm -U --nodeps yourpackage.rpm
```

chroot-archlinux/dev/pts has not been unmounted
-----------------------------------------------

This is a known problem when there are errors during building. Just unmount what you can (or reboot your vm if you are too lazy :) )

Error when building the gui-agent-linux
---------------------------------------

``` {.wiki}
module-vchan-sink.c:62:34: fatal error: pulsecore/core-error.h: No such file or directory
 #include <pulsecore/core-error.h>
```

This error is because Archlinux update package too quickly. Probably, a new version of pulseaudio has been released, but the qubes team has not imported the new development headers yet.

You can create fake new headers just by copying the old headers:

``` {.wiki}
cd qubes-builder/qubes-src/gui-agent-linux/pulse
ls
cp -r pulsecore-#lastversion pulsecore-#archlinuxversion
```

You can check the current archlinux pulseaudio version like this:

``` {.wiki}
sudo chroot chroot-archlinux/ pacman -Qi pulseaudio
```

The sound does not work in AppVMs and there are messages related to pulse segfault in glibc when running dmesg
--------------------------------------------------------------------------------------------------------------

This is apparently a bug in Archlinux pulseaudio package 4.0-6. The packages pulseaudio-4.0-2 and libpulse-4.0-2 are known to work and can be downloaded and reinstalled manually.
