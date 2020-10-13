---
layout: doc
title: Out of Memory
permalink: /doc/out-of-memory/
redirect_from:
- /en/doc/out-of-memory/
- /doc/OutOfmemory/
- /wiki/OutOfmemory/
---

VMs (especially templates) use pre-allocated space. The default private storage max size is 2 GB, but it's very easy to increase as needed. If the disk is completely full, you will get an `Out of disk space` error that may crash your system because Dom0 does not have enough disk space to work. So it's good practice to regularly check disk space usage with the command `df -h` in dom0 terminal.

A system that's out of space should be able to boot, but may be unable to load a desktop manager. In this case it is possible to login to dom0 terminal with Alt + Ctrl + F2. To recover disk space it may be possible to delete files in a userVM by connecting to the userVM terminal:

~~~
qvm-start <VMname>
qvm-console-dispvm <VMname>
~~~

If this does not work, check the size of /var/lib/qubes/qubes.xml. If it is zero, you'll need to use one of the file backup (stored in /var/lib/qubes/backup), hopefully you have the current data there. Find the most recent one and place in /var/lib/qubes/qubes.xml instead of the empty file.

In any case you'll need some disk space to start the VM. Check `df -h` output if you have some. If not, here are some hints how to free some disk space:

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

