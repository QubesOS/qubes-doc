---
layout: doc
title: qvm-pci
permalink: /doc/tools/3.2/dom0/qvm-pci/
redirect_from:
- /doc/dom0-tools/qvm-pci/
- /en/doc/dom0-tools/qvm-pci/
- /doc/Dom0Tools/QvmPci/
- /wiki/Dom0Tools/QvmPci/
---

qvm-pci
=======

NAME
----

qvm-pci - list/set VM PCI devices

Date  
2012-04-11

SYNOPSIS
--------

qvm-pci -l [options] \<vm-name\>
qvm-pci -a [options] \<vm-name\> \<device\>
qvm-pci -d [options] \<vm-name\> \<device\>

OPTIONS
-------

-h, --help  
Show this help message and exit

-l, --list  
List VM PCI devices

-a, --add  
Add a PCI device to specified VM

-C, --add-class  
Add all devices of given class:  
net - network interfaces, usb - USB controllers

-d, --delete  
Remove a PCI device from specified VM

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
