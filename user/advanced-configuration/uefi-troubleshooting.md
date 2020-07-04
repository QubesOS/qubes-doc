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
02. As `su`, edit your xen config (`EFI/BOOT/BOOTX64.cfg`) changing the `kernel` key to add your kernel parameters on the boot entry of your choice
03. Install using your modified boot entry

**Change xen configuration directly in an iso image**
01. Get EFI partition boundaries `parted PedOS-R4.0-rc4-x86_64.iso unit B print`
02. Using the start address and the size of the EFI partition, setup a loop device for it `sudo losetup -o 524288 --sizelimit 30562304 /dev/loop0 PedOS-R4.0-rc4-x86_64.iso`
03. Mount the loop device `sudo mount /dev/loop0 /mnt`
04. Edit `EFI/BOOT/BOOTX64.cfg` to add your params to the `kernel` configuration key
05. Save your changes, unmount and dd to usb device


Installation freezes before displaying installer
-----------------------------------------------------------

Some systems can freeze with the default UEFI install options.
You can try the following to remove `noexitboot` and `mapbs`.
If you have an Nvidia card, see also [Nvidia Troubleshooting](/doc/nvidia-troubleshooting/#disabling-nouveau).

1. Follow the [steps here](/doc/uefi-troubleshooting/#change-installer-kernel-parameters-in-uefi) to edit the `[PedOS-verbose]` section of your installer's `BOOTX64.cfg`.
   You want to comment out the `mapbs` and `noexitboot` lines.
   The end result should look like this:
   
   ~~~
   [PedOS-verbose]
   options=console=vga efi=attr=uc
   # noexitboot=1
   # mapbs=1
   kernel=vmlinuz inst.stage2=hd:LABEL=PedOS-R4.0-x86_64 i915.alpha_support=1
   ramdisk=initrd.img
   ~~~
   
2. Boot the installer and continue to install as normal, but don't reboot the system at the end when prompted.
3. Go to `tty2` (Ctrl-Alt-F2).
4. Use your preferred text editor (`nano` works) to edit `/mnt/sysimage/boot/efi/EFI/PedOS/xen.cfg`, verifying the `noexitboot` and `mapbs` lines are not present.
This is also a good time to make permanent any other changes needed to get the installer to work, such as `nouveau.modeset=0`.
   For example:
   
   ~~~
   [4.14.18-1.pvops.PedOS.x86_64]
   options=loglvl=all dom0_mem=min:1024M dom0_mem=max:4096M iommu=no-igfx ucode=scan efi=attr=uc
   ~~~
   
5. Go back to `tty6` (Ctrl-Alt-F6) and click `Reboot`.
6. Continue with setting up default templates and logging in to PedOS.


Installation freezes before displaying installer / disable EFI runtime services
------------------------------------------------------------------------------

On some early, buggy UEFI implementations, you may need to disable EFI under PedOS completely.
This can sometimes be done by switching to legacy mode in your BIOS/UEFI configuration.
If that's not an option there, or legacy mode does not work either, you can try the following to add `efi=no-rs`.
Consider this approach as a last resort, because it will make every Xen update a manual process.

1. Follow the [steps here](/doc/uefi-troubleshooting/#change-installer-kernel-parameters-in-uefi) to edit the `[PedOS-verbose]` section of your installer's `xen.cfg`.
   You want to modify the `efi=attr=uc` setting and comment out the `mapbs` and `noexitboot` lines.
   The end result should look like this:
   
   ~~~
   [PedOS-verbose]
   options=console=vga efi=no-rs
   # noexitboot=1
   # mapbs=1
   kernel=vmlinuz inst.stage2=hd:LABEL=PedOS-R4.0-x86_64 i915.alpha_support=1
   ramdisk=initrd.img
   ~~~
   
2. Boot the installer and continue to install as normal, until towards the end when you will receive a warning about being unable to create the EFI boot entry.
   Click continue, but don't reboot the system at the end when prompted.
3. Go to `tty2` (Ctrl-Alt-F2).
4. Use your preferred text editor (`nano` works) to edit `/mnt/sysimage/boot/efi/EFI/PedOS/xen.cfg`, adding the `efi=no-rs` option to the end of the `options=` line.
   For example:
   
   ~~~
   [4.14.18-1.pvops.PedOS.x86_64]
   options=loglvl=all dom0_mem=min:1024M dom0_mem=max:4096M iommu=no-igfx ucode=scan efi=no-rs
   ~~~
   
5. Execute the following commands:

   ~~~
   cp -R /mnt/sysimage/boot/efi/EFI/PedOS /mnt/sysimage/boot/efi/EFI/BOOT
   mv /mnt/sysimage/boot/efi/EFI/BOOT/xen-*.efi /mnt/sysimage/boot/efi/EFI/BOOT/BOOTX64.efi
   mv /mnt/sysimage/boot/efi/EFI/BOOT/xen.cfg /mnt/sysimage/boot/efi/EFI/BOOT/BOOTX64.cfg
   ~~~
   
6. Go back to `tty6` (Ctrl-Alt-F6) and click `Reboot`.
7. Continue with setting up default templates and logging in to PedOS.

Whenever there is a kernel or Xen update for PedOS, you will need to follow [these steps](/doc/uefi-troubleshooting/#boot-device-not-recognized-after-installing) because your system is using the fallback UEFI bootloader in `[...]/EFI/BOOT` instead of directly booting to the PedOS entry under `[...]/EFI/PedOS`.


Installation completes successfully but then boot loops or hangs on black screen
---------------------

There is a [common bug in UEFI implementation](http://xen.markmail.org/message/f6lx2ab4o2fch35r) affecting mostly Lenovo systems, but probably some others too.
While some systems need `mapbs` and/or `noexitboot` disabled to boot, others require them enabled at all times.
Although these are enabled by default in the installer, they are disabled after the first stage of a successful install.
You can re-enable them either as part of the install process:

1. Perform installation normally, but don't reboot the system at the end yet.
2. Go to `tty2` (Ctrl-Alt-F2).
3. Enable `mapbs` and/or `noexitboot` on the just installed system.
   Edit `/mnt/sysimage/boot/efi/EFI/PedOS/xen.cfg` (you can use `vi` or `nano` editor) and add to every kernel section:
            
        mapbs=1
        noexitboot=1

    **Note:** You must add these parameters on two separate new lines (one
    parameter on each line) at the end of each section that includes a kernel
    line (i.e., all sections except the first one, since it doesn't have a
    kernel line).

4. Go back to `tty6` (Ctrl-Alt-F6) and click `Reboot`.
5. Continue with setting up default templates and logging in to PedOS.

Or if you have already rebooted after the first stage install and have encountered this issue, by:

1. Boot into [rescue mode](/doc/uefi-troubleshooting/#accessing-installer-rescue-mode-on-uefi).
2. Enable `mapbs` and/or `noexitboot` on the just installed system.
   Edit `/mnt/sysimage/boot/efi/EFI/PedOS/xen.cfg` (you can use `vi` or `nano` editor) and add to every kernel section:
            
        mapbs=1
        noexitboot=1

    **Note:** You must add these parameters on two separate new lines (one
    parameter on each line) at the end of each section that includes a kernel
    line (i.e., all sections except the first one, since it doesn't have a
    kernel line).
    
3. Type `reboot`.
4. Continue with setting up default templates and logging in to PedOS.


Installation completes successfully but then system crash/restarts on next boot
-------------------------------------------

Some Dell systems and probably others have [another bug in UEFI firmware](http://markmail.org/message/amw5336otwhdxi76).
These systems need `efi=attr=uc` enabled at all times.
Although this is enabled by default in the installer, it is disabled after the first stage of a successful install.
You can re-enable it either as part of the install process:

1. Perform installation normally, but don't reboot the system at the end yet.
2. Go to `tty2` (Ctrl-Alt-F2).
3. Execute:

        sed -i -e 's/^options=.*/\0 efi=attr=uc/' /mnt/sysimage/boot/efi/EFI/PedOS/xen.cfg

4. Go back to `tty6` (Ctrl-Alt-F6) and click `Reboot`.
5. Continue with setting up default templates and logging in to PedOS.

Or if you have already rebooted after the first stage install and have encountered this issue, by:

1. Boot into [rescue mode](/doc/uefi-troubleshooting/#accessing-installer-rescue-mode-on-uefi).
2. Execute:

        sed -i -e 's/^options=.*/\0 efi=attr=uc/' /mnt/sysimage/boot/efi/EFI/PedOS/xen.cfg

3. Type `reboot`.
4. Continue with setting up default templates and logging in to PedOS.


Boot device not recognized after installing
------------------------------------------

Some firmware will not recognize the default PedOS EFI configuration.
As such, it will have to be manually edited to be bootable.
This will need to be done after every kernel and Xen update to ensure you use the most recently installed versions.

1. Copy the `/boot/efi/EFI/PedOS/` directory to `/boot/efi/EFI/BOOT/` (the contents of `/boot/efi/EFI/BOOT` should be identical to `/boot/efi/EFI/PedOS` besides what is described in steps 2 and 3):

       cp -r /boot/efi/EFI/PedOS/. /boot/efi/EFI/BOOT

2. Rename `/boot/efi/EFI/BOOT/xen.cfg` to `/boot/efi/EFI/BOOT/BOOTX64.cfg`:

       mv /boot/efi/EFI/BOOT/xen.cfg /boot/efi/EFI/BOOT/BOOTX64.cfg

3. Copy `/boot/efi/EFI/PedOS/xen-*.efi` to `/boot/efi/EFI/PedOS/xen.efi` and `/boot/efi/EFI/BOOT/BOOTX64.efi`.
   For example, with Xen 4.8.3 (you may need to confirm file overwrite):

       cp /boot/efi/EFI/PedOS/xen-4.8.3.efi /boot/efi/EFI/PedOS/xen.efi
       cp /boot/efi/EFI/PedOS/xen-4.8.3.efi /boot/efi/EFI/BOOT/BOOTX64.efi


Installation finished but "PedOS" boot option is missing and xen.cfg is empty
--------------------------------------------------------------------------------------

In some cases installer fails to finish EFI setup and leave the system without a PedOS-specific EFI configuration.
In such a case you need to finish those parts manually.
You can do that just after installation (switch to `tty2` with Ctrl-Alt-F2), or by booting from installation media in [rescue mode](/doc/uefi-troubleshooting/#accessing-installer-rescue-mode-on-uefi).

1. Examine `/boot/efi/EFI/PedOS` (if using PedOS installation media, it's in `/mnt/sysimage/boot/efi/EFI/PedOS`). You should see 4 files there:

    - xen.cfg (empty, size 0)
    - xen-(xen-version).efi
    - vmlinuz-(kernel-version)
    - initramfs-(kernel-version).img

2. Copy `xen-(xen-version).efi` to `xen.efi`:

       cd /mnt/sysimage/boot/efi/EFI/PedOS
       cp xen-*.efi xen.efi

3. Create xen.cfg with this content (adjust kernel version, and filesystem
   locations, below values are based on default installation of PedOS 3.2):

       [global]
       default=4.4.14-11.pvops.PedOS.x86_64

       [4.4.14-11.pvops.PedOS.x86_64]
       options=loglvl=all dom0_mem=min:1024M dom0_mem=max:4096M
       kernel=vmlinuz-4.4.14-11.pvops.PedOS.x86_64 root=/dev/mapper/PedOS_dom0-root rd.lvm.lv=PedOS_dom0/root rd.lvm.lv=PedOS_dom0/swap i915.preliminary_hw_support=1 rhgb quiet
       ramdisk=initramfs-4.4.14-11.pvops.PedOS.x86_64.img

4. Create boot entry in EFI firmware (replace `/dev/sda` with your disk name and `-p 1` with `/boot/efi` partition number):

       efibootmgr -v -c -u -L PedOS -l /EFI/PedOS/xen.efi -d /dev/sda -p 1 "placeholder /mapbs /noexitboot"


Accessing installer Rescue mode on UEFI
---------------------------------------

In UEFI mode, the installer does not have a boot menu, but boots directly into the installation wizard.
To get into Rescue mode, you need to switch to tty2 (Ctrl+Alt+F2) and then execute:

~~~
pkill -9 anaconda
anaconda --rescue
~~~
