---
layout: doc
title: qvm-shutdown
permalink: /doc/tools/3.2/dom0/qvm-shutdown/
redirect_from:
- /doc/dom0-tools/qvm-shutdown/
- /en/doc/dom0-tools/qvm-shutdown/
- /doc/Dom0Tools/QvmShutdown/
- /wiki/Dom0Tools/QvmShutdown/
---

```
============
qvm-shutdown
============

NAME
====
qvm-shutdown

SYNOPSIS
========
| qvm-shutdown [options] <vm-name> [vm-name ...]

OPTIONS
=======
-h, --help
    Show this help message and exit
-q, --quiet
    Be quiet           
--force
    Force operation, even if may damage other VMs (eg. shutdown of NetVM)
--wait
    Wait for the VM(s) to shutdown
--wait-time
    Timeout after which VM will be killed when --wait is used
--all
    Shutdown all running VMs
--exclude=EXCLUDE_LIST
    When --all is used: exclude this VM name (might be repeated)

AUTHORS
=======
| Joanna Rutkowska <joanna at invisiblethingslab dot com>
| Rafal Wojtczuk <rafal at invisiblethingslab dot com>
| Marek Marczykowski <marmarek at invisiblethingslab dot com>
```
