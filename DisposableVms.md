---
layout: doc
title: DisposableVms
permalink: /doc/DisposableVms/
redirect_from: /wiki/DisposableVms/
---

Disposable VMs (DispVMs)
========================

Background
----------

See [this article](http://theinvisiblethings.blogspot.com/2010/06/disposable-vms.html) for a background on why would one want to use a Disposable VM and what it is.

Opening a file in a Disposable VM (via GUI)
-------------------------------------------

In some AppVM, right click on the file you wish to open in a Disposable VM (in the Nautilus file manager), then choose Scripts -\> Open in Disposable VM. Wait a few seconds and an default application for this file type should appear displaying the file content. This app is running in a whole new VM -- a disposable VM created for the purpose of view this very file. Once you close the viewing application then whole Disposable VM will get destroyed.

![r1-open-in-dispvm-1.png](/attachment/wiki/DisposableVms/r1-open-in-dispvm-1.png) ![r1-open-in-dispvm-2.png](/attachment/wiki/DisposableVms/r1-open-in-dispvm-2.png)

Opening a fresh web browser instance in a new Disposable VM
-----------------------------------------------------------

Sometimes it is convenient to open a fresh instance of Firefox within a new fresh Disposable VM. This can be easily done by using the Start Menu: just go to Start -\> Disposable VM -\> Firefox and wait a few seconds until a web browser starts. Once you close the viewing application then whole Disposable VM will get destroyed.

![r1-open-in-dispvm-3.png](/attachment/wiki/DisposableVms/r1-open-in-dispvm-3.png)

Opening a file in a Disposable VM via command line (from AppVM)
---------------------------------------------------------------

Use the `qvm-open-in-dvm` command line (from your AppVM), e.g.:

{% highlight trac-wiki %}
[user@work-pub ~]$ qvm-open-in-dvm Downloads/apple-sandbox.pdf
{% endhighlight %}

The qvm-open-in-dvm will not exit until you close the application in the Disposable VM.

Starting an arbitrary application in a disposable VM via command line (from Dom0)
---------------------------------------------------------------------------------

**Note:** Normally there should be no need for doing this -- this is just for Qubes hackers ;)

{% highlight trac-wiki %}
[joanna@dom0 ~]$ echo gnome-terminal | /usr/lib/qubes/qfile-daemon-dvm qubes.VMShell dom0 DEFAULT red
{% endhighlight %}

In fact the Disposable VM appmenu used for starting Firefox contains a very similar command to the above. Please note, however, that it generally makes little sense to start any other application other than a Web Browser this way...

Starting an arbitrary program in a Disposable VM from an AppVM
--------------------------------------------------------------

Sometimes it might be useful to start an arbitrary program, such as e.g. terminal in an Disposable VM from an AppVM. This could be simply done this way:

{% highlight trac-wiki %}
[user@vault ~]$ qvm-run '$dispvm' gnome-terminal
{% endhighlight %}

Note the above command is issued in an AppVM, not in Dom0. The created Disposable VM can be normally accessed via other tools, such as e.g. `qvm-copy-to-vm`, using its 'dispX' name, as shown by the Qubes Manager or `qvm-ls` tools. The created Disposable VM will inherit firewall settings of the ancestor VM, which is useful in some cases (e.g. when the original AppVM had networking cut off).

Using a non-default template as a basis for Disposable VM
---------------------------------------------------------

In some situations it might be beneficial to use a non-default template as a basis for Disposable VM. One example is to use a less-trusted template with some less trusted, 3rd party, often unsigned, applications installed, such as e.g. 3rd part printer drivers.

In order to regenerate Disposable VM "snapshot" (called 'savefile' on Qubes) one can conveniently use the following command in Dom0:

{% highlight trac-wiki %}
[joanna@dom0 ~]$ qvm-create-default-dvm <custom-template-name>
{% endhighlight %}

This would create a new Disposable VM savefile based on the custom template. Now, whenever one opens a file (from any AppVM) in a Disposable VM, a Disposable VM based on this template will be used.

One can easily verify if the new Disposable VM template is indeed based on a custom template (in the example below the template called "f17-yellow" was used as a basis for the Disposable VM):

{% highlight trac-wiki %}
[joanna@dom0 ~]$ ll /var/lib/qubes/dvmdata/
total 0
lrwxrwxrwx 1 joanna joanna 45 Mar 11 13:59 default_dvm.conf -> /var/lib/qubes/appvms/f17-yellow-dvm/dvm.conf
lrwxrwxrwx 1 joanna joanna 49 Mar 11 13:59 default_savefile -> /var/lib/qubes/appvms/f17-yellow-dvm/dvm-savefile
lrwxrwxrwx 1 joanna joanna 47 Mar 11 13:59 savefile_root -> /var/lib/qubes/vm-templates/f17-yellow/root.img
{% endhighlight %}

Disposable VMs and Local Forensics
----------------------------------

At this time, DispVMs should not be relied upon to circumvent local forensics, as they do not run entirely in RAM. For details, see [this thread](https://groups.google.com/d/topic/qubes-devel/QwL5PjqPs-4/discussion).
