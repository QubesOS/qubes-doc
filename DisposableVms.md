---
layout: wiki
title: DisposableVms
permalink: /wiki/DisposableVms/
---

Using Disposable VMs
====================

Background
----------

See [​this article](http://theinvisiblethings.blogspot.com/2010/06/disposable-vms.html) for a background on why would one want to use a Disposable VM and what it is.

Opening a file in a Disposable VM (via GUI)
-------------------------------------------

In some AppVM, right click on the file you wish to open in a Disposable VM (in the Nautilus file manager), then choose Scripts -\> Open in Disposable VM. Wait a few seconds and an default application for this file type should appear displaying the file content. This app is running in a whole new VM -- a disposable VM created for the purpose of view this very file. Once you close the viewing application then whole Disposable VM will get destroyed.

[![No image "r1-open-in-dispvm-1.png" attached to DisposableVms](/chrome/common/attachment.png "No image "r1-open-in-dispvm-1.png" attached to DisposableVms")](/attachment/wiki/DisposableVms/r1-open-in-dispvm-1.png) [![No image "r1-open-in-dispvm-2.png" attached to DisposableVms](/chrome/common/attachment.png "No image "r1-open-in-dispvm-2.png" attached to DisposableVms")](/attachment/wiki/DisposableVms/r1-open-in-dispvm-2.png)

Opening a fresh web browser instance in a new Disposable VM
-----------------------------------------------------------

Sometimes it is convenient to open a fresh instance of Firefox within a new fresh Disposable VM. This can be easily done by using the Start Menu: just go to Start -\> Disposable VM -\> Firefox and wait a few seconds until a web browser starts. Once you close the viewing application then whole Disposable VM will get destroyed.

[![No image "r1-open-in-dispvm-3.png" attached to DisposableVms](/chrome/common/attachment.png "No image "r1-open-in-dispvm-3.png" attached to DisposableVms")](/attachment/wiki/DisposableVms/r1-open-in-dispvm-3.png)

Opening a file in a Disposable VM via command line (from AppVM)
---------------------------------------------------------------

Use the `qvm-open-in-dvm` command line (from your AppVM), e.g.:

``` {.wiki}
[user@work-pub ~]$ qvm-open-in-dvm Downloads/apple-sandbox.pdf
```

The qvm-open-in-dvm will not exit until you close the application in the Disposable VM.

Starting an arbitrary application in a disposable VM via command line (from Dom0)
---------------------------------------------------------------------------------

**Note:** Normally there should be no need for doing this -- this is just for Qubes hackers ;)

``` {.wiki}
[joanna@dom0 applications]$ echo gnome-terminal | /usr/lib/qubes/qfile-daemon-dvm qubes.VMShell dom0 DEFAULT red
```

In fact the Disposable VM appmenu used for starting Firefox contains a very similar command to the above. Please note, however, that it generally makes little sense to start any other application other than a Web Browser this way...

Using a non-default template as a basis for Disposable VM
---------------------------------------------------------

In some situations it might be beneficial to use a non-default template as a basis for Disposable VM. One example is to use a less-trusted template with some less trusted, 3rd party, often unsigned, applications installed, such as e.g. 3rd part printer drivers.

In order to regenerate Disposable VM "snapshot" (called 'savefile' on Qubes) one can conveniently use the following command in Dom0:

``` {.wiki}
[joanna@dom0 ~]$ qvm-create-default-dvm <custom-template-name>
```

This would create a new Disposable VM savefile based on the custom template. Now, whenever one opens a file (from any AppVM) in a Disposable VM, a Disposable VM based on this template will be used.
