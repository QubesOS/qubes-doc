---
layout: doc
title: QvmShutdown
permalink: /en/doc/dom0-tools/qvm-shutdown/
redirect_from:
- /doc/Dom0Tools/QvmShutdown/
- /wiki/Dom0Tools/QvmShutdown/
---

qvm-shutdown
============

NAME
----

qvm-shutdown

Date  
2012-04-11

SYNOPSIS
--------

qvm-shutdown [options] \<vm-name\>

OPTIONS
-------

-h, --help  
Show this help message and exit

-q, --quiet  
Be quiet

--force  
Force operation, even if may damage other VMs (eg. shutdown of NetVM)

--wait  
Wait for the VM(s) to shutdown

--all  
Shutdown all running VMs

--exclude=EXCLUDE\_LIST  
When --all is used: exclude this VM name (might be repeated)

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
