---
layout: wiki
title: TemplateImplementation
permalink: /wiki/TemplateImplementation/
---

Qubes TemplateVM implementation
===============================

TemplateVM has a shared root.img across all AppVMs that are based on it. This mechanism has some advantages over a simple common device connected to multiple VMs:

-   root.img can be modified while there are AppVMs running - without corrupting the filesystem
-   multiple AppVMs that are using different versions of root.img (from various points in time) can be running concurrently

There are two layers of the device-mapper snapshot device; the first one enables modifying root.img without stopping the AppVMs and the second one, which is contained in the AppVM, enables modifying its filesystem. These modifications will be discarded after a restart of the AppVM.

Snapshot device in Dom0
-----------------------

This device consists of:

-   root.img - real template filesystem
-   root-cow.img - differences between the device as seen by AppVM and the current root.img

The above is achieved through creating device-mapper snapshots for each version of root.img. When an AppVM is started, a xen hotplug script (/etc/xen/scripts/block-snapshot) reads the inode numbers of root.img and root-cow.img; these numbers are used as the snapshot device's name. When a device with the same name exists the new AppVM will use it - therefore, AppVMs based on the same version of root.img will use the same device. Of course, the device-mapper cannot use the files directly - it must be connected through /dev/loop\*. The same mechanism detects if there is a loop device associated with a file determined by the device and inode numbers - or if creating a new loop device is necessary.

When an AppVM is stopped the xen hotplug script checks whether the device is still in use - if it is not, the script removes the snapshot and frees the loop device.

### Changes to template filesystem

In order for the full potential of the snapshot device to be realized, every change in root.img must save the original version of the modified block in root-cow.img. This is achieved by a snapshot-origin device.

When TemplateVM is started, it receives the snapshot-origin device connected as a root device (in read-write mode). Therefore, every change to this device is immediately saved in root.img - but remains invisible to the AppVM, which uses the snapshot.

When TemplateVM is stopped, the xen script removes root-cow.img and creates a new one (using the qvm-template-commit tool). The snapshot device will remain untouched due to the loop device, which uses an actual file on the disk (by inode, not by name). Linux kernel frees the old root-cow.img files as soon as they are unused by all snapshot devices (to be exact, loop devices). The new root-cow.img file will get a new inode number, and so new AppVMs will get new snapshot devices (with different names).

Snapshot device in AppVM
------------------------

Root device is exposed to AppVM in read-only mode. AppVM can write only in:

-   private.img - persistent storage (mounted in /rw) used for /home, /usr/local - in future versions, its use may be extended
-   volatile.img - temporary storage, which is discarded after an AppVM restart

volatile.img is divided into two partitions:

1.  changes to root device
2.  swap partition

Inside of an AppVM, the root device is wrapped by the snapshot in the first partition of volatile.img. Therefore, the AppVM can write anything to its filesystem - however, such changes will be discarded after a restart.
