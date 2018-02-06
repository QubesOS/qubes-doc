---
layout: doc
title: Disk TRIM
permalink: /doc/disk-trim/
redirect_from:
- /en/doc/disk-trim/
- /doc/DiskTRIM/
- /wiki/DiskTRIM/
---

Disk Trim
----------

Disk trimming is the procedure by which the operating system informs the underlying storage device of which storage blocks are no longer in use.
It does this by issuing an `ATA_TRIM` command for the block. This is also known as a `discard`.
In this way, the storage device can perform garbage collection of the unused blocks and internally prepare them for reuse. SSDs in general benefit from this, while HDDs do not.

In a Linux system running on bare metal, this is relatively straight-forward. 
When instructed by the operating system, discards are issued by the file-system driver directly to the storage driver and then to the SSD.

In Qubes, this gets more complex due to virtualization, LUKS, and LVM (and thin pools on R4.0 and up).
If you run `fstrim --all` inside a TemplateVM, the `discard` can follow a path like:

    OS -> File-system Driver -> Virtual Storage Driver -> Backend Storage Driver -> LVM Storage Driver -> LUKS Driver -> Physical Storage Driver -> Physical Storage Device
    
If discards are not supported at any one of those layers, it will not make it to the underlying physical device.

There are some security implications to permitting TRIM (read for example [this article](https://asalor.blogspot.com/2011/08/trim-dm-crypt-problems.html)), but in most cases not exploitable.


Configuration
----------

In all versions of Qubes, you may want to set up a periodic job in `dom0` to trim the disk.

This can be done from a terminal as root, by creating a `trim` file in `/etc/cron.daily` (or `/etc/cron.weekly`).
Add the following contents:

```
#!/bin/bash
/sbin/fstrim --all
```

And mark it as executable with `chmod 755 /etc/cron.daily/trim`.

**Note** Although discards can be issued on every delete by adding the `discard` mount option to `/etc/fstab`, this option can hurt performance so the above procedure is recommended instead.

If you are using Qubes with LVM, you may also want to set `issue_discards = 1` in `/etc/lvm/lvm.conf`.
Setting this option will permit LVM to issue discards to the SSD when logical volumes are shrunk or deleted.
This is relatively rare in R3.x, but more frequent in R4.x with disposable VMs.

To verify if discards are enabled you may use `dmsetup table` (confirm the line for your device mentions "discards") or just run `fstrim -av` (you should see a number of bytes trimmed).

See also version specific notes below.


R4.0
----------

TRIM support is enabled by default at all layers, including LUKS.

LVM Logical volumes are frequently deleted (every time a disposable VM is shut down, for example) so setting `issue_discards = 1` in `/etc/lvm/lvm.conf` is recommended if using an SSD.


R3.2.1
----------

TRIM support is enabled by default at all layers, including LUKS.


R3.2
----------

VMs have already TRIM enabled by default, but dom0 doesn't. 

To enable TRIM in dom0 you need:

1. Get your LUKS device UUID:

    ~~~
    ls /dev/mapper/luks-*
    ~~~

2. Add entry to `/etc/crypttab` (replace luks-\<UUID\> with the device name and the \<UUID\> with UUID alone):

    ~~~
    luks-<UUID> UUID=<UUID> none discard
    ~~~

3. Add `rd.luks.options=discard` to kernel cmdline (follow either GRUB2 or EFI, not both): 
    * GRUB2: `/etc/default/grub`, `GRUB_CMDLINE_LINUX` line and  
      Rebuild grub config (`grub2-mkconfig -o /boot/grub2/grub.cfg`)   
    * EFI: `/boot/efi/EFI/qubes/xen.cfg`, `kernel=` line(s)

4. Rebuild initrd **in hostonly mode**:

    ~~~
    dracut -H -f
    ~~~

5. Reboot the system and verify that discards are really enabled.

