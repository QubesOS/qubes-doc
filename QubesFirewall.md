---
layout: wiki
title: QubesFirewall
permalink: /wiki/QubesFirewall/
---

Using Quebes Firewall
=====================

How to edit rules
-----------------

In order to edit rules for a given domain, select this domain in the Qubes Manager and press the "policeman's helmet" button.

See the screenshot [​here](http://www.qubes-os.org/files/screenshots/release-1-beta-1/snapshot25.png).

Note that if you specify a rule by DNS name it will be resolved to IP(s) *at the moment of applying the rules*, and not on the fly for each new connection. This means it will not work for serves using load balancing. More on this in the message quoted below.

Understanding firewalling in Qubes
----------------------------------

For now, see this message:

-   [​https://groups.google.com/group/qubes-devel/browse\_thread/thread/9e231b0e14bf9d62](https://groups.google.com/group/qubes-devel/browse_thread/thread/9e231b0e14bf9d62)

