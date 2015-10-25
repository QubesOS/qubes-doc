---
layout: doc
title: Templates
permalink: /en/doc/templates/
redirect_from:
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
[here](/en/doc/getting-started/#appvms-domains-and-templatevms). The technical
details of this implementation are described in the developer documentation
[here](/en/doc/template-implementation/).

Some templates are available in ready-to-use binary form, but some of them are
available only as source code, which can be built using
[Qubes Builder](/en/doc/qubes-builder/). In particular, some template "flavors"
are available in source code form only. Take a look at the [Qubes Builder
documentation](/en/doc/qubes-builder/) for instructions on how to compile them.


ITL Supported templates
-----------------------

These are templates which ITL is responsible for building and releasing updates
for. ITL guarantees that the binary updates are compiled from exactly the same
source code as we publish.

 * Fedora (default base template)
 * [Fedora - Minimal](/en/doc/templates/fedora-minimal)
 * [Debian](/en/doc/templates/debian/)


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

 * [Whonix](/en/doc/privacy/whonix/)
 * [Ubuntu](/en/doc/templates/ubuntu/)
 * [Archlinux](/en/doc/templates/archlinux/)


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
