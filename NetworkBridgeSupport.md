---
layout: wiki
title: NetworkBridgeSupport
permalink: /wiki/NetworkBridgeSupport/
---

Network Bridge Support (EXPERIMENTAL and UNSUPPORTED)
=====================================================

The Qubes developpement team does not support bridging the network interfaces found in NetVM and don't plan to support it at all. Several reasons for that:

-   Using a bridged VM is almost only necessary for developpers testing or working on OSI layer 2 or layer 3 tools (MAC or routing protocols). If not for testing, such tools are almost only used directly on routers ...).
-   Most of these tools can be anyway used directly inside the NetVM, which has direct access to the network card.
-   It is also possible to use a secondary network card plugged into a specific development VM.
-   Such a setup could break security features of Qubes such as AppVM firewalling.

Now if you really want to work with OSI layer2 / layer 3 tools, that you don't have a secondary network card, or that you want to completely expose services of a given AppVM (at your own risk), a bridged setup may help you.

Qubes manager patch (Qubes R2B3)
--------------------------------

The following patches can be applied to the Qubes Manager GUI in order to add an option to easily bridge a VM. Use it at your own risk. If the patch breaks the Qubes Manager, you can try to restore the qubes packages:

``` {.wiki}
# qubes-dom-update reinstall qubes-core-dom0 qubes-manager
```
