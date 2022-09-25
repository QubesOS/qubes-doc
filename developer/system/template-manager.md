---
layout: doc
title: Template manager
permalink: /doc/template-manager/
---

This document discusses the designs and technical details of `qvm-template`, a
template manager application. The goal of the project is to design a new
mechanism for template distribution and a unified tool for template management.

## Motivation

This project was originally proposed in the 2020 Google Summer of Code program.

Previously, templates were distributed by RPM packages and managed by
`yum`/`dnf`. However, tracking inherently dynamic VM images with a package
manager suited for static files creates some challenges. For example, users may
accidentally update the images, overriding local changes
([#996](https://github.com/QubesOS/qubes-issues/issues/996),
[#1647](https://github.com/QubesOS/qubes-issues/issues/1647)). (Or in the case
of [#2061](https://github.com/QubesOS/qubes-issues/issues/2061), want to
specifically override the changes.) Other operations that work well on normal
VMs are also somewhat inconsistent on RPM-managed templates. This includes
actions such as renaming
([#839](https://github.com/QubesOS/qubes-issues/issues/839)), removal
([#5509](https://github.com/QubesOS/qubes-issues/issues/5509)) and
backup/restore ([#1385](https://github.com/QubesOS/qubes-issues/issues/1385),
[#1453](https://github.com/QubesOS/qubes-issues/issues/1453), [discussion thread 1](https://groups.google.com/forum/#!topic/qubes-devel/rwc2_miCNNE/discussion),
[discussion thread 2](https://groups.google.com/forum/#!topic/qubes-users/uQEUpv4THsY/discussion)).
In turn, this creates inconveniences and confusion for users
([#1403](https://github.com/QubesOS/qubes-issues/issues/1403),
[#4518](https://github.com/QubesOS/qubes-issues/issues/4518)).

Also, the usage of RPM packages meant that installing a template results in
arbitrary code execution, which is not ideal.

Besides distribution, users may also wish to have an integrated template
management application
([#2062](https://github.com/QubesOS/qubes-issues/issues/2062),
[#2064](https://github.com/QubesOS/qubes-issues/issues/2064),
[#2534](https://github.com/QubesOS/qubes-issues/issues/2534),
[#3040](https://github.com/QubesOS/qubes-issues/issues/3040)), as opposed to
the situation where multiple programs are required for different purposes,
e.g., `qubes-dom0-update`, `dnf`, `qvm-remove`, `qubes-manager`.

To tackle these issues, `qvm-template` was created. It strives to provide not
only a better mechanism for handling template installation but also a
consistent user-facing interface to deal with template management.

## Features

- Install/reinstall/downgrade/upgrade templates, either from local packages or
  remote repositories
  - Ability to install templates in alternative pools
  - Possibility for the template package to specify options such as the kernel
    or `virt_mode` used by the resulting template
- List and show information about local and available templates
  - Machine-readable output for easy extension
- Search for templates
- Remove templates
  - Optionally, VMs based on the template to be removed can be either removed
    or "disassociated" -- namely, have their templates changed to a "dummy"
    one.
- Show available repositories
- Works in both dom0 and management VMs by utilizing the Admin API
- Works well with existing tools
- Command-line interface with DNF-like usage
- A graphical interface also available

## Package format

The RPM package format is still used. However, the contents are manually
extracted instead of installing the whole package. This allows us to take
advantage of existing tools for things like repository management. We can also
avoid the burden of dealing with verification, reducing the risk of issues like
[QSB-028](/news/2016/12/19/qsb-28/).

The package name should be in the form `qubes-template-<TEMPLATE_NAME>`.

The package metadata (summary, description, etc.) should not contain the `|`
character to avoid possibly cryptic errors. This is because of its use as an
internal separator. Note that as we already consider the repository metadata
untrusted. This should not result in security issues.

The file structure should be quite similar to previous template RPMs. Namely,
there should be the following files in the package:

- `var/lib/qubes/vm-templates/<TEMPLATE_NAME>/root.img.part.[00,01,...]`
  - Split tarball of template `root.img`
  - Note that the file is still split due to tools such as `rpm2cpio` not
    supporting large files. (Notably, the cpio format does not support files
    over 4GiB.)
- `var/lib/qubes/vm-templates/<TEMPLATE_NAME>/template.conf`
  - Stores custom package metadata (as RPM does not support custom attributes).
  - Uses `KEY=VALUE` format.
  - Fields (corresponding to
    [qvm-prefs](https://dev.qubes-os.org/projects/core-admin-client/en/stable/manpages/qvm-prefs.html#common-properties)
    and
    [qvm-features](https://dev.qubes-os.org/projects/core-admin-client/en/stable/manpages/qvm-features.html#list-of-known-features)
    tags with the same names)
    - `virt_mode`
      - Setting this to `pv` requires user confirmation.
      - Permitted values: `pv`, `pvh`, `hvm`.
    - `kernel`
      - Only allowed to be set to "" (without quotes), i.e., "none", for
	PVGrub.
    - Network-related flags: (Must be set to IPv4 addresses in the form of
      `x.x.x.x`.)
      - `net.fake-ip`
      - `net.fake-gateway`
      - `net.fake-netmask`
    - Boolean flags: (Permitted values are "1" and "0", denoting "true" and
      "false" respectively.)
      - `no-monitor-layout`
      - `pci-e820-host`
      - `linux-stubdom`
      - `gui`
      - `gui-emulated`
      - `qrexec`
- `var/lib/qubes/vm-templates/<TEMPLATE_NAME>/whitelisted-appmenus.list`
  - Contains default app menu entries of the template itself.
- `var/lib/qubes/vm-templates/<TEMPLATE_NAME>/vm-whitelisted-appmenus.list`
  - Contains default app menu entries of VMs based on the template.
- `var/lib/qubes/vm-templates/<TEMPLATE_NAME>/netvm-whitelisted-appmenus.list`
  - Contains default app menu entries of NetVMs based on the template.
  - These three files are the same as the current format.
  - Note that the contents of these files are stored in `qvm-features` upon
    installation. See the section below for details.

## Metadata storage

The template manager needs to keep metadata of installed templates such as
versions and origin. This data can be stored via `qvm-features` to keep things
consistent when, e.g., `qvm-remove` is used. Besides, backups are also more
easily handled this way.

Also, the fields can serve as an indicator of whether a template is installed
by `qvm-template`.

### Fields

Most of the fields should be fairly self-explanatory.

- `template-name`
  - Note that this field needs to be consistent with the template name to be
    considered valid.
- `template-epoch`
- `template-version`
- `template-release`
- `template-reponame`
- `template-buildtime`
- `template-installtime`
  - The times are in UTC, and are of the format `YYYY-MM-DD HH:MM:SS`.
- `template-license`
- `template-url`
- `template-summary`
- `template-description`
  - Note that the newlines in this field are converted to `|` to work better
    with existing tools like `qvm-features`.
- `menu-items`
- `default-menu-items`
- `netvm-menu-items`
  - The `*menu-items` entries store the contents of
    `var/lib/qubes/vm-templates/<TEMPLATE_NAME>/whitelisted-appmenus.list`,
    `var/lib/qubes/vm-templates/<TEMPLATE_NAME>/vm-whitelisted-appmenus.list`,
    `var/lib/qubes/vm-templates/<TEMPLATE_NAME>/netvm-whitelisted-appmenus.list`
    respectively.
  - Note that newlines are converted to spaces, again for it to work better
    with existing tools. This should not cause ambiguity as [the FreeDesktop specifications](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html)
    forbid spaces in .desktop file names.

## Repository management

For UpdateVMs to access the repository configuration, the package
[qubes-repo-templates](https://github.com/WillyPillow/qubes-repo-templates) is
created with the following contents:

- `/etc/qubes/repo-templates/*.repo`: repository configuration
- `/etc/qubes/repo-templates/keys`: PGP keys

As template keys may be less trusted, they are *not* added to the system RPM
keychain but instead managed separately.

## Qrexec protocol

Dom0 and management VMs without network access also need to interact with
template repositories. The following qrexec calls that list and download
templates are thus proposed.

- `qubes.TemplateSearch`: wraps `dnf repoquery`
- `qubes.TemplateDownload`: wraps `dnf download`

### Input

Both calls accept the following format from standard input:

```text
arg1
arg2
...
argN
package-file-spec
---
repo config
```

In other words, the input consists of two parts separated by the line `---`.
The first part contains some arguments and `package-file-spec` that indicates
the pattern to be queried or downloaded. The following arguments are allowed:

- `--enablerepo=<repoid>`
- `--disablerepo=<repoid>`
- `--repoid=<repoid>`
- `--releasever=<release>`
- `--refresh`

where the usage is identical to that of DNF.

For the exact definition of `package-file-spec`, refer to the DNF
documentation.

The second part contains the repository configurations in `yum.repos.d` format.

### Output

`qubes.TemplateSearch` prints each package in
`%{name}|%{epoch}|%{version}|%{release}|%{reponame}|%{downloadsize}|%{buildtime}|%{license}|%{url}|%{summary}|%{description}|`
format to standard output, separated by newlines. Note that there is a `|` at
the end of the line. This is because `%{description}` may contain newlines, and
doing so allows us to split the entries by `|\n`. (As we are using `dnf
repoquery --qf`, we are unable to escape the newlines in advance.)

`qubes.TemplateDownload`, on the other hand, directly outputs the downloaded
content to standard output.

## Machine-readable output

The commands `qvm-template list` and `qvm-template info` provide
machine-readable output in both pipe(`|`)-separated and JSON format. See the
`qvm-template` man page for details.

## Interactions with existing tools

### `qvm-remove`

The existing `qvm-remove` tool should behave identically to `qvm-template
remove` -- albeit without fancy features like disassociation. This is unlike
the previous situation where `qvm-remove` cannot remove RPM-installed
templates.

Notably, the metadata needs no special handling as it is stored in VM features
and thus automatically consistent.

### Renaming and cloning

A template is treated as non-manager-installed once renamed or cloned. However,
relevant metadata in the VM features is still retained for future extension and
to serve as a hint for the user.

## Further reading

Initial Google Summer of Code (2020) project proposal:

- <https://hackmd.io/aYauztkGR0iOIoh8fJLecw>

Previous design document:

- <https://gist.github.com/WillyPillow/b8a643ddbd9235a97bc187e6e44b16e4>

Discussion threads:

- <https://groups.google.com/forum/#!topic/qubes-devel/6Zb_WLy3GY4>
- <https://groups.google.com/forum/#!topic/qubes-devel/PyJogqT1TUg>
- <https://groups.google.com/forum/#!topic/qubes-devel/2XaMP4Us3kg>
- <https://groups.google.com/forum/#!topic/qubes-devel/wF_84b1BR0A>
- <https://groups.google.com/forum/#!topic/qubes-devel/pYHnihVCBM0>
