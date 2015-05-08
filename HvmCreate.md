---
layout: doc
title: HvmCreate
permalink: /doc/HvmCreate/
redirect_from: /wiki/HvmCreate/
---

Creating and using HVM (fully virtualized) domains in Qubes 2
=============================================================

What are HVM domains?
---------------------

HVM domains (Hardware VM), in contrast to PV domains (Paravirtualized domains), allow to create domains based on any OS, if one only has its installation ISO. E.g. this allows to have Windows-based VMs in Qubes.

Interested readers might want to check [this article](http://theinvisiblethings.blogspot.com/2012/03/windows-support-coming-to-qubes.html) to learn why it took so long for Qubes OS to support HVM domains (Qubes 1 only supported Linuxed-based PV domains).

Creating an HVM domain
----------------------

First, lets create a new HVM domain (use the --hvm switch to qvm-create, or choose HVM type in the Qubes Manager VM creation dialog box):

{% highlight trac-wiki %}
qvm-create win7 --hvm --label green
{% endhighlight %}

(Of course, the name of the domain ("win7"), as well as it's label ("green"), are just exemplary).

Now, we need to install an OS inside this VM, this can done by attaching an installation ISO upon starting the VM (this currently can be done only from command line, but in the future we surely will added an option to do this also from the manager):

{% highlight trac-wiki %}
qvm-start win7 --cdrom=/usr/local/iso/win7_en.iso
{% endhighlight %}

The command above assumes the installation ISO was somehow transferred to Dom0, e.g. copied using `dd` command from an installation CDROM. If one wishes to use the actual physical media without copying it first to a file, then one can just pass `/dev/cdrom` as an argument to `--cdrom`:

{% highlight trac-wiki %}
qvm-start win7 --cdrom=/dev/cdrom
{% endhighlight %}

Now, the VM will start booting from the attached CDROM device, which in the example above just happens to be the Windows 7 installation disk. Depending on the OS that is being installed in the VM, one might be required to start the VM several times (as is the case e.g. with Windows 7 installation), because whenever the installer wants to "reboot the system", it actually shutdowns the VM (and Qubes won't automatically start it), so several invocations of qvm-start command (as shown above) might be needed.

[![r2b1-win7-installing.png](attachment/wiki/HvmCreate/r2b1-win7-installing.png)](attachment/wiki/HvmCreate/r2b1-win7-installing.png)

Using Installation ISOs located in other VMs
--------------------------------------------

Sometimes one wants to download the installation ISO from the Web and use it for HVM creation. However, for security reasons, networking is disabled for Qubes Dom0, which makes it not possible to download an ISO within Dom0. Also Qubes do not provide any (easy to use) mechanisms for copying files between AppVMs and Dom0, and generally tries to discourage such actions. So, it would be inconvenient to require that the installation ISO for an HVM domain be always located in Dom0. And the good news is that this is indeed not required -- one can use the following syntax when specifying the location of /usr/local/iso/win7\_en.iso the installation ISO:

{% highlight trac-wiki %}
--cdrom=[appvm]:[/path/to/iso/within/appvm]
{% endhighlight %}

Assuming e.g. the an installation ISO named `ubuntu-12.10-desktop-i386.iso` has been downloaded in `work-web` AppVM, and located within `/home/user/Downloads` directory within this AppVM, one can immediately create a new HVM and use this ISO as an installation media with the following command (issued in Dom0, of course):

{% highlight trac-wiki %}
qvm-create --hvm ubuntu --label red
qvm-start ubuntu --cdrom=work-web:/home/user/Downloads/ubuntu-12.10-desktop-i386.iso
{% endhighlight %}

Of course the AppVM where the ISO is kept must also be running for this to work (this VM is now serving the ISO and acting as a disk backend).

![r2b1-installing-ubuntu-1.png](/attachment/wiki/HvmCreate/r2b1-installing-ubuntu-1.png)

Setting up networking for HVM domains
-------------------------------------

Just like standard (paravirtualized) AppVMs, the HVM domains got fixed IP addresses centrally assigned by Qubes. Normally Qubes agent scripts, running within each AppVM, are responsible for setting up networking within the VM according the configuration created by Qubes. Such centrally managed networking infrastructure allows for [advanced networking configuration](http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html).

However, a generic HVM domain, e.g. a standard Windows or Ubuntu installation, has (at least initially) no Qubes agent scripts running inside it, and thus requires manual networking configuration, so that it match the values assigned by Qubes for this domain.

Even though we do have a small DHCP server (that runs inside HVM untrusted stub domain) to make the manual network configuration not necessary for many VMs, this won't work for most modern Linux distributions which contain Xen networking PV drivers built in (but not Qubes tools) and which bypass the stub-domain networking (their net frontends connect directly to the net backend in the netvm), and so our DHCP server is not useful.

In order to manually configure networking in a VM, one should first find out the IP/netmask/gateway assigned to the particular VM by Qubes. This can be seen e.g. in the Qubes Manager in the VM's properties:

![r2b1-manager-networking-config.png](/attachment/wiki/HvmCreate/r2b1-manager-networking-config.png)

Alternatively, one can use `qvm-ls -n` command to obtain the same information.

Now, one should configure the networking within the HVM according to those settings (IP/netmask/gateway). Only IPv4 networking is currently supported in Qubes.

**Note:** If one plans on installing Qubes Tools for Windows guests (see below) it is 'not' necessary to configure networking manually as described in this section, because the tools will take care of setting the networking automatically for such Windows domains.

Using Template-based HVM domains
--------------------------------

TODO (Coming in Qubes R2 beta 3).

Cloning HVM domains
-------------------

Just like normal AppVMs, the HVM domains can also be cloned, either using a command-line `qvm-clone` command, or via manager's 'Clone VM' option in the right-click menu.

The cloned VM will get identical root and private image, and essentially will be identical to the original VM, except that it will get a different MAC address for the networking interface:

{% highlight trac-wiki %}
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
{% endhighlight %}

Note how the MAC addresses differ between those two, otherwise identical VMs. Of course, the IP addresses, assigned by Qubes, will also be different, to allow networking to function properly:

{% highlight trac-wiki %}
[joanna@dom0 ~]$ qvm-ls -n
/.../
         win7-copy |    |  Halted |   Yes |       | *firewallvm |  green |  10.137.2.3 |        n/a |  10.137.2.1 |
              win7 |    |  Halted |   Yes |       | *firewallvm |  green |  10.137.2.7 |        n/a |  10.137.2.1 |
/.../
{% endhighlight %}

If, for any reason, one would like to make sure that the two VMs have the same MAC address, one can use qvm-prefs to set a fixed MAC address for the VM:

{% highlight trac-wiki %}
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
{% endhighlight %}

Please note that as of now Qubes does not support shared templates for HVM domains. This means that HVM domains cloned this way will have two separate copies of the whole filesystems. This has consequences in taking much more disk space compared to standard AppVMs that share the root fs with the Template VM. Another consequence is that it's probably not legal to clone a proprietary OS, such as Windows this way, unless your license specifically allows for that (even though Windows Activation won't complain when one sets identical MAC address for the cloned VMs, it's doubtful practice at best).

In the near future we plan on introducing shared template also for HVM domains, hopefully solving the problems described above.

~~Installing Qubes support tools in Windows 7 VMs~~ (only for R2 Beta 2)
------------------------------------------------------------------------

Note: the R2 Beta 3 (which is coming soon) has automated most of the actions described below -- please see [this page instead](/wiki/WindowsAppVms).

Qubes support tools for Windows VMs is a set of programs and drivers that provide integration of Windows VMs with the rest of the Qubes system. Currently the following features become available for Windows VMs after installation of those tools:

-   Support for [secure clipboard copy/paste](/wiki/CopyPaste) between the Windows VM and other AppVMs
-   Support for [secure file exchange](/wiki/CopyingFiles) between the Windows VM and other AppVMs
-   Support for qvm-run and generic qrexec for the Windows VM (e.g. ability to run custom service within/from the Windows VM)
-   Xen PV drivers for Windows that increase performance compared to qemu emulated devices

Features that are currently not supported, but are planned for future releases (as soon as R2 Beta 2):

-   Video driver for Windows allowing custom resolutions (arbitrary HVM window resizing) and VM's mouse cursor hiding
-   Seamless app window mode, in which application windows are extracted and composed onto a common desktop just like it's currently done for Linux AppVMs. Currently Windows HVMs run in a window that contains the whole desktop of the VM.

Qubes Windows Support Tools are not open source and are distributed under a commercial license and their source code is not publicly available.

Because the Windows Support Tools are not licensed under a GPL license they are not distributed with Qubes installation ISO. Instead, one can download them when needed using the standard Qubes command for installing software in Dom0:

{% highlight trac-wiki %}
sudo qubes-dom0-update qubes-windows-tools
{% endhighlight %}

This should install `qubes-windows-tools-*.rpm` in your system, a package that brings an ISO with Windows Support Tools:

{% highlight trac-wiki %}
[joanna@dom0 ~]$ rpm -ql qubes-windows-tools-1-201211301354.noarch
/usr/lib/qubes/qubes-windows-tools-201211301354.iso
{% endhighlight %}

Now, in order to install the tools in a Windows VM one should start the VM with the ISO attached:

{% highlight trac-wiki %}
qvm-start lab-win7 --cdrom=/usr/lib/qubes/qubes-windows-tools-201211301354.iso
{% endhighlight %}

Once the Windows VM boots, a CDROM should appear in the 'My Computer' menu (typically as `D:`) with a setup program in its main directory:

[![r2b1-win7-installing-qubes-tools-1.png](/attachment/wiki/HvmCreate/r2b1-win7-installing-qubes-tools-1.png)](/attachment/wiki/HvmCreate/r2b1-win7-installing-qubes-tools-1.png)

Before proceeding with the installation we need to disable Windows mechanism that allows only signed drivers to be installed, because currently the drivers we provide as part of the Windows Support Tools are not digitally signed with a publicly recognizable certificate. How to do that is explained in the `README` file also located on the installation CDROM. In the future this step will not be necessary anymore, because we will sign our drivers with a publicly verifiable certificate. However, it should be noted that even now, the fact that those drivers are not digitally signed, this doesn't affect security of the Windows VM in 'any' way. This is because the actual installation ISO (the `qubes-windows-tools-*.iso` file) is distributed as a signed RPM package and its signature is verified by the `qubes-dom0-update` utility once it's being installed in Dom0. The only downside of those drivers not being signed is the inconvenience to the user that he or she must disable the signature enforcement policy before installing the tools, and also to accept a few scary looking warning windows during the installation process, as shown below.

[![r2b1-win7-installing-qubes-tools-2.png](/attachment/wiki/HvmCreate/r2b1-win7-installing-qubes-tools-2.png)](/attachment/wiki/HvmCreate/r2b1-win7-installing-qubes-tools-2.png)
[![r2b1-win7-installing-qubes-tools-4.png](/attachment/wiki/HvmCreate/r2b1-win7-installing-qubes-tools-4.png)](/attachment/wiki/HvmCreate/r2b1-win7-installing-qubes-tools-4.png)
[![r2b1-win7-installing-qubes-tools-5.png](/attachment/wiki/HvmCreate/r2b1-win7-installing-qubes-tools-5.png)](/attachment/wiki/HvmCreate/r2b1-win7-installing-qubes-tools-5.png)

After successful installation, the Windows VM must be shut down.

Additionally, once should inform Qubes that tools have been installed in this VM by setting the `qrexec_installed` flag in the VM's properties -- this can be done using the `qvm-prefs` command in Dom0, e.g.:

{% highlight trac-wiki %}
qvm-prefs lab-win7 -s qrexec_installed true
{% endhighlight %}

Also, by default Qubes assumes that the default user in the Windows VM is named `user` -- if one has chosen a different user during Windows installation, Qubes should be informed about this by setting the `default_user` property for the VM, e.g.:

{% highlight trac-wiki %}
qvm-prefs lab-win7 -s default_user joanna
{% endhighlight %}

If everything went fine (please remember about the need to reboot the Windows VM after installation of the tools), one can run some simple tests to see if qrexec service runs fine with this VM, e.g.:

{% highlight trac-wiki %}
qvm-run lab-win7 calc
{% endhighlight %}

... or something more fancy (a "networkless" telnet to Windows ;):

{% highlight trac-wiki %}
[joanna@dom0 ~]$ qvm-run lab-win7 -p cmd.exe
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>dir c:\
dir c:\
 Volume in drive C has no label.
 Volume Serial Number is 64FB-0198

 Directory of c:\

08/26/2012  12:06 PM    <DIR>          DRIVERS
12/12/2012  03:36 PM    <DIR>          Program Files
10/25/2012  12:12 PM    <DIR>          Program Files (x86)
03/22/2012  02:50 PM    <DIR>          SWTOOLS
03/02/2012  12:22 AM    <DIR>          Users
12/12/2012  03:40 PM    <DIR>          Windows
               0 File(s)              0 bytes
               6 Dir(s)   1,432,260,608 bytes free

C:\Windows\system32>exit
exit
{% endhighlight %}

Another things to check are if clipboard copy/paste and file copy works fine with this VM. If it doesn't, then perhaps one more VM reboot is necessary (seriously, hey this is Windows!).

And the screenshot below illustrates the Send To entries in a Windows VM that can be used to copy/send files to other Qubes domains:

[![win7-sendto-another-vm.png](/attachment/wiki/HvmCreate/win7-sendto-another-vm.png)](/attachment/wiki/HvmCreate/win7-sendto-another-vm.png)

Assigning PCI devices to HVM domains
------------------------------------

HVM domains (including Windows VMs) can be [assigned PCI devices](/wiki/AssigningDevices) just like normal AppVMs. E.g. one can assign one of the USB controllers to the Windows VM and should be able to use various devices that require Windows software, such as phones, electronic devices that are configured via FTDI, etc.

Once problem, however, at the moment, is that after the whole system gets suspend into S3 sleep, and subsequently resumed, such attached devices stop working and should be restarted within the VM. Under Windows this can be achieved by opening the Device Manager, selecting the actual device, such as a USB controller, and then first 'Disabling', and then 'Enabling' the device again. This is illustrated on the screenshot below:

[![r2b1-win7-usb-disable.png](/attachment/wiki/HvmCreate/r2b1-win7-usb-disable.png)](/attachment/wiki/HvmCreate/r2b1-win7-usb-disable.png)

Further reading
---------------

Other documents related to HVM:

-   [LinuxHVMTips](/wiki/LinuxHVMTips)

