---
lang: en
layout: doc
permalink: /doc/4.0/4.0/how-to-use-devices/
redirect_from:
- /doc/device-handling/
- /doc/external-device-mount-point/
- /en/doc/external-device-mount-point/
- /doc/ExternalDeviceMountPoint/
- /wiki/ExternalDeviceMountPoint/
ref: 188
title: How to use devices
---

This is an overview of device handling in Qubes OS.
For specific devices ([block](/doc/how-to-use-block-storage-devices/), [USB](/doc/how-to-use-usb-devices/) and [PCI](/doc/how-to-use-pci-devices/) devices), please visit their respective pages.

**Important security warning:** Device handling comes with many security implications.
Please make sure you carefully read and understand the **[security considerations](/doc/device-handling-security/)**.


## Introduction ##

The interface to deal with devices of all sorts was unified in Qubes 4.0 with the `qvm-device` command and the Qubes Devices Widget.
In Qubes 3.X, the Qubes VM Manager dealt with attachment as well.
This functionality was moved to the Qubes Device Widget, the tool tray icon with a yellow square located in the top right of your screen by default.

There are currently four categories of devices Qubes understands:
 - Microphones
 - Block devices
 - USB devices
 - PCI devices

Microphones, block devices and USB devices can be attached with the GUI-tool.
PCI devices can be attached using the Qube Settings, but require a VM reboot.


## General Qubes Device Widget Behavior And Handling ##

When clicking on the tray icon (which looks similar to this): ![SD card and thumbdrive](/attachment/doc/media-removable.png) several device-classes separated by lines are displayed as tooltip.
Block devices are displayed on top, microphones one below and USB-devices at the bottom.

On most laptops, integrated hardware such as cameras and fingerprint-readers are implemented as USB-devices and can be found here.


### Attaching Using The Widget ###

Click the tray icon.
Hover on a device you want to attach to a VM.
A list of running VMs (except dom0) appears.
Click on one and your device will be attached!


### Detaching Using The Widget ###

To detach a device, click the Qubes Devices Widget icon again.
Attached devices are displayed in bold.
Hover the one you want to detach.
A list of VMs appears, one showing the eject symbol: ![eject icon](/attachment/doc/media-eject.png)


### Attaching a Device to Several VMs ###

Only `mic` should be attached to more than one running VM.
You may *assign* a device to more than one VM (using the `--persistent` option), however, only one of them can be started at the same time.

But be careful: There is a [bug in `qvm-device block` or `qvm-block`](https://github.com/QubesOS/qubes-issues/issues/4692) which will allow you to *attach* a block device to two running VMs.
Don't do that!


## General `qvm-device` Command Line Tool Behavior ##

All devices, including PCI-devices, may be attached from the commandline using the `qvm-device`-tools.


### Device Classes ###

`qvm-device` expects DEVICE_CLASS as first argument.
DEVICE_CLASS can be one of

 - `pci`
 - `usb`
 - `block`
 - `mic`


### Actions ###

`qvm-device` supports three actions:

 - `list` (ls, l) - list all devices of DEVICE_CLASS
 - `attach` (at, a) - attach a specific device of DEVICE_CLASS
 - `detach` (dt, d) - detach a specific device of DEVICE_CLASS


### Global Options ###

These three options are always available:

- `--help`, `-h` - show help message and exit
- `--verbose`, `-v` - increase verbosity
- `--quiet`, `-q` - decrease verbosity

A full command consists of one DEVICE_CLASS and one action.
If no action is given, list is implied.
DEVICE_CLASS however is required.

**SYNOPSIS**:
`qvm-device DEVICE_CLASS {action} [action-specific arguments] [options]`

## Actions

Actions are applicable to every DEVICE_CLASS and expose some additional options.

### Listing Devices

The `list` action lists known devices in the system.
`list` accepts VM-names to narrow down listed devices.
Devices available in, as well as attached to the named VMs will be listed.

`list` accepts two options:

- `--all` - equivalent to specifying every VM name after `list`.
No VM-name implies `--all`.
- `--exclude` - exclude VMs from `--all`.
Requires `--all`.

**SYNOPSIS**
`qvm-device DEVICE_CLASS {list|ls|l} [--all [--exclude VM [VM [...]]] | VM [VM [...]]]`

### Attaching Devices

The `attach` action assigns an exposed device to a VM.
This makes the device available in the VM it's attached to.
Required argument are targetVM and sourceVM:deviceID.
(sourceVM:deviceID can be determined from `list` output)

`attach` accepts two options:

- `--persistent` - attach device on targetVM-boot.
If the device is unavailable (physically missing or sourceVM not started), booting the targetVM fails.
- `--option`, `-o` - set additional options specific to DEVICE_CLASS.

**SYNOPSIS**
`qvm-device DEVICE_CLASS {attach|at|a} targetVM sourceVM:deviceID [options]`

### Detaching Devices

The `detach` action removes an assigned device from a targetVM.
It won't be available afterwards anymore.
Though it tries to do so gracefully, beware that data-connections might be broken unexpectedly, so close any transaction before detaching a device!

If no specific `sourceVM:deviceID` combination is given, *all devices of that DEVICE_CLASS will be detached.*

`detach` accepts no options.

**SYNOPSIS**
`qvm-device DEVICE_CLASS {detach|dt|d} targetVM [sourceVM:deviceID]`
