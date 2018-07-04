---
layout: doc
title: qvm-prefs
permalink: /doc/tools/3.2/dom0/qvm-prefs/
redirect_from:
- /doc/dom0-tools/qvm-prefs/
- /en/doc/dom0-tools/qvm-prefs/
- /doc/Dom0Tools/QvmPrefs/
- /wiki/Dom0Tools/QvmPrefs/
---

```
=========
qvm-prefs
=========

NAME
====
qvm-prefs - list/set various per-VM properties

SYNOPSIS
========
| qvm-prefs -l [options] <vm-name>
| qvm-prefs -g [options] <vm-name> <property>
| qvm-prefs -s [options] <vm-name> <property> [...]


OPTIONS
=======
-h, --help
    Show this help message and exit
-l, --list
    List properties of a specified VM
-g, --get
    Get a single property of a specified VM
-s, --set
    Set properties of a specified VM
--force-root
    Force to run, even with root privileges
--offline-mode
    Offline mode

PROPERTIES
==========

include_in_backups
    Accepted values: ``True``, ``False``

    Control whenever this VM will be included in backups by default (for now
    works only in qubes-manager). You can always manually select or
    deselect any VM for backup.

pcidevs
    PCI devices assigned to the VM. Should be edited using qvm-pci tool.

pci_strictreset
    Accepted values: ``True``, ``False``

    Control whether prevent assigning to VM a device which does not support any
    reset method. Generally such devices should not be assigned to any VM,
    because there will be no way to reset device state after VM shutdown, so
    the device could attack next VM to which it will be assigned. But in some
    cases it could make sense - for example when the VM to which it is assigned
    is trusted one, or is running all the time.

pci_e820_host
    Accepted values: ``True``, ``False``

    Give VM with PCI devices a memory map (e820) of the host. This is
    required for some devices to properly resolve conflicts in address space.
    This option is enabled by default for VMs with PCI devices and have no
    effect for VMs without devices.

label
    Accepted values: ``red``, ``orange``, ``yellow``, ``green``, ``gray``,
    ``blue``, ``purple``, ``black``

    Color of VM label (icon, appmenus, windows border). If VM is running,
    change will be applied at first VM restart.

netvm
    Accepted values: netvm name, ``default``, ``none``

    To which NetVM connect. Setting to ``default`` will follow system-global
    default NetVM (managed by qubes-prefs). Setting to ``none`` will disable
    networking in this VM.

dispvm_netvm
    Accepted values: netvm name, ``default``, ``none``

    Which NetVM should be used for Disposable VMs started by this one.
    ``default`` is to use the same NetVM as the VM itself.

maxmem
    Accepted values: memory size in MB

    Maximum memory size available for this VM. Dynamic memory management (aka
    qmemman) will not be able to balloon over this limit. For VMs with
    qmemman disabled, this will be overridden by *memory* property (at VM
    startup).

memory
    Accepted values: memory size in MB

    Initial memory size for VM. This should be large enough to allow VM startup
    - before qmemman starts managing memory for this VM. For VM with qmemman
    disabled, this is static memory size.

kernel
    Accepted values: kernel version, ``default``, ``none``

    Kernel version to use (only for PV VMs). Available kernel versions will be
    listed when no value given (there are in /var/lib/qubes/vm-kernels).
    Setting to ``default`` will follow system-global default kernel (managed
    via qubes-prefs). Setting to ``none`` will use "kernels" subdir in
    VM directory - this allows having VM-specific kernel; also this the only
    case when /lib/modules is writable from within VM.

template
    Accepted values: TemplateVM name

    TemplateVM on which VM base. It can be changed only when VM isn't running.

vcpus
    Accepted values: no of CPUs

    Number of CPU (cores) available to VM. Some VM types (eg DispVM) will not
    work properly with more than one CPU.

kernelopts
    Accepted values: string, ``default``

    VM kernel parameters (available only for PV VMs). This can be used to
    workaround some hardware specific problems (eg for NetVM). Setting to
    ``default`` will use some reasonable defaults (currently different for VMs
    with PCI devices and without). For VM without PCI devices
    ``default`` option means inherit this value from the VM template (if any).
    Some helpful options (for debugging purposes): ``earlyprintk=xen``,
    ``init=/bin/bash``

name
    Accepted values: alphanumerical name

    Name of the VM. Can be only changed when VM isn't running.

drive
    Accepted values: [hd:\|cdrom:][backend-vm:]path

    Additional drive for the VM (available only for HVMs). This can be used to
    attach installation image. ``path`` can be file or physical device (eg.
    /dev/sr0). The same syntax can be used in qvm-start --drive - to
    attach drive only temporarily.

mac
    Accepted values: MAC address, ``auto``

    Can be used to force specific of virtual ethernet card in the VM. Setting
    to ``auto`` will use automatic-generated MAC - based on VM id. Especially
    useful when licensing requires a static MAC address.
    For template-based HVM ``auto`` mode means to clone template MAC.

default_user
    Accepted values: username

    Default user used by qvm-run. Note that it make sense only on non-standard
    template, as the standard one always have "user" account.

debug
    Accepted values: ``on``, ``off``

    Enables debug mode for VM. This can be used to turn on/off verbose logging
    in many Qubes components at once (gui virtualization, VM kernel, some other
    services).
    For template-based HVM, enabling debug mode also disables automatic reset
    root.img (actually volatile.img) before each VM startup, so changes made to
    root filesystem stays intact. To force reset root.img when debug mode
    enabled, either change something in the template (simple start+stop will
    do, even touch its root.img is enough), or remove VM's volatile.img
    (check the path with qvm-prefs).

qrexec_installed
    Accepted values: ``True``, ``False``

    This HVM have qrexec agent installed. When VM have qrexec agent installed,
    one can use qvm-run to start VM process, VM will benefit from Qubes RPC
    services (like file copy, or inter-vm clipboard). This option will be
    automatically turned on during Qubes Windows Tools installation, but if you
    install qrexec agent in some other OS, you need to turn this option on
    manually.

guiagent_installed
    Accepted values: ``True``, ``False``

    This HVM have gui agent installed. This option disables full screen GUI
    virtualization and enables per-window seemless GUI mode. This option will
    be automatically turned on during Qubes Windows Tools installation, but if
    you install Qubes gui agent in some other OS, you need to turn this option
    on manually. You can turn this option off to troubleshoot some early HVM OS
    boot problems (enter safe mode etc), but the option will be automatically
    enabled at first VM normal startup (and will take effect from the next
    startup).

    *Notice:* when Windows GUI agent is installed in the VM, SVGA device (used
    to full screen video) is disabled, so even if you disable this
    option, you will not get functional full desktop access (on normal VM
    startup). Use some other means for that (VNC, RDP or so).

autostart
    Accepted values: ``True``, ``False``

    Start the VM during system startup. The default netvm is autostarted
    regardless of this setting.

timezone
    Accepted values: ``localtime``, time offset in seconds

    Set emulated HVM clock timezone. Use ``localtime`` (the default) to use the
    same time as dom0 have. Note that HVM will get only clock value, not the
    timezone itself, so if you use ``localtime`` setting, OS inside of HVM
    should also be configured to treat hardware clock as local time (and have
    proper timezone set).

AUTHORS
=======
| Joanna Rutkowska <joanna at invisiblethingslab dot com>
| Rafal Wojtczuk <rafal at invisiblethingslab dot com>
| Marek Marczykowski <marmarek at invisiblethingslab dot com>
```

-----

**Note:** The Markdown source of this page in [`qubes-doc`] was generated by running the [`update-manpages-3-2`] script on `qubes-core-admin/doc/qvm-tools/`.
If you wish to update the contents of this page as it appears on the Qubes OS website, please submit a pull request to change the appropriate file in `qubes-core-admin/doc/qvm-tools/`.
Do not attempt to change the Markdown source of this page in [`qubes-doc`] directly.
All direct changes to the Markdown file will be overwritten the next time this page is regenerated.

[`qubes-doc`]: https://github.com/QubesOS/qubes-doc/
[`update-manpages-3-2`]: https://github.com/QubesOS/qubesos.github.io/blob/master/_utils/update-manpages-3-2

