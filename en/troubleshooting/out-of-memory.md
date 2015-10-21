---
layout: doc
title: Out of Memory
permalink: /en/doc/out-of-memory/
redirect_from:
- /doc/OutOfmemory/
- /wiki/OutOfmemory/
---

VMs specially templates use disk space. Also default private storage max size is 2 GB, but it is very easy to increase it as required. In case you use all disk space you get the Out of disk space error that may crash your system because also Dom0 does not have enough disk space to work.

So it is a good practice to regularly check disk space usage with command

~~~
df
~~~

in dom0 terminal.

A system in out of space condition should be able to boot, but may be unable to load a desktop manager. In this case it is possible to login to dom0 terminal with Alt + Ctrl + F2. To recover disk space it may be possible to delete files in a userVM connecting to the userVM terminal:

~~~
qvm-start <VMname>
sudo xl console <VMname>
~~~

If this does not work, check the size of /var/lib/qubes/qubes.xml. If it is zero, you'll need to use one of the file backup (stored in /var/lib/qubes/backup), hopefully you have the current data there. Find the most recent one and place in /var/lib/qubes/qubes.xml instead of the empty file.

In any case you'll need some disk space to start the VM. Check "df" output if you have some. If not, some hints how to free some disk space:

1.  Clean yum cache:

~~~
sudo yum clean all
~~~

1.  Delete .img files of a less important VM, that can be found in

/var/lib/qubes/appvms/. Then, when the system is working again, cleanup the rest with:

~~~
qvm-remove <VMname>
~~~

With this method you lose one VM data, but it'll more securely work.

1.  Decrease filesystem safety margin (5% by default):

~~~
sudo tune2fs -m 4 /dev/mapper/vg_dom0-lv_root
~~~

1.  Remove some unneeded files in dom0 home (if you have one, most likely no).

