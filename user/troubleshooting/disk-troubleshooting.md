---
layout: doc
title: Disk Troubleshooting
permalink: /doc/disk-troubleshooting/
redirect_from:
- /en/doc/out-of-memory/
- /doc/OutOfmemory/
- /wiki/OutOfmemory/
- /doc/out-of-memory/
---

# Disk Troubleshooting Guide #

## "Out of disk space" error ##

VMs (especially templates) use pre-allocated space. 
The default private storage max size is 2 GB, but it's very easy to increase as needed. 
If the disk is completely full, you will get an `Out of disk space` error that may crash your system because Dom0 does not have enough disk space to work. 
So it's good practice to regularly check disk space usage with the command `df -h` in dom0 terminal.

A system that's out of space should be able to boot, but may be unable to load a desktop manager. 
In this case it is possible to login to dom0 terminal with Alt + Ctrl + F2. 
To recover disk space it may be possible to delete files in a userVM by connecting to the userVM terminal:

~~~
qvm-start <VMname>
qvm-console-dispvm <VMname>
~~~

If this does not work, check the size of /var/lib/qubes/qubes.xml. 
If it is zero, you'll need to use one of the file backup (stored in /var/lib/qubes/backup), hopefully you have the current data there. 
Find the most recent one and place in /var/lib/qubes/qubes.xml instead of the empty file.

In any case you'll need some disk space to start the VM. Check `df -h` output if you have some. 
If not, here are some hints how to free some disk space:

1.  Clean yum cache.

    ~~~
    sudo yum clean all
    ~~~

2.  Delete `.img` files of a less important VM, which can be found in `/var/lib/qubes/appvms/`.
    Then, when the system is working again, clean up the rest.

    ~~~
    qvm-remove <VMname>
    ~~~

    With this method, you lose the data of one VM, but it'll work more reliably.

3.  Decrease the filesystem safety margin (5% by default).

    ~~~
    sudo tune2fs -m 4 /dev/mapper/vg_dom0-lv_root
    ~~~

4.  Remove some unneeded files in dom0 home (if you have any, most likely not).

## Can't resize VM storage / "resize2fs: Permission denied" error ##

[Resizing a volume](/doc/resize-disk-image/) in the Qubes interface should be a straightforward process.
But sometimes, an attempt to resize will look like it worked, when it in fact fails silently.
If you then try the same operation in the dom0 console using the `qvm-volume extend` command, it fails with the error message: `resize2fs: Permission denied to resize filesystem`.
This error indicates that a `resize2fs` will not work, unless `fsck` is run first.
Qubes OS utilities cannot yet handle this case.

To fix this issue:

1. In the dom0 terminal get a root console on the vm (eg. sys-usb) with:

    ~~~
    sudo xl console -t pv sys-usb
    ~~~

2. Unmount everything mounted on the private volume `/dev/xvdb partition`. 
There are typically several mounts listed in `/etc/mtab`. 

3. When you attempt to unmount the `/home` directory using the `umount /home` command, you will encounter an error because there are processes using the `/home` directory. You can view a list of these processes with the `fuser` command:

    ~~~
    fuser -m /home
    ~~~

Kill these process until they are all gone using `kill <process ID>`.

4. Finally, run:

    ~~~
    umount /home
    fsck /dev/xvdb
    resize2fs /dev/xvdb
    ~~~

After restarting your VM, everything should now work as expected. 
The private volume size shown externally in the VM's settings interface is the same as that seen within the VM.
