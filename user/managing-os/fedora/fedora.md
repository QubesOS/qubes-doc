---
layout: doc
title: The Fedora TemplateVM
permalink: /doc/templates/fedora/
---

# The Fedora TemplateVM

The Fedora [TemplateVM] is the default TemplateVM in Qubes OS. This page is about the standard (or "full") Fedora TemplateVM. For the minimal and Xfce versions, please see the [Minimal TemplateVMs] and [Fedora Xfce] pages.


## Installing

To [install] a specific Fedora TemplateVM that is not currently installed in your system, use the following command in dom0:

    $ sudo qubes-dom0-update qubes-template-fedora-XX

   (Replace `XX` with the Fedora version number of the template you wish to install.)

To reinstall a Fedora TemplateVM that is already installed in your system, see [How to Reinstall a TemplateVM].


## After Installing

After installing a fresh Fedora TemplateVM, we recommend performing the following steps:

1. [Update the TemplateVM].

2. [Switch any TemplateBasedVMs that are based on the old TemplateVM to the new one][switch].

3. If desired, [uninstall the old TemplateVM].


## Updating

Routine daily updates within a given release.

Please see [Updating software in TemplateVMs].


## Upgrading

There are two ways to upgrade a TemplateVM. The easiest way is to [install] the new Fedora TemplateVM next to the Fedora TemplateVM you are currently using. Then redo all desired template modifications, and switch everything that was set to the old template to the new template.To make this process as efficient as possible, document modifications to your TemplateVMs in a text file. If you do not have this documentation yet, open a terminal in the old Fedora TemplateVM, and use the `history` command. (There is currently no other way to gain a list of explicitly installed packages. Methods like `dnf repoquery --userinstalled` and `rpm -qa` all include packages that have been installed as dependencies.)

You can also do an in-place upgrade of an installed Fedora TemplateVM. Please see [Upgrading Fedora TemplateVMs].



[TemplateVM]: /doc/templates/
[Fedora Xfce]: /doc/templates/fedora-xfce/
[Minimal TemplateVMs]: /doc/templates/minimal/
[end-of-life]: https://fedoraproject.org/wiki/Fedora_Release_Life_Cycle#Maintenance_Schedule
[supported]: /doc/supported-versions/#templatevms
[How to Reinstall a TemplateVM]: /doc/reinstall-template/
[Update the TemplateVM]: /doc/software-update-vm/
[switch]: /doc/templates/#switching
[uninstall the old TemplateVM]: /doc/templates/#uninstalling
[Updating software in TemplateVMs]: /doc/software-update-domu/#updating-software-in-templatevms
[Upgrading Fedora TemplateVMs]: /doc/template/fedora/upgrade/
[install]: /doc/templates/#installing

