---
lang: en
layout: doc
permalink: /doc/4.0/4.0/networking/
redirect_from:
- /doc/qubes-net/
- /en/doc/qubes-net/
- /doc/QubesNet/
- /wiki/QubesNet/
ref: 59
title: Networking
---

## Overall description

In Qubes, the standard Xen networking is used, based on backend driver in the driver domain and frontend drivers in VMs. In order to eliminate layer 2 attacks originating from a compromised VM, routed networking is used instead of the default bridging of `vif` devices and NAT is applied at each network hop. The default *vif-route* script had some deficiencies (requires `eth0` device to be up, and sets some redundant iptables rules), therefore the custom *vif-route-qubes* script is used.

The IP address of `eth0` interface in AppVM, as well as two IP addresses to be used as nameservers (`DNS1` and `DNS2`), are passed via QubesDB to AppVM during its boot (thus, there is no need for DHCP daemon in the network driver domain). `DNS1` and `DNS2` are private addresses; whenever an interface is brought up in the network driver domain, the */usr/lib/qubes/qubes\_setup\_dnat\_to\_ns* script sets up the DNAT iptables rules translating `DNS1` and `DNS2` to the newly learned real dns servers. This way AppVM networking configuration does not need to be changed when configuration in the network driver domain changes (e.g. user switches to a different WLAN). Moreover, in the network driver domain, there is no DNS server either, and consequently there are no ports open to the VMs.

## Routing tables examples

VM routing table is simple:

||
|Destination|Gateway|Genmask|Flags|Metric|Ref|Use|Iface|
|0.0.0.0|0.0.0.0|0.0.0.0|U|0|0|0|eth0|

Network driver domain routing table is a bit longer:

||
|Destination|Gateway|Genmask|Flags|Metric|Ref|Use|Iface|
|10.137.0.16|0.0.0.0|255.255.255.255|UH|0|0|0|vif4.0|
|10.137.0.7|0.0.0.0|255.255.255.255|UH|0|0|0|vif10.0|
|10.137.0.9|0.0.0.0|255.255.255.255|UH|0|0|0|vif9.0|
|10.137.0.8|0.0.0.0|255.255.255.255|UH|0|0|0|vif8.0|
|10.137.0.12|0.0.0.0|255.255.255.255|UH|0|0|0|vif3.0|
|192.168.0.0|0.0.0.0|255.255.255.0|U|1|0|0|eth0|
|0.0.0.0|192.168.0.1|0.0.0.0|UG|0|0|0|eth0|

## IPv6

Starting with Qubes 4.0, there is opt-in support for IPv6 forwarding. Similar to the IPv4, traffic is routed and NAT is applied at each network gateway. This way we avoid reconfiguring every connected qube whenever uplink connection is changed, and even telling the qube what that uplink is - which may be complex when VPN or other tunneling services are employed.
The feature can be enabled on any network-providing qube, and will be propagated down the network tree, so every qube connected to it will also have IPv6 enabled.
To enable the `ipv6` feature use `qvm-features` tool and set the value to `1`. For example to enable it on `sys-net`, execute in dom0:

```
qvm-features sys-net ipv6 1
```

It is also possible to explicitly disable IPv6 support for some qubes, even if it is connected to IPv6-providing one. This can be done by setting `ipv6` feature to empty value:

```
qvm-features ipv4-only-qube ipv6 ''
```

This configuration is presented below - green qubes have IPv6 access, red one does not.

![ipv6-1](/attachment/doc/ipv6-1.png)

In that case, system uplink connection have native IPv6. But in some cases it may not be true. Then some tunneling solution can be used (for example teredo). The same will apply when the user is connected to VPN service providing IPv6 support, regardless of user's internet connection.
Such configuration can be expressed by enabling `ipv6` feature only on some subset of Qubes networking, for example by creating separate qube to encapsulate IPv6 traffic and setting `ipv6` to `1` only there. See diagram below

![ipv6-2](/attachment/doc/ipv6-2.png)

Besides enabling IPv6 forwarding, standard Qubes firewall can be used to limit what network resources are available to each qube. Currently only `qvm-firewall` command support adding IPv6 rules, GUI firewall editor will have this ability later.

### Limitations

Currently only IPv4 DNS servers are configured, regardless of `ipv6` feature state. It is done this way to avoid reconfiguring all connected qubes whenever IPv6 DNS becomes available or not. Configuring qubes to always use IPv6 DNS and only fallback to IPv4 may result in relatively long timeouts and poor usability.
But note that DNS using IPv4 does not prevent to return IPv6 addresses. In practice this is only a problem for IPv6-only networks.
