---
layout: doc
title: TemplateVMs
permalink: /doc/templates/
redirect_from:
- /doc/template/
- /en/doc/templates/
- /doc/Templates/
- /wiki/Templates/
---

# TemplateVMs

In [Getting Started], we covered the distinction in Qubes OS between where you *install* your software and where you *run* your software.
Your software is installed in [TemplateVMs] (or "templates" for short).
Each TemplateVM shares its root filesystem (i.e., all of its programs and system files) with other qubes called [TemplateBasedVMs].
TemplateBasedVMs are where you run your software and store your data.

The TemplateVM system has significant benefits:

 * **Security:** Each qube has read-only access to the TemplateVM on which it's based, so if a qube is compromised, it cannot infect its TemplateVM or any of the other qubes based on that TemplateVM.
 * **Storage:** Each qube based on a TemplateVM uses only the disk space required to store its own data (i.e., your files in its home directory), which dramatically saves on disk space.
 * **Speed:** It is extremely fast to create new TemplateBasedVMs, since the root filesystem already exists in the TemplateVM.
 * **Updates:** Updates are naturally centralized, since updating a TemplateVM means that all qubes based on it will automatically use those updates after they're restarted.

An important side effect of this system is that any software installed in a TemplateBasedVM (rather than in the TemplateVM on which it is based) will disappear after the TemplateBasedVM reboots (see [Inheritance and Persistence]).
For this reason, we recommend installing most of your software in TemplateVMs, not TemplateBasedVMs.

The default TemplateVM in Qubes is based on Fedora, but there are additional templates based on other Linux distributions.
There are also templates available with or without certain software preinstalled.
You may find it useful to have multiple TemplateVMs installed in order to provide:

 * Different security levels (e.g., more or less trusted software installed)
 * Different environments (e.g., Fedora, Debian, Whonix)
 * Different tools (e.g., office, media, development, hardware drivers)


## Official

These are the official Qubes OS Project templates.
We build and release updates for these templates.
We guarantee that the binary updates are compiled from exactly the same source code as we publish.

 * [Fedora] (default)
 * Fedora [Minimal]
 * Fedora [Xfce]
 * [Debian]
 * Debian [Minimal]

## Community

These templates are supported by the Qubes community.
Some of them are available in ready-to-use binary package form (built by the Qubes developers), while others are available only in source code form.
In all cases, the Qubes OS Project does not provide updates for these templates.
However, such updates may be provided by the template maintainer.

By installing these templates, you are trusting not only the Qubes developers and the distribution maintainers, but also the template maintainer.
In addition, these templates may be somewhat less stable, since the Qubes developers do not test them.

 * [Whonix]
 * [Ubuntu]
 * [Arch Linux]
 * [CentOS]
 * CentOS [Minimal]

## Installing

Certain TemplateVMs come preinstalled with Qubes OS.
However, there may be times when you wish to install a fresh TemplateVM from the Qubes repositories, e.g.:

 * When a TemplateVM version you're using reaches [end-of-life][supported].
 * When a new version of a TemplateVM that you wish to use becomes [supported].
 * When you suspect your TemplateVM has been compromised.
 * When you have made modifications to your TemplateVM that you no longer want.

Please refer to each TemplateVM's installation instructions.
Usually, the installation method is to execute the following type of command in dom0:

    $ sudo qubes-dom0-update qubes-template-<name>

(where `qubes-template-<name>` is the name of your TemplateVM package)


## After Installing

After installing a fresh TemplateVM, we recommend performing the following steps:

1. [Update the TemplateVM].

2. [Switch any TemplateBasedVMs that are based on the old TemplateVM to the new one][switch].

3. If desired, [uninstall the old TemplateVM].


## Updating

Updating TemplateVMs is an important part of [Updating Qubes OS].
Please see [Updating software in TemplateVMs].


## Uninstalling

To uninstall a TemplateVM, execute the following type of command in dom0:

    $ sudo dnf remove qubes-template-<name>

(where `qubes-template-<name>` is the name of your TemplateVM package)

If this doesn't work, please see [How to Remove VMs Manually].

If the Applications Menu entry doesn't go away after you uninstall a TemplateVM, execute the following type of command in dom0:

    $ rm ~/.local/share/applications/<template-vm-name>


## Reinstalling

Please see [How to Reinstall a TemplateVM].


## Switching

When you install a new template or upgrade a clone of a template, it is recommended that you switch everything that was set to the old template to the new template:

1. Make the new template the default template.

        Applications Menu --> System Tools --> Qubes Global Settings --> Default template

2. Base AppVMs on the new template.

        Applications Menu --> System Tools --> Qubes Template Manager

3. Base the [DisposableVM Template] on the new template.

        [user@dom0 ~]$ qvm-create -l red -t new-template new-template-dvm
        [user@dom0 ~]$ qvm-prefs new-template-dvm template_for_dispvms True
        [user@dom0 ~]$ qvm-features new-template-dvm appmenus-dispvm 1
        [user@dom0 ~]$ qubes-prefs default-dispvm new-template-dvm

## Advanced

The following sections cover advanced topics pertaining to TemplateVMs.


### Inheritance and Persistence

Whenever a TemplateBasedVM is created, the contents of the `/home` directory of its parent TemplateVM are *not* copied to the child TemplateBasedVM's `/home`.
The child TemplateBasedVM's `/home` is always independent from its parent TemplateVM's `/home`, which means that any subsequent changes to the parent TemplateVM's `/home` will not affect the child TemplateBasedVM's `/home`.

Once a TemplateBasedVM has been created, any changes in its `/home`, `/usr/local`, or `/rw/config` directories will be persistent across reboots, which means that any files stored there will still be available after restarting the TemplateBasedVM.
No changes in any other directories in TemplateBasedVMs persist in this manner. If you would like to make changes in other directories which *do* persist in this manner, you must make those changes in the parent TemplateVM.

|                    | Inheritance (1)                                           | Persistence (2)
|--------------------|-----------------------------------------------------------|------------------------------------------
|TemplateVM          | n/a                                                       | Everything
|TemplateBasedVM (3) | `/etc/skel` to `/home`, `/usr/local.orig` to `/usr/local` | `/rw` (includes `/home`, `/usr/local` and `bind-dirs`)
|DisposableVM        | `/rw` (includes `/home`, `/usr/local` and `bind-dirs`)    | Nothing

(1) Upon creation  
(2) Following shutdown  
(3) Including [DisposableVM Template]s


### Trusting your TemplateVMs

As the TemplateVM is used for creating filesystems for other AppVMs where you actually do the work, it means that the TemplateVM is as trusted as the most trusted AppVM based on this template.
In other words, if your template VM gets compromised, e.g. because you installed an application, whose *installer's scripts* were malicious, then *all* your AppVMs (based on this template) will inherit this compromise.

There are several ways to deal with this problem:

 * Only install packages from trusted sources -- e.g. from the pre-configured Fedora repositories.
   All those packages are signed by Fedora, and we expect that at least the package's installation scripts are not malicious.
   This is enforced by default (at the [firewall VM level](/doc/firewall/)), by not allowing any networking connectivity in the default template VM, except for access to the Fedora repos.

 * Use *standalone VMs* (see below) for installation of untrusted software packages.

 * Use multiple templates (see below) for different classes of domains, e.g. a less trusted template, used for creation of less trusted AppVMs, would get various packages from less trusted vendors, while the template used for more trusted AppVMs will only get packages from the standard Fedora repos.

Some popular questions:

> So, why should we actually trust Fedora repos -- it also contains large amount of third-party software that might be buggy, right?

As far as the template's compromise is concerned, it doesn't really matter whether `/usr/bin/firefox` is buggy and can be exploited, or not.
What matters is whether its *installation* scripts (such as %post in the rpm.spec) are benign or not.
Template VM should be used only for installation of packages, and nothing more, so it should never get a chance to actually run `/usr/bin/firefox` and get infected from it, in case it was compromised.
Also, some of your more trusted AppVMs would have networking restrictions enforced by the [firewall VM](/doc/firewall/), and again they should not fear this proverbial `/usr/bin/firefox` being potentially buggy and easy to compromise.

> But why trust Fedora?

Because we chose to use Fedora as a vendor for the Qubes OS foundation (e.g. for Dom0 packages and for AppVM packages).
We also chose to trust several other vendors, such as Xen.org, kernel.org, and a few others whose software we use in Dom0.
We had to trust *somebody* as we are unable to write all the software from scratch ourselves.
But there is a big difference in trusting all Fedora packages to be non-malicious (in terms of installation scripts) vs. trusting all those packages are non-buggy and non-exploitable.
We certainly do not assume the latter.

> So, are the template VMs as trusted as Dom0?

Not quite.
Dom0 compromise is absolutely fatal, and it leads to Game Over<sup>TM</sup>.
However, a compromise of a template affects only a subset of all your AppVMs (in case you use more than one template, or also some standalone VMs).
Also, if your AppVMs are network disconnected, even though their filesystems might get compromised due to the corresponding template compromise, it still would be difficult for the attacker to actually leak out the data stolen in an AppVM.
Not impossible (due to existence of cover channels between VMs on x86 architecture), but difficult and slow.


### Note on treating TemplateBasedVMs' root filesystem non-persistence as a security feature

Any TemplateBasedVM that is based on a TemplateVM has its root filesystem non-persistent across VM reboots.
In other words, whatever changes the VM makes (or the malware running in this VM makes) to its root filesystem, are automatically discarded whenever one restarts the VM.

This might seem like an excellent anti-malware mechanism to be used inside the VM.
However, one should be careful with treating this property as a reliable way to keep the VM malware-free.
This is because the non-persistence, in the case of normal VMs, applies only to the root filesystem and not to the user filesystem (on which the `/home`, `/rw`, and `/usr/local` are stored) for obvious reasons.
It is possible that malware, especially malware that could be specifically written to target a Qubes-based VMs, could install its hooks inside the user home directory files only.
Examples of obvious places for such hooks could be: `.bashrc`, the Firefox profile directory which contains the extensions, or some PDF or DOC documents that are expected to be opened by the user frequently (assuming the malware found an exploitable bug in the PDF or DOC reader), and surely many others places, all in the user's home directory.

One advantage of the non-persistent rootfs though, is that the malware is still inactive before the user's filesystem gets mounted and "processed" by system/applications, which might theoretically allow for some scanning programs (or a skilled user) to reliably scan for signs of infections of the AppVM.
But, of course, the problem of finding malware hooks in general is hard, so this would work likely only for some special cases (e.g. an AppVM which doesn't use Firefox, as otherwise it would be hard to scan the Firefox profile directory reliably to find malware hooks there).
Also note that the user filesystem's metadata might got maliciously modified by malware in order to exploit a hypothetical bug in the AppVM kernel whenever it mounts the malformed filesystem.
However, these exploits will automatically stop working (and so the infection might be cleared automatically) after the hypothetical bug got patched and the update applied (via template update), which is an exceptional feature of Qubes OS.

Also note that DisposableVMs do not have persistent user filesystem, and so they start up completely "clean" every time.
Note the word "clean" means in this context: the same as their template filesystem, of course.


### Important Notes

 * `qvm-trim-template` is no longer necessary or available in Qubes 4.0 and higher.
   All VMs are created in a thin pool and trimming is handled automatically.
   No user action is required.
   See [Disk Trim] for more information.

 * RPM-installed templates are "system managed" and therefore cannot be backed up using Qubes' built-in backup function.
   In order to ensure the preservation of your custom settings and the availability of a "known-good" backup template, you may wish to clone the default system template and use your clone as the default template for your AppVMs.

 * Some templates are available in ready-to-use binary form, but some of them are available only as source code, which can be built using the [Qubes Builder].
   In particular, some template "flavors" are available in source code form only.
   For the technical details of the template system, please see [TemplateVM Implementation].
   Take a look at the [Qubes Builder] documentation for instructions on how to compile them.


[Getting Started]: /getting-started/
[TemplateVMs]: /doc/glossary/#templatevm
[TemplateBasedVMs]: /doc/glossary/#templatebasedvm
[Fedora]: /doc/templates/fedora/
[Minimal]: /doc/templates/minimal/
[Xfce]: /doc/templates/fedora-xfce
[Debian]: /doc/templates/debian/
[Whonix]: /doc/templates/whonix/
[Ubuntu]: /doc/templates/ubuntu/
[Arch Linux]: /doc/templates/archlinux/
[CentOS]: /doc/templates/centos/
[Qubes Builder]: /doc/qubes-builder/
[TemplateVM Implementation]: /doc/template-implementation/
[How to Remove VMs Manually]: /doc/remove-vm-manually/
[DisposableVM Template]: /doc/glossary/#disposablevm-template
[Updating Qubes OS]: /doc/updating-qubes-os/
[Disk Trim]: /doc/disk-trim
[Inheritance and Persistence]: #inheritance-and-persistence
[supported]: /doc/supported-versions/
[Update the TemplateVM]: #updating
[switch]: #switching
[uninstall the old TemplateVM]: #uninstalling
[Updating software in TemplateVMs]: /doc/software-update-domu/#updating-software-in-templatevms
[How to Reinstall a TemplateVM]: /doc/reinstall-template/
