---
layout: doc
title: Templates
permalink: /doc/templates/
redirect_from:
- /en/doc/templates/
- /doc/Templates/
- /wiki/Templates/
---

TemplateVMs
===========

Every TemplateBasedVM in Qubes is, as the name implied, based on some
TemplateVM. The TemplateVM is where all the software available to
TemplateBasedVMs is installed. The default template is based on Fedora,
but there are additional templates based on other Linux distributions. There
are also templates available with or without certain software preinstalled. The
concept of TemplateVMs is initially described
[here](/getting-started/#appvms-qubes-and-templatevms). The technical
details of this implementation are described in the developer documentation
[here](/doc/template-implementation/).

Some templates are available in ready-to-use binary form, but some of them are
available only as source code, which can be built using
[Qubes Builder](/doc/qubes-builder/). In particular, some template "flavors"
are available in source code form only. Take a look at the [Qubes Builder
documentation](/doc/qubes-builder/) for instructions on how to compile them.

To reinstall a currently installed TemplateVM, see [here](/doc/reinstall-template/).

ITL Supported templates
-----------------------

These are templates which ITL is responsible for building and releasing updates
for. ITL guarantees that the binary updates are compiled from exactly the same
source code as we publish.

 * Fedora (default base template)
 * [Fedora - Minimal](/doc/templates/fedora-minimal)
 * [Debian](/doc/templates/debian/)


Community Supported templates
-----------------------------

These templates are supported by the Qubes community. Some of them are
available in ready-to-use binary package form (built by ITL), while others
are available only in source code form. In all cases ITL, does not provide
updates for these templates. However, such updates may be provided by the
template maintainer.

By installing these templates, you are trusting not only ITL and the
distribution maintainers, but also the template maintainer. In addition,
these templates may be somewhat less stable, since ITL does not test them.

* [Whonix](/doc/templates/whonix/)
* [Ubuntu](/doc/templates/ubuntu/)
* [Archlinux](/doc/templates/archlinux/)


Important Notes
---------------

 * Whenever a TemplateBasedVM is created, the contents of the `/home`
   directory of its parent TemplateVM are copied to the child TemplateBasedVM's
   `/home`. From that point onward, the child TemplateBasedVM's `/home`
   is independent from its parent TemplateVM's `/home`, which means that any
   subsequent changes to the parent TemplateVM's `/home` will no longer affect
   the child TemplateBasedVM's `/home`.

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

       $ sudo yum remove qubes-template-fedora-24

 * Standalone VMs using Template VMs as a basis can be created easily. These
   VMs receive a *copy* of the operating system and do not get automatically
   updated when Template VMs are updated--they must be updated individually.
   
 * Template VMs can occupy more space on the dom0 filesystem than necessary
   because they cannot employ automatic TRIM/discard on the root fs. The
   `qvm-trim-template` command in dom0 is used to recover this unused space.

   Conversely, the root filesystems in Standalone VMs *can* employ
   TRIM/discard on the root fs using normal tools and configuration options.
 
 * On XFCE based Dom0, a manual action may be required to remove the "Start Menu"
   sub-menu of the removed TemplateVM. For example, to remove a dangling sub-menu
   for a removed "fedora-24" template, open a Dom0 Terminal and type:

       $ rm ~/.local/share/applications/fedora-24-*

   Just make sure there are no other TemplateVMs whose names start with "fedora-24"
   or else their menu items will be removed too. 
       
