---
layout: doc
title: Dom0SecureUpdates
permalink: /doc/Dom0SecureUpdates/
redirect_from: /wiki/Dom0SecureUpdates/
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

Problems with traditional network-based update mechanisms
---------------------------------------------------------

Dom0 is the most trusted domain on Qubes OS, and for this reason we decided to design Qubes in such a way that Dom0 is not connected to any network. In fact only select domains can be connected to a network via so called network domains. There could also be more than one network domain, e.g. in case the user is connected to more than one physically or logically separated networks.

Secure update mechanism we use in Qubes (starting from Beta 2
-------------------------------------------------------------

Keeping Dom0 not connected to any network makes it hard, however, to provide updates for software in Dom0. For this reason we have come up with the following mechanism for Dom0 updates, which minimizes the amount of untrusted input processed by Dom0 software:

The update process is initiated by [qvm-dom0-update script](http://git.qubes-os.org/?p=joanna/core.git;a=blob;f=dom0/qvm-tools/qvm-dom0-update;h=d6ac222fdc3850a0f1269df27746c9ed6e84c8a9;hb=HEAD), running in Dom0.

Updates (\*.rpm files) are checked and downloaded by UpdateVM, which by default is the same as the firewall VM, but can be configured to be any other, network-connected VM. This is done by [qubes\_download\_dom0\_updates.sh script](http://git.qubes-os.org/?p=joanna/core.git;a=blob;f=common/qubes_download_dom0_updates.sh;h=dfc46123e9c0904d019d3f05008bc3adca21921d;hb=HEAD) (this script is executed using qrexec by the previously mentioned qvm-dom0-update). Note that we assume that this script might get compromised and might download a maliciously compromised downloads -- this is not a problem as Dom0 verifies digital signatures on updates later. The downloaded rpm files are placed in a ```/var/lib/qubes/dom0-updates``` directory on UpdateVM filesystem (again, they might get compromised while being kept there, still this isn't a problem). This directory is passed to yum using the ```--installroot=``` option.

Once updates are downloaded, the update script that runs in UpdateVM requests an RPM service [qubes.ReceiveUpdates](http://git.qubes-os.org/?p=joanna/core.git;a=blob;f=dom0/aux-tools/qubes.ReceiveUpdates;h=7134323902b37a0be41b98ef8dbde61a94b1d189;hb=HEAD) to be executed in Dom0. This service is implemented by [qubes-receive-updates script](http://git.qubes-os.org/?p=joanna/core.git;a=blob;f=dom0/aux-tools/qubes-receive-updates;h=af386090b4a98de7f00736b60b9a1ca16f337822;hb=HEAD) running in Dom0. The Dom0's qvm-dom0-update script (which originally initiated the whole update process) waits until qubes-receive-updates finished.

The qubes-receive-updates script processes the untrusted input from Update VM: it first extracts the received \*.rpm files (that are sent over qrexec data connection) and then verifies digital signature on each file. The qubes-receive-updates script is a security-critical component of the Dom0 update process (as is the [qfile-dom0-unpacker.c](http://git.qubes-os.org/?p=joanna/core.git;a=blob;f=dom0/aux-tools/qfile-dom0-unpacker.c;h=757a2c43ba9e6780e8173b0049b2678efa0fda84;hb=HEAD) and the rpm utility, both used by the qubes-receive-updates for processing the untrusted input.

Once qubes-receive-updates finished unpacking and verifying the updates, the updates are placed in ``qubes-receive-updates`` directory in Dom0 filesystem. Those updates are now trusted. Dom0 is configured (see /etc/yum.conf in Dom0) to use this directory as a default (and only) [yum repository](http://git.qubes-os.org/?p=joanna/core.git;a=blob;f=dom0/qubes-cached.repo;h=963a7ba524d4d63296718161fe4bcd3cad1ff5e7;hb=HEAD).

Finally, qvm-dom0-updates runs ``yum update`` that fetches the rpms from qubes-cached repo and installs them as usual.

Security benefit of our update mechanism
----------------------------------------

The benefit of the above scheme is that one doesn't need to trust the TCP/IP stack, the HTTP stack, and wget implementation in order to safely deliver and install updates in Dom0. One only needs to trust a few hundred lines of code as discussed above, as well as the rpm utility for properly checking digital signature (but this is required in any update scheme).
