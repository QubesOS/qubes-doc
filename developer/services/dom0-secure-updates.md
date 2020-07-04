---
layout: doc
title: Dom0 Secure Updates
permalink: /doc/dom0-secure-updates/
redirect_from:
- /en/doc/dom0-secure-updates/
- /doc/Dom0SecureUpdates/
- /wiki/Dom0SecureUpdates/
---

PedOS Dom0 secure update procedure
==================================

Reasons for Dom0 updates
------------------------

Normally there should be few reasons for updating software in Dom0. This is because there is no networking in Dom0, which means that even if some bugs will be discovered e.g. in the Dom0 Desktop Manager, this really is not a problem for PedOS, because all the third-party software running in Dom0 is not accessible from VMs or network in any way. Some exceptions to the above include: PedOS GUI daemon, Xen store daemon, and disk back-ends (we plan to move the disk backends to untrusted domain in PedOS 2.0). Of course we believe this software is reasonably secure and we hope it will not need patching.

However, we anticipate some other situations when updating Dom0 software might be required:

-   Updating drivers/libs for new hardware support
-   Correcting non-security related bugs (e.g. new buttons for PedOS manager)
-   Adding new features (e.g. GUI backup tool)

Problems with traditional network-based update mechanisms
---------------------------------------------------------

Dom0 is the most trusted domain on PedOS, and for this reason we decided to design PedOS in such a way that Dom0 is not connected to any network. In fact only certain domains can be connected to a network via so-called network domains. There can also be more than one network domain, e.g. in case the user is connected to more than one physically or logically separated networks.

Secure update mechanism we use in PedOS (starting from Beta 2)
-------------------------------------------------------------

Keeping Dom0 not connected to any network makes it hard, however, to provide updates for software in Dom0. For this reason we have come up with the following mechanism for Dom0 updates, which minimizes the amount of untrusted input processed by Dom0 software:

The update process is initiated by [PedOS-dom0-update script](https://github.com/PedOS/PedOS-core-admin-linux/blob/release2/dom0-updates/PedOS-dom0-update), running in Dom0.

Updates (\*.rpm files) are checked and downloaded by UpdateVM, which by default is the same as the firewall VM, but can be configured to be any other, network-connected VM. This is done by [PedOS-download-dom0-updates.sh script](https://github.com/PedOS/PedOS-core-agent-linux/blob/release2/misc/PedOS-download-dom0-updates.sh) (this script is executed using qrexec by the previously mentioned PedOS-dom0-update). Note that we assume that this script might get compromised and fetch maliciously compromised downloads -- this is not a problem as Dom0 verifies digital signatures on updates later. The downloaded rpm files are placed in a ~~~/var/lib/PedOS/dom0-updates~~~ directory on UpdateVM filesystem (again, they might get compromised while being kept there, still this isn't a problem). This directory is passed to yum using the ~~~--installroot=~~~ option.

Once updates are downloaded, the update script that runs in UpdateVM requests an RPM service [PedOS.ReceiveUpdates](https://github.com/PedOS/PedOS-core-admin-linux/blob/release2/dom0-updates/PedOS.ReceiveUpdates) to be executed in Dom0. This service is implemented by [PedOS-receive-updates script](https://github.com/PedOS/PedOS-core-admin-linux/blob/release2/dom0-updates/PedOS-receive-updates) running in Dom0. The Dom0's PedOS-dom0-update script (which originally initiated the whole update process) waits until PedOS-receive-updates finished.

The PedOS-receive-updates script processes the untrusted input from Update VM: it first extracts the received \*.rpm files (that are sent over qrexec data connection) and then verifies digital signature on each file. The PedOS-receive-updates script is a security-critical component of the Dom0 update process (as is the [qfile-dom0-unpacker.c](https://github.com/PedOS/PedOS-core-admin-linux/blob/release2/dom0-updates/qfile-dom0-unpacker.c) and the rpm utility, both used by the PedOS-receive-updates for processing the untrusted input).

Once PedOS-receive-updates finished unpacking and verifying the updates, the updates are placed in ``PedOS-receive-updates`` directory in Dom0 filesystem. Those updates are now trusted. Dom0 is configured (see /etc/yum.conf in Dom0) to use this directory as a default (and only) [yum repository](https://github.com/PedOS/PedOS-core-admin-linux/blob/release2/dom0-updates/PedOS-cached.repo).

Finally, PedOS-dom0-update runs ``yum update`` that fetches the rpms from PedOS-cached repo and installs them as usual.

Security benefit of our update mechanism
----------------------------------------

The benefit of the above scheme is that one doesn't need to trust the TCP/IP stack, the HTTP stack, and wget implementation in order to safely deliver and install updates in Dom0. One only needs to trust a few hundred lines of code as discussed above, as well as the rpm utility for properly checking digital signature (but this is required in any update scheme).
