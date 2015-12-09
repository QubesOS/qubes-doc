---
layout: doc
title: Install Whonix in Qubes
permalink: /doc/privacy/install-whonix/
---


Install Whonix in Qubes
=======================

Installing Whonix in Qubes is simple and only requires a few simple steps.

### First Time Users

Using privacy and anonymization tools like Whonix is not a magical solution that instantly makes you anonymous online. Please consider:

* Do you know what a metadata or a man-in-the-middle attack is?
* Do you think nobody can eavesdrop on your communications because you are using Tor?
* Do you know how Whonix works?

If you answered no, have a look at the [about](https://www.whonix.org/wiki/About), [warning](https://www.whonix.org/wiki/Warning) and [do not](https://www.whonix.org/wiki/DoNot) pages (on the Whonix website) to make sure Whonix is the right tool for you and you understand  it's limitations.

---

### Install Templates

Launch the `dom0` terminal `Konsole` from your Qubes App Launcher. Then enter the following command to install the Whonix Gateway and Workstation TemplateVMs.

~~~
sudo qubes-dom0-update --enablerepo=qubes-templates-community qubes-template-whonix-gw qubes-template-whonix-ws
~~~

After doing this, you should see two new TemplateVMs in the VM Manager called `whonix-gw` and `whonix-ws`

### Configuring Whonix VMs

Create a **Whonix Gateway** ProxyVM by clicking on `Create a New VM` and select `whonix-gw` as the template and select ProxyVM as the type.

![Create Whonix Gateway ProxyVMs](/attachment/wiki/Whonix/Create_Qubes-Whonix-Gateway_ProxyVM.png)

Create a **Whonix Workstation** AppVM by clicking on `Create a New VM` and select `whonix-ws` as the template and select AppVM (should be default) as the type.

![Create Workstation AppVMs](/attachment/wiki/Whonix/Create_Qubes-Whonix-Workstation_AppVM.png)

Configure the **Whonix Gateway TemplateVM** to use the `sys-whonix` ProxyVM that you just created.

![TemplateVM Proxy Settings](/attachment/wiki/Whonix/Qubes-Whonix-Gateway_TemplateVM_Qubes_VM_Manager_Settings.png)

Great. You should be all done installing Whonix into Qubes. Use these two TemplateVMs and the ProxyVM you just added, like you would for any other VMs.

### Running Applications

To start an application in the **Whonix Workstation AppVM** that you created, launch it like any other- open the `Qubes App Launcher` and then select an app such as `Privacy Browser` which will then launch the Tor Browser


### Advanced Information

You can learn more about [customizing Whonix here](/doc/privacy/customizing-whonix/)
