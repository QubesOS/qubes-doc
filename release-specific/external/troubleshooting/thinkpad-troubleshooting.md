---
layout: doc
title: Lenovo ThinkPad Troubleshooting
permalink: /doc/thinkpad-troubleshooting/
redirect_from:
- /doc/thinkpad_x201/
- /en/doc/thinkpad_x201/
- /doc/Thinkpad_X201/
- /wiki/Thinkpad_X201/
- /doc/lenovo450-tinkering/
- /en/doc/lenovo450-tinkering/
- /doc/Lenovo450Tinkering/
- /wiki/Lenovo450Tinkering/
---

# Lenovo ThinkPad Troubleshooting #

## Instructions to create USB installation medium for newer (UEFI-only) ThinkPads ##
Newer ThinkPads (e.g. T470, T470p, ThinkPad 25) are likely to fail installation attempts made from a USB stick that was created with dd or Rufus, and even from a DVD burned using official ISO images - if the ThinkPad is configured for UEFI boot. If you don't want to use Legacy Mode as a workaround, the following instructions should help you create a Qubes Installation USB stick that works in UEFI-only mode.

In a nutshell, you need to use the Fedora livecd-tools to make a Qubes Installation USB Stick from the Qubes ISO image, then update the label on the partition of that USB stick to "BOOT", and then update the BOOT/EFI/xen.cfg file on the USB stick so that all labels point to BOOT. In more detail:

1. On your ThinkPad, enter the UEFI setup (press F1 at startup) and make sure to set at least the following options:
   - *USB UEFI BIOS Support: Enabled*
   - *UEFI/Legacy Boot: UEFI Only*
   - *Secure Boot: Disabled*
2. On a different computer, create a "Fedora Live USB Stick": Download a current Fedora Live CD image, and put it onto a USB stick (e.g. using dd or Rufus). Start your ThinkPad from the Fedora Live USB Stick on your ThinkPad (Press F12 at startup to select boot device). Of course, you can alternatively start a different machine from the Fedora Live USB Stick, or use an existing Fedora installation. The next steps all occur within Fedora:
3. Install livecd-tools: `# dnf install livecd-tools`
4. Download the desired Qubes ISO image (or attach a storage device containing it), and verify the signatures as described in the Qubes installation guide. For these instructions, I assume the ISO image is at */run/media/liveuser/qsrc/Qubes-R4.0-rc3-x86_64.iso* (so whenever you see that path going forward in these instructions, replace it with whatever your own path is)
5. Within Fedora, attach the USB stick that you would like to turn into your Qubes Installation USB Stick. Use `dmesg` to figure out what the device name of that stick is. For these instructions, I assume it's */dev/sdd* (so whenever you see */dev/sdd* going forward in these instructions, replace it with whatever your actual device name is)
6. Make sure your target USB stick (presumed to be /dev/sdd) has no mounted partitions: ``# umount /dev/sdd*`` (the asterisk at the end makes sure to unmount all partitions if more than one exists). If none are mounted you'll get an error that you can ignore.
7. Use livecd-tools to copy the image: ``# livecd-iso-to-disk --format --efi /run/media/liveuser/qsrc/Qubes-R4.0-rc3-x86_64.iso /dev/sdd``. **This will erase everything on the drive. Make sure you specify the correct destination.** Then press ENTER when prompted to proceed. This process will take quite a while, be patient.
8. When imaging is complete, change the partition label to BOOT: ``# dosfslabel /dev/sdd1 BOOT``
9. Now create a mount point and mount the partition:

   ``# mkdir /mnt/qinst``

   ``# mount /dev/sdd1 /mnt/qinst/``

10. Use your favorite editor to edit the file */mnt/qinst/EFI/BOOT/xen.cfg*: Replace all instances of ``LABEL=Qubes-R4.0-rc3-x86_64`` with ``LABEL=BOOT``. There is typically no space in front of ``LABEL``, but there is a space at the end of the portion you replace.
11. Unmount the Qubes Installation USB stick: ``# umount /dev/sdd*`` and disconnect it.

That's it! You can now reboot the machine with the Qubes USB Installation stick attached, and press F12 to select it as the boot device at startup. Proceed to install Qubes OS normally. Enjoy!

## ThinkPads with Intel HD 3000 graphics ##

Several ThinkPad models have Intel HD 3000 graphics, including the T420s and the
T520. Some users with these laptops have experienced random reboots, which were
solved by adding `i915.enable_rc6=0` as a kernel parameter to
`GRUB_CMDLINE_LINUX` in the file `/etc/default/grub` in dom0.


## Instructions for getting your Lenovo Thinkpad X201 & X200 laptop working with Qubes/Linux ##

For being able to boot the installer from USB, you have to disable VT-d in the BIOS.
Enter the BIOS by hitting F1, go to Config - CPU and then disable VT-d there.

After the installation, you have to set a startup-parameter for Xen, to be able to activate VT-d again:

1. Open a terminal in dom0
2. Edit `/etc/default/grub`
3. Add to the line `GRUB_CMDLINE_XEN_DEFAULT` the setting `iommu=no-igfx`, save and quit
4. sudo `grub2-mkconfig --output /boot/grub2/grub.cfg`

Then reboot, enter BIOS and re-enable VT-d.

### Getting scrolling with the Trackpoint and the Middle Button to work ###

1. Create a script with the following content:

   ~~~
   #!/bin/sh
   xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation" 1
   xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation Button" 2
   xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation Timeout" 200
   xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation Axes" 6 7 4 5
   ~~~

2. Add the script to the startup-items of your desktop environment.


## Instructions for getting your Lenovo 450 laptop working with Qubes/Linux ##

Lenovo 450 uses UEFI, so some settings are needed to get Qubes (or Fedora) to boot, otherwise Qubes install USB stick will reboot right after boot selector screen and not continue install.

### Setting UEFI options to get Qubes install to boot ###

1.  Enable Legacy USB mode
2.  Disable all Secure Boot and UEFI options, but leave this enabled: Config / USB / USB UEFI BIOS SUPPORT
3.  Save settings and reboot
5.  Install Qubes

... and now enjoy :) These settings may be needed also in other UEFI computers.

