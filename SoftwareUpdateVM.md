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

The default template is called **fedora-14-x64** in Qubes R1 and **fedora-18-x64** in Qubes R2 Beta2.

The side effect of this mechanism is, of course, that if you install any software in your AppVM, more specifically in any directory other than `/home` or `/usr/local` then it will disappear after the AppVM reboot (as the root filesystem for this AppVM will again be "taken" from the Template VM). **This means one normally install software in the Template VM, not in AppVMs.**

Installing (or updating) software in the template VM
----------------------------------------------------

In order to permanently install new software, you should:

-   Start the template VM and then start either console (e.g. `gnome-terminal`) or dedicated software management application, such as `gpk-application` (*Start-\>Applications-\>Template: fedora-XX-x64-\>Add/Remove software*),

-   Install/update software as usual (e.g. using yum, or the dedicated GUI application). Then, shutdown the template VM,

-   You will see now that all the AppVMs based on this template (by default all your VMs) will be marked as "outdated" in the manager. This is because their fielsystems have not been yet updated -- in order to do that, you must restart each VM. You don't need to restart all of them at the same time -- e.g. if you just need the newly installed software to be available in your 'personal' domain, then restart only this VM. You will restart others whenever this will be convenient to you.

Notes on trusting your Template VM(s)
-------------------------------------

As the template VM is used for creating filesystems for other AppVMs, where you actually do the work, it means that the template VM is as trusted as the most trusted AppVM based on this template. In other words, if your template VM gets compromised, e.g. because you installed an application, whose *installer's scripts* were malicious, then *all* your AppVMs (based on this template) will inherit this compromise.

There are several ways to deal with this problem:

-   Only install packages from trusted sources -- e.g. from the pre-configured Fedora repositories. All those packages are signed by Fedora, and as we expect that at least the package's installation scripts are not malicious. This is enforced by default (at the [firewall VM level](/wiki/QubesFirewall)), by not allowing any networking connectivity in the default template VM, except for access to the Fedora repos.

-   Use *standalone VMs* (see below) for installation of untrusted software packages.

-   Use multiple templates (see below) for different classes of domains, e.g. a less trusted template, used for creation of less trusted AppVMs, would get various packages from somehow less trusted vendors, while the template used for more trusted AppVMs will only get packages from the standard Fedora repos.

Some popular questions:

-   So, why should we actually trust Fedora repos -- it also contains large amount of 3rd party software that might buggy, right?

As long as template's compromise is considered, it doesn't really matter whether /usr/bin/firefox is buggy and can be exploited, or not. What matters is whether its *installation* scripts (such as %post in the rpm.spec) are benign or not. Template VM should be used only for installation of packages, and nothing more, so it should never get a chance to actually run the /usr/bin/firefox and got infected from it, in case it was compromised. Also, some of your more trusted AppVMs, would have networking restrictions enforced by the [firewall VM](/wiki/QubesFirewall), and again they should not fear this proverbial /usr/bin/firefox being potentially buggy and easy to compromise.

-   But why trusting Fedora?

Because we chose to use Fedora as a vendor for the Qubes OS foundation (e.g. for Dom0 packages and for AppVM packages). We also chose to trust several other vendors, such as Xen.org, kernel.org, and a few others whose software we use in Dom0. We had to trust *somebody* as we are unable to write all the software from scratch ourselves. But there is a big difference in trusting all Fedora packages to be non-malicious (in terms of installation scripts) vs. trusting all those packages are non-buggy and non-epxloitable. We certainly do not assume the latter.

-   So, are the template VMs as trusted as Dom0?

Not quite. Dom0 compromise is absolutely fatal, and it leads to Game Over (TM). However, a compromise of a template affects only a subset of all your AppVMs (in case you use more than one template, or also some standalone VMs). Also, if your AppVMs are network disconnected, even though their filesystems might got compromised due to the corresponding template compromise, it still would be difficult for the attacker to actually leak out the data stolen in an AppVM. Not impossible (due to existence of cover channels between VMs on x86 architecture), but difficult and slow.

Standalone VMs
--------------

Standalone VMs have their own copy of the whole filesystem, and thus can be updated and managed on its own. But this means that they take a few GBs on disk, and also that centralized updates do not apply to them.

Sometime it might be convenient to have a VM that has its own filesystem, where you can directly introduce changes, without the need to start/stop the template VM. Such situations include e.g.:

-   VMs used for development (devel environments requires a lot of \*-devel packages and specific devel tools)

-   VMs used for installing untrusted packages. Normally you install digitally signed software from Red Hat/Fedora repositories, and it's reasonable that such software has non malicious *installation* scripts (rpm pre/post scripts). However, when you would like to install some packages form less trusted sources, or unsigned, then using a dedicated (untrusted) standalone VM might be a better way.

In order to create a standalone VM you can use a command line like this (from console in Dom0):

``` {.wiki}
qvm-create <vmname> --standalone --label <label>
```

... or click appropriate options in the Qubes Manager's Create VM window.

Using more than one template
----------------------------

It's also possible to have more than one template VM in the system. E.g. one could clone the default template using the `qvm-clone-template` command in Dom0. This allows to have a customized template, e.g. with devel packages, or less trusted apps, shared by some subset of domains.

When you create a new domain you can choose which template this VM should be based on. If you use command line, you should use the `--template` switch:

``` {.wiki}
qvm-create <vmname> --template <templatename> --label <label>
```
