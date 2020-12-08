---
layout: doc
title: Gentoo Template
redirect_to: https://github.com/Qubes-Community/Contents/blob/master/docs/os/templates/gentoo.md
redirect_from:
- /doc/templates/gentoo/
---

# Gentoo Template

If you would like to use a stable, predictable, manageable and reproducible distribution in your AppVMs, you can install the Gentoo template, provided by Qubes in ready to use binary package. For the minimal and Xfce versions, please see the [Minimal TemplateVMs] and [Xfce TemplateVMs] pages.


## Installation

The standard Gentoo TemplateVM can be installed with the following command in dom0:

    [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community qubes-template-gentoo

To switch, reinstall and uninstall a Gentoo TemplateVM that is already installed in your system, see *How to [switch], [reinstall] and [uninstall]*.

#### After Installing

After a fresh install, we recommend to [Update the TemplateVM](/doc/software-update-vm/). We highlight that the template memory/CPU allocation certainly need to be adjusted in some cases. As Gentoo is a *linux source distribution*, the template needs resources to perform updates or installing any packages. By default, each TemplateVM has *2 VCPUs* for *4000 MB Max memory* allocated. If needed, double those values, *4 VCPUs* for *8000 MB Max memory*. For example, it has been observed failing updates or builds with *4 VCPUs* for *4000 MB Max memory* due to out of memory issue. For more general considerations, we refer to the official [Gentoo Handbook].

## Want to contribute?

*   [How can I contribute to the Qubes Project?](/doc/contributing/)

*   [Guidelines for Documentation Contributors](/doc/doc-guidelines/)

[switch]: /doc/templates/#switching
[reinstall]: /doc/reinstall-template/
[uninstall]: /doc/templates/#uninstalling
[Minimal TemplateVMs]: /doc/templates/minimal/
[Xfce TemplateVMs]: /doc/templates/xfce/
[Gentoo Handbook]: https://wiki.gentoo.org/wiki/Handbook:AMD64