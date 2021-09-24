---
lang: en
layout: doc
permalink: /doc/4.0/4.0/vm-troubleshooting/
redirect_from:
- /doc/remove-vm-manually/
ref: 223
title: Qube troubleshooting
---

## VM Kernel troubleshooting

This troubleshoot applies to the non-default kernel choice described in the [Managing VM docs](/doc/managing-vm-kernels/#using-kernel-installed-in-the-vm).

In case of problems, you can access the VM console using `qvm-console-dispvm VMNAME` in dom0, then access the GRUB menu.
You need to call it just after starting the VM (until `GRUB_TIMEOUT` expires); for example, in a separate dom0 terminal window.

In any case you can later access the VM's logs (especially the VM console log `/var/log/xen/console/guest-VMNAME.log`).

You can always set the kernel back to some dom0-provided value to fix a VM kernel installation.

## Qubes starts, but no VMs load

First, try to start a particular VM, check any failure message and direct further steps based on that.

This issue has been seen to occur if a dom0 update is interrupted halfway through and/or a hard power off is done without shutting down Qubes, which results in files getting corrupted.

## Can not uninstall a VM / “ERROR: VM installed by package manager: template-vm-name”

All of the following commands should be executed in a dom0 terminal.

When a template is marked as 'installed by package manager', but cannot be uninstalled there, trying to uninstall manually will result in the error "ERROR: VM installed by package manager: template-vm-name". Do as follows to be able to uninstall the template:

1. Check the state of `installed_by_rpm`

    ```
    $ qvm-prefs template-vm-name
    ```

2. If `installed_by_rpm - True]`, mark the template as not installed by package manager

    ```
    $ qvm-prefs template-vm-name installed_by_rpm false
    ```

3. Re-check the state of `installed_by_rpm`

- If `installed_by_rpm - False`, remove the template like you would a regular qube:

    ```
    $ qvm-remove template-vm-name
    ```

- If `installed_by_rpm` remains `True`, reboot your computer to bring qubes.xml in sync with qubesd, and try again to remove the template.

## Fixing package installation errors

By default, templates in 4.0 only have a loopback interface.

Some packages will throw an error on installation in this situation.
For example, Samba expects to be configured using a network interface post installation.

One solution is to add a dummy interface to allow the package to install correctly:

```
ip link add d0 type dummy
ip addr add 192.168.0.1/24 dev d0
ip link set d0 up
```

## "Cannot connect to qrexec agent" error

If you face this error when starting a VM, look into the VM logs at `/var/log/xen/console/guest-VMNAME.log`.
Common reasons that may be revealed are: too low memory, corrupted files or a VM crash on startup.

If the error occurs as a result of too little initial memory, increase the initial memory from 200MB to 400MB by navigating to VM settings » Advanced » Initial memory.

## "No match found" when trying to install a template

For example:

```
[user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-itl qubes-template-debian-10
Using sys-whonix as UpdateVM to download updates for Dom0; this may take some time...
No Match for argument qubes-template-debian-10
Nothing to download
```

This normally means you already have the template installed.
It may be that you have the matching package installed, but you removed or renamed the template.
Check `rpm -q qubes-template-<name>`.
If it lists the package, but you don't really have the template present (`qvm-ls` doesn't list it), you need to clean up leftovers of the package with `rpm -e --noscripts qubes-template-<name>`, then install it normally.
