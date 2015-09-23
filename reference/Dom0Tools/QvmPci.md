---
layout: doc
title: QvmPci
permalink: /doc/Dom0Tools/QvmPci/
redirect_from: /wiki/Dom0Tools/QvmPci/
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

-d, --delete  
Remove a PCI device from specified VM

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
