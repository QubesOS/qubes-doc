---
layout: doc
title: UEFI Troubleshooting
permalink: /doc/uefi-troubleshooting/
---

Troubleshooting UEFI related problems
========================================


Cannot start installation, installation completes successfully but then BIOS loops at boot device selection, hangs at four penguins after choosing "Test media and install Qubes OS" in GRUB menu
---------------------

There is some [common bug in UEFI implementation](http://xen.markmail.org/message/f6lx2ab4o2fch35r), affecting mostly Lenovo systems, but probably some others too. You can try existing workaround:

01. In GRUB menu<sup id="a1-1">[1](#f1)</sup>, select "Troubleshoot", then "Boot from device", then press `e`.
02. At the end of `chainloader` line add `/mapbs /noexitboot`.
03. Perform installation normally, but not reboot system at the end yet.
04. Go to `tty2` (Ctrl-Alt-F2).
05. Enable `/mapbs /noexitboot` on just installed system. This step differs between Qubes releases:
   
    **For Qubes 3.1:**

06. Execute `mount | grep boot/efi` and note device name (first column). It should be something like `/dev/sda1`.
07. Execute `efibootmgr -v`, search for `Qubes` entry and note its number (it should be something like `Boot0001` - `0001` is an entry number).
08. Replace existing `Qubes` entry with modified one. Replace `XXXX` with entry number from previous step, `/dev/sda` with your disk name and `-p 1` with `/boot/efi` partition number):

        efibootmgr -b XXXX -B
        efibootmgr -v -c -u -L Qubes -l /EFI/qubes/xen.efi -d /dev/sda -p 1 "placeholder /mapbs /noexitboot"

09. Compare new entry with the old one (printed in step 6) - it should only differ in additional options at the end, and look probably something like this:

        Boot0001* Qubes HD(1,GPT,partition-guid-here,0x800,0x64000)/File(\EFI\qubes\xen.efi)p.l.a.c.e.h.o.l.d.e.r. ./.m.a.p.b.s. ./.n.o.e.x.i.t.b.o.o.t.

    If instead it looks like:

        Boot0001* Qubes HD(1,0,00000000...0,0x0,0x0)/File(\EFI\qubes\xen.efi)p.l.a.c.e.h.o.l.d.e.r. ./.m.a.p.b.s. ./.n.o.e.x.i.t.b.o.o.t.

    then try passing `/dev/sda1` or `/dev/nvme0n1p1` or whatever is your EFI partition instead of `/dev/sda` and `-p 1`.

10. Now you can reboot the system by issuing `reboot` command.

    **For Qubes 3.2 or later:**

11. Edit `/mnt/sysimage/boot/efi/EFI/qubes/xen.cfg` (you can use `vi` editor) and add to every kernel section:
            
        mapbs=1
        noexitboot=1

    **Note:** You must add these parameters on two separate new lines (one
    paramater on each line) at the end of each section that includes a kernel
    line (i.e., all sections except the first one, since it doesn't have a
    kernel line).

12. Now you can reboot the system by issuing `reboot` command.


System crash/restart when booting installer
-------------------------------------------

Some Dell systems and probably others have [another bug in UEFI firmware](http://markmail.org/message/amw5336otwhdxi76). And there is another workaround for it:


1. In GRUB menu<sup id="a1-2">[1](#f1)</sup> press `e`.
2. At the end of `chainloader` line add `-- efi=attr=uc`.
3. Perform installation normally, but not reboot system at the end yet.
4. Go to `tty2` (Ctrl-Alt-F2).
5. Execute:

        sed -i -e 's/^options=.*/\0 efi=attr=uc/' /mnt/sysimage/boot/efi/qubes/xen.cfg
        
   or if you're installing 3.2 execute:
   
        sed -i -e 's/^options=.*/\0 efi=attr=uc/' /mnt/sysimage/boot/efi/EFI/qubes/xen.cfg

6. Now you can reboot the system by issuing `reboot` command.

* * *
<b name="f1">1</b> If you use rEFInd, you can see 3 options regarding the USB installer. Choose "Fallback Boot Loader" to enter the GRUB menu. [↩](#a1-1) [↩](#a1-2)


Boot device not recognized after installing
------------------------------------------

Some firmware will not recognize the default Qubes EFI configuration. As such,
it will have to be manually edited to be bootable (this will need to be done after
every kernel and Xen update.)

1. Copy `/boot/efi/EFI/qubes/` to `/boot/efi/EFI/BOOT/`.
2. Rename `/boot/efi/EFI/BOOT/xen.efi` to `/boot/efi/EFI/BOOT/BOOTX64.efi`.
3. Rename `/boot/efi/EFI/BOOT/xen.cfg` to `/boot/efi/EFI/BOOT/BOOTX64.cfg`.
