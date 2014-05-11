---
layout: wiki
title: DiskTRIM
permalink: /wiki/DiskTRIM/
---

VMs have already TRIM enabled by default, but dom0 doesn't. There are some security implications (read for example [​this article](http://asalor.blogspot.com/2011/08/trim-dm-crypt-problems.html)), but IMO not very serious.

To enable TRIM in dom0 you need:

1.  Get your root device UUID:

    ``` {.wiki}
    blkid /dev/mapper/*root
    ```

2.  Add entry to `/etc/crypttab` (replace \<UUID\> with the device UUID):

    ``` {.wiki}
    luks-<UUID> UUID=<UUID> none allow-discards
    ```

3.  Add `rd.luks.allow-discards=1` to kernel cmdline (`/etc/default/grub`, GRUB\_CMDLINE\_LINUX line)
4.  Rebuild grub config (`grub2-mkconfig -o /boot/grub2/grub.cfg`)
5.  Rebuild initrd **in hostonly mode**:

    ``` {.wiki}
    dracut -H -f
    ```

6.  Add "discard" option to `/etc/fstab` for root device
7.  Reboot the system, verify that allow-discards is really enabled (`dmsetup table`)

There is a [​bug affecting allow-discards option](https://bugzilla.redhat.com/show_bug.cgi?id=890533), once it will be fixed, first two steps will be no longer needed.
