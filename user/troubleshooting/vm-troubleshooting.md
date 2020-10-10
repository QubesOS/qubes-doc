---
layout: doc
title: Suspend/Resume Troubleshooting
permalink: /doc/vm-troubleshooting/
redirect_from:
- /doc/remove-vm-manually/
---

# VM troubleshooting #

## VM Kernel troubleshooting ##

In case of problems, you can access the VM console using `qvm-console-dispvm VMNAME` in dom0, then access the GRUB menu.
You need to call it just after starting the VM (until `GRUB_TIMEOUT` expires); for example, in a separate dom0 terminal window.

In any case you can later access the VM's logs (especially the VM console log `/var/log/xen/console/guest-VMNAME.log`).

You can always set the kernel back to some dom0-provided value to fix a VM kernel installation.

## Qubes starts, but no VMs load ##

This issue may occur if a dom0 update is interrupted halfway through and/or a hard power off is done without shutting down Qubes, which results in files getting corrupted. 
In this case, the best fix is to reinstall Qubes and restore your files from a backup. 
Even if you have not backed up data in a while, you should be able to mount the volumes to pull data from them. 

## Can not uninstall a VM / “ERROR: VM installed by package manager: template-vm-name”

Try the [normal method] before resorting to this method to remove a VM manually.
All of the following commands should be executed in a dom0 terminal.

When a template is marked as 'installed by package manager', but cannot be uninstalled there, trying to uninstall manually will result in the error "ERROR: VM installed by package manager: template-vm-name". Do as follows to be able to uninstall the template:

1. Check the state of `installed_by_rpm`

       $ qvm-prefs template-vm-name

2. If `installed_by_rpm - True]`, mark the template as not installed by package manager

       $ qvm-prefs template-vm-name installed_by_rpm false

3. Re-check the state of `installed_by_rpm`

- If `installed_by_rpm - False`, remove the template like you would a regular qube:

       $ qvm-remove template-vm-name

- If `installed_by_rpm` remains `True`, reboot your computer to bring qubes.xml in sync with qubesd, and try again to remove the template.


[normal method]: /doc/templates/#uninstalling


## Fixing package installation errors ##

By default, templates in 4.0 only have a loopback interface.

Some packages will throw an error on installation in this situation.
For example, Samba expects to be configured using a network interface post installation.

One solution is to add a dummy interface to allow the package to install correctly:

    ip link add d0 type dummy
    ip addr add 192.168.0.1/24 dev d0
    ip link set d0 up

## "Cannot connect to qrexec agent" error ##

If you face this error when starting a VM, it may be due to too little initial memory. 
A solution is to increase the initial memory from 200MB to 400MB by navigating to VM settings » Advanced » Initial memory. 

