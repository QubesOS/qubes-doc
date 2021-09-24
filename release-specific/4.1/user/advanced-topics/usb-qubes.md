---
lang: en
layout: doc
permalink: /doc/4.1/usb-qubes/
redirect_from:
- /doc/usbvm/
- /en/doc/usbvm/
- /doc/USBVM/
- /wiki/USBVM/
- /doc/sys-usb/
ref: 181
title: USB qubes
---

If during installation you enabled the creation of a USB-qube, your system should be setup already and none of the mentioned steps here should be necessary. (Unless you want to [remove your USB-qube](#removing-a-usb-qube).) If for any reason no USB-qube was created during installation, this guide will show you how to do so.

**Caution:** If you want to use a USB-keyboard, please beware of the possibility to lock yourself out! To avoid this problem [enable your keyboard for login](#enable-a-usb-keyboard-for-login)!

## Creating and Using a USB qube ##

**Warning:** This has the potential to prevent you from connecting a keyboard to Qubes via USB.
There are problems with doing this in an encrypted install (LUKS).
If you find yourself in this situation, see this [issue](https://github.com/QubesOS/qubes-issues/issues/2270#issuecomment-242900312).

A USB qube acts as a secure handler for potentially malicious USB devices, preventing them from coming into contact with dom0 (which could otherwise be fatal to the security of the whole system). It thereby mitigates some of the [security implications](/doc/device-handling-security/#usb-security) of using USB devices.
With a USB qube, every time you connect an untrusted USB drive to a USB port managed by that USB controller, you will have to attach it to the qube in which you wish to use it (if different from the USB qube itself), either by using Qubes VM Manager or the command line (see instructions above).
The USB controller may be assigned on the **Devices** tab of a qube's settings page in Qubes VM Manager or by using the [qvm-pci](/doc/how-to-use-pci-devices/) command.
For guidance on finding the correct USB controller, see the [according passage on PCI-devices](/doc/how-to-use-usb-devices/#finding-the-right-usb-controller).
You can create a USB qube using the management stack by performing the following steps as root in dom0:

```
sudo qubesctl state.sls qvm.sys-usb
```

Alternatively, you can create a USB qube manually as follows:

1. Read the [PCI Devices](/doc/how-to-use-pci-devices/) page to learn how to list and identify your USB controllers.
   Carefully check whether you have a USB controller that would be appropriate to assign to a USB qube.
   Note that it should be free of input devices, programmable devices, and any other devices that must be directly available to dom0.
   If you find a free controller, note its name and proceed to step 2.
2. Create a new qube.
   Give it an appropriate name and color label (recommended: `sys-usb`, red).
3. In the qube's settings, go to the "Devices" tab.
   Find the USB controller that you identified in step 1 in the "Available" list.
   Move it to the "Selected" list by highlighting it and clicking the single arrow `>` button.

   **Caution:** By assigning a USB controller to a USB qube, it will no longer be available to dom0.
   This can make your system unusable if, for example, you have only one USB controller, and you are running Qubes off of a USB drive.

4. Click `OK`.
   Restart the qube.
5. Recommended: Check the box on the "Basic" tab which says "Start VM automatically on boot".
   (This will help to mitigate attacks in which someone forces your system to reboot, then plugs in a malicious USB device.)

If the USB qube will not start, please have a look at the [faq](/faq/#i-created-a-usb-vm-and-assigned-usb-controllers-to-it-now-the-usb-vm-wont-boot).

## Enable a USB keyboard for login ##

**Caution:** Please carefully read the [Security Warning about USB Input Devices](/doc/device-handling-security/#security-warning-on-usb-input-devices) before proceeding!

If you use USB keyboard, automatic USB qube creation during installation is disabled.
Additional steps are required to avoid locking you out from the system.
Those steps are not performed by default, because of risk explained in [Security Warning about USB Input Devices](/doc/device-handling-security/#security-warning-on-usb-input-devices).

### Automatic setup ###

To allow USB keyboard usage (including early boot for LUKS passphrase), make sure you have the latest `qubes-mgmt-salt-dom0-virtual-machines` package (simply [install dom0 updates](/doc/how-to-install-software-in-dom0/#how-to-update-dom0)) and execute in dom0:

```
sudo qubesctl state.sls qvm.usb-keyboard
```

The above command will take care of all required configuration, including creating USB qube if not present.
Note that it will expose dom0 to USB devices while entering LUKS passphrase.
Users are advised to physically disconnect other devices from the system for that time, to minimize the risk.

To undo these changes, please follow the section on [**Removing a USB qube**](#removing-a-usb-qube)!

If you wish to perform only a subset of this configuration (for example do not enable USB keyboard during boot), see manual instructions below.

### Manual setup ###

In order to use a USB keyboard, you must first attach it to a USB qube, then give that qube permission to pass keyboard input to dom0.
Edit the `qubes.InputKeyboard` policy file in dom0, which is located here:

```
/etc/qubes-rpc/policy/qubes.InputKeyboard
```

Add a line like this one to the top of the file:

```
sys-usb dom0 allow
```

(Change `sys-usb` to your desired USB qube.)

You can now use your USB keyboard to login and for LUKS decryption during boot.

For a confirmation dialog each time the USB keyboard is connected, *which will effectively disable your USB keyboard for login and LUKS decryption*, change this line to:

```
sys-usb dom0 ask,default_target=dom0
```

*Don't do that if you want to unlock your device with a USB keyboard!*

Additionally, if you want to use USB keyboard to enter LUKS passphrase, it is incompatible with [hiding USB controllers from dom0](#how-to-hide-all-usb-controllers-from-dom0).
You need to revert that procedure (remove `rd.qubes.hide_all_usb` option from files mentioned there) and employ alternative protection during system boot - disconnect other devices during startup.

## Auto Enabling A USB Mouse ##

**Caution:** Please carefully read the [Security Warning about USB Input Devices](/doc/device-handling-security/#security-warning-on-usb-input-devices) before proceeding.

Handling a USB mouse isn't as critical as handling a keyboard, since you can login using the keyboard and accept the popup dialogue using your keyboard alone.

If you want to attach the USB mouse automatically anyway, you have to edit the `qubes.InputMouse` policy file in dom0, located at:

```
/etc/qubes-rpc/policy/qubes.InputMouse
```

The first line should read similar to:

```
sys-usb dom0 ask,default_target=dom0
```

which will ask for conformation each time a USB mouse is attached. If the file is empty or does not exist, maybe something went wrong during setup, try to rerun `qubesctl state.sls qvm.sys-usb` in dom0.

In case you are absolutely sure you do not want to confirm mouse access from `sys-usb` to `dom0`, you may add the following line on top of the file:

```
sys-usb dom0 allow
```

(Change `sys-usb` to your desired USB qube.)

## How to hide all USB controllers from dom0 ##

(Note: `rd.qubes.hide_all_usb` is set automatically if you opt to create a USB qube during installation.
This also occurs automatically if you choose to [create a USB qube](#creating-and-using-a-usb-qube) using the `qubesctl` method, which is the
first pair of steps in the linked section.)

**Warning:** A USB keyboard cannot be used to type the disk passphrase if USB controllers were hidden from dom0.
Before hiding USB controllers, make sure your laptop keyboard is not internally connected via USB (by checking output of the `lsusb` command) or that you have a PS/2 keyboard at hand (if using a desktop PC).
Failure to do so will render your system unusable.

If you create a USB qube manually, there will be a brief period of time during the boot process when dom0 will be exposed to your USB controllers (and any attached devices).
This is a potential security risk, since even brief exposure to a malicious USB device could result in dom0 being compromised.
There are two approaches to this problem:

1. Physically disconnect all USB devices whenever you reboot the host.
2. Hide (i.e., blacklist) all USB controllers from dom0.

**Warning:** If you use a USB [AEM](/doc/anti-evil-maid/) device, do not use the second option.
Using a USB AEM device requires dom0 to have access to the USB controller to which your USB AEM device is attached.
If dom0 cannot read your USB AEM device, AEM will hang.

The procedure to hide all USB controllers from dom0 is as follows:

* GRUB2

  1. Open the file `/etc/default/grub` in dom0.
  2. Find the line that begins with `GRUB_CMDLINE_LINUX`.
  3. Add `rd.qubes.hide_all_usb` to that line.
  4. Save and close the file.
  5. Run the command `grub2-mkconfig -o /boot/grub2/grub.cfg` in dom0.
  6. Reboot.

* EFI

  1. Open the file `/boot/efi/EFI/qubes/xen.cfg` in dom0.
  2. Find the lines that begin with `kernel=`. There may be more than one.
  3. Add `rd.qubes.hide_all_usb` to those lines.
  4. Save and close the file.
  5. Reboot.

## Removing a USB qube ##

**Warning:** This procedure will result in your USB controller(s) being attached directly to dom0.

* GRUB2

  1. Shut down the USB qube.
  2. In Qubes Manager, right-click on the USB qube and select "Remove VM."
  3. Open the file `/etc/default/grub` in dom0.
  4. Find the line(s) that begins with `GRUB_CMDLINE_LINUX`.
  5. If `rd.qubes.hide_all_usb` appears anywhere in those lines, remove it.
  6. Save and close the file.
  7. Run the command `grub2-mkconfig -o /boot/grub2/grub.cfg` in dom0.
  8. Reboot.

* EFI

  1. Shut down the USB qube.
  2. In Qubes Manager, right-click on the USB qube and select "Remove VM."
  3. Open the file `/boot/efi/EFI/qubes/xen.cfg` in dom0.
  4. Find the line(s) that begins with `kernel=`.
  5. If `rd.qubes.hide_all_usb` appears anywhere in those lines, remove it.
  6. Save and close the file.
  7. Reboot.
