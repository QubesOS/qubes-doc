---
layout: doc
title: The Fedora TemplateVM
permalink: /doc/templates/fedora/
---

The Fedora TemplateVM
=====================

The Fedora [TemplateVM] is the default TemplateVM in Qubes OS.
This page is about the standard (or "full") Fedora TemplateVM.
For the minimal and Xfce versions, please see the [Fedora Minimal] and [Fedora Xfce] pages.

Installing
----------

The Fedora TemplateVM comes preinstalled with Qubes OS.
However, there may be times when you wish to install a fresh copy from the Qubes repositories, e.g.:

 * When a version of Fedora reaches EOL ([end-of-life]).
 * When a new version of Fedora you wish to use becomes [supported] as a TemplateVM.
 * When you suspect your Fedora TemplateVM has been compromised.
 * When you have made modifications to the Fedora TemplateVM that you no longer want.

To install a specific Fedora TemplateVM that is not currently installed in your system, use the following command in dom0:

    $ sudo qubes-dom0-update qubes-template-fedora-XX

   (Replace `XX` with the Fedora version number of the template you wish to install.)

To reinstall a Fedora TemplateVM that is already installed in your system, see [How to Reinstall a TemplateVM].


After Installing
----------------

After installing a fresh Fedora TemplateVM, we recommend performing the following steps:

1. [Update the TemplateVM].

2. [Switch any TemplateBasedVMs that are based on the old TemplateVM to the new one][switch-templates].

3. If desired, [uninstall the old TemplateVM].


Upgrading
---------

To upgrade your Fedora TemplateVM, please consult the guide that corresponds to your situation:

 * [Upgrading the Fedora 29 Template to Fedora 30](/doc/template/fedora/upgrade-29-to-30/)
 * [Upgrading the Fedora 28 Template to Fedora 29](/doc/template/fedora/upgrade-28-to-29/)
 * [Upgrading the Fedora 27 Template to Fedora 28](/doc/template/fedora/upgrade-27-to-28/)
 * [Upgrading the Fedora 26 Template to Fedora 27](/doc/template/fedora/upgrade-26-to-27/)


[TemplateVM]: /doc/templates/
[Fedora Minimal]: /doc/templates/fedora-minimal/
[Fedora Xfce]: /doc/templates/fedora-xfce/
[end-of-life]: https://fedoraproject.org/wiki/Fedora_Release_Life_Cycle#Maintenance_Schedule
[supported]: /doc/supported-versions/#templatevms
[How to Reinstall a TemplateVM]: /doc/reinstall-template/
[Update the TemplateVM]: /doc/software-update-vm/
[switch-templates]: /doc/templates/#how-to-switch-templates
[uninstall the old TemplateVM]: /doc/templates/#how-to-uninstall

