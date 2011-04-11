---
layout: wiki
title: UsbInstallation
permalink: /wiki/UsbInstallation/
---

How to create a bootable USB stick from Qubes ISO
=================================================

-   download the qubes-usb-installer archive and its signature:
    -   [​http://www.qubes-os.org/files/misc/qubes-usb-installer-1.2.tgz](http://www.qubes-os.org/files/misc/qubes-usb-installer-1.2.tgz)
    -   [​http://www.qubes-os.org/files/misc/qubes-usb-installer-1.2.tgz.asc](http://www.qubes-os.org/files/misc/qubes-usb-installer-1.2.tgz.asc)

-   verify the archive signature the same way you have verified iso integrity:

    ``` {.wiki}
    gpg -v <file>.asc
    ```

-   Unpack the archive (e.g. in your home directory):

    ``` {.wiki}
    tar -zxvf qubes-usb-installer-1.2.tgz
    ```

-   "Burn" the Qubes ISO onto the USB stick:

    ``` {.wiki}
    ./qubes-usb-installer-1.2/qubes-usb-installer path_to_qubes_iso /dev/sdX
    ```

... where ```/dev/sdX``` is your USB stick. Note that all contents of the ```/dev/sdX``` device will be destroyed - be careful to pass the correct device name there (e.g. not your harddrive).
