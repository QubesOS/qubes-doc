---
layout: doc
title: ResizeRootDiskImage
permalink: /doc/ResizeRootDiskImage/
redirect_from: /wiki/ResizeRootDiskImage/
---

Resizing \`root.img\` Size
--------------------------

The safest way to increase the size of \`root.img\` is to do it for a standalone
VM (qvm-create --standalone) - which has its own root filesystem
(copy of template, instead of smart sharing).
But it should also work for a normal template (as long as changes in the
template between reboots didn't exceed 10G).

Replace the size and the path (name) of the template as wished and run your
modified command:
~~~
truncate -s 20G /var/lib/qubes/vm-templates/fedora-21/root.img
~~~

Then start your template or standalone VM and run:
~~~
sudo resize2fs /dev/mapper/dmroot
~~~

after that shutdown the template.

Then you should have extended \`root.img\` in your VM/template
