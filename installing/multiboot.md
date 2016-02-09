---
layout: doc
title: Multibooting
permalink: /doc/multiboot/
---

Multibooting Qubes 
========================================

1.  [Introduction](#introduction)
2.  [Windows](#windows)
3.  [Linux](#linux)
4.  [Troubleshooting](#troubleshooting)

Introduction
---------------------

You should think carefully before dual booting Qubes on your box.
Read the [guidelines](/doc/security-guidelines) carefully.

One problem is that when you dual or multiboot, even if you are using
encryption on your Qubes installation, /boot is still unprotected and
could be maliciously modified by the other OS, possibly leading to Qubes
itself being maliciously modifed.

The other problem is firmware security - for example the other system
could infect BIOS firmware, which might enable compromise or spying on
the Qubes system.

You can use [Anti Evil Maid](/doc/anti-evil-maid/), which would inform
you if /boot had been modified, but it cannot prevent or fix the problem.

If you have considered these issues, tried out the live system and want to
install Qubes alongside your existing OS, these notes should help.

They assume that you are installing Qubes on a PC where you already have
another OS installed.

The first thing to do is STOP.  
Before you do anything else back up all your data.  
If possible do a full system backup.  
Back up the MBR.  
Back up /boot.  
If you are really paranoid clone your disc.

Make sure you have install discs to hand for the existing operating system.

Qubes 3.0 does not support UEFI boot. If you are already using it the first step
is to change boot mode.

Most PCs using UEFI firmware and bootloader can be configured to disable
UEFI entirely and instead revert to legacy MBR boot mode. 

Two separate steps are often required to achieve this:

*    Enabling legacy boot mode
*    Disabling Secure Boot


Qubes by default does not include other systems in the generated grub menu, 
because handling of other systems has been disabled. This means
that you will have to manually add grub entries for any other OS.

The general approach is:

* Enable legacy boot mode
* Ensure current OS boots in legacy mode.  
* Install Qubes
* Manually add boot stanzas to /etc/grub.d/40_custom
* Update grub



Windows
----------------------

If you change boot mode to legacy boot almost certainly the Windows
installation will not boot.
You will either have to format the disk and reinitialise it, and then reinstall
Windows in legacy boot mode, or use a utility like Easy Recovery Essentials
which will change the existing installation to be bootable in both
UEFI/GPT and BIOS/MBR mode in-place, without losing any data.

At this stage you can install Qubes.

As noted above the default configuration will not add an entry for Windows to
the grub menu, so you will need to add one.

1. Boot into Qubes.

2. Identify the Windows system partition that has /bootmgr 

    In blkid output, the system partition is the one with LABEL='SYSTEM
    RESERVED' or LABEL='SYSTEM' and is only about 100 to 200 MB in size

3. Add this stanza to /etc/grub.d/40_custom,

~~~
menuentry "Windows" {
     insmod part_msdos
     insmod ntldr
     insmod ntfs
     ntldr (hd1,X)/bootmgr
}
(Change X to reflect the relevant system partition.)
~~~

Then update the grub config:

~~~
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
~~~

There is no  need to reinstall grub itself.



Linux
----------------------

If you have had to change to legacy boot mode then you may have to reinstall grub in
the existing OS. (Make sure that you use grub rather than a grub-efi version).

Micah Lee
[suggests](https://micahflee.com/2014/04/dual-booting-qubes-and-ubuntu-with-encrypted-disks/)
installing grub to a partition, and then installing Qubes with grub
installed in MBR.

If you take this approach then you need to add to /etc/grub.d/40_custom in Qubes
dom0:

~~~
menuentry "Other Linux" {
set root=(hd1,X)
chainloader +1
}
(Change X to reflect the relevant partition where grub is installed.)
~~~

Then update the grub config:

~~~
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
~~~

There is no  need to reinstall grub itself.


Existing /boot partition, grub installed in MBR
----------------------

Most distros will have already installed grub to the MBR.

It is possible to use the *same* /boot for both OS.  
To do this, do **NOT** choose the automatic configuration option when installing
Qubes.  
Select 'custom' layout, and assign the existing /boot partition as /boot.  
Deselect the 'Format' option.  
Then continue with the installation.  
This will install the qubes boot files in /boot *alongside* the existing files,
but overwrite the grub.cfg file in /boot/grub2.

If the other distro uses legacy grub you can simply copy the relevant sections
from /boot/grub/grub.cfg into /etc/grub.d/40_custom.  

If the other distro uses grub2 then copy the relevant sections
from the backup you made into /etc/grub.d/40_custom.

Then update the grub config:

~~~
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
~~~



Troubleshooting
----------------------

If you install Qubes without making any backups beforehand, dont worry.  
If you didnt overwrite the original partitions, then it is usually
possible to recover your old systems relatively easily, as described above.

If you decided to use a shared /boot and *dont* have backups of your previous
grub config, it is quite easy to fix this.  
This example may help.  

* Boot into Qubes.  
* Back up (at a minimum) /boot/grub2  
* Identify the partition containing the other OS.  
* Then mount the other OS and chroot in to it.  

~~~
sudo mount /dev/sdX /mnt
sudo mount --bind /dev/sdY /mnt/boot
sudo mount --bind /dev /mnt/dev 
sudo mount --bind /dev/pts /mnt/dev/pts
sudo mount --bind /proc /mnt/proc 
sudo mount --bind /sys /mnt/sys 

sudo chroot /mnt
~~~

* Update the grub config:

~~~
sudo grub2-mkconfig -o /boot/grub2/grub.cfg.new
~~~

* Exit out the chroot, and reverse the mounts.  
* Copy the relevant sections from /boot/grub2/grub.cfg.new in to
/etc/grub.d/40_custom.
* Update the grub config:

~~~
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
~~~
