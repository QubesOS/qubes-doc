---
layout: doc
title: VMInterface
permalink: /doc/SystemDoc/VMInterface/
redirect_from: /wiki/SystemDoc/VMInterface/
---

VM Configuration Interface
==========================

Qubes VM have some settings set by dom0 based on VM settings. There are multiple configuration channels, which includes:

-   XenStore
-   QubesDB - replacing most of xenstore (in R3 only)
-   Qubes RPC (called at VM startup, or when configuration changed)
-   GUI protocol

xenstore
--------

Keys exposed by dom0 to VM (only Qubes specific included):

-   `qubes-vm-type` - VM type, the same as `type` field in `qvm-prefs`. One of `AppVM`, `ProxyVM`, `NetVM`, `TemplateVM`, `HVM`, `TemplateHVM`
-   `qubes-vm-updatable` - flag whether VM is updatable (whether changes in root.img will survive VM restart). One of `True`, `False`
-   `qubes-timezone - name of timezone based on dom0 timezone. For example `Europe/Warsaw`
-   `qubes-keyboard` - keyboard layout based on dom0 layout. Its syntax is suitable for `xkbcomp` command (after expanding escape sequences like `\n` or `\t`). This is meant only as some default value, VM can ignore this option and choose its own keyboard layout (this is what keyboard setting from Qubes Manager does). This entry is created as part of gui-daemon initialization (so not available when gui-daemon disabled, or not started yet).
-   `qubes-debug-mode` - flag whether VM have debug mode enabled (qvm-prefs setting). One of `1`, `0`
-   `qubes-service/SERVICE_NAME` - subtree for VM services controlled from dom0 (using qvm-service command or Qubes Manager). One of `1`, `0`. Note that not every service will be listed here, if entry is missing, it means "use VM default". List of currently supported services is in [qvm-service man page](/wiki/Dom0Tools/QvmService)
-   `qubes-netmask` - network mask (only when VM has netvm set); currently hardcoded "255.255.255.0"
-   \`qubes-ip - IP address for this VM (only when VM has netvm set)
-   `qubes-gateway` - default gateway IP and primary DNS address (only when VM has netvm set); VM should add host route to this address directly via eth0 (or whatever default interface name is)
-   `qubes-secondary-dns` - secondary DNS address (only when VM has netvm set)
-   `qubes-netvm-gateway` - same as `qubes-gateway` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM); because this is also set as primary DNS in connected VMs, traffic sent to this IP on port 53 should be redirected to DNS server
-   `qubes-netvm-netmask` - same as `qubes-netmask` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM)
-   `qubes-netvm-network` - network address (only when VM serves as network backend - ProxyVM and NetVM); can be also calculated from qubes-netvm-gateway and qubes-netvm-netmask
-   `qubes-netvm-secondary-dns` - same as `qubes-secondary-dns` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM); traffic sent to this IP on port 53 should be redirected to secondary DNS server

Keys set by VM for passing info to dom0:

-   `memory/meminfo` - used memory (updated by qubes-meminfo-writer), input information for qmemman; Format: 6 lines (EOL encoded as `\n`), each in format "FIELD: VALUE kB"; fields: `MemTotal`, `MemFree`, `Buffers`, `Cached`, `SwapTotal`, `SwapFree`; meaning the same as in `/proc/meminfo` in Linux
-   `qubes-block-devices` - list of block devices exposed by this VM, each device (subdirectory) should be named in a way that VM can attach the device based on it. Each should contain those entries:
    -   `desc` - device description (ASCII text)
    -   `size` - device size in bytes
    -   `mode` - default connection mode; `r` for read-only, `w` for read-write
-   `qubes-usb-devices` - list of USB devices exposed by this VM, each device (subdirectory) should contain:
    -   `desc` - device description (ASCII text)
    -   `usb-ver` - USB version (1, 2 or 3)

Qubes RPC
---------

Services called by dom0 to provide some VM configuration:

-   qubes.SetMonitorLayout - provide list of monitors, one in a line, each line contains four numbers: width height X Y
-   qubes.WaitForSession - called to wait for full VM startup
-   qubes.GetAppmenus - receive appmenus from given VM (template); TODO: describe format here
-   qubes.GetImageRGBA - receive image/application icon: TODO: describe format and parameters here

GUI protocol
------------

GUI initialization includes passing the whole screen dimensions from dom0 to VM. This will most likely be overwritten by qubes.SetMonitorLayout Qubes RPC call.
