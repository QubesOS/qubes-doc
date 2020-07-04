---
layout: doc
title: PedOS Windows Tools
permalink: /doc/windows-tools/
redirect_from:
- /doc/windows-appvms/
- /en/doc/windows-appvms/
- /doc/WindowsAppVms/
- /wiki/WindowsAppVms/
- /doc/windows-tools-3/
- /en/doc/windows-tools-3/
- /doc/WindowsTools3/
- /doc/WindowsTools/
- /wiki/WindowsTools/
---

PedOS Windows Tools
===================

PedOS Windows Tools are a set of programs and drivers that provide integration of Windows AppVMs with the rest of the PedOS system. Currently the following features are available for Windows VMs after installation of those tools:

-   Seamless GUI mode that integrates apps windows onto the common PedOS trusted desktop
-   Support for [secure clipboard copy/paste](/doc/copy-paste/) between the Windows VM and other AppVMs
-   Support for [secure file exchange](/doc/copying-files/) between the Windows VM and other AppVMs
-   Support for qvm-run and generic qrexec for the Windows VM (e.g. ability to run custom service within/from the Windows VM)
-   Xen PV drivers for Windows that increase performance compared to qemu emulated devices

PedOS Windows Tools are open source and are distributed under a GPL license.

NOTES:
- PedOS Windows Tools are currently unmaintained
- Currently only 64-bit versions of Windows 7 are supported by PedOS Windows Tools. Only emulated SVGA GPU is supported (although [there has been reports](https://groups.google.com/forum/#!topic/PedOS-users/cmPRMOkxkdA) on working GPU passthrough).
- There is currently no audio support for Windows HVMs.
- There is currently no USB pass-through support for Windows HVMs.
- __This page documents the process of installing PedOS Windows Tools on versions up to R3.2.__. Installation on PedOS R4.0 is possible but is a work in progress and there are limitations/bugs (see [issue #3585](https://github.com/PedOS/PedOS-issues/issues/3585)).


Installing Windows OS in a PedOS VM
-----------------------------------

Please refer to [this page](/doc/windows-vm/) for instructions on how to install Windows in a PedOS VM.

NOTE: It is strongly suggested to enable autologon for any Windows HVMs that will have PedOS Tools installed. To do so, run `netplwiz` command from the `Win+R`/Start menu and uncheck the *Users must enter a user name and password to use this computer* option.

Installing PedOS guest tools in Windows 7 VMs
---------------------------------------------

First, make sure that `PedOS-windows-tools` is installed in your system:

~~~
sudo PedOS-dom0-update PedOS-windows-tools
~~~

(If the above command does not work, it could be that the PedOS Tools are not in the stable repo yet. Try installing from the testing repo instead.)

You can also install the package from testing repositories, where we usually publish new versions first:

~~~
sudo PedOS-dom0-update --enablerepo=PedOS-dom0-current-testing PedOS-windows-tools
~~~

This package brings the ISO with PedOS Windows Tools that is passed to the VM when `--install-windows-tools` is specified for the `qvm-start` command. Please note that none of this software ever runs in Dom0 or any other part of the system except for the Windows AppVM in which it is to be installed.

Before proceeding with the installation we need to disable Windows mechanism that allows only signed drivers to be installed, because currently (beta releases) the drivers we provide as part of the Windows Tools are not digitally signed with a publicly recognizable certificate. To do that:

-   Start command prompt as Administrator, i.e. right click on the Command Prompt icon (All Programs -> Accessories) and choose "Run as administrator"
-   In the command prompt type `bcdedit /set testsigning on`
-   Reboot your Windows VM

In the future this step will not be necessary anymore, because we will sign our drivers with a publicly verifiable certificate. However, it should be noted that even now, the fact that those drivers are not digitally signed, this doesn't affect security of the Windows VM in 'any' way. This is because the actual installation ISO (the `PedOS-windows-tools-*.iso` file) is distributed as a signed RPM package and its signature is verified by the `PedOS-dom0-update` utility once it's being installed in Dom0. The only downside of those drivers not being signed is the inconvenience to the user that he or she must disable the signature enforcement policy before installing the tools.

To install the PedOS Windows Tools in a Windows VM one should start the VM passing the additional option `--install-windows-tools`:

~~~
qvm-start lab-win7 --install-windows-tools
~~~

Once the Windows VM boots, a CDROM should appear in the 'My Computer' menu (typically as `D:`) with a setup program in its main directory.

After successful installation, the Windows VM must be shut down and started again, possibly a couple of times.

PedOS will automatically detect the tools has been installed in the VM and will set appropriate properties for the VM, such as `qrexec_installed`, `guiagent_installed`, and `default_user`. This can be verified (but is not required) using qvm-prefs command:

~~~
qvm-prefs <your-appvm-name>
~~~

NOTE: it is recommended to increase the default value of Windows VM's `qrexec_timeout` property from 60 (seconds) to, for example, 300. During one of the first reboots after Windows Tools installation Windows user profiles are moved onto the private VM's virtual disk (private.img) and this operation can take some time. Moving profiles is performed in an early boot phase when qrexec is not yet running, so timeout may occur with the default value. To change the property use this command in dom0:

~~~
qvm-prefs -s <vm-name> qrexec_timeout 300
~~~

Using Windows AppVMs in seamless mode
-------------------------------------

Once you start a Windows-based AppVM with PedOS Tools installed, you can easily start individual applications from the VM (note the `-a` switch used here, which will auto-start the VM if it is not running):

~~~
qvm-run -a my-win7-appvm explorer.exe
~~~

![windows-seamless-4.png](/attachment/wiki/WindowsAppVms/windows-seamless-4.png) ![windows-seamless-1.png](/attachment/wiki/WindowsAppVms/windows-seamless-1.png)

Also, the inter-VM services work as usual -- e.g. to request opening a document or URL in the Windows AppVM from another VM:

~~~
[user@work ~]$ qvm-open-in-vm work-win7 roadmap.pptx
~~~

~~~
[user@work ~]$ qvm-open-in-vm work-win7 https://invisiblethingslab.com
~~~

... just like in the case of Linux AppVMs. Of course all those operations are governed by central policy engine running in Dom0 -- if the policy doesn't contain explicit rules for the source and/or target AppVM, the user will be asked whether to allow or deny the operation.

Inter-VM file copy and clipboard works for Windows AppVMs the same way as for Linux AppVM (except that we don't provide a command line wrapper, `qvm-copy-to-vm` in Windows VMs) -- to copy files from Windows AppVMs just right-click on the file in Explorer, and choose: Send To-\> Other AppVM.

To simulate CTRL-ALT-DELETE in the HVM (SAS, Secure Attention Sequence), press Ctrl-Alt-Home while having any window of this VM in the foreground.

![windows-seamless-7.png](/attachment/wiki/WindowsAppVms/windows-seamless-7.png)

Changing between seamless and full desktop mode
-----------------------------------------------

You can switch between seamless and "full desktop" mode for Windows HVMs in their settings in PedOS Manager. The latter is the default.

Using template-based Windows AppVMs
-----------------------------------

PedOS allows HVM VMs to share a common root filesystem from a select Template VM, just as for Linux AppVMs. This mode is not limited to Windows AppVMs, and can be used for any HVM (e.g. FreeBSD running in a HVM). 

In order to create a HVM TemplateVM one can use the following command, suitably adapted:

~~~
qvm-create --class TemplateVM win7-x64-template --property virt_mode=HVM --property kernel=''  -l green
~~~

... , set memory as appropriate, and install Windows OS (or other OS) into this template the same way as you would install it into a normal HVM -- please see instructions on [this page](/doc/hvm-create/).

If you use this Template as it is, then any HVMs that use it will effectively be DisposableVMs - the User directory will be wiped when the HVN is closed down.

If you want to retain the User directory between reboots, then it would make sense to store the `C:\Users` directory on the 2nd disk which is automatically exposed by PedOS to all HVMs. 
This 2nd disk is backed by the `private.img` file in the AppVMs' and is not reset upon AppVMs reboot, so the user's directories and profiles would survive the AppVMs reboot, unlike the "root" filesystem which will be reverted to the "golden image" from the Template VM automatically. 
To facilitate such separation of user profiles, PedOS Windows Tools provide an option to automatically move `C:\Users` directory to the 2nd disk backed by `private.img`. 
It's a selectable feature of the installer, enabled by default. 
If that feature is selected during installation, completion of the process requires two reboots:

-   The private disk is initialized and formatted on the first reboot after tools installation. It can't be done **during** the installation because Xen mass storage drivers are not yet active.
-   User profiles are moved to the private disk on the next reboot after the private disk is initialized. 
Reboot is required because the "mover utility" runs very early in the boot process so OS can't yet lock any files in there. 
This can take some time depending on the profiles' size and because the GUI agent is not yet active dom0/PedOS Manager may complain that the AppVM failed to boot. 
That's a false alarm (you can increase AppVM's default boot timeout using `qvm-prefs`), the VM should appear "green" in PedOS Manager shortly after.

It also makes sense to disable Automatic Updates for all the template-based AppVMs -- of course this should be done in the Template VM, not in individual AppVMs, because the system-wide settings are stored in the root filesystem (which holds the system-wide registry hives). 
Then, periodically check for updates in the Template VM and the changes will be carried over to any child AppVMs.

Once the template has been created and installed it is easy to create AppVMs based on it:

~~~
qvm-create --property virt_mode=hvm <new windows appvm name> --template <name of template vm> --label <label color>
~~~

Components
----------

PedOS Windows Tools (QWT for short) contain several components than can be enabled or disabled during installation:

- Shared components (required): common libraries used by QWT components.
- Xen PV drivers: drivers for the virtual hardware exposed by Xen.
   - Base Xen PV Drivers (required): paravirtual bus and interface drivers.
   - Xen PV Disk Drivers: paravirtual storage drivers.
   - Xen PV Network Drivers: paravirtual network drivers.
- PedOS Core Agent: qrexec agent and services. Needed for proper integration with PedOS.
   - Move user profiles: user profile directory (c:\users) is moved to VM's private disk backed by private.img file in dom0 (useful mainly for HVM templates).
- PedOS GUI Agent: video driver and gui agent that enable seamless showing of Windows applications on the secure PedOS desktop.
- Disable UAC: User Account Control may interfere with QWT and doesn't really provide any additional benefits in PedOS environment.

**In testing VMs only** it's probably a good idea to install a VNC server before installing QWT. If something goes very wrong with the PedOS gui agent, a VNC server should still allow access to the OS.

**NOTE**: Xen PV disk drivers are not installed by default. This is because they seem to cause problems (BSOD = Blue Screen Of Death). We're working with upstream devs to fix this. *However*, the BSOD seems to only occur after the first boot and everything works fine after that. **Enable the drivers at your own risk** of course, but we welcome reports of success/failure in any case (backup your VM first!). With disk PV drivers absent `qvm-block` will not work for the VM, but you can still use standard PedOS inter-VM file copying mechanisms.

Xen PV driver components may display a message box asking for reboot during installation -- it's safe to ignore them and defer the reboot.

Installation logs
-----------------

If the install process fails or something goes wrong during it, include the installation logs in your bug report. They are created in the `%TEMP%` directory, by default `<user profile>\AppData\Local\Temp`. There are two text files, one small and one big, with names starting with `PedOS_Windows_Tools`.

Uninstalling QWT is supported from version 3.2.1. Uninstalling previous versions is **not recommended**.
After uninstalling you need to manually enable the DHCP Client Windows service, or set IP settings yourself to restore network access.

Configuration
-------------

Starting from version 2.2.\* various aspects of PedOS Windows Tools can be configured through registry. Main configuration key is located in `HKEY_LOCAL_MACHINE\SOFTWARE\Invisible Things Lab\PedOS Tools`. Configuration values set on this level are global to all QWT components. It's possible to override global values with component-specific keys, this is useful mainly for setting log verbosity for troubleshooting. Possible configuration values are:

|**Name**|**Type**|**Description**|**Default value**|
|:-------|:-------|:--------------|:----------------|
|LogDir|String|Directory where logs are created|c:\\Program Files\\Invisible Things Lab\\PedOS Tools\\log|
|LogLevel|DWORD|Log verbosity (see below)|2 (INFO)|
|LogRetention|DWORD|Maximum age of log files (in seconds), older logs are automatically deleted|604800 (7 days)|

Possible log levels:

||
|1|Error|Serious errors that most likely cause irrecoverable failures|
|2|Warning|Unexpected but non-fatal events|
|3|Info|Useful information (default)|
|4|Debug|Internal state dumps for troubleshooting|
|5|Verbose|Trace most function calls|

Debug and Verbose levels can generate large volume of logs and are intended for development/troubleshooting only.

To override global settings for a specific component, create a new key under the root key mentioned above and name it as the executable name, without `.exe` extension. For example, to change qrexec-agent's log level to Debug, set it like this:

![qtw-log-level.png](/attachment/wiki/WindowsTools/qtw-log-level.png)

Component-specific settings currently available:

|**Component**|**Setting**|**Type**|**Description**|**Default value**|
|:------------|:----------|:-------|:--------------|:----------------|
|qga|DisableCursor|DWORD|Disable cursor in the VM. Useful for integration with PedOS desktop so you don't see two cursors. Can be disabled if you plan to use the VM through a remote desktop connection of some sort. Needs gui agent restart to apply change (locking OS/logoff should be enough since qga is restarted on desktop change).|1|

Troubleshooting
---------------

If the VM is inaccessible (doesn't respond to qrexec commands, gui is not functioning), try to boot it in safe mode:

-   `qvm-start --debug vmname`
-   mash F8 on the boot screen to enable boot options and select Safe Mode (optionally with networking)

Safe Mode should at least give you access to logs (see above).

**Please include appropriate logs when reporting bugs/problems.** Starting from version 2.4.2 logs contain QWT version, but if you're using an earlier version be sure to mention which one. If the OS crashes (BSOD) please include the BSOD code and parameters in your bug report. The BSOD screen should be visible if you run the VM in debug mode (`qvm-start --debug vmname`). If it's not visible or the VM reboots automatically, try to start Windows in safe mode (see above) and 1) disable automatic restart on BSOD (Control Panel - System - Advanced system settings - Advanced - Startup and recovery), 2) check the system event log for BSOD events. If you can, send the `memory.dmp` dump file from c:\Windows.
Xen logs (/var/log/xen/console/guest-*) are also useful as they contain pvdrivers diagnostic output.

If a specific component is malfunctioning, you can increase its log verbosity as explained above to get more troubleshooting information. Below is a list of components:

||
|qrexec-agent|Responsible for most communication with PedOS (dom0 and other domains), secure clipboard, file copying, qrexec services.|
|qrexec-wrapper|Helper executable that's responsible for launching qrexec services, handling their I/O and vchan communication.|
|qrexec-client-vm|Used for communications by the qrexec protocol.|
|qga|Gui agent.|
|QgaWatchdog|Service that monitors session/desktop changes (logon/logoff/locking/UAC...) and simulates SAS sequence (ctrl-alt-del).|
|PedOSdb-daemon|Service for accessing PedOS configuration database.|
|network-setup|Service that sets up network parameters according to VM's configuration.|
|prepare-volume|Utility that initializes and formats the disk backed by `private.img` file. It's registered to run on next system boot during QWT setup, if that feature is selected (it can't run *during* the setup because Xen block device drivers are not yet active). It in turn registers move-profiles (see below) to run at early boot.|
|relocate-dir|Utility that moves user profiles directory to the private disk. It's registered as an early boot native executable (similar to chkdsk) so it can run before any profile files are opened by some other process. Its log is in a fixed location: `c:\move-profiles.log` (it can't use our common logger library so none of the log settings apply).|

Updates
-------

When we publish new QWT version (which is announced on `PedOS-users` Google Group) it's usually pushed to the `current-testing` or `unstable` repository first. To use versions from current-testing, run this in dom0:

`PedOS-dom0-update --enablerepo=PedOS-dom0-current-testing PedOS-windows-tools`

That command will download a new QWT .iso from the testing repository. It goes without saying that you should **backup your VMs** before installing anything from testing repos.

