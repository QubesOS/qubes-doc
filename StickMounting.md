---
layout: doc
title: StickMounting
permalink: /doc/StickMounting/
redirect_from: /wiki/StickMounting/
---

How to Mount USB Sticks to AppVMs
=================================

(**Note:** In the present context, the term "USB stick" denotes any [USB mass storage device](https://en.wikipedia.org/wiki/USB_mass_storage_device_class). In addition to smaller flash memory sticks, this includes things like USB external hard drives.)

Qubes supports the ability to attach a USB stick (or just one or more of its partitions) to any AppVM easily, no matter which VM actually handles the USB controller. (The USB controller may be assigned on the **Devices** tab of an AppVM's settings page in Qubes VM Manager or by using the [qvm-pci command](/doc/AssigningDevices/).)

As of Qubes R2 Beta 3, USB stick mounting has been integrated into the Qubes VM Manger GUI. Simply insert your USB stick, right-click the desired AppVM in the Qubes VM Manager list, click **Attach/detach block devices**, and select your desired action and device. This, however, only works for the whole device. If you would like to attach individual partitions you must use the command-line tool (shown below). The reason for this is that when attaching a single partition, it used to be that Nautilus file manager would not see it and automatically mount it (see [this ticket](https://github.com/QubesOS/qubes-issues/issues/623)). This problem, however, seems to be resolved (see [this issue comment](https://github.com/QubesOS/qubes-issues/issues/1072#issuecomment-124270051)). If for some reason it does not show up in nautilus for you and you still need to attach just a single partition to a device, you will need to mount it manually; the device will show up as /dev/xvdi (or /dev/xvdj if there is already one device attached--/dev/xvdk and so on).

The command-line tool you may use to mount whole USB sticks or their partitions is `qvm-block`. This tool can be used to assign a USB stick to an AppVM as follows:

1.  Insert your USB stick.

1.  In a dom0 console (running as normal user), list all available block devices:

    {% highlight trac-wiki %}
    qvm-block -l
    {% endhighlight %}

This will list all available block devices connected to any USB controller in your system, no matter in which VM hosts the controller. The name of the VM hosting the USB controller is displayed before the colon in the device name. The string after the colon is the name of the device used within the VM.

**Note:** If your device is not listed here, you may refresh the list by calling (from the VM to which device is connected):

{% highlight trac-wiki %}
sudo udevadm trigger --action=change
{% endhighlight %}

1.  Assuming our USB stick is sdb, we attach the device to an AppVM like so:

    {% highlight trac-wiki %}
    qvm-block -a personal dom0:sdb
    {% endhighlight %}

This will attach the device as "/dev/xvdi", if not already taken by another attached device, in the AppVM. You may also mount one partition at a time by using the same command with the partition number after sdb.

**Warning: when working with single partitions, it is possible to assign the same partition to multiple VMs.** For example, you could attach sdb1 to VM1 and then sdb to VM2. It is up to the user not to make this mistake. Xen block device framework currently does not provide an easy way around this. Point 2 of [this ticket comment](https://github.com/QubesOS/qubes-issues/issues/1072#issuecomment-124119309) gives details on this.

1.  The USB stick is now attached to the AppVM. If using a default AppVM, you may open Nautilus file manager in the AppVM, and your stick should be visible in the **Devices** panel on the left.

1.  When you finish using your USB stick, click the eject button or right-click and select **Unmount**.

1.  In a dom0 console, unmount the stick:

{% highlight trac-wiki %}
qvm-block -d <device> <vmname>
{% endhighlight %}

1.  You may now remove the device.

**Warning: Do not remove the device before detatching it from the VM!** Otherwise you will not be able to attach it anywhere later. See point 3 of [this ticket comment](https://github.com/QubesOS/qubes-issues/issues/1072#issuecomment-124119309) for details.
