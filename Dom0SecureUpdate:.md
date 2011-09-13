---
layout: wiki
title: Dom0SecureUpdate:
permalink: /wiki/Dom0SecureUpdate:/
---

Qubes Dom0 secure update procedure
==================================

Reasons for Dom0 updates
------------------------

Normally there should be few reasons for updating software in Dom0. This is because there is no networking in Dom0, which means that even if some bugs will be discovered e.g. in the Dom0 Desktop Manager, this really is not a problem for Qubes, because all the 3rd party software running in Dom0 is not accessible from VMs or network in any way. Some exceptions to the above include: Qubes GUI daemon, Xen store daemon, and disk back-ends (we plan move the disk backends to untrusted domain in Qubes 2.0). Of course we believe this software is reasonably secure and we hope it will not need patching.

However, we anticipate some other situations when updating Dom0 software might be required:

-   Updating drivers/libs for new hardware support
-   Correcting non-security related bugs (e.g. new buttons for qubes manager)
-   Adding new features (e.g. GUI backup tool)

Problems with traditional network-based update mechnisms
--------------------------------------------------------

TODO

Secure update mechanism we use in Qubes (starting from Beta 2
-------------------------------------------------------------

TODO
