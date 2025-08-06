---
lang: en
layout: doc
permalink: /doc/uefi-troubleshooting/
ref: 177
title: UEFI troubleshooting
---

## Successfully installed in legacy mode, but had to change some xen parameters

**Note**: If you make changes, you must boot from "Partition 1" explicitly from UEFI boot menu.

**Change the xen configuration on a USB media**

1. Attach the usb disk, mount the EFI partition (second partition available on the disk)
2. Open a terminal and enter the command `sudo su -`. Use your preferred text editor (e.g `vi`) to edit your xen config (`EFI/BOOT/grub.cfg`):

    ```
    vi EFI/BOOT/grub.cfg
    ```

3. Change the `multiboot2 /images/pxeboot/xen.gz` line to add your xen parameters on the boot entry of your choice
4. Install using your modified boot entry

**Change xen configuration directly in an iso image**

1. Set up a loop device (replacing `X` with your ISO's version name): `losetup -P /dev/loop0 Qubes-RX-x86_64.iso`
2. Mount the loop device: `sudo mount /dev/loop0p2 /mnt`
3. Edit `EFI/BOOT/grub.cfg` to add your params to the `multiboot2 /images/pxeboot/xen.gz` line
4. Save your changes, unmount and dd to usb device

## Installation freezes before displaying installer

If you have an Nvidia card, see also [Nvidia Troubleshooting](https://forum.qubes-os.org/t/19021#disabling-nouveau).


## Installation from USB stick hangs on black screen

Some laptops cannot read from an external boot device larger than 8GB. If you encounter a black screen when performing an installation from a USB stick, ensure you are using a USB drive less than 8GB, or a partition on that USB lesser than 8GB and of format FAT32.

## Installation completes successfully but then system crash/restarts on next boot

Some Dell systems and probably others have [another bug in UEFI firmware](https://web.archive.org/web/20170901231026/https://markmail.org/message/amw5336otwhdxi76).
These systems need `efi=attr=uc` enabled at all times.
Although this is enabled by default in the installer, it is disabled after the first stage of a successful install.
You can re-enable it either as part of the install process:

1. Perform installation normally, but don't reboot the system at the end yet.
2. Go to `tty2` (Ctrl-Alt-F2).
3. Execute:

    ```
    sed -i -e 's/ucode=scan/\0 efi=attr=uc/' /mnt/sysimage/boot/efi/EFI/qubes/grub.cfg
    ```

4. Go back to `tty6` (Ctrl-Alt-F6) and click `Reboot`.
5. Continue with setting up default templates and logging in to Qubes.

Or if you have already rebooted after the first stage install and have encountered this issue, by:

1. Boot Qubes OS install media into [rescue mode](/doc/uefi-troubleshooting/#accessing-installer-rescue-mode-on-uefi)

2. Press '3' to go to the shell

3. Find and mount the EFI system partition. (replace `/dev/sda` with your disk name. If unsure, use the `lsblk` command to display a list of disks):
    ```
    fdisk -l /dev/sda | grep EFI
    ```
    The output should look like this:
    ```
    /dev/sda1   2048    1230847 1228800 600M EFI System
    ```
    Then mount it:
    ```
    mkdir -p /mnt/sysimage/boot/efi
    mount /dev/sda1 /mnt/sysimage/boot/efi
    ```
4. Execute:

    ```
    sed -i -e 's/ucode=scan/\0 efi=attr=uc/' /mnt/sysimage/boot/efi/EFI/qubes/grub.cfg
    ```

5. Type `reboot`.
6. Continue with setting up default templates and logging in to Qubes.

## Boot device not recognized after installing

Some firmware will not recognize the default Qubes EFI configuration.
As such, it will have to be manually edited to be bootable.

1. Boot Qubes OS install media into [rescue mode](/doc/uefi-troubleshooting/#accessing-installer-rescue-mode-on-uefi)

2. Press '3' to go to the shell

3. Find and mount the EFI system partition. (replace `/dev/sda` with your disk name. If unsure, use the `lsblk` command to display a list of disks):
    ```
    fdisk -l /dev/sda | grep EFI
    ```
    The output should look like this:
    ```
    /dev/sda1   2048    1230847 1228800 600M EFI System
    ```
    Then mount it:
    ```
    mkdir -p /mnt/sysimage/boot/efi
    mount /dev/sda1 /mnt/sysimage/boot/efi
    ```
    
4. Copy `grubx64.efi` to the fallback path:
    
    ```
    cp /mnt/sysimage/boot/efi/EFI/qubes/grubx64.efi /mnt/sysimage/boot/efi/EFI/BOOT/bootx64.efi
    ```
    
5. Type `reboot`

## "Qubes" boot option is missing after removing / attaching a disk or updating the BIOS

1. Boot Qubes OS install media into [rescue mode](/doc/uefi-troubleshooting/#accessing-installer-rescue-mode-on-uefi)

2. Press '3' to go to the shell
3. Create boot entry in EFI firmware (replace `/dev/sda` with your disk name and `-p 1` with `/boot/efi` partition number):

    ```
    efibootmgr -v -c -u -L Qubes -l /EFI/qubes/grubx64.efi -d /dev/sda -p 1 
    ```

## Accessing installer Rescue mode on UEFI

Choose "Rescue a Qubes OS system" from grub2 boot menu.
