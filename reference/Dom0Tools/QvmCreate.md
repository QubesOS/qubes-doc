---
layout: doc
title: QvmCreate
permalink: /en/doc/dom0-tools/qvm-create/
redirect_from:
- /doc/Dom0Tools/QvmCreate/
- /wiki/Dom0Tools/QvmCreate/
---

qvm-create
==========

NAME
----

qvm-create - creates a new VM

Date  
2012-04-10

SYNOPSIS
--------

qvm-create [options] \<vm-name\>

OPTIONS
-------

-h, --help  
Show this help message and exit

-t TEMPLATE, --template=TEMPLATE  
Specify the TemplateVM to use

-l LABEL, --label=LABEL  
Specify the label to use for the new VM (e.g. red, yellow, green, ...)

-p, --proxy  
Create ProxyVM

-n, --net  
Create NetVM

-H, --hvm  
Create HVM (standalone, unless --template option used)

--hvm-template  
Create HVM template

-R ROOT\_MOVE, --root-move-from=ROOT\_MOVE  
Use provided root.img instead of default/empty one (file will be MOVED)

-r ROOT\_COPY, --root-copy-from=ROOT\_COPY  
Use provided root.img instead of default/empty one (file will be COPIED)

-s, --standalone  
Create standalone VM - independent of template

-m MEM, --mem=MEM  
Initial memory size (in MB)

-c VCPUS, --vcpus=VCPUS  
VCPUs count

-i, --internal  
Create VM for internal use only (hidden in qubes-manager, no appmenus)

--force-root  
Force to run, even with root privileges

-q, --quiet  
Be quiet

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
