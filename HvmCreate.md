---
layout: wiki
title: HvmCreate
permalink: /wiki/HvmCreate/
---

Creating and using HVM (fully virtualized) domains in Qubes 2
=============================================================

What are HVM domains?
---------------------

HVM domains (Hardware VM), in contrast to PV domains (Paravirtualized domains), allow to create domains based on any OS, if one only has its installation ISO. E.g. this allows to have Windows-based VMs in Qubes.

Interested readers might want to check [​this article](http://theinvisiblethings.blogspot.com/2012/03/windows-support-coming-to-qubes.html) to learn why it took so long for Qubes OS to support HVM domains (Qubes 1 only supported Linuxed-based PV domains).

Creating an HVM domain
----------------------

First, lets create a new HVM domain (use the --hvm switch to qvm-create, or choose HVM type in the Qubes Manager VM creation dialog box):

``` {.wiki}
qvm-create win7 --hvm --label green
```

(Of course, the name of the domain ("win7"), as well as it's label ("green"), are just exemplary).

Now, we need to install an OS inside this VM, this can done by attacking an installation ISO upon starting the VM (this currently can be done only from command line, but in the future we surely will added an option to do this also from the manager):

``` {.wiki}
qvm-start win7 --cdrom=/usr/local/iso/win7_en.iso
```

Now, the VM will start booting from the attached CDROM device, which in the example above just happens to be the Windows 7 installation disk. Depending on the OS that is being installed in the VM, one might be required to start the VM several times (as is the case e.g. with Windows 7 installation), because whenever the installer wants to "reboot the system", it actually shutdowns the VM (and Qubes won't automatically start it), so several invocations of qvm-start command (as shown above) might be needed.

\<screenshot\>

Using Installation ISOs located in other VMs
--------------------------------------------

TODO

Setting up networking for HVM domains
-------------------------------------

TODO

Cloning HVM domains
-------------------

TODO

Installing Qubes support tools in Windows 7 VMs
-----------------------------------------------

TODO

Assigning PCI devices to HVM domains
------------------------------------

TODO

-   Manually disable/enable on resume from S3

