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

The safest way to increase the size of `root.img` is to turn your TemplateVM into a StandaloneVM. Doing this means it will have it's own root filesystem *(StandaloneVMs use a copy of template, instead of smart sharing)*. To do this run `qvm-create --standalone` from `dom0` Konsole.

### Resize a StandaloneVM Root Image

In `dom0` Konsole run the following command (replace the size and path):

~~~
truncate -s 20G /var/lib/qubes/appvms/standalonevm/root.img
~~~

Then start Terminal for this StandaloneVM and run:

~~~
sudo resize2fs /dev/mapper/dmroot
~~~

Shutdown the StandaloneVM and you will have extended the size of it's `root.img`


### Resize a TemplateVM Root Image

Shut down the TemplateVM, as well as all VMs based on that template (since they
share `root.img`).
In `dom0` Konsole run the following command (replace the size and path):
*Make sure changes in the TemplateVM between reboots didn't exceed 10G.*

~~~
truncate -s 20G /var/lib/qubes/vm-templates/fedora-21/root.img
~~~

Then start only the TemplateVM and run the following. Note that if you are
resizing the TemplateVM used by, e.g., your NetVM, you may need to disable
networking so when the TemplateVM is started, it does not autostart other VMs
based on the same `root.img`. Otherwise you will get an error message `Nothing
to do!`.

~~~
sudo resize2fs /dev/mapper/dmroot
~~~

Shutdown the TemplateVM and you will have extended the size of it's `root.img`.
