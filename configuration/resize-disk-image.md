---
layout: doc
title: Resize Private Disk Image
permalink: /doc/resize-disk-image/
redirect_from:
- /en/doc/resize-disk-image/
- /doc/ResizeDiskImage/
- /wiki/ResizeDiskImage/
---

Resize Private Disk Image
-----------------

There are several disk images which can be easily extended, but pay attention to the overall consumed space of your sparse disk images. See also additional information and caveats about [resizing the root disk image](/doc/resize-root-disk-image/).


### Private disk image (R4.0)

1048576 MiB is the maximum size which can be assigned to a private storage through Qube Manager.

To grow the private disk image of an AppVM beyond this limit, [qvm-volume](/doc/dom0-tools/qvm-volume/) can be used:

~~~
qvm-volume extend <vm_name>:private <size>
~~~

Note: Size is the target size (i.e. 4096MB or 16GB, ...), not the size to add to the existing disk.

### Private disk image (R3.2)

1048576 MB is the maximum size which can be assigned to a private storage through Qubes Manager.

To grow the private disk image of an AppVM beyond this limit, [qvm-grow-private](/doc/dom0-tools/qvm-grow-private/) can be used:

~~~
qvm-grow-private <vm-name> <size>
~~~

Note: Size is the target size (i.e. 4096MB or 16GB, ...), not the size to add to the existing disk. 

### Shrinking private disk image (Linux VM, R4.0)

1.  Create a new qube with smaller disk using Qube Manager or qvm-create
2.  Move data using OS tools
3.  Delete old qube using Qube Manager or qvm-remove

### Shrinking private disk image (Linux VM, R3.2)

**This operation is dangerous and this is why it isn't available in standard Qubes tools. If you have enough disk space, it is safer to create a new VM with a smaller disk and move the data.**

The basic idea is to:

1.  Shrink filesystem on the private disk image.
2.  Then shrink the image.

Ext4 does not support online shrinking, so it can't be done as conveniently as growing the image.
Note that we don't want to touch the VM filesystem directly in dom0 for security reasons. 
First you need to start VM without `/rw` mounted. One possibility is to interrupt its normal startup
by adding the `rd.break` kernel option:

~~~
qvm-prefs -s <vm-name> kernelopts rd.break
qvm-start --no-guid <vm-name>
~~~

And wait for qrexec connect timeout (or simply press Ctrl-C). Then you can connect to VM console and shrink the filesystem:

~~~
sudo xl console <vm-name>
# you should get dracut emergency shell here
mount --bind /dev /sysroot/dev
chroot /sysroot
mount /proc
e2fsck -f /dev/xvdb
resize2fs /dev/xvdb <new-desired-size>
umount /proc
exit
umount /sysroot/dev
poweroff
~~~

Now you can resize the image:

~~~
truncate -s <new-desired-size> /var/lib/qubes/appvms/<vm-name>/private.img
~~~

**It is critical to use the same (or bigger for some safety margin) size in truncate call compared to resize2fs call. Otherwise you will loose your data!** Then reset kernel options back to default:

~~~
qvm-prefs -s <vm-name> kernelopts default
~~~

Done.

>In order to avoid error, you might want to first reduce the filesystem to a smaller size than desired (say 3G), then truncate the image to the target size (for example 4G), and lastly grow the filesystem to the target size. In order to do this, after the `truncate` step, start the vm again in maintenance mode and use the following command to extend the filesystem to the correct size : `resize2fs /dev/xvdb`.
>
>With no argument, resize2fs grows the filesystem to match the underlying block device (the .img file you just shrunk)


OS Specific Follow-up Instructions
-----------------

After resizing volumes, the partition table and file-system may need to be adjusted.
Use tools appropriate to the OS in your qube. Brief instructions for Windows 7,
FreeBSD, and Linux are provided below.

#### Windows 7

1.  Click Start
2.  type "diskmgmt.msc" - this takes you to Disk Management
3.  Right-click on your existing volume, select "Extend Volume..."
4.  Click through the wizard.

No reboot required.

#### FreeBSD

~~~
gpart recover ada0
sysctl kern.geom.debugflags=0x10
gpart resize -i index ada0
zpool online -e poolname ada0
~~~

#### Linux

Qubes will automatically grow the filesystem for you on AppVMs but not HVMs.
You will see that there is unallocated free space at the end of your primary disk.
You can use standard linux tools like fdisk and mkfs to make this space available.
