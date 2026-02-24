============================
Qube configuration interface
============================


Qubes VMs have some settings set by dom0 based on that VM's settings. There are multiple configuration channels, including:

- QubesDB

- XenStore (in Qubes 2, data the same as in QubesDB, keys without leading ``/``)

- Qubes RPC (called at VM startup, or when configuration changed)

- GUI protocol



QubesDB
-------


Keys exposed by dom0 to VM
^^^^^^^^^^^^^^^^^^^^^^^^^^


- ``/qubes-base-template`` - base template

- ``/qubes-vm-type`` - VM type, the same as the ``type`` field in ``qvm-prefs``. One of ``AppVM``, ``ProxyVM``, ``NetVM``, ``TemplateVM``, ``HVM``, ``TemplateHVM``

- ``/qubes-vm-updatable`` - flag indicating whether the VM is updatable (whether changes in root.img will survive VM restart). One of ``True``, ``False``

- ``/qubes-vm-persistence`` - what data do persist between VM restarts:

  - ``full`` - all disks

  - ``rw-only`` - only ``/rw`` disk

  - ``none`` - nothing



- ``/qubes-timezone`` - name of timezone based on dom0's timezone. Example: ``Europe/Warsaw``

- ``/qubes-keyboard`` (deprecated in R4.1) - keyboard layout based on dom0's layout. Its syntax is suitable for the ``xkbcomp`` command (after expanding escape sequences like ``\n`` or ``\t``). This is meant only as some default value, the VM can ignore this option and choose its own keyboard layout (this is what the keyboard setting in Qubes Manager does). This entry is created as part of gui-daemon initialization (it's not available when gui-daemon is disabled, or has not started yet).

- ``/keyboard-layout`` - keyboard layout based on the GuiVM's layout. The key's syntax can be ``layout+variant+options``, ``layout+variant``, ``layout++options`` or simply ``layout``. Example, ``fr+oss``, ``pl++compose:caps`` or ``fr``. This is meant only as some default value, the VM can ignore this option and choose its own keyboard layout (this is what the keyboard setting in Qubes Manager does).

- ``/qubes-debug-mode`` - flag indicating whether the VM has debug mode enabled (qvm-prefs setting). One of ``1``, ``0``

- ``/qubes-service/SERVICE_NAME`` - subtree for VM services controlled from dom0 (using the ``qvm-service`` command or Qubes Manager). One of ``1``, ``0``. Note that not every service will be listed here, if an entry is missing, it means “use VM default”. A list of currently supported services can be found in the ``qvm-service`` man page.

- ``/qubes-netmask`` - network mask (only when the VM has a netvm set); currently hardcoded “255.255.255.0”

- ``/qubes-ip`` - IP address for this VM (only when the VM has a netvm set)

- ``/qubes-gateway`` - the default gateway's IP address (only when the VM has a netvm set); VM should add a host route to this address directly via eth0 (or whatever the default interface name is)

- ``/qubes-primary-dns`` - primary DNS address (only when the VM has a netvm set)

- ``/qubes-secondary-dns`` - secondary DNS address (only when the VM has a netvm set)

- ``/qubes-netvm-gateway`` - same as ``qubes-gateway`` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM)

- ``/qubes-netvm-netmask`` - same as ``qubes-netmask`` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM)

- ``/qubes-netvm-network`` - network address (only when VM serves as network backend - ProxyVM and NetVM); can be also calculated from qubes-netvm-gateway and qubes-netvm-netmask

- ``/qubes-netvm-primary-dns`` - same as ``qubes-primary-dns`` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM); traffic sent to this IP on port 53 should be redirected to the primary DNS server

- ``/qubes-netvm-secondary-dns`` - same as ``qubes-secondary-dns`` in connected VMs (only when VM serves as network backend - ProxyVM and NetVM); traffic sent to this IP on port 53 should be redirected to the secondary DNS server

- ``/guivm-windows-prefix`` - title prefix for any window not originating from another qube. This means windows of applications running in the GuiVM itself



Firewall rules in 3.x
^^^^^^^^^^^^^^^^^^^^^


QubesDB is also used to configure the firewall in ProxyVMs. Rules are stored in separate keys for each target VM. Entries:

- ``/qubes-iptables`` - control entry - dom0 writing ``reload`` here signals the ``qubes-firewall`` service to reload rules

- ``/qubes-iptables-header`` - rules not related to any particular VM, should be applied before domain rules

- ``/qubes-iptables-domainrules/NNN`` - rules for domain ``NNN`` (arbitrary number) in ``iptables-save`` format. Rules are self-contained - they fill ``FORWARD`` iptables chain and contain all required matches (source IP address etc.), as well as a final default action (``DROP``/``ACCEPT``)



After applying the rules, the VM may signal some error, writing a message to the ``/qubes-iptables-error`` key. This does not preclude any other way of communicating problems, such as with a popup.

Firewall rules in 4.x
^^^^^^^^^^^^^^^^^^^^^


QubesDB is also used to configure the firewall in ProxyVMs. Each rule is stored as a separate entry, grouped by target VMs:

- ``/qubes-firewall/SOURCE_IP`` - base tree under which rules are placed. All rules there should be applied to filter traffic coming from ``SOURCE_IP``. This can be either an IPv4 or IPv6 address. Dom0 will do an empty write to this top level entry after finishing an update of the rules, so the VM can setup a watch here to trigger rules reload.

- ``/qubes-firewall/SOURCE_IP/policy`` - default action if no rule matches: ``drop`` or ``accept``.

- ``/qubes-firewall/SOURCE_IP/NNNN`` - rule number ``NNNN`` - decimal number, padded with zeros. See below for rule format. All the rules should be applied in the order of rules implied by those numbers. Note that QubesDB itself does not impose any ordering (you need to sort the rules after retrieving them). The first rule has the number ``0000``.



Each rule is a single QubesDB entry, consisting of ``key=value`` pairs separated by a space. QubesDB enforces a limit on a single entry's length - 3072 bytes. Possible options for a single rule:

- ``action``, values: ``accept``, ``drop``; this is present in every rule

- ``dst4``, value: destination IPv4 address with a mask; for example: ``192.168.0.0/24``

- ``dst6``, value: destination IPv6 address with a mask; for example: ``2000::/3``

- ``dsthost``, value: DNS hostname of the destination host

- ``proto``, values: ``tcp``, ``udp``, ``icmp``

- ``specialtarget``, value: One of predefined target, currently defined values:

  - ``dns`` - such option should match DNS traffic to default DNS server (but not any DNS server), on both TCP and UDP



- ``dstports``, value: destination ports range separated with ``-``, valid only together with ``proto=tcp`` or ``proto=udp``; for example ``1-1024``, ``80-80``

- ``icmptype``, value: numeric (decimal) icmp message type, for example ``8`` for echo request, valid only together with ``proto=icmp``

- ``dpi``, value: Deep Packet Inspection protocol (like: HTTP, SSL, SMB, SSH, SMTP) or the default ‘NO’ as no DPI, only packet filtering



Options must appear in the rule in the order listed above. Duplicated options are forbidden.

A rule matches only when all predicates match. Only one of ``dst4``, ``dst6`` or ``dsthost`` can be used in a single rule.

If the tool applying firewall rules encounters any parsing errors (unknown option, invalid value, duplicated option, etc.), it should drop all the traffic coming from that ``SOURCE_IP``, regardless of properly parsed rules.

Example valid rules:

- ``action=accept dst4=8.8.8.8 proto=udp dstports=53-53``

- ``action=drop dst6=2a00:1450:4000::/37 proto=tcp``

- ``action=accept specialtarget=dns``

- ``action=drop proto=tcp specialtarget=dns`` - drop DNS queries sent using TCP

- ``action=drop``



Keys set by VM for passing info to dom0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


- ``memory/meminfo`` (**xenstore**) - used memory (updated by qubes-meminfo-writer), input information for qmemman;

  - Qubes 3.x format: 6 lines (EOL encoded as ``\n``), each in the format “FIELD: VALUE kB”; fields: ``MemTotal``, ``MemFree``, ``Buffers``, ``Cached``, ``SwapTotal``, ``SwapFree``; meaning the same as in ``/proc/meminfo`` on Linux.

  - Qubes 4.0+ format: used memory size in the VM, in kbytes



- ``/qubes-block-devices`` - list of block devices exposed by this VM, each device (subdirectory) should be named in a way that VM can attach the device based on the name. Each should contain these entries:

  - ``desc`` - device description (ASCII text)

  - ``size`` - device size in bytes

  - ``mode`` - default connection mode; ``r`` for read-only, ``w`` for read-write



- ``/qubes-usb-devices`` - list of USB devices exposed by this VM, each device (subdirectory) should contain:

  - ``desc`` - device description (ASCII text)

  - ``usb-ver`` - USB version (1, 2 or 3)





Qubes RPC
---------


Services called by dom0 to provide some VM configuration:

- ``qubes.SetMonitorLayout`` - provide a list of monitors (displays), one per line. Each line contains four numbers: ``width height X Y width_mm height_mm`` (physical dimensions - ``width_mm`` and ``height_mm`` - are optional)

- ``qubes.WaitForSession`` - called to wait for full VM startup

- ``qubes.GetAppmenus`` - receive appmenus from a given VM (template); TODO: describe format here

- ``qubes.GetImageRGBA`` - receive image/application icon. Protocol:

  1. Caller sends the name of the requested icon. This can be one of:



    - ``xdgicon:NAME`` - search for NAME in a standard icon theme

    - ``-`` - get icon data from stdin (the caller), can be prefixed with format name, for example ``png:-``

    - file name



  2. The service responds with image dimensions: width and height as decimal numbers, separated with a space and with an EOL marker at the end; then image data in RGBA format (32 bits per pixel)





- ``qubes.SetDateTime`` - set the VM's clock, called periodically by dom0 (can be triggered manually from dom0 by calling ``qvm-sync-clock``). The service receives one line at stdin - time in the format of ``date -u -Iseconds``, for example ``2015-07-31T16:10:43+0000``.

- ``qubes.SetGuiMode`` - called in a HVM to switch between fullscreen and seamless GUI mode. The service receives a single word on stdin - either ``FULLSCREEN`` or ``SEAMLESS``

- ``qubes.ResizeDisk`` - called to inform that an underlying disk was resized. Name of the disk image is passed on standard input (``root``, ``private``, ``volatile``, or other). This is used starting with Qubes 4.0.



Other Qrexec services installed by default:

- ``qubes.Backup`` - store a Qubes backup. The service receives a location chosen by the user (one line, terminated by ``\n``) and the backup archive (:doc:`description of backup format </user/how-to-guides/backup-emergency-restore-v2>`)

- ``qubes.DetachPciDevice`` - service called in reaction to a ``qvm-pci -d`` call on a running VM. The service receives one word - BDF of the device to detach. When the service call ends, the device will be detached

- ``qubes.Filecopy`` - receive some files from another VM. Files sent in :doc:`qfile format </developer/services/qfilecopy>`

- ``qubes.OpenInVM`` - open a file in the called VM. Service receives a single file on stdin (in :doc:`qfile format </developer/services/qfilecopy>`. After a file viewer/editor is terminated, if the file was modified, it can be sent back (just raw content, without any headers); otherwise service should just terminate without sending anything. This service is used by both ``qvm-open-in-vm`` and ``qvm-open-in-dvm`` tools. When called in a DispVM, service termination will trigger DispVM cleanup.

- ``qubes.Restore`` - retrieve a Qubes backup. The service receives the backup location entered by the user (one line, terminated by ``\n``). Afterwards, it should output the backup archive in :doc:`qfile format </developer/services/qfilecopy>` (core-agent-linux component contains the ``tar2qfile`` utility to do the conversion)

- ``qubes.SelectDirectory``, ``qubes.SelectFile`` - services which should show the file/directory selection dialog and return (to stdout) a single line containing the selected path, or nothing in the case of cancellation

- ``qubes.SuspendPre`` - service called in every VM with a PCI device attached just before system suspend

- ``qubes.SuspendPost`` - service called in every VM with a PCI device attached just after system resume

- ``qubes.SyncNtpClock`` - service called to trigger network time synchronization. Service should synchronize the local VM's time and terminate when done.

- ``qubes.WindowIconUpdater`` - service called by the VM to send icons of individual windows. The protocol there is simple one direction stream: VM sends a window ID followed by an icon in ``qubes.GetImageRGBA`` format, then the next window ID etc. VM can send an icon for the same window multiple times to replace the previous one (for example for animated icons)

- ``qubes.VMShell`` - call any command in the VM; the commands are passed one per line

  - ``qubes.VMShell+WaitForSession`` waits for full VM startup first



- ``qubes.VMExec`` - call any command in the VM, without using a shell, the command needs to be passed as argument and encoded as follows:

  - the executable name and arguments are separated by ``+``

  - everything except alphanumeric characters, ``.`` and ``_`` needs to be escaped

  - bytes are escaped as ``-HH`` (where ``HH`` is hex code, capital letters only)

  - ``-`` itself can be escaped as ``--``

  - example: to run ``ls -a /home/user``, use ``qubes.VMExec+ls+--a+-2Fhome-2Fuser``



- ``qubes.VMExecGUI`` - a variant of ``qubes.VMExec`` that waits for full VM startup first



Services called in the GuiVM:

- ``policy.Ask``, ``policy.Notify`` - confirmation prompts and notifications for Qubes RPC calls, see :ref:`qrexec-policy implementation <developer/services/qrexec-internals:\`\`qrexec-policy\`\` implementation>` for a detailed description.



Currently, Qubes still calls a few tools in VM directly, not using the service abstraction. This will change in the future. Those tools are:

- ``/usr/lib/qubes/qubes-download-dom0-updates.sh`` - script to download updates (or new packages to be installed) for dom0 (``qubes-dom0-update`` tool)

- ``date -u -Iseconds`` - called directly to retrieve time after calling the ``qubes.SyncNtpClock`` service (``qvm-sync-clock`` tool)

- ``nm-online -x`` - called before the ``qubes.SyncNtpClock`` service call by the ``qvm-sync-clock`` tool

- ``resize2fs`` - called to resize the filesystem on the /rw partition by the ``qvm-grow-private`` tool

- ``gpk-update-viewer`` - called by Qubes Manager to display available updates in a TemplateVM

- ``systemctl start qubes-update-check.timer`` (and similarly stop) - called when enabling/disabling update checking in a given VM (``qubes-update-check`` :doc:`qvm-service </user/advanced-topics/qubes-service>`)



Additionally, automatic tests extensively run various commands directly in VMs. We do not plan to change that.

GUI protocol
------------


GUI initialization includes passing the whole screen dimensions from dom0 to VM. This will most likely be overwritten by qubes.SetMonitorLayout Qubes RPC call.
