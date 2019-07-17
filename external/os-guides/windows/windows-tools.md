---
layout: doc
title: Qubes Windows Tools
permalink: /doc/windows-tools/
redirect_from:
- /doc/windows-appvms/
- /en/doc/windows-appvms/
- /doc/WindowsAppVms/
- /wiki/WindowsAppVms/
---

Qubes Windows Tools
===================

Qubes Windows Tools are a set of programs and drivers that provide integration of Windows AppVMs with the rest of the Qubes system. Currently the following features are available for Windows VMs after installation of those tools:

-   Seamless GUI mode that integrates apps windows onto the common Qubes trusted desktop
-   Support for [secure clipboard copy/paste](/doc/copy-paste/) between the Windows VM and other AppVMs
-   Support for [secure file exchange](/doc/copying-files/) between the Windows VM and other AppVMs
-   Support for qvm-run and generic qrexec for the Windows VM (e.g. ability to run custom service within/from the Windows VM)
-   Xen PV drivers for Windows that increase performance compared to qemu emulated devices

Qubes Windows Tools are open source and are distributed under a GPL license.

NOTES:
- Qubes Windows Tools are currently unmaintained
- Currently only 64-bit versions of Windows 7 are supported by Qubes Windows Tools. Only emulated SVGA GPU is supported (although [there has been reports](https://groups.google.com/forum/#!topic/qubes-users/cmPRMOkxkdA) on working GPU passthrough).
- There is currently no audio support for Windows HVMs.
- There is currently no USB pass-through support for Windows HVMs.
- __This page documents the process of installing Qubes Windows Tools on versions up to R3.2.__. Installation on Qubes R4.0 is possible but is a work in progress and there are limitations/bugs (see [issue #3585](https://github.com/QubesOS/qubes-issues/issues/3585)).


Installing Windows OS in a Qubes VM
-----------------------------------

Please refer to [this page](/doc/windows-vm/) for instructions on how to install Windows in a Qubes VM.

NOTE: It is strongly suggested to enable autologon for any Windows HVMs that will have Qubes Tools installed. To do so, run `netplwiz` command from the `Win+R`/Start menu and uncheck the *Users must enter a user name and password to use this computer* option.

Installing Qubes guest tools in Windows 7 VMs
---------------------------------------------

First, make sure that `qubes-windows-tools` is installed in your system:

~~~
sudo qubes-dom0-update qubes-windows-tools
~~~

(If the above command does not work, it could be that the Qubes Tools are not in the stable repo yet. Try installing from the testing repo instead.)

You can also install the package from testing repositories, where we usually publish new versions first:

~~~
sudo qubes-dom0-update --enablerepo=qubes-dom0-current-testing qubes-windows-tools
~~~

This package brings the ISO with Qubes Windows Tools that is passed to the VM when `--install-windows-tools` is specified for the `qvm-start` command. Please note that none of this software ever runs in Dom0 or any other part of the system except for the Windows AppVM in which it is to be installed.

Before proceeding with the installation we need to disable Windows mechanism that allows only signed drivers to be installed, because currently (beta releases) the drivers we provide as part of the Windows Tools are not digitally signed with a publicly recognizable certificate. To do that:

-   Start command prompt as Administrator, i.e. right click on the Command Prompt icon (All Programs -> Accessories) and choose "Run as administrator"
-   In the command prompt type `bcdedit /set testsigning on`
-   Reboot your Windows VM

In the future this step will not be necessary anymore, because we will sign our drivers with a publicly verifiable certificate. However, it should be noted that even now, the fact that those drivers are not digitally signed, this doesn't affect security of the Windows VM in 'any' way. This is because the actual installation ISO (the `qubes-windows-tools-*.iso` file) is distributed as a signed RPM package and its signature is verified by the `qubes-dom0-update` utility once it's being installed in Dom0. The only downside of those drivers not being signed is the inconvenience to the user that he or she must disable the signature enforcement policy before installing the tools.

To install the Qubes Windows Tools in a Windows VM one should start the VM passing the additional option `--install-windows-tools`:

~~~
qvm-start lab-win7 --install-windows-tools
~~~

Once the Windows VM boots, a CDROM should appear in the 'My Computer' menu (typically as `D:`) with a setup program in its main directory.

After successful installation, the Windows VM must be shut down and started again, possibly a couple of times.

Qubes will automatically detect the tools has been installed in the VM and will set appropriate properties for the VM, such as `qrexec_installed`, `guiagent_installed`, and `default_user`. This can be verified (but is not required) using qvm-prefs command:

~~~
qvm-prefs <your-appvm-name>
~~~

NOTE: it is recommended to increase the default value of Windows VM's `qrexec_timeout` property from 60 (seconds) to, for example, 300. During one of the first reboots after Windows Tools installation Windows user profiles are moved onto the private VM's virtual disk (private.img) and this operation can take some time. Moving profiles is performed in an early boot phase when qrexec is not yet running, so timeout may occur with the default value. To change the property use this command in dom0:

~~~
qvm-prefs -s <vm-name> qrexec_timeout 300
~~~

Using Windows AppVMs in seamless mode
-------------------------------------

Once you start a Windows-based AppVM with Qubes Tools installed, you can easily start individual applications from the VM (note the `-a` switch used here, which will auto-start the VM if it is not running):

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

You can switch between seamless and "full desktop" mode for Windows HVMs in their settings in Qubes Manager. The latter is the default.

Using template-based Windows AppVMs
-----------------------------------

Qubes allows HVM VMs to share a common root filesystem from a select Template VM, just as for Linux AppVMs. This mode is not limited to Windows AppVMs, and can be used for any HVM (e.g. FreeBSD running in a HVM). 

In order to create a HVM TemplateVM one can use the following command, suitably adapted:

~~~
qvm-create --class TemplateVM win7-x64-template --property virt_mode=HVM --property kernel=''  -l green
~~~

... , set memory as appropriate, and install Windows OS (or other OS) into this template the same way as you would install it into a normal HVM -- please see instructions on [this page](/doc/hvm-create/).

If you use this Template as it is, then any HVMs that use it will effectively be DisposableVMs - the User directory will be wiped when the HVN is closed down.

If you want to retain the User directory between reboots, then it would make sense to store the `C:\Users` directory on the 2nd disk which is automatically exposed by Qubes to all HVMs. 
This 2nd disk is backed by the `private.img` file in the AppVMs' and is not reset upon AppVMs reboot, so the user's directories and profiles would survive the AppVMs reboot, unlike the "root" filesystem which will be reverted to the "golden image" from the Template VM automatically. 
To facilitate such separation of user profiles, Qubes Windows Tools provide an option to automatically move `C:\Users` directory to the 2nd disk backed by `private.img`. 
It's a selectable feature of the installer, enabled by default. 
If that feature is selected during installation, completion of the process requires two reboots:

-   The private disk is initialized and formatted on the first reboot after tools installation. It can't be done **during** the installation because Xen mass storage drivers are not yet active.
-   User profiles are moved to the private disk on the next reboot after the private disk is initialized. 
Reboot is required because the "mover utility" runs very early in the boot process so OS can't yet lock any files in there. 
This can take some time depending on the profiles' size and because the GUI agent is not yet active dom0/Qubes Manager may complain that the AppVM failed to boot. 
That's a false alarm (you can increase AppVM's default boot timeout using `qvm-prefs`), the VM should appear "green" in Qubes Manager shortly after.

It also makes sense to disable Automatic Updates for all the template-based AppVMs -- of course this should be done in the Template VM, not in individual AppVMs, because the system-wide settings are stored in the root filesystem (which holds the system-wide registry hives). 
Then, periodically check for updates in the Template VM and the changes will be carried over to any child AppVMs.

Once the template has been created and installed it is easy to create AppVMs based on it:

~~~
qvm-create --hvm <new windows appvm name> --template <name of template vm> --label <label color>
~~~

