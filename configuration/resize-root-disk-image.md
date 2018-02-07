---
layout: doc
title: Resize Root Disk Image
permalink: /doc/resize-root-disk-image/
redirect_from:
- /en/doc/resize-root-disk-image/
- /doc/ResizeRootDiskImage/
- /wiki/ResizeRootDiskImage/
---

Resize Root Disk Image
----------------------

See additional information and caveats about [resizing private disk images](/doc/resize-disk-image/), paying particular attention to "OS Specific Follow-up Instructions" at the end.

### Template disk image 

If you want install a lot of software in your TemplateVM, you may need to increase the amount of disk space your TemplateVM can use. 
*Make sure changes in the TemplateVM between reboots don't exceed 10G.*

1.  Make sure that all the VMs based on this template are shut off (including netvms etc).
2.  Resize root image using Qubes version specific procedure below.
3.  If any netvm/proxyvm used by this template is based on it, set template's netvm to none.
4.  Start the template.
5.  Resize the filesystem using OS appropriate tools (Qubes will handle this automatically with Linux templates).
6.  Verify available space in the template using `df -h` or OS specific tools.
7.  Shutdown the template.
8.  Restore original netvm setting (if changed), check firewall settings (setting netvm to none causes the firewall to reset to "block all")

### Root disk image (R4.0)

1048576 MiB is the maximum size which can be assigned to root storage through Qube Manager.

To grow the root disk image of an AppVM beyond this limit, `qvm-volume` can be used:

~~~
qvm-volume extend <vm_name>:root <size>
~~~

Note: Size is the target size (i.e. 4096MB or 16GB, ...), not the size to add to the existing disk.

### Root disk image (R3.2)

1048576 MB is the maximum size which can be assigned to root storage through Qubes Manager.

To grow the root disk image of an AppVM beyond this limit, `qvm-grow-root` can be used:

~~~
qvm-grow-root <vm-name> <size>
~~~

Note: Size is the target size (i.e. 4096MB or 16GB, ...), not the size to add to the existing disk. 

### Resize a StandaloneVM Root Image (R3.2)

Another way to increase the size of `root.img` is to turn your TemplateVM into a StandaloneVM.
Doing this means it will have it's own root filesystem *(StandaloneVMs use a copy of template, instead of smart sharing)*.
To do this run `qvm-create --standalone` from `dom0` console.

In `dom0` console run the following command (replace the size and path):

~~~
truncate -s 20G /var/lib/qubes/appvms/standalonevm/root.img
~~~

Then start Terminal for this StandaloneVM and run:

~~~
sudo resize2fs /dev/mapper/dmroot
~~~

Shutdown the StandaloneVM and you will have extended the size of its `root.img`.
