---
layout: doc
title: qvm-start
permalink: /doc/tools/3.2/dom0/qvm-start/
redirect_from:
- /doc/dom0-tools/qvm-start/
- /en/doc/dom0-tools/qvm-start/
- /doc/Dom0Tools/QvmStart/
- /wiki/Dom0Tools/QvmStart/
---

```
=========
qvm-start
=========

NAME
====
qvm-start - start a specified VM

SYNOPSIS
========
| qvm-start [options] <vm-name>

OPTIONS
=======
-h, --help
    Show this help message and exit
-q, --quiet
    Be quiet           
--tray
    Use tray notifications instead of stdout
--no-guid
    Do not start the GUId (ignored)
--drive
    Temporarily attach specified drive as CD/DVD or hard disk (can be specified with prefix 'hd' or 'cdrom:', default is cdrom)
--hddisk
    Temporarily attach specified drive as hard disk
--cdrom
    Temporarily attach specified drive as CD/DVD
--install-windows-tools
    Attach Windows tools CDROM to the VM
--dvm
    Do actions necessary when preparing DVM image
--custom-config=CUSTOM_CONFIG
    Use custom Xen config instead of Qubes-generated one
--skip-if-running
    Do no fail if the VM is already running
--debug
    Enable debug mode for this VM (until its shutdown)

AUTHORS
=======
| Joanna Rutkowska <joanna at invisiblethingslab dot com>
| Rafal Wojtczuk <rafal at invisiblethingslab dot com>
| Marek Marczykowski <marmarek at invisiblethingslab dot com>
```
