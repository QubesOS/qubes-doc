---
layout: doc
title: The Fedora TemplateVM
permalink: /doc/templates/fedora/
---

The Fedora TemplateVM
=====================

The Fedora [TemplateVM] is the default TemplateVM in Qubes OS.
This page is about the standard (or "full") Fedora TemplateVM.
For the minimal version, please see the [Fedora Minimal] page.

Installing
----------

The Fedora TemplateVM comes preinstalled with Qubes OS.
However, there may be times when you wish to install a fresh copy from the Qubes repositories, e.g.:

1. When a version of Fedora reaches EOL ([end-of-life]).
2. When a new version of Fedora you wish to use becomes [supported] as a TemplateVM.
3. When you suspect your Fedora TemplateVM has been compromised.
4. When you have made modifications to the Fedora TemplateVM that you no longer want.

To install a specific Fedora TemplateVM that is not currently installed in your system, use the following command in dom0:

    $ sudo qubes-dom0-update qubes-template-fedora-27

(If necessary, replace `27` with your desired Fedora version.)

To reinstall a Fedora TemplateVM that is already installed in your system, see [How to Reinstall a TemplateVM].


After Installing
----------------

After installing a fresh Fedora TemplateVM, we recommend performing the following steps:

1. [Update the TemplateVM].
2. Switch any [TemplateBasedVMs] that are based on the old TemplateVM to the new one.
3. If desired, remove the old TemplateVM by running the following command in dom0:

        $ sudo dnf remove qubes-template-fedora-27

   (If necessary, replace `27` with your desired Fedora version.)


Upgrading
---------

To upgrade your Fedora TemplateVM, please consult the guide that corresponds to your situation:

 * [Upgrading the Fedora 27 Template to Fedora 28](/doc/template/fedora/upgrade-27-to-28/)
 * [Upgrading the Fedora 26 Template to Fedora 27](/doc/template/fedora/upgrade-26-to-27/)
 * [Upgrading the Fedora 25 Template to Fedora 26](/doc/template/fedora/upgrade-25-to-26/)
 * [Upgrading the Fedora 24 Template to Fedora 25](/doc/template/fedora/upgrade-24-to-25/)
 * [Upgrading the Fedora 23 Template to Fedora 24](/doc/template/fedora/upgrade-23-to-24/)
 * [Upgrading the Fedora 21 Template to Fedora 23](/doc/template/fedora/upgrade-21-to-23/)
 * [Upgrading the Fedora 20 Template to Fedora 21](/doc/template/fedora/upgrade-20-to-21/)
 * [Upgrading the Fedora 18 Template to Fedora 20](/doc/template/fedora/upgrade-18-to-20/)


[TemplateVM]: /doc/templates/
[Fedora Minimal]: /doc/templates/fedora-minimal/
[end-of-life]: https://fedoraproject.org/wiki/Fedora_Release_Life_Cycle#Maintenance_Schedule
[supported]: /doc/supported-versions/#templatevms
[How to Reinstall a TemplateVM]: /doc/reinstall-template/
[Update the TemplateVM]: /doc/software-update-vm/
[TemplateBasedVMs]: /doc/glossary/#templatebasedvm
[remove the old TemplateVM]: /doc/templates/#important-notes

