---
layout: doc
title: WindowsTools
permalink: /doc/WindowsTools/
redirect_from: /wiki/WindowsTools/
---

Qubes Tools for Windows: advanced settings and troubleshooting
==============================================================

''Only 64-bit Windows 7 (any edition) is supported currently. Windows 8+ support is under development.''

Installable components
----------------------

Qubes Tools for Windows (QTW for short) contain several components than can be enabled or disabled during installation:

-   Xen GPL PV drivers (required): drivers for the hardware exposed by Xen.
-   Core Windows Agent: qrexec agent and services. Needed for proper integration with Qubes.
-   Move user profiles: User profiles directory (c:\\Users) will be moved into the private disk backed by private.img. This disk will be initialized/formatted automatically if needed. This feature is useful for Windows-based HVM templates, so child AppVMs can have their separate user profiles.
-   GUI Windows Agent: video driver and gui agent that enable seamless showing of Windows applications on the secure Qubes desktop.
-   Disable UAC: disables User Account Control prompts. *Is this still needed/wanted? Gui agent can handle UAC prompts now.*

It's probably a good idea to install a VNC server in the VM before installing QTW. If something goes very wrong with the Qubes gui agent, a VNC server should still allow access to the OS.

Verbose installation
--------------------

If the install process fails you can retry it using the command line below to get a detailed installation log (and send that to us):

`msiexec /i path-to-qubes-tools.msi /lv path-to-log-file.txt`

Uninstalling QTW 2.x is **not recommended**. It will most likely make the OS non-bootable because drivers for Xen storage devices will be uninstalled.

Configuration
-------------

Starting from version 2.2.\* various aspects of Qubes Tools for Windows can be configured through registry. Main configuration key is located in `HKEY_LOCAL_MACHINE\SOFTWARE\Invisible Things Lab\Qubes Tools`. Configuration values set on this level are global to all QTW components. It's possible to override global values with component-specific keys, this is useful mainly for setting log verbosity for troubleshooting. Possible configuration values are:

|**Name**|**Type**|**Description**|**Default value**|
|:-------|:-------|:--------------|:----------------|
|LogDir|String|Directory where logs are created|c:\\Program Files\\Invisible Things Lab\\Qubes OS Windows Tools\\log|
|LogLevel|DWORD|Log verbosity (see below)|2 (INFO)|
|LogRetention|DWORD|Maximum age of log files (in seconds), older logs are automatically deleted|604800 (7 days)|

Possible log levels:

||
|0|Error|Serious errors that most likely cause irrecoverable failures|
|1|Warning|Unexpected but non-fatal events|
|2|Info|Useful information|
|3|Debug|Internal state dumps for troubleshooting|
|4|Verbose|Trace most function calls|

Debug and Verbose levels can generate large volume of logs and are intended for development/troubleshooting only.

To override global settings for a specific component, create a new key under the root key mentioned above and name it as the executable name, without `.exe` extension. For example, to change qrexec-agent's log level to Debug, set it like this:

![qtw-log-level.png](/attachment/wiki/WindowsTools/qtw-log-level.png)

Component-specific settings currently available:

|**Component**|**Setting**|**Type**|**Description**|**Default value**|
|:------------|:----------|:-------|:--------------|:----------------|
|wga|UseDirtyBits|DWORD|Enable experimental feature of the gui agent/qvideo driver: use page table dirty bits to determine changed display regions. This can improve performance but may impact display responsiveness (some changes may not be detected resulting in "stale" image). Needs VM restart to apply change.|0|
|wga|DisableCursor|DWORD|Disable cursor in the VM. Useful for integration with Qubes desktop so you don't see two cursors. Can be disabled if you plan to use the VM through a remote desktop connection of some sort. Needs gui agent restart to apply change (locking OS/logoff should be enough since wga is restarted on desktop change).|1|

Troubleshooting
---------------

If the VM is inaccessible (doesn't respond to qrexec commands, gui is not functioning), try to boot it in safe mode:

-   `qvm-start --debug vmname`
-   mash F8 on the boot screen to enable boot options and select Safe Mode (optionally with networking)

Safe Mode should at least give you access to logs (see above).

**Please include appropriate logs when reporting bugs/problems.** Starting from version 2.4.2 logs contain QTW version, but if you're using an earlier version be sure to mention which one. If the OS crashes (BSOD) please include the BSOD code and parameters in your bug report. The BSOD screen should be visible if you run the VM in debug mode (`qvm-start --debug vmname`). If it's not visible or the VM reboots automatically, try to start Windows in safe mode (see above) and 1) disable automatic restart on BSOD (Control Panel - System - Advanced system settings - Advanced - Startup and recovery), 2) check the system event log for BSOD events.

If a specific component is malfunctioning, you can increase it's log verbosity as explained above to get more troubleshooting information. Below is a list of components:

||
|qrexec-agent|Responsible for most communication with Qubes (dom0 and other domains), secure clipboard, file copying, qrexec services.|
|qrexec-client-vm|Used for communications by the qrexec protocol.|
|wga|Gui agent.|
|QTWHelper|Service that monitors session/desktop changes (logon/logoff/locking/UAC...) and simulates SAS sequence (ctrl-alt-del).|
|prepare-volume|Utility that initializes and formats the disk backed by `private.img` file. It's registered to run on next system boot during QTW setup, if that feature is selected (it can't run *during* the setup because Xen block device drivers are not yet active). It in turn registers move-profiles (see below) to run at early boot.|
|move-profiles|Utility that moves user profiles directory to the private disk. It's registered as an early boot native executable (similar to chkdsk) so it can run before any profile files are opened by some other process. Its log is in a fixed location: `c:\move-profiles.log` (it can't use our common logger library so none of the log settings apply).|

Updates
-------

When we publish new QTW version (which is announced on `qubes-users` Google Group) it's usually pushed to the `current-testing` repository first. To use versions from current-testing, run this in dom0:

`qubes-dom0-update --enablerepo=qubes-dom0-current-testing qubes-windows-tools`

That command will download a new QTW .iso from the testing repository. It goes without saying that you should **backup your VMs** before installing anything from testing repos.
