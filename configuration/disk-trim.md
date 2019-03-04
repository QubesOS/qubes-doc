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
=========

Disk trimming is the procedure by which the operating system informs the underlying storage device of which storage blocks are no longer in use.
It does this by issuing an `ATA_TRIM` command for the block. This is also known as a `discard`.
In this way, the storage device can perform garbage collection of the unused blocks and internally prepare them for reuse. SSDs in general benefit from this, while HDDs do not.

In a Linux system running on bare metal, this is relatively straight-forward. 
When instructed by the operating system, discards are issued by the file-system driver directly to the storage driver and then to the SSD.

In Qubes, this gets more complex due to virtualization, LUKS, and LVM (and thin pools on R4.0 and up).
If you run `fstrim --all` inside a TemplateVM, in a worst case the `discard` can follow a path like:

    OS -> File-system Driver -> Virtual Storage Driver -> Backend Storage Driver -> LVM Storage Driver -> LUKS Driver -> Physical Storage Driver -> Physical Storage Device
    
If discards are not supported at any one of those layers, it will not make it to the underlying physical device.

There are some security implications to permitting TRIM (read for example [this article](https://asalor.blogspot.com/2011/08/trim-dm-crypt-problems.html)), but in most cases not exploitable.
Conversely, TRIM can improve security against local forensics when using SSDs, because with TRIM enabled deleting data (usually) results in the actual data being erased quickly, rather than remaining in unallocated space indefinitely.
However deletion is not guaranteed, and can fail to happen without warning for a variety of reasons.


Configuration
----------

In all versions of Qubes, you may want to set up a periodic job in `dom0` to trim the disk.
This can be done with either systemd (weekly only) or cron (daily or weekly).

 * **Systemd**

   From a terminal as a regular user:

   ```
   systemctl enable fstrim.timer
   systemctl start fstrim.timer
   ```

 * **Cron**

   This can be done from a terminal as root, by creating a `trim` file in `/etc/cron.daily` (or `/etc/cron.weekly`).
    Add the following contents:

    ```
   #!/bin/bash
   /sbin/fstrim --all
   ```
   And mark it as executable with `chmod 755 /etc/cron.daily/trim`.

**Note** Although discards can be issued on every delete inside `dom0` by adding the `discard` mount option to `/etc/fstab`, this option can hurt performance so the above procedure is recommended instead.
However, inside App and Template qubes, the `discard` mount option is on by default to notify the LVM thin pool driver (R4.0) or sparse file driver (R3.2) that the space is no longer needed and can be zeroed and re-used.

If you are using Qubes with LVM, you may also want to set `issue_discards = 1` in `/etc/lvm/lvm.conf`.
Setting this option will permit LVM to issue discards to the SSD when logical volumes are shrunk or deleted.
In R4.x, LVM Logical volumes are frequently deleted (every time a disposable VM is shut down, for example) so you may want to set `issue_discards = 1` if using an SSD, but see the article linked in the first section of this page.
However, this is relatively rare in R3.x.


LUKS
----------

If you have enabled LUKS in dom0, discards will not get passed down to the storage device. 

To enable TRIM support in dom0 with LUKS you need to:

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
      Rebuild grub config (`grub2-mkconfig -o /boot/grub2/grub.cfg`), then  
      Rebuild initrd (`dracut -f`)
    * EFI: `/boot/efi/EFI/qubes/xen.cfg`, `kernel=` line(s), then  
      Rebuild initrd (`dracut -f /boot/efi/EFI/qubes/initramfs-$(uname -r).img $(uname -r)`)

4. Reboot the system.

5. To verify if discards are enabled you may use `dmsetup table` (confirm the line for your device mentions "discards") or just run `fstrim -av` (you should see a `/` followed by the number of bytes trimmed).


Swap Space
----------

By default TRIM is not enabled for swap.
To enable it add the `discard` flag to the options for the swap entry in `/etc/fstab`.
This may or may not actually improve performance.
If you only want the security against local forensics benefit of TRIM, you can use the `discard=once` option instead to only perform the TRIM operation once during at boot.

To verify that TRIM is enabled, check `dmesg` for what flags were enabled when the swap space was activated.
You should see something like the following:

    Adding 32391164k swap on /dev/mapper/qubes_dom0-swap.  Priority:-2 extents:1 across:32391164k SSDscFS

The `s` indicates that the entire swap device will be trimmed at boot, and `c` indicates that individual pages are trimmed after they are no longer being used.
