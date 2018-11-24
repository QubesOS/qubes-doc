---
layout: doc
title: qvm-block
permalink: /doc/tools/4.0/dom0/qvm-block/
redirect_from:
- /doc/dom0-tools/qvm-block/
- /doc/dom0-tools/qvm-block/
- /en/doc/dom0-tools/qvm-block/
- /doc/Dom0Tools/QvmBlock/
- /wiki/Dom0Tools/QvmBlock/
---

#qvm-block

##Synopsis

    qvm-block [COMMAND] [OPTIONS] <target-vm-name> <block-vm-name>:<device>

`qvm-block` is an alias for `qvm-device block`. [`qvm-device`](/doc/tools/4.0/dom0/qvm-device/) offers a generalised interface for attachment and detachment of devices (in the case of `qvm-block` block devices), only the options specific to `qvm-block` will be discussed here.

##Usage

Please follow the [`qvm-device`](/doc/tools/4.0/dom0/qvm-device/) documentation for general usage.

See also [handling USB-devices](/doc/usb/#r40) for a quick guide of the most common use-case.

##Options Specific to Block-Devices

These options can be specified using the `-o` or `--option` handle. The general syntax is

    qvm-block a -o <option=value>[ -o <option=value>[...]] <target-vm> <source-vm>:<device-id>

###frontend-dev
Specify device node in target domain.

Possible values are non-space strings.

Default is first available, starting from `xvdi`.

###read-only
Attach block-device in read-only mode. If device itself is read-only, only read-only attach is allowed.

Possible values are `True` and `False`.

Default is `False`, if read-write attachment is possible.

###devtype
Type of device

Possible Values are `disk` and `cdrom`.

Default: `disk`

##Deprecated --attach-file option
Up until Qubes 3.2, `qvm-block` exposed an option to attach a [file as block-device](/doc/tools/3.2/dom0/qvm-block/) to another VM. Qubes 4.0 does _not_ support this behavior. As a workaround, `losetup` can be used in linux VMs.

In the linux-source VM run

    sudo losetup /dev/loop0 /path/to/file

(Where `loop0` is just a generic device-id.)
Afterwards, run `qvm-block` in dom0 to list known block devices. The newly created loop-device should show up:

    ~]$ qvm-block
    BACKEND:DEVID  DESCRIPTION  USED BY
    <source-vm>:loop0 /path/to/file

You can now attach the `loop0`-device to any other vm using `qvm-block` as usual

    qvm-block a <target-vm> <source-vm>:loop0

After detaching the the device again, detach the loop-device within the source-vm:

    sudo losetup -d /dev/loop0