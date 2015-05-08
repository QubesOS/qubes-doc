---
layout: doc
title: AssigningDevices
permalink: /doc/AssigningDevices/
redirect_from: /wiki/AssigningDevices/
---

Assigning Devices to VMs
========================

In order to assign a whole PCI(e) device to a VM, one should use `qvm-pci` tool. E.g.

{% highlight trac-wiki %}
lspci
{% endhighlight %}

Find the BDF address of the device you want to assign, and then:

{% highlight trac-wiki %}
qvm-pci -a <vmname> <bdf>
{% endhighlight %}

E.g. assuming 00:1a.0 is a BDF of the device I want to assign to the "personal" domain:

{% highlight trac-wiki %}
qvm-pci -a personal 00:1a.0
{% endhighlight %}

Note that one can only assign full PCI or PCI Express devices. This means one cannot assign single USB devices -- only the whole USB controller with whatever USB devices connected to it. This limit is imposed by PC and VT-d architecture.

Using Qubes Manager
-------------------

TODO

\<screenshot\>

Finding the right USB controller
--------------------------------

If you want assign certain USB device to a VM (by attaching a whole USB controller), you need to figure out which PCI device is the right controller. First check to which USB bus the device is connected:

{% highlight trac-wiki %}
lsusb
{% endhighlight %}

For example I want assign a broadband modem to the netvm. In lsusb output it can be listed as something like this (in this case device isn't fully identified):

{% highlight trac-wiki %}
Bus 003 Device 003: ID 413c:818d Dell Computer Corp.
{% endhighlight %}

The device is connected to the USB bus \#3. Then check which other devices are connected to the same bus - all of them will be assigned to the same VM. Now is the time to find right USB controller:

{% highlight trac-wiki %}
readlink /sys/bus/usb/devices/usb3
{% endhighlight %}

This should output something like:

{% highlight trac-wiki %}
../../../devices/pci-0/pci0000:00/0000:00:1a.0/usb3
{% endhighlight %}

Now you see BDF address in the path (right before final usb3). Strip leading "0000:" and pass the rest to qvm-pci tool:

{% highlight trac-wiki %}
qvm-pci -a netvm 00:1a.0
{% endhighlight %}

Possible issues
---------------

### DMA buffer size

VMs with assigned PCI devices in Qubes have allocated a small buffer for DMA operations (called swiotlb). By default it is 2MB, but some devices need a larger buffer. To change this allocation, edit VM's kernel parameters (this is expressed in 512B chunks):

{% highlight trac-wiki %}
# qvm-prefs netvm |grep kernelopts
kernelopts       : iommu=soft swiotlb=2048 (default)
# qvm-prefs -s netvm kernelopts "iommu=soft swiotlb=4096"
{% endhighlight %}

This is [known to be needed](https://groups.google.com/group/qubes-devel/browse_thread/thread/631c4a3a9d1186e3) for Realtek RTL8111DL Gigabit Ethernet Controller.

### PCI passthrough issues

Sometimes PCI arbitrator is too strict. There is a way to enable permissive mode for it. Create `/etc/systemd/system/qubes-pre-netvm.service`:

{% highlight trac-wiki %}
[Unit]
Description=Netvm fixup
Before=qubes-netvm.service

[Service]
ExecStart=/bin/sh -c 'echo 0000:04:00.0 > /sys/bus/pci/drivers/pciback/permissive'
Type=oneshot
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
{% endhighlight %}

Then enable it with `systemctl enable qubes-pre-netvm.service`

See also: [https://groups.google.com/forum/\#!topic/qubes-users/Fs94QAc3vQI](https://groups.google.com/forum/#!topic/qubes-users/Fs94QAc3vQI), [http://wiki.xen.org/wiki/Xen\_PCI\_Passthrough](http://wiki.xen.org/wiki/Xen_PCI_Passthrough)

**NOTE:** By setting the permissive flag for the PCI device, you're potentially weakening the device isolation, especially if your system is not equipped with VT-d Interrupt Remapping unit -- see [this paper, page 7](http://www.invisiblethingslab.com/resources/2011/Software%20Attacks%20on%20Intel%20VT-d.pdf) for more details.

Bringing PCI device back to dom0
--------------------------------

By default device detached from some VM (or when VM with PCI device attached get shut down) isn't attached back to dom0. This is an intended feature. A device which was previously assigned to a less trusted AppVM could attack dom0 if it were automatically reassigned there. In order to re-enable the device in dom0, either:

1.  Reboot the physical machine.

or

1.  Go to the sysfs (`/sys/bus/pci`), find the right device, detach it from the pciback driver and attach back to the original driver. Replace `<BDF>` with your device, for example `00:1c.2`:

    {% highlight trac-wiki %}
    echo 0000:<BDF> > /sys/bus/pci/drivers/pciback/unbind
    MODALIAS=`cat /sys/bus/pci/devices/0000:<BDF>/modalias`
    MOD=`modprobe -R $MODALIAS | head -n 1`
    echo <BDF> > /sys/bus/pci/drivers/$MOD/bind 
    {% endhighlight %}


