---
lang: en
layout: doc
permalink: /doc/templates/fedora/
ref: 136
title: Fedora Templates
---


The Fedora [TemplateVM](/doc/templates/) is the default TemplateVM in Qubes OS. This page is about the standard (or "full") Fedora TemplateVM. For the minimal and Xfce versions, please see the [Minimal TemplateVMs](/doc/templates/minimal/) and [Xfce TemplateVMs](/doc/templates/xfce/) pages.

## Installing

To [install](/doc/templates/#installing) a specific Fedora TemplateVM that is not currently installed in your system, use the following command in dom0:

```
$ sudo qubes-dom0-update qubes-template-fedora-XX
```

   (Replace `XX` with the Fedora version number of the template you wish to install.)

To reinstall a Fedora TemplateVM that is already installed in your system, see [How to Reinstall a TemplateVM](/doc/reinstall-template/).

## After Installing

After installing a fresh Fedora TemplateVM, we recommend performing the following steps:

1. [Update the TemplateVM](/doc/software-update-vm/).

2. [Switch any app qubes that are based on the old TemplateVM to the new one](/doc/templates/#switching).

3. If desired, [uninstall the old TemplateVM](/doc/templates/#uninstalling).

## Updating

For routine daily updates within a given release, see [Updating software in TemplateVMs](/doc/how-to-install-software/#updating-software-in-templatevms).

## Upgrading

There are two ways to upgrade your TemplateVM to a new Fedora release:

- [Install a fresh template to replace the existing one.](#installing) **This option may be simpler for less experienced users.** After you install the new template, redo all desired template modifications and [switch everything that was set to the old template to the new template](/doc/templates/#switching). You may want to write down the modifications you make to your templates so that you remember what to redo on each fresh install. To see a log of package manager actions, open a terminal in the old Fedora template and use the `dnf history` command.

- [Perform an in-place upgrade of an existing Fedora template.](/doc/template/fedora/upgrade/) This option will preserve any modifications you've made to the template, **but it may be more complicated for less experienced users.**

