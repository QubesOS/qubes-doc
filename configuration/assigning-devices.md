---
layout: doc
title: Assigning Devices in R3.2
permalink: /doc/assigning-devices/
redirect_from:
- /en/doc/assigning-devices/
- /doc/AssigningDevices/
- /wiki/AssigningDevices/
---

Assigning Devices to VMs in R3.2
================================
(In case you were looking for the [R4.0 documentation](/doc/pci-devices/).)

Sometimes you may need to assign an entire PCI or PCI Express device directly to a qube.
This is also known as PCI passthrough.
The Qubes installer does this by default for `sys-net` (assigning all network class controllers), as well as `sys-usb` (assigning all USB controllers) if you chose to create the USB qube during install.
While this covers most use cases, there are some occasions when you may want to manually assign one NIC to `sys-net` and another to a custom NetVM, or have some other type of PCI controller you want to manually assign.

Note that one can only assign full PCI or PCI Express devices by default.
This limit is imposed by the PC and VT-d architectures.
This means if a PCI device has multiple functions, all instances of it need to be assigned to the same qube unless you have disabled the strict requirement for FLR with the `no-strict-reset` (R4.0) or `pci_strictreset` (R3.2) option.
In the steps below, you can tell if this is needed if you see the BDF for the same device listed multiple times with only the number after the "." changing.

While PCI device can only be used by one powered on VM at a time, it *is* possible to *assign* the same device to more than one VM at a time. 
This means that you can use the device in one VM, shut that VM down, start up a different VM (to which the same device is also assigned), then use the device in that VM.
This can be useful if, for example, you have only one USB controller, but you have multiple security domains which all require the use of different USB devices.

Using the Command Line
------------------------

In order to assign a whole PCI(e) device to a VM, one should use the `qvm-pci` tool.
First, list the available PCI devices:

~~~
lspci
~~~

This will show you the BDF address of each PCI device.
It will look something like `00:1a.0`. 
Once you've found the BDF address of the device you want to assign, then attach it like so:

~~~
qvm-pci -a <vmname> <bdf>
~~~

For example, if `00:1a.0` is the BDF of the device you want to assign to the "personal" domain, you would do this:

~~~
qvm-pci -a personal 00:1a.0
~~~

Using Qubes Manager
-------------------

The above steps can also be done in Qubes Manager.
Simply go into the VM settings of your desired VM, then go to the "Devices" tab.
This will show you a list of available devices, which you can select to be assigned to that VM.


Finding the right USB controller
--------------------------------
This was moved to the [current documentation][finding controller].

Possible issues
---------------
Please refer to the [current documentation][possible issues] for an issue description and carefully read the [security implications]!
Return here for a guide on how to enable permissive mode and disable strict reset!

Enabling permissive mode
------------------------

Permissive mode is enabled system wide per device.

Create `/etc/systemd/system/qubes-pre-netvm.service`:

~~~
[Unit]
Description=Netvm fixup
Before=qubes-netvm.service

[Service]
ExecStart=/bin/sh -c 'echo 0000:04:00.0 > /sys/bus/pci/drivers/pciback/permissive'
Type=oneshot
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
~~~

Then enable it with `systemctl enable qubes-pre-netvm.service`

The strict reset option is set for all devices attached to a VM with:

```
qvm-prefs usbVM -s pci_strictreset false
```

**Note** again that in most cases you should not need either of these options set.
Only set one or more of them as required to get your device to function, or replace the device with one that functions properly with Qubes.

Bringing PCI device back to dom0
--------------------------------
This was moved to the [current documentation][bring back devices].



[usb]: /doc/usb/
[finding controller]: /doc/usb-devices/#finding-the-right-usb-controller
[possible issues]: /doc/pci-devices/#possible-issues
[security implications]: /doc/device-considerations/#pci-security
[bring back devices]: /doc/pci-devices/#bringing-pci-devices-back-to-dom0