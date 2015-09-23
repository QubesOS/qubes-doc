---
layout: doc
title: QubesDom0Update
permalink: /doc/Dom0Tools/QubesDom0Update/
redirect_from: /wiki/Dom0Tools/QubesDom0Update/
---

qubes-dom0-update
=================

NAME
----

qubes-dom0-update - update software in dom0

Date  
2012-04-13

SYNOPSIS
--------

qubes-dom0-update [--clean] [--check-only] [--gui] [\<yum opts\>] [\<pkg list\>]

OPTIONS
-------

--clean  
Clean yum cache before doing anything

--check-only  
Only check for updates (no install)

--gui  
Use gpk-update-viewer for update selection

\<pkg list\>  
Download (and install if run by root) new packages in dom0 instead of updating

Besides above options, when no --gui or --check-only given, all other options are passed to yum call. So for example --enablerepo/--disablerepo options works as well.

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
