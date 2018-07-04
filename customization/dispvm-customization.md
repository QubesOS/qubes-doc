---
layout: doc
title: Disposable VM Customization
permalink: /doc/dispvm-customization/
redirect_from:
- /en/doc/dispvm-customization/
- /doc/DispVMCustomization/
- /doc/UserDoc/DispVMCustomization/
- /wiki/UserDoc/DispVMCustomization/
---

Disposable VM Customization
============================

Qubes 4.0
----------

Disposable VM (DispVM) in Qubes 4.0 can be based on any TemplateBasedVM. You can also choose to use different AppVMs for different Disposable VMs. To prepare AppVM to be a base for Disposable VM, you need to set `template_for_dispvms` property, for example:

    [user@dom0 ~]$ qvm-prefs fedora-26-dvm template_for_dispvms True

Additionally, if you want to have menu entries for starting applications in Disposable VM based on this AppVM (instead of in the AppVM itself), you can achieve it with `appmenus-dispvm` feature:

    [user@dom0 ~]$ qvm-features fedora-26-dvm appmenus-dispvm 1

### Creating new Disposable VM base AppVM ###

In Qubes 4.0, you're no longer restricted to a single DVM Template. Instead, you can create as many as you want. Whenever you start a new Disposable VM, you can choose to base it on whichever DVM Template you like.
To create new DVM Template, lets say `custom-dvm`, based on `debian-9` template, use following commands:

    [user@dom0 ~]$ qvm-create --template debian-9 --label red custom-dvm
    [user@dom0 ~]$ qvm-prefs custom-dvm template_for_dispvms True
    [user@dom0 ~]$ qvm-features custom-dvm appmenus-dispvm 1

Additionally you may want to set it as default DVM Template:

    [user@dom0 ~]$ qubes-prefs default_dispvm custom-dvm

The above default is used whenever a qube request starting a new Disposable VM and do not specify which one (for example `qvm-open-in-dvm` tool). This can be also set in qube settings and will affect service calls from that qube. See [qrexec documentation](/doc/qrexec3/#extra-keywords-available-in-qubes-40-and-later) for details.

If you wish to use the `fedora-minimal` template as a DVM Template, see the "DVM Template" use case under [fedora-minimal customization](/doc/templates/fedora-minimal/#customization).


### Customization of Disposable VM ###

It is possible to change the settings for each new Disposable VM (DispVM). This can be done by customizing the base AppVM:

1.  Start a terminal in the `fedora-26-dvm` qube (or another base for DispVM) by running the following command in a dom0 terminal. (If you enable `appmenus-dispvm` feature (as explained at the top), applications menu for this VM (`fedora-26-dvm`) will be "Disposable: fedora-26-dvm" (instead of "Domain: fedora-26-dvm") and entries there will start new DispVM based on that VM (`fedora-26-dvm`). Not in that VM (`fedora-26-dvm`) itself).

        [user@dom0 ~]$ qvm-run -a fedora-26-dvm gnome-terminal

2.  Change the qube's settings and/or applications, as desired. Some examples of changes you may want to make include:
    -   Changing Firefox's default startup settings and homepage.
    -   Changing default editor, image viewer.
    -   Changing the DispVM's default NetVM. For example, you may wish to set the NetVM to "none." Then, whenever you start a new DispVM, you can choose your desired ProxyVM manually (by changing the newly-started DispVMs settings). This is useful if you sometimes wish to use a DispVM with a Whonix Gateway, for example. It is also useful if you sometimes wish to open untrusted files in a network-disconnected DispVM.

4.  Shutdown the qube (either by `poweroff` from qube's terminal, or `qvm-shutdown` from dom0 terminal).


### Using static Disposable VMs for sys-* ###

You can use a static DispVM for `sys-*` as long as it is stateless.
For example, a `sys-net` using DHCP or `sys-usb` will work.
In most cases `sys-firewall` will also work, even if you have configured AppVM firewall rules.
The only exception is if you require something like VM to VM communication and have manually edited `iptables` or other items directly inside the firewall AppVM.

To create one that has no PCI devices attached, such as for `sys-firewall`:

~~~
qvm-create -C DispVM -l red <sys-VMName>
qvm-prefs <sys-VMName> autostart true
qvm-prefs <sys-VMName> netvm <sys-net>
qvm-prefs <sys-VMName> provides_network true
~~~

Next, set the old `sys-firewall` autostart to false, and update any references to the old one to instead point to the new.
For example, with `qvm-prefs work netvm sys-firewall2`.

To create one with a PCI device attached such as for `sys-net` or `sys-usb`, use the additional commands as follows.

**Note** You can use `qvm-pci` to [determine](/doc/assigning-devices/#r40) the `<BDF>`.
Also, you will often need to include the `-o no-strict-reset=True` [option](/doc/assigning-devices/#r40-1) with USB controllers.

~~~
qvm-create -C DispVM -l red <sys-VMName>
qvm-prefs <sys-VMName> virt_mode hvm
qvm-service <sys-VMName> meminfo-writer off
qvm-pci attach --persistent <sys-VMName> dom0:<BDF>
qvm-prefs <sys-VMName> autostart true
qvm-prefs <sys-VMName> netvm ''
# optional, if this DispVM will be providing networking
qvm-prefs <sys-VMName> provides_network true
~~~

Next, set the old `sys-` VM's autostart to false, and update any references to the old one.
For example, `qvm-prefs sys-firewall netvm <sys-VMName>`.
See below for a complete example of a `sys-net` replacement:

~~~
qvm-create -C DispVM -l red sys-net2
qvm-prefs sys-net2 virt_mode hvm
qvm-service sys-net2 meminfo-writer off
qvm-pci attach --persistent sys-net2 dom0:00_1a.0
qvm-prefs sys-net2 autostart true
qvm-prefs sys-net2 netvm ''
qvm-prefs sys-net2 provides_network true
qvm-prefs sys-net autostart false
qvm-prefs sys-firewall netvm sys-net2
qubes-prefs clockvm sys-net2
~~~

Note that these types of DispVMs will not show in the Application menu, but you can still get to a terminal if needed with `qvm-run <sys-VMName> gnome-terminal`.

### Adding programs to Disposable VM Application Menu ###

For added convenience, arbitrary programs can be added to the Application Menu of the Disposable VM. 

In order to do that, select "Qube settings" entry in selected base AppVM, go to "Applications" tab and select desired applications as for any other qube.

Note that currently only applications whose main process keeps running until you close the application (i.e. do not start a background process instead) will work. One of known examples of incompatible applications is GNOME Terminal (shown on the list as "Terminal"). Choose different terminal emulator (like XTerm) instead.

### Create Custom sys-net sys-firewall and sys-usb DispVMs ###

Users have the option of creating customized DispVMs for the `sys-net`, `sys-firewall` and `sys-usb` VMs. In this configuration, a fresh VM instance is created each time a DispVM is launched. Functionality is near-identical to the default VMs created following a new Qubes’ installation, except the user benefits from a non-persistent filesystem.

Functionality is not limited, users can:

   * Set custom firewall rule sets and run Qubes VPN scripts. 
   * Set DispVMs to autostart at system boot.
   * Attach PCI devices with the `--persistent` option. 

Using DispVMs in this manner is ideal for untrusted qubes which require persistent PCI devices, such as USB VMs and NetVMs.

>_**Note:**_ Users who want customized VPN or firewall rule sets must create a separate dvm for use by each DispVM. If dvm customization is not needed, then a single dvm is used as a template for all DispVMs.
 
#### Create and configure the dvm from which the DispVM will be based on ####

   1. Create the dvm 

    [user@dom0 ~]$ qvm-create --class AppVM --label gray <dvm-name>

   2. _(optional)_ In the dvm, add custom firewall rule sets, Qubes VPN scripts etc

    Firewall rules sets and Qubes VPN scripts can be added just like any other VM   
    
   3. Set the dvm as template for DispVMs

    [user@dom0 ~]$ qvm-prefs <dvm_name> template_for_dispvms true

#### Create the sys-net DispVM #### 

  1. Create `sys-net` DispVM based on the dvm

    [user@dom0 ~]$ qvm-create --template <dvm_name> --class DispVM --label red disp-sys-net

  2. Set `disp-sys-net` virtualization mode to [hvm](/doc/hvm/)

    [user@dom0 ~]$ qvm-prefs disp-sys-net virt_mode hvm

  3. Set `disp-sys-net` to provide network for other VMs

    [user@dom0 ~]$ qvm-prefs disp-sys-net provides_network true

  4. Set `disp-sys-net` NetVM to none

    [user@dom0 ~]$ qvm-prefs disp-sys-net netvm ""

  5. List all available PCI devices to determine the correct _backend:BDF_ address(es) to assign to `disp-sys-net`

    [user@dom0 ~]$ qvm-pci

  6. Attach the network PCI device(s) to `disp-sys-net`: Finding and assigning PCI devices can be found [here](/doc/assigning-devices/)

    [user@dom0 ~]$ qvm-pci attach --persistent disp-sys-net <backend>:<bdf>

  7. _(recommended)_ Set `disp-sys-net` to start automatically when Qubes boots

    [user@dom0 ~]$ qvm-prefs disp-sys-net autostart true
     

  8. _(optional)_ Set `disp-sys-net` as the dom0 time source

    [user@dom0 ~]$ qubes-prefs clockvm disp-sys-net

#### Create the sys-firewall DispVM ####

  1. Create `sys-firewall` DispVM

    [user@dom0 ~]$ qvm-create --template <dvm_name> --class DispVM --label green disp-sys-firewall

  2. Set `disp-sys-firewall` to provide network for other VMs

    [user@dom0 ~]$ qvm-prefs disp-sys-firewall provides_network true

  3. Set `disp-sys-net` as the NetVM for `disp-sys-firewall`

    [user@dom0 ~]$ qvm-prefs disp-sys-firewall netvm disp-sys-net

  4. Set `disp-sys-firewall` as NetVM for other AppVMs

    [user@dom0 ~]$ qvm-prefs <vm_name> netvm disp-sys-firewall

  5. _(recommended)_ Set `disp-sys-firewall` to auto-start when Qubes boots

    [user@dom0 ~]$ qvm-prefs disp-sys-firewall autostart true

  6. _(optional)_ Set `disp-sys-firewall` as the default NetVM

    [user@dom0 ~]$ qubes-prefs default_netvm disp-sys-firewall

#### Create the sys-usb DispVM ####

  1. Create the `disp-sys-usb`

    [user@dom0 ~]$ qvm-create --template <dvm-name> --class DispVM --label red disp-sys-usb

  2. Set the `disp-sys-usb` virtualization mode to hvm

    [user@dom0 ~]$ qvm-prefs disp-sys-usb virt_mode hvm

  3. Set `disp-sys-usb` NetVM to none

    [user@dom0 ~]$ qvm-prefs usb-disp netvm ""

  4. List all available PCI devices

    [user@dom0 ~]$ qvm-pci

  5. Attach the USB controller to the `disp-sys-usb`
  
     >_**Note:**_ Most of the commonly used USB controllers (all Intel integrated controllers) require the `-o no-strict-reset=True` option to be set. Instructions detailing how this option is set can be found [here](/doc/assigning-devices/#r40-1).

    [user@dom0 ~]$ qvm-pci attach --persistent disp-sys-usb <backined>:<bdf>
    
  6. _(optional)_ Set `disp-sys-usb` to auto-start when Qubes boots
  
    [user@dom0 ~]$ qvm-prefs disp-sys-usb autostart true

  7. Users should now follow instructions on [How to hide USB controllers from dom0](/doc/usb/#how-to-hide-all-usb-controllers-from-dom0)


#### Starting the DispVMs ####

Prior to starting the new VMs, users should ensure that no other VMs such as the old `sys-net` and `sys-usb` VMs are running. This is because no two VMs can share the same PCI device while both running. It is recommended that users detach the PCI devices from the old VMs without deleting them. This will allow users to reattach the PCI devices if the newly created DispVMs fail to start.  

   Detach PCI device from VM

    [user@dom0~]$ qvm-pci detach <vm_name> <backend>:<bdf>


#### Troubleshooting ####

The `disp-sys-usb` VM does not start

If the `disp-sys-usb` does not start, it could be due to a PCI passthrough problem. For more details on this issue along with possible solutions, users can look [here](/doc/assigning-devices/#pci-passthrough-issues)


### Deleting Disposable VM ###

Deleting disposable VM is slightly peculiar. While working in a VM or disposable VM, you may want to open a document in another disposable VM. For this reason, the property `default_dispvm` may be set to the name of your disposable VM in a number of VMs:

    [user@dom0 ~]$ qvm-prefs workvm | grep default_dispvm
    default_dispvm        -  custom-dvm

This will prevent the deletion of the DVM. In order to fix this you need to unset the `default_dispvm` property:

    [user@dom0 ~]$ qvm-prefs workvm default_dispvm ""

You can then delete the DVM:

    [user@dom0 ~]$ qvm-remove custom-dvm
    This will completely remove the selected VM(s)
      custom-dvm
      
If you still encounter the issue, you may have forgot to clean an entry. Looking at the system logs will help you

    [user@dom0 ~]$ journalctl | tail

Qubes 3.2
----------

### Changing the DVM Template ###

You may want to use a non-default template the [DVM Template](/doc/glossary/#dvm-template). One example is to use a less-trusted template with some less trusted, third-party, often unsigned, applications installed, such as e.g. third-party printer drivers.

In order to regenerate the Disposable VM "snapshot" (called 'savefile' on Qubes) one can use the following command in Dom0:

    [user@dom0 ~]$ qvm-create-default-dvm <custom-template-name>

This would create a new Disposable VM savefile based on the custom template.
For example `<custom-template-name>` could be the name of the existing `debian-8` vm, which creates the disposable vm `debain-8-dvm`.
Now, whenever one opens a file (from any AppVM) in a Disposable VM, a Disposable VM based on this template will be used.

One can easily verify if the new Disposable VM template is indeed based on a custom template (in the example below the template called "f17-yellow" was used as a basis for the Disposable VM):


    [user@dom0 ~]$ ll /var/lib/qubes/dvmdata/
    total 0
    lrwxrwxrwx 1 user user 45 Mar 11 13:59 default_dvm.conf -> /var/lib/qubes/appvms/f17-yellow-dvm/dvm.conf
    lrwxrwxrwx 1 user user 49 Mar 11 13:59 default_savefile -> /var/lib/qubes/appvms/f17-yellow-dvm/dvm-savefile
    lrwxrwxrwx 1 user user 47 Mar 11 13:59 savefile_root -> /var/lib/qubes/vm-templates/f17-yellow/root.img

If you wish to use the `fedora-minimal` template as a DVM Template, see the "DVM Template" use case under [fedora-minimal customization](/doc/templates/fedora-minimal/#customization).


### Customization of Disposable VM ###

It is possible to change the settings of each new Disposable VM (DispVM). This can be done by customizing the DispVM template:

1.  Start a terminal in the `fedora-23-dvm` TemplateVM by running the following command in a dom0 terminal. (By default, this TemplateVM is not shown in Qubes VM Manager. However, it can be shown by selecting "Show/Hide internal VMs.")


        [user@dom0 ~]$ qvm-run -a fedora-23-dvm gnome-terminal

2.  Change the VM's settings and/or applications, as desired. Note that currently Qubes supports exactly one DispVM template, so any changes you make here will affect all DispVMs. Some examples of changes you may want to make include:
    -   Changing Firefox's default startup settings and homepage.
    -   Changing Nautilus' default file preview settings.
    -   Changing the DispVM's default NetVM. For example, you may wish to set the NetVM to "none." Then, whenever you start a new DispVM, you can choose your desired ProxyVM manually (by changing the newly-started DispVM's settings). This is useful if you sometimes wish to use a DispVM with a Whonix Gateway, for example. It is also useful if you sometimes wish to open untrusted files in a network-disconnected DispVM.

3.  Create an empty `/home/user/.qubes-dispvm-customized` file in the VM (not in dom0):


        [user@fedora-23-dvm ~]$ touch /home/user/.qubes-dispvm-customized

4.  Shutdown the VM (either by `poweroff` from VM terminal, or `qvm-shutdown` from dom0 terminal).
5.  Regenerate the DispVM template using the default template:

        [user@dom0 ~]$ qvm-create-default-dvm --default-template
        
    Or, if you're [using a non-default template](#changing-the-dvm-template), regenerate the DispVM using your custom template:
    
        [user@dom0 ~]$ qvm-create-default-dvm <custom-template-name>


**Note:** All of the above requires at least qubes-core-vm \>= 2.1.2 installed in template.


### Adding arbitrary programs to Disposable VM Application Menu ###

For added convenience, arbitrary programs can be added to the Application Menu of the Disposable VM. In order to do that create (e.g.) `arbitrary.desktop` file in `/usr/local/share/applications` in Dom0. That file will point to the desired program. Use the following template for the file:

    [Desktop Entry]
    Version=1.0
    Type=Application
    Exec=sh -c 'echo arbitrary | /usr/lib/qubes/qfile-daemon-dvm qubes.VMShell dom0 DEFAULT red'
    Icon=dispvm-red
    Terminal=false
    Name=DispVM: Arbitrary Name
    GenericName=DispVM: Arbitrary Generic Name
    StartupNotify=false
    Categories=Network;X-Qubes-VM;

Next, the `/etc/xdg/menus/applications-merged/qubes-dispvm.menu` file has to be modified so that it points to the newly-created .desktop file. (If you use i3 you can skip this step; the shortcut gets added to dmenu automatically.)

Add a `<Filename>arbitrary.desktop</Filename>` line so that your modified file looks like this:

    <Include>
    <Filename>qubes-dispvm-firefox.desktop</Filename>
    <Filename>qubes-dispvm-xterm.desktop</Filename>
    <Filename>arbitrary.desktop</Filename>
    </Include>

After saving the changes the new shortcut should appear in the Disposable VM Applications menu.
