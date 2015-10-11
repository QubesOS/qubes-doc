---
layout: doc
title: QvmStart
permalink: /en/doc/dom0-tools/qvm-start/
redirect_from:
- /doc/Dom0Tools/QvmStart/
- /wiki/Dom0Tools/QvmStart/
---

qvm-start
=========

NAME
----

qvm-start - start a specified VM

Date  
2012-04-11

SYNOPSIS
--------

qvm-start [options] \<vm-name\>

OPTIONS
-------

-h, --help  
Show this help message and exit

-q, --quiet  
Be quiet

--no-guid  
Do not start the GUId (ignored)

--console  
Attach debugging console to the newly started VM

--dvm  
Do actions necessary when preparing DVM image

--custom-config=CUSTOM\_CONFIG  
Use custom Xen config instead of Qubes-generated one

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
