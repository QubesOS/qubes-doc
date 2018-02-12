---
layout: doc
title: qvm-add-appvm
permalink: /doc/tools/3.2/dom0/qvm-add-appvm/
redirect_from:
- /doc/dom0-tools/qvm-add-appvm/
- /en/doc/dom0-tools/qvm-add-appvm/
- /doc/Dom0Tools/QvmAddAppvm/
- /wiki/Dom0Tools/QvmAddAppvm/
---

```
=============
qvm-add-appvm
=============

NAME
====
qvm-add-appvm - add an already installed appvm to the Qubes DB

WARNING: Normally you should not need this command, and you should use qvm-create instead!

SYNOPSIS
========
| qvm-add-appvm [options] <appvm-name> <vm-template-name>

OPTIONS
=======
-h, --help
    Show this help message and exit
-p DIR_PATH, --path=DIR_PATH
    Specify path to the template directory
-c CONF_FILE, --conf=CONF_FILE
    Specify the Xen VM .conf file to use(relative to the template dir path)
--force-root
    Force to run, even with root privileges

AUTHORS
=======
| Joanna Rutkowska <joanna at invisiblethingslab dot com>
| Rafal Wojtczuk <rafal at invisiblethingslab dot com>
| Marek Marczykowski <marmarek at invisiblethingslab dot com>
```
