---
layout: doc
title: Apple MacBook Troubleshooting
permalink: /doc/macbook/
---

Apple MacBook Troubleshooting
=============================

MacBook Air 13" mid 2011 (MacBookAir 4,2)
-----------------------------------------

In this section, I explain how to install Qubes on a MacBook Air 13" mid 2011
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

I first tried to install Qubes using the UEFI boot, but it failed. Not wanting
to waste too much time, I quickly opted for the legacy BIOS install.

### 1. Boot from Mac OS X (or Internet Recovery Image with `CMD`+`R` during bootup)

Run in a terminal [[1]]:

~~~
# diskutil list
(find your usb device)
# bless –device /dev/diskX –legacy –setBoot –nextonly  # bless the disk not the partition
# reboot
~~~

Insert your Qubes 3.2 USB flash drive. The ISOLINUX boot screen should come up.
Install Qubes normally.

If you try to boot Qubes now, it will freeze while  "setting up networking." You
need to put the Broadcom wireless device into PCI passtrough [[2],[3]]. Or, as
an alternative [remove it from your Mac][bluetooth-replacement] and Qubes will
boot up smoothly. If you choose to remove the card, jump to step 3.

### 2. Boot from Mac OS X again

Run in a terminal:

~~~
# diskutil list
(find your usb device)
# bless –device /dev/diskX –legacy –setBoot –nextonly  # bless the disk not the partition
# reboot
~~~

Insert your Qubes 3.2 USB flash drive. The ISOLINUX boot screen should come up.
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

Then create `/etc/systemd/system/qubes-pre-netvm.service` with:

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

Run:

~~~
systemctl enable qubes-pre-netvm.service
~~~

And that's it.

### 3. After reboot, boot Mac OS X again

Run in a terminal:

~~~
# diskutil list
(find the HD device where you installed Qubes)
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
  with tails Linux, more tests are required)

### References

1. <https://github.com/QubesOS/qubes-issues/issues/794>
2. <https://github.com/QubesOS/qubes-issues/issues/1261>
3. <https://www.qubes-os.org/doc/assigning-devices/>


[1]: https://github.com/QubesOS/qubes-issues/issues/794
[2]: https://github.com/QubesOS/qubes-issues/issues/1261
[3]: https://www.qubes-os.org/doc/assigning-devices/
[bluetooth-replacement]: https://www.ifixit.com/Guide/MacBook+Air+13-Inch+Mid+2011+AirPort-Bluetooth+Card+Replacement/6360

