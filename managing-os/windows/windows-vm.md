---
layout: doc
title: Installing a Windows VM
permalink: /doc/windows-vm/
---


Installing a Windows VM
=======================

Importing from R3.2 to R4.x
---------------------------

Importing should work, simply make sure that you are not using Xen's newer linux stubdomain and that the VM is in HVM mode (these steps should be done automatically when importing the VM):

R4.0:
~~~
qvm-features VMNAME linux-stubdom ''
qvm-prefs VMNAME virt_mode hvm
~~~

Note however that you are better off creating a new Windows VM to benefit from the more recent emulated hardware: R3.2 uses a MiniOS based stubdomain with an old and mostly unmaintained 'qemu-traditional' while R4.0 uses a Linux based stubdomain with a recent version of upstream qemu (see [this post](https://groups.google.com/d/msg/qubes-devel/tBqwJmOAJ94/xmFCGJnuAwAJ)).


Windows installation
----------------------

See [below](/doc/windows-vm/#command-summary) if you are only looking for a quick summary of the necessary commands.

MS Windows versions considerations:

- The instructions *may* work on other versions than Windows 7 x64 but haven't been tested.
- Qubes Windows Tools (QWT) only supports Windows 7 x64.


Create a VM named win7new in [HVM](/doc/hvm/) mode (Xen's current PVH limitations precludes from using PVH):

R3.2:
~~~
qvm-create win7new --hvm --label red
~~~

R4.0:
~~~
qvm-create --class StandaloneVM --label red --property virt_mode=hvm win7new
~~~

Windows' installer requires a significant amount of memory or else the VM will crash with such errors:

`/var/log/xen/console/hypervisor.log`:

> p2m_pod_demand_populate: Dom120 out of PoD memory! (tot=102411 ents=921600 dom120)
> (XEN) domain_crash called from p2m-pod.c:1218
> (XEN) Domain 120 (vcpu#0) crashed on cpu#3:

So, increase the VM's memory to 4000Mo (memory = maxmen because we don't use memory balancing).

R3.2:
~~~
qvm-prefs -s win7new memory 4000
qvm-prefs -s win7new maxmem 4000
~~~

R4.0:
~~~
qvm-prefs win7new memory 4000
qvm-prefs win7new maxmem 4000
~~~


On R4.0, disable direct boot so that the VM will go through the standard cdrom/HDD boot sequence:

~~~
qvm-prefs win7new kernel ''
~~~

A typical Windows 7 installation requires between 15Go up to 19Go of disk space depending on the version (Home/Professional/...). Windows updates also end up using significant space. So, extend the root volume from the default 10Go to 25Go (note: it is straightforward to increase the root volume size after Windows is installed: simply extend the volume again in dom0 and then extend the system partition with Windows's disk manager).

R3.2:
~~~
qvm-grow-root win7new 25g 
~~~

R4.0:
~~~
qvm-volume extend win7new:root 25g
~~~

Set the debug flag in order to have a graphical console:

R3.2:
~~~
qvm-prefs -s win7new debug true
~~~

R4.0:
~~~
qvm-prefs win7new debug true
~~~

The second part of the installation process will crash with the standard vga video adapter and the VM will stay in "transient" mode with the following error in `guest-win7new-dm.log`:

> qemu: /home/user/qubes-src/vmm-xen-stubdom-linux/build/qemu/exec.c:1187: cpu_physical_memory_snapshot_get_dirty: Assertion `start + length <= snap->end' failed.

To avoid that error we temporarily have to switch the video adapter to 'cirrus':

R3.2: backup the VM's configuration file and substitute the video driver from 'xen' to 'cirrus':
~~~
cp /var/lib/qubes/appvms/win7new/win7new.conf /tmp
sed -i "s/<model \+type='xen' \+vram=/<model type='cirrus' vram=/" /var/lib/qubes/appvms/win7new/win7new.conf
# or edit the file manually ; either way, make sure the adapter is now cirrus.
~~~

R4.0:
~~~
qvm-features win7new video-model cirrus
~~~

The VM is now ready to be started; the best practice is to use an installation ISO [located in a VM](/doc/hvm/#installing-an-os-in-an-hvm-domain):

~~~
qvm-start --cdrom=untrusted:/home/user/windows_install.iso win7new
~~~

Given the higher than usual memory requirements of Windows, you may get a `Not enough memory to start domain 'win7new'` error. In that case try to free memory by shutdown unneeded VMs before starting the Windows VM.

At this point you may open a few tabs in dom0 for debugging should something go amiss: 

~~~
tail -f /var/log/qubes/vm-win7new.log
tail -f /var/log/xen/console/hypervisor.log
tail -f /var/log/xen/console/guest-win7new-dm.log
~~~

The VM will shutdown after the installer completes the extraction of Windows installation files. It's a good idea to clone the VM now (eg. `qvm-clone win7new win7newbkp1`). Then, (re)start the VM with `qvm-start win7new`.

The second part of Windows' installer should then be able to complete successfully. You may then decrease the VM's memory to a more reasonable value:

R3.2:
~~~
qvm-prefs -s win7new memory 2000
qvm-prefs -s win7new maxmem 2000
~~~

R4.0:
~~~
qvm-prefs win7new memory 2000
qvm-prefs win7new maxmem 2000
~~~

Revert to the standard VGA adapter :

R3.2:
~~~
cp /tmp/win7new.conf /var/lib/qubes/appvms/win7new/win7new.conf
~~~

R4.0:
~~~
qvm-features --unset win7new video-model
~~~

At that point you should have a functional Windows VM, although without updates, Xen's PV drivers nor Qubes integration. It is a good time to clone the VM again.


Windows update
--------------

Depending on how old your installation media is, fully updating your Windows VM may take *hours* (this isn't specific to Xen/Qubes) so make sure you clone your VM between the mandatory reboots in case something goes wrong. This [comment](https://github.com/QubesOS/qubes-issues/issues/3585#issuecomment-366471111) provides useful links on updating a Windows 7 SP1 VM.

Note: if you already have Qubes Windows Tools installed the video adapter in Windows will be "Qubes video driver" and you won't be able to see the Windows Update process when the VM is being powered off because Qubes services would have been stopped by then. Depending on the size of the Windows update packs it may take a bit of time until the VM shutdowns by itself, leaving one wondering if the VM has crashed or still finalizing the updates (in dom0 a changing CPU usage - eg. shown with `xentop` - usually indicates that the VM hasn't crashed).
To avoid guessing the VM's state enable debugging (R3.2: `qvm-prefs -s win7new debug true`, R4.0: `qvm-prefs win7new debug true`) and in Windows' device manager (My computer -> Manage / Device manager / Display adapters) temporarily re-enable the standard VGA adapter and disable "Qubes video driver". You can disable debugging and revert to Qubes' display once the VM is updated.


Xen PV drivers + Qubes integration
----------------------------------

If you plan to update your newly isntalled Windows VM it is recommended that you do so *before* installing Qubes Windows Tools (QWT). If QWT are installed, you should temporarily re-enable the standard VGA adapter in Windows and disable Qubes' (see the section above).

Increase the VM's qrexec_timeout before installing QWT:

- The first time the VM is run after QWT is installed, some time is needed to move the user profiles to the private volume (if you didn't disable that step in the installer, of course).
- In case you happen to get a BSOD or a similar crash in the VM, chkdsk won't complete on restart before qrexec_timeout automatically halts the VM. That can really put the VM in a totally unrecoverable state, whereas with higher qrexec_timeout, chkdsk or the appropriate utility has plenty of time to fix the VM.

R3.2:
~~~
qvm-prefs -s win7new qrexec_timeout 300
~~~

R4.0:
~~~
qvm-prefs win7new qrexec_timeout 300
~~~

Installing QWT on R3.2: see [this page](/doc/windows-tools/)

Installing QWT on R4.0: you'll have to install QWT for Qubes R3.2. See [issue #3585](https://github.com/QubesOS/qubes-issues/issues/3585) for instructions and known issues.

Qubes Windows Tools install Xen's PV drivers by default so there is no need to install the [official ones](https://www.xenproject.org/developers/teams/windows-pv-drivers.html). *However*, Xen's VBD (storage) PV driver is disabled by default during QWT's setup and enabling it on a Windows 7 VM that isn't fully updated results in a BSOD and broken VM. Updating Windows takes *hours* and for casual usage there isn't much of a performance between the disk PV driver and the default one; so there is likely no need to go through the lengthy Windows Update process if your VM is isolated from the network and you don't use I/O intensive apps.
With a fully updated Windows 7 and QWT already installed (without the storage PV driver) you can install the storage PV driver from Xen's site (xenvbd.tar).

You can now turn off debugging (early graphical console):

R3.2:
~~~
qvm-prefs -s win7new debug false
~~~

R4.0:
~~~
qvm-prefs win7new debug false
~~~


Tweaks
------

- Set a fixed size page file size (system properties / advanced tab / Performance settings / advanced tab / Virtual memory / Change...) 
- Adjust for best performance (system properties / advanced tab /  Performance settings).


Command summary
-----------------

Most of the commands below can be combined into only a few commands but they are split for the sake of clarity.

R3.2:
~~~
qvm-create win7new --hvm --label red
qvm-prefs -s win7new memory 4000
qvm-prefs -s win7new maxmem 4000
qvm-grow-root win7new 25g 
qvm-prefs -s win7new debug true
cp /var/lib/qubes/appvms/win7new/win7new.conf /tmp
sed -i "s/<model \+type='xen' \+vram=/<model type='cirrus' vram=/" /var/lib/qubes/appvms/win7new/win7new.conf
qvm-start --cdrom=untrusted:/home/user/windows_install.iso win7new
# restart after the first part of the windows installation process ends
qvm-start win7new
# once Windows is installed and working
qvm-prefs -s win7new memory 2000
qvm-prefs -s win7new maxmem 2000
cp /tmp/win7new.conf /var/lib/qubes/appvms/win7new/win7new.conf
qvm-prefs -s win7new qrexec_timeout 300
# with Qubes Windows Tools installed:
qvm-prefs -s win7new debug false
~~~

R4.0:
~~~
qvm-create --class StandaloneVM --label red --property virt_mode=hvm win7new
qvm-prefs win7new memory 4000
qvm-prefs win7new maxmem 4000
qvm-prefs win7new kernel ''
qvm-volume extend win7new:root 25g
qvm-prefs win7new debug true
qvm-features win7new video-model cirrus
qvm-start --cdrom=untrusted:/home/user/windows_install.iso win7new
# restart after the first part of the windows installation process ends
qvm-start win7new
# once Windows is installed and working
qvm-prefs win7new memory 2000
qvm-prefs win7new maxmem 2000
qvm-features --unset win7new video-model
qvm-prefs win7new qrexec_timeout 300
# with Qubes Windows Tools installed:
qvm-prefs win7new debug false
~~~

