---
layout: doc
title: qvm-block
permalink: /doc/tools/3.2/dom0/qvm-block/
redirect_from:
- /doc/dom0-tools/qvm-block/
- /doc/dom0-tools/qvm-block/
- /en/doc/dom0-tools/qvm-block/
- /doc/Dom0Tools/QvmBlock/
- /wiki/Dom0Tools/QvmBlock/
---

```
=========
qvm-block
=========

NAME
====
qvm-block - list/set VM PCI devices.

SYNOPSIS
========
| qvm-block -l [options]
| qvm-block -a [options] <vm-name> <device-vm-name>:<device>
| qvm-block -A [options] <vm-name> <file-vm-name>:<file>
| qvm-block -d [options] <device-vm-name>:<device>
| qvm-block -d [options] <vm-name>

OPTIONS
=======
-h, --help
    Show this help message and exit
-l, --list
    List block devices            
-A, --attach-file
    Attach specified file instead of physical device
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
--show-system-disks
    List also system disks
--force-root
    Force to run, even with root privileges

AUTHORS
=======
| Joanna Rutkowska <joanna at invisiblethingslab dot com>
| Rafal Wojtczuk <rafal at invisiblethingslab dot com>
| Marek Marczykowski <marmarek at invisiblethingslab dot com>
```
