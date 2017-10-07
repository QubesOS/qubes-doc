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
=============================================================

What are HVM domains?
---------------------

HVM domains (Hardware VM), in contrast to PV domains (Paravirtualized domains), allow one to create domains based on any OS for which one has an installation ISO.  For example, this allows one to have Windows-based VMs in Qubes.

Interested readers might want to check [this article](https://blog.invisiblethings.org/2012/03/03/windows-support-coming-to-qubes.html) to learn why it took so long for Qubes OS to support HVM domains (Qubes 1 only supported Linux based PV domains).

Creating an HVM domain
----------------------

First, lets create a new HVM domain.  Use the --hvm switch to qvm-create, or choose HVM type in the Qubes Manager VM creation dialog box:

~~~
qvm-create win7 --hvm --label green
~~~

(The name of the domain ("win7") as well as it's label ("green") are just exemplary of course).

If you receive an error like this one, then you must first enable VT-x in your BIOS:

~~~
libvirt.libvirtError: invalid argument: could not find capabilities for arch=x86_64 
~~~

Now we need to install an OS inside this VM.  This can done by attaching an installation ISO to and starting the VM (this can currently only be done from command line, but in the future we will surely add an option to do this also from the manager):

~~~
qvm-start win7 --cdrom=/usr/local/iso/win7_en.iso
~~~

The above command assumes the installation ISO was transferred to Dom0 (copied using `dd` command from an installation CDROM for example). If one wishes to use the actual physical media without copying it first to a file, then one can just pass `/dev/cdrom` as an argument to `--cdrom`:

~~~
qvm-start win7 --cdrom=/dev/cdrom
~~~

Next the VM will start booting from the attached CDROM device (which in the example above just happens to be a Windows 7 installation disk). Depending on the OS that is being installed in the VM one might be required to start the VM several times (as is the case with Windows 7 installations), because whenever the installer wants to "reboot the system" it actually shutdowns the VM and Qubes won't automatically start it.  Several invocations of qvm-start command (as shown above) might be needed.

**Note:** If your Windows installation gets stuck at the glowing Windows logo, you might want to read [Issue 2488](https://github.com/QubesOS/qubes-issues/issues/2488) for a solution.

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

Copy file to Dom0:

~~~
qvm-run --pass-io untrusted 'cat "/media/user/externalhd/win10.raw"' > /var/lib/qubes/appvms/win10/root.img
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

Setting up networking for HVM domains
-------------------------------------

Just like standard paravirtualized AppVMs, the HVM domains get fixed IP addresses centrally assigned by Qubes. Normally Qubes agent scripts running within each AppVM are responsible for setting up networking within the VM according the configuration created by Qubes. Such centrally managed networking infrastructure allows for [advanced networking configuration](https://blog.invisiblethings.org/2011/09/28/playing-with-qubes-networking-for-fun.html).

A generic HVM domain such as a standard Windows or Ubuntu installation, however, has no Qubes agent scripts running inside it initially and thus requires manual networking configuration so that it match the values assigned by Qubes for this domain.

Even though we do have a small DHCP server that runs inside HVM untrusted stub domain to make the manual network configuration not necessary for many VMs, this won't work for most modern Linux distributions which contain Xen networking PV drivers (but not Qubes tools) built in which bypass the stub-domain networking (their net frontends connect directly to the net backend in the netvm).  In this instance our DHCP server is not useful.

In order to manually configure networking in a VM, one should first find out the IP/netmask/gateway assigned to the particular VM by Qubes. This can be seen e.g. in the Qubes Manager in the VM's properties:

![r2b1-manager-networking-config.png](/attachment/wiki/HvmCreate/r2b1-manager-networking-config.png)

Alternatively, one can use `qvm-ls -n` command to obtain the same information.  One should configure the networking within the HVM according to those settings (IP/netmask/gateway). One should set DNS addresses to the same IP as gateway.

Only IPv4 networking is currently supported in Qubes.

**Note:** If one plans on installing Qubes Tools for Windows guests (see below) it is 'not' necessary to configure networking manually as described in this section, because the tools will take care of setting the networking automatically for such Windows domains.

Using Template-based HVM domains
--------------------------------

Please see our dedicated page on [installing and using Windows-based AppVMs](/doc/windows-appvms/).

Cloning HVM domains
-------------------

Just like normal AppVMs, the HVM domains can also be cloned either using a command-line `qvm-clone` command or via manager's 'Clone VM' option in the right-click menu.

The cloned VM will get identical root and private image and will essentially be an identical of the original VM except that it will get a different MAC address for the networking interface:

~~~
[joanna@dom0 ~]$ qvm-prefs win7
name              : win7
label             : green
type              : HVM
netvm             : firewallvm
updateable?       : True
installed by RPM? : False
include in backups: False
dir               : /var/lib/qubes/appvms/win7
config            : /var/lib/qubes/appvms/win7/win7.conf
pcidevs           : []
root img          : /var/lib/qubes/appvms/win7/root.img
private img       : /var/lib/qubes/appvms/win7/private.img
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

[joanna@dom0 ~]$ qvm-clone win7 win7-copy

/.../

[joanna@dom0 ~]$ qvm-prefs win7-copy
name              : win7-copy
label             : green
type              : HVM
netvm             : firewallvm
updateable?       : True
installed by RPM? : False
include in backups: False
dir               : /var/lib/qubes/appvms/win7-copy
config            : /var/lib/qubes/appvms/win7-copy/win7-copy.conf
pcidevs           : []
root img          : /var/lib/qubes/appvms/win7-copy/root.img
private img       : /var/lib/qubes/appvms/win7-copy/private.img
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
         win7-copy |    |  Halted |   Yes |       | *firewallvm |  green |  10.137.2.3 |        n/a |  10.137.2.1 |
              win7 |    |  Halted |   Yes |       | *firewallvm |  green |  10.137.2.7 |        n/a |  10.137.2.1 |
/.../
~~~

If for any reason one would like to make sure that the two VMs have the same MAC address, one can use qvm-prefs to set a fixed MAC address for the VM:

~~~
[joanna@dom0 ~]$ qvm-prefs win7-copy -s mac 00:16:3E:5E:6C:05
[joanna@dom0 ~]$ qvm-prefs win7-copy
name              : win7-copy
label             : green
type              : HVM
netvm             : firewallvm
updateable?       : True
installed by RPM? : False
include in backups: False
dir               : /var/lib/qubes/appvms/win7-copy
config            : /var/lib/qubes/appvms/win7-copy/win7-copy.conf
pcidevs           : []
root img          : /var/lib/qubes/appvms/win7-copy/root.img
private img       : /var/lib/qubes/appvms/win7-copy/private.img
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

[![r2b1-win7-usb-disable.png](/attachment/wiki/HvmCreate/r2b1-win7-usb-disable.png)](/attachment/wiki/HvmCreate/r2b1-win7-usb-disable.png)

Further reading
---------------

Other documents related to HVM:

-   [LinuxHVMTips](/doc/linux-hvm-tips/)

