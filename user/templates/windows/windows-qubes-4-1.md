---
lang: en
layout: doc
permalink: /doc/templates/windows/windows-qubes-4-1/
redirect_from:
- /doc/templates/windows/windows-vm41/
- /doc/templates/windows/windows-vm41/
title: How to install Windows qubes in Qubes OS
---

You can install Windows just like any other OS as an [HVM](/doc/hvm/), if you just want something simple and you can live without some features. This works for Windows XP, 7, 8.1, 10 and 11.

Please keep in mind that Qubes Windows Tools are not supported on Windows XP.

You will get an environment in which basic functions are supported, but integration into the Qubes environment is rather restricted. The following functions will work right out of the box:

- display (1440x900 or 1280x1024 are a nice fit onto FHD hw display)
- keyboard (incl. correct mapping), pointing device
- network (emulated Realtek NIC)
- audio output and input (available even without QWT installation if `qvm-features audio-model` is set as `ich6`)

For better integration, a set of drivers and services, called Qubes Windows Tools (QWT) is available. Installation of these tools is straightforward and is described in a [separate document](/doc/templates/windows/qubes-windows-tools-4-1). QWT’s main features are:

- copy/paste between qubes
- copy files between qubes
- attaching USB devices to the qube
- attaching block devices to the qube (XEN PV disk driver must be installed)
- automatically set up networking
- automatically set up time/clock synchronization
- XEN PV drivers (some of them optional)
- optional user migration from `C:` to the qubes’ private volume (to be able use the qubes as a TemplateVM).
- seamless mode (Windows 7 only for now)
- propagating keyboard layout ?

## Importing a Windows VM from an earlier version of Qubes

- Importing from R3.2 or earlier will not work, because  Qubes R3.2 has the old stubdomain by default and this is preserved over backup and restore (as Windows otherwise won't boot.

- Importing from R4.0 should work, see [Migrate backups of Windows VMs created under Qubes R4.0 to R4.1](/doc/templates/windows/migrate-to-4-1).


## Windows VM installation

**qvm-create-windows-qube**: An unofficial, third-party tool for automating this process is available [here](https://github.com/elliotkillick/qvm-create-windows-qube). (Please note that this tool has not been reviewed by the Qubes OS Project. Use it at your own risk.)

However, if you are an expert or want to do it manually you may continue below.

**Notes:**
- The instructions may work on other versions than Windows 7, 8.1, 10 and 11 x64 but haven't been tested.
- Qubes Windows Tools (QWT) only supports Windows 7, 8.1, 10 and 11 x64. For installation, see [Qubes Windows Tools](/doc/templates/windows/qubes-windows-tools-4-1).

**Provide installation media**

Have the Windows ISO image (preferrably the 64-bit version) downloaded in some qube.

Windows ISOs can be downloaded directly from Microsoft (eg. [here](https://www.microsoft.com/en-us/software-download/windows10ISO) for Win10), or selected and downloaded via the [Windows Media Creation Tool](https://go.microsoft.com/fwlink/?LinkId=691209). You should, however, regard the downloaded image to be untrustworthy, since there is no reliable way to check that the download was not somehow compromised (see the discussion in issue [Simplify Qubes Windows Tools Installation for R4.1 #7240](https://github.com/QubesOS/qubes-issues/issues/7240)).

Unofficial “debloated” ISOs from projects like reviOS 18 or ameliorated 10 can be found on the net, although obviously you should consider them even “unsafer” than MS provided ISOs. Alternatively, one could download an official ISO and run scripts/apply patches before installation. Some of the “tweaks” might end up being too much depending on the qube’s planned usage though (eg. no appx functionality in ameliorated windows - so the installation of Windows Store apps is impossible, even with powershell).

**Create Windows VM**

Create a VM named WindowsNew in [HVM](/doc/hvm/) mode (Xen's current PVH limitations precludes from using PVH). This can be done in either of two ways:

- Using Qube Manager

   In order to create the new qube, select the command Qube -> New Qube in the Qube Manager::
     - Name: `WindowsNew`, Color: `orange` (for a standalone qubes, `black` for a template)
     - Type: `StandaloneVM (fully persistent)` or `TemplateVM (template home, persistent root)`
     - Template: `(none)`
     - Networking: `sys-firewall (default)`
     - Launch settings after creation: check
     - Click "OK".
  
     - Settings:
        - Basic:
          - System storage: 60.0+ GB
        - Advanced:
          - Include in memory balancing: uncheck
          - Initial memory: 4096+ MB
          - Kernel: `(none)`
          - Mode: `HVM`
        - Click "Apply".

   After creation, set `qvm-prefs WindowsNew qrexec_timeout 7200` via CLI in a dom0 terminal.

- Using CLI in a dom0 terminal
 
   - This can also be done via the following CLI commands in dom0, for a standalone qube:
      ~~~
      qvm-create --class StandaloneVM --label orange --property virt_mode=hvm WindowsNew
      ~~~
     and for a template:
      ~~~
      qvm-create --class TemplateVM --label black --property virt_mode=hvm WindowsNew
      ~~~
   - After creation, set the following parameters via CLI in a dom0 terminal:
      ~~~
      qvm-volume extend WindowsNew:root 60g
      qvm-prefs WindowsNew memory 4096
      qvm-prefs WindowsNew maxmem 4096
      qvm-prefs WindowsNew kernel ''
      qvm-prefs WindowsNew qrexec_timeout 7200
      ~~~

These parameters are set for the following reasons:
  
- A typical Windows installation requires between 25GB up to 60GB of disk space depending on the version (Home/Professional/...). Windows updates also end up using significant space. So, extend the root volume from the default 10GB to at least 60GB (note: it is straightforward to increase the root volume size after Windows is installed: simply extend the volume again in dom0 and then extend the system partition with Windows's disk manager).

- Setting memory to 4096MB may work in most cases, but using 6144MB (or even 8192MB) may reduce the likelihood of crashes during installation, especially for Windows 10 or 11. This is important as Windows qubes have to be created without memory balancing, as requested by the parameter settings described above.

- The Windows' installer requires a significant amount of memory or else the VM will crash with such errors:
  ~~~
  /var/log/xen/console/hypervisor.log:

  p2m_pod_demand_populate: Dom120 out of PoD memory! (tot=102411 ents=921600 dom120)
  (XEN) domain_crash called from p2m-pod.c:1218
  (XEN) Domain 120 (vcpu#0) crashed on cpu#3:
  ~~~
  So, increase the VM's memory to 4096MB (memory = maxmem because we don't use memory balancing), or 6144MB / 8192MB, as recommended above.
     
- Disable direct boot so that the VM will go through the standard cdrom/HDD boot sequence. This is done by setting the qube's kernel to an empty value.

- After creating the new qube, increase the VM's `qrexec_timeout`: in case you happen to get a BSOD or a similar crash in the VM, utilities like `chkdsk` won't complete on restart before `qrexec_timeout` automatically halts the VM. That can really put the VM in a totally unrecoverable state, whereas with higher `qrexec_timeout`, `chkdsk` or the appropriate utility has plenty of time to fix the VM. Note that Qubes Windows Tools also require a larger timeout to move the user profiles to the private volume the first time the VM reboots after the tools' installation. So set the parameter via the following CLI command from a dom0 terminal, because the Qube manager does not support this setting:
  
**Start Windows VM**

- The VM is now ready to be started; the best practice is to use an installation ISO [located in a VM](/doc/standalones-and-hvms/#installing-an-os-in-an-hvm). Now boot the newly created qube from the Windows installation media. In the Qubes Manager:

  - Select the new qube, in this example "WindowsNew".
  - Switch to the "Advanced" tab.
  - Click "Boot from CDROM":
   - "from file in qube":
     - Select the qube that has the ISO.
     - Select ISO by clicking "...".
     - Click "OK" to boot into the windows installer.

   This can also be done via the following CLI command in dom0 (assuming that the Windows installer ISO is stored in the directory `/home/user/` in the AppVM `untrusted`):
    ~~~
    qvm-start --cdrom=untrusted:/home/user/windows_install.iso WindowsNew
    ~~~

- Install Windows on the new VM

  - At the first start, the Windows logo may be briefly shown, and then a black screen with a blinking cursor may appear and stay for a few minutes. This is normal, and you just have to wait until the installation window appears.
  - The installation will run mostly as usual, but automatic reboots will halt the qube - just restart it again and again until the installation is finished. Note, however, that for these restarts, the parameter `--cdrom` **must not** be used, because otherwise the installation will start all over.
  - Install on first disk.
  - **For Windows 11 only**: Windows 11 requires TPM 2.0, which currently is not supported from Xen. In Order to install Windows 11 under Qubes, the check for TPM in the Windows installer has to be disabled:
 
    -  When the window allowing you to select a Windows version is displayed, **do not select a version and close this window**, but instead type Shift-F10 to open a console window.
    -  Here you type `regedit` to start the registry editor.
    -  There you position to the key `HKEY_LOCAL_MACHINE\SYSTEM\Setup`.
    -  Now create the key `LabConfig`.
    -  Position to this key and create 3 DWORD values called `BypassTPMCheck`, `BypassSecureBootCheck` and `BypassRAMCheck` and set each value to `1`.
    -  Close the registry editor and console windows.
    -  You will then return to the setup, which will continue normally and install Windows 11 without TPM 2.0.
   
    :warning: **Caution:** This temporary patch may cease to work if it so pleases Microsoft sometime. With version 24H2 it is still working.
    
    The installation of Windows 11 may require an internet connection to grab a Microsoft ID. Previously, this was true only for the home edition, but since version 24H2, it extends to the Pro edition, too. A workaround to bypass the internet connection requirements of the Windows 11 setup has been published that works for version 21H2 but may be blocked for newer versions:
    
    - When you reach the “Let’s Connect You To A Network” page, type Shift-F10 to open a console window.
    - Here you type `taskmgr` to start the Task Manager window so you can see all running processes.
    - Expand the Task Manager by clicking the “More Details” button, and then find “Network Connection Flow.”
    - Select this process and then hit the “End Task” button.
    - Now you can close these newly opened windows and return to the Windows 11 setup, where you will enter local account information.
 
    For Windows 11 version 22H2, the following sequence of actions to use a local account instead of a Microsoft account has been published:

    - Enter `no@thankyou.com` (or some other senseless address) as the email address and click `Next` when Windows 11 setup prompts you to log into your Microsoft account.
    - Enter any text you want in the password field and click `Sign in`. If this method works, you'll get a message saying "Oops, something went wrong."
    - Click `Next`. A screen appears saying "Who's going to use this device?" This is the local account creation screen.
    - Enter the username you want to use and click `Next`.
    - Enter a password and click `Next`. You can leave the field blank but it's not recommended.
   
    For Windows 11 version 24H2, the following sequence of actions to use a local account instead of a Microsoft account has been proved working:

    For version 24H2, the following actions allow you to install Windows 11 with a local account, if the VM is defined, at least temporarily, without a netVM:
     - After some reboots, the VM will show a window allowing the selection of an installation country. In this window, type  Shift-F10 to open a console window.
     - In this window, type `oobe\bypassnro`. The VM will then reboot and return to the country selection window. The network connection window will now show an option "I don't have internet", allowing you to define a local account.

    In new preview builds of Windows (26120 and beyond, and eventually the next release version), the `oobe\bypassnro` command has been erased and no longer works. Instead, there's a new command called start `ms-chx:localonly` that does something similar. In this case, proceed as follows:
     - Follow the Windows 11 install process until you get to the Sign in screen. Here, type  Shift-F10 to open a console window.
     - Enter start `ms-cxh:localonly` at the command prompt.
     - A "Create a user for this PC" dialog window appears, allowing you to define a local account.

- On systems shipped with a Windows license, the product key may be read from flash via root in dom0:

    `strings < /sys/firmware/acpi/tables/MSDM`

    Alternatively, you can also try a Windows 7 license key (as of 2018/11 they are still accepted for a free upgrade to Windows 10).
    
 - The VM will shutdown after the installer completes the extraction of Windows installation files. It's a good idea to clone the VM now (eg. `qvm-clone WindowsNew WindowsNewbkp1`). Then, (re)start the VM via the Qubes Manager or with `qvm-start WindowsNew` from a dom0 terminal (without the `--cdrom` parameter!).

    The second part of Windows' installer should then be able to complete successfully.

**After Windows installation**

  - From the Windows command line, disable hibernation in order to avoid incomplete Windows shutdown, which could lead to corruption of the VM's disk. 
     ~~~
     powercfg -H off
     ~~~
    Also, recent versions of Windows won’t show the CD-ROM drive after starting the qube with `qvm-start vm --cdrom ...` (or using the GUI). The solution is to disable hibernation in Windows with this command. (That command is included in QWT’s setup but it’s necessary to run it manually in order to be able to open QWT’s setup ISO/CD-ROM in Windows).

  - In case you switch from `sys-firewall` to `sys-whonix`, you'll need a static IP network configuration, DHCP won't work for `sys-whonix`. Sometimes this may also happen if you keep using `sys-firewall`. In both cases, proceed as follows:
    - Check the IP address allocated to the qube - either from GUI Manager, or via `qvm-ls -n WindowsNew` from a dom0 terminal (E.g. 10.137.0.x with gateway 10.138.y.z).
    - In the Windows qube, open the Network manager and change the IPv4 configuration of the network interfacefrom "Automatic" to "Manual".
      - Enter the Address: 10.137.0.x in our example.
      - Enter the Netmask: 255.255.255.0
      - Enter the Gateway: 10.138.y.z in our example.
      - Enter DNS: 10.139.1.1,10.139.1.2 (the Virtual DNS addresses used by Qubes.
    - Click "Apply". You should now see "Connected".

  - Given the higher than usual memory requirements of Windows, you may get a `Not enough memory to start domain 'WindowsNew'` error. In that case try to shutdown unneeded VMs to free memory before starting the Windows VM.

    At this point you may open a tab in dom0 for debugging, in case something goes amiss:

     ~~~
     tailf /var/log/qubes/vm-WindowsNew.log \
        /var/log/xen/console/hypervisor.log \
        /var/log/xen/console/guest-WindowsNew-dm.log
     ~~~

At that point you should have a functional and stable Windows VM, although without updates, Xen's PV drivers nor Qubes integration (see sections [Windows Update](/doc/templates/windows/windows-qubes-4-1/#windows-update) and [Xen PV drivers and Qubes Windows Tools](/doc/templates/windows/qubes-windows-tools-4-1/#xen-pv-drivers-and-qubes-windows-tools)). It is a good time to clone the VM again.

**Installing Qubes Windows Tools**

To install Qubes Windows Tools, follow instructions in [Qubes Windows Tools](/doc/templates/windows/qubes-windows-tools-4-1), but don’t forget to `qvm-clone` your qube before you install Qubes Windows Tools (QWT) in case something goes south.

**Post-install best practices**

Optimize resources for use in virtual machine as “vanilla” version of Windows are bloated; e.g.:

- set up Windows for best performance (this pc → advanced settings → …)
- think about Windows’ page file: is it needed ? should you set it with a fixed size ? maybe on the private volume ?
- disable services you don’t need
- disable networking stuff in the network adapter’s setting (eg. link discovery, file and print server, …)
- background: set a solid color
- …

For additional information on configuring a Windows qube, see the [Customizing Windows 7 templates](/doc/windows-template-customization/) page (despite the focus on preparing the VM for use as a template, most of the instructions are independent from how the VM will be used - i.e. TemplateVM or StandaloneVM).

## Windows as a template

As described above Windows 7, 8.1, 10, and 11 can be installed as TemplateVM. To have the user data stored in AppVMs depending on this template, the user data have to be stored on a private disk named `Q:`. If there is already a disk for user data, possibly called `D:`, it has to be renamed to `Q:`. Otherwise, this disk has to be created via the Windows `diskpart` utility, or the Disk Management administrative function by formatting the qube's private volume and associating the letter `Q:` with it. The volume name is of no importance.

Moving the user data is not directly possible under Windows, because the directory `C:\Users` is permanently open and thus locked. Qubes Windows Tools provides a function to move these data on Windows reboot when the directory is not yet locked. To use this function, a working version of QWT has to be used (see the documentation on QWT installation). For Qubes R4.2, this is currently the version 4.1.69. There are two possibilities to move the user data to this volume `Q:`.

- If Qubes Windows Tools is installed, the option `Move User Profiles` has to be selected on the installation. In this case, the user files are moved to the new disk during the reboot at the end of the installation.

- This can also be accomplished without QWT installation, avoiding the installation of the Xen PV drivers, if the risk of a compromised version of these drivers according to QSB-091 is considered too severe. In this case, the file `relocate_dir.exe` has to be extracted from the QWT installer kit `qubes-tools-x64.msi`, which will be shown as the content of the CDROM made available by starting the Windows qube with the additional option `--install-windows-tools` (see the QWT installation documentation). The installer kit is a specially formatted archive, from which the file `relocate_dir.exe` can be extracted using a utility like 7-Zip. The file has then to be copied to `%windir%\system32`, i.e. usually `C:\Windows\system32`. Furthermore, locate the registry key `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager`, and add the text `relocate_dir.exe C:\Users Q:\Users` as a new line to the `REG_MULTI_SZ` value `\BootExecute` in this key. On rebooting the Windows qube, the user files will be moved to the disk `Q:`, and the additional registry entry will be removed, such that this action occurs only once.

If the user data have been moved to `Q:`, be sure not to user the option `Move User Profeiles`on subsequent installations of Qubes Windows tools.


AppVMs based on these templates can be created the normal way by using the Qube Manager or by specifying
~~~
qvm-create --class=AppVM --template=<VMname> 
~~~

On starting the AppVM, sometimes a message is displayed that the Xen PV Network Class needs to restart the system. This message can be safely ignored and closed by selecting "No".

**Caution:** These AppVMs must not be started while the corresponding TemplateVM is running, because they share the TemplateVM's license data. Even if this could work sometimes, it would be a violation of the license terms.

Furthermore, if manual IP setup was used for the template, the IP address selected for the template will also be used for the AppVM, as it inherits this address from the template. Qubes, however, will have assigned a different address to the AppVM, which will have to changed to that of the template (e.g. 10.137.0.x) so that the AppVM can access the network, vis the CLI command in a dom0 terminal:
~~~
qvm-prefs WindowsNew ip 10.137.0.x
~~~

## Windows 10 and 11 Usage According to GDPR

If Windows 10 or 11 is used in the EU to process personal data, according to GDPR no automatic data transfer to countries outside the EU is allowed without explicit consent of the person(s) concerned, or other legal consent, as applicable. Since no reliable way is found to completely control the sending of telemetry from Windows 10 or 11, the system containing personal data must be completely shielded from the internet.

This can be achieved by installing Windows 10 or 11 in a TemplateVM with the user data directory moved to a separate drive (usually `Q:`). Personal data must not be stored within the TemplateVM, but only in AppVMs depending on this TemplateVM. Network access by these AppVMs must be restricted to the local network and perhaps additional selected servers within the EU. Any data exchange of the AppVMs must be restricted to file and clipboard operations to and from other VMs in the same Qubes system.

## Windows update

Depending on how old your installation media is, fully updating your Windows VM may take *hours* (this isn't specific to Xen/Qubes) so make sure you clone your VM between the mandatory reboots in case something goes wrong. For Windows 7, you may find the necessary updates bundled at [WinFuture Windows 7 SP1 Update Pack 2.107 (Vollversion)](https://10gbit.winfuture.de/9Y6Lemoxl-I1_901xOu6Hg/1648348889/2671/Update%20Packs/2020_01/WinFuture_7SP1_x64_UpdatePack_2.107_Januar_2020-Vollversion.exe). At your own risk you may use such an installation image with bundled updates, but generally we do not recommend this way for security reasons - so, if you do it anyhow, check that you get this image from a source that you trust, which may be quite different from that one named here!

Note: if you already have Qubes Windows Tools installed the video adapter in Windows will be "Qubes video driver" and you won't be able to see the Windows Update process when the VM is being powered off because Qubes services would have been stopped by then. Depending on the size of the Windows update packs it may take a bit of time until the VM shutdowns by itself, leaving one wondering if the VM has crashed or still finalizing the updates (in dom0 a changing CPU usage - eg. shown with the domains widget in the task bar, or with `xentop` - usually indicates that the VM hasn't crashed).

To avoid guessing the VM's state enable debugging (`qvm-prefs -s WindowsNew debug true`) and in Windows' device manager (My computer -> Manage / Device manager / Display adapters) temporarily re-enable the standard VGA adapter and disable "Qubes video driver". You can disable debugging and revert to Qubes' display once the VM is updated.

## Troubleshooting

**Windows 7 - USB drives are not visible in your domain**

After Qubes Windows Tools have been installed on your Windows 7 system, please install the [Chipset_Driver_X2NF0_WN_2.1.39.0_A03.EXE driver](https://web.archive.org/web/20221007093126/https://dl.dell.com/FOLDER01557883M/3/Chipset_Driver_X2NF0_WN_2.1.39.0_A03.EXE). Then shut down your domain.

From now on you should be able to attach your USB drive by passing it from your *Qubes Devices* menu as a *USB device* rather than *Data (Block) Device*

This procedure has been tested on Windows 7 installed as a TemplateVM. Different combinations (such as StandaloneVM or different Windows versions) have not been tested.
