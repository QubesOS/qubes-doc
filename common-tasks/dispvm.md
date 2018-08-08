---
layout: doc
title: Disposable VMs
permalink: /doc/dispvm/
redirect_from:
- /en/doc/dispvm/
- /doc/DisposableVms/
- /wiki/DisposableVMs/
---

Disposable VMs (DispVMs)
========================

A Disposable VM (DispVM) is a lightweight VM that can be created quickly and will disappear when closed.
Disposable VMs are usually created in order to host a single application, like a viewer, editor, or web browser.

From inside an AppVM, choosing the `Open in Disposable VM` option on a file will launch a DispVM for just that file.
Changes made to a file opened in a DispVM are passed back to the originating VM.
This means that you can safely work with untrusted files without risk of compromising your other VMs.
DispVMs can be launched either directly from Dom0's Start Menu or terminal window, or from within AppVMs.
While running, DispVMs will appear in Qubes VM Manager with the name `disp####`.

See [this article](https://blog.invisiblethings.org/2010/06/01/disposable-vms.html) for more on why one would want to use a Disposable VM.


Disposable VMs and Networking (R4.0 and later)
-----------------------------

Similarly to how AppVMs are based on their underlying [TemplateVM](https://www.qubes-os.org/doc/glossary/#templatevm), DispVMs are based on their underlying [DVM Template](https://www.qubes-os.org/doc/glossary/#dvm-template).
R4.0 introduces the concept of multiple DVM Templates, whereas R3.2 was limited to only one.

On a fresh installation of Qubes, the default DVM Template is called `fedora-XX-dvm` (where `XX` is the Fedora version of the default TemplateVM).
If you have included the Whonix option in your install, there will also be a `whonix-ws-dvm` DVM Template available for your use.

You can set any AppVM to have the ability to act as a DVM Template with:

    qvm-prefs <vmname> template_for_dispvms True

The default system wide DVM Template can be changed with `qubes-prefs default_dispvm`.
By combining the two, choosing `Open in Disposable VM` from inside an AppVM will open the document in a DispVM based on the default DVM Template you specified.

You can change this behaviour for individual VMs: in the Application Menu, open Qube Settings for the VM in question and go to the "Advanced" tab. 
Here you can edit the "Default DispVM" setting to specify which DVM Template will be used to launch DispVMs from that VM.
This can also be changed from the command line with:

    qvm-prefs <vmname> default_dispvm <dvmtemplatename>

For example, `anon-whonix` has been set to use `whonix-ws-dvm` as its `default_dispvm`, instead of the system default.
You can even set an AppVM that has also been configured as a DVM Template to use itself, so DispVMs launched from within the AppVM/DVM Template would inherit the same settings.

NetVM and firewall rules for DVM Templates can be set as they can for a normal VM. 
By default a DispVM will inherit the NetVM and firewall settings of the DVM Template on which it is based.
This is a change in behaviour from R3.2, where DispVMs would inherit the settings of the AppVM from which they were launched.
Therefore, launching a DispVM from an AppVM will result in it using the network/firewall settings of the DVM Template on which it is based.
For example, if an AppVM uses sys-net as its NetVM, but the default system DispVM uses sys-whonix, any DispVM launched from this AppVM will have sys-whonix as its NetVM.

**Warning:** The opposite is also true. This means if you have changed anon-whonix's `default_dispvm` to use the system default, and the system default DispVM uses sys-net, launching a DispVM from inside anon-whonix will result in the DispVM using sys-net.

A Disposable VM launched from the Start Menu inherits the NetVM and firewall settings of the DVM Template on which it is based.
Note that changing the "NetVM" setting for the system default DVM Template *does* affect the NetVM of DispVMs launched from the Start Menu.
Different DVM Templates with individual NetVM settings can be added to the Start Menu. 

Disposable VMs and Networking (R3.2 and earlier)
-----------------------------

NetVM and firewall rules for Disposable VMs can be set as they can for a normal VM. 
By default a DispVM will inherit the NetVM and firewall settings of the VM from which it is launched. 
Thus if an AppVM uses sys-net as its NetVM, any DispVM launched from this AppVM will also have sys-net as its NetVM. 
You can change this behaviour for individual VMs: in Qubes VM Manager open VM Settings for the VM in question and go to the "Advanced" tab. 
Here you can edit the "NetVM for DispVM" setting to change the NetVM of any DispVM launched from that VM.

A Disposable VM launched from the Start Menu inherits the NetVM of the [DVM Template](/doc/glossary/#dvm-template). 
By default the DVM template is called `fedora-XX-dvm` (where `XX` is the Fedora version of the default TemplateVM). 
As an "internal" VM it is hidden in Qubes VM Manager, but can be shown by selecting "Show/Hide internal VMs". 
Note that changing the "NetVM for DispVM" setting for the DVM Template does *not* affect the NetVM of DispVMs launched from the Start Menu; only changing the DVM Template's own NetVM does.

Opening a file in a Disposable VM via GUI
-----------------------------------------

In an AppVM's file manager, right click on the file you wish to open in a Disposable VM, then choose "Open in Disposable VM". 
Wait a few seconds and the default application for this file type should appear displaying the file content. 
This app is running in its own dedicated VM -- a Disposable VM created for the purpose of viewing or editing this very file. 
Once you close the viewing application the whole Disposable VM will be destroyed. 
If you have edited the file and saved the changes, the changed file will be saved back to the original AppVM, overwriting the original.

![r1-open-in-dispvm-1.png](/attachment/wiki/DisposableVms/r1-open-in-dispvm-1.png) ![r1-open-in-dispvm-2.png](/attachment/wiki/DisposableVms/r1-open-in-dispvm-2.png)

Opening a fresh web browser instance in a new Disposable VM
-----------------------------------------------------------

Sometimes it is desirable to open an instance of Firefox within a new fresh Disposable VM. 
This can be done easily using the Start Menu: just go to **Application Menu -\> DisposableVM -\> DispVM:Firefox web browser**. 
Wait a few seconds until a web browser starts. 
Once you close the viewing application the whole Disposable VM will be destroyed. 

![r1-open-in-dispvm-3.png](/attachment/wiki/DisposableVms/r1-open-in-dispvm-3.png)

Opening a file in a Disposable VM via command line (from AppVM)
---------------------------------------------------------------

Use the `qvm-open-in-dvm` command from a terminal in your AppVM:

~~~
[user@work-pub ~]$ qvm-open-in-dvm Downloads/apple-sandbox.pdf
~~~

Note that the `qvm-open-in-dvm` process will not exit until you close the application in the Disposable VM.

Starting an arbitrary program in a Disposable VM from an AppVM
--------------------------------------------------------------

Sometimes it can be useful to start an arbitrary program in a DispVM. This can be done from an AppVM by running

~~~
[user@vault ~]$ qvm-run '$dispvm' xterm
~~~

The created Disposable VM can be accessed via other tools (such as `qvm-copy-to-vm`) using its `disp####` name as shown in the Qubes Manager or `qvm-ls`.

Starting an arbitrary application in a Disposable VM via command line (from Dom0)
---------------------------------------------------------------------------------

The Start Menu has shortcuts for opening a terminal and a web browser in dedicated DispVMs, since these are very common tasks.
However, it is possible to start an arbitrary application in a DispVM directly from Dom0 by running

R4.0 (border colour will be inherited from that set in the `dispvm-template`)
~~~
[joanna@dom0 ~]$ qvm-run --dispvm=dispvm-template --service qubes.StartApp+xterm
~~~

R3.2 (border colour can be specified in the command)
~~~
[joanna@dom0 ~]$ echo xterm | /usr/lib/qubes/qfile-daemon-dvm qubes.VMShell dom0 DEFAULT red
~~~

(The Disposable VM appmenu used for starting Firefox runs a very similar command to the one above.)

Customizing Disposable VMs
--------------------------

You can change the template used to generate the Disposable VMs, and change settings used in the Disposable VM savefile. 
These changes will be reflected in every new Disposable VM based on that template. 
Full instructions can be found [here](/doc/dispvm-customization/).

Disposable VMs and Local Forensics
----------------------------------

At this time, DispVMs should not be relied upon to circumvent local forensics, as they do not run entirely in RAM. 
For details, see [this thread](https://groups.google.com/d/topic/qubes-devel/QwL5PjqPs-4/discussion).

When it is essential to avoid leaving any trace, consider using [Tails](https://tails.boum.org/).
