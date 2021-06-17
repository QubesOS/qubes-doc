---
lang: en
layout: doc
permalink: /doc/disposablevm-implementation/
redirect_from:
- /doc/dvm-impl/
- /en/doc/dvm-impl/
- /doc/DVMimpl/
- /wiki/DVMimpl/
ref: 34
title: DisposableVM Implementation
---

**Note: The content below applies to Qubes R3.2.**

DisposableVM image preparation
------------------------------

DisposableVM is not started like other VMs, by executing equivalent of `xl create` - it would be too slow. Instead, DisposableVM are started by restore from a savefile.

Preparing a savefile is done by `/usr/lib/qubes/qubes_prepare_saved_domain.sh` script. It takes two mandatory arguments, appvm name (APPVM) and the savefile name, and optional path to "prerun" script. The script executes the following steps:

1. APPVM is started by `qvm-start`
2. xenstore key `/local/domain/appvm_domain_id/qubes_save_request` is created
3. if prerun script was specified, copy it to `qubes_save_script` xenstore key
4. wait for the `qubes_used_mem` key to appear
5. (in APPVM) APPVM boots normally, up to the point in `/etc/init.d/qubes_core` script when the presence of `qubes_save_request` key is tested. If it exists, then
    1. (in APPVM) if exists, prerun script is retrieved from the respective xenstore key and executed. This preloads filesystem cache with useful applications, so that they will start faster.
    2. (in APPVM) the amount of used memory is stored to `qubes_used_mem` xenstore key
    3. (in APPVM) busy-waiting for `qubes_restore_complete` xenstore key to appear

6. when `qubes_used_mem` key appears, the domain memory is reduced to this amount, to make the savefile smaller.
7. APPVM private image is detached
8. the domain is saved via `xl save`
9. the COW file volatile.img (cow for root fs and swap) is packed to `saved_cows.tar` archive

The `qubes_prepare_saved_domain.sh` script is lowlevel. It is usually called by `qvm-create-default-dvm` script, that takes care of creating a special AppVM (named template\_name-dvm) to be passed to `qubes_prepare_saved_domain.sh`, as well as copying the savefile to /dev/shm (the latter action is not done if the `/var/lib/qubes/dvmdata/dont_use_shm` file exists).

Restoring a DisposableVM from the savefile
------------------------------------------

Normally, disposable VM is created when qubes rpc request with target *\$dispvm* is received. Then, as a part of rpc connection setup, the `qfile-daemon-dvm` program is executed; it executes `/usr/lib/qubes/qubes_restore` program. It is crucial that this program executes quickly, to make DisposableVM creation overhead bearable for the user. Its main steps are:

1. modify the savefile so that the VM name, VM UUID, MAC address and IP address are unique
2. restore the COW files from the `saved_cows.tar`
3. create the `/var/run/qubes/fast_block_attach` file, whose presence tells the `/etc/xen/scripts/block` script to bypass some redundant checks and execute as fast as possible.
4. execute `xl restore` in order to restore a domain.
5. create the same xenstore keys as normally created when AppVM boots (e.g. `qubes_ip`)
6. create the `qubes_restore_complete` xenstore key. This allows the boot process in DisposableVM to continue.

The actual passing of files between AppVM and a DisposableVM is implemented via qubes rpc.

Validating the DisposableVM savefile
------------------------------------

DisposableVM savefile contains references to template rootfs and to COW files. The COW files are restored before each DisposableVM start, so they cannot change. On the other hand, if templateVM is started, the template rootfs will change, and it may not be coherent with the COW files.

Therefore, the check for template rootfs modification time being older than DisposableVM savefile modification time is required. It is done in `qfilexchgd` daemon, just before restoring DisposableVM. If necessary, an attempt is made to recreate the DisposableVM savefile, using the last template used (or default template, if run for the first time) and the default prerun script, residing at `/var/lib/qubes/vm-templates/templatename/dispvm_prerun.sh`. Unfortunately, the prerun script takes a lot of time to execute - therefore, after template rootfs modification, the next DisposableVM creation can be longer by about 2.5 minutes.
