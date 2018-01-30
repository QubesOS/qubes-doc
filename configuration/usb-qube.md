---
layout: doc
title: Configuring a USB Qube
permalink: /doc/usb-qube/
redirect_from:
- /doc/usbvm/
- /en/doc/usbvm/
- /doc/USBVM/
- /wiki/USBVM/
- /doc/sys-usb/
---

Configuring a USB Qube
==============================

Creating and Using a USB qube
-----------------------------

**Warning:** This has the potential to prevent you from connecting a keyboard to Qubes via USB. There are problems with doing this in an encrypted install (LUKS). If you find yourself in this situation, see this [issue][2270-comm23].

Connecting an untrusted USB device to dom0 is a security risk since dom0,
like almost every OS, reads partition tables automatically. The whole
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

        sudo qubesctl top.enable qvm.sys-usb

 2. Apply the configuration:

        sudo qubesctl state.highstate

Alternatively, you can create a USB qube manually as follows:

 1.  Read the [Assigning Devices] page to learn how to list and identify your
     USB controllers. Carefully check whether you have a USB controller that
     would be appropriate to assign to a USB qube. Note that it should have no
     input devices, programmable devices, and any other devices that must be
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

**Warning:** USB keyboard cannot be used to type the disk passphrase
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
In addition to having control over your system, such VM can also sniff all the input you enter there (for example, passwords in the case of a USB keyboard).

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

    sys-usb dom0 allow,user=root

(Change `sys-usb` to your desired USB qube.)

You can now use your USB keyboard.

For a confirmation dialog each time the USB keyboard is connected, change this line to:
```
sys-usb dom0 ask,default_target=dom0
```

How to use a USB mouse
----------------------

**Caution:** Please carefully read the [Security Warning about USB Input Devices] before proceeding.

In order to use a USB mouse, you must first attach it to a USB qube, then give that qube permission to pass mouse input to dom0.
Edit the `qubes.InputMouse` policy file in dom0, which is located here:

    /etc/qubes-rpc/policy/qubes.InputMouse

Add a line like this to the top of the file:

    sys-usb dom0 allow,user=root
    
(Change `sys-usb` to your desired USB qube.)

You can now use your USB mouse.

For a confirmation dialog each time the USB mouse is connected, change this line to:
```
sys-usb dom0 ask,default_target=dom0
```


[2270-comm23]: https://github.com/QubesOS/qubes-issues/issues/2270#issuecomment-242900312
[Assigning Devices]: /doc/assigning-devices/
[faq-usbvm]: /faq/#i-created-a-usbvm-and-assigned-usb-controllers-to-it-now-the-usbvm-wont-boot
[AEM]: /doc/anti-evil-maid/
[create a USB qube]: #creating-and-using-a-usb-qube
[YubiKey]: /doc/YubiKey/
[Security Warning about USB Input Devices]: #security-warning-about-usb-input-devices
