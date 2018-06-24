---
layout: doc
title: Creating and Using HVM Domains
permalink: /doc/hvm/
redirect_from:
- /doc/hvm-create/
- /en/doc/hvm-create/
- /doc/HvmCreate/
- /wiki/HvmCreate/
---

Creating and using HVM (fully virtualized) domains
==================================================

What are HVM domains?
---------------------

HVM domains (Hardware VM), in contrast to PV domains (Paravirtualized domains), allow one to create domains based on any OS for which one has an installation ISO.  For example, this allows one to have Windows-based VMs in Qubes.

Interested readers might want to check [this article](https://blog.invisiblethings.org/2012/03/03/windows-support-coming-to-qubes.html) to learn why it took so long for Qubes OS to support HVM domains (Qubes 1 only supported Linux based PV domains). As of Qubes 4, every VM is PVH by default, except those with attached PCI devices which are HVM. [See here](https://blog.invisiblethings.org/2017/07/31/qubes-40-rc1.html) for a discussion of the switch to HVM from R3.2's PV, and [here](/news/2018/01/11/qsb-37/) for changing the default to PVH.

Creating an HVM domain
----------------------

With a GUI: in Qubes Manager VM creation dialog box choose the "Standalone qube not based on a template" type. If "install system from device" is selected (which is by default), then `virt_mode` will be set to `hvm` automatically. Otherwise, open the newly created VM's Qube Settings GUI and in the "Advanced" tab select "HVM" in the virtualization mode drop-down list.

Command line (the VM's name and label color are for illustration purposes):

R3.2:
~~~
qvm-create my-new-vm --hvm --label green
~~~

R4.0: VMs are template-based by default so the `--class StandaloneVM` option is needed to create a StandaloneVM:
~~~
qvm-create my-new-vm --class StandaloneVM --property virt_mode=hvm 
~~~

Next the VM will start booting from the attached CDROM device (which in the example above just happens to be a Windows 7 installation disk). Depending on the OS that is being installed in the VM one might be required to start the VM several times (as is the case with Windows 7 installations), because whenever the installer wants to "reboot the system" it actually shutdowns the VM and Qubes won't automatically start it.  Several invocations of qvm-start command (as shown above) might be needed.

[![r2b1-win7-installing.png](/attachment/wiki/HvmCreate/r2b1-win7-installing.png)](/attachment/wiki/HvmCreate/r2b1-win7-installing.png)

Using Installation ISOs located in other VMs
--------------------------------------------

Sometimes one wants to download the installation ISO from the Web and use it for HVM creation.  For security reasons, networking is disabled for Qubes Dom0, which makes it impossible to download an ISO within Dom0.  Qubes also does not provide any easy to use mechanisms for copying files between AppVMs and Dom0 and generally tries to discourage such actions. Due to these factors it would be inconvenient to require that the installation ISO for an HVM domain be always located in Dom0.  The good news, however, is that this is indeed not required.  One can use the following syntax when specifying the location of an installation ISO (such as the Windows 7 installation ISO):

~~~
--cdrom=[appvm]:[/path/to/iso/within/appvm]
~~~

Assuming that an installation ISO named `ubuntu-12.10-desktop-i386.iso` has been downloaded in `work-web` AppVM and is located within the `/home/user/Downloads` directory within this AppVM, one can immediately create a new HVM using this ISO as an installation media with the following command issued in Dom0:

~~~
qvm-create --hvm ubuntu --label red
qvm-start ubuntu --cdrom=work-web:/home/user/Downloads/ubuntu-12.10-desktop-i386.iso
~~~

The AppVM where the ISO is kept must be running for this to work as this VM is now serving the ISO and acting as a disk backend.

![r2b1-installing-ubuntu-1.png](/attachment/wiki/HvmCreate/r2b1-installing-ubuntu-1.png)

Converting VirtualBox VM to HVM
-------------------------------

Microsoft provides [free 90 day evaluation VirtualBox VMs for browser testing](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/).

About 60 GB of disk space is required for conversion, use external harddrive if needed. Final root.img size is 40 GB.

In Debian AppVM, install qemu-utils and unzip:

~~~
sudo apt install qemu-utils unzip
~~~

Unzip VirtualBox zip file:

~~~
unzip *.zip 
~~~

Extract OVA tar archive:

~~~
tar -xvf *.ova
~~~

Convert vmdk to raw:

~~~
qemu-img convert -O raw *.vmdk win10.raw
~~~

Create new HVM in Dom0, with amount of RAM in MB you wish:

~~~
qvm-create --hvm win10 --label red --mem=4096
~~~

Because Windows image is a sparse file, tar it with -S option:

~~~
tar -Scf win10.raw.tar win10.raw
du -h win10.raw.tar
~~~

Copy file to Dom0:

~~~
qvm-run --pass-io untrusted 'cat "/media/user/externalhd/win10.raw.tar"' > win10.raw.tar
~~~

Untar the image and move to AppVM dir:

~~~
tar -xf win10.raw.tar win10.raw
mv win10.raw /var/lib/qubes/appvms/win10/root.img
~~~

Start win10 VM:
If you receive an error like this one, then you must first enable VT-x in your BIOS:

~~~
libvirt.libvirtError: invalid argument: could not find capabilities for arch=x86_64
~~~

Installing an OS in an HVM domain
---------------------------------

You will have to boot the VM with the installation media "attached" to it. You may either use the GUI or command line instructions. That can be accomplished in three ways:

1. If you have the physical cdrom media and a disk drive
    ~~~
    qvm-start my-new-vm --cdrom=/dev/cdrom
    ~~~
2. If you have an ISO image of the installation media located in dom0
    ~~~
    qvm-start my-new-vm --cdrom=dom0:/usr/local/iso/installcd.iso
    ~~~
3. If you have an ISO image of the installation media located in a VM (obviously the VM where the media is located must be running)
    ~~~
    qvm-start my-new-vm --cdrom=someVM:/home/user/installcd.iso
    ~~~

For security reasons you should *never* copy untrusted data to dom0. Qubes doesn't provide any easy to use mechanism for copying files between VMs and Dom0 anyway and generally tries to discourage such actions.

Next, the VM will start booting from the attached installation media. Depending on the OS being installed in the VM, one might be required to start the VM several times (as is the case with Windows 7 installations) because whenever the installer wants to "reboot the system" it actually shuts down the VM and Qubes won't automatically start it. Several invocations of `qvm-start` command (as shown above) might be needed.

Setting up networking for HVM domains
-------------------------------------

Just like standard paravirtualized AppVMs, the HVM domains get fixed IP addresses centrally assigned by Qubes.  Normally Qubes agent scripts (or services on Windows) running within each AppVM are responsible for setting up networking within the VM according the configuration created by Qubes (through [keys](/doc/vm-interface/#qubesdb) exposed by dom0 to the VM). Such centrally managed networking infrastructure allows for [advanced networking configuration](https://blog.invisiblethings.org/2011/09/28/playing-with-qubes-networking-for-fun.html).

A generic HVM domain such as a standard Windows or Ubuntu installation, however, has no Qubes agent scripts running inside it initially and thus requires manual networking configuration so that it match the values assigned by Qubes for this domain.

Even though we do have a small DHCP server that runs inside HVM untrusted stub domain to make the manual network configuration not necessary for many VMs, this won't work for most modern Linux distributions which contain Xen networking PV drivers (but not Qubes tools) built in which bypass the stub-domain networking (their net frontends connect directly to the net backend in the netvm).  In this instance our DHCP server is not useful.

In order to manually configure networking in a VM, one should first find out the IP/netmask/gateway assigned to the particular VM by Qubes. This can be seen e.g. in the Qubes Manager in the VM's properties:

![r2b1-manager-networking-config.png](/attachment/wiki/HvmCreate/r2b1-manager-networking-config.png)

Alternatively, one can use the `qvm-ls -n` command to obtain the same information and configure the networking within the HVM according to those settings (IP/netmask/gateway).

DNS servers: in R3.2 the DNS addresses are the same as the gateway's IP. In R4.0, the DNS ips are `10.139.1.1` and `10.139.1.2`.

Qubes R3.2 only supports IPv4. Qubes R4.0 has [opt-in support](https://www.qubes-os.org/doc/networking/#ipv6) for IPv6 forwarding.

Using Template-based HVM domains
--------------------------------

Please see our dedicated page on [installing and using Windows-based AppVMs](/doc/windows-appvms/).

Cloning HVM domains
-------------------

Just like normal AppVMs, the HVM domains can also be cloned either using a command-line `qvm-clone` command or via manager's 'Clone VM' option in the right-click menu.

The cloned VM will get identical root and private images and will essentially be identical to the original VM except that it will get a different MAC address for the networking interface:

~~~
[joanna@dom0 ~]$ qvm-prefs my-new-vm
name              : my-new-vm
label             : green
type              : HVM
netvm             : firewallvm
updateable?       : True
installed by RPM? : False
include in backups: False
dir               : /var/lib/qubes/appvms/my-new-vm
config            : /var/lib/qubes/appvms/my-new-vm/my-new-vm.conf
pcidevs           : []
root img          : /var/lib/qubes/appvms/my-new-vm/root.img
private img       : /var/lib/qubes/appvms/my-new-vm/private.img
vcpus             : 4
memory            : 512
maxmem            : 512
MAC               : 00:16:3E:5E:6C:05 (auto)
debug             : off
default user      : user
qrexec_installed  : False
qrexec timeout    : 60
drive             : None
timezone          : localtime

[joanna@dom0 ~]$ qvm-clone my-new-vm my-new-vm-copy

/.../

[joanna@dom0 ~]$ qvm-prefs my-new-vm-copy
name              : my-new-vm-copy
label             : green
type              : HVM
netvm             : firewallvm
updateable?       : True
installed by RPM? : False
include in backups: False
dir               : /var/lib/qubes/appvms/my-new-vm-copy
config            : /var/lib/qubes/appvms/my-new-vm-copy/my-new-vm-copy.conf
pcidevs           : []
root img          : /var/lib/qubes/appvms/my-new-vm-copy/root.img
private img       : /var/lib/qubes/appvms/my-new-vm-copy/private.img
vcpus             : 4
memory            : 512
maxmem            : 512
MAC               : 00:16:3E:5E:6C:01 (auto)
debug             : off
default user      : user
qrexec_installed  : False
qrexec timeout    : 60
drive             : None
timezone          : localtime
~~~

Note how the MAC addresses differ between those two otherwise identical VMs. The IP addresses assigned by Qubes will also be different of course to allow networking to function properly:

~~~
[joanna@dom0 ~]$ qvm-ls -n
/.../
         my-new-vm-copy |    |  Halted |   Yes |       | *firewallvm |  green |  10.137.2.3 |        n/a |  10.137.2.1 |
              my-new-vm |    |  Halted |   Yes |       | *firewallvm |  green |  10.137.2.7 |        n/a |  10.137.2.1 |
/.../
~~~

If for any reason one would like to make sure that the two VMs have the same MAC address, one can use qvm-prefs to set a fixed MAC address for the VM:

~~~
[joanna@dom0 ~]$ qvm-prefs my-new-vm-copy -s mac 00:16:3E:5E:6C:05
[joanna@dom0 ~]$ qvm-prefs my-new-vm-copy
name              : my-new-vm-copy
label             : green
type              : HVM
netvm             : firewallvm
updateable?       : True
installed by RPM? : False
include in backups: False
dir               : /var/lib/qubes/appvms/my-new-vm-copy
config            : /var/lib/qubes/appvms/my-new-vm-copy/my-new-vm-copy.conf
pcidevs           : []
root img          : /var/lib/qubes/appvms/my-new-vm-copy/root.img
private img       : /var/lib/qubes/appvms/my-new-vm-copy/private.img
vcpus             : 4
memory            : 512
maxmem            : 512
MAC               : 00:16:3E:5E:6C:05
debug             : off
default user      : user
qrexec_installed  : False
qrexec timeout    : 60
drive             : None
timezone          : localtime
~~~

Installing Qubes support tools in Windows 7 VMs
-----------------------------------------------

Windows specific steps are described on [separate page](/doc/windows-appvms/).

Assigning PCI devices to HVM domains
------------------------------------

HVM domains (including Windows VMs) can be [assigned PCI devices](/doc/assigning-devices/) just like normal AppVMs. E.g. one can assign one of the USB controllers to the Windows VM and should be able to use various devices that require Windows software, such as phones, electronic devices that are configured via FTDI, etc.

One problem at the moment however, is that after the whole system gets suspended into S3 sleep and subsequently resumed, some attached devices may stop working and should be restarted within the VM. This can be achieved under a Windows HVM by opening the Device Manager, selecting the actual device (such as a USB controller), 'Disabling' the device, and then 'Enabling' the device again. This is illustrated on the screenshot below:

![r2b1-win7-usb-disable.png](/attachment/wiki/HvmCreate/r2b1-win7-usb-disable.png)

Converting VirtualBox VM to HVM
-------------------------------

Microsoft provides [free 90 day evaluation VirtualBox VMs for browser testing](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/).

About 60 GB of disk space is required for conversion, use external harddrive if needed. Final root.img size is 40 GB.

In Debian AppVM, install qemu-utils and unzip:

~~~
sudo apt install qemu-utils unzip
~~~

Unzip VirtualBox zip file:

~~~
unzip *.zip
~~~

Extract OVA tar archive:

~~~
tar -xvf *.ova
~~~

Convert vmdk to raw:

~~~
qemu-img convert -O raw *.vmdk win10.raw
~~~

Copy the root image file to a temporary location in Dom0:

~~~
qvm-run --pass-io untrusted 'cat "/media/user/externalhd/win10.raw"' > /home/user/win10-root.img
~~~

Create a new HVM in Dom0 with the root image we just copied to Dom0 (change the amount of RAM in GB as you wish):

~~~
qvm-create --hvm win10 --label red --mem=4096 --root-move-from /home/user/win10-root.img
~~~

Start win10 VM:

~~~
qvm-start win10
~~~

**Optional ways to get more information**

Filetype of OVA file:

~~~
file *.ova
~~~

List files of OVA tar archive:

~~~
tar -tf *.ova
~~~

List filetypes supported by qemu-img:

~~~
qemu-img -h | tail -n1
~~~


Further reading
---------------

Other documents related to HVM:

-   [Windows VMs](/doc/windows-vm/)
-   [LinuxHVMTips](/doc/linux-hvm-tips/)
