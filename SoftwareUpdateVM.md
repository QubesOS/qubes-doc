---
layout: wiki
title: SoftwareUpdateVM
permalink: /wiki/SoftwareUpdateVM/
---

Installing and updating software in VMs
=======================================

How Template VM works in Qubes
------------------------------

Most of the AppVMs (domains) are based on a *template VM*, which means that their root filesystem (i.e. all the programs and system files) is based on the root filesystem of the corresponding template VM. This dramatically saves disk space, because each new AppVM needs disk space only for storing the user's files (i.e. the home directory). Of course the AppVM has only read-access to the template's filesystem -- it cannot modify it in any way.

In addition to saving on the disk space, and reducing domain creation time, another advantage of such scheme is the possibility for centralized software update. It's just enough to do the update in the template VM, and then all the AppVMs based on this template get updates automatically after they are restarted.

The default template in Qubes R1 is called **fedora-14-x64**.

Installing (or updating) software in the template VM
----------------------------------------------------

In order to permanently install new software, you should start the template VM and then start either console or dedicated software management application, such as gpk-application (Start-\>Applications-\>Template: fedora-14-x64-\>[Add/Remove?](/wiki/Add/Remove) software".

Install/update software as usual (e.g. using yum, or the dedicated GUI application). Then, shutdown the template VM.

You will see now that all the AppVMs based on this template (by default all your VMs) will be marked as "outdated" in the manager. This is because their fielsystem has not been yet updated -- in order to do that, you must restart each VM. You don't need to restart all of them at the same time -- e.g. if you just need the newly installed software to be available in your 'personal' domain, then restart only this VM. You will restart others whenever this will be convenient to you.

Standalone VMs
--------------

Standalone VMs have their own copy of the whole filesystem, and thus can be updated and managed on its own. But this means that they take a few GBs on disk, and also that centralized updates do not apply to them.

Sometime it might be convenient to have a VM that has its own filesystem, where you can directly introduce changes, without the need to start/stop the template VM. Such situations include e.g.:

-   VMs used for development (devel environments requires a lot of \*-devel packages and specific devel tools)
-   VMs used for installing untrusted packages. Normally you install digitally signed software from Red [Hat/Fedora?](/wiki/Hat/Fedora) repositories, and it's reasonable that such software has non malicious *installation* scripts (rpm pre/post scripts). However, when you would like to install some packages form less trusted sources, or unsigned, then using a dedicated (untrusted) standalone VM might be a better way.

In order to create a standalone VM you must currently use command line (from console in Dom0):

``` {.wiki}
qvm-create <vmname> --standalone --label <label>
```

Using more than one template
----------------------------

It's also possible to have more than one template VM in the system. E.g. one could clone the default template using the ```qvm-clone-template``` command in Dom0. This allows to have a customized template, e.g. with devel packages, or less trusted apps, shared by some subset of domains.

When you create a new domain you can choose which template this VM should be based on. If you use command line, you should use the ```--template`\` switch:

``` {.wiki}
qvm-create <vmname> --template <templatename> --label <label>
```
