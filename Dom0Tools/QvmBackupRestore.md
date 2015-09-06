---
layout: doc
title: QvmBackupRestore
permalink: /doc/Dom0Tools/QvmBackupRestore/
redirect_from: /wiki/Dom0Tools/QvmBackupRestore/
---

qvm-backup-restore
==================

NAME
----

qvm-backup-restore - restores Qubes VMs from backup

Date  
2012-04-10

SYNOPSIS
--------

`qvm-backup-restore [options] <backup-dir>`

OPTIONS
-------

`-h`, `--help` 
Show this help message and exit

`--skip-broken`  
Do not restore VMs that have missing templates or netvms

`--ignore-missing`  
Ignore missing templates or netvms, restore VMs anyway

`--skip-conflicting`  
Do not restore VMs that are already present on the host

`--force-root`  
Force to run, even with root privileges

`--replace-template=REPLACE_TEMPLATE`  
Restore VMs using another template, syntax: old-template-name:new-template-name (may be repeated)

-x EXCLUDE, `--exclude=EXCLUDE`  
Skip restore of specified VM (may be repeated)

`--skip-dom0-home`  
Do not restore dom0 user home dir

`--ignore-username-mismatch`  
Ignore dom0 username mismatch while restoring homedir

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
