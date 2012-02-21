---
layout: wiki
title: StickMounting
permalink: /wiki/StickMounting/
---

In Qubes Beta 3 a new tool, ```qvm-block``` has been introduced that makes mounting USB devices to any user AppVM very easy, no matter which actual VM is handling the USB controller (those can be assigned using the [qvm-pci command](/wiki/AssigningDevices)).

In order to assign a USB disk to a VM, follow these steps:

1.  Insert your USB stick.

1.  In Dom0 konsole (running as normal user) do:

    ``` {.wiki}
    qvm-block -l
    ```

> This will list available block devices connected to any USB controller in your system, no matter in which VM this controller is hosted. The name of the VM hosting the USB controller is displayed before the colon in the device name. The string after the colon is the name of the device used within the VM.

> NOTE: If your device is not listed here, you can refresh the list calling (from VM to which device is connected):
>
> ``` {.wiki}
> sudo udevadm trigger
> ```

1.  Connect the device, e.g.:

    ``` {.wiki}
    qvm-block -a dom0:sda personal
    ```

> This will attach the device as "/dev/xvdi" in VM.

1.  Open Nautilus file manager in the AppVM. Your stick should be visible in the "Places" panel on the left. Just click on the device.

1.  When you finish using your USB stick, right-click its icon in Dolphin and chose "Safely Remove \<Your stick name\>".

1.  Back to Dom0 konsole -- in order to unmount the stick do the following:

``` {.wiki}
qvm-block -d <device> <vmname>
```

1.  You can remove the device.

> In the next release this will get integrated into the Qubes GUI manager...
