---
lang: en
layout: doc
permalink: /doc/salt-troubleshooting/
redirect_from:
- /doc/salt/
- /en/doc/salt/
ref: 1000000000000
title: Salt troubleshooting
---

For ease of Qubes Os managament and reproductible deployment, [Salt](/doc/salt/) allows to control states on `dom0` and other vms from the `dom0`.

Behind the scenes
-----------------

Except for `dom0` where the host is controlled locally.
Each vm (named `minion-vm` for instance) is controlled by a disposable master vm based on `disposable-mgmt-vm`, named `disp-mgmt-minion-vm` and created only for the duration of `qubesctl` execution.

The required files are copied from `dom0` to `disp-mgmt-minion-vm` via `qubes.Filecopy`, then `qubes.SaltLinuxVM` and expect two lines on stdin :
```
minion-vm
salt-command
```

Usually `salt-command` is `state.apply` with the provided arguments like `test=True`.

Then, a fake `ssh` command wrapper included in `qubes-mgmt-salt-vm-connector` allow to run the command on the target (`minion-vm`) via `qubes.VMShell` or `qubes.VMRootShell`.
On the management vm `disp-mgmt-minion-vm`, salt firstly creates `/var/cache/salt/master/thin/thin.tgz` and transfers it to the `minion-vm` to ensure destination host has the required python files.

How to debug the ephemeral disposable management vm
---------------------------------------------------

First, the transfered content from `dom0` to the disposable management vm needs to be retrieved. To do so, it is suggested to:
1. Call from `dom0`, `qubesctl` with requested command like `qubesctl --show-output --targets minion-vm --skip-dom0 state.apply`,
2. Freeze the previous command with `Ctrl+Z` as soon as you see `minion-vm is starting`.
3. Get the console on the disposable management vm with `qvm-console-dispvm disp-mgmt-minion-vm` on the dom0
4. Type `root` to log as root on the console
5. Edit in `disp-mgmt-minion-vm`, `/etc/qubes-rpc/qubes.SaltLinuxVM` and add after the line `eval "dir=~$user/QubesIncoming/dom0/srv"`, the line `qvm-copy $dir`.
6. On the `dom0` resume the freezed process with `fg`
7. Copy the content to another qubes vm (`side-vm` for instance)

Second, a debugable disposable management vm is setup. To do so, it is suggested to:
1. Call from `dom0`, `qubesctl` with requested command like `qubesctl --show-output --targets minion-vm --skip-dom0 state.apply`,
2. Freeze the previous command with `Ctrl+Z` as soon as you see `minion-vm is starting`.
3. Copy the retrieved content from `side-vm` to the disposable management vm `disp-mgmt-minion-vm` (with `qvm-copy`)
4. Get the console on the disposable management vm with `qvm-console-dispvm disp-mgmt-minion-vm` on the dom0
5. Type `root` to log as root on the console. All following commands are done inside the console.
6. Move the copied content to emulate a content coming from `dom0`: `cd /home/user/QubesIncoming; mv * dom0`. `dom0` directory should contain a directory `srv`.
7. Emulate a call to `qubes.SaltLinuxVM` with `bash /etc/qubes-rpc/qubes.SaltLinuxVM`
8. Emulate stdin. Type the destination vm on the first line (`minion-vm`), the salt command on the second line (`state.apply` for instance) then `Ctrl+D`.
9. A first execution is launched
10. Get wrappers in the `PATH` with `export PATH="/usr/lib/qubes-vm/connector/ssh-wrapper:$PATH" (the line is available in `/etc/qubes-rpc/qubes.SaltLinuxVM`

Third, launch as many times as needed the following command to emulate a new call of master to the minion `rm -r /var/cache/salt /var/tmp/.root*; salt-ssh -w minion-vm salt-command` in the console.
