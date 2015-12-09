---
layout: doc
title: Uninstall Whonix from Qubes
permalink: /doc/privacy/uninstall-whonix/
---

Uninstall Whonix from Qubes
===========================

If you just want to remove your **Whonix-Gateway ProxyVMs** or **Whonix-Workstation AppVMs** this would not be the guide for doing that. Just use the Qubes VM Manager or command line tools for doing that.

*Warning: This guide will completely uninstall your underlying Whonix TemplateVMs. Only do this if you want to stop using Whonix or start over with a clean install of Whonix.*

### Unset or Remove Whonix TemplateVM from All VMs

In order to uninstall a Whonix TemplateVM, you first must ensure that no VMs have this TemplateVM set as its underlying template, or else the uninstall will not work. You can accomplish this by either unsetting the TemplateVM from VMs or simply by removing the VMs altogether. You only have to do this for VMs that use the TemplateVM that you will uninstall.

**Option 1a. Unsetting TemplateVM from VMs**

This option allows you to keep any VMs and their user storage contents. Note that the root storage will still be lost when uninstalling the TemplateVM, so you may want to backup anything important first.

```
dom0 -> Qubes VM Manager -> right click Whonix VM -> Shutdown VM
```

In Dom0 &raquo; Qubes VM Manager:

```
dom0 -> Qubes VM Manager -> right click Whonix VM -> VM Settings -> Basic tab -> Template -> Choose a different TemplateVM from the Template list, such as your Fedora TemplateVM.
```

**Option 1b. Removing VMs with TemplateVM**

This option will delete your user storage contents, so you may want to backup anything important first.

```
dom0 -> Qubes VM Manager -> right click Whonix VM -> Remove AppVM
```

### Uninstall Whonix TemplateVM

Note that if you have customized your TemplateVM, these will be lost when uninstalling the TemplateVM, so you may want to backup anything important first.

**Option 2a. Uninstall Whonix-Gateway TemplateVM**

Open the `dom0` terminal `Konsole`

```
Qubes App Launcher (blue/grey "Q") -> System Tools -> Konsole
```

Uninstall the qubes-template-whonix-gw template package.

~~~
sudo yum erase qubes-template-whonix-gw
~~~

**Option 2b. Uninstall Whonix-Workstation TemplateVM**

Open the `dom0` terminal `Konsole`

Uninstall the qubes-template-whonix-ws template package.

~~~
sudo yum erase qubes-template-whonix-ws
~~~
