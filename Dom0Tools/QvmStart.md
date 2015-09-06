---
layout: doc
title: QvmStart
permalink: /doc/Dom0Tools/QvmStart/
redirect_from: /wiki/Dom0Tools/QvmStart/
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

`qvm-start [options] <vm-name>`

OPTIONS
-------

`-h, --help`   
Show this help message and exit

`-q, --quiet`   
Be quiet

`--no-guid`   
Do not start the GUId (ignored)

`--console`   
Attach debugging console to the newly started VM

`--dvm`   
Do actions necessary when preparing DVM image

`--custom-config=CUSTOM_CONFIG`    
Use custom Xen config instead of Qubes-generated one

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
