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

Installation
------------

The Fedora TemplateVM comes preinstalled with Qubes OS.
However, there may be times when you wish to install a fresh copy from the Qubes repositories, e.g.:

1. When a version of Fedora reaches EOL ([end-of-life]).
2. When a new version of Fedora you wish to use becomes [supported] as a TemplateVM.
3. When you suspect your Fedora TemplateVM has been compromised.
4. When you have made modifications to the Fedora TemplateVM that you no longer want.

To install a specific Fedora TemplateVM that is not currently installed in your system, use the following command in dom0:

    $ sudo qubes-dom0-update qubes-template-fedora-26

(If necessary, replace `26` with your desired Fedora version.)

To reinstall a Fedora TemplateVM that is already installed in your system, see [How to Reinstall a TemplateVM].


After Installing
----------------

After installing a fresh Fedora TemplateVM, we recommend performing the following steps:

1. [Update the TemplateVM].
2. Switch any [TemplateBasedVMs] that are based on the old TemplateVM to the new one.
3. If desired, remove the old TemplateVM by running the following command in dom0:

        $ sudo dnf remove qubes-template-fedora-26

   (If necessary, replace `26` with your desired Fedora version.)


[TemplateVM]: /doc/templates/
[Fedora Minimal]: /doc/templates/fedora-minimal/
[end-of-life]: https://fedoraproject.org/wiki/Fedora_Release_Life_Cycle#Maintenance_Schedule
[supported]: /doc/supported-versions/#templatevms
[How to Reinstall a TemplateVM]: /doc/reinstall-template/
[Update the TemplateVM]: /doc/software-update-vm/
[TemplateBasedVMs]: /doc/glossary/#templatebasedvm
[remove the old TemplateVM]: /doc/templates/#important-notes

