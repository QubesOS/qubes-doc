---
layout: wiki
title: TemplateImplementation
permalink: /wiki/TemplateImplementation/
---

Qubes TemplateVM implementation
===============================

TemplateVM has shared root.img across all AppVMs based on it. This mechanism has some advantages over simple common device connected to multiple VMs:

-   root.img can be modified while there are running AppVMs, without corrupting filesystem
-   multiple AppVMs can be running, using different versions of root.img (from different point in time)

There is two layer of device-mapper snapshot device. The first one in dom0 to enable modify of root.img without stopping AppVMs. The second one in AppVM to enable modifications of its filesystem, which will be discarded after AppVM restart.

Snapshot device in Dom0
-----------------------

This device consists of:

-   root.img - real template filesystem
-   root-cow.img - differences between device seen by AppVM and current root.img

This is achieved by creating device-mapper snapshots for each version of root.img. When AppVM is started, xen hotplug scripts (/etc/xen/scripts/block-snapshot) reads inode number of root.img and root-cow.img and uses this numbers for snapshot device name. When device with same name exists - new AppVM will use it, so AppVMs based on the same version of root.img will use common device. Of course device-mapper cannot use files directly - it must be connected through /dev/loop\*. The same mechanism detects if there is loop device connected with some file (by device+inode number) already, or creating new loop device is needed.

When AppVM is stopped, xen hotplug script checks if this device is still used, and if not - removes snapshot and frees loop devices.

### Changes to template filesystem

To take advantages of snapshot device, every change in root.img must save original version of modified block in root-cow.img. This is achieved by snapshot-origin device.

When TemplateVM is started - it got snapshot-origin device connected as root device (in read-write mode). So every change to this device is immediately saved in root.img, but is not visible to AppVM, which uses snapshot.

When TemplateVM is stopped, xen scripts removes root-cow.img and creates new one (by qvm-template-commit tool). Because of loop devices which uses concrete file on disk (by inode, not name), snapshot device will not be touched. And Linux kernel frees old root-cow.img files as soon as it will not be used by any snapshot device (precisely loop devices). The new root-cow.img file will got new inode number, so new AppVMs will got new snapshot device (with different name).

Snapshot device in AppVM
------------------------

Root device is exposed to AppVM in read-only mode. The only place where AppVM can write something is:

-   private.img - persistent storage (mounted in /rw) used for /home, /usr/local and maybe more in future versions
-   volatile.img - temporary storage, which is discarded after AppVM restart

The volatile.img is divided into two partitions:

1.  changes to root device
2.  swap partition

Inside of AppVM, root device is wrapped by snapshot with first partition of volatile.img. Thanks to this AppVM can write anything to its filesystem (but this changes will be discarded after restart).
