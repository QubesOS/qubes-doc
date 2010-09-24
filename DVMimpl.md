---
layout: wiki
title: DVMimpl
permalink: /wiki/DVMimpl/
---

DisposableVM implementation in Qubes
====================================

DisposableVM image preparation
------------------------------

DisposableVM is not started like other VMs, by executing equivalent of *xm create* - it would be too slow. Instead, DisposableVM are started by restore from a savefile.

Preparing a savefile is done by */usr/lib/qubes/qubes\_prepare\_saved\_domain.sh* script. It takes two mandatory arguments, appvm name (APPVM) and the savefile name, and optional path to "prerun" script. The script executes the following steps:

1.  APPVM is started by *qvm-start*
2.  xenstore key `/local/domain/appvm_domain_id/qubes_save_request` is created
3.  if prerun script was specified, copy it to `qubes_save_script` xenstore key
4.  wait for the `qubes_used_mem` key to appear
5.  (in APPVM) APPVM boots normally, up to the point in */etc/init.d/qubes\_core* script when the presence of `qubes_save_request` key is tested. If it exists, then
    1.  (in APPVM) if exists, prerun script is retrieved from the respective xenstore key and executed. This preloads filesystem cache with useful applications, so that they will start faster.
    2.  (in APPVM) the amount of used memory is stored to `qubes_used_mem` xenstore key
    3.  (in APPVM) busy-waiting for `qubes_restore_complete` xenstore key to appear

6.  when `qubes_used_mem` key appears, the domain memory is reduced to this amount, to make the savefile smaller.
7.  APPVM private image is detached
8.  the domain is saved via *xm save*
9.  the COW files for root fs and swap are packed to `saved_cows.tar` archive

*qubes\_prepare\_saved\_domain.sh* script is somehow lowlevel. It is usually called by *qvm-create-default-dvm* script, that takes care of creating a special AppVM (named template\_name-dvm) to be passed to *qubes\_prepare\_saved\_domain.sh*, as well as copying the savefile to /dev/shm (the latter action is not done if the `/var/lib/qubes/dvmdata/dont_use_shm` file exists).

Restoring a DisposableVM from the savefile
------------------------------------------

When *qfilexchgd* daemon, described [here](/wiki/Qfileexchgd), sees a request to create a DVM, it executes */usr/lib/qubes/qubes\_restore* script. It is crucial that this script executes quickly, to make DisposableVM creation overhead bearable for the user. Its main steps are:

1.  modify the savefile so that the VM name, VM UUID, MAC address and IP address are unique
2.  restore the COW files from the `saved_cows.tar`
3.  create the `/var/run/qubes/fast_block_attach` file, whose presence tells the */etc/xen/scripts/block* script to bypass some redundant checks and execute as fast as possible.
4.  tell Xend to restore domain. In order to be as quick as possible, raw xmlrpc request is sent to the Xend socket, instead of calling *xm* program or using XendAPI
5.  create the same xenstore keys as normally created when AppVM boots (e.g. `qubes_ip`)
6.  create the `qubes_restore_complete` xenstore key. This allows the boot process in DisposableVM to continue.

The actual passing of files between AppVM and a DisposableVM is implemented in *qfilexchgd* daemon and accordingly described [here](/wiki/Qfileexchgd).

Validating the DisposableVM savefile
------------------------------------

DisposableVM savefile contains references to template rootfs and to COW files. The COW files are restored before each DisposableVM start, so they cannot change. On the other hand, if templateVM is started, the template rootfs will change, and it may not be coherent with the COW files.

Therefore, the check for template rootfs modification time being older than DisposableVM savefile modification time is required. It is done in two places:

-   in the */etc/init.d/qubes\_dvm* script
-   in *qfilexchgd* daemon, just before restoring DisposableVM

In both cases, an attempt is made to recreate the DisposableVM savefile, using the default template and the default prerun script, residing at */var/lib/qubes/vm-templates/templatename/dispvm\_prerun.sh*. Unfortunately, the prerun script takes a lot of time to execute - therefore, after template rootfs modification, the next DisposableVM creation or system boot can be longer by about 2.5 minutes. Also, if nondefault template or nondefault prerun script is intended to be used to create DisposableVM savefile, the *qvm-create-default-dvm* script must be run manually with respective arguments everytime the template rootfs changes.
