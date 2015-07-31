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

-   `qubes.SetMonitorLayout` - provide list of monitors, one in a line, each line contains four numbers: `width height X Y`
-   `qubes.WaitForSession` - called to wait for full VM startup
-   `qubes.GetAppmenus` - receive appmenus from given VM (template); TODO: describe format here
-   `qubes.GetImageRGBA` - receive image/application icon: TODO: describe format and parameters here
-   `qubes.SetDateTime` - set VM time, called periodically by dom0 (can be
    triggered manually from dom0 by calling `qvm-sync-clock`). The service
    receives one line at stdin - time in format of `date -u -Iseconds`, for
    example `2015-07-31T16:10:43+0000`.
-   `qubes.SetGuiMode` - called in HVM to switch between fullscreen and seamless
    GUI mode. The service receives a single word on stdin - either `FULLSCREEN`
    or `SEAMLESS`


Other Qrexec services installed by default:

- `qubes.Backup` - store Qubes backup. The service receives location chosen by
  the user (one line, terminated by '\n'), the backup archive ([description of
  backup format](/doc/BackupEmergencyRestoreV2/))
- `qubes.DetachPciDevice` - service called in reaction to `qvm-pci -d` call on
  running VM. The service receives one word - BDF of device to detach. When the
  service call ends, the device will be detached
- `qubes.Filecopy` - receive some files from other VM. Files sent in [qfile format](/doc/Qfilecopy/)
- `qubes.OpenInVM` - open a file in called VM. Service receives a single file on stdin (in
  [qfile format](/doc/Qfilecopy/). After a file viewer/editor is terminated, if
  the file was modified, can be sent back (just raw content, without any
  headers); otherwise service should just terminate without sending anything.
  This service is used by both `qvm-open-in-vm` and `qvm-open-in-dvm` tools. When
  called in DispVM, service termination will trigger DispVM cleanup.
- `qubes.Restore` - retrieve Qubes backup. The service receives backup location
  entered by the user (one line, terminated by '\n'), then should output backup
  archive in [qfile format](/doc/Qfilecopy/) (core-agent-linux component contains
  `tar2qfile` utility to do the conversion
- `qubes.SelectDirectory`, `qubes.SelectFile` - services which should show
  file/directory selection dialog and return (to stdout) a single line
  containing selected path, or nothing in case of cancellation
- `qubes.SuspendPre` - service called in every VM with PCI device attached just
  before system suspend
- `qubes.SuspendPost` - service called in every VM with PCI device attached just
  after system resume
- `qubes.SyncNtpClock` - service called to trigger network time synchronization.
  Service should synchronize local VM time and terminate when done.
- `qubes.VMShell` - call any command in the VM; the command(s) is passed one per line

Currently Qubes still calls few tools in VM directly, not using service
abstraction. This will change in the future. Those tools are:

- `/usr/lib/qubes/qubes-download-dom0-updates.sh` - script to download updates (or new packages to be installed) for dom0 (`qubes-dom0-update` tool)
- `date -u -Iseconds` - called directly to retrieve time after calling `qubes.SyncNtpClock` service (`qvm-sync-clock` tool)
- `nm-online -x` - called before `qubes.SyncNtpClock` service call by `qvm-sync-clock` tool
- `resize2fs` - called to resize filesystem on /rw partition by `qvm-grow-private` tool
- `gpk-update-viewer` - called by Qubes Manager to display available updates in a TemplateVM
- `systemctl start qubes-update-check.timer` (and similarly stop) - called when enabling/disabling updates checking in given VM (`qubes-update-check` [qvm-service](/doc/QubesService/))

Additionally automatic tests extensively calls various commands directly in VMs. We do not plan to change that.

GUI protocol
------------

GUI initialization includes passing the whole screen dimensions from dom0 to VM. This will most likely be overwritten by qubes.SetMonitorLayout Qubes RPC call.
