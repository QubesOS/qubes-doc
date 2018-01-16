---
layout: doc
title: qvm-copy-to-vm
permalink: /doc/vm-tools/qvm-copy-to-vm/
redirect_from:
- /en/doc/vm-tools/qvm-copy-to-vm/
- /doc/VmTools/QvmCopyToVm/
- /wiki/VmTools/QvmCopyToVm/
---

qvm-copy-to-vm
==============

NAME
----

qvm-copy - copy specified files to destination VM (chosen afterward in dom0 qubes.Filecopy popup dialog)

deprecated: qvm-copy-to-vm - copy specified files to specified destination VM
qvm-copy-to-vm/qvm-move-to-vm tools are deprecated 2017-01, use qvm-copy/qvm-move to avoid typing target qube name twice

Date  
2012-05-30

SYNOPSIS
--------

qvm-copy file [file]+

OPTIONS
-------

--without-progress  
Don't display progress info

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
