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

How Template VM works in Qubes
------------------------------

Most of the AppVMs (domains) are based on a *template VM*, which means that their root filesystem (i.e. all the programs and system files) is based on the root filesystem of the corresponding template VM. This dramatically saves disk space, because each new AppVM needs disk space only for storing the user's files (i.e. the home directory). Of course the AppVM has only read-access to the template's filesystem -- it cannot modify it in any way.

In addition to saving on the disk space, and reducing domain creation time, another advantage of such scheme is the possibility for centralized software update. It's just enough to do the update in the template VM, and then all the AppVMs based on this template get updates automatically after they are restarted.

The default template is called **fedora-14-x64** in Qubes R1 and **fedora-20-x64** in Qubes R2.

The side effect of this mechanism is, of course, that if you install any software in your AppVM, more specifically in any directory other than `/home` or `/usr/local` then it will disappear after the AppVM reboot (as the root filesystem for this AppVM will again be "taken" from the Template VM). **This means one normally install software in the Template VM, not in AppVMs.**

Unlike VM private filesystems, the template VM root filesystem does not support discard, so deleting files does not free the space in dom0. See [these instructions](/doc/FedoraTemplateUpgrade/#compacting-templates-rootimg) to recover space in dom0.

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

-   Only install packages from trusted sources -- e.g. from the pre-configured Fedora repositories. All those packages are signed by Fedora, and as we expect that at least the package's installation scripts are not malicious. This is enforced by default (at the [firewall VM level](/doc/qubes-firewall/)), by not allowing any networking connectivity in the default template VM, except for access to the Fedora repos.

-   Use *standalone VMs* (see below) for installation of untrusted software packages.

-   Use multiple templates (see below) for different classes of domains, e.g. a less trusted template, used for creation of less trusted AppVMs, would get various packages from somehow less trusted vendors, while the template used for more trusted AppVMs will only get packages from the standard Fedora repos.

Some popular questions:

-   So, why should we actually trust Fedora repos -- it also contains large amount of 3rd party software that might buggy, right?

As long as template's compromise is considered, it doesn't really matter whether /usr/bin/firefox is buggy and can be exploited, or not. What matters is whether its *installation* scripts (such as %post in the rpm.spec) are benign or not. Template VM should be used only for installation of packages, and nothing more, so it should never get a chance to actually run the /usr/bin/firefox and got infected from it, in case it was compromised. Also, some of your more trusted AppVMs, would have networking restrictions enforced by the [firewall VM](/doc/qubes-firewall/), and again they should not fear this proverbial /usr/bin/firefox being potentially buggy and easy to compromise.

-   But why trusting Fedora?

Because we chose to use Fedora as a vendor for the Qubes OS foundation (e.g. for Dom0 packages and for AppVM packages). We also chose to trust several other vendors, such as Xen.org, kernel.org, and a few others whose software we use in Dom0. We had to trust *somebody* as we are unable to write all the software from scratch ourselves. But there is a big difference in trusting all Fedora packages to be non-malicious (in terms of installation scripts) vs. trusting all those packages are non-buggy and non-exploitable. We certainly do not assume the latter.

-   So, are the template VMs as trusted as Dom0?

Not quite. Dom0 compromise is absolutely fatal, and it leads to Game Over<sup>TM</sup>. However, a compromise of a template affects only a subset of all your AppVMs (in case you use more than one template, or also some standalone VMs). Also, if your AppVMs are network disconnected, even though their filesystems might got compromised due to the corresponding template compromise, it still would be difficult for the attacker to actually leak out the data stolen in an AppVM. Not impossible (due to existence of cover channels between VMs on x86 architecture), but difficult and slow.

Standalone VMs
--------------

Standalone VMs have their own copy of the whole filesystem, and thus can be updated and managed on its own. But this means that they take a few GBs on disk, and also that centralized updates do not apply to them.

Sometime it might be convenient to have a VM that has its own filesystem, where you can directly introduce changes, without the need to start/stop the template VM. Such situations include e.g.:

-   VMs used for development (devel environments requires a lot of \*-devel packages and specific devel tools)

-   VMs used for installing untrusted packages. Normally you install digitally signed software from Red Hat/Fedora repositories, and it's reasonable that such software has non malicious *installation* scripts (rpm pre/post scripts). However, when you would like to install some packages form less trusted sources, or unsigned, then using a dedicated (untrusted) standalone VM might be a better way.

In order to create a standalone VM you can use a command line like this (from console in Dom0):

~~~
qvm-create <vmname> --standalone --label <label>
~~~

... or click appropriate options in the Qubes Manager's Create VM window.

Using more than one template
----------------------------

It's also possible to have more than one template VM in the system. E.g. one could clone the default template using the `qvm-clone` command in Dom0. This allows to have a customized template, e.g. with devel packages, or less trusted apps, shared by some subset of domains. It is important to note that the default template is "system managed" and therefore cannot be backed up using Qubes' built-in backup function. In order to ensure the preservation of your custom settings and the availability of a "known-good" backup template, you may wish to clone the default system template and use your clone as the default template for your AppVMs.

When you create a new domain you can choose which template this VM should be based on. If you use command line, you should use the `--template` switch:

~~~
qvm-create <vmname> --template <templatename> --label <label>
~~~

Temporarily allowing networking for software installation
---------------------------------------------------------

Some 3rd party applications cannot be installed using the standard yum repositories, and need to be manually downloaded and installed. When the installation requires internet connection to access 3rd party repositories, it will naturally fail when run in a Template VM because the default firewall rules for templates only allow connections to standard yum repositories. So it is necessary to modify firewall rules to allow less restrictive internet access for the time of the installation, if one really wants to install those applications into a template. As soon as software installation is completed, firewall rules should be returned back to the default state. The user should decided by themselves whether such 3rd party applications should be equally trusted as the ones that come from the standard Fedora signed repositories and whether their installation will not compromise the default Template VM, and potentially consider installing them into a separate template or a standalone VM (in which case the problem of limited networking access doesn't apply by default), as described above.

Updates proxy
-------------

Updates proxy is a service which filter http access to allow access to only something that looks like yum or apt repository. This is meant to mitigate user errors (like using browser in the template VM), rather than some real isolation. It is done with http proxy instead of simple firewall rules because it is hard to list all the repository mirrors (and keep that list up to date). The proxy is used only to filter the traffic, not to cache anything.

The proxy is running in selected VMs (by default all the NetVMs (1)) and intercept traffic directed to 10.137.255.254:8082. Thanks to such configuration all the VMs can use the same proxy address, and if there is a proxy on network path, it will handle the traffic (of course when firewall rules allows that). If the VM is configured to have access to the updates proxy (2), the startup scripts will automatically configure yum to really use the proxy (3). Also access to updates proxy is independent of any other firewall settings (VM will have access to updates proxy, even if policy is set to block all the traffic).

(1) Services tab -\> "qubes-yum-proxy" entry; check qvm-service manual for details

(2) Firewall tab -\> Allow connections to Updates Proxy; this setting works immediately (once OK is clicked)

(3) Services tab -\> "yum-proxy-setup" entry; this setting works at next VM startup

### Technical details

1.  Updates proxy: It is running as "qubes-yum-proxy" service. Startup script of this service setup firewall rule to intercept proxy traffic:

    ~~~
    iptables -t nat -A PR-QBS-SERVICES -d 10.137.255.254/32 -i vif+ -p tcp -m tcp --dport 8082 -j REDIRECT
    ~~~

1.  VM using the proxy service Startup script (qubes-misc-post service) configure yum using /etc/yum.conf.d/qubes-proxy.conf file. It can either contain

    ~~~
    proxy=http://10.137.255.254:8082/
    ~~~

    line, or be empty. Note that this file is specifically included from main yum.conf, yum does not support real conf.d configuration style...

Note on treating AppVM's root filesystem non-persistency as a security feature
------------------------------------------------------------------------------

As explained above, any AppVM that is based on a Template VM (i.e. which is not a Standalone VM) has its root filesystem non-persistent across the VM reboots. In other words whatever changes the VM makes (or the malware running in this AppVM makes) to its root filesystem, are automatically discarded whenever one restarts the AppVM. This might seem like an excellent anti-malware mechanism to be used inside the AppVM...

However, one should be careful with treating this property as a reliable way to keep the AppVM malware-free. This is because the non-persistency, in case of normal AppVMs, applies only to the root filesystem and not to the user filesystem (on which the `/home`, `/rw`, and `/usr/local` are stored) for obvious reasons. It is possible that malware, especially malware that could be specifically written to target a Qubes-based AppVMs, could install its hooks inside the user home directory files only. Examples of obvious places for such hooks could be: `.bashrc`, the Firefox profile directory which contains the extensions, or some PDF or DOC documents that are expected to be opened by the user frequently (assuming the malware found an exploitable bug in the PDF or DOC reader), and surely many others places, all in the user's home directory.

One advantage of the non-persistent rootfs though, is that the malware is still inactive before the user's filesystem gets mounted and "processed" by system/applications, which might theoretically allow for some scanning programs (or a skilled user) to reliably scan for signs of infections of the AppVM. But, of course, the problem of finding malware hooks in general is hard, so this would work likely only for some special cases (e.g. an AppVM which doesn't use Firefox, as otherwise it would be hard to scan the Firefox profile directory reliably to find malware hooks there). Also note that the user filesystem's metadata might got maliciously modified by malware in order to exploit a hypothetical bug in the AppVM kernel whenever it mounts the malformed filesystem. However, these exploits will automatically stop working (and so the infection might be cleared automatically) after the hypothetical bug got patched and the update applied (via template update), which is an exceptional feature of Qubes OS.

Also note that Disposable VMs do not have persistent user filesystem, and so they start up completely "clean" every time. Note the word "clean" means in this context: the same as their template filesystem, of course.

RPMFusion for a Fedora TemplateVM
---------------------------------

If you would like to enable the [RPM Fusion](http://rpmfusion.org/) repository: open a Terminal of the TemplateVM and type the following commands (you may need to Allow Full Access for some minutes in the VM Firewall rules, while the new repositories are fetched): 

~~~
sudo dnf install --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager --set-enabled rpmfusion-free rpmfusion-nonfree
~~~

