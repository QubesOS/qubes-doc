---
layout: doc
title: qvm-remove
permalink: /doc/dom0-tools/qvm-remove/
redirect_from:
- /en/doc/dom0-tools/qvm-remove/
- /doc/Dom0Tools/QvmRemove/
- /wiki/Dom0Tools/QvmRemove/
---

qvm-remove
==========

NAME
----

qvm-remove - remove a VM

SYNOPSIS
--------

qvm-remove [options] \<vm-name\>

OPTIONS
-------

-h, --help  
Show this help message and exit

-q, --quiet  
Be quiet

--just-db  
Remove only from the Qubes Xen DB, do not remove any files

--force-root  
Force to run, even with root privileges

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
