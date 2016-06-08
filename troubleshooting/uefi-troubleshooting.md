---
layout: doc
title: UEFI Troubleshooting
permalink: /doc/uefi-troubleshooting/
---

Troubleshooting UEFI related problems
========================================


Cannot start installation, hangs at four penguins after choosing "Test media and install Qubes OS" in GRUB menu
---------------------

There is some [common bug in UEFI implementation](http://xen.markmail.org/message/f6lx2ab4o2fch35r), affecting mostly Lenovo systems, but probably some others too. You can try existing workaround:

01. In GRUB menu<sup id="a1-1">[1](#f1)</sup> press `e`.
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

09. Compare new entry with the old one (printed in step 6) - it should only differ in additional options at the end.
10. Now you can reboot the system by issuing `reboot` command.

    **For Qubes 3.2 or later:**

11. Edit `/mnt/sysimage/boot/efi/EFI/qubes/xen.cfg` (you can use `vi` editor) and add to every kernel section:
            
        mapbs=1
        noexitboot=1

12. Now you can reboot the system by issuing `reboot` command.


System crash/restart when booting installer
-------------------------------------------

Some Dell systems and probably others have [another bug in UEFI firmware](http://markmail.org/message/amw5336otwhdxi76). And there is another workaround for it:


1. In GRUB menu<sup id="a1-2">[1](#f1)</sup> press `e`.
2. At the end of `chainloader` line add `-- efi=attr=uc`.
3. Perform installation normally, but not reboot system at the end yet.
4. Go to `tty2` (Ctrl-Alt-F2).
5. Execute:

        sed -i -e 's/^options=.*/\0 efi=attr=uc' /mnt/sysimage/boot/efi/qubes/xen.cfg

6. Now you can reboot the system by issuing `reboot` command.

* * *
<b name="f1">1</b> If you use rEFInd, you can see 3 options regarding the USB installer. Choose "Fallback Boot Loader" to enter the GRUB menu. [↩](#a1-1) [↩](#a1-2)
