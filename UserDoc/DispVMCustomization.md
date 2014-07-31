---
layout: wiki
title: DispVMCustomization
permalink: /wiki/UserDoc/DispVMCustomization/
---

Customization of Disposable VM
==============================

It is possible to change the settings of each new Disposable VM (DispVM). This can be done by customizing the DispVM template:

1.  Start a terminal in the `fedora-20-x64-dvm` TemplateVM by running the following command in a dom0 terminal. (By default, this TemplateVM is not shown in Qubes VM Manager. However, it can be shown by selecting "Show/Hide internal VMs.")

    ``` {.wiki}
    [user@dom0 ~]$ qvm-run -a fedora-20-x64-dvm gnome-terminal
    ```

2.  Change the VM's settings and/or applications, as desired. Note that currently Qubes supports exactly one DispVM template, so any changes you make here will affect all DispVMs. Some examples of changes you may want to make include:
    -   Changing Firefox's default startup settings and homepage.
    -   Changing Nautilus' default file preview settings.
    -   Changing the DispVM's default NetVM. For example, you may wish to set the NetVM to "none." Then, whenever you start a new DispVM, you can choose your desired ProxyVM manually (by changing the newly-started DipsVMs settings). This is useful if you sometimes wish to use a DispVM with a TorVM, for example. It is also useful if you sometimes wish to open untrusted files in a network-disconnected DispVM.

3.  Create an empty `/home/user/.qubes-dispvm-customized` file:

    ``` {.wiki}
    [user@fedora-20-x64-dvm ~]$ touch /home/user/.qubes-dispvm-customized
    ```

4.  Shutdown the VM (either by `poweroff` from VM terminal, or `qvm-shutdown` from dom0 terminal).
5.  Regenerate the DispVM template:

    ``` {.wiki}
    [user@dom0 ~]$ qvm-create-default-dvm --default-template --default-script
    ```

**Note:** All of the above requires at least qubes-core-vm \>= 2.1.2 installed in template.
