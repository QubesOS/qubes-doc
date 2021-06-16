---
lang: en
layout: doc
redirect_from:
- /doc/vm-interface/
- /en/doc/vm-interface/
- /doc/VMInterface/
- /doc/SystemDoc/VMInterface/
- /wiki/SystemDoc/VMInterface/
ref: 47
---

# VM Configuration Interface

Qubes VM have some settings set by dom0 based on VM settings. There are multiple configuration channels, which includes:

- QubesDB
- XenStore (in Qubes 2, data the same as in QubesDB, keys without leading `/`)
- Qubes RPC (called at VM startup, or when configuration changed)
- GUI protocol

## QubesDB

### Keys exposed by dom0 to VM

- `/qubes-vm-type` - VM type, the same as `type` field in `qvm-prefs`. One of `AppVM`, `ProxyVM`, `NetVM`, `TemplateVM`, `HVM`, `TemplateHVM`
- `/qubes-vm-updatable` - flag whether VM is updatable (whether changes in root.img will survive VM restart). One of `True`, `False`
- `/qubes-vm-persistence` - what data do persist between VM restarts:
  - `full` - all disks
  - `rw-only` - only `/rw` disk
  - `none` - none
- `/qubes-timezone - name of timezone based on dom0 timezone. For example `Europe/Warsaw`
- `/qubes-keyboard` (deprecated in R4.1) - keyboard layout based on dom0 layout. Its syntax is suitable for `xkbcomp` command (after expanding escape sequences like `\n` or `\t`). This is meant only as some default value, VM can ignore this option and choose its own keyboard layout (this is what keyboard setting from Qubes Manager does). This entry is created as part of gui-daemon initialization (so not available when gui-daemon disabled, or not started yet).
- `/keyboard-layout` - keyboard layout based on GuiVM layout. Its syntax can be `layout+variant+options`, `layout+variant`, `layout++options` or simply `layout`. For example, `fr+oss`, `pl++compose:caps` or `fr`. This is meant only as some default value, VM can ignore this option and choose its own keyboard layout (this is what keyboard setting from Qubes Manager does).
- `/qubes-debug-mode` - flag whether VM has debug mode enabled (qvm-prefs setting). One of `1`, `0`
- `/qubes-service/SERVICE_NAME` - subtree for VM services controlled from dom0 (using the `qvm-service` command or Qubes Manager). One of `1`, `0`. Note that not every service will be listed here, if entry is missing, it means "use VM default". A list of currently supported services is in the `qvm-service` man page.
- `/qubes-netmask` - network mask (only when VM has netvm set); currently hardcoded "255.255.255.0"
- `/qubes-ip - IP address for this VM (only when VM has netvm set)
- `/qubes-gateway` - default gateway IP (only when VM has netvm set); VM should add host route to this address directly via eth0 (or whatever default interface name is)
- `/qubes-primary-dns` - primary DNS address (only when VM has netvm set)
- `/qubes-secondary-dns` - secondary DNS address (only when VM has netvm set)
- `/qubes-netvm-gateway` - same as `qubes-gateway` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM)
- `/qubes-netvm-netmask` - same as `qubes-netmask` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM)
- `/qubes-netvm-network` - network address (only when VM serves as network backend - ProxyVM and NetVM); can be also calculated from qubes-netvm-gateway and qubes-netvm-netmask
- `/qubes-netvm-primary-dns` - same as `qubes-primary-dns` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM); traffic sent to this IP on port 53 should be redirected to primary DNS server
- `/qubes-netvm-secondary-dns` - same as `qubes-secondary-dns` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM); traffic sent to this IP on port 53 should be redirected to secondary DNS server
- `/guivm-windows-prefix` - title prefix for any window not originating from another qube. This means windows of applications running in GuiVM itself

#### Firewall rules in 3.x

QubesDB is also used to configure firewall in ProxyVMs. Rules are stored in
separate key for each target VM. Entries:

- `/qubes-iptables` - control entry - dom0 writing `reload` here signals `qubes-firewall` service to reload rules
- `/qubes-iptables-header` - rules not related to any particular VM, should be applied before domains rules
- `/qubes-iptables-domainrules/NNN` - rules for domain `NNN` (arbitrary number)
in `iptables-save` format. Rules are self-contained - fill `FORWARD` iptables
chain and contains all required matches (source IP address etc), as well as
final default action (`DROP`/`ACCEPT`)

VM after applying rules may signal some error, writing a message to
`/qubes-iptables-error` key. This does not exclude any other way of
communicating problems - like a popup.

#### Firewall rules in 4.x

QubesDB is also used to configure firewall in ProxyVMs. Each rule is stored as
a separate entry, grouped on target VM:

- `/qubes-firewall/SOURCE_IP` - base tree under which rules are placed. All
rules there should be applied to filter traffic coming from `SOURCE_IP`. This
can be either IPv4 or IPv6 address.
Dom0 will do an empty write to this top level entry after finishing rules
update, so VM can setup a watch here to trigger rules reload.
- `/qubes-firewall/SOURCE_IP/policy` - default action if no rule matches:
`drop` or `accept`.
- `/qubes-firewall/SOURCE_IP/NNNN` - rule number `NNNN` - decimal number,
    padded with zeros. Se below for rule format. All the rules should be
    applied in order of rules implied by those numbers. Note that QubesDB
    itself does not impose any ordering (you need to sort the rules after
    retrieving them). The first rule has number `0000`.

Each rule is a single QubesDB entry, consisting of pairs `key=value` separated
by space. QubesDB enforces limit on a single entry length - 3072 bytes.
Possible options for a single rule:

- `action`, values: `accept`, `drop`; this is present in every rule
- `dst4`, value: destination IPv4 address with a mask; for example: `192.168.0.0/24`
- `dst6`, value: destination IPv6 address with a mask; for example: `2000::/3`
- `dsthost`, value: DNS hostname of destination host
- `proto`, values: `tcp`, `udp`, `icmp`
- `specialtarget`, value: One of predefined target, currently defined values:
  - `dns` - such option should match DNS traffic to default DNS server (but
      not any DNS server), on both TCP and UDP
- `dstports`, value: destination ports range separated with `-`, valid only
 together with `proto=tcp` or `proto=udp`; for example `1-1024`, `80-80`
- `icmptype`, value: numeric (decimal) icmp message type, for example `8` for
 echo request, valid only together with `proto=icmp`
- `dpi`, value: Deep Packet Inspection protocol (like: HTTP, SSL, SMB, SSH, SMTP) or the default 'NO' as no DPI, only  packet filtering

Options must appear in the rule in the order listed above. Duplicated options
are forbidden.

A rule matches only when all predicates match. Only one of `dst4`, `dst6` or
`dsthost` can be used in a single rule.

If tool applying firewall encounters any parse error (unknown option, invalid
value, duplicated option, etc), it should drop all the traffic coming from that `SOURCE_IP`,
regardless of properly parsed rules.

Example valid rules:

- `action=accept dst4=8.8.8.8 proto=udp dstports=53-53`
- `action=drop dst6=2a00:1450:4000::/37 proto=tcp`
- `action=accept specialtarget=dns`
- `action=drop proto=tcp specialtarget=dns` - drop DNS queries sent using TCP
- `action=drop`

### Keys set by VM for passing info to dom0

- `memory/meminfo` (**xenstore**) - used memory (updated by qubes-meminfo-writer), input information for qmemman;
  - Qubes 3.x format: 6 lines (EOL encoded as `\n`), each in format "FIELD: VALUE kB"; fields: `MemTotal`, `MemFree`, `Buffers`, `Cached`, `SwapTotal`, `SwapFree`; meaning the same as in `/proc/meminfo` in Linux.
  - Qubes 4.0+ format: used memory size in the VM, in kbytes
- `/qubes-block-devices` - list of block devices exposed by this VM, each device (subdirectory) should be named in a way that VM can attach the device based on it. Each should contain these entries:
  - `desc` - device description (ASCII text)
  - `size` - device size in bytes
  - `mode` - default connection mode; `r` for read-only, `w` for read-write
- `/qubes-usb-devices` - list of USB devices exposed by this VM, each device (subdirectory) should contain:
  - `desc` - device description (ASCII text)
  - `usb-ver` - USB version (1, 2 or 3)

## Qubes RPC

Services called by dom0 to provide some VM configuration:

- `qubes.SetMonitorLayout` - provide list of monitors, one per line. Each line contains four numbers: `width height X Y width_mm height_mm` (physical dimensions - `width_mm` and `height_mm` - are optional)
- `qubes.WaitForSession` - called to wait for full VM startup
- `qubes.GetAppmenus` - receive appmenus from given VM (template); TODO: describe format here
- `qubes.GetImageRGBA` - receive image/application icon. Protocol:

  1. Caller sends name of requested icon. This can be one of:
    * `xdgicon:NAME` - search for NAME in standard icons theme
    * `-` - get icon data from stdin (the caller), can be prefixed with format name, for example `png:-`
    * file name
  2. The service responds with image dimensions: width and height as
     decimal numbers, separated with space and with EOL marker at the and; then
     image data in RGBA format (32 bits per pixel)
- `qubes.SetDateTime` - set VM time, called periodically by dom0 (can be
    triggered manually from dom0 by calling `qvm-sync-clock`). The service
    receives one line at stdin - time in format of `date -u -Iseconds`, for
    example `2015-07-31T16:10:43+0000`.
- `qubes.SetGuiMode` - called in HVM to switch between fullscreen and seamless
    GUI mode. The service receives a single word on stdin - either `FULLSCREEN`
    or `SEAMLESS`
- `qubes.ResizeDisk` - called to inform that underlying disk was resized.
    Name of disk image is passed on standard input (`root`, `private`, `volatile`,
    or other). This is used starting with Qubes 4.0.

Other Qrexec services installed by default:

- `qubes.Backup` - store Qubes backup. The service receives location chosen by
  the user (one line, terminated by `\n`), the backup archive ([description of
  backup format](/doc/BackupEmergencyRestoreV2/))
- `qubes.DetachPciDevice` - service called in reaction to `qvm-pci -d` call on
  running VM. The service receives one word - BDF of device to detach. When the
  service call ends, the device will be detached
- `qubes.Filecopy` - receive some files from other VM. Files sent in [qfile format](/doc/qfilecopy/)
- `qubes.OpenInVM` - open a file in called VM. Service receives a single file on stdin (in
  [qfile format](/doc/qfilecopy/). After a file viewer/editor is terminated, if
  the file was modified, can be sent back (just raw content, without any
  headers); otherwise service should just terminate without sending anything.
  This service is used by both `qvm-open-in-vm` and `qvm-open-in-dvm` tools. When
  called in DispVM, service termination will trigger DispVM cleanup.
- `qubes.Restore` - retrieve Qubes backup. The service receives backup location
  entered by the user (one line, terminated by `\n`), then should output backup
  archive in [qfile format](/doc/qfilecopy/) (core-agent-linux component contains
  `tar2qfile` utility to do the conversion)
- `qubes.SelectDirectory`, `qubes.SelectFile` - services which should show
  file/directory selection dialog and return (to stdout) a single line
  containing selected path, or nothing in the case of cancellation
- `qubes.SuspendPre` - service called in every VM with PCI device attached just
  before system suspend
- `qubes.SuspendPost` - service called in every VM with PCI device attached just
  after system resume
- `qubes.SyncNtpClock` - service called to trigger network time synchronization.
  Service should synchronize local VM time and terminate when done.
- `qubes.WindowIconUpdater` - service called by VM to send icons of individual
  windows. The protocol there is simple one direction stream: VM sends window ID
  followed by icon in `qubes.GetImageRGBA` format, then next window ID etc. VM
  can send icon for the same window multiple times to replace previous one (for
  example for animated icons)
- `qubes.VMShell` - call any command in the VM; the command(s) is passed one per line
  - `qubes.VMShell+WaitForSession` waits for full VM startup first
- `qubes.VMExec` - call any command in the VM, without using shell, the command
  needs to be passed as argument and encoded as follows:
  - the executable name and arguments are separated by `+`
  - everything except alphanumeric characters, `.` and `_` needs to be
      escaped
  - bytes are escaped as `-HH` (where `HH` is hex code, capital letters only)
  - `-` itself can be escaped as `--`
  - example: to run `ls -a /home/user`, use
      `qubes.VMExec+ls+--a+-2Fhome-2Fuser`
- `qubes.VMExecGUI` - a variant of `qubes.VMExec` that waits for full VM
  startup first

Services called in GuiVM:

- `policy.Ask`, `policy.Notify` - confirmation prompt and notifications for
Qubes RPC calls, see [qrexec-policy implementation](/doc/qrexec-internals/#qrexec-policy-implementation)
for a detailed description.

Currently Qubes still calls few tools in VM directly, not using service
abstraction. This will change in the future. Those tools are:

- `/usr/lib/qubes/qubes-download-dom0-updates.sh` - script to download updates (or new packages to be installed) for dom0 (`qubes-dom0-update` tool)
- `date -u -Iseconds` - called directly to retrieve time after calling `qubes.SyncNtpClock` service (`qvm-sync-clock` tool)
- `nm-online -x` - called before `qubes.SyncNtpClock` service call by `qvm-sync-clock` tool
- `resize2fs` - called to resize filesystem on /rw partition by `qvm-grow-private` tool
- `gpk-update-viewer` - called by Qubes Manager to display available updates in a TemplateVM
- `systemctl start qubes-update-check.timer` (and similarly stop) - called when enabling/disabling updates checking in given VM (`qubes-update-check` [qvm-service](/doc/qubes-service/))

Additionally, automatic tests extensively run various commands directly in VMs. We do not plan to change that.

## GUI protocol

GUI initialization includes passing the whole screen dimensions from dom0 to VM. This will most likely be overwritten by qubes.SetMonitorLayout Qubes RPC call.
