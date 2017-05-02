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

Cooperative Covert Channels Between Domains
-------------------------------------------

Qubes does not attempt to eliminate cooperative covert channels between two or more compromised domains. We don't believe this is possible to achieve on x86 hardware, and we also doubt it makes any sense in practice for most users -- after all, if the two domains are compromised, then it's probably already all lost anyway.

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
