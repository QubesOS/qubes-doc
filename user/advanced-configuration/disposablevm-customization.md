---
lang: en
layout: doc
permalink: /doc/disposablevm-customization/
redirect_from:
- /doc/dispvm-customization/
- /en/doc/dispvm-customization/
- /doc/DispVMCustomization/
- /doc/UserDoc/DispVMCustomization/
- /wiki/UserDoc/DispVMCustomization/
ref: 174
title: DisposableVM Customization
---

# DisposableVM Customization

## Introduction

A [DisposableVM](/doc/disposablevm) can be based on any [TemplateBasedVM](/doc/glossary/#templatebasedvm).
You can also choose to use different [DisposableVM Templates](/doc/glossary/#disposablevm-template) for different DisposableVMs.
To prepare an AppVM to be a DisposableVM Template, you need to set `template_for_dispvms` property, for example:

```shell_session
[user@dom0 ~]$ qvm-prefs fedora-26-dvm template_for_dispvms True
```

Additionally, if you want to have menu entries for starting applications in DisposableVM based on this AppVM (instead of in the AppVM itself), you can achieve it with `appmenus-dispvm` feature:

```shell_session
[user@dom0 ~]$ qvm-features fedora-26-dvm appmenus-dispvm 1
```

Note: application shortcuts that existed before setting this feature will not be updated automatically. Please go the the "Applications" tab in the qube's "Settings" dialog and unselect all existing shortcuts by clicking "<<", then click "OK" and close the dialog. Give it a few seconds time and then reopen and re-select all the shortcuts you want to see in the menu. See [this page](/doc/managing-appvm-shortcuts) for background information.

## Security

If a DisposableVM Template becomes compromised, then any DisposableVM based on that DisposableVM Template could be compromised.
Therefore, you should not make any risky customizations (e.g., installing untrusted browser plugins) in important DisposableVM Templates.
In particular, the *default* DisposableVM Template is important because it is used by the "Open in DisposableVM" feature.
This means that it will have access to everything that you open with this feature.
For this reason, it is strongly recommended that you base the default DisposableVM Template on a trusted TemplateVM and refrain from making any risky customizations to it.

## Creating a new DisposableVM Template

In Qubes 4.0, you're no longer restricted to a single DisposableVM Template. Instead, you can create as many as you want. Whenever you start a new DisposableVM, you can choose to base it on whichever DisposableVM Template you like.
To create new DisposableVM Template, lets say `custom-disposablevm-template`, based on `debian-9` template, use following commands:

```shell_session
[user@dom0 ~]$ qvm-create --template debian-9 --label red custom-disposablevm-template
[user@dom0 ~]$ qvm-prefs custom-disposablevm-template template_for_dispvms True
[user@dom0 ~]$ qvm-features custom-disposablevm-template appmenus-dispvm 1
```

Additionally you may want to set it as default DisposableVM Template:

```shell_session
[user@dom0 ~]$ qubes-prefs default_dispvm custom-disposablevm-template
```

The above default is used whenever a qube request starting a new DisposableVM and do not specify which one (for example `qvm-open-in-dvm` tool). This can be also set in qube settings and will affect service calls from that qube. See [qrexec documentation](/doc/qrexec/#specifying-vms-tags-types-targets-etc) for details.

If you wish to use a [Minimal TemplateVM](/doc/templates/minimal/) as a DisposableVM Template, please see the [Minimal TemplateVM](/doc/templates/minimal/) page.

## Customization of DisposableVM

_**Note:** If you are trying to customize Tor Browser in a Whonix DisposableVM, please consult the [Whonix documentation](https://www.whonix.org/wiki/Tor_Browser/Advanced_Users#DVM_Template_Customization)._

It is possible to change the settings for each new DisposableVM.
This can be done by customizing the DisposableVM Template on which it is based:

1. Start a terminal in the `fedora-26-dvm` qube (or another DisposableVM Template) by running the following command in a dom0 terminal. (If you enable `appmenus-dispvm` feature (as explained at the top), applications menu for this VM (`fedora-26-dvm`) will be "Disposable: fedora-26-dvm" (instead of "Domain: fedora-26-dvm") and entries there will start new DisposableVM based on that VM (`fedora-26-dvm`). Not in that VM (`fedora-26-dvm`) itself).

    ```shell_session
    [user@dom0 ~]$ qvm-run -a fedora-26-dvm gnome-terminal
    ```

2. Change the qube's settings and/or applications, as desired. Some examples of changes you may want to make include:
    - Changing Firefox's default startup settings and homepage.
    - Changing default editor, image viewer. In Debian-based templates this can be done with the `mimeopen` command.
    - Changing the DisposableVM's default NetVM. For example, you may wish to set the NetVM to "none." Then, whenever you start a new DisposableVM, you can choose your desired ProxyVM manually (by changing the newly-started DisposableVMs settings). This is useful if you sometimes wish to use a DisposableVM with a Whonix Gateway, for example. It is also useful if you sometimes wish to open untrusted files in a network-disconnected DisposableVM.

4. Shutdown the qube (either by `poweroff` from qube's terminal, or `qvm-shutdown` from dom0 terminal).

## Using static DisposableVMs for sys-*

You can use a static DisposableVM for `sys-*` as long as it is stateless.
For example, a `sys-net` using DHCP or `sys-usb` will work.
In most cases `sys-firewall` will also work, even if you have configured AppVM firewall rules.
The only exception is if you require something like VM to VM communication and have manually edited `iptables` or other items directly inside the firewall AppVM.

To create one that has no PCI devices attached, such as for `sys-firewall`:

~~~
qvm-create -C DispVM -l green <sys-VMName>
qvm-prefs <sys-VMName> autostart true
qvm-prefs <sys-VMName> netvm <sys-net>
qvm-prefs <sys-VMName> provides_network true
qvm-features <sys-VMName> appmenus-dispvm ''
~~~

Next, set the old `sys-firewall` autostart to false, and update any references to the old one to instead point to the new.
For example, with `qvm-prefs work netvm sys-firewall2`.

To create one with a PCI device attached such as for `sys-net` or `sys-usb`, use the additional commands as follows.

**Note** You can use `qvm-pci` to [determine](/doc/pci-devices/#qvm-pci-usage) the `<BDF>`.
Also, you will often need to include the `-o no-strict-reset=True` [option](/doc/pci-devices/#no-strict-reset) with USB controllers.

~~~
qvm-create -C DispVM -l red <sys-VMName>
qvm-prefs <sys-VMName> virt_mode hvm
qvm-service <sys-VMName> meminfo-writer off
qvm-pci attach --persistent <sys-VMName> dom0:<BDF>
qvm-prefs <sys-VMName> autostart true
qvm-prefs <sys-VMName> netvm ''
qvm-features <sys-VMName> appmenus-dispvm ''
# optional, if this DisposableVM will be providing networking
qvm-prefs <sys-VMName> provides_network true
~~~

Next, set the old `sys-` VM's autostart to false, and update any references to the old one.
In particular, make sure to update `/etc/qubes-rpc/policy/qubes.UpdatesProxy` in dom0.

For example, `qvm-prefs sys-firewall netvm <sys-VMName>`.
See below for a complete example of a `sys-net` replacement:

~~~
qvm-create -C DispVM -l red sys-net2
qvm-prefs sys-net2 virt_mode hvm
qvm-service sys-net2 meminfo-writer off
qvm-pci attach --persistent sys-net2 dom0:00_1a.0
qvm-prefs sys-net2 autostart true
qvm-prefs sys-net2 netvm ''
qvm-features sys-net2 appmenus-dispvm ''
qvm-prefs sys-net2 provides_network true
qvm-prefs sys-net autostart false
qvm-prefs sys-firewall netvm sys-net2
qubes-prefs clockvm sys-net2
~~~

## Adding programs to DisposableVM Application Menu

For added convenience, arbitrary programs can be added to the Application Menu of the DisposableVM. 

In order to do that, select "Qube settings" entry in selected base AppVM, go to "Applications" tab and select desired applications as for any other qube.

Note that currently only applications whose main process keeps running until you close the application (i.e. do not start a background process instead) will work. One of known examples of incompatible applications is GNOME Terminal (shown on the list as "Terminal"). Choose different terminal emulator (like XTerm) instead.

## Create Custom sys-net sys-firewall and sys-usb DisposableVMs

Users have the option of creating customized DisposableVMs for the `sys-net`, `sys-firewall` and `sys-usb` VMs. In this configuration, a fresh VM instance is created each time a DisposableVM is launched. Functionality is near-identical to the default VMs created following a new Qubes’ installation, except the user benefits from a non-persistent filesystem.

Functionality is not limited, users can:

- Set custom firewall rule sets and run Qubes VPN scripts. 
- Set DisposableVMs to autostart at system boot.
- Attach PCI devices with the `--persistent` option. 

Using DisposableVMs in this manner is ideal for untrusted qubes which require persistent PCI devices, such as USB VMs and NetVMs.

>_**Note:**_ Users who want customized VPN or firewall rule sets must create a separate DisposableVM Template for use by each DisposableVM. If DisposableVM Template customization is not needed, then a single DisposableVM Template is used as a template for all DisposableVMs.

### Create and configure the DisposableVM Template on which the DisposableVM will be based

1. Create the DisposableVM Template:

    ```shell_session
    [user@dom0 ~]$ qvm-create --class AppVM --label gray <DisposableVM-Template-Name>
    ```

2. _(optional)_ In the DisposableVM Template, add custom firewall rule sets, Qubes VPN scripts, etc.

    Firewall rules sets and Qubes VPN scripts can be added just like any other VM.   
    
3. Set the DisposableVM Template as template for DisposableVMs:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs <DisposableVM-Template-Name> template_for_dispvms true
    ```

### Create the sys-net DisposableVM

1. Create `sys-net` DisposableVM based on the DisposableVM Template:

    ```shell_session
    [user@dom0 ~]$ qvm-create --template <DisposableVM-Template-Name> --class DispVM --label red disp-sys-net
    ```

2. Set `disp-sys-net` virtualization mode to [hvm](/doc/hvm/):

    ```shell_session
    [user@dom0 ~]$ qvm-prefs disp-sys-net virt_mode hvm
    ```

3. Set `disp-sys-net` to provide network for other VMs:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs disp-sys-net provides_network true
    ```

4. Set `disp-sys-net` NetVM to none:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs disp-sys-net netvm ""
    ```

5. List all available PCI devices to determine the correct _backend:BDF_ address(es) to assign to `disp-sys-net`:

    ```shell_session
    [user@dom0 ~]$ qvm-pci
    ```

6. Attach the network PCI device(s) to `disp-sys-net` (finding and assigning PCI devices can be found [here](/doc/pci-devices/):

    ```shell_session
    [user@dom0 ~]$ qvm-pci attach --persistent disp-sys-net <backend>:<bdf>
    ```

7. _(recommended)_ Set `disp-sys-net` to start automatically when Qubes boots:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs disp-sys-net autostart true
    ```

8. _(recommended)_ Disable the `appmenus-dispvm` feature, as disp-sys-net is not itself a DisposableVM template (Note: this is only necessary if you enabled the `appmenus-dispvm` feature for the DisposableVM template):

    ```shell_session
    [user@dom0 ~]$ qvm-features disp-sys-net appmenus-dispvm ''
    ```

9. _(optional)_ Set `disp-sys-net` as the dom0 time source:

    ```shell_session
    [user@dom0 ~]$ qubes-prefs clockvm disp-sys-net
    ```

10. _(recommended)_ Allow templates to be updated via `disp-sys-net`. In dom0, edit `/etc/qubes-rpc/policy/qubes.UpdatesProxy` to change the target from `sys-net` to `disp-sys-net`.

### Create the sys-firewall DisposableVM

1. Create `sys-firewall` DisposableVM:

    ```shell_session
    [user@dom0 ~]$ qvm-create --template <DisposableVM-Template-Name> --class DispVM --label green disp-sys-firewall
    ```

2. Set `disp-sys-firewall` to provide network for other VMs:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs disp-sys-firewall provides_network true
    ```

3. Set `disp-sys-net` as the NetVM for `disp-sys-firewall`:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs disp-sys-firewall netvm disp-sys-net
    ```

4. Set `disp-sys-firewall` as NetVM for other AppVMs:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs <vm_name> netvm disp-sys-firewall
    ```

5. _(recommended)_ Set `disp-sys-firewall` to auto-start when Qubes boots:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs disp-sys-firewall autostart true
    ```

6. _(recommended)_ Disable the `appmenus-dispvm` feature, as disp-sys-firewall is not itself a DisposableVM template (Note: this is only necessary if you enabled the `appmenus-dispvm` feature for the DisposableVM template):

    ```shell_session
    [user@dom0 ~]$ qvm-features disp-sys-firewall appmenus-dispvm ''
    ```

7. _(optional)_ Set `disp-sys-firewall` as the default NetVM:

    ```shell_session
    [user@dom0 ~]$ qubes-prefs default_netvm disp-sys-firewall
    ```

### Create the sys-usb DisposableVM

1. Create the `disp-sys-usb`:

    ```shell_session
    [user@dom0 ~]$ qvm-create --template <disposablevm-template-name> --class DispVM --label red disp-sys-usb
    ```

2. Set the `disp-sys-usb` virtualization mode to hvm:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs disp-sys-usb virt_mode hvm
    ```

3. Set `disp-sys-usb` NetVM to none:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs disp-sys-usb netvm ""
    ```

4. List all available PCI devices:

    ```shell_session
    [user@dom0 ~]$ qvm-pci
    ```

5. Attach the USB controller to the `disp-sys-usb`:
   >_**Note:**_ Most of the commonly used USB controllers (all Intel integrated controllers) require the `-o no-strict-reset=True` option to be set. Instructions detailing how this option is set can be found [here](/doc/pci-devices/#no-strict-reset).

    ```shell_session
    [user@dom0 ~]$ qvm-pci attach --persistent disp-sys-usb <backined>:<bdf>
    ```

6. _(optional)_ Set `disp-sys-usb` to auto-start when Qubes boots:

    ```shell_session
    [user@dom0 ~]$ qvm-prefs disp-sys-usb autostart true
    ```

7. _(recommended)_ Disable the `appmenus-dispvm` feature, as disp-sys-usb is not itself a DisposableVM template (Note: this is only necessary if you enabled the `appmenus-dispvm` feature for the DisposableVM template):

    ```shell_session
    [user@dom0 ~]$ qvm-features disp-sys-usb appmenus-dispvm ''
    ```

8. Users should now follow instructions on [How to hide USB controllers from dom0](/doc/usb-qubes/#how-to-hide-all-usb-controllers-from-dom0).

9. At this point, your mouse may not work.
   Edit the `qubes.InputMouse` policy file in dom0, which is located here:

    ```
    /etc/qubes-rpc/policy/qubes.InputMouse
    ```

   Add a line like this to the top of the file:

    ```
    disp-sys-usb dom0 allow,user=root
    ```

### Starting the DisposableVMs

Prior to starting the new VMs, users should ensure that no other VMs such as the old `sys-net` and `sys-usb` VMs are running. This is because no two VMs can share the same PCI device while both running. It is recommended that users detach the PCI devices from the old VMs without deleting them. This will allow users to reattach the PCI devices if the newly created DisposableVMs fail to start. 

Detach PCI device from VM:

```shell_session
[user@dom0~]$ qvm-pci detach <vm_name> <backend>:<bdf>
```

### Troubleshooting

If the `disp-sys-usb` does not start, it could be due to a PCI passthrough problem. For more details on this issue along with possible solutions, users can look [here](/doc/pci-troubleshooting/#pci-passthrough-issues).

## Deleting DisposableVMs

While working in a DisposableVM, you may want to open a document in another DisposableVM.
For this reason, the property `default_dispvm` may be set to the name of your DisposableVM in a number of VMs:

```shell_session
[user@dom0 ~]$ qvm-prefs workvm | grep default_dispvm
default_dispvm        -  custom-disposablevm-template
```

This will prevent the deletion of the DisposableVM Template. In order to fix this you need to unset the `default_dispvm` property:

```shell_session
[user@dom0 ~]$ qvm-prefs workvm default_dispvm ""
```

You can then delete the DisposableVM Template:

```shell_session
[user@dom0 ~]$ qvm-remove custom-disposablevm-template
This will completely remove the selected VM(s)
  custom-disposablevm-template
```

      
If you still encounter the issue, you may have forgot to clean an entry. Looking at the system logs will help you:

```shell_session
[user@dom0 ~]$ journalctl | tail
```
