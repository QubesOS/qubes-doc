---
layout: doc
title: QvmAddAppvm
permalink: /doc/Dom0Tools/QvmAddAppvm/
redirect_from: /wiki/Dom0Tools/QvmAddAppvm/
---

qvm-add-appvm
=============

NAME
----

qvm-add-appvm - add an already installed appvm to the Qubes DB

WARNING: Noramlly you would not need this command, and you would use qvm-create instead!

Date  
2012-04-10

SYNOPSIS
--------

qvm-add-appvm [options] \<appvm-name\> \<vm-template-name\>

OPTIONS
-------

-h, --help  
Show this help message and exit

-p DIR\_PATH, --path=DIR\_PATH  
Specify path to the template directory

-c CONF\_FILE, --conf=CONF\_FILE  
Specify the Xen VM .conf file to use(relative to the template dir path)

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
