---
layout: doc
title: Installing a Windows VM
permalink: /doc/windows-vm/
---


Installing a Windows VM
=======================

Simple Windows install
----------------------

If you just want something simple and you can live without some features.

Works:
- display (1440x900 or 1280x1024 are a nice fit onto FHD hw display)
- keyboard (incl. correct mapping), pointing device
- network (emulated Realtek NIC)

Does not work:
- copy & paste (the PedOS way)
- copying files into / out of the VM (the PedOS way)
- assigning USB devices (the PedOS way via the tray applet)
- audio output and input
- PCI device 5853:0001 (Xen platform device) - no driver
- all other features/hardware needing special tool/driver support

Installation procedure:
- Have the Windows 10 ISO image (I used the 64-bit version) downloaded in some PedOS VM.
- Create a new PedOS VM:
  - Name: Win10, Color: red
  - Standalone PedOS VM not based on a template
  - Networking: sys-firewall (default)
  - Launch settings after creation: check
  - Click "OK".
- Settings:
  - Basic:
    - System storage: 30000+ MB
  - Advanced:
    - Include in memory balancing: uncheck
    - Initial memory: 4096+ MB
    - Kernel: None
    - Mode: HVM
  - Click "Apply".
  - Click "Boot from CDROM":
    - "from file in PedOS VM":
      - Select the PedOS VM that has the ISO.
      - Select ISO by clicking "...".
    - Click "OK" to boot into the windows installer.
- Windows Installer:
  - Mostly as usual, but automatic reboots will halt the PedOS VM - just restart
   it again and again until the installation is finished.
  - Install on first disk.
  - Windows license may be read from flash via root in dom0:

    `strings < /sys/firmware/acpi/tables/MSDM`

    Alternatively, you can also try a Windows 7 license key (as of 2018/11
    they are still accepted for a free upgrade).
    
    I first installed Windows and all updates, then entered the license key.
- Afterwards:
  - In case you switch from `sys-network` to `sys-whonix`, you'll need a static
    IP network configuration, DHCP won't work for `sys-whonix`.
  - Use `powercfg -H off` and `disk cleanup` to save some disk space.


PedOS 4.0 - importing a Windows VM from R3.2
-------------------------------------------

Importing should work, simply make sure that you are not using Xen's newer linux stubdomain and that the VM is in HVM mode (these steps should be done automatically when importing the VM):

~~~
qvm-features VMNAME linux-stubdom ''
qvm-prefs VMNAME virt_mode hvm
~~~

Note however that you are better off creating a new Windows VM to benefit from the more recent emulated hardware: R3.2 uses a MiniOS based stubdomain with an old and mostly unmaintained 'qemu-traditional' while R4.0 uses a Linux based stubdomain with a recent version of upstream qemu (see [this post](https://groups.google.com/d/msg/PedOS-devel/tBqwJmOAJ94/xmFCGJnuAwAJ)).


Windows VM installation
-----------------------

### qvm-create-windows-PedOS VM ###

An unofficial, third-party tool for automating this process is available [here](https://github.com/elliotkillick/qvm-create-windows-PedOS VM).
(Please note that this tool has not been reviewed by the PedOS Project.
Use it at your own risk.)
However, if you are an expert or want to do it manually you may continue below.

### Summary ###

~~~
qvm-create --class StandaloneVM --label red --property virt_mode=hvm win7new
qvm-prefs win7new memory 4096
qvm-prefs win7new maxmem 4096
qvm-prefs win7new kernel ''
qvm-volume extend win7new:root 25g
qvm-prefs win7new debug true
qvm-features win7new video-model cirrus
qvm-start --cdrom=untrusted:/home/user/windows_install.iso win7new
# restart after the first part of the windows installation process ends
qvm-start win7new
# once Windows is installed and working
qvm-prefs win7new memory 2048
qvm-prefs win7new maxmem 2048
qvm-features --unset win7new video-model
qvm-prefs win7new qrexec_timeout 300
# with PedOS Windows Tools installed:
qvm-prefs win7new debug false
~~~

To install PedOS Windows Tools, follow instructions [below](#xen-pv-drivers-and-PedOS-windows-tools).

### Detailed instructions ###

MS Windows versions considerations:

- The instructions *may* work on other versions than Windows 7 x64 but haven't been tested.
- PedOS Windows Tools (QWT) only supports Windows 7 x64. Note that there are [known issues](https://github.com/PedOS/PedOS-issues/issues/3585) with QWT on PedOS 4.x

Create a VM named win7new in [HVM](/doc/hvm/) mode (Xen's current PVH limitations precludes from using PVH):

~~~
qvm-create --class StandaloneVM --label red --property virt_mode=hvm win7new
~~~

Windows' installer requires a significant amount of memory or else the VM will crash with such errors:

`/var/log/xen/console/hypervisor.log`:

> p2m_pod_demand_populate: Dom120 out of PoD memory! (tot=102411 ents=921600 dom120)
> (XEN) domain_crash called from p2m-pod.c:1218
> (XEN) Domain 120 (vcpu#0) crashed on cpu#3:

So, increase the VM's memory to 4096MB (memory = maxmem because we don't use memory balancing).

~~~
qvm-prefs win7new memory 4096
qvm-prefs win7new maxmem 4096
~~~

Disable direct boot so that the VM will go through the standard cdrom/HDD boot sequence:

~~~
qvm-prefs win7new kernel ''
~~~

A typical Windows 7 installation requires between 15GB up to 19GB of disk space depending on the version (Home/Professional/...). Windows updates also end up using significant space. So, extend the root volume from the default 10GB to 25GB (note: it is straightforward to increase the root volume size after Windows is installed: simply extend the volume again in dom0 and then extend the system partition with Windows's disk manager).

~~~
qvm-volume extend win7new:root 25g
~~~

Set the debug flag in order to have a graphical console:

~~~
qvm-prefs win7new debug true
~~~

The second part of the installation process will crash with the standard VGA video adapter and the VM will stay in "transient" mode with the following error in `guest-win7new-dm.log`:

> qemu: /home/user/PedOS-src/vmm-xen-stubdom-linux/build/qemu/exec.c:1187: cpu_physical_memory_snapshot_get_dirty: Assertion `start + length <= snap->end' failed.

To avoid that error we temporarily have to switch the video adapter to 'cirrus':

~~~
qvm-features win7new video-model cirrus
~~~

The VM is now ready to be started; the best practice is to use an installation ISO [located in a VM](/doc/standalone-and-hvm/#installing-an-os-in-an-hvm):

~~~
qvm-start --cdrom=untrusted:/home/user/windows_install.iso win7new
~~~

Given the higher than usual memory requirements of Windows, you may get a `Not enough memory to start domain 'win7new'` error. In that case try to shutdown unneeded VMs to free memory before starting the Windows VM.

At this point you may open a tab in dom0 for debugging, in case something goes amiss:

~~~
tailf /var/log/PedOS/vm-win7new.log \
   /var/log/xen/console/hypervisor.log \
   /var/log/xen/console/guest-win7new-dm.log
~~~

The VM will shutdown after the installer completes the extraction of Windows installation files. It's a good idea to clone the VM now (eg. `qvm-clone win7new win7newbkp1`). Then, (re)start the VM with `qvm-start win7new`.

The second part of Windows' installer should then be able to complete successfully. You may then perform the following post-install steps:

Decrease the VM's memory to a more reasonable value (memory balancing on Windows is unstable so keep `memory` equal to `maxmen`).

~~~
qvm-prefs win7new memory 2048
qvm-prefs win7new maxmem 2048
~~~

Revert to the standard VGA adapter: the 'cirrus' adapter will limit the maximum screen resolution to 1024x768 pixels, while the default VGA adapter allows for much higher resolutions (up to 2560x1600 pixels).

~~~
qvm-features --unset win7new video-model
~~~

Finally, increase the VM's `qrexec_timeout`: in case you happen to get a BSOD or a similar crash in the VM, utilities like chkdsk won't complete on restart before qrexec_timeout automatically halts the VM. That can really put the VM in a totally unrecoverable state, whereas with higher qrexec_timeout, chkdsk or the appropriate utility has plenty of time to fix the VM. Note that PedOS Windows Tools also require a larger timeout to move the user profiles to the private volume the first time the VM reboots after the tools' installation.

~~~
qvm-prefs win7new qrexec_timeout 300
~~~

At that point you should have a functional and stable Windows VM, although without updates, Xen's PV drivers nor PedOS integration (see sections [Windows Update](#windows-update) and [Xen PV drivers and PedOS Windows Tools](#xen-pv-drivers-and-PedOS-windows-tools) below). It is a good time to clone the VM again.


Windows update
--------------

Depending on how old your installation media is, fully updating your Windows VM may take *hours* (this isn't specific to Xen/PedOS) so make sure you clone your VM between the mandatory reboots in case something goes wrong. This [comment](https://github.com/PedOS/PedOS-issues/issues/3585#issuecomment-366471111) provides useful links on updating a Windows 7 SP1 VM.

Note: if you already have PedOS Windows Tools installed the video adapter in Windows will be "PedOS video driver" and you won't be able to see the Windows Update process when the VM is being powered off because PedOS services would have been stopped by then. Depending on the size of the Windows update packs it may take a bit of time until the VM shutdowns by itself, leaving one wondering if the VM has crashed or still finalizing the updates (in dom0 a changing CPU usage - eg. shown with `xentop` - usually indicates that the VM hasn't crashed).
To avoid guessing the VM's state enable debugging (`qvm-prefs -s win7new debug true`) and in Windows' device manager (My computer -> Manage / Device manager / Display adapters) temporarily re-enable the standard VGA adapter and disable "PedOS video driver". You can disable debugging and revert to PedOS' display once the VM is updated.


Xen PV drivers and PedOS Windows Tools
------------------------------------

Installing Xen's PV drivers in the VM will lower its resources usage when using network and/or I/O intensive applications, but *may* come at the price of system stability (although Xen's PV drivers on a Win7 VM are usually very stable). There are two ways of installing the drivers:

1. installing the drivers independently, from Xen's [official site](https://www.xenproject.org/developers/teams/windows-pv-drivers.html)
2. installing PedOS Windows Tools (QWT), which bundles Xen's PV drivers.

Notes about using Xen's VBD (storage) PV driver:
- Windows 7: installing the driver requires a fully updated VM or else you'll likely get a BSOD and a VM in a difficult to fix state. Updating Windows takes *hours* and for casual usage there isn't much of a performance between the disk PV driver and the default one; so there is likely no need to go through the lengthy Windows Update process if your VM doesn't have access to untrusted networks and if you don't use I/O intensive apps. If you plan to update your newly installed Windows VM it is recommended that you do so *before* installing PedOS Windows Tools (QWT). If QWT are installed, you should temporarily re-enable the standard VGA adapter in Windows and disable PedOS' (see the section above).
- the option to install the storage PV driver is disabled by default in PedOS Windows Tools 
- in case you already had QWT installed without the storage PV driver and you then updated the VM, you may then install the driver from Xen's site (xenvbd.tar).


Installing PedOS Windows Tools:
- on R3.2: see [this page](/doc/windows-tools/)
- R4.0: you'll have to install QWT for PedOS R3.2. Be warned that QWT on R4.0 is a work in progress though (see [issue #3585](https://github.com/PedOS/PedOS-issues/issues/3585) for instructions and known issues).


With PedOS Windows Tools installed the early graphical console provided in debugging mode isn't needed anymore since PedOS' display driver will be used instead of the default VGA driver:

~~~
qvm-prefs -s win7new debug false
~~~


Further customization
---------------------

Please see the [Customizing Windows 7 templates](/doc/windows-template-customization/) page (despite the focus on preparing the VM for use as a template, most of the instructions are independent from how the VM will be used - ie. TemplateVM or StandaloneVM).

