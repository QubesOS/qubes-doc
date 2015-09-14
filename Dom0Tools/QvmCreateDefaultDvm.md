---
layout: doc
title: QvmCreateDefaultDvm
permalink: /doc/Dom0Tools/QvmCreateDefaultDvm/
redirect_from: /wiki/Dom0Tools/QvmCreateDefaultDvm/
---

qvm-create-default-dvm
======================

NAME
----

qvm-create-default-dvm - creates a default disposable VM

Date  
2012-04-10

SYNOPSIS
--------

`qvm-create-default-dvm templatename|--default-template|--used-template [script-name|--default-script]`

OPTIONS
-------

`templatename`  
Base DispVM on given template. The command will create AppVM named after template with "-dvm" suffix. This VM will be used to create DispVM savefile. If you want to customize DispVM, use this VM - take a look at <https://wiki.qubes-os.org/wiki/UserDoc/DispVMCustomization>

`--default-template`  
Use default template for the DispVM

`--used-template`  
Use the same template as earlier

`--default-script`  
Use default script for seeding DispVM home.

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>  
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>  
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
