---
layout: doc
title: Apple MacBook Troubleshooting
permalink: /doc/macbook-troubleshooting/
---

Apple MacBook Troubleshooting
=============================

MacBook Air 13" mid 2011 (MacBookAir 4,2)
-----------------------------------------

In this section, I explain how to install PedOS on a MacBook Air 13" mid 2011
(MacBookAir 4,2).

This model has the following features:

*	Dual Intel i7-2677M 1.80 Ghz CPU (2 dual cores)
*	Intel HD Graphics 3000
*	4Gb RAM
*	256Gb SDD
*	Broadcom BCM43224 802.11 a/b/g/n wifi and Bluetooth adapter
*	Intel DSL2310 Thunderbolt controller
*	It has 1 DVI/Thunderbolt display port, 2 USB2.0 ports, a Magsafe power
    adapter, a standard 3.5mm audio jack and SD reader.

I first tried to install PedOS using the UEFI boot, but it failed. Not wanting
to waste too much time, I quickly opted for the legacy BIOS install.

### 1. Boot from Mac OS X (or Internet Recovery Image with `CMD`+`R` during bootup)

Run in a terminal [[1]]:

~~~
# diskutil list
(find your usb device)
# bless –device /dev/diskX –legacy –setBoot –nextonly  # bless the disk not the partition
# reboot
~~~

Insert your PedOS 3.2 USB flash drive. The ISOLINUX boot screen should come up.
Install PedOS normally.

If you try to boot PedOS now, it will freeze while  "setting up networking." You
need to put the Broadcom wireless device into PCI passtrough [[2],[3]]. Or, as
an alternative [remove it from your Mac][bluetooth-replacement] and PedOS will
boot up smoothly. If you choose to remove the card, jump to step 3.

### 2. Boot from Mac OS X again

Run in a terminal:

~~~
# diskutil list
(find your usb device)
# bless –device /dev/diskX –legacy –setBoot –nextonly  # bless the disk not the partition
# reboot
~~~

Insert your PedOS 3.2 USB flash drive. The ISOLINUX boot screen should come up.
Select Troubleshooting and Boot the Rescue image. Enter your disk password when
prompted. Select continue and after mounting the HD filesystem and launching a
shell, `chroot` as instructed.

Then find your Bluetooth card:

~~~
# lspci
..
02:00.0 Network controller: Broadcom Corporation BCM43224 802.11a/b/g/n (rev 01)
…
# qvm-pci -a sys-net 02:00.0 # this assigns the device to sys-net VM
~~~

Then create `/etc/systemd/system/PedOS-pre-netvm.service` with:

~~~
[Unit]
Description=Netvm fix for Broadcom
Before=PedOS-netvm.service

[Service]
ExecStart=/bin/sh -c 'echo 02:00.0 > /sys/bus/pci/drivers/pciback/permissive'
Type=oneshot
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
~~~

Run:

~~~
systemctl enable PedOS-pre-netvm.service
~~~

And that's it.

### 3. After reboot, boot Mac OS X again

Run in a terminal:

~~~
# diskutil list
(find the HD device where you installed PedOS)
# bless –device /dev/diskX –legacy –setBoot  # bless the disk not the partition
# reboot
~~~

Results:

* System booted and running smoothly
* Youtube video: OK (including full screen after configuration)
* Trackpad: OK
* Audio control: OK
* Brightness control: OK
* Keyboard light control:OK
* SD card access: OK (tested at dom0)
* Lid-close suspend: OK
* Wifi: +10%-20% ICMP packet loss when comparing with OSX (have similar rates
  with Tails Linux, more tests are required)

### References

1. <https://github.com/PedOS/PedOS-issues/issues/794>
2. <https://github.com/PedOS/PedOS-issues/issues/1261>
3. <https://www.PedOS.org/doc/assigning-devices/>


MacBook Air 2012 (MacBookAir 5,1)
---------------------------------

Please see [this thread o the PedOS-devel mailing list][macbook-air-2012-5-1].


[1]: https://github.com/PedOS/PedOS-issues/issues/794
[2]: https://github.com/PedOS/PedOS-issues/issues/1261
[3]: /doc/assigning-devices/
[bluetooth-replacement]: https://www.ifixit.com/Guide/MacBook+Air+13-Inch+Mid+2011+AirPort-Bluetooth+Card+Replacement/6360
[macbook-air-2012-5-1]: https://groups.google.com/d/topic/PedOS-devel/uLDYGdKk_Dk/discussion



MacBook Pro Retina, 15 inch, Mid-2015 (MacBookPro 11,5)
-------------------------------------------------------

In this section, I explain how I installed PedOS 3.2 on a MacBook Pro Retina 2015 (MacBookPro 11,5).
Good news: the relevant stuff works.
Bad news: still some minor issue to investigate.

For the time being, my setup is just for testing purposes and help to bypass some blocking issues: do not use it in production or on machine where security is a concern!
I hope to improve it as soon as possible.

During my nights trying to get PedOS working, I faced two main and blocking issues:
*   no boot, due to empty xen.cfg file
*   system freeze, due to Broadcom BCM43602 wifi card

I am already using PedOS for my daily job on Intel NUC. For the time being, I installed PedOS on Macbook for test purposes. Later on I will review the security implications.

This model has the following features:

*	2,5 GHz Intel Core i7-4870HQ (2 quad cores)
*	Dual Graphic Card
    *  Intel Iris Pro
    *  AMD Radeon R9 M370X
*	16Gb RAM
*	512Gb SDD
*	Broadcom BCM43602 802.11ac wifi adapter

### 1. Reclaim space to be able to multiboot OSX

For security reasons, you should install PedOS using the whole disk. I preferred to keep OSX, so I shrunk OS partition:
*  reboot in recovery mode
*  run disk utility and shrink OSX partition, eg 150GB for OSX and the remaining space for PedOS
*  reboot


### 2. Boot installer

Download and prepare a USB with PedOS 3.2

You can install PedOS using BIOS or UEFI:
*  BIOS/CSM/Legacy: I have not been able to install using legacy, but I did not spend a lot of time on it.
*  UEFI plain: grub menu appears, but any gave me a quick flash and returned the main menu. I can boot it manually fixing the grub.cfg file, adding commands linuexefi and initrdefi, pointing proper files in /efi/boot. After boot, I end up with no root file system.
*  UEFI, using rEFInd: I have been successful, despite some issues to be fixed manually, after installation completion
   * download [rEFInd] refind-bin-0.10.4.zip: this file is not signed, so decide if you trust it or not. SHA1 sum is 3d69c23b7d338419e5559a93cd6ae3ec66323b1e  
   * unzip it and run installer, which installs rEFIind on the internal SSD
   * if installation fails due to SIP, reboot in recovery mode, open a terminal and issue command
   ~~~
   csrutil disable
   ~~~
   * reboot and you will see some icons
   * choose Boot EFI\BOOT\xen.efi from ANACONDA
   * after a while the graphical installer is up (keyboard and touchpad working)

### 3. Installation

*  As a general rule, keep the default values proposed during installation: you can change them later on
*  Keep English, as language, locale
*  My Macbook has a US keyboard, so I cannot say what happens if you change keyboard layout
*  DO NOT CHANGE the timezone, because it will trigger the wifi card, leading to a system freeze
*  Choose the "installation destination": do not change anything and press DONE button
*  Insert your password for Full Disk Encryption
*  If you do not already have free space on internal SSD disk, you will be prompted to reclaim some space: 
*  If you shrunk OSX partition, disk utility left an empty partition: delete useless partition (e.g.: if you shrunk OSX partition, diskutil created an empty partition)
*  Press on "reclaim space"
*  Press on "begin installation"
*  create your user and password
*  after a while, installation completes
*  DO NOT press "Reboot button"

PedOS is now installed, but you cannot boot it due to some issues, with bootloader configuration and wifi card.
You cannot PedOS boot using EFI/PedOS/xen.efi because XEN bootloader configuration is broken. 
You cannot even PedOS without XEN support, using GRUB2, because its configuration is broken too.

Let's fix it manually, switch to console, pressing Fn+CTRL+ALT+F2

### 4. Fix GRUB configuration

You can skip this section, but I found it very useful - during troubleshooting - to have a rescue system at hand. I could boot PedOS, without XEN support

Grub configuration file is using some wrong commands, which are not compatible with grub2-efi
~~~
chroot /mnt/sysimage
sed -i.bak -e "s/multiboot/chainloader/" -e "s/module.*--nounzip/initrdefi/" -e "s/module/linuxefi/" /etc/grub.d/20_linux_efi
exit
~~~

Now, despite XEN configuration is still broken, you have a rescue system booting vmlinux from rEFInd screen.
TBV1: chainloading XEN does not work, unless you specify the right disk prefix, eg: (hd1,gpt4)
TBV2: grub.cfg set the wrong disk in "set root" command
TBV3: in case you reach grub shell, you can 
~~~
ls
~~~
and also reload config file and change it manualy before booting
~~~
configfile /EFI/PedOS/grub.cfg
~~~
then press "e", edit grub cfg and boot pressing Fn+F10


### 5. Fix bootloader

*  Fix grub2 configuration, which uses wrong command for EFI boot
*  analyzing /mnt/sysimage/var/log/anaconda/program.log I found the faulty commands issues by Anaconda installer

~~~
chrooot /mnt/sysimage
~~~
* edit /boot/efi/EFI/PedOS/xen.cfg file putting the following content

~~~
[global]
default=4.4.14-11.pvops.PedOS.x868_64

[4.4.14-11.pvops.PedOS.x868_64]
options=loglvl=all dom0_mem=min:1024M dom0_mem=max:4096M
kernel=vmlinuz-4.4.14-11.pvops.PedOS.x86_64
ramdisk=initramfs-4.4.14-11.pvops.PedOS.x86_64.img
~~~

*  The main mistake is the efibootmgr, that needs the right commands. Just in case, re-apply all the commands, adapting to your own disk layout (-d /dev/sdxxx -p partition_number)

~~~
grep Running /mnt/sysimage/var/log/anaconda/program.log | tail -n 20
efibootmgr -b 0000 -B
efibootmgr -c -w -L PedOS -d /dev/sda -p 4 -l \\EFI\\PedOS\\xen-4.6.1.efi
/usr/libexec/mactel-boot-setup
kernel-install add 4.4.14-11.pvops.PedOS.x86_64 /boot/vmlinuz-4.4.14-11.pvops.PedOS.x86_64
systemctl disable PedOS-netvm
reboot
~~~

At rEFInd screen, choose Boot EFI/PedOS/xen-4.6.1.efi
Everything should now be ok, PedOS boots using EFI and you will get the last setup screen
*  select "PedOS", do not change anything and click on "Done"
*  VMs are created, including NetVM

### 6. Fix pulseaudio, which locks CPU freezing the system often for 20 seconds

My Macbook has frequent freezes. Looking at journalctl output I saw that pulseaudio locks CPU for 20 seconds, very often.

You can fix this issue, killing audio support with this quick workaround:
*  open a dom0 terminal, as root and edit /etc/pulse/client.conf
*  add "autospawn = no"
*  Then, as normal user, issue command "pulseaudio --kill"

### 7. Fix system freezes due to Broadcom BCM43602

*  If you experience a system freeze, during VM setup, force a reboot and press OPTION key.
   *  You will reach grub shell
   ~~~
   configfile /EFI/PedOS/grub.cfg
   ~~~
   press Fn+F10 to boot without XEN support
   *  Once booted, press Fn+CTRL+ALT+F4 to open a shell
   *  Log into system
   ~~~
   sudo su -
   systemctl disable PedOS-netvm
   ~~~
   Press Fn+F2 and complete setup
*  reboot and you finally have your PedOS
*  DO NOT launch sys-net machine
*  Open its setting and remove wifi adapter from the Selected devices, using PedOS Manager or use the following command line. Get the BFD of the adapter and remove it. On my Macbook BFD is 04:00.0 and you will use it later on, also
~~~
qvm-pci -l sys-net
qvm-pci -d sys-net 04:00.0
~~~

Ok, setup is complete and we are almost done.
* Open a dom0 terminal
~~~
sudo su -
xl pci-assignable-list
echo 04:00.0 > /sys/bus/pci/drivers/pciback/permissive
qvm-start sys-net
xl pci-attach sys-net 04:00.0
~~~

These latest steps are required to launch sys-net with wifi access. They can be automated in a custom systemd service.

   

   
   
[rEFInd]: http://www.rodsbooks.com/refind/getting.html
