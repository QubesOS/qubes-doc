---
layout: doc
title: QvmBlock
permalink: /doc/Dom0Tools/QvmBlock/
redirect_from: /wiki/Dom0Tools/QvmBlock/
---

qvm-block
=========

NAME
----

qvm-block - list/set VM PCI devices.

Date  
2012-04-10

SYNOPSIS
--------

qvm-block -l [options]
qvm-block -a [options] \<device\> \<vm-name\>
qvm-block -d [options] \<device\>
qvm-block -d [options] \<vm-name\>

OPTIONS
-------

-h, --help  
Show this help message and exit

-l, --list  
List block devices

-a, --attach  
Attach block device to specified VM

-d, --detach  
Detach block device

-f FRONTEND, --frontend=FRONTEND  
Specify device name at destination VM [default: xvdi]

--ro  
Force read-only mode

--no-auto-detach  
Fail when device already connected to other VM

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
