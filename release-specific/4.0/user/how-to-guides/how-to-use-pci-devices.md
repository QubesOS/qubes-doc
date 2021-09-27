---
lang: en
release: 4.0
reviewed: yes
layout: doc
permalink: /doc/how-to-use-pci-devices/
redirect_from:
- /doc/pci-devices/
- /doc/assigning-devices/
- /en/doc/assigning-devices/
- /doc/AssigningDevices/
- /wiki/AssigningDevices/
ref: 197
title: How to use PCI devices
---

*This page is part of [device handling in qubes](/doc/how-to-use-devices/).*

**Warning:** Only dom0 exposes PCI devices.
Some of them are strictly required in dom0 (e.g., the host bridge).
You may end up with an unusable system by attaching the wrong PCI device to a VM.
PCI passthrough should be safe by default, but non-default options may be required.
Please make sure you carefully read and understand the **[security considerations](/doc/device-handling-security/#pci-security)** before deviating from default behavior.

## Introduction

Unlike other devices ([USB](/doc/how-to-use-usb-devices/), [block](/doc/how-to-use-block-storage-devices/), mic), PCI devices need to be attached on VM-bootup.
Similar to how you can't attach a new sound-card after your computer booted (and expect it to work properly), attaching PCI devices to already booted VMs isn't supported.

The Qubes installer attaches all network class controllers to `sys-net` and all USB controllers to `sys-usb` by default, if you chose to create the network and USB qube during install.
While this covers most use cases, there are some occasions when you may want to manually attach one NIC to `sys-net` and another to a custom NetVM, or have some other type of PCI controller you want to manually attach.

Some devices expose multiple functions with distinct BDF-numbers.
Limits imposed by the PC and VT-d architectures may require all functions belonging to the same device to be attached to the same VM.
This requirement can be dropped with the `no-strict-reset` option during attachment, bearing in mind the aforementioned [security considerations](/doc/device-handling-security/#pci-security).
In the steps below, you can tell if this is needed if you see the BDF for the same device listed multiple times with only the number after the "." changing.

While PCI device can only be used by one powered on VM at a time, it *is* possible to *assign* the same device to more than one VM at a time.
This means that you can use the device in one VM, shut that VM down, start up a different VM (to which the same device is now attached), then use the device in that VM.
This can be useful if, for example, you have only one USB controller, but you have multiple security domains which all require the use of different USB devices.

## Attaching Devices Using the GUI

The qube settings for a VM offers the "Devices"-tab.
There you can attach PCI-devices to a qube.

1. To reach the settings of any qube either

   - Press Alt+F3 to open the application finder, type in the VM name, select the "![appmenu](/attachment/doc/qubes-appmenu-select.png)\[VM-name\]: Qube Settings" menu entry and press enter or click "Launch"!
   - Select the VM in Qube Manager and click the settings-button or right-click the VM and select `Qube settings`.
   - Click the Domain Manager, hover the VM you want to attach a device to and select "settings" in the additional menu. (only running VMs!)

2. Select the "Devices" tab on the top bar.
3. Select a device you want to attach to the qube and click the single arrow right! (`>`)
4. You're done.
   If everything worked out, once the qube boots (or reboots if it's running) it will start with the pci device attached.
5. In case it doesn't work out, first try disabling memory-balancing in the settings ("Advanced" tab).
   If that doesn't help, read on to learn how to disable the strict reset requirement!

## `qvm-pci` Usage

The `qvm-pci` tool allows PCI attachment and detachment.
It's a shortcut for [`qvm-device pci`](/doc/how-to-use-devices/#general-qubes-device-widget-behavior-and-handling).

To figure out what device to attach, first list the available PCI devices by running (as user) in dom0:

```
qvm-pci
```

This will show you the `backend:BDF` (Bus_Device.Function) address of each PCI device.
It will look something like `dom0:00_1a.0`.
Once you've found the address of the device you want to attach, then attach it like this:

```
qvm-pci attach targetVM sourceVM:[BDF] --persistent
```

Since PCI devices have to be attached on bootup, attaching has to happen with the `--persistant` option.

For example, if `00_1a.0` is the BDF of the device you want to attach to the "work" domain, you would do this:

```
qvm-pci attach work dom0:00_1a.0 --persistent
```

## Possible Issues

Visit the [PCI Troubleshooting guide](/doc/pci-troubleshooting/) to see issues that may arise due to PCI devices and how to troubleshoot them.

## Additional Attach Options

Attaching a PCI device through the commandline offers additional options, specifiable via the `--option`/`-o` option.
(Yes, confusing wording, there's an [issue for that](https://github.com/QubesOS/qubes-issues/issues/4530).)

`qvm-pci` exposes two additional options.
Both are intended to fix device or driver specific issues, but both come with [heavy security implications](/doc/device-handling-security/#pci-security)! **Make sure you understand them before continuing!**

### no-strict-reset

Do not require PCI device to be reset before attaching it to another VM.
This may leak usage data even without malicious intent!

usage example:

```
qvm-pci a work dom0:00_1a.0 --persistent -o no-strict-reset=true
```

### permissive

Allow write access to full PCI config space instead of whitelisted registers.
This increases attack surface and possibility of [side channel attacks](https://en.wikipedia.org/wiki/Side-channel_attack).

usage example:

```
qvm-pci a work dom0:00_1a.0 --persistent -o permissive=true
```

## Bringing PCI Devices Back to dom0

By default, when a device is detached from a VM (or when a VM with an attached PCI device is shut down), the device is *not* automatically attached back to dom0.

This is an intended feature.

A device which was previously attached to a VM less trusted than dom0 (which, in Qubes, is *all* of them) could attack dom0 if it were automatically reattached there.

In order to re-enable the device in dom0, either:

- Reboot the physical machine. (Best practice)

or

- Go to the sysfs (`/sys/bus/pci`), find the right device, detach it from the pciback driver, and attach it back to the original driver.
  Replace `<BDF>` with your full device, for example `0000:00:1c.2`:

    ```
    echo <BDF> > /sys/bus/pci/drivers/pciback/unbind
    MODALIAS=`cat /sys/bus/pci/devices/<BDF>/modalias`
    MOD=`modprobe -R $MODALIAS | head -n 1`
    echo <BDF> > /sys/bus/pci/drivers/$MOD/bind
    ```

It is **strongly discouraged to reattach PCI devices to dom0**, especially if they don't support resetting!
