---
layout: doc
title: Installation Troubleshooting
permalink: /doc/installation-troubleshooting/
---
# Installation Troubleshooting #

## "An unknown error has occurred" error during installation ##

Some people have encountered this error message when trying to install Qubes on drives that already have data on them. 
The solution is to exit the installer, wipe all data or delete all partitions, then restart the Qubes installation. 

## Trouble installing from USB stick ##

If you are facing issues when booting using UEFI mode, see the [UEFI troubleshooting guide](/doc/uefi-troubleshooting/). 

There are a variety of other problems that could arise when using a USB installation medium, and some of the issues can be fixed by doing one or more of the following:

* **Use a different USB drive:** 
If possible, try several drives of different sizes and formats. 
This determines whether the problem stems from the flash drive or Qubes installer.
Some laptops cannot read from an external boot device larger than 8GB. 
If you encounter a black screen when performing an installation from a USB stick, ensure you are using a USB drive less than 8GB, or a partition on that USB less than 8GB and of format FAT32.
Note that the Qubes installation image is over 4GB, so it may not fit on a smaller USB. 
If a machine can not boot from a bigger USB, it may be too old to run Qubes. 
* **Verify your Qubes ISO:** 
Errors will occur if the Qubes installer is corrupted. 
Ensure that the installer is correct and complete before writing it to a flash drive by [verifying the ISO](/security/verifying-signatures/#how-to-verify-qubes-iso-signatures). 
* **Change the method you used to [write your ISO to a USB key](/doc/installation-guide/#copying-the-iso-onto-the-installation-medium):** 
Some people use the ``dd`` command (recommended), others use tools like Rufus, balenaEtcher or the GNOME Disk Utility. 
If installation fails after using one tool, try a different one. 
For example, if you are facing trouble installing Qubes after writing the ISO using Rufus, then try using other tools like balenaEtcher or the ``dd`` command. 
In case the boot partition is not set to "active" after copying the ISO, you can use some other tool like `gparted` on a Linux system to activate it. 

## Boot screen does not appear / system does not detect your installation medium ##

If the boot screen does not appear, there are several options to troubleshoot.
First, try rebooting your computer. 
If it still loads your currently installed operating system or does not detect your installation medium, make sure the boot order is set up appropriately. 

The process to change the boot order varies depending on the currently installed system and the motherboard manufacturer. 

If **Windows 10** is installed on your machine, you may need to follow specific instructions to change the boot order. 
This may require an [advanced reboot](https://support.microsoft.com/en-us/help/4026206/windows-10-find-safe-mode-and-other-startup-settings).

## "Not asking for VNC because we don't have a network" / "X startup failed, aborting installation" / "Pane is dead" error during installation ##

The boot mode in use may be causing these error messages. 
Try to install after enabling both UEFI and legacy boot modes. 
If that doesn't help, then disable one and try the other. 
Visit the [UEFI Troubleshooting guide](/doc/uefi-troubleshooting/) if other errors arise during UEFI booting. 

These errors may also occur due to an incompatible Nvidia graphics card. If you have one, follow the following instructions:
1. Disable secure/fast boot and use legacy mode
2. Enter GRUB, move the selection to the first choice, and then press the Tab key. 
3. Now, you are in edit mode. Move the text cursor with your arrow key and after ``kernel=`` line, add:

       nouveau.modeset=0 rd.driver.blacklist=nouveau video=vesa:off
   
   If the above code doesn't fix the problem, replace it with:
   
       noexitboot=1 modprobe.blacklist=nouveau rd.driver.blacklist=nouveau --- intitrd.img

For more information, look at the [Nvidia Troubleshooting guide](https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/nvidia-troubleshooting.md#disabling-nouveau).
 

## Installation freezes at "Setting up Networking" ##
 
If you are facing this problem on an Apple computer, check out the [Macbook Troubleshooting guide](https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/macbook-troubleshooting.md).

This issue occurs due to the network card, which may be missing some drivers or is incompatible with Qubes. 

First, install all available drivers for the card. 
You can install the drivers without internet access by first downloading them on another machine, then transferring them over to the current machine (e.g., with a USB drive). 

If installing the available drivers does not help, disable the network card in the BIOS and perform the installation before re-enabling the card. 
If this solves the issue, it confirms the PCI card is incompatible with Qubes. 
In this case, you may want to consider replacing it with a network card of a different brand. 
Broadcom cards are notoriously problematic with Qubes.
 


