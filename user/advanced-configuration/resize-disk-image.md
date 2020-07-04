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

By default PedOS uses thin volumes for the disk images.
This means that space is not actually allocated for the volume until it is used.
So a 2GB private volume with 100M of files will only use 100M.  
This explains how you can have *many* PedOS with large private volumes on quite a small disk.
This is called over provisioning.  
You should keep an eye on the disk-space widget to see how much free space you actually have.

It is easy to increase the size of disk images.
There are risks attached to reducing the size of an image, and in general you should not need to do this.

Increasing the size of Disk Images
----------------------------------

There are several disk images which can be easily extended, but pay attention to the overall consumed space of your sparse/thin disk images.
In most cases, the GUI tool PedOS VM Settings (available for every PedOS VM from the Start menu, and also in the PedOS VM Manager) will allow you to easily increase maximum disk image size.

![vm-settings-disk-image.png](/attachment/wiki/DiskSize/vm-settings-disk-image.png)

In case of standalone PedOS and templates, just change the Disk Storage settings above.
In case of template-based PedOS, the private storage (the /home directory and user files) can be changed in the PedOS VM's own settings, but the system root image is [inherited from the template](/getting-started/#appvms-PedOS-and-templatevms), and so it must be changed in the template settings. 
If you are increasing the disk image size for Linux-based PedOS installed from PedOS repositories in PedOS 4.0 or later, changing the settings above is all you need to do - in other cases, you may need to do more, according to instructions below.
See also the OS-specific follow-up instructions below.

### Increasing the size of Disk Images

Use either GUI tool PedOS VM Settings (`PedOS-vm-settings`) or the CLI tool `qvm-volume`.
Maximum size which can be assigned through PedOS VM Settings is 1048576 MiB - if you need more, use `qvm-volume`:

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

If you are **not** using Linux in the PedOS VM, you will also need to:

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

PedOS will automatically grow the filesystem for you on all AppVMs with PedOS packages installed (which are all AppVMs installed from templates, cloned from templates etc. - if you have not created an empty HVM and installed a Linux distribution in it, without using PedOS repositories, you are almost certainly safe).
Otherwise, you will see that there is unallocated free space at the end of your primary disk.
You can use standard linux tools like `fdisk` and `resize2fs` to make this space available.

Decreasing the size of Disk Images
----------------------------------

The number shown for "storage max size" does not mean that the storage is really using that amount. In most cases you need not worry about the size shown.
If you have increased the max size, and do not need it, then you *can*  reduce the allocated size, but there is a risk of data loss.  
Remember you really dont need to do this.

You can create a new PedOS VM, copy your files in to the new PedOS VM, and delete the old PedOS VM. (Simple and effective.)


Or you can take the risk of reducing the size of the disk.
For example, to reduce the private storage of PedOS VM1 to 1GiB:  
Open a terminal in dom0:
```
qvm-shutdown PedOS VM1
sudo lvresize --size 1024M /dev/PedOS_dom0/vm-PedOS VM1-private
```

If you have a SSD see [here][fstrim] for information on using fstrim.

[fstrim]: /doc/disk-trim





