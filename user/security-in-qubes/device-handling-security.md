---
lang: en
layout: doc
permalink: /doc/device-handling-security/
ref: 170
title: Device Handling Security
---


Any additional ability a VM gains is additional attack surface.
It's a good idea to always attach the minimum entity required in a VM.

For example, attaching a full USB-device offers [more attack surface than attaching a single block device](https://blog.invisiblethings.org/2011/05/31/usb-security-challenges.html "ITL blog post on USB security"), while
attaching a full block device (e.g. `sda`) again offers more attack surface than attaching a single partition (e.g. `sda1`), since the targetVM doesn't have to parse the partition-table.
(Attaching a full block device offers the advantage that most file-managers will mount and display them correctly, whereas they don't expect single partitions to be added and therefore don't handle them correctly.)

## PCI Security

Attaching a PCI device to a qube has serious security implications.
It exposes the device driver running in the qube to an external device (and sourceVM, which contains the device - e.g. `sys-usb`).
In many cases a malicious device can choose what driver will be loaded (for example by manipulating device metadata like vendor and product identifiers) - even if the intended driver is sufficiently secure, the device may try to attack a different, less secure driver.
Furthermore that VM has full control of the device and may be able to exploit bugs or malicious implementation of the hardware, as well as plain security problems the hardware may pose.
(For example, if you attach a USB controller, all the security implications of USB passthrough apply as well.)

By default, Qubes requires any PCI device to be resettable from the outside (i.e. via the hypervisor), which completely reinitialises the device.
This ensures that any device that was attached to a compromised VM, even if that VM was able to use bugs in the PCI device to inject malicious code, can be trusted again.
(Or at least as trusted as it was when Qubes booted.)

Some devices do not implement a reset option.
In these cases, Qubes by default does not allow attaching the device to any VM.
If you decide to override this precaution, beware that the device may only be trusted when attached to the first VM.
Afterwards, it should be **considered tainted** until the whole system is shut down.
Even without malicious intent, usage data may be leaked.

In case device reset is disabled for any reason, detaching the device should be considered a risk.
Ideally, devices for which the `no-strict-reset` option is set are attached once to a VM which isn't shut down until the system is shut down.

Additionally, Qubes restricts the config-space a VM may use to communicate with a PCI device.
Only whitelisted registers are accessible.
However, some devices or applications require full PCI access.
In these cases, the whole config-space may be allowed.
You're potentially weakening the device isolation, especially if your system is not equipped with a VT-d Interrupt Remapping unit.
This increases the VM's ability to run a [side channel attack](https://en.wikipedia.org/wiki/Side-channel_attack) and vulnerability to the same.
See [Xen PCI Passthrough: PV guests and PCI quirks](https://wiki.xenproject.org/wiki/Xen_PCI_Passthrough#PV_guests_and_PCI_quirks) and [Software Attacks on Intel VT-d](https://invisiblethingslab.com/resources/2011/Software%20Attacks%20on%20Intel%20VT-d.pdf) \(page 7) for more details.

## USB Security

The connection of an untrusted USB device to dom0 is a security risk since the device can attack an arbitrary USB driver (which are included in the linux kernel), exploit bugs during partition-table-parsing or simply pretend to be a keyboard.
There are many ready-to-use implementations of such attacks, e.g. a [USB Rubber Ducky](https://shop.hak5.org/products/usb-rubber-ducky-deluxe).
The whole USB stack is put to work to parse the data presented by the USB device in order to determine if it is a USB mass storage device, to read its configuration, etc.
This happens even if the drive is then assigned and mounted in another qube.

To avoid this risk, use a [USB qube](/doc/usb-qubes/).

Attaching a USB device to a VM (USB passthrough) will **expose your target qube** to most of the [security issues](https://blog.invisiblethings.org/2011/05/31/usb-security-challenges.html "ITL blog post on USB security") associated with the USB-stack.
If possible, use a method specific for particular device type (for example, block devices described above), instead of this generic one.

## Security Warning On USB Input Devices

If you connect USB input devices (keyboard and mouse) to a VM, that VM will effectively have control over your system.
Because of this, the benefits of using a [USB qube](/doc/usb-qubes/) entrusted with a keyboard or other interface device are much smaller than using a fully untrusted USB qube.
In addition to having control over your system, such a VM can also sniff all the input you enter there (for example, passwords in the case of a USB keyboard).

There is no simple way to protect against sniffing, but you can make it harder to exploit control over input devices.

If you have only a USB mouse connected to a USB qube, but the keyboard is connected directly to dom0 (using a PS/2 connector, for example), you simply need to lock the screen when you are away from your computer.
You must do this every time you leave your computer unattended, even if there no risk of anyone else having direct physical access to your computer.
This is because you are guarding the system not only against anyone with local access, but also against possible actions from a potentially compromised USB qube.

If your keyboard is also connected to a USB qube, things are much harder.
Locking the screen (with a traditional password) does not solve the problem, because the USB qube can simply sniff this password and later easily unlock the screen.
One possibility is to set up the screen locker to require an additional step to unlock (i.e., two-factor authentication).
One way to achieve this is to use a [YubiKey](/doc/YubiKey/), or some other hardware token, or even to manually enter a one-time password.

Support for [two factor authentication](/news/2018/09/11/qubes-u2f-proxy/) was recently added, though there are [issues](https://github.com/QubesOS/qubes-issues/issues/4661).

