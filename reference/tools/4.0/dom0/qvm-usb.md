---
layout: doc
title: qvm-usb
permalink: /doc/tools/4.0/dom0/qvm-usb/
redirect_from:
- /doc/dom0-tools/qvm-usb/
- /en/doc/dom0-tools/qvm-usb/
---

#qvm-usb

##Synopsis

    qvm-usb [COMMAND] [OPTIONS] <target-vm-name> <block-vm-name>:<device>

`qvm-usb` is an alias for `qvm-device usb`. [`qvm-device`](/doc/tools/4.0/dom0/qvm-device/) offers a generalised interface for attachment and detachment of devices (in the case of `qvm-usb` usb devices).

##Usage

Please follow the [`qvm-device`](/doc/tools/4.0/dom0/qvm-device/) documentation for general usage.

Attaching a USB-device instead of just block-devices to a VM enables non-storage applications of USB-devices, e.g. webcams, microcontroller-programming, wifi- and bluetooth dongles, etc.

##Options Specific to USB-Devices
There are no USB-specific options.