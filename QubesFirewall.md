---
layout: wiki
title: QubesFirewall
permalink: /wiki/QubesFirewall/
---

Understanding Qubes networking and firewall
===========================================

Understanding firewalling in Qubes
----------------------------------

Every AppVM in Qubes is connected to the network via a FirewallVM, which is used to enforce network-level policies. By default there is one default Firewall VM, but the user is free to create more, if needed.

For more information, see the following:

-   [​https://groups.google.com/group/qubes-devel/browse\_thread/thread/9e231b0e14bf9d62](https://groups.google.com/group/qubes-devel/browse_thread/thread/9e231b0e14bf9d62)
-   [​http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html](http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html)

How to edit rules
-----------------

In order to edit rules for a given domain, select this domain in the Qubes Manager and press the "firewall" button:

[Screenshot]

Note that if you specify a rule by DNS name it will be resolved to IP(s) *at the moment of applying the rules*, and not on the fly for each new connection. This means it will not work for serves using load balancing. More on this in the message quoted below.

Alternatively, one can use the `qvm-firewall` command from Dom0 to edit the firewall rules by hand:
