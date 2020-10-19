---
layout: doc
title: Installing contributed packages
permalink: /doc/installing-contributed-packages/
---

# Installing contributed packages

_This page is for users who wish to install contributed packages.
If you want to contribute a package, please see [package contributions]._


Qubes OS contributed packages are available under the [QubesOS-contrib] GitHub Project.
This is a place where our community can [contribute Qubes OS related packages, additions and various customizations][package contributions].

## Installing the repositories

If you want to install one of these packages, first you need to enable the repository in your system (dom0 and/or templates). This can be done by installing the `qubes-repo-contrib` package. This package includes the repository definition and keys necessary to download, verify, and install [QubesOS-contrib] packages.

In dom0, use `qubes-dom0-update`:

    sudo qubes-dom0-update qubes-repo-contrib

In a Fedora-based template, use `dnf`:

    sudo dnf install qubes-repo-contrib

In a Debian-based template, use `apt`:

    sudo apt update && sudo apt install qubes-repo-contrib

## Installing packages

After you've installed the repositories, you can install contributed packages.
For example, to install `qvm-screenshot-tool` in dom0:

    sudo qubes-dom0-update --clean qvm-screenshot-tool

[package contributions]: /doc/package-contributions/
[QubesOS-contrib]: https://github.com/QubesOS-contrib/

