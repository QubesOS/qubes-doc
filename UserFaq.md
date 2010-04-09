---
layout: wiki
title: UserFaq
permalink: /wiki/UserFaq/
---

Qubes User's FAQ
================

### Q: Can I install Qubes on a system without VT-d?

Yes you can. You can even run a netvm but, of course, you will not benefit from DMA protection for driver domains. So, on a system without VT-d, everything should work the same, but there is no real security benefit of having a separate netvm, as the attacker can always use a simple DMA attack to go from netvm to Dom0.

The above is in theory -- in practice, if you have a broken network card driver and try to run it in a netvm on a system without VT-d, it might crash your system. This might happen e.g. if the driver is not properly using DMA-API.
