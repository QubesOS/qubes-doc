---
layout: wiki
title: WindowsAppVms
permalink: /wiki/WindowsAppVms/
---

Installing and using Windows-based AppVMs
=========================================

Qubes provides special support for running Windows-based AppVMs. This requires the user to install Windows 7 x64 in a Qubes VM and subsequently install Qubes Windows Support tools inside the VM. This page describes this process in detail.

Qubes support tools for Windows is a set of programs and drivers that provide integration of Windows AppVMs with the rest of the Qubes system. Currently the following features are available for Windows VMs after installation of those tools:

-   Seamless GUI mode that integrates apps windows onto the common Qubes trusted desktop (available on Qubes R2 Beta 3 and later)
-   Support for [secure clipboard copy/paste](/wiki/CopyPaste) between the Windows VM and other AppVMs
-   Support for [secure file exchange](/wiki/CopyingFiles) between the Windows VM and other AppVMs
-   Support for qvm-run and generic qrexec for the Windows VM (e.g. ability to run custom service within/from the Windows VM)
-   Xen PV drivers for Windows that increase performance compared to qemu emulated devices

Qubes Windows Support Tools are not open source and are distributed under a commercial license and their source code is not publicly available.

Installing Windows OS in a Qubes VM
-----------------------------------

Please refer to [this page](/wiki/HvmCreate) for instructions on how to install Windows in a Qubes VM.

Installing Qubes support tools in Windows 7 VMs
-----------------------------------------------

To install the Qubes Windows support tools in a Windows VM one should start the VM passing the additional option `--install-windows-tools`:

``` {.wiki}
qvm-start lab-win7 --install-windows-tools
```

Once the Windows VM boots, a CDROM should appear in the 'My Computer' menu (typically as `D:`) with a setup program in its main directory.

Before proceeding with the installation we need to disable Windows mechanism that allows only signed drivers to be installed, because currently (beta releases) the drivers we provide as part of the Windows Support Tools are not digitally signed with a publicly recognizable certificate. How to do that is explained in the `README` file also located on the installation CDROM. In the future this step will not be necessary anymore, because we will sign our drivers with a publicly verifiable certificate. However, it should be noted that even now, the fact that those drivers are not digitally signed, this doesn't affect security of the Windows VM in 'any' way. This is because the actual installation ISO (the `qubes-windows-tools-*.iso` file) is distributed as a signed RPM package and its signature is verified by the `qubes-dom0-update` utility once it's being installed in Dom0. The only downside of those drivers not being signed is the inconvenience to the user that he or she must disable the signature enforcement policy before installing the tools, and also to accept a few scary looking warning windows during the installation process, as shown below.

[![No image "r2b1-win7-installing-qubes-tools-5.png" attached to HvmCreate](/chrome/common/attachment.png "No image "r2b1-win7-installing-qubes-tools-5.png" attached to HvmCreate")](/attachment/wiki/HvmCreate/r2b1-win7-installing-qubes-tools-5.png)

After successful installation, the Windows VM must be shut down and started again.

Qubes (R2 Beta 3 and later releases) will automatically detect the tools has been installed in the VM and will set appropriate properties for the VM, such as `qrexec_installed`, `guiagent_installed`, and `default_user`. This can be verified (but is not required) using qvm-prefs command:

``` {.wiki}
qvm-prefs <your-appvm-name>
```

Using Windows AppVMs in seamless mode (Qubes R2 Beta 3 and later)
-----------------------------------------------------------------

TODO

Forcing Windows AppVM into full desktop mode
--------------------------------------------

TODO

Using template-based Windows AppVMs (Qubes R2 Beta 3 and later)
---------------------------------------------------------------

TODO
