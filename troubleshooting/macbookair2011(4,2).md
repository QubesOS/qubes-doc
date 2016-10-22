
After browsing through multiple posts, I finally was able to install Qubes on a MacBook Air 13” mid 2011 (MacBookAir 4,2). I’m just sharing this, so ppl don’t need to read through multiple forums to understand how to do it.

This model is features with:
•	Dual Intel i7-2677M 1.80 Ghz CPU (2 dual cores)
•	Intel HD Graphics 3000 
•	4Gb RAM
•	256Gb SDD
•	Broadcom BCM43224 802.11 a/b/g/n wifi and Bluetooth adapter
•	Intel DSL2310 Thunderbolt controller
•	It has 1 DVI/Thunderbolt display port, 2 USB2.0 ports, a Magsafe power adapter, a standard 3.5mm audio jack and SD reader.

First try to install Qubes using the UEFI boot failed, and not wanting to waste too much time, I quickly opted for the legacy BIOS install.  

1.	Boot from MacOSX (or Internet Recovery Image with CMD+R during bootup).
Run Terminal application as root [1]:
~~~
# diskutil list
(find your usb device)
# bless –device /dev/diskX –legacy –setBoot –nextonly  # bless the disk not the partition
# reboot
~~~

Insert Qubes 3.2 USB flash:
ISOLINUX boot screen should come up.
Install Qubes normaly


If you try to boot Qubes now, it will freeze while  “setting up networking”. You need to put the Broadcom wireless device into PCI passtrough [2,3]. Or, as an alternative remove it from your mac (https://www.ifixit.com/Guide/MacBook+Air+13-Inch+Mid+2011+AirPort-Bluetooth+Card+Replacement/6360) and Qubes will boot up smoothly.
If you choose to remove the card jump to step 3.

2.	Boot from MacOSX, again.
~~~
Run Terminal application as root:
# diskutil list
(find your usb device)
# bless –device /dev/diskX –legacy –setBoot –nextonly  # bless the disk not the partition
# reboot
~~~

Insert Qubes 3.2 USB flash:
ISOLINUX boot screen should come up. 
Select Troubleshooting and Boot the Rescue image; insert disk password when prompted; select continue and after mounting the HD filesystem, launching a shell, chroot as instructed.

Then:
a)	Find your Bluetooth card:
~~~
# lspci
..
02:00.0 Network controller: Broadcom Corporation BCM43224 802.11a/b/g/n (rev 01)
…
# qvm-pci -a sys-net 02:00.0 # this assigns the device to sys-net VM
~~~

then create Create /etc/systemd/system/qubes-pre-netvm.service
with:
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
And that’s it.


3.	After reboot, boot MacOSX, again.
Run Terminal application as root:
~~~
# diskutil list
(find the HD device where you installed Qubes)
# bless –device /dev/diskX –legacy –setBoot  # bless the disk not the partition
# reboot
~~~

Results:
•	System booted and running smoothly. 
•	Youtube video: OK (including full screen after configuration)
•	Trackpad: OK
•	Audio control: OK
•	Brightness control: OK
•	Keyboard light control:OK
•	SD card access: OK (tested at dom0)
•	Lid-close suspend: OK
•	Wifi: +10%-20% ICMP packet loss when comparing with OSX (have similar rates with tails Linux, more tests are required)

References:
[1] https://github.com/QubesOS/qubes-issues/issues/794
[2] https://github.com/QubesOS/qubes-issues/issues/1261
[3] https://www.qubes-os.org/doc/assigning-devices/
