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
====================

Changing the DVM Template
-------------------------

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


Customization of Disposable VM
------------------------------

It is possible to change the settings of each new Disposable VM (DispVM). This can be done by customizing the DispVM template:

1.  Start a terminal in the `fedora-23-dvm` TemplateVM by running the following command in a dom0 terminal. (By default, this TemplateVM is not shown in Qubes VM Manager. However, it can be shown by selecting "Show/Hide internal VMs.")


        [user@dom0 ~]$ qvm-run -a fedora-23-dvm gnome-terminal

2.  Change the VM's settings and/or applications, as desired. Note that currently Qubes supports exactly one DispVM template, so any changes you make here will affect all DispVMs. Some examples of changes you may want to make include:
    -   Changing Firefox's default startup settings and homepage.
    -   Changing Nautilus' default file preview settings.
    -   Changing the DispVM's default NetVM. For example, you may wish to set the NetVM to "none." Then, whenever you start a new DispVM, you can choose your desired ProxyVM manually (by changing the newly-started DispVM's settings). This is useful if you sometimes wish to use a DispVM with a TorVM, for example. It is also useful if you sometimes wish to open untrusted files in a network-disconnected DispVM.

3.  Create an empty `/home/user/.qubes-dispvm-customized` file in the VM (not in dom0):


        [user@fedora-23-dvm ~]$ touch /home/user/.qubes-dispvm-customized

4.  Shutdown the VM (either by `poweroff` from VM terminal, or `qvm-shutdown` from dom0 terminal).
5.  Regenerate the DispVM template using the default template:

        [user@dom0 ~]$ qvm-create-default-dvm --default-template
        
    Or, if you're [using a non-default template](#changing-the-dvm-template), regenerate the DispVM using your custom template:
    
        [user@dom0 ~]$ qvm-create-default-dvm <custom-template-name>


**Note:** All of the above requires at least qubes-core-vm \>= 2.1.2 installed in template.


Adding arbitrary programs to Disposable VM Application Menu
-----------------------------------------------------------

For added convenience, arbitrary programs can be added to the Application Menu of the Disposable VM. In order to do that create (e.g.) `arbitrary.desktop` file in `/usr/share/applications` in Dom0. That file will point to the desired program. Use the following template for the file:

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
