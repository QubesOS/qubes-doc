---
layout: wiki
title: UsbInstallation
permalink: /wiki/UsbInstallation/
---

How to create a bootable USB stick from Qubes ISO
=================================================

-   download the qubes-usb-installer archive and its signature from here FIXME; it is a bash script, so you need to run it on an existing Linux system
-   verify the archive signature the same way you have verified iso integrity
-   ` tar -zxvf qubes-usb-installer-1.2.tgz `
-   ` ./qubes-usb-installer-1.2/qubes-usb-installer path_to_qubes_iso /dev/sdX `, where /dev/sdX is your USB stick

Note that all contents of the /dev/sdX device will be destroyed - be careful to pass the correct device name there (e.g. not your harddrive).
