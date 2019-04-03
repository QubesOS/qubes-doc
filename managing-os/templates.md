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

TemplateVMs
===========

Every TemplateBasedVM in Qubes is, as the name implies, based on some TemplateVM.
The TemplateVM is where all the software available to TemplateBasedVMs is installed.
The default template is based on Fedora, but there are additional templates based on other Linux distributions.
There are also templates available with or without certain software preinstalled.
The concept of TemplateVMs is initially described [here](/getting-started/#appvms-qubes-and-templatevms).
The technical details of this implementation are described in the developer documentation [here](/doc/template-implementation/).

Some templates are available in ready-to-use binary form, but some of them are available only as source code, which can be built using the [Qubes Builder](/doc/qubes-builder/).
In particular, some template "flavors" are available in source code form only.
Take a look at the [Qubes Builder documentation](/doc/qubes-builder/) for instructions on how to compile them.


How to install, uninstall, reinstall, and switch
------------------------------------------------

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

### How to reinstall

To reinstall a currently installed TemplateVM, see [here](/doc/reinstall-template/).

### How to switch templates (3.2)

When you install a new template or upgrade a clone of a template, it is recommended that you switch everything that was set to the old template to the new template:

1. Make the new template the default template:

        Qubes Manager --> Global settings --> Default template

2. Base AppVMs on the new template.
   In Qubes Manager, for each VM that is currently based on `old-template` that you would like to base on `new-template`, enter its VM settings and change the Template selection:

        Qubes Manager --> (Select a VM) --> VM settings --> Template

3. Base the [DisposableVM Template](/doc/glossary/#disposablevm-template) on the new template.
   If you have set the new template as your default template:

        [user@dom0 ~]$ qvm-create-default-dvm --default-template

   Otherwise:

        [user@dom0 ~]$ qvm-create-default-dvm new-template

### How to switch templates (4.0)

When you install a new template or upgrade a clone of a template, it is recommended that you switch everything that was set to the old template to the new template:

1. Make the new template the default template:

        Applications Menu --> System Tools --> Qubes Global Settings --> Default template

2. Base AppVMs on the new template.

        Applications Menu --> System Tools --> Qubes Template Manager

3. Base the [DisposableVM Template](/doc/glossary/#disposablevm-template) on the new template.

        [user@dom0 ~]$ qvm-create -l red -t new-template new-template-dvm
        [user@dom0 ~]$ qvm-prefs new-template-dvm template_for_dispvms True
        [user@dom0 ~]$ qvm-features new-template-dvm appmenus-dispvm 1
        [user@dom0 ~]$ qubes-prefs default-dispvm new-template-dvm


Invisible Things Lab (ITL) Supported templates
-----------------------

These are the templates ITL builds and releases updates for.
ITL guarantees that the binary updates are compiled from exactly the same source code as we publish.

 * [Fedora](/doc/templates/fedora/) (default base template)
 * [Fedora - Minimal](/doc/templates/fedora-minimal)
 * [Debian](/doc/templates/debian/)


Community Supported templates
-----------------------------

These templates are supported by the Qubes community. Some of them are available in ready-to-use binary package form (built by ITL), while others are available only in source code form. In all cases, ITL does not provide updates for these templates. However, such updates may be provided by the template maintainer.

By installing these templates, you are trusting not only ITL and the distribution maintainers, but also the template maintainer. In addition, these templates may be somewhat less stable, since ITL does not test them.

* [Whonix](/doc/templates/whonix/)
* [Ubuntu](/doc/templates/ubuntu/)
* [Archlinux](/doc/templates/archlinux/)


Important Notes (R4.0)
---------------

 * Whenever a TemplateBasedVM is created, the contents of the `/home`
   directory of its parent TemplateVM are *not* copied to the child TemplateBasedVM's
   `/home`. The child TemplateBasedVM's `/home`
   is always independent from its parent TemplateVM's `/home`, which means that any
   subsequent changes to the parent TemplateVM's `/home` will not affect
   the child TemplateBasedVM's `/home`.

 * `qvm-trim-template` is not necessary. All VMs are created in a thin pool
   and trimming is handled automatically. No user action is required.

|                    | Inheritance (1)                                           | Persistence (2)
|--------------------|-----------------------------------------------------------|------------------------------------------
|TemplateVM          | n/a                                                       | Everything
|TemplateBasedVM (3) | `/etc/skel` to `/home`, `/usr/local.orig` to `/usr/local` | `/rw` (includes `/home`, `/usr/local` and `bind-dirs`)
|DisposableVM        | `/rw` (includes `/home`, `/usr/local` and `bind-dirs`)    | Nothing

(1) Upon creation
(2) Following shutdown
(3) Including [DisposableVM Templates](/doc/glossary/#disposablevm-template)

Important Notes (R3.2 and earlier)
---------------

 * Whenever a TemplateBasedVM is created, the contents of the `/home`
   directory of its parent TemplateVM are copied to the child TemplateBasedVM's
   `/home`. From that point onward, the child TemplateBasedVM's `/home`
   is independent from its parent TemplateVM's `/home`, which means that any
   subsequent changes to the parent TemplateVM's `/home` will no longer affect
   the child TemplateBasedVM's `/home`.

 * Template VMs can occupy more space on the dom0 filesystem than necessary
   because they cannot employ automatic TRIM/discard on the root fs. The
   `qvm-trim-template` command in dom0 is used to recover this unused space.

   Conversely, the root filesystems in Standalone VMs *can* employ
   TRIM/discard on the root fs using normal tools and configuration options.

Important Notes (all versions)
---------------

 * Once a TemplateBasedVM has been created, any changes in its `/home`,
   `/usr/local`, or `/rw/config` directories will be persistent across reboots,
   which means that any files stored there will still be available after
   restarting the TemplateBasedVM. No changes in any other directories in
   TemplateBasedVMs persist in this manner. If you would like to make changes
   in other directories which *do* persist in this manner, you must make those
   changes in the parent TemplateVM.

 * Templates are not automatically updated when
   [updating dom0](/doc/software-update-dom0/). This is by design, since doing
   so would cause all user modifications to templates to be lost. Instead, you
   should update your templates
   [from within each template](/doc/software-update-vm/). If you *do* want to
   update a template from dom0 (and thereby lose any user modifications in the
   existing template), you must first uninstall the existing template from dom0:

       $ sudo dnf remove qubes-template-fedora-25

 * Standalone VMs using Template VMs as a basis can be created easily. These
   VMs receive a *copy* of the operating system and do not get automatically
   updated when Template VMs are updated--they must be updated individually.

 * On XFCE based Dom0, a manual action may be required to remove the "Start Menu"
   sub-menu of the removed TemplateVM. For example, to remove a dangling sub-menu
   for a removed "fedora-25" template, open a Dom0 Terminal and type:

       $ rm ~/.local/share/applications/fedora-25-*

   Just make sure there are no other TemplateVMs whose names start with "fedora-25"
   or else their menu items will be removed too.

