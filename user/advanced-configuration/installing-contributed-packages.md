---
lang: en
layout: doc
redirect_from:
- /doc/installing-contributed-packages/
ref: 225
---

# Installing contributed packages

_This page is for users who wish to install contributed packages.
If you want to contribute a package, please see [package contributions](/doc/package-contributions/)._

Qubes OS contributed packages are available under the [QubesOS-contrib](https://github.com/QubesOS-contrib/) GitHub Project.
This is a place where our community can [contribute Qubes OS related packages, additions and various customizations](/doc/package-contributions/).

## Installing the repositories

If you want to install one of these packages, first you need to enable the repository in your system (dom0 and/or templates). This can be done by installing the `qubes-repo-contrib` package. This package includes the repository definition and keys necessary to download, verify, and install [QubesOS-contrib](https://github.com/QubesOS-contrib/) packages.

In dom0, use `qubes-dom0-update`:

```bash_session
sudo qubes-dom0-update qubes-repo-contrib
```

In a Fedora-based template, use `dnf`:

```bash_session
sudo dnf install qubes-repo-contrib
```

In a Debian-based template, use `apt`:

```bash_session
sudo apt update && sudo apt install qubes-repo-contrib
```

The new repository definition will be in the usual location for your distro, and it will follow the naming pattern `qubes-contrib-*`, depending on your Qubes release and whether it is in dom0 or a TemplateVM.
For example, in a Fedora TemplateVM on Qubes 4.0, the new repository definition would be:

```
/etc/yum.repos.d/qubes-contrib-vm-r4.0.repo
```

## Installing packages

After you've installed the repositories, you can install contributed packages.

**Note:** The first time you install a contrib package in dom0, you must use the `--clean` flag.

For example, to install `qvm-screenshot-tool` in dom0:

```bash_session
sudo qubes-dom0-update --clean qvm-screenshot-tool
```

Please see the package's README for specific installation and setup instructions.

