---
layout: doc
title: The Fedora Xfce TemplateVM
permalink: /doc/templates/fedora-xfce/
---

The Fedora Xfce TemplateVM
=====================

If you would like to use Fedora Xfce (more lightweight compared to GNOME desktop environment) Linux distribution in your qubes, you can install one of the available Fedora Xfce templates.


Installing
----------

To install a specific Fedora Xfce TemplateVM that is not currently installed in your system, use the following command in dom0:

    $ sudo qubes-dom0-update --enablerepo=qubes-templates-itl-testing qubes-template-fedora-XX-xfce

   (Replace `XX` with the Fedora Xfce version number of the template you wish to install.)

To reinstall a Fedora Xfce TemplateVM that is already installed in your system, see [How to Reinstall a TemplateVM](/doc/reinstall-template/).

Upgrading
---------

To upgrade your Fedora TemplateVM, please see [Upgrade Fedora TemplateVM](/doc/templates/fedora/#upgrading).