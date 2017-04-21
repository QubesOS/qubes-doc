---
layout: doc
title: Using and Managing USB Devices
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

Using and Managing USB Devices
==============================

Creating and Using a USB qube
-----------------------------

The connection of an untrusted USB device to dom0 is a security risk since dom0,
like almost every OS, reads partition tables automatically and since the whole
USB stack is put to work to parse the data presented by the USB device in order
to determine if it is a USB mass storage device, to read its configuration, etc.
This happens even if the drive is then assigned and mounted in another qube.

To avoid this risk, it is possible to prepare and utilize a USB qube.

A USB qube acts as a secure handler for potentially malicious USB devices,
preventing them from coming into contact with dom0 (which could otherwise be
fatal to the security of the whole system). With a USB qube, every time you
connect an untrusted USB drive to a USB port managed by that USB controller, you
will have to attach it to the qube in which you wish to use it (if different
from the USB qube itself), either by using Qubes VM Manager or the command line
(see instructions above). 
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

How to hide all USB controllers from dom0
-----------------------------------------

If you create a USB qube manually, there will be a brief period of time during the
boot process during which dom0 will be exposed to your USB controllers (and any
attached devices). This is a potential security risk, since even brief exposure
to a malicious USB device could result in dom0 being compromised. There are two
approaches to this problem:

1. Physically disconnect all USB devices whenever you reboot the host.
2. Hide (i.e., blacklist) all USB controllers from dom0.

**Warning:** If you use a USB [AEM] device, do not use the second option. Using
a USB AEM device requires dom0 to have access to the USB controller to which
your USB AEM device is attached. If dom0 cannot read your USB AEM device, AEM
will hang.

The procedure to hide all USB controllers from dom0 is as follows:

1. Open the file `/etc/default/grub` in dom0.
2. Find the line that begins with `GRUB_CMDLINE_LINUX`.
3. Add `rd.qubes.hide_all_usb` to that line.
4. Save and close the file.
5. Run the command `grub2-mkconfig -o /boot/grub2/grub.cfg` in dom0.
6. Reboot.

(Note: Beginning with R3.2, `rd.qubes.hide_all_usb` is set automatically if you
opt to create a USB qube during installation. This also occurs automatically if
you choose to [create a USB qube] using the `qubesctl` method, which is the
first pair of steps in the linked section.)

**Warning** USB keyboard cannot be used to type the disk passphrase
if USB controllers were hidden from dom0. Before hiding USB controllers
make sure your laptop keyboard is not internally connected via USB
(by checking output of `lsusb` command) or that you have a PS/2 keyboard at hand
(if using a desktop PC). Failure to do so will render your system unusable.


Removing a USB qube
-------------------

**Warning:** This procedure will result in your USB controller(s) being attached
directly to dom0.

1. Shut down the USB qube.
2. In Qubes Manager, right-click on the USB qube and select "Remove VM."
3. Open the file `/etc/default/grub` in dom0.
4. Find the line(s) that begins with `GRUB_CMDLINE_LINUX`.
5. If `rd.qubes.hide_all_usb` appears anywhere in those lines, remove it.
6. Save and close the file.
7. Run the command `grub2-mkconfig -o /boot/grub2/grub.cfg` in dom0.
8. Reboot.


Security Warning about USB Input Devices
----------------------------------------

**Important security warning. Please read this section carefully!**

If you connect USB input devices (keyboard and mouse) to a VM, that VM will effectively have control over your system.
Because of this, the benefits of using a USB qube are much smaller than using a fully untrusted USB qube.
In addition to having control over your system, such VM can also sniff all the input your enter there (for example, passwords in the case of a USB keyboard).

There is no simple way to protect against sniffing, but you can make it harder to exploit control over input devices.

If you have only a USB mouse connected to a USB qube, but the keyboard is connected directly to dom0 (using a PS/2 connector, for example), you simply need to lock the screen when you are away from your computer.
You must do this every time you leave your computer unattended, even if there no risk of anyone else having direct physical access to your computer.
This is because you are guarding the system not only against anyone with local access, but also against possible actions from a potentially compromised USB qube.

If your keyboard is also connected to a USB qube, things are much harder.
Locking the screen (with a traditional password) does not solve the problem, because the USB qube can simply sniff this password and later easily unlock the screen.
One possibility is to set up the screen locker to require an additional step to unlock (i.e., two-factor authentication).
One way to achieve this is to use a [YubiKey], or some other hardware token, or even to manually enter a one-time password.

How to use a USB keyboard
-------------------------

**Caution:** Please carefully read the [Security Warning about USB Input Devices] before proceeding.

In order to use a USB keyboard, you must first attach it to a USB qube, then give that qube permission to pass keyboard input to dom0.
Edit the `qubes.InputKeyboard` policy file in dom0, which is located here:

    /etc/qubes-rpc/policy/qubes.InputKeyboard

Add a line like this one to the top of the file:

    sys-usb dom0 ask,user=root

(Change `sys-usb` to your desired USB qube.)

You can now use your USB keyboard.

How to use a USB mouse
----------------------

**Caution:** Please carefully read the [Security Warning about USB Input Devices] before proceeding.

In order to use a USB mouse, you must first attach it to a USB qube, then give that qube permission to pass mouse input to dom0.
Edit the `qubes.InputMouse` policy file in dom0, which is located here:

    /etc/qubes-rpc/policy/qubes.InputMouse

Add a line like this to the op of the file:

    sys-usb dom0 ask,user=root
    
(Change `sys-usb` to your desired USB qube.)

You can now use your USB mouse.

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
     device to a qube with the name `personal` like so:

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

 6.  In a dom0 console, detach the stick

         qvm-block -d <device>
         
     or
     
         qvm-block -d <vmname>

 7.  You may now remove the device.

**Warning:** Do not remove the device before detaching it from the VM!
Otherwise, you will not be able to attach it anywhere later. See issue [1082]
for details.

If the device does not appear in Nautilus, you will need to mount it
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


Attaching a single USB device to a qube (USB passthrough)
---------------------------------------------------------

Starting with Qubes 3.2, it is possible to attach a single USB device to any
Qube. While this is useful feature, it should be used with care, because there
are [many security implications][usb-challenges] from using USB devices and USB
passthrough will **expose your target qube** for most of them. If possible, use 
method specific for particular device type (for example block devices described
above), instead of this generic one.

To use this feature, you need to install `qubes-usb-proxy` package in the
templates used for USB qube and qubes you want to connect USB devices to. Note
you cannot pass through devices from dom0 (in other words: USB VM is required).

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

This feature is not yet available in Qubes Manager however, if you would like to contribute to Qubes OS project by implementing it and are a student please consider applying for the [Google Summer of Code][gsoc-page] scholarship and choosing QubesOS Project as a mentor organization. You can find list of our our Project Ideas [here][project-page].


[mass-storage]: https://en.wikipedia.org/wiki/USB_mass_storage_device_class
[Assigning Devices]: /doc/assigning-devices/
[usb-controller]: /doc/assigning-devices/#finding-the-right-usb-controller
[623]: https://github.com/QubesOS/qubes-issues/issues/623
[1072-comm1]: https://github.com/QubesOS/qubes-issues/issues/1072#issuecomment-124270051
[1072-comm2]: https://github.com/QubesOS/qubes-issues/issues/1072#issuecomment-124119309
[1082]: https://github.com/QubesOS/qubes-issues/issues/1082
[hide-usb]: #how-to-hide-all-usb-controllers-from-dom0
[faq-usbvm]: /doc/user-faq/#i-created-a-usbvm-and-assigned-usb-controllers-to-it-now-the-usbvm-wont-boot
[AEM]: /doc/anti-evil-maid/
[1618]: https://github.com/QubesOS/qubes-issues/issues/1618
[create a USB qube]: #creating-and-using-a-usb-qube
[usb-challenges]: http://blog.invisiblethings.org/2011/05/31/usb-security-challenges.html
[project-page]: /gsoc/
[gsoc-page]: https://summerofcode.withgoogle.com/organizations/6239659689508864/
[YubiKey]: /doc/YubiKey/
[Security Warning about USB Input Devices]: #security-warning-about-usb-input-devices
