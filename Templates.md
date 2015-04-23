---
layout: doc
title: Templates
permalink: /doc/Templates/
redirect_from: /wiki/Templates/
---

Templates
=========

Every AppVM in Qubes is based on some template, this is where all the software
available for AppVMs is installed. Default template is based on Fedora, but
there are additional templates based on other Linux distributions, or with some
additional software installed by default. This concept is described
[here](/doc/GettingStarted/#appvms-domains-and-templatevms).

Some templates are available in ready to use binary form, but some of them are
only as a source code, which can be built using [Qubes Builder](/doc/QubesBuilder/).
Especially some templates "flavors" are available in source code form only.
Take a look at [Qubes Builder
documentation](https://github.com/QubesOS/qubes-builder/blob/master/README.md)
how to compile them.

ITL Supported templates
-----------------------

For those templates ITL is responsible for build and releasing updates,
especially ITL guarantees that the binary updates are compiled from exactly
the source code we publish.

-   Fedora
-   [Fedora - Minimal](/doc/Templates/FedoraMinimal)
-   [Debian](/doc/Templates/Debian/)

Community Supported templates
-----------------------------

Those templates are supported by Qubes Community. Some of them are available in
ready to use binary package (built by ITL), some are only in source code form.
In any case ITL does not provide updates for those templates, but such updates
can be provided by template maintainer.

In short - by installing those templates, you trust not only ITL and
distribution maintainers, but also the template maintainer. It can also happen
that those templates are somehow less stable, because we do not test them.

-   [Whonix](/doc/Templates/Whonix/)
-   [Ubuntu](/doc/Templates/Ubuntu/)
-   [Archlinux](/doc/Templates/Archlinux/)

