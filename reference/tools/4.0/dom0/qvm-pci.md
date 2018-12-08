---
layout: doc
title: qvm-pci
permalink: /doc/tools/4.0/dom0/qvm-pci/
redirect_from:
- /doc/dom0-tools/qvm-pci/
- /en/doc/dom0-tools/qvm-pci/
- /doc/Dom0Tools/QvmPci/
- /wiki/Dom0Tools/QvmPci/
---

#qvm-pci

##Synopsis

    qvm-pci [COMMAND] [OPTIONS] <target-vm-name> <block-vm-name>:<device>

`qvm-pci` is an alias for `qvm-device usb`. [`qvm-device`](/doc/tools/4.0/dom0/qvm-device/) offers a generalised interface for attachment and detachment of devices (in the case of `qvm-pci` usb devices).

##Usage

**BEWARE:** Only dom0 exposes PCI-devices and some, like host bridge, are strictly required to stay in dom0.
Move ahead if you know what your doing and/or this documentation specifically called for it.

Please follow the [`qvm-device`](/doc/tools/4.0/dom0/qvm-device/) documentation for general usage.

See also [assigning PCI-devices](/doc/assigning-devices/#r40) for a quick guide of the most common use-case.


##Options Specific to PCI-Devices

These options can be specified using the `-o` or `--option` handle. The general syntax is

    qvm-pci a -o <option=value>[ -o <option=value>[...]] <target-vm> dom0:<device-id>

###no-strict-reset
Allow attaching device even if no reliable reset-method is supported.
Switching non-resettable devices poses a security risk, as VM-isolation is weakened.

Possible values are `True` and `False`.

Default value is `False`.

###permissive
Allow write access to most of PCI config space, instead of only selected whitelisted registers.
A workaround for some PCI passthrough problems, potentially unsafe though!


Possible values are `True` and `False`.

Default value is `False`.