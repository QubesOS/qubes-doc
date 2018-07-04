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

Resize Disk Image
-----------------

There are several disk images which can be easily extended, but pay attention to the overall consumed space of your sparse/thin disk images.
See also [OS Specific Follow-up Instructions](/doc/resize-disk-image/#os-specific-follow-up-instructions) at the end of this page.


### Template disk image (R4.0)

If you want install a lot of software in your TemplateVM, you may need to increase the amount of disk space your TemplateVM can use. 
*Make sure changes in the TemplateVM between reboots don't exceed 10G.*

1.  Resize the *root image* using Qubes version specific procedure below.
2.  Start the template.
3.  Resize the filesystem using OS appropriate tools (Qubes will handle this automatically under Linux).
4.  Verify available space in the template using `df -h` or OS specific tools.
5.  Shutdown the template.

### Template disk image (R3.2)

If you want install a lot of software in your TemplateVM, you may need to increase the amount of disk space your TemplateVM can use. 
*Make sure changes in the TemplateVM between reboots don't exceed 10G.*

1.  Make sure that all the VMs based on this template are shut down (including netvms etc).
2.  Resize the *root image* using Qubes version specific procedure below.
3.  If any netvm/proxyvm used by this template is based on it, set template's netvm to none.
4.  Start the template.
5.  Resize the filesystem using OS appropriate tools (Linux is `sudo resize2fs /dev/mapper/dmroot`).
6.  Verify available space in the template using `df -h` or OS specific tools.
7.  Shutdown the template.
8.  Restore original netvm setting (if changed), and check firewall settings (setting netvm to none causes the firewall to reset to "block all")

### Expand disk image (R4.0)

1048576 MiB is the maximum size which can be assigned to storage through Qube Manager.

To grow the root or private disk image of an AppVM beyond this limit, `qvm-volume` can be used:

~~~
qvm-volume extend <vm_name>:root <size>
~~~
OR
~~~
qvm-volume extend <vm_name>:private <size>
~~~

Note: Size is the target size (i.e. 4096MB or 16GB, ...), not the size to add to the existing disk.

### Expand disk image (R3.2)

1048576 MB is the maximum size which can be assigned to storage through Qubes Manager.

To grow the private disk image of an AppVM beyond this limit, `qvm-grow-root` or [qvm-grow-private](/doc/dom0-tools/qvm-grow-private/) can be used:

~~~
qvm-grow-root <vm-name> <size>
~~~
OR
~~~
qvm-grow-private <vm-name> <size>
~~~

Note: Size is the target size (i.e. 4096MB or 16GB, ...), not the size to add to the existing disk. 

### Resize a StandaloneVM Root Image

For more flexibility, you may also turn your TemplateVM into a StandaloneVM.
Doing this means it will have its own root filesystem *(StandaloneVMs use a copy of the template, instead of smart sharing)*.
To do this run `qvm-create --standalone` from `dom0` console, then perform the [OS Specific Follow-up Instructions](/doc/resize-disk-image/#os-specific-follow-up-instructions) below.

### Shrinking a disk image

Ext4 and most other filesystems do not support online shrinking, so it can't be done as conveniently as growing the image.
Note that we don't want to touch the VM filesystem directly in dom0 for security reasons. 

1.  Create a new qube with smaller disk using Qube Manager or `qvm-create`
2.  Move data to the new qube using `qvm-copy`, backup & restore, or OS utilities
3.  Delete old qube using Qube Manager or `qvm-remove`

OS Specific Follow-up Instructions
-----------------

After expanding volumes, the partition table and file-system may need to be adjusted.
Use tools appropriate to the OS in your qube.
Brief instructions for Windows 7, FreeBSD, and Linux are provided below.

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

Qubes will automatically grow the filesystem for you on AppVMs but not HVMs (or Template root images on R3.2).
You will see that there is unallocated free space at the end of your primary disk.
You can use standard linux tools like `fdisk` and `resize2fs` to make this space available.
