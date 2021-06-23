---
lang: en
layout: doc
permalink: /doc/standalones-and-hvms/
redirect_from:
- /doc/standalones-and-hvm/
- /doc/standalone-and-hvm/
- /doc/hvm/
- /doc/hvm-create/
- /en/doc/hvm-create/
- /doc/HvmCreate/
- /wiki/HvmCreate/
ref: 130
title: Standalones and HVMs
---

A [standalone](/doc/glossary/#standalone) is a type of qube that is created by cloning a [template](/doc/templates/).
Unlike templates, however, standalones do not supply their root filesystems to other qubes.
Examples of situations in which standalones can be useful include:

- Qubes used for development (dev environments often require a lot of specific packages and tools)
- Qubes used for installing untrusted packages.
  Normally, you install digitally signed software from Red Hat/Fedora repositories, and it's reasonable that such software has non malicious *installation* scripts (rpm pre/post scripts).
  However, when you would like to install some packages from less trusted sources, or unsigned, then using a dedicated (untrusted) standalone might be a better way.

Meanwhile, a [Hardware-assisted Virtual Machine (HVM)](/doc/glossary/#hvm), also known as a "Fully-Virtualized Virtual Machine," utilizes the virtualization extensions of the host CPU.
These are typically contrasted with Paravirtualized (PV) VMs.

HVMs allow you to create qubes based on any OS for which you have an installation ISO, so you can easily have qubes running Windows, *BSD, or any Linux distribution.
You can also use HVMs to run "live" distros.

By default, every Qubes VM runs in PVH mode (which has security advantages over both PV and HVM) except for those with attached PCI devices, which run in HVM mode.
See [here](https://blog.invisiblethings.org/2017/07/31/qubes-40-rc1.html) for a discussion of the switch from PV to HVM and [here](/news/2018/01/11/qsb-37/) for the announcement about the change to using PVH as default.

The standalone/template distinction and the HVM/PV/PVH distinctions are orthogonal.
The former is about root filesystem inheritance, whereas the latter is about the virtualization mode.
In practice, however, it is most common for standalones to be HVMs and for HVMs to be standalones.
Hence, this page covers both topics.

## Creating a standalone

You can create a standalone in the Qube Manager by selecting the "Type" of "Standalone qube copied from a template" or "Empty standalone qube (install your own OS)."

Alternatively, from the dom0 command line:

```
qvm-create --class StandaloneVM --label <LABEL> --property virt_mode=hvm <VMNAME>
```

(Note: Technically, `virt_mode=hvm` is not necessary for every standalone.
However, it makes sense if you want to use a kernel from within the VM.)

## Updating standalones

When you create a standalone from a template, the standalone is a complete
clone of the template, including the entire filesystem. After the moment of
creation, the standalone becomes completely independent from the template.
Therefore, the standalone will not be updated merely by updating the template
from which it was originally cloned. Rather, it must be updated as an
independent qube. See [How to Update](/doc/how-to-update/).

## Creating an HVM

### Using the GUI:

In Qube Manager, select "Create new qube" from the Qube menu, or select the "Create a new qube" button.
In the "create new qube" dialog box set Type to "Empty standalone qube (install your own OS)".
If "install system from device" is selected (which is by default), then `virt_mode` will be set to `hvm` automatically.
Otherwise, open the newly created qube's Settings GUI and in the "Advanced" tab select `HVM` in the virtualization mode drop-down list.
Also, make sure "Kernel" is set to `(none)` on the same tab.

## Command line:

Qubes are template-based by default so you must set the `--class StandaloneVM` option to create a standalone:
(name and label color are for illustration purposes).

~~~
qvm-create my-new-vm --class StandaloneVM --property virt_mode=hvm --property kernel='' --label=green
~~~

If you receive an error like this one, then you must first enable VT-x in your BIOS:

~~~
libvirt.libvirtError: invalid argument: could not find capabilities for arch=x86_64
~~~

Make sure that you give the new qube adequate memory to install and run.

## Installing an OS in an HVM

You will have to boot the qube with the installation media "attached" to it. You may either use the GUI or use command line instructions.
At the command line you can do this in three ways:

1. If you have the physical cdrom media and a disk drive

    ~~~
    qvm-start my-new-vm --cdrom=/dev/cdrom
    ~~~

2. If you have an ISO image of the installation media located in dom0

    ~~~
    qvm-start my-new-vm --cdrom=dom0:/usr/local/iso/installcd.iso
    ~~~

3. If you have an ISO image of the installation media located in a qube (obviously the qube where the media is located must be running)

    ~~~
    qvm-start my-new-vm --cdrom=someVM:/home/user/installcd.iso
    ~~~

For security reasons you should *never* copy untrusted data to dom0. Qubes doesn't provide any easy to use mechanism for copying files between qubes and Dom0 and generally tries to discourage such actions.

Next, the qube will start booting from the attached installation media, and you can start installation.
Whenever the installer wants to "reboot the system" it actually shuts down the qube, and Qubes won't automatically start it.
You may have to restart the qube several times in order to complete installation, (as is the case with Windows 7 installations).
Several invocations of `qvm-start` command (as shown above) might be needed.

## Setting up networking for HVMs

Just like standard paravirtualized app qubes, the HVM qubes get fixed IP addresses centrally assigned by Qubes.
Normally Qubes agent scripts (or services on Windows) running within each app qube are responsible for setting up networking within the VM according to the configuration created by Qubes (through [keys](/doc/vm-interface/#qubesdb) exposed by dom0 to the VM).
Such centrally managed networking infrastructure allows for [advanced networking configuration](https://blog.invisiblethings.org/2011/09/28/playing-with-qubes-networking-for-fun.html).

A generic HVM domain such as a standard Windows or Ubuntu installation, however, has no Qubes agent scripts running inside it initially and thus requires manual configuration of networking so that it matches the values assigned by Qubes for this qube.

Even though we do have a small DHCP server that runs inside HVM untrusted stub domain to make the manual network configuration unnecessary for many VMs, this won't work for most modern Linux distributions which contain Xen networking PV drivers (but not Qubes tools) which bypass the stub-domain networking (their net frontends connect directly to the net backend in the netvm).
In this instance our DHCP server is not useful.

In order to manually configure networking in a VM, one should first find out the IP/netmask/gateway assigned to the particular VM by Qubes.
This can be seen e.g. in the Qube Manager in the qube's properties:

![r2b1-manager-networking-config.png](/attachment/doc/r2b1-manager-networking-config.png)

Alternatively, one can use the `qvm-ls -n` command to obtain the same information, (IP/netmask/gateway).

The DNS IP addresses are `10.139.1.1` and `10.139.1.2`.
There is [opt-in support](/doc/networking/#ipv6) for IPv6 forwarding.

## Using TemplateBasedHVMs

Qubes allows HVMs to share a common root filesystem from a select template.
This mode can be used for any HVM (e.g. FreeBSD running in a HVM).

In order to create a TemplateHVM you use the following command, suitably adapted:

~~~
qvm-create --class TemplateVM <QUBE> --property virt_mode=HVM --property kernel=''  -l green
~~~

Set memory as appropriate, and install the OS into this template in the same way you would install it into a normal HVM.
Generally you should install in to the first "system" disk. (Resize it as needed before starting installation.)

You can then create a new qube using the new template.
If you use this Template as it is, then any HVMs that use it will effectively be disposables - all file system changes will be wiped when the HVM is closed down.

Please see [this page](https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows-tools.md) for specific advice on installing and using Windows-based templates.

## Cloning HVMs

Just like normal app qubes, the HVM domains can also be cloned either using the command-line `qvm-clone` or via the Qube Manager's 'Clone VM' option in the right-click menu.

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

Note how the MAC addresses differ between those two otherwise identical qubes.
The IP addresses assigned by Qubes will also be different of course to allow networking to function properly:

~~~
[joanna@dom0 ~]$ qvm-ls -n
/.../
         my-new-vm-copy |    |  Halted |   Yes |       | *firewallvm |  green |  10.137.2.3 |        n/a |  10.137.2.1 |
              my-new-vm |    |  Halted |   Yes |       | *firewallvm |  green |  10.137.2.7 |        n/a |  10.137.2.1 |
/.../
~~~

If for any reason you would like to make sure that the two qubes have the same MAC address, you can use `qvm-prefs` to set a fixed MAC address for the qube:

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

## Assigning PCI devices to HVMs

HVM domains (including Windows qubes) can be [assigned PCI devices](/doc/how-to-use-pci-devices/) just like normal app qubes.
E.g. one can assign one of the USB controllers to the Windows VM and should be able to use various devices that require Windows software, such as phones, electronic devices that are configured via FTDI, etc.

One problem at the moment however, is that after the whole system gets suspended into S3 sleep and subsequently resumed, some attached devices may stop working and should be restarted within the qube.
This can be achieved under a Windows HVM by opening the Device Manager, selecting the actual device (such as a USB controller), 'Disabling' the device, and then 'Enabling' the device again.
This is illustrated on the screenshot below:

![r2b1-win7-usb-disable.png](/attachment/doc/r2b1-win7-usb-disable.png)

## Converting VirtualBox VMs to Qubes HVMs

You can convert any VirtualBox VM to a Qubes HVM using this method.

For example, Microsoft provides [free 90 day evaluation VirtualBox VMs for browser testing](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/).

About 60 GB of disk space is required for conversion.
Use an external harddrive if needed.
The final root.img size is 40 GB.

In Debian app qube, install `qemu-utils` and `unzip`:

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

Copy the root image file from the originating qube (here called `untrusted`) to a temporary location in dom0, typing this in a Dom0 terminal:

~~~
qvm-run --pass-io untrusted 'cat "/media/user/externalhd/win10.raw"' > /home/user/win10-root.img
~~~

From within Dom0, create a new HVM (here called `win10`) with the root image we just copied to Dom0 (change the amount of RAM in GB as you wish):

~~~
qvm-create --property=virt_mode=hvm --property=memory=4096 --property=kernel='' --label red --standalone --root-move-from /home/user/win10-root.img win10
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

## Further reading

Other documents related to HVM:

- [Windows VMs](https://github.com/Qubes-Community/Contents/blob/master/docs/os/windows/windows-vm.md)
- [Linux HVM Tips](https://github.com/Qubes-Community/Contents/blob/master/docs/os/linux-hvm-tips.md)
