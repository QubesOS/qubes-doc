---
layout: doc
title: UEFI Troubleshooting
permalink: /doc/uefi-troubleshooting/
---

Troubleshooting UEFI related problems
========================================

Change installer kernel parameters in UEFI
---------------------

If you've installed successfully in legacy mode but had to change some kernel parameters for it to work, you should try installing in UEFI mode with the same parameters.

**Change the xen configuration on a USB media**
01. Attach the usb disk, mount the EFI partition (second partition available on the disk) 
02. With `sudo`, edit your xen config (`EFI/BOOT/BOOTX64.cfg`) changing the `kernel` key to add your kernel parameters on the boot entry of your choice
03. Install using your modified boot entry

**Change xen configuration directly in an iso image**
01. Get EFI partition boundaries `parted Qubes-R4.0-rc4-x86_64.iso unit B print`
02. Using the start address and the size of the EFI partition, setup a loop device for it `sudo losetup -o 524288 --sizelimit 30562304 /dev/loop0 Qubes-R4.0-rc4-x86_64.iso`
03. Mount the loop device `sudo mount /dev/loop0 /mnt`
04. Edit `EFI/BOOT/BOOTX64.cfg` to add your params to the `kernel` configuration key
05. Save your changes, unmount and dd to usb device


Boot device not recognized after installing
------------------------------------------

Some firmware will not recognize the default Qubes EFI configuration. As such,
it will have to be manually edited to be bootable. This will need to be done after
every kernel and Xen update to ensure you use the most recently installed versions.

1. Copy the `/boot/efi/EFI/qubes/` directory to `/boot/efi/EFI/BOOT/`
(the contents of `/boot/efi/EFI/BOOT` should be identical to `/boot/efi/EFI/qubes`
besides what is described in steps 2 and 3):

       cp -r /boot/efi/EFI/qubes/. /boot/efi/EFI/BOOT

2. Rename `/boot/efi/EFI/BOOT/xen.cfg` to `/boot/efi/EFI/BOOT/BOOTX64.cfg`:

       mv /boot/efi/EFI/BOOT/xen.cfg /boot/efi/EFI/BOOT/BOOTX64.cfg

3. Copy `/boot/efi/EFI/qubes/xen-*.efi` to `/boot/efi/EFI/qubes/xen.efi`
and `/boot/efi/EFI/BOOT/BOOTX64.efi`. For example with Xen 4.8.3
(you may need to confirm file overwrite):

       cp /boot/efi/EFI/qubes/xen-4.8.3.efi /boot/efi/EFI/qubes/xen.efi
       cp /boot/efi/EFI/qubes/xen-4.8.3.efi /boot/efi/EFI/BOOT/BOOTX64.efi

Installation finished but "Qubes" boot option is missing and xen.cfg is empty
--------------------------------------------------------------------------------------

In some cases installer fails to finish EFI setup and leave the system without
Qubes-specific EFI configuration. In such a case you need to finish those parts
manually. You can do that just after installation (switch to `tty2` with
Ctrl-Alt-F2), or booting from installation media in "Rescue a Qubes system" mode.

1. Examine `/boot/efi/EFI/qubes` (if using Qubes installation media, it's in `/mnt/sysimage/boot/efi/EFI/qubes`). You should see 4 files there:

    - xen.cfg (empty, size 0)
    - xen-(xen-version).efi
    - vmlinuz-(kernel-version)
    - initramfs-(kernel-version).img

2. Copy `xen-(xen-version).efi` to `xen.efi`:

       cd /mnt/sysimage/boot/efi/EFI/qubes
       cp xen-*.efi xen.efi

3. Create xen.cfg with this content (adjust kernel version, and filesystem
   locations, below values are based on default installation of Qubes 3.2):


       [global]
       default=4.4.14-11.pvops.qubes.x86_64

       [4.4.14-11.pvops.qubes.x86_64]
       options=loglvl=all dom0_mem=min:1024M dom0_mem=max:4096M
       kernel=vmlinuz-4.4.14-11.pvops.qubes.x86_64 root=/dev/mapper/qubes_dom0-root rd.lvm.lv=qubes_dom0/root rd.lvm.lv=qubes_dom0/swap i915.preliminary_hw_support=1 rhgb quiet
       ramdisk=initramfs-4.4.14-11.pvops.qubes.x86_64.img

4. Create boot entry in EFI firmware (replace `/dev/sda` with your disk name and `-p 1` with `/boot/efi` partition number):

       efibootmgr -v -c -u -L Qubes -l /EFI/qubes/xen.efi -d /dev/sda -p 1 "placeholder /mapbs /noexitboot"


Installation freezes before displaying installer
-----------------------------------------------------------

Some systems can freeze with the default UEFI install options.
You can try the following to remove `noexitboot` and `mapbs`.
If you have an Nvidia card, see also [Nvidia Troubleshooting](/doc/nvidia-troubleshooting/#disabling-nouveau).

1. Follow the [steps above](/doc/uefi-troubleshooting/#change-installer-kernel-parameters-in-uefi) to edit the `[qubes-verbose]` section of your installer's `xen.cfg`.
   You want to comment out the `mapbs` and `noexitboot` lines.
   The end result should look like this:
   ~~~
   [qubes-verbose]
   options=console=vga efi=attr=uc
   # noexitboot=1
   # mapbs=1
   kernel=vmlinuz inst.stage2=hd:LABEL=Qubes-R4.0-x86_64 i915.alpha_support=1
   ramdisk=initrd.img
   ~~~
2. Boot the installer and continue to install as normal, but don't reboot the system at the end when prompted.
3. Go to `tty2` (Ctrl-Alt-F2).
4. Use your preferred text editor (`nano` works) to edit `/mnt/sysimage/boot/efi/EFI/qubes/xen.cfg`, verifying the `noexitboot` and `mapbs` lines are not present.
This is also a good time to make permanent any other changes needed to get the installer to work, such as `nouveau.modeset=0`.
   For example:
   ~~~
   [4.14.18-1.pvops.qubes.x86_64]
   options=loglvl=all dom0_mem=min:1024M dom0_mem=max:4096M iommu=no-igfx ucode=scan efi=attr=uc
   ~~~
5. Go back to `tty6` (Ctrl-Alt-F6) and click `Reboot`.
6. Continue with setting up default templates and logging in to Qubes.


Installation freezes before displaying installer / disable EFI runtime services
------------------------------------------------------------------------------

On some early, buggy UEFI implementations, you may need to disable EFI under Qubes completely.
This can sometimes be done by switching to legacy mode in your BIOS/UEFI configuration.
If that's not an option there, or legacy mode does not work either, you can try the following to add `efi=no-rs`.

1. Follow the [steps above](/doc/uefi-troubleshooting/#change-installer-kernel-parameters-in-uefi) to edit the `[qubes-verbose]` section of your installer's `xen.cfg`.
   You want to modify the `efi=attr=uc` setting and comment out the `mapbs` and `noexitboot` lines.
   The end result should look like this:
   ~~~
   [qubes-verbose]
   options=console=vga efi=no-rs
   # noexitboot=1
   # mapbs=1
   kernel=vmlinuz inst.stage2=hd:LABEL=Qubes-R4.0-x86_64 i915.alpha_support=1
   ramdisk=initrd.img
   ~~~
2. Boot the installer and continue to install as normal, until towards the end when you will receive a warning about being unable to create the EFI boot entry.
   Click continue, but don't reboot the system at the end when prompted.
3. Go to `tty2` (Ctrl-Alt-F2).
4. Use your preferred text editor (`nano` works) to edit `/mnt/sysimage/boot/efi/EFI/qubes/xen.cfg`, adding the `efi=no-rs` option to the end of the `options=` line.
   For example:
   ~~~
   [4.14.18-1.pvops.qubes.x86_64]
   options=loglvl=all dom0_mem=min:1024M dom0_mem=max:4096M iommu=no-igfx ucode=scan efi=no-rs
   ~~~
5. Execute the following commands:
   ~~~
   cp -R /mnt/sysimage/boot/efi/EFI/qubes /mnt/sysimage/boot/efi/EFI/BOOT
   mv /mnt/sysimage/boot/efi/EFI/BOOT/xen.efi /mnt/sysimage/boot/efi/EFI/BOOT/BOOTX64.efi
   mv /mnt/sysimage/boot/efi/EFI/BOOT/xen.cfg /mnt/sysimage/boot/efi/EFI/BOOT/BOOTX64.cfg
   ~~~
6. Go back to `tty6` (Ctrl-Alt-F6) and click `Reboot`.
7. Continue with setting up default templates and logging in to Qubes.

Whenever there is a kernel or Xen update for Qubes, you will need to follow these [other steps above](/doc/uefi-troubleshooting/#boot-device-not-recognized-after-installing) because your system is using the fallback UEFI bootloader in `[...]/EFI/BOOT` instead of directly booting to the Qubes entry under `[...]/EFI/qubes`.

Accessing installer Rescue mode on UEFI
---------------------------------------

In UEFI mode installer do not have boot menu, but starts directly the installation wizard. To get into Rescue mode, you need to switch to tty2 (Ctrl+Alt+F2) and then execute:

~~~
pkill -9 anaconda
anaconda --rescue
~~~
