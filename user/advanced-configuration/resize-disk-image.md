---
layout: doc
title: Resize Disk Image
permalink: /doc/resize-disk-image/
redirect_from:
- /en/doc/resize-disk-image/
- /en/doc/resize-root-disk-image/
- /doc/ResizeDiskImage/
- /doc/ResizeRootDiskImage/
- /wiki/ResizeDiskImage/
- /wiki/ResizeRootDiskImage/
---

Resizing Disk Images
-----------------

By default Qubes uses thin volumes for the disk images.
This means that space is not actually allocated for the volume until it is used.
So a 2GB private volume with 100M of files will only use 100M.  
This explains how you can have *many* qubes with large private volumes on quite a small disk.
This is called over provisioning.  
You should keep an eye on the disk-space widget to see how much free space you actually have.

It is easy to increase the size of disk images.
There are risks attached to reducing the size of an image, and in general you should not need to do this.

Increasing the size of Disk Images
----------------------------------

There are several disk images which can be easily extended, but pay attention to the overall consumed space of your sparse/thin disk images.
In most cases, the GUI tool Qube Settings (available for every qube from the Start menu, and also in the Qube Manager) will allow you to easily increase maximum disk image size.

![vm-settings-disk-image.png](/attachment/wiki/DiskSize/vm-settings-disk-image.png)

In case of standalone qubes and templates, just change the Disk Storage settings above.
In case of template-based qubes, the private storage (the /home directory and user files) can be changed in the qube's own settings, but the system root image is [inherited from the template](/getting-started/), and so it must be changed in the template settings. 
If you are increasing the disk image size for Linux-based qubes installed from Qubes OS repositories in Qubes 4.0 or later, changing the settings above is all you need to do - in other cases, you may need to do more, according to instructions below.
See also the OS-specific follow-up instructions below.

### Increasing the size of Disk Images

Use either GUI tool Qube Settings (`qubes-vm-settings`) or the CLI tool `qvm-volume`.
Maximum size which can be assigned through Qube Settings is 1048576 MiB - if you need more, use `qvm-volume`:

~~~
qvm-volume extend <vm_name>:root <size>
~~~
OR
~~~
qvm-volume extend <vm_name>:private <size>
~~~

Note: Size is the target size (i.e. 4096MB or 16GB, ...), not the size to add to the existing disk.

If you have run out of space for software in your Template, you need to increase *root image* of the Template (not private storage!). 
**Make sure changes in the Template between reboots don't exceed 10G.**
It is recommended that you restart (or start and then shutdown, if it is not running) the template after resizing the root image.

If you are **not** using Linux in the qube, you will also need to:

1.  Start the template.
2.  Resize the filesystem using OS appropriate tools.
3.  Verify available space in the template using `df -h` or OS specific tools.
4.  Shutdown the template.

#### Windows 7 ####

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

Qubes will automatically grow the filesystem for you on all AppVMs with Qubes packages installed (which are all AppVMs installed from templates, cloned from templates etc. - if you have not created an empty HVM and installed a Linux distribution in it, without using Qubes repositories, you are almost certainly safe).
Otherwise, you will see that there is unallocated free space at the end of your primary disk.
You can use standard linux tools like `fdisk` and `resize2fs` to make this space available.

Decreasing the size of Disk Images
----------------------------------

The number shown for "storage max size" does not mean that the storage is really using that amount. In most cases you need not worry about the size shown.
If you have increased the max size, and do not need it, then you *can*  reduce the allocated size, but there is a risk of data loss.  
Remember you really dont need to do this.

You can create a new qube, copy your files in to the new qube, and delete the old qube. (Simple and effective.)


Or you can take the risk of reducing the size of the disk.
For example, to reduce the private storage of qube1 to 1GiB:  
Open a terminal in dom0:
```
qvm-shutdown qube1
sudo lvresize --size 1024M /dev/qubes_dom0/vm-qube1-private
```

If you have a SSD see [here][fstrim] for information on using fstrim.

[fstrim]: /doc/disk-trim

Troubleshooting Disk Resize
---------------------------

Generally in Qubes OS a resize of a private volume is very straight-forward. 
However, sometimes in the GUI, the resize looks like it worked, but it 
in fact fails silently. If you then try the same operation in the 
dom0 console with a qvm-volume extend, and it fails with an error that 
that looks something like "resize2fs: Permission denied to resize 
filesystem" you have probably run into something that requires more 
extensive manual intervention.

What has probably happened is that there are file system errors, which 
means that a resize2fs will not work until fsck is run first. Qubes OS 
utilities cannot yet handle this case. To fix:

In the dom0 terminal get a root console on the vm (eg. sys-usb) with

~~~
sudo xl console -t pv sys-usb
~~~

Then umount everything mounted on the private volume /dev/xvdb partition. 
(There are typically several mounts listed in /etc/mtab.) At least one 
of them,

~~~
umount /home
~~~

will throw an error because there are processes using the /home directory. 
Get a list of those processes with

~~~
fuser -m /home
~~~

Kill these process until they are all gone. Then

~~~
umount /home
fsck /dev/xvdb
resize2fs /dev/xvdb
~~~

This should square everything away, now restart your VM and observe that 
the private volume size shown externally in the VM's settings GUI is the 
same as that seen within the VM.
