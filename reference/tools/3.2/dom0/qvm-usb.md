---
layout: doc
title: qvm-usb
permalink: /doc/tools/3.2/dom0/qvm-usb/
redirect_from:
- /doc/dom0-tools/qvm-usb/
- /en/doc/dom0-tools/qvm-usb/
---

```
=======
qvm-usb
=======

NAME
====
qvm-usb - List/set VM USB devices

SYNOPSIS
========
| qvm-usb -l [options]
| qvm-usb -a [options] <vm-name> <device-vm-name>:<device>
| qvm-usb -d [options] <device-vm-name>:<device>

OPTIONS
=======
-h, --help
    Show this help message and exit
-l, -list
    List devices
-a, --attach
    Attach specified device to specified VM
-d, --detach
    Detach specified device
--no-auto-detach
    Fail when device already connected to other VM
--force-root
    Force to run, even with root privileges

AUTHORS
=======
| Joanna Rutkowska <joanna at invisiblethingslab dot com>
| Rafal Wojtczuk <rafal at invisiblethingslab dot com>
| Marek Marczykowski <marmarek at invisiblethingslab dot com>
```
