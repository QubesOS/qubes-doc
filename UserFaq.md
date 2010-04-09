---
layout: wiki
title: UserFaq
permalink: /wiki/UserFaq/
---

Qubes User's FAQ
================

### Q: How much memory is recommended for Qubes?

4 GB at least. Sure, you can try it on a system with 2GB, but don't expect to be able to run more than 3 AppVMs at the same time.

### Q: Can I install Qubes on a system without VT-x?

Yes. Xen doesn't use VT-x (not AMD-v) for PV guests virtualization (it uses ring0/3 separation instead). But, of course, without VT-x, you will also not have VT-d -- see the next question.

### Q: Can I install Qubes on a system without VT-d?

Yes you can. You can even run a netvm but, of course, you will not benefit from DMA protection for driver domains. So, on a system without VT-d, everything should work the same, but there is no real security benefit of having a separate netvm, as the attacker can always use a simple DMA attack to go from netvm to Dom0.

The above is in theory -- in practice, if you have a broken network card driver and try to run it in a netvm on a system without VT-d, it might crash your system. This might happen e.g. if the driver is not properly using DMA-API.
