---
layout: doc
title: qvm-backup-restore
permalink: /doc/dom0-tools/qvm-backup-restore/
redirect_from:
- /en/doc/dom0-tools/qvm-backup-restore/
- /doc/Dom0Tools/QvmBackupRestore/
- /wiki/Dom0Tools/QvmBackupRestore/
---

qvm-backup-restore
==================

NAME
----

qvm-backup-restore - restores Qubes VMs from backup

SYNOPSIS
--------

qvm-backup-restore [options] \<backup-dir\>

OPTIONS
-------

-h, --help  
Show this help message and exit

--verify-only  
Do not restore the data, only verify backup integrity

--skip-broken  
Do not restore VMs that have missing templates or netvms

--ignore-missing  
Ignore missing templates and netvms, and restore the VMs anyway

--skip-conflicting  
Do not restore VMs that are already present on the host

--force-root  
Force to run with root privileges

--replace-template=REPLACE\_TEMPLATE  
Restore VMs using another template, syntax: old-template-name:new-template-name (can be repeated)

-x EXCLUDE, --exclude=EXCLUDE  
Skip restore of specified VM (can be repeated)

--skip-dom0-home  
Do not restore dom0's user home directory

--ignore-username-mismatch  
Ignore dom0 username mismatch when restoring dom0's user home directory

-d APPVM, --dest-vm=APPVM  
Restore from a backup located in a specific AppVM

-e, --encrypted  
The backup is encrypted

-z, --compressed  
The backup is compressed

--debug  
Enable (a lot of) debug output

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
