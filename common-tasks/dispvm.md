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

Background
----------

A Disposable VM (DispVM) is a lightweight VM that can be created quickly and which will disappear when it is finished with. Usually a Disposable VM is created in order to host a single application, like a viewer or an editor. This means that you can safely work with files without risk of compromising any of your VMs. Changes made to a file opened in a disposable VM are passed back to the originating VM. See [this article](https://blog.invisiblethings.org/2010/06/01/disposable-vms.html) for more on why would one want to use a Disposable VM.

By default a DispVM will inherit the NetVM and firewall settings of the ancestor VM, that is the VM it is launched from. Thus if an AppVM uses sys-net as NetVM (instead of, say, sys-whonix), any DispVM launched from this AppVM will also have sys-net as its NetVM. You can change this behaviour for individual VMs: in Qubes VM Manager open VM Settings for the VM in question and go to the "Advanced" tab. Here you can edit the "NetVM for DispVM" setting to change the NetVM of any DispVM launched from that VM.

A DispVM launched from the Start Menu inherits the NetVM of the [DVM Template](https://www.qubes-os.org/doc/glossary/#dvm-template). By default it is named `fedora-XX-dvm` (where `XX` is the Fedora version of the default TemplateVM) and, as a so-called internal VM, hidden in Qubes VM Manager; it can be shown by selecting "Show/Hide internal VMs". Notice that changing the "NetVM for DispVM" setting for the DVM Template does *not* affect the NetVM of DispVMs launched from the Start Menu; only changing the DVM Template's own NetVM does.

Once a DispVM has been created it will appear in Qubes VM Manager with the name "dispX", and NetVM and firewall rules can be set as for a normal VM.


Opening a file in a Disposable VM (via GUI)
-------------------------------------------

In some AppVM, right click on the file you wish to open in a Disposable VM (in the Nautilus file manager), then choose "Open in Disposable VM". Wait a few seconds and the default application for this file type should appear displaying the file content. This app is running in a whole new VM -- a disposable VM created for the purpose of viewing or editing this very file. Once you close the viewing application the whole Disposable VM will be destroyed. If you have edited the file and saved the changes the changed file will be saved back to the original VM, overwriting the original.

![r1-open-in-dispvm-1.png](/attachment/wiki/DisposableVms/r1-open-in-dispvm-1.png) ![r1-open-in-dispvm-2.png](/attachment/wiki/DisposableVms/r1-open-in-dispvm-2.png)

Opening a fresh web browser instance in a new Disposable VM
-----------------------------------------------------------

Sometimes it is convenient to open a fresh instance of Firefox within a new fresh Disposable VM. This can be easily done by using the Start Menu: just go to Start -\> System Tools -\> DispVM:Firefox web browser . Wait a few seconds until a web browser starts. Once you close the viewing application the whole Disposable VM will get destroyed.

![r1-open-in-dispvm-3.png](/attachment/wiki/DisposableVms/r1-open-in-dispvm-3.png)

Opening a file in a Disposable VM via command line (from AppVM)
---------------------------------------------------------------

Use the `qvm-open-in-dvm` command line (from your AppVM), e.g.:

~~~
[user@work-pub ~]$ qvm-open-in-dvm Downloads/apple-sandbox.pdf
~~~

The qvm-open-in-dvm will not exit until you close the application in the Disposable VM.

Starting an arbitrary application in a disposable VM via command line (from Dom0)
---------------------------------------------------------------------------------

**Note:** Normally there should be no need for doing this -- this is just for Qubes hackers ;)

~~~
[joanna@dom0 ~]$ echo xterm | /usr/lib/qubes/qfile-daemon-dvm qubes.VMShell dom0 DEFAULT red
~~~

In fact the Disposable VM appmenu used for starting Firefox contains a very similar command to the above. Please note, however, that it generally makes little sense to start any other application other than a Web Browser this way...

Starting an arbitrary program in a Disposable VM from an AppVM
--------------------------------------------------------------

Sometimes it might be useful to start an arbitrary program, such as e.g. terminal in an Disposable VM from an AppVM. This could be simply done this way:

~~~
[user@vault ~]$ qvm-run '$dispvm' xterm
~~~

Note the above command is issued in an AppVM, not in Dom0. The created Disposable VM can be normally accessed via other tools, such as e.g. `qvm-copy-to-vm`, using its 'dispX' name, as shown by the Qubes Manager or `qvm-ls` tools. 


Customizing Disposable VMs
---------------------------------------------------------

You can change the template used to generate the Disposable VM, and change settings used in the Disposable VM savefile. These changes will be reflected in every new Disposable VM.
Full instructions are [here](/doc/dispvm-customization/).


Disposable VMs and Local Forensics
----------------------------------

At this time, DispVMs should not be relied upon to circumvent local forensics, as they do not run entirely in RAM. For details, see [this thread](https://groups.google.com/d/topic/qubes-devel/QwL5PjqPs-4/discussion).
