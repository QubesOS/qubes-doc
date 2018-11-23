---
layout: doc
title: qvm-device
permalink: /doc/tools/4.0/dom0/qvm-device/
---

#qvm-device

##Synopsis

    qvm-device [DEVICE_CLASS] [COMMAND] <target-vm> <source-vm>:<device-id> [OPTIONS]

##Device Classes
Possible device classes are:
 - [pci](/doc/tools/4.0/dom0/qvm-pci/) (Alias for `qvm-device pci` is `qvm-pci`.)
 - [usb](/doc/tools/4.0/dom0/qvm-usb/) (Alias for `qvm-device usb` is `qvm-usb`.)
 - [block](/doc/tools/4.0/dom0/qvm-block/) (Alias for `qvm-device block` is `qvm-block`.)
 - mic
 - **?**

##Commands

###`list`, `ls`, `l`
List available devices of specified class. Output will show 

Syntax:

    qvm-device [DEVICE_CLASS] list [<source-vm>[ <source-vm>[...]]] [OPTIONS]

Optionally accepts a list of source-vms. Lists devices found in all vms if omitted.

####Command Specific Options:

#####`--all`
Used instead of source-vm list. **[Does this take precedence over a given list?]**

#####`--exclude`
Exclude list of following VMs from listing. Only valid in conjunction with `--all`. **[WHY?]**

###`attach`, `at`, `a`
Attach device of given device-id found in source-vm to target-vm.

Syntax:

    qvm-device [DEVICE_CLASS] attach <target-vm> <source-vm>:<device-id> [OPTIONS]

Requires target-vm, source-vm and device-id. The attached device will be available in target-vm. **[Will it stay available in source-vm? To what degree]**

####Command Specific Options:

#####`--option`, `-o`
Specify device-specific options (see [qvm-pci](/doc/tools/4.0/dom0/qvm-pci/) and [qvm-block](/doc/tools/4.0/dom0/qvm-block/)) using `name=value` format. Specify this option multiple times to set multiple device-specific options.

####`--persistent`, `-p`
Attach device automatically to the qube, **not tested/may be wrong** once both the source-vm and target-vm are started, even after reboot.**[What happens when source-vm doesn't expose device?]**

###`detach`, `dt`, `d`
Detach device of given device-id found in source-vm from target-vm.

Syntax:

    qvm-device [DEVICE_CLASS] detach <target-vm> <source-vm>:<device-id> [OPTIONS]

Requires target-vm, source-vm and device-id. The detached device will no longer be available in the target-vm.

##General Options
These options apply to all devices and commands.

###`--verbose`, `-v`
increase verbosity during command-completion.

###`--quiet`, `-q`
decrease verbosity during command-completion.

###`--help`, `-h`
Show help-message