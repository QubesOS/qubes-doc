---
layout: doc
title: DispVMCustomization
permalink: /doc/UserDoc/DispVMCustomization/
redirect_from: /wiki/UserDoc/DispVMCustomization/
---

Chaanging the template used as a basis for Disposable VM
========================================================

You may want to use a non-default template as a basis for Disposable VM. One example is to use a less-trusted template with some less trusted, 3rd party, often unsigned, applications installed, such as e.g. 3rd part printer drivers.

In order to regenerate the Disposable VM "snapshot" (called 'savefile' on Qubes) one can use the following command in Dom0:

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


Customization of Disposable VM
==============================

It is possible to change the settings of each new Disposable VM (DispVM). This can be done by customizing the DispVM template:

1.  Start a terminal in the `fedora-20-x64-dvm` TemplateVM by running the following command in a dom0 terminal. (By default, this TemplateVM is not shown in Qubes VM Manager. However, it can be shown by selecting "Show/Hide internal VMs.")

    {% highlight trac-wiki %}
    [user@dom0 ~]$ qvm-run -a fedora-20-x64-dvm gnome-terminal
    {% endhighlight %}

2.  Change the VM's settings and/or applications, as desired. Note that currently Qubes supports exactly one DispVM template, so any changes you make here will affect all DispVMs. Some examples of changes you may want to make include:
    -   Changing Firefox's default startup settings and homepage.
    -   Changing Nautilus' default file preview settings.
    -   Changing the DispVM's default NetVM. For example, you may wish to set the NetVM to "none." Then, whenever you start a new DispVM, you can choose your desired ProxyVM manually (by changing the newly-started DipsVMs settings). This is useful if you sometimes wish to use a DispVM with a TorVM, for example. It is also useful if you sometimes wish to open untrusted files in a network-disconnected DispVM.

3.  Create an empty `/home/user/.qubes-dispvm-customized` file:

    {% highlight trac-wiki %}
    [user@fedora-20-x64-dvm ~]$ touch /home/user/.qubes-dispvm-customized
    {% endhighlight %}

4.  Shutdown the VM (either by `poweroff` from VM terminal, or `qvm-shutdown` from dom0 terminal).
5.  Regenerate the DispVM template:

    {% highlight trac-wiki %}
    [user@dom0 ~]$ qvm-create-default-dvm --default-template --default-script
    {% endhighlight %}

**Note:** All of the above requires at least qubes-core-vm \>= 2.1.2 installed in template.
