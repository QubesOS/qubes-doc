---
layout: doc
title: Apple MacBook Troubleshooting
redirect_to: https://github.com/Qubes-Community/Contents/blob/master/docs/troubleshooting/macbook-troubleshooting.md
redirect_from:
- /doc/macbook-troubleshooting/
---

# Apple MacBook Troubleshooting

## System freezes after attaching Broadcom BCM43602 Wi-Fi card

You may experience system freezes or crashes after attaching a Broadcom Wi-Fi adapter to the sys-net VM. This issue has been reported to exist on both Qubes 3.2 and 4.0. 

### Qubes 3.2

To fix this issue on Qubes 3.2:

1. During VM setup, force a reboot and press `OPTION` key.

2. You will reach the grub shell
   ~~~
   configfile /EFI/qubes/grub.cfg
   ~~~

3. Press Fn+F10 to boot without XEN support.

4. Once booted, press Fn+CTRL+ALT+F4 to open a shell.

5. Log into the system
   ~~~
   sudo su -
   systemctl disable qubes-netvm
   ~~~

6. Press Fn+F2 and complete the setup.
7. Reboot Qubes.
8. DO NOT launch the sys-net qube.
Rather, open its setting and remove the Wi-Fi adapter from the Selected devices using the Qubes Manager. 
You can also remove it from the command line, if you know the BDF of the adapter. 
You can see the list of devices attached to sys-net and their associated BDFs by running:
    ~~~
    qvm-pci -l sys-net
    ~~~
For a device with a BDF of `04:00.0`, you can remove it with:
    ~~~
    qvm-pci -d sys-net 04:00.0
    ~~~
9. In a dom0 terminal, run:
    ~~~
    sudo su -
    xl pci-assignable-list
    echo 04:00.0 > /sys/bus/pci/drivers/pciback/permissive
    qvm-start sys-net
    xl pci-attach sys-net DEVICE_BDF
    ~~~
Be sure to replace "DEVICE_BDF" with the actual BDF of the Wi-Fi adapter. 

After following the above steps, you should be able to launch sys-net with Wi-Fi access. These steps can be automated in a custom `systemd` service.

### Qubes 4.0

For Qubes 4.0, you may have to remove the wireless card from sys-net or replace it, as described in the [PCI Troubleshooting](/doc/pci-troubleshooting/#broadcom-bcm43602-wi-fi-card-causes-system-freeze) guide. 

It is a bit tricky to execute, but you may be able to successfully attach a Broadcom BCM43602 to sys-net by executing the `attach` command immediately after starting sys-net. Follow these steps:

1. Disable "Start qube automatically on boot" for sys-net and sys-firewall in the Qubes Manager.
2. Manually start sys-net using the `qvm-start sys-net` command. 
3. Immediately (About 2 seconds later) after stating sys-net, attach the device to sys-net using permissive mode:
`sudo xl pci-attach sys-net 'DEVICE_BDF,permissive=1`
Replace `DEVICE_BDF,` with the BDF of your wireless card. If you can immediately attach the device to sys-net while it is still starting up, it could work. If it is attached too late, the VM doesn't seem to detect it. 

You can use the following script to do the above steps quickly after each boot:

~~~
#!/bin/bash
qvm-start sys-net &
sleep 3
sudo xl pci-attach sys-net '03:00.0,permissive=1'
~~~

## Broadcom BCM4360 doesn't work in a Fedora-based qube

Several people have been unable use the Broadcom BCM4360 Wireless card on a Fedora-based qube. This issue appears to be [related to Fedora](https://ask.fedoraproject.org/t/cant-connect-to-wifi-after-update-bcm4360-with-broadcom-wl-driver/482?page=2), not Qubes. 

To get internet access in sys-net, try shutting down all your VMs, then changing sys-net to use the Debian 10 template. Finally, install the [broadcom-sta-dkms](https://pkgs.org/download/broadcom-sta-dkms) package. 

## Boot freezes at "Setting up networking"

After installing Qubes 3.2 on a MacBook Air 13" mid-2011 (MacBookAir 4,2), it may freeze at "Setting up networking" during booting. This issue is caused by the Broadcom Wireless adapter, if you have one.

To fix the problem, you need to [remove the Wi-Fi card from your Mac][bluetooth-replacement] or put the Wi-Fi adapter into PCI passthrough, as explained below:

1. Run in a terminal:
    ~~~
    # diskutil list
    (find your usb device)
    # bless –device /dev/diskX –legacy –setBoot –nextonly  # bless the disk not the partition
    # reboot
    ~~~

2. Insert your Qubes 3.2 USB flash drive. The ISOLINUX boot screen should come up.
Select Troubleshooting and Boot the Rescue image. Enter your disk password when
prompted. Select continue and after mounting the HD filesystem and launching a
shell, `chroot` as instructed.

3. Find your Wi-Fi card:
    ~~~
    # lspci
    ...
    02:00.0 Network controller: Broadcom Corporation BCM43224 802.11a/b/g/n (rev 01)
    ~~~
In the above example, the device has a BDF of `02:00.0`. 
To assign this device to the sys-net VM:
    ~~~
    # qvm-pci -a sys-net 02:00.0
    ~~~

4. Create `/etc/systemd/system/qubes-pre-netvm.service` with:
    ~~~
    [Unit]
    Description=Netvm fix for Broadcom
    Before=qubes-netvm.service
    
    [Service]
    ExecStart=/bin/sh -c 'echo 02:00.0 > /sys/bus/pci/drivers/pciback/permissive'
    Type=oneshot
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target
    ~~~

5. To enable the `qubes-pre-netvm` services, run:

    ~~~
    systemctl enable qubes-pre-netvm.service
    ~~~

6. After reboot, boot Mac OS X again by running in a terminal:

    ~~~
    # diskutil list
    (find the HD device where you installed Qubes)
    # bless –device /dev/diskX –legacy –setBoot  # bless the disk not the partition
    # reboot
    ~~~

## Can't boot the installer

You can install Qubes 3.2 on a MacBook Pro Retina, 15 inch, Mid-2015 (MacBookPro 11,5) using BIOS or UEFI (If one method fails, try the other):
*  BIOS/CSM/Legacy
*  UEFI plain: Here, the grub menu appears, but any gives a quick flash and returns the main menu. Then, you can boot it manually and fix the `grub.cfg` file by adding the commands `linuexefi` and `initrdefi` and pointing to the proper files in `/efi/boot`. After boot, you may end up with no root file system.
*  UEFI, using rEFInd: This method may prove successful, but there are some issues to be fixed manually after the installation is complete.
   1. Download [rEFInd] refind-bin-0.10.4.zip. Note that this file is not signed, so decide if you trust it or not. The SHA1 sum is 3d69c23b7d338419e5559a93cd6ae3ec66323b1e 
   2. Unzip it and run the installer, which installs rEFInd on the internal SSD
   3. If installation fails due to SIP, reboot in recovery mode, open a terminal and run the command:
   ~~~
   csrutil disable
   ~~~
   4. Reboot. You will see some icons.
   5. Choose Boot EFI\BOOT\xen.efi from ANACONDA. After a while, the graphical installer is up (keyboard and touchpad working)

## Can't boot using GRUB2

After installing Qubes 3.2 on a MacBook Mid-2015, you may be unable to boot using `EFI/qubes/xen.efi` because the [XEN bootloader configuration is broken](/doc/macbook-troubleshooting/#cant-boot-using-xen-bootloader).
You can't also boot using GRUB2 without XEN support because the GRUB configuration is broken as well. 

To start fixing this issue manually, switch to the console by pressing Fn+CTRL+ALT+F2.

It can be very useful – during troubleshooting – to have a rescue system at hand. It could help you boot Qubes, even without XEN support. This troubleshoot assumes you are performing a [UEFI boot, using rEFInd](/doc/macbook-troubleshooting/#cant-boot-the-installer).

At this point, the GRUB configuration file is using some wrong commands, which are not compatible with grub2-efi

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
and also reload config file and change it manually before booting
~~~
configfile /EFI/qubes/grub.cfg
~~~
Then press "e", edit `grub.cfg` and boot by pressing Fn+F10.


## Can't boot using XEN bootloader

You may be unable to boot Qubes 3.2 using `EFI/qubes/xen.efi` on a MacBook Mid-2015 because the XEN bootloader configuration is broken. This issue is accompanied by the GRUB2 configuration being broken as well. After [fixing the GRUB configuration](/doc/macbook-troubleshooting/#cant-boot-using-grub2), follow the following steps to fix the bootloader. This troubleshoot assumes you are performing a [UEFI boot, using rEFInd](/doc/macbook-troubleshooting/#cant-boot-the-installer).

*  Fix grub2 configuration, which uses wrong command for EFI boot
*  Analyzing `/mnt/sysimage/var/log/anaconda/program.log`, you may find the faulty commands issued by the Anaconda installer.
    ~~~
    chrooot /mnt/sysimage
    ~~~
* Edit the `/boot/efi/EFI/qubes/xen.cfg` file to add the following content:
    ~~~
    [global]
    default=4.4.14-11.pvops.qubes.x868_64

    [4.4.14-11.pvops.qubes.x868_64]
    options=loglvl=all dom0_mem=min:1024M dom0_mem=max:4096M
    kernel=vmlinuz-4.4.14-11.pvops.qubes.x86_64
    ramdisk=initramfs-4.4.14-11.pvops.qubes.x86_64.img
    ~~~

*  The main mistake is that `efibootmgr` needs the right commands. Just in case, reapply all the commands, adapting them to your own disk layout (`-d /dev/sdxxx -p partition_number`)

~~~
grep Running /mnt/sysimage/var/log/anaconda/program.log | tail -n 20
efibootmgr -b 0000 -B
efibootmgr -c -w -L Qubes -d /dev/sda -p 4 -l \\EFI\\qubes\\xen-4.6.1.efi
/usr/libexec/mactel-boot-setup
kernel-install add 4.4.14-11.pvops.qubes.x86_64 /boot/vmlinuz-4.4.14-11.pvops.qubes.x86_64
systemctl disable qubes-netvm
reboot
~~~

At the rEFInd screen, choose Boot EFI/qubes/xen-4.6.1.efi.
Everything should now be ok, Qubes OS boots using EFI and you will get the last setup screen.
Select "Qubes OS", do not change anything and click on "Done".
VMs are created, including NetVM.

## System freezes often for 20 seconds

Using Qubes 3.2 on the MacBook Mid-2015 was reported to have frequent freezes, which lasts for 20 seconds. Upon looking at the `journalctl` output, you may see that pulseaudio locks the CPU for 20 seconds, very often.

To fix this issue, kill audio support with this quick workaround:
1. Open a dom0 terminal as root 
2. Edit `/etc/pulse/client.conf` and add `autospawn = no`
3. As normal user, kill pulseaudio with the command `pulseaudio --kill`


[bluetooth-replacement]: https://www.ifixit.com/Guide/MacBook+Air+13-Inch+Mid+2011+AirPort-Bluetooth+Card+Replacement/6360
[rEFInd]: http://www.rodsbooks.com/refind/getting.html
