---
layout: doc
title: StickMounting
permalink: /doc/StickMounting/
redirect_from: /wiki/StickMounting/
---

How to Mount USB Sticks to AppVMs
=================================

(**Note:** In the present context, the term "USB stick" denotes any [USB mass storage device](https://en.wikipedia.org/wiki/USB_mass_storage_device_class). In addition to smaller flash memory sticks, this includes things like USB external hard drives.)

Qubes supports the ability to mount a USB stick to any AppVM easily, no matter which VM actually handles the USB controller. (The USB controller may be assigned on the **Devices** tab of an AppVM's settings page in Qubes VM Manager or by using the [qvm-pci command](/wiki/AssigningDevices).)

As of Qubes R2 Beta 3, USB stick mounting has been integrated into the Qubes VM Manger GUI. Simply insert your USB stick, right-click the desired AppVM in the Qubes VM Manager list, click **Attach/detach block devices**, and select your desired action and device.

A command-line tool, `qvm-block`, is also available. This tool can be used to assign a USB stick to an AppVM as follows:

1.  Insert your USB stick.

1.  In a dom0 console (running as normal user), list all available block devices:

    {% highlight trac-wiki %}
    qvm-block -l
    {% endhighlight %}

> This will list all available block devices connected to any USB controller in your system, no matter in which VM hosts the controller. The name of the VM hosting the USB controller is displayed before the colon in the device name. The string after the colon is the name of the device used within the VM.

> **Note:** If your device is not listed here, you may refresh the list by calling (from the VM to which device is connected):
>
> {% highlight trac-wiki %}
> sudo udevadm trigger --action=change
> {% endhighlight %}

1.  Connect the device to an AppVM:

    {% highlight trac-wiki %}
    qvm-block -a personal dom0:sda
    {% endhighlight %}

    **Note:** The order of these parameters was changed in Qubes 1.0-rc1.

> This will attach the device as "/dev/xvdi" in the AppVM.

1.  The USB stick is now attached to the AppVM. If using a default AppVM, you may open Nautilus file manager in the AppVM, and your stick should be visible in the **Devices** panel on the left.

1.  When you finish using your USB stick, click the eject button or right-click and select **Unmount**.

1.  In a dom0 console, unmount the stick:

{% highlight trac-wiki %}
qvm-block -d <device> <vmname>
{% endhighlight %}

1.  You may now remove the device.

