---
layout: doc
title: Assigning Devices
permalink: /doc/assigning-devices/
redirect_from:
- /en/doc/assigning-devices/
- /doc/AssigningDevices/
- /wiki/AssigningDevices/
---

Assigning Devices to VMs
========================

Sometimes you may need to assign an entire PCI or PCI Express device directly to a qube.
This is also known as PCI pass-through.
The Qubes installer does this by default for `sys-net` (assigning all network class controllers), as well as `sys-usb` (assigning all USB controllers) if you chose to create the USB qube during install.
While this covers most use cases, there are some occasions when you may want to manually assign one NIC to `sys-net` and another to a custom NetVM, or have some other type of PCI controller you want to manually assign.

Note that one can only assign full PCI or PCI Express devices by default.
This limit is imposed by the PC and VT-d architectures.
This means if a PCI device has multiple functions, all instances of it need to be assigned to the same qube unless you have disabled the strict requirement for FLR with the `no-strict-reset` (R4.0) or `pci_strictreset` (R3.2) option.
In the steps below, you can tell if this is needed if you see the BDF for the same device listed multiple times with only the number after the "." changing.

While PCI device can only be used by one powered on VM at a time, it *is* possible to *assign* the same device to more than one VM at a time. 
This means that you can use the device in one VM, shut that VM down, start up a different VM (to which the same device is also assigned), then use the device in that VM.
This can be useful if, for example, you have only one USB controller, but you have multiple security domains which all require the use of different USB devices.

R4.0
------------------------

In order to assign a whole PCI(e) device to a VM, one should use the `qvm-pci` tool.
First, list the available PCI devices:

~~~
qvm-pci
~~~

This will show you the `backend:BDF` address of each PCI device. 
It will look something like `dom0:00_1a.0`.
Once you've found the address of the device you want to assign, then attach it like so:

~~~
qvm-pci attach --persistent <vmname> <backend>:<bdf>
~~~

For example, if `00_1a.0` is the BDF of the device you want to assign to the "personal" domain, you would do this:

~~~
qvm-pci attach --persistent personal dom0:00_1a.0
~~~

R3.2
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

Some USB devices are not compatible with the USB pass-through method Qubes employs.
In situations like this, you can still often get the USB device to work by passing through the entire USB controller to a qube.
However, with this approach one cannot assign single USB devices, only the whole USB controller with whatever USB devices are connected to it. 
More information on using and managing USB devices with qubes is available on the [USB] page. 
If you want assign a certain USB device to a VM (by attaching the whole USB controller), you need to figure out which PCI device is the right controller. 
First, check to which USB bus the device is connected (note that these steps need to be run from a terminal inside `dom0`):

~~~
lsusb
~~~

For example, I want assign a broadband modem to the netvm. 
In the output of `lsusb` it can be listed as something like this. 
(In this case, the device isn't fully identified):

~~~
Bus 003 Device 003: ID 413c:818d Dell Computer Corp.
~~~

The device is connected to USB bus \#3. 
Then check which other devices are connected to the same bus, since *all* of them will be assigned to the same VM.
Now is the time to find right USB controller:

~~~
readlink /sys/bus/usb/devices/usb3
~~~

This should output something like:

~~~
../../../devices/pci-0/pci0000:00/0000:00:1a.0/usb3
~~~

Now you see the BDF address in the path (right before final `usb3`).
Strip the leading `0000:` and pass the rest to the `qvm-pci` tool to attach the controller with the version specific steps above.

Possible issues
---------------

### DMA buffer size

VMs with assigned PCI devices in Qubes have allocated a small buffer for DMA operations (called swiotlb).
By default it is 2MB, but some devices need a larger buffer.
To change this allocation, edit VM's kernel parameters (this is expressed in 512B chunks):

~~~
# qvm-prefs netvm |grep kernelopts
kernelopts       : iommu=soft swiotlb=2048 (default)
# qvm-prefs -s netvm kernelopts "iommu=soft swiotlb=8192"
~~~

This is [known to be needed][ml1] for the Realtek RTL8111DL Gigabit Ethernet Controller.

### PCI passthrough issues

Sometimes the PCI arbitrator is too strict. 
There is a way to enable permissive mode for it.
See also: [this thread][ml2] and the Xen wiki's [PCI passthrough] page.

**NOTE:** By setting the permissive flag for the PCI device, you're potentially weakening the device isolation, especially if your system is not equipped with a VT-d Interrupt Remapping unit. 
See [Software Attacks on Intel VT-d] (page 7)
for more details.

At other times, you may instead need to disable the FLR requirement on a device.
This will also weaken device isolation; see the "I created a usbVM..." entry in the [FAQ](/doc/user-faq/) for more details.

R4.0
------------------------

Permissive mode and strict reset are options set as part of PCI device attachment. 
If you've already attached the PCI device to a VM, detach it first either with Qube Manager or `qvm-pci`, then list the available PCI devices:

~~~
qvm-pci
~~~

This will show you the `backend:BDF` address of each PCI device.
It will look something like `dom0:00_1a.0`. 
Once you've found the address of the device you want to assign, then attach it like so:

~~~
qvm-pci attach --persistent --option <option1> [--option <option2>] <vmname> <backend>:<bdf>
~~~

For example, if `00_1a.0` is the BDF of the device you want to assign to the "personal" domain, and it is particularly difficult to pass through you would do this:

~~~
qvm-pci attach --persistent --option permissive=true --option no-strict-reset=true personal dom0:00_1a.0
~~~

Running `qvm-pci` again should then show your PCI device attached with both the `permissive` and `no-strict-reset` options set.

**Note** again that in most cases you should not need either of these options set. 
Only set one or more of them as required to get your device to function, or replace the device with one that functions properly with Qubes.

R3.2
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

By default, when a device is detached from a VM (or when a VM with an attached PCI device is shut down), the device is *not* automatically attached back to dom0. 
This is an intended feature. 
A device which was previously assigned to a VM less trusted than dom0 (which, in Qubes, is *all* of them) could attack dom0 if it were automatically reassigned there.

In order to re-enable the device in dom0, either:

 *  Reboot the physical machine.

or

 *  Go to the sysfs (`/sys/bus/pci`), find the right device, detach it from the pciback driver, and attach it back to the original driver. 
    Replace `<BDF>` with your device, for example `00:1c.2`:

    ~~~
    echo 0000:<BDF> > /sys/bus/pci/drivers/pciback/unbind
    MODALIAS=`cat /sys/bus/pci/devices/0000:<BDF>/modalias`
    MOD=`modprobe -R $MODALIAS | head -n 1`
    echo <BDF> > /sys/bus/pci/drivers/$MOD/bind 
    ~~~


[usb]: /doc/usb/
[ml1]: https://groups.google.com/group/qubes-devel/browse_thread/thread/631c4a3a9d1186e3
[ml2]: https://groups.google.com/forum/#!topic/qubes-users/Fs94QAc3vQI
[PCI passthrough]: https://wiki.xen.org/wiki/Xen_PCI_Passthrough
[Software Attacks on Intel VT-d]: https://invisiblethingslab.com/resources/2011/Software%20Attacks%20on%20Intel%20VT-d.pdf

