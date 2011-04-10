---
layout: wiki
title: SoftwareUpdateVM
permalink: /wiki/SoftwareUpdateVM/
---

Installing and updating software in VMs
=======================================

How Template VM works in Qubes
------------------------------

Most of the AppVMs (domains) are based on a *template VM*, which means that their root filesystem (i.e. all the programs and system files) is based on the root filesystem of the corresponding template VM. This dramatically saves disk space, because each new AppVM needs disk space only for storing the user's files (i.e. the home directory). Of course the AppVM has only read-access to the template's filesystem -- it cannot modify it in any way.

In addition to saving on the disk space, and reducing domain creation time, another advantage of such scheme is the possibility for centralized software update. It's just enough to do the update in the template VM, and then all the AppVMs based on this template get updates automatically after they are restarted.

The default template in Qubes R1 is called **fedora-14-x64**.

"Outdated" VMs
--------------

TODO

Standalone VMs
--------------

TODO

Using more than one template
----------------------------

TODO
