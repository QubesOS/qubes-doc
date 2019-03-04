---
layout: doc
title: USB Devices in Qubes R4.0
permalink: /doc/usb-devices/
redirect_from:
- /doc/usb-devices-in-qubes-R4.0/
---

USB and Storage Devices in Qubes R4.0
=====================================
*This page is part of [device handling in qubes]*
(In case you were looking for the [R3.2 documentation](/doc/usb/).)

Drives And Block Devices
========================
This part describes how to handle drives, referred to as "block device". If you don't know what a block device is, just think of it as a fancy way to say "something that stores data".

#Using The GUI to Attach a Drive
(**Note:** In the present context, the term "USB drive" denotes any [USB mass storage device][mass-storage].
In addition to smaller flash memory sticks, this includes things like USB external hard drives.)

Qubes OS supports the ability to attach a USB drive (or just its partitions) to any qube easily, no matter which qube handles the USB controller.

Attaching USB drives is integrated into the Devices Widget: ![device manager icon]  
Simply insert your USB drive and click on the widget.
You will see multiple entries for your USB drive; typically, `sys-usb:sda`, `sys-usb:sda1`, and `sys-usb:2-1` for example.
Entries starting with a number (e.g. here `2-1`) are the [whole usb-device][USB]. Entries without a number (e.g. here `sda`) are the whole block-device. Other entries are partitions of that block-device (e.r. here `sda1`).

The simplest option is to attach the entire block drive.
In our example, this is `sys-usb:sda`, so hover over it.
This will pop up a submenu showing running VMs to which the USB drive can be connected.
Click on one and your USB drive will be attached!

**Note:** attaching individual partitions (e.g. `sys-usb:sda1`) can be slightly more secure because it doesn't force the target AppVM to parse the partition table.
However, it often means the AppVM won't detect the new partition and you will need to manually mount it inside the AppVM.
See below for more detailed steps.

#Block Devices in VMs
If not specified otherwise, block devices will show up as `/dev/xvdi*` in a linux VM, where `*` may be the partition-number. If a block device isn't automatically mounted after attaching, open a terminal in the VM and execute:

    cd ~
    mkdir mnt
    sudo mount /dev/xvdi2 mnt

where `xvdi2` needs to be replaced with the partition you want to mount.
This will make your drive content accessible under `~/mnt`.

Beware that when you attach a whole block device, partitions can be identified by their trailing integer (i.e. `/dev/xvdi2` for the second partition, `/dev/xvdi` for the whole device), whereas if you attach a single parition, the partition has *no trailing integer*.

If several different block-devices are attached to a single VM, the last letter of the device node name is advanced through the alphabet, so after `xvdi` the next device will be named `xvdj`, the next `xvdk`, and so on.

To specify this device node name, you need to use the command line tool and its [`frontend-dev`-option][frontend-dev].

#Command Line Tool Guide
The command-line tool you may use to mount whole USB drives or their partitions is `qvm-block`, a shortcut for `qvm-device block`.

`qvm-block` won't recognise your device by any given name, but rather the device-node the sourceVM assigns. So make sure you have the drive available in the sourceVM, then list the available block devices (step 1.) to find the corresponding device-node.

In case of a USB-drive, make sure it's attached to your computer. If you don't see anything that looks like your drive, run `sudo udevadm trigger --action=change` in your USB-qube (typically `sys-usb`)

 1. In a dom0 console (running as a normal user), list all available block devices:
    
        qvm-block
    
    This will list all available block devices in your system across all VMs.
    The name of the qube hosting the block device is displayed before the colon in the device ID.
    The string after the colon is the ID of the device used within the qube, like so:

        sourceVM:sdb     Cruzer () 4GiB
        sourceVM:sdb1    Disk () 2GiB

 2. Assuming your block device is attached to `sys-usb` and its device node is `sdb`, we attach the device to a qube with the name `work` like so:
    
        qvm-block attach work sys-usb:sdb
    
    This will attach the device to the qube as `/dev/xvdi` if that name is not already taken by another attached device, or `/dev/xvdj`, etc.
    
    You may also mount one partition at a time by using the same command with the partition number, e.g. `sdb1`.

 3. The block device is now attached to the qube.
    If using a default qube, you may open the Nautilus file manager in the qube, and your drive should be visible in the **Devices** panel on the left.
    If you've attached a single partition (e.g. `sdb2` instead of `sdb` in our example), you may need to manually mount before it becomes visible:
    
        cd ~
        mkdir mnt
        sudo mount /dev/xvdi mnt
    

 4. When you finish using the block device, click the eject button or right-click and select **Unmount**.

    If you've manually mounted a single partition in the above step, use:

        sudo umount mnt

 5. In a dom0 console, detach the device

        qvm-block detach work sys-usb:sdb

 6.  You may now remove the device or attach it to another qube.

#Recovering From Premature Device Destruction
If the you fail to detach the device before it's destroyed in the sourceVM (e.g. by physically detaching the thumbdrive), [there will be problems][premature removal].

To recover from this error state, in dom0 run

    virsh detach-disk targetVM xvdi

(where `targetVM` is to be replaced with the VM name you attached the device to and `xvdi` is to be replaced with the used [frontend device node][frontend-dev].)

However, if the block device originated in dom0, you will have to refer to the [old way][detach dom0 device].

#Attaching a File
To attach a file as block device to another qube, first turn it into a loopback device inside the sourceVM.

 1. In the linux sourceVM run

        sudo losetup -f --show /path/to/file

    [This command][losetup] will create the device node `/dev/loop0` or, if that is already in use, increase the trailing integer until that name is still available. Afterwards it prints the device-node-name it found.

 2. If you want to use the GUI, you're done. Click the Device Manager ![device manager icon] and select the `loop0`-device to attach it to another qube.

    If you rather use the command line, continue:

    In dom0, run `qvm-block` to display known block devices. The newly created loop device should show up:

        ~]$ qvm-block
        BACKEND:DEVID  DESCRIPTION  USED BY
        sourceVM:loop0 /path/to/file

 3. Attach the `loop0`-device using qvm-block as usual:

        qvm-block a targetVM sourceVM:loop0

 4. After detaching, destroy the loop-device inside the sourceVM as follows:

        sudo losetup -d /dev/loop0

#Additional Attach Options
Attaching a block device through the command line offers additional customisation options, specifiable via the `--option`/`-o` option. (Yes, confusing wording, there's an [issue for that](https://github.com/QubesOS/qubes-issues/issues/4530).)

##frontend-dev
This option allows you to specify the name of the device node made available in the targetVM. This defaults to `xvdi` or, if already occupied, the first available device node name in alphabetical order. (The next one tried will be `xvdj`, then `xvdk`, and so on ...)

usage example:

    qvm-block a work sys-usb:sda1 -o frontend-dev=xvdz

This command will attach the partition `sda1` to `work` as `/dev/xvdz`.

##read-only
Attach device in read-only mode. Protects the block device in case you don't trust the targetVM.

If the device is a read-only device, this option is forced true.

usage example:

    qvm-block a work sys-usb:sda1 -o read-only=true

There exists a shortcut to set read-only `true`, `--ro`:

    qvm-block a work sys-usb:sda1 --ro

The two commands are equivalent.

##devtype
Usually, a block device is attached as disk. In case you need to attach a block device as cdrom, this option allows that.

usage example:

    qvm-block a work sys-usb:sda1 -o devtype=cdrom

This option accepts `cdrom` and `disk`, default is `disk`.

Handling other USB Devices
==========================
**Important security warning:** USB passthrough comes with many security implications! Please make sure you carefully read and understood the **[security considerations]**! Especially, whenever possible, attach a [block device] instead!

Examples for valid cases for USB-passthrough:

 - [microcontroller programming]
 - using [external audio devices]
 - [optical drives] for recording

(If you are thinking to use a two-factor-authentication device, [there is an app for that][qubes u2f proxy]. But it has some [issues][4661].)

#Attaching And Detaching a USB Device
##With Qubes Device Manager
Click the device-manager-icon: ![device manager icon]  
A list of available devices appears. USB-devices have a USB-icon to their right: ![usb icon]

Hover on one device to display a list of VMs you may attach it to.

Click one of those. The USB device will be attached to it. You're done.

After you finished using the USB-device, you can detach it the same way by clicking on the Devices Widget.
You will see an entry in bold for your device such as **`sys-usb:2-5 - 058f_USB_2.0_Camera`**.
Hover on the attached device to display a list of running VMs.
The one to which your device is connected will have an eject button ![eject icon] next to it.
Click that and your device will be detached.

##With The Command Line Tool
In dom0, you can use `qvm-usb` from the commandline to attach and detach devices.

Listing available USB devices:

    [user@dom0 ~]$ qvm-usb
    BACKEND:DEVID   DESCRIPTION                    USED BY
    sys-usb:2-4     04ca:300d 04ca_300d
    sys-usb:2-5     058f:3822 058f_USB_2.0_Camera
    sys-usb:2-1     03f0:0641 PixArt_HP_X1200_USB_Optical_Mouse

Attaching selected USB device:

    [user@dom0 ~]$ qvm-usb attach work sys-usb:2-5
    [user@dom0 ~]$ qvm-usb
    BACKEND:DEVID   DESCRIPTION                    USED BY
    sys-usb:2-4     04ca:300d 04ca_300d
    sys-usb:2-5     058f:3822 058f_USB_2.0_Camera  work
    sys-usb:2-1     03f0:0641 PixArt_Optical_Mouse

Now, you can use your USB device (camera in this case) in the `work` qube.
If you see the error `ERROR: qubes-usb-proxy not installed in the VM` instead, please refer to the [Installation Section].

When you finish, detach the device.

    [user@dom0 ~]$ qvm-usb detach work sys-usb:2-5
    [user@dom0 ~]$ qvm-usb
    BACKEND:DEVID   DESCRIPTION                    USED BY
    sys-usb:2-4     04ca:300d 04ca_300d
    sys-usb:2-5     058f:3822 058f_USB_2.0_Camera
    sys-usb:2-1     03f0:0641 PixArt_Optical_Mouse

#Maintenance And Customisation

##Creating And Using a USB qube
If you've selected to install a usb-qube during system installation, everything is already set up for you in `sys-usb`. If you've later decided to create a usb-qube, please follow [this guide][USB-qube howto].

##Installation Of `qubes-usb-proxy`
To use this feature, the[`qubes-usb-proxy`][qubes-usb-proxy] package needs to be installed in the templates used for the USB qube and qubes you want to connect USB devices to.
This section exists for reference or in case something broke and you need to reinstall `qubes-usb-proxy`. Under normal conditions, `qubes-usb-proxy` should already be installed and good to go.

If you receive this error: `ERROR: qubes-usb-proxy not installed in the VM`, you can install the `qubes-usb-proxy` with the package manager in the VM you want to attach the USB device to.
Note: you cannot pass through devices from dom0 (in other words: a [USB qube][USB-qube howto] is required).
`qubes-usb-proxy` should be installed by default in the template VM.

- Fedora: `sudo dnf install qubes-usb-proxy`
- Debian/Ubuntu: `sudo apt-get install qubes-usb-proxy`


##Using USB Keyboards And Other Input Devices
**Warning:** especially keyboards need to be accepted by default when using them to login! Please make sure you carefully read and understood the **[security considerations]** before continuing!

Mouse and keyboard setup are part of [setting up a USB-qube][keyboard setup].


##Finding The Right USB Controller

Some USB devices are not compatible with the USB pass-through method Qubes employs.
In situations like these, you can try to pass through the entire USB controller to a qube as PCI device.
However, with this approach one cannot attach single USB devices but has to attach the whole USB controller with whatever USB devices are connected to it.

If you have multiple USB controllers, you must first figure out which PCI device is the right controller.

First, find out which USB bus the device is connected to (note that these steps need to be run from a terminal inside your USB qube):

    lsusb

For example, I want to attach a broadband modem to the NetVM. 
In the output of `lsusb` it may be listed as something like:

    Bus 003 Device 003: ID 413c:818d Dell Computer Corp.

(In this case, the device isn't fully identified)

The device is connected to USB bus \#3. 
Check which other devices are connected to the same bus, since *all* of them will be attach to the same VM.

To find the right controller, follow the usb bus:

    readlink /sys/bus/usb/devices/usb3


This should output something like:

    ../../../devices/pci-0/pci0000:00/0000:00:1a.0/usb3


Now you see the BDF address in the path (right before final `usb3`).
Strip the leading `0000:` and pass the rest to the [`qvm-pci` tool][qvm-pci] to attach the controller to the targetVM.



[device handling in qubes]: /doc/device-handling/
[block device]: #drives-and-block-devices
[security considerations]: /doc/device-considerations/#usb-security
[usb-challenges]: https://blog.invisiblethings.org/2011/05/31/usb-security-challenges.html
[usb icon]: /attachment/wiki/Devices/generic-usb.png
[microcontroller programming]: https://www.arduino.cc/en/Main/Howto
[external audio devices]: /doc/external-audio/
[optical drives]: /doc/recording-optical-discs/
[qubes u2f proxy]: /doc/u2f-proxy/
[4661]: https://github.com/QubesOS/qubes-issues/issues/4661
[device manager icon]:/attachment/wiki/Devices/media-removable.png
[eject icon]:/attachment/wiki/Devices/media-eject.png
[Installation Section]:#installation-of-qubes-usb-proxy
[USB-qube howto]: /doc/usb-qube-howto/
[keyboard setup]: /doc/usb-qube-howto/#enable-a-usb-keyboard-for-login
[qvm-pci]: /doc/pci-devices-in-qubes-R4.0/

[device handling in qubes]: /doc/device-handling/
[mass-storage]: https://en.wikipedia.org/wiki/USB_mass_storage_device_class
[frontend-dev]: #frontend-dev
[premature removal]: https://github.com/QubesOS/qubes-issues/issues/1082
[detach dom0 device]: /doc/usb/#what-if-i-removed-the-device-before-detaching-it-from-the-vm
[losetup]: https://linux.die.net/man/8/losetup
[USB]:/dock/usb-devices-in-qubes-R4.0/
