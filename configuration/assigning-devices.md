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

In order to assign a whole PCI(e) device to a VM, one should use the `qvm-pci`
tool. First, list the available PCI devices:

~~~
lspci
~~~

This will show you the BDF address of each PCI device. It will look something
like `00:1a.0`. Once you've found the BDF address of the device you want to
assign, then attach it like so:

~~~
qvm-pci -a <vmname> <bdf>
~~~

For example, if `00:1a.0` is the BDF of the device I want to assign to the
"personal" domain, I would do this:

~~~
qvm-pci -a personal 00:1a.0
~~~

Note that one can only assign full PCI or PCI Express devices. This means one
cannot assign single USB devices -- only the whole USB controller with whatever
USB devices are connected to it. This limit is imposed by the PC and VT-d
architectures. More information on using and managing USB devices with qubes is
available on the [USB] page.

While a device can only be attached to one VM at a time, it *is* possible to
*assign* the same device to more than one VM at a time. This means that you can
use the device in one VM, shut that VM down, start up a different VM (to which
the same device is also assigned), then use the device in that VM. This can be
useful if, for example, you have only one USB controller, but you have multiple
security domains which all require the use of different USB devices.


Using Qubes Manager
-------------------

The above steps can also be done in Qubes Manager. Simply go into the VM
settings of your desired VM, then go to the "Devices" tab. This will show you a
list of available devices, which you can select to be assigned to that VM.


Finding the right USB controller
--------------------------------

If you want assign a certain [USB] device to a VM (by attaching the whole
USB controller), you need to figure out which PCI device is the right
controller. First, check to which USB bus the device is connected:

~~~
lsusb
~~~

For example, I want assign a broadband modem to the netvm. In the out put of
`lsusb` it can be listed as something like this. (In this case, the device isn't
fully identified):

~~~
Bus 003 Device 003: ID 413c:818d Dell Computer Corp.
~~~

The device is connected to USB bus \#3. Then check which other devices are
connected to the same bus, since *all* of them will be assigned to the same VM.
Now is the time to find right USB controller:

~~~
readlink /sys/bus/usb/devices/usb3
~~~

This should output something like:

~~~
../../../devices/pci-0/pci0000:00/0000:00:1a.0/usb3
~~~

Now you see the BDF address in the path (right before final `usb3`). Strip the
leading `0000:` and pass the rest to the `qvm-pci` tool:

~~~
qvm-pci -a netvm 00:1a.0
~~~


Possible issues
---------------

### DMA buffer size

VMs with assigned PCI devices in Qubes have allocated a small buffer for DMA
operations (called swiotlb). By default it is 2MB, but some devices need a
larger buffer. To change this allocation, edit VM's kernel parameters (this is
expressed in 512B chunks):

~~~
# qvm-prefs netvm |grep kernelopts
kernelopts       : iommu=soft swiotlb=2048 (default)
# qvm-prefs -s netvm kernelopts "iommu=soft swiotlb=4096"
~~~

This is [known to be needed][ml1] for the Realtek RTL8111DL Gigabit Ethernet
Controller.

### PCI passthrough issues

Sometimes PCI arbitrator is too strict. There is a way to enable permissive mode
for it. Create `/etc/systemd/system/qubes-pre-netvm.service`:

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

See also: [this thread][ml2] and the Xen wiki's [PCI passthrough] page.

**NOTE:** By setting the permissive flag for the PCI device, you're potentially
weakening the device isolation, especially if your system is not equipped with
VT-d Interrupt Remapping unit. See [Software Attacks on Intel VT-d] (page 7)
for more details.


Bringing PCI device back to dom0
--------------------------------

By default, when a device is detached from a VM (or when a VM with an attached
PCI device is shut down), the device is *not* automatically attached back to
dom0. This is an intended feature. A device which was previously assigned to a
VM less trusted than dom0 (which, in Qubes, is *all* of them) could attack dom0
if it were automatically reassigned there.

In order to re-enable the device in dom0, either:

 *  Reboot the physical machine.

or

 *  Go to the sysfs (`/sys/bus/pci`), find the right device, detach it from the
    pciback driver, and attach it back to the original driver. Replace `<BDF>`
    with your device, for example `00:1c.2`:

    ~~~
    echo 0000:<BDF> > /sys/bus/pci/drivers/pciback/unbind
    MODALIAS=`cat /sys/bus/pci/devices/0000:<BDF>/modalias`
    MOD=`modprobe -R $MODALIAS | head -n 1`
    echo <BDF> > /sys/bus/pci/drivers/$MOD/bind 
    ~~~


[usb]: /doc/usb/
[ml1]: https://groups.google.com/group/qubes-devel/browse_thread/thread/631c4a3a9d1186e3
[ml2]: https://groups.google.com/forum/#!topic/qubes-users/Fs94QAc3vQI
[PCI passthrough]: http://wiki.xen.org/wiki/Xen_PCI_Passthrough
[Software Attacks on Intel VT-d]: http://www.invisiblethingslab.com/resources/2011/Software%20Attacks%20on%20Intel%20VT-d.pdf

