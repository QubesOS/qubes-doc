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

See [this article](http://theinvisiblethings.blogspot.com/2010/06/disposable-vms.html) for a background on why would one want to use a Disposable VM and what it is.

A DisposableVM is a lightweight VM that can be created quickly and which will disappear when it is finished with. Usually a Disposable VM is created in order to host a single application, like a viewer or an editor. This means that you can safely work with files without risk of compromising any of your VMs. Changes made to a file opened in a disposable VM are passed back to the originating VM. 

By default a Disposable VM will inherit the netVM and firewall settings of the ancestor VM. You can change this behaviour: in the Qubes Manager go to the advanced tab of VM Settings where you can set the default netVM to be used for DisposableVMs created from that VM. 

Once a dispVM has been created it will appear in the Qubes Manager with the name "dispX", and NetVM and firewall rules can be set as for a normal VM.

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
Full instructions are [here](/doc/disp-vm-customization/) 


Disposable VMs and Local Forensics
----------------------------------

At this time, DispVMs should not be relied upon to circumvent local forensics, as they do not run entirely in RAM. For details, see [this thread](https://groups.google.com/d/topic/qubes-devel/QwL5PjqPs-4/discussion).
