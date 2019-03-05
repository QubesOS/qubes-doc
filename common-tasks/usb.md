---
layout: doc
title: Using and Managing USB Devices in R3.2
permalink: /doc/usb/
redirect_from:
- /doc/stick-mounting/
- /en/doc/stick-mounting/
- /doc/StickMounting/
- /wiki/StickMounting/
- /doc/external-device-mount-point/
- /en/doc/external-device-mount-point/
- /doc/ExternalDeviceMountPoint/
- /wiki/ExternalDeviceMountPoint/
- /doc/usbvm/
- /en/doc/usbvm/
- /doc/USBVM/
- /wiki/USBVM/
- /doc/sys-usb/
---

Using and Managing USB Devices in R3.2
======================================
(In case you were looking for the [R4.0 documentation](/doc/usb-devices/).)

How to attach USB drives
------------------------

(**Note:** In the present context, the term "USB drive" denotes any [USB mass storage device][mass-storage].
In addition to smaller flash memory sticks, this includes things like USB external hard drives.)

Qubes OS supports the ability to attach a USB drive (or just one or more of its partitions) to any qube easily, no matter which qube actually handles the USB controller.

USB drive mounting is integrated into the Qubes VM Manager GUI.
Simply insert your USB drive, right-click on the desired qube in the Qubes VM Manager list, click **Attach/detach block devices**, and select your desired action and device.
However, this only works for the whole device.
If you would like to attach individual partitions, you must use the command-line tool.

Note that attaching individual partitions can be slightly more secure because it doesn't force the target AppVM to parse the partition table.
However, it often means the AppVM won't detect the new partition and you will need to manually mount it inside the AppVM.
See below for more detailed steps.
    
The command-line tool you may use to mount whole USB drives or their partitions is `qvm-block`.
This tool can be used to assign a USB drive to a qube as follows:

 1. Insert your USB drive.

 2. In a dom0 console (running as a normal user), list all available block devices:

        qvm-block

    This will list all available block devices connected to any USB controller in your system, no matter which qube hosts the controller.
    The name of the qube hosting the USB controller is displayed before the colon in the device name.
    The string after the colon is the name of the device used within the qube, like so:

        dom0:sdb1     Cruzer () 4GiB
        
        usbVM:sdb1    Disk () 2GiB

    **Note:** If your device is not listed here, you may refresh the list by calling from the qube to which the device is connected (typically `sys-usb`):

        sudo udevadm trigger --action=change

 3.  Assuming your USB drive is attached to `sys-usb` and is `sdb`, we attach the device to a qube with the name `personal` like so:

         qvm-block -a personal sys-usb:sdb

     This will attach the device to the qube as `/dev/xvdi` if that name is not already taken by another attached device, or `/dev/xvdj`, etc.

     You may also mount one partition at a time by using the same command with the partition number after `sdb`.
     This is slightly more secure because it does not force the target AppVM to parse the partition table.

     **Warning:** when working with single partitions, it is possible to assign the same partition to multiple qubes.
     For example, you could attach `sdb1` to qube1 and then `sdb` to qube2.
     It is up to the user not to make this mistake.
     The Xen block device framework currently does not provide an easy way around this.
     Point 2 of [this comment on issue 1072][1072-comm2] gives details about this.

 4.  The USB drive is now attached to the qube.
     If using a default qube, you may open the Nautilus file manager in the qube, and your drive should be visible in the **Devices** panel on the left.
     If you've attached a single partition, you may need to manually mount before it becomes visible:
     ```
     cd ~
     mkdir mnt
     sudo mount /dev/xvdi mnt
     ```
   
 5.  When you finish using your USB drive, click the eject button or right-click and select **Unmount**.
     If you've manually mounted a single partition in the above step, use:
     `sudo umount mnt`

 6.  In a dom0 console, detach the stick

         qvm-block -d <device>
         
     or
     
         qvm-block -d <vmname>

 7.  You may now remove the device.

**Warning:** Do not remove the device before detaching it from the VM!
Otherwise, you will not be able to attach it anywhere later.
See issue [1082] for details.

If the device does not appear in Nautilus, you will need to mount it manually.
The device will show up as `/dev/xvdi` (or `/dev/xvdj` if there is already one device attached -- if two, `/dev/xvdk`, and so on).


### What if I removed the device before detaching it from the VM?###

Currently (until issue [1082] gets implemented), if you remove the device before detaching it from the qube, Qubes OS (more precisely, `libvirtd`) will think that the device is still attached to the qube and will not allow attaching further devices under the same name.
The easiest way to recover from such a situation is to reboot the qube to which the device was attached.
If this isn't an option, you can manually recover from the situation by following these steps:

 1. Physically connect the device back.
    You can use any device as long as it will be detected under the same name (for example, `sdb`).

 2. Attach the device manually to the same VM using the `xl block-attach` command.
    It is important to use the same "frontend" device name (by default, `xvdi`).
    You can get it from the `qvm-block` listing:

        [user@dom0 ~]$ qvm-block
        sys-usb:sda DataTraveler_2.0 () 246 MiB (attached to 'testvm' as 'xvdi')
        [user@dom0 ~]$ sudo xl block-attach testvm phy:/dev/sda backend=sys-usb xvdi

    In above example, all `xl block-attach` parameters can be deduced from the output of `qvm-block`.
    In order:

    * `testvm` - name of target qube to which device was attached - listed in brackets by `qvm-block` command
    * `phy:/dev/sda` - physical path at which device appears in source qube (just after source qube name in `qvm-block` output)
    * `backend=sys-usb` - name of source qube, can be omitted in the case of dom0
    * `xvdi` - "frontend" device name (listed at the end of line in `qvm-block` output)

 3. Now properly detach the device, either using Qubes VM Manager or the `qvm-block -d` command.


Attaching a single USB device to a qube (USB passthrough)
---------------------------------------------------------

Starting with Qubes 3.2, it is possible to attach a single USB device to any Qube.
While this is a useful feature, it should be used with care, because there are [many security implications][usb-challenges] from using USB devices and USB passthrough will **expose your target qube** to most of them.
If possible, use a method specific for particular device type (for example, block devices described above), instead of this generic one.

### Installation of qubes-usb-proxy ###
[installation]: #installation-of-qubes-usb-proxy

Note, you cannot pass through devices from dom0 (in other words: a USB VM is required).

To use this feature, you need to have the [`qubes-usb-proxy`][qubes-usb-proxy] package installed in the template used for the USB qube and in the qube to which you want to connect USB devices. ( If the qube is TemplateBased then it should be installed in the relevant template as usual. )
If you do not have the package installed you will see this error: `ERROR: qubes-usb-proxy not installed in the VM`.

`qubes-usb-proxy` should be installed by default in the standard Fedora and Debian templates.

You install the `qubes-usb-proxy` package using the package manager as usual.

- Fedora: `sudo dnf install qubes-usb-proxy`
- Debian/Ubuntu: `sudo apt-get install qubes-usb-proxy`

### Usage of qubes-usb-proxy ###

Listing available USB devices:

    [user@dom0 ~]$ qvm-usb
    sys-usb:2-4     04ca:300d 04ca_300d
    sys-usb:2-5     058f:3822 058f_USB_2.0_Camera
    sys-usb:2-1     03f0:0641 PixArt_HP_X1200_USB_Optical_Mouse

Attaching selected USB device:

    [user@dom0 ~]$ qvm-usb -a conferences sys-usb:2-5
    [user@dom0 ~]$ qvm-usb
    conferences:2-1 058f:3822 058f_USB_2.0_Camera
    sys-usb:2-4     04ca:300d 04ca_300d
    sys-usb:2-5     058f:3822 058f_USB_2.0_Camera (attached to conferences)
    sys-usb:2-1     03f0:0641 PixArt_HP_X1200_USB_Optical_Mouse

Now, you can use your USB device (camera in this case) in the `conferences` qube.
If you see the error `ERROR: qubes-usb-proxy not installed in the VM` instead, please refer to the [Installation Section][installation].

When you finish, detach the device:

    [user@dom0 ~]$ qvm-usb -d sys-usb:2-5
    [user@dom0 ~]$ qvm-usb
    sys-usb:2-4     04ca:300d 04ca_300d
    sys-usb:2-5     058f:3822 058f_USB_2.0_Camera
    sys-usb:2-1     03f0:0641 PixArt_HP_X1200_USB_Optical_Mouse

This feature is not available in Qubes Manager.

Additional Reading:
-------------------

 - [Creating a USB qube]
 - [Using a USB keyboard]

[mass-storage]: https://en.wikipedia.org/wiki/USB_mass_storage_device_class
[1072-comm2]: https://github.com/QubesOS/qubes-issues/issues/1072#issuecomment-124119309
[1082]: https://github.com/QubesOS/qubes-issues/issues/1082
[usb-challenges]: https://blog.invisiblethings.org/2011/05/31/usb-security-challenges.html
[YubiKey]: /doc/YubiKey/
[Creating a USB qube]: /doc/usb-qube-howto/
[Using a USB keyboard]: /doc/usb-qube-howto/#enable-a-usb-keyboard-for-login
[qubes-usb-proxy]: https://github.com/QubesOS/qubes-app-linux-usb-proxy
