---
layout: doc
title: Templates
permalink: /doc/templates/
redirect_from:
- /doc/template/
- /en/doc/templates/
- /doc/Templates/
- /wiki/Templates/
---

# TemplateVMs

Every TemplateBasedVM in Qubes is, as the name implies, based on some TemplateVM.
The TemplateVM is where all the software available to TemplateBasedVMs is installed.
The default template is based on Fedora, but there are additional templates based on other Linux distributions.
There are also templates available with or without certain software preinstalled.
The concept of TemplateVMs is initially described [here](/getting-started/#appvms-qubes-and-templatevms).
The technical details of this implementation are described in the developer documentation [here](/doc/template-implementation/).

Some templates are available in ready-to-use binary form, but some of them are available only as source code, which can be built using the [Qubes Builder](/doc/qubes-builder/).
In particular, some template "flavors" are available in source code form only.
Take a look at the [Qubes Builder documentation](/doc/qubes-builder/) for instructions on how to compile them.


## Official templates

These are the official Qubes OS Project templates.
We build and release updates for these templates.
We guarantee that the binary updates are compiled from exactly the same source code as we publish.

 * [Fedora](/doc/templates/fedora/) (default base template)
 * [Fedora - Minimal](/doc/templates/fedora-minimal)
 * [Debian](/doc/templates/debian/)


## Community templates

These templates are supported by the Qubes community. Some of them are available in ready-to-use binary package form (built by the Qubes developers), while others are available only in source code form. In all cases, the Qubes OS Project does not provide updates for these templates. However, such updates may be provided by the template maintainer.

By installing these templates, you are trusting not only the Qubes developers and the distribution maintainers, but also the template maintainer. In addition, these templates may be somewhat less stable, since the Qubes developers do not test them.

* [Whonix](/doc/templates/whonix/)
* [Ubuntu](/doc/templates/ubuntu/)
* [Archlinux](/doc/templates/archlinux/)


## How to install, uninstall, reinstall, and switch


### How to install

Please refer to each TemplateVM's installation instructions below.
Usually, the installation method is to execute the following type of command in dom0:

    $ sudo qubes-dom0-update qubes-template-<name>

(where `qubes-template-<name>` is the name of your TemplateVM package)


### How to uninstall

To uninstall a TemplateVM, execute the following type of command in dom0:

    $ sudo dnf remove qubes-template-<name>

(where `qubes-template-<name>` is the name of your TemplateVM package)

If this doesn't work, you can [remove it manually](/doc/remove-vm-manually/).

If the Applications Menu entry doesn't go away after you uninstall a TemplateVM, execute the following type of command in dom0:

    $ rm ~/.local/share/applications/<template-vm-name>


### How to reinstall

To reinstall a currently installed TemplateVM, see [here](/doc/reinstall-template/).


### How to switch templates

When you install a new template or upgrade a clone of a template, it is recommended that you switch everything that was set to the old template to the new template:

1. Make the new template the default template.

        Applications Menu --> System Tools --> Qubes Global Settings --> Default template

2. Base AppVMs on the new template.

        Applications Menu --> System Tools --> Qubes Template Manager

3. Base the [DisposableVM Template](/doc/glossary/#disposablevm-template) on the new template.

        [user@dom0 ~]$ qvm-create -l red -t new-template new-template-dvm
        [user@dom0 ~]$ qvm-prefs new-template-dvm template_for_dispvms True
        [user@dom0 ~]$ qvm-features new-template-dvm appmenus-dispvm 1
        [user@dom0 ~]$ qubes-prefs default-dispvm new-template-dvm


## Inheritance and Persistence

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
(3) Including [DisposableVM Templates](/doc/glossary/#disposablevm-template)


## Updating TemplateVMs

Templates are not automatically updated when [updating dom0](/doc/software-update-dom0/).
This is by design, since doing so would cause all user modifications to templates to be lost.
Instead, you should update your templates [from within each template](/doc/software-update-vm/).

When you create a StandaloneVM from a TemplateVM, the StandaloneVM is independent from the TemplateVM.
It will not be updated when the TemplateVM is updated.
Rather, it must be updated individually from inside the StandaloneVM.


## Important Notes

 * `qvm-trim-template` is no longer necessary or available in Qubes 4.0 and higher.
   All VMs are created in a thin pool and trimming is handled automatically.
   No user action is required.

