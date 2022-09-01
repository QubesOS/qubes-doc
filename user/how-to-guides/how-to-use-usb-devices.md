---
lang: en
layout: doc
permalink: /doc/how-to-use-usb-devices/
redirect_from:
- /doc/usb-devices/
- /doc/usb/
ref: 195
title: How to use USB devices
---

*This page is part of [device handling in qubes](/doc/how-to-use-devices/).*

If you are looking to handle USB *storage* devices (thumbdrives or USB-drives), please have a look at the [block device](/doc/how-to-use-block-storage-devices/) page.

**Note:** Attaching USB devices to VMs requires a [USB qube](/doc/usb-qubes/).

**Important security warning:** USB passthrough comes with many security implications.
Please make sure you carefully read and understand the **[security considerations](/doc/device-handling-security/#usb-security)**.
Whenever possible, attach a [block device](/doc/how-to-use-block-storage-devices/) instead.

Examples of valid cases for USB-passthrough:

- [microcontroller programming](https://www.arduino.cc/en/Main/Howto)
- [external audio devices](/doc/external-audio/)
- [optical drives](/doc/recording-optical-discs/) for recording

(If you are thinking to use a two-factor-authentication device, [there is an app for that](/doc/u2f-proxy/).
But it has some [issues](https://github.com/QubesOS/qubes-issues/issues/4661).)

## Attaching and detaching a USB device

### With Qubes device manager

Click the device-manager-icon: ![device manager icon](/attachment/doc/media-removable.png)
A list of available devices appears.
USB-devices have a USB-icon to their right: ![usb icon](/attachment/doc/generic-usb.png)

Hover on one device to display a list of VMs you may attach it to.

Click one of those.
The USB device will be attached to it.
You're done.

After you finished using the USB-device, you can detach it the same way by clicking on the Devices Widget.
You will see an entry in bold for your device such as **`sys-usb:2-5 - 058f_USB_2.0_Camera`**.
Hover on the attached device to display a list of running VMs.
The one to which your device is connected will have an eject button ![eject icon](/attachment/doc/media-eject.png) next to it.
Click that and your device will be detached.

### With the command line tool

In dom0, you can use `qvm-usb` from the commandline to attach and detach devices.

Listing available USB devices:

```shell_session
[user@dom0 ~]$ qvm-usb
BACKEND:DEVID   DESCRIPTION                    USED BY
sys-usb:2-4     04ca:300d 04ca_300d
sys-usb:2-5     058f:3822 058f_USB_2.0_Camera
sys-usb:2-1     03f0:0641 PixArt_HP_X1200_USB_Optical_Mouse
```

Attaching selected USB device:

```shell_session
[user@dom0 ~]$ qvm-usb attach work sys-usb:2-5
[user@dom0 ~]$ qvm-usb
BACKEND:DEVID   DESCRIPTION                    USED BY
sys-usb:2-4     04ca:300d 04ca_300d
sys-usb:2-5     058f:3822 058f_USB_2.0_Camera  work
sys-usb:2-1     03f0:0641 PixArt_Optical_Mouse
```

Now, you can use your USB device (camera in this case) in the `work` qube.
If you see the error `ERROR: qubes-usb-proxy not installed in the VM` instead, please refer to the [Installation Section](#installation-of-qubes-usb-proxy).

When you finish, detach the device.

```shell_session
[user@dom0 ~]$ qvm-usb detach work sys-usb:2-5
[user@dom0 ~]$ qvm-usb
BACKEND:DEVID   DESCRIPTION                    USED BY
sys-usb:2-4     04ca:300d 04ca_300d
sys-usb:2-5     058f:3822 058f_USB_2.0_Camera
sys-usb:2-1     03f0:0641 PixArt_Optical_Mouse
```

## Maintenance and customisation

### Creating and using a USB qube

If you've selected to install a usb-qube during system installation, everything is already set up for you in `sys-usb`.
If you've later decided to create a usb-qube, please follow [this guide](/doc/usb-qubes/).

### Installation of `qubes-usb-proxy`

To use this feature, the `qubes-usb-proxy` package needs to be installed in the templates used for the USB qube and qubes you want to connect USB devices to.
This section exists for reference or in case something broke and you need to reinstall `qubes-usb-proxy`.
Under normal conditions, `qubes-usb-proxy` should already be installed and good to go.

If you receive this error: `ERROR: qubes-usb-proxy not installed in the VM`, you can install the `qubes-usb-proxy` with the package manager in the VM you want to attach the USB device to.

- Fedora: 
  ```
  sudo dnf install qubes-usb-proxy
  ```
- Debian/Ubuntu: 
  ```
  sudo apt-get install qubes-usb-proxy
  ```

### Using USB keyboards and other input devices

**Warning:** especially keyboards need to be accepted by default when using them to login! Please make sure you carefully read and understood the **[security considerations](/doc/device-handling-security/#usb-security)** before continuing!

Mouse and keyboard setup are part of [setting up a USB qube](/doc/usb-qubes/).

### Finding the right USB controller

Some USB devices are not compatible with the USB pass-through method Qubes employs.
In situations like these, you can try to pass through the entire USB controller to a qube as PCI device.
However, with this approach one cannot attach single USB devices but has to attach the whole USB controller with whatever USB devices are connected to it.

If you have multiple USB controllers, you must first figure out which PCI device is the right controller.

First, find out which USB bus the device is connected to (note that these steps need to be run from a terminal inside your USB qube):

```
lsusb
```

For example, I want to attach a broadband modem to the NetVM.
In the output of `lsusb` it may be listed as something like:

```
Bus 003 Device 003: ID 413c:818d Dell Computer Corp.
```

(In this case, the device isn't fully identified)

The device is connected to USB bus \#3.
Check which other devices are connected to the same bus, since *all* of them will be attach to the same VM.

To find the right controller, follow the usb bus:

```
readlink /sys/bus/usb/devices/usb3
```

This should output something like:

```
../../../devices/pci-0/pci0000:00/0000:00:1a.0/usb3
```

Now you see the path and the text between `/pci0000:00/0000:` and `/usb3` i.e. `00:1a.0` is the BDF address. Strip the address and pass it to the [`qvm-pci` tool](/doc/how-to-use-pci-devices/) to attach the controller to the targetVM.

For example, On R 4.0 the command would look something like

```
qvm-pci attach --persistent personal dom0:00_1a.0
```
