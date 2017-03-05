---
layout: doc
title: Networking
permalink: /doc/networking/
redirect_from:
- /doc/qubes-net/
- /en/doc/qubes-net/
- /doc/QubesNet/
- /wiki/QubesNet/
---

VM network in Qubes
===================

Overall description
-------------------

In Qubes, the standard Xen networking is used, based on backend driver in the driver domain and frontend drivers in VMs. In order to eliminate layer 2 attacks originating from a compromised VM, routed networking is used instead of the default bridging of `vif` devices. The default *vif-route* script had some deficiencies (requires `eth0` device to be up, and sets some redundant iptables rules), therefore the custom *vif-route-qubes* script is used.

The IP address of `eth0` interface in AppVM, as well as two IP addresses to be used as nameservers (`DNS1` and `DNS2`), are passed via xenstore to AppVM during its boot (thus, there is no need for DHCP daemon in the network driver domain). `DNS1` and `DNS2` are private addresses; whenever an interface is brought up in the network driver domain, the */usr/lib/qubes/qubes\_setup\_dnat\_to\_ns* script sets up the DNAT iptables rules translating `DNS1` and `DNS2` to the newly learned real dns servers. This way AppVM networking configuration does not need to be changed when configuration in the network driver domain changes (e.g. user switches to a different WLAN). Moreover, in the network driver domain, there is no DNS server either, and consequently there are no ports open to the VMs.

Routing tables examples
-----------------------

VM routing table is simple:

||
|Destination|Gateway|Genmask|Flags|Metric|Ref|Use|Iface|
|0.0.0.0|0.0.0.0|0.0.0.0|U|0|0|0|eth0|

Network driver domain routing table is a bit longer:

||
|Destination|Gateway|Genmask|Flags|Metric|Ref|Use|Iface|
|10.2.0.16|0.0.0.0|255.255.255.255|UH|0|0|0|vif4.0|
|10.2.0.7|0.0.0.0|255.255.255.255|UH|0|0|0|vif10.0|
|10.2.0.9|0.0.0.0|255.255.255.255|UH|0|0|0|vif9.0|
|10.2.0.8|0.0.0.0|255.255.255.255|UH|0|0|0|vif8.0|
|10.2.0.12|0.0.0.0|255.255.255.255|UH|0|0|0|vif3.0|
|192.168.0.0|0.0.0.0|255.255.255.0|U|1|0|0|eth0|
|0.0.0.0|192.168.0.1|0.0.0.0|UG|0|0|0|eth0|

Location of the network driver domain
-------------------------------------

Traditionally, the network driver domain is dom0. This design means that a lot of code (networking stack, drivers) running in the all-powerful domain is exposed to potential attack. Although it is supported (one can execute *qvm-set-default-netvm dom0*), it is strongly discouraged.

Instead, a dedicated domain called `netvm` should be used. In order to activate it, one needs to install the `qubes-servicevm-netvm` rpm package, and enable it via command *qvm-set-default-netvm netvm*. This domain will be assigned all PCI devices that are network cards. One can interact with the *Networkmanager* daemon running in `netvm` in the same way as with any other VM GUI application (with one detail that *nm-applet* requires a system tray, thus one needs to start it via "KDEMenu-\>Applications-\>Netvm-\>Show Tray").

Note that in order to isolate `netvm` properly, the platform must support VTd and it must be activated. Otherwise, compromised `netvm` can use DMA to get control over dom0 and even the hypervisor.

When using `netvm`, there is no network connectivity in dom0. This is the desired configuration - it eliminates all network-bourne attacks. Observe that dom0 is meant to be used for administrative tasks only, and (with one exception) they do not need network. Anything not related to system administration should be done in one of AppVMs.

The above-mentioned exception is the system packages upgrade. Again, one must not install random applications in dom0, but there is a need to e.g. upgrade existing packages. While one may argue that the new packages could be downloaded on a separate machine and copied to dom0 via a pendrive, this solution has its own problems. Therefore, the advised method to temporarily grant network connectivity to dom0 is to use *qvm-dom0-network-via-netvm up* command. It will pause all running VMs (so that they can do no harm to dom0) and connect dom0 to netvm network just like another AppVM. Having completed package upgrade, execute *qvm-dom0-network-via-netvm down* to revert to the normal state.
