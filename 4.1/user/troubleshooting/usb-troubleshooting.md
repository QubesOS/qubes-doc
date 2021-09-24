---
lang: en
layout: doc
permalink: /doc/4.1/4.1/usb-troubleshooting/
ref: 234
title: USB troubleshooting
---

## disp-sys-usb does not start

If the disp-sys-usb does not start, it could be due to a PCI passthrough problem.
For more details on this issue along with possible solutions, look at [PCI passthrough issues](/doc/pci-troubleshooting/#pci-passthrough-issues).

## Can't attach a USB device / USB device not showing in qvm-usb

To successfully attach a USB device, you require a VM dedicated to handling the USB input and output.
For guidance setting up a USB qube, see the [USB documentation](/doc/how-to-use-usb-devices/#creating-and-using-a-usb-qube).

Currently (until issue [1082](https://github.com/QubesOS/qubes-issues/issues/1082) gets implemented), if you remove the device before detaching it from the qube, Qubes OS (more precisely, `libvirtd`) will think that the device is still attached to the qube and will not allow attaching further devices under the same name.
This may be characterized by VM manager crashes and the error message: `Houston, we have a problem`.
The easiest way to recover from such a situation is to reboot the qube to which the device was attached.
If this isn't an option, you can manually recover from the situation by following the instructions at the [Block Devices documentation](/doc/how-to-use-block-storage-devices/#what-if-i-removed-the-device-before-detaching-it-from-the-vm)

## "Device attach failed" error

Upon trying to attach a USB device using the `qvm-usb -a vm-name device-vm-name:device` command, you may face the error `Device attach failed: no device info received, connection failed, check backend side for details`.
This error mainly arises due to problems specific to the particular device, such as the device being incompatible with qvm-usb or a broken cable.

## Attaching device to a qube works, but the device disconnects or disappears upon usage

After attaching a device to a qube, upon attempting to use the device results in the device disappearing or disconnecting. This may be observed by the device no longer existing in the Devices widget or the application within the attached qube indicating the device is no longer found.

As a first line of defense, increase the amount of memory given to the USB VM (sys-usb). High-bandwidth devices such as webcams have been [observed](https://github.com/QubesOS/qubes-issues/issues/6200) to need more memory in sys-usb. If increasing the amount of memory does not resolve the issue, check kernel logs within sys-usb as well as the attached qube for errors before filing a bug report.

## USB VM does not boot after creating and assigning USB controllers to it

This is probably because one of the controllers does not support reset.
In Qubes R2 any such errors were ignored. In Qubes R3.x they are not.
In R4.x, devices that are automatically added to sys-net and sys-usb on install but do not support FLR will be attached with the no-strict-reset option, but see the related warning in the last sentence in this answer.

A device that does not support reset is not ideal and generally should not be assigned to a VM.

Most likely the offending controller is a USB 3.0 device.
You can remove this controller from the USB VM, and see if this allows the VM to boot.
Alternatively you may be able to disable USB 3.0 in the BIOS.
If the BIOS does not have the option to disable USB 3.0, try running the following command in dom0 to force USB 2.0 modes for the USB ports:

```
lspci -nn | grep USB | cut -d '[' -f3 | cut -d ']' -f1 | xargs -I@ setpci -H1 -d @ d0.l=0
```

Errors suggesting this issue:

- in `xl dmesg` output:

  ```
  (XEN) [VT-D] It's disallowed to assign 0000:00:1a.0 with shared RMRR at dbe9a000 for Dom19.
  (XEN) XEN_DOMCTL_assign_device: assign 0000:00:1a.0 to dom19 failed (-1)
  ```

- during `qvm-start sys-usb`:

  ```
  internal error: Unable to reset PCI device [...]  no FLR, PM reset or bus reset available.
  ```

Another solution would be to set the pci_strictreset option in dom0:

- In Qubes R4.x, when attaching the PCI device to the VM (where `<BDF>` can be obtained from running `qvm-pci`):

  ```
  qvm-pci attach --persistent --option no-strict-reset=true usbVM dom0:<BDF>
  ```

- In Qubes R3.x, by modifying the VM's properties:

  ```
  qvm-prefs usbVM -s pci_strictreset false
  ```

These options allow the VM to ignore the error and the VM will start.
Please review the notes in the `qvm-prefs` man page and [here](/doc/how-to-use-devices/) and be aware of the potential risks.

## Can't use keyboard or mouse after creating sys-usb

You risk locking yourself out of your computer if you have a USB keyboard and use full disk encryption alongside sys-usb.
On boot, the keyboard may be inactive, preventing you from entering your LUKS decryption password.

When you enable a USB qube, it hides all the USB controllers from dom0, even before it gets started.
So, if your only keyboard is on USB, you should undo this hiding.

To solve the problem, disable the USB qube by not having it autostart, or unassigning your USB controller(s) from it. If you had created the USB qube by checking the box in the installer, then your USB controller(s) are probably hidden from dom0. To unhide them, reverse the procedure described in the [USB Qubes documentation](/doc/usb-qubes/#how-to-hide-all-usb-controllers-from-dom0) (under "How to hide all USB controllers from dom0"). That is, remove `rd.qubes.hide_all_usb`, instead of adding it.

Note that this procedure will attach your USB controllers to dom0, so do this only with USB devices you trust.

If your computer has a PS/2 port, you may instead use a PS/2 keyboard to enter the LUKS password.

## "qubes-usb-proxy not installed in the VM" error

When trying to [create and use a USB qube](/doc/how-to-use-usb-devices/#creating-and-using-a-usb-qube) with the `qubes-usb-proxy` package, you may receive this error: `ERROR: qubes-usb-proxy not installed in the VM`.

If you encounter this error, you can install the `qubes-usb-proxy` with the package manager in the VM you want to attach the USB device to.
Depending on your operating system, open a terminal in the template and enter one of the following commands:

- Fedora: `sudo dnf install qubes-usb-proxy`
- Debian/Ubuntu: `sudo apt-get install qubes-usb-proxy`
