---
layout: doc
title: Using and Managing USB Devices
permalink: /doc/usb/
redirect_from:
- /doc/stick-mounting/
- /en/doc/stick-mounting/
- /doc/StickMounting/
- /wiki/StickMounting/
- /doc/usbvm/
- /en/doc/usbvm/
- /doc/USBVM/
- /wiki/USBVM/
- /doc/sys-usb/
---

Using and Managing USB Devices
==============================

How to attach USB drives
------------------------

(**Note:** In the present context, the term "USB drive" denotes any
[USB mass storage device][mass-storage]. In addition to smaller flash memory
sticks, this includes things like USB external hard drives.)

Qubes OS supports the ability to attach a USB drive (or just one or more of its
partitions) to any qube easily, no matter which qube actually handles the USB
controller. (The USB controller may be assigned on the **Devices** tab of a
qube's settings page in Qubes VM Manager or by using the
[qvm-pci][Assigning Devices] command. For guidance on finding the correct USB
controller, see [here][usb-controller].)

USB drive mounting is integrated into the Qubes VM Manager GUI. Simply insert
your USB drive, right-click on the desired qube in the Qubes VM Manager list,
click **Attach/detach block devices**, and select your desired action and
device. This, however, only works for the whole device. If you would like to
attach individual partitions, you must use the command-line tool.

The command-line tool you may use to mount whole USB drives or their partitions
is `qvm-block`. This tool can be used to assign a USB drive to a qube as
follows:

 1. Insert your USB drive.

 2. In a dom0 console (running as a normal user), list all available block
   devices:

        qvm-block -l

    This will list all available block devices connected to any USB controller
    in your system, no matter which qube hosts the controller. The name of the
    qube hosting the USB controller is displayed before the colon in the device
    name. The string after the colon is the name of the device used within the
    qube, like so:

        dom0:sdb1     Cruzer () 4GiB
        
        usbVM:sdb1    Disk () 2GiB

    **Note:** If your device is not listed here, you may refresh the list by
    calling (from the qube to which the device is connected):

        sudo udevadm trigger --action=change

 3.  Assuming your USB drive is attached to dom0 and is `sdb`, we attach the
     device to a qube like so:

        qvm-block -a personal dom0:sdb

     This will attach the device to the qube as `/dev/xvdi` if that name is not
     already taken by another attached device, or `/dev/xvdj`, etc.

     You may also mount one partition at a time by using the same command with
     the partition number after `sdb`.

     **Warning:** when working with single partitions, it is possible to assign
     the same partition to multiple qubes. For example, you could attach `sdb1`
     to qube1 and then `sdb` to qube2. It is up to the user not to make this
     mistake. The Xen block device framework currently does not provide an easy
     way around this. Point 2 of [this comment on issue 1072][1072-comm2] gives
     details about this.

 4.  The USB drive is now attached to the qube. If using a default qube, you may
     open the Nautilus file manager in the qube, and your drive should be
     visible in the **Devices** panel on the left.

 5.  When you finish using your USB drive, click the eject button or right-click
     and select **Unmount**.

 6.  In a dom0 console, detach the stick:

        qvm-block -d <device> <vmname>

 7.  You may now remove the device.

**Warning:** Do not remove the device before detaching it from the VM!
Otherwise, you will not be able to attach it anywhere later. See issue [1082]
for details.

There have been reports that when attaching a single partition, the Nautilus
file manager would not see it and automatically mount it (see issue [623]).
This problem seems to be resolved (see [this comment on issue 1072][1072-comm1]).

If, however, the device does not appear in Nautilus, you will need to mount it
manually. The device will show up as `/dev/xvdi` (or `/dev/xvdj` if there is
already one device attached -- if two, `/dev/xvdk`, and so on).


### What if I removed the device before detaching it from the VM? ###

Currently (until issue [1082] gets implemented), if you remove the device
before detaching it from the qube, Qubes OS (more precisely, `libvirtd`) will
think that the device is still attached to the qube and will not allow attaching
further devices under the same name. The easiest way to recover from such a
situation is to reboot the qube to which the device was attached, but if this
isn't an option, you can manually recover from the situation by following these
steps:

 1. Physically connect the device back. You can use any device as long as it
    will be detected under the same name (for example, `sdb`).

 2. Attach the device manually to the same VM using the `xl block-attach`
    command. It is important to use the same "frontend" device name (by default,
    `xvdi`). You can get it from the `qvm-block` listing:

        [user@dom0 ~]$ qvm-block
        sys-usb:sda DataTraveler_2.0 () 246 MiB (attached to 'testvm' as 'xvdi')
        [user@dom0 ~]$ xl block-attach testvm phy:/dev/sda backend=sys-usb xvdi

    In above example, all `xl block-attach` parameters can be deduced from the
    output of `qvm-block`. In order:

    * `testvm` - name of target qube to which device was attached - listed in
      brackets by `qvm-block` command
    * `phy:/dev/sda` - physical path at which device appears in source qube
      (just after source qube name in `qvm-block` output)
    * `backend=sys-usb` - name of source qube, can be omitted in case of dom0
    * `xvdi` - "frontend" device name (listed at the end of line in `qvm-block`
      output)

 3. Now properly detach the device, either using Qubes VM Manager or the
    `qvm-block -d` command.


Creating and Using a USB qube
-----------------------------

The connection of an untrusted USB device to dom0 is a security risk since dom0,
like almost every OS, reads partition tables automatically and since the whole
USB stack is put to work to parse the data presented by the USB device in order
to determine if it is a USB mass storage device, to read its configuration, etc.
This happens even if the drive is then assigned and mounted in another qube.

To avoid this risk, it is possible to prepare and utilize a USB qube. However,
Xen does not yet provide working PVUSB functionality, so only USB mass storage
devices can be passed to individual qubes.

For this reason, you may wish to avoid using a USB qube if you do not have a USB
controller free of input devices and programmable devices, although Qubes R3.1 
introduced support for USB mice and keyboards (see below).

A USB qube acts as a secure handler for potentially malicious USB devices,
preventing them from coming into contact with dom0 (which could otherwise be
fatal to the security of the whole system). With a USB qube, every time you
connect an untrusted USB drive to a USB port managed by that USB controller, you
will have to attach it to the qube in which you wish to use it (if different
from the USB qube itself), either by using Qubes VM Manager or the command line
(see instructions above). Again, this works only for USB mass storage devices.
Other devices cannot currently be virtualized.

You can create a USB qube using the management stack by performing the following
steps as root in dom0:

 1. Enable `sys-usb`:

        qubesctl top.enable qvm.sys-usb

 2. Apply the configuration:

        qubesctl state.highstate

Alternatively, you can create a USB qube manually as follows:

 1.  Read the [Assigning Devices] page to learn how to list and identify your
     USB controllers. Carefully check whether you have a USB controller that
     would be appropriate to assign to a USB qube. Note that it should be free
     of input devices, programmable devices, and any other devices that must be
     directly available to dom0. If you find a free controller, note its name
     and proceed to step 2.
 2.  Create a new qube. Give it an appropriate name and color label
     (recommended: `sys-usb`, red). If you need to attach a networking device,
     it might make sense to create a NetVM. If not, an AppVM might make more
     sense. (The default `sys-usb` is a NetVM.)
 3.  In the qube's settings, go to the "Devices" tab. Find the USB controller
     that you identified in step 1 in the "Available" list. Move it to the
     "Selected" list.

     **Caution:** By assigning a USB controller to a USB qube, it will no longer
     be available to dom0. This can make your system unusable if, for example,
     you have only one USB controller, and you are running Qubes off of a USB
     drive.

 4.  Click "OK." Restart the qube.
 5.  Recommended: Check the box on the "Basic" tab which says "Start VM
     automatically on boot." (This will help to mitigate attacks in which
     someone forces your system to reboot, then plugs in a malicious USB
     device.)

If the USB qube will not start, see [here][faq-usbvm].


Supported USB device types
--------------------------

As of Qubes R3.1, it is possible to attach:

 * USB mice
 * USB keyboards (see below)
 * USB block devices (such as USB mass storage devices)
   * When attaching one of these, you should get a notification about the
     new device, then you should be able to attach it to a qube in Qubes VM
     Manager.

Other devices, such as USB webcams, will also work, but they will be
accessible only from the USB qube itself, as explained above.


How to use a USB keyboard
-------------------------

In order to use a USB keyboard, you must first attach it to a USB qube, then
give that qube permission to pass keyboard input to dom0. Note that allowing
keyboard access from a USB qube gives it great power. In short:

 * It will see whatever you type on that keyboard (including passwords).
 * It will be able to inject keystrokes, which basically means that it will be
   able to enter any command. For example, if some malware catches your
   screenlocker password, it will be able to unlock the screen when you are not
   present. (For more details, see [here][input-proxy].)

If you are sure you wish to proceed, then you must edit the
`qubes.InputKeyboard` policy file in dom0, which is located here:

    /etc/qubes-rpc/policy/qubes.InputKeyboard

Add a line like this one to the top of the file:

    sys-usb dom0 ask

(Change `sys-usb` to your desired USB qube.)

You can now use your USB keyboard.

Attaching a single USB device to a qube (USB passthrough)
------------------------------------------------

Stating with Qubes 3.2, it is possible to attach a single USB device to any
Qube. While this is useful feature, it should be used with care, because there
are [many security implications][usb-challenges] from using USB devices and USB
passthrough will **expose your target qube** for most of them. If possible, use use
method specific for particular device type (for example block devices described
above), instead of this generic one.

To use this feature, you need to install `qubes-usb-proxy` package in the
templates used for USB qube and qubes you want to connect USB devices to.

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

Now, you can use your USB device (camera in this case) in `conferences` qube.

When you finish, detach the device:

    [user@dom0 ~]$ qvm-usb -d sys-usb:2-5
    [user@dom0 ~]$ qvm-usb
    sys-usb:2-4     04ca:300d 04ca_300d
    sys-usb:2-5     058f:3822 058f_USB_2.0_Camera
    sys-usb:2-1     03f0:0641 PixArt_HP_X1200_USB_Optical_Mouse

This feature is not yet available in Qubes Manager.


[mass-storage]: https://en.wikipedia.org/wiki/USB_mass_storage_device_class
[Assigning Devices]: /doc/assigning-devices/
[usb-controller]: /doc/assigning-devices/#finding-the-right-usb-controller
[623]: https://github.com/QubesOS/qubes-issues/issues/623
[1072-comm1]: https://github.com/QubesOS/qubes-issues/issues/1072#issuecomment-124270051
[1072-comm2]: https://github.com/QubesOS/qubes-issues/issues/1072#issuecomment-124119309
[1082]: https://github.com/QubesOS/qubes-issues/issues/1082
[faq-usbvm]: /doc/user-faq/#i-created-a-usbvm-and-assigned-usb-controllers-to-it-now-the-usbvm-wont-boot
[1618]: https://github.com/QubesOS/qubes-issues/issues/1618
[input-proxy]: https://github.com/qubesos/qubes-app-linux-input-proxy
[usb-challenges]: http://blog.invisiblethings.org/2011/05/31/usb-security-challenges.html
