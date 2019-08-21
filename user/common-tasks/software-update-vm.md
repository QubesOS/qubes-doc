---
layout: doc
title: Installing and updating software in VMs
permalink: /doc/software-update-vm/
redirect_from:
- /en/doc/software-update-vm/
- /doc/SoftwareUpdateVM/
- /wiki/SoftwareUpdateVM/
---

Installing and updating software in VMs
=======================================

How TemplateVMs work in Qubes
------------------------------

Most of the AppVMs (domains) are based on a *TemplateVM*, which means that their root filesystem (i.e. all the programs and system files) is based on the root filesystem of the corresponding template VM.
This dramatically saves disk space, because each new AppVM needs disk space only for storing the user's files (i.e. the home directory).
Of course the AppVM has only read-access to the template's filesystem -- it cannot modify it in any way.

In addition to saving on the disk space, and reducing domain creation time, another advantage of such scheme is the possibility for centralized software update.
It's just enough to do the update in the template VM, and then all the AppVMs based on this template get updates automatically after they are restarted.

The side effect of this mechanism is, of course, that if you install any software in your AppVM, more specifically in any directory other than `/home`, `/usr/local`, or `/rw` then it will disappear after the AppVM reboots (as the root filesystem for this AppVM will again be "taken" from the TemplateVM).
**This means one normally installs software in the TemplateVM, not in AppVMs.**

The template root filesystem is created in a thin pool, so manual trims are not necessary.
See [here](/doc/disk-trim) for further discussion on enabling discards/trim support.

Installing (or updating) software in the TemplateVM
----------------------------------------------------

In order to permanently install new software, you should:

-   Start the template VM and then start either console (e.g. `gnome-terminal`) or dedicated software management application, such as `gpk-application` (*Start-\>Applications-\>Template: fedora-XX-\>Add/Remove software*),

-   Install/update software as usual (e.g. using dnf, or the dedicated GUI application).
    Then, shutdown the template VM.

-   You will see now that all the AppVMs based on this template (by default all your VMs) will be marked as "outdated" in the manager.
    This is because their filesystems have not been yet updated -- in order to do that, you must restart each VM.
    You don't need to restart all of them at the same time -- e.g. if you just need the newly installed software to be available in your 'personal' domain, then restart only this VM.
    You can restart others whenever this will be convenient to you.

Testing repositories
--------------------

### Fedora ###

There are three Qubes VM testing repositories (where `*` denotes the Release):

* `qubes-vm-*-current-testing` -- testing packages that will eventually land in the stable (`current`) repository
* `qubes-vm-*-security-testing` -- a subset of `qubes-vm-*-current-testing` that contains packages that qualify as security fixes
* `qubes-vm-*-unstable` -- packages that are not intended to land in the stable (`qubes-vm-*-current`) repository; mostly experimental debugging packages

To temporarily enable any of these repos, use the `--enablerepo=<repo-name>` option.
Example commands:

~~~
sudo dnf upgrade --enablerepo=qubes-vm-*-current-testing
sudo dnf upgrade --enablerepo=qubes-vm-*-security-testing
sudo dnf upgrade --enablerepo=qubes-vm-*-unstable
~~~

To enable or disable any of these repos permanently, change the corresponding `enabled` value to `1` in `/etc/yum.repos.d/qubes-*.repo`.

### Debian ###

Debian also has three Qubes VM testing repositories (where `*` denotes the Release):

* `*-testing` -- testing packages that will eventually land in the stable (`current`) repository
* `*-securitytesting` -- a subset of `*-testing` that contains packages that qualify as security fixes
* `*-unstable` -- packages that are not intended to land in the stable repository; mostly experimental debugging packages

To enable or disable any of these repos permanently, uncomment the corresponding `deb` line in `/etc/apt/sources.list.d/qubes-r*.list`

Reverting changes to a TemplateVM
---------------------------------

Perhaps you've just updated your TemplateVM, and the update broke your template.
Or perhaps you've made a terrible mistake, like accidentally confirming the installation of an unsigned package that could be malicious.
Fortunately, it's easy to revert changes to TemplateVMs using the command appropriate to your version of Qubes.

**Important:** This command will roll back any changes made *during the last time the TemplateVM was run, but **not** before.*
This means that if you have already restarted the TemplateVM, using this command is unlikely to help, and you'll likely want to reinstall it from the repository instead.
On the other hand, if the template is already broken or compromised, it won't hurt to try reverting first.
Just make sure to **back up** all of your data and changes first!

For example, to revert changes to the `fedora-26` TemplateVM:

1. Shut down `fedora-26`.
   If you've already just shut it down, do **not** start it again (see above).
2. In a dom0 terminal, type:

        qvm-volume revert fedora-26:root

Notes on trusting your TemplateVM(s)
-------------------------------------

As the TemplateVM is used for creating filesystems for other AppVMs where you actually do the work, it means that the TemplateVM is as trusted as the most trusted AppVM based on this template.
In other words, if your template VM gets compromised, e.g. because you installed an application, whose *installer's scripts* were malicious, then *all* your AppVMs (based on this template) will inherit this compromise.

There are several ways to deal with this problem:

-   Only install packages from trusted sources -- e.g. from the pre-configured Fedora repositories.
    All those packages are signed by Fedora, and we expect that at least the package's installation scripts are not malicious.
    This is enforced by default (at the [firewall VM level](/doc/firewall/)), by not allowing any networking connectivity in the default template VM, except for access to the Fedora repos.

-   Use *standalone VMs* (see below) for installation of untrusted software packages.

-   Use multiple templates (see below) for different classes of domains, e.g. a less trusted template, used for creation of less trusted AppVMs, would get various packages from less trusted vendors, while the template used for more trusted AppVMs will only get packages from the standard Fedora repos.

Some popular questions:

-   So, why should we actually trust Fedora repos -- it also contains large amount of third-party software that might be buggy, right?

As far as the template's compromise is concerned, it doesn't really matter whether `/usr/bin/firefox` is buggy and can be exploited, or not.
What matters is whether its *installation* scripts (such as %post in the rpm.spec) are benign or not.
Template VM should be used only for installation of packages, and nothing more, so it should never get a chance to actually run `/usr/bin/firefox` and get infected from it, in case it was compromised.
Also, some of your more trusted AppVMs would have networking restrictions enforced by the [firewall VM](/doc/firewall/), and again they should not fear this proverbial `/usr/bin/firefox` being potentially buggy and easy to compromise.

-   But why trust Fedora?

Because we chose to use Fedora as a vendor for the Qubes OS foundation (e.g. for Dom0 packages and for AppVM packages).
We also chose to trust several other vendors, such as Xen.org, kernel.org, and a few others whose software we use in Dom0.
We had to trust *somebody* as we are unable to write all the software from scratch ourselves.
But there is a big difference in trusting all Fedora packages to be non-malicious (in terms of installation scripts) vs. trusting all those packages are non-buggy and non-exploitable.
We certainly do not assume the latter.

-   So, are the template VMs as trusted as Dom0?

Not quite.
Dom0 compromise is absolutely fatal, and it leads to Game Over<sup>TM</sup>.
However, a compromise of a template affects only a subset of all your AppVMs (in case you use more than one template, or also some standalone VMs).
Also, if your AppVMs are network disconnected, even though their filesystems might get compromised due to the corresponding template compromise, it still would be difficult for the attacker to actually leak out the data stolen in an AppVM.
Not impossible (due to existence of cover channels between VMs on x86 architecture), but difficult and slow.

Standalone VMs
--------------
Standalone VMs have their own copy of the whole filesystem, and thus can be updated and managed on their own.
But this means that they take a few GBs on disk, and also that centralized updates do not apply to them.

Sometimes it might be convenient to have a VM that has its own filesystem, where you can directly introduce changes, without the need to start/stop the template VM.
Such situations include e.g.:

-   VMs used for development (devel environments require a lot of \*-devel packages and specific devel tools)

-   VMs used for installing untrusted packages.
    Normally you install digitally signed software from Red Hat/Fedora repositories, and it's reasonable that such software has non malicious *installation* scripts (rpm pre/post scripts).
    However, when you would like to install some packages from less trusted sources, or unsigned, then using a dedicated (untrusted) standalone VM might be a better way.

In order to create a standalone VM you can use a command line like this (from console in Dom0):

```
qvm-create --class StandaloneVM --label <label> --property virt_mode=hvm <vmname>
```

... or click appropriate options in the Qubes Manager's Create VM window.

(Note: Technically, `virt_mode=hvm` is not necessary for every StandaloneVM.
However, it makes sense if you want to use a kernel from within the VM.)


Using more than one template
----------------------------

It's also possible to have more than one template VM in the system.
E.g. one could clone the default template using the `qvm-clone` command in Dom0.
This allows to have a customized template, e.g. with devel packages, or less trusted apps, shared by some subset of domains.
It is important to note that the default template is "system managed" and therefore cannot be backed up using Qubes' built-in backup function.
In order to ensure the preservation of your custom settings and the availability of a "known-good" backup template, you may wish to clone the default system template and use your clone as the default template for your AppVMs.

When you create a new domain you can choose which template this VM should be based on.
If you use command line, you should use the `--template` switch:

~~~
qvm-create <vmname> --template <templatename> --label <label>
~~~

Temporarily allowing networking for software installation
---------------------------------------------------------

Some third-party applications cannot be installed using the standard yum repositories, and need to be manually downloaded and installed.
When the installation requires internet connection to access third-party repositories, it will naturally fail when run in a Template VM because the default firewall rules for templates only allow connections from package managers.
So it is necessary to modify firewall rules to allow less restrictive internet access for the time of the installation, if one really wants to install those applications into a template.
As soon as software installation is completed, firewall rules should be returned back to the default state.
The user should decide by themselves whether such third-party applications should be equally trusted as the ones that come from the standard Fedora signed repositories and whether their installation will not compromise the default Template VM, and potentially consider installing them into a separate template or a standalone VM (in which case the problem of limited networking access doesn't apply by default), as described above.

Updates proxy
-------------

Updates proxy is a service which allows access only from package managers.
This is meant to mitigate user errors (like using browser in the template VM), rather than some real isolation.
It is done with http proxy (tinyproxy) instead of simple firewall rules because it is hard to list all the repository mirrors (and keep that list up to date).
The proxy is used only to filter the traffic, not to cache anything.

The proxy is running in selected VMs (by default all the NetVMs (1)) and intercepts traffic directed to 10.137.255.254:8082.
Thanks to such configuration all the VMs can use the same proxy address, and if there is a proxy on network path, it will handle the traffic (of course when firewall rules allow that).
If the VM is configured to have access to the updates proxy (2), the startup scripts will automatically configure dnf to really use the proxy (3).
Also access to updates proxy is independent of any other firewall settings (VM will have access to updates proxy, even if policy is set to block all the traffic).

There are two services (`qvm-service`, [service framework](https://www.qubes-os.org/doc/qubes-service/)):

1. qubes-updates-proxy (and its deprecated name: qubes-yum-proxy) - a service providing a proxy for templates - by default enabled in NetVMs (especially: sys-net)
2. updates-proxy-setup (and its deprecated name: yum-proxy-setup) - use a proxy provided by another VM (instead of downloading updates directly), enabled by default in all templates

Both the old and new names work.
The defaults listed above are applied if the service is not explicitly listed in the services tab.

### Technical details

The updates proxy uses RPC/qrexec.
The proxy is configured in qrexec policy on dom0: `/etc/qubes-rpc/policy/qubes.UpdatesProxy`.
By default this is set to sys-net and/or sys-whonix, depending on firstboot choices.
This new design allows for templates to be updated even when they are not connected to any netvm.


Example policy file in R4.0 (with whonix installed, but not set as default updatevm for all templates):
```
# any VM with tag `whonix-updatevm` should use `sys-whonix`; this tag is added to `whonix-gw` and `whonix-ws` during installation and is preserved during template clone
@tag:whonix-updatevm @default allow,target=sys-whonix
@tag:whonix-updatevm @anyvm deny

# other templates use sys-net
@type:TemplateVM @default allow,target=sys-net
@anyvm @anyvm deny
```

Note on treating AppVM's root filesystem non-persistence as a security feature
------------------------------------------------------------------------------

As explained above, any AppVM that is based on a Template VM (i.e. which is not a Standalone VM) has its root filesystem non-persistent across the VM reboots.
In other words whatever changes the VM makes (or the malware running in this AppVM makes) to its root filesystem, are automatically discarded whenever one restarts the AppVM.
This might seem like an excellent anti-malware mechanism to be used inside the AppVM...

However, one should be careful with treating this property as a reliable way to keep the AppVM malware-free.
This is because the non-persistence, in the case of normal AppVMs, applies only to the root filesystem and not to the user filesystem (on which the `/home`, `/rw`, and `/usr/local` are stored) for obvious reasons.
It is possible that malware, especially malware that could be specifically written to target a Qubes-based AppVMs, could install its hooks inside the user home directory files only.
Examples of obvious places for such hooks could be: `.bashrc`, the Firefox profile directory which contains the extensions, or some PDF or DOC documents that are expected to be opened by the user frequently (assuming the malware found an exploitable bug in the PDF or DOC reader), and surely many others places, all in the user's home directory.

One advantage of the non-persistent rootfs though, is that the malware is still inactive before the user's filesystem gets mounted and "processed" by system/applications, which might theoretically allow for some scanning programs (or a skilled user) to reliably scan for signs of infections of the AppVM.
But, of course, the problem of finding malware hooks in general is hard, so this would work likely only for some special cases (e.g. an AppVM which doesn't use Firefox, as otherwise it would be hard to scan the Firefox profile directory reliably to find malware hooks there).
Also note that the user filesystem's metadata might got maliciously modified by malware in order to exploit a hypothetical bug in the AppVM kernel whenever it mounts the malformed filesystem.
However, these exploits will automatically stop working (and so the infection might be cleared automatically) after the hypothetical bug got patched and the update applied (via template update), which is an exceptional feature of Qubes OS.

Also note that DisposableVMs do not have persistent user filesystem, and so they start up completely "clean" every time.
Note the word "clean" means in this context: the same as their template filesystem, of course.

RPMFusion for a Fedora TemplateVM
---------------------------------

If you would like to enable the [RPM Fusion](http://rpmfusion.org/) repository, open a Terminal of the TemplateVM and type the following commands: 

~~~
sudo dnf config-manager --set-enabled rpmfusion-free rpmfusion-nonfree
sudo dnf upgrade --refresh
~~~

