---
lang: en
layout: doc
permalink: /doc/supported-versions/
ref: 154
title: Supported Versions
---

This page details the level and period of support for versions of operating
systems in the Qubes ecosystem.

## Qubes OS

Qubes OS releases are supported for **six months** after each subsequent major
or minor release (see [Version Scheme](/doc/version-scheme/)). The current
release and past major releases are always available on the
[Downloads](/downloads/) page, while all ISOs, including past minor releases,
are available from our [download mirrors](/downloads/#mirrors).

| Qubes OS    | Start Date | End Date   | Status                |
| ----------- | ---------- | ---------- | --------------------- |
| Release 1   | 2012-09-03 | 2015-03-26 | Unsupported           |
| Release 2   | 2014-09-26 | 2016-04-01 | Unsupported           |
| Release 3.0 | 2015-10-01 | 2016-09-09 | Unsupported           |
| Release 3.1 | 2016-03-09 | 2017-03-29 | Unsupported           |
| Release 3.2 | 2016-09-29 | 2019-03-28 | Unsupported           |
| Release 4.0 | 2018-03-28 | TBA        | Supported             |
| Release 4.1 | TBA        | TBA        | [In development](https://github.com/QubesOS/qubes-issues/issues?utf8=%E2%9C%93&q=is%3Aissue+milestone%3A%22Release+4.1%22+) |

### Note on point releases

Please note that point releases, such as 3.2.1 and 4.0.1, do not designate
separate, new versions of Qubes OS. Rather, they designate their respective
major or minor releases, such as 3.2 and 4.0, inclusive of all package updates
up to a certain point. For example, installing Release 4.0 and fully updating
it results in the same system as installing Release 4.0.1. Therefore, point
releases are not displayed as separate rows on any of the tables on this page.

## Dom0

The table below shows the OS used for dom0 in each Qubes OS release.

| Qubes OS    | Dom0 OS   |
| ----------- | --------- |
| Release 1   | Fedora 13 |
| Release 2   | Fedora 18 |
| Release 3.0 | Fedora 20 |
| Release 3.1 | Fedora 20 |
| Release 3.2 | Fedora 23 |
| Release 4.0 | Fedora 25 |
| Release 4.1 | Fedora 32 |

### Note on dom0 and EOL

Dom0 is isolated from domUs. DomUs can access only a few interfaces, such as
Xen, device backends (in the dom0 kernel and in other VMs, such as the NetVM),
and Qubes tools (gui-daemon, qrexec-daemon, etc.). These components are
[security-critical](/doc/security-critical-code/), and we provide updates for
all of them (when necessary), regardless of the support status of the base
distribution. For this reason, we consider it safe to continue using a given
base distribution in dom0 even after it has reached end-of-life (EOL).

## Templates

The following table shows select [template](/doc/templates/) versions that are
currently supported. Currently, only [Fedora](/doc/templates/fedora/) and
[Debian](/doc/templates/debian/) templates are officially supported by the
Qubes OS Project. [Whonix](https://www.whonix.org/wiki/Qubes) templates are
supported by our partner, the [Whonix Project](https://www.whonix.org/). Qubes
support for each template ends when that upstream release reaches end-of-life
(EOL). Please see below for distribution-specific notes.

It is the responsibility of each distribution to clearly notify its users in
advance of its own EOL dates, and it is users' responsibility to heed these
notices by upgrading to supported releases. As a courtesy to Qubes users, we
attempt to pass along any upstream EOL notices we receive for
officially-supported templates, but our ability to do this reliably is
dependent on the upstream distribution's practices. If a distribution provides
a mailing list similar to [qubes-announce](/support/#qubes-announce), which
allows us to receive only very important, infrequent messages, including EOL
announcements, we are much more likely to be able to pass along EOL notices to
Qubes users reliably. Qubes users can always check the EOL status of an
upstream release on the upstream distribution's website (see [Fedora
EOL](https://fedoraproject.org/wiki/End_of_life) and [Debian
Releases](https://wiki.debian.org/DebianReleases)).

| Qubes OS    | Fedora | Debian                                   | Whonix |
| ----------- | ------ | ---------------------------------------- | ------ |
| Release 4.0 | 33     | 9 ("stretch"),<sup>*</sup> 10 ("buster") | 15     |
| Release 4.1 | 33     | 10 ("buster")                            | 15     |

<sup>\*</sup> Although Debian 9 has reached regular EOL and is now in
[LTS](https://wiki.debian.org/LTS), we continue to support it for Qubes R4.0.
This is a *temporary* exception to our [policy](#note-on-debian-support) of
ending Qubes support at each Debian release's *regular* (not LTS) EOL date,
since this policy was introduced after the release of Qubes R4.0. In Qubes R4.1
and beyond, Qubes support for each Debian release will end when that release
reaches regular EOL and will not extend into LTS.

### Note on Debian support

Debian releases have two EOL dates: regular and [long-term support
(LTS)](https://wiki.debian.org/LTS). See [Debian Production
Releases](https://wiki.debian.org/DebianReleases#Production_Releases) for a
chart that illustrates this. Qubes support ends at the *regular* EOL date,
*not* the LTS EOL date, unless a specific exception has been made.

### Note on Whonix support

[Whonix](https://www.whonix.org/wiki/Qubes) templates are supported by our
partner, the [Whonix Project](https://www.whonix.org/). The Whonix Project has
set its own support policy for Whonix templates in Qubes.

This policy requires Whonix template users to stay reasonably close to the
cutting edge by upgrading to new stable versions of Qubes OS and Whonix
templates within a month of their respective releases. To be precise:

* One month after a new stable version of Qubes OS is released, Whonix
  templates will no longer be supported on any older version of Qubes OS. This
  means that users who wish to continue using Whonix templates on Qubes must
  always upgrade to the latest stable Qubes OS version within one month of its
  release.

* One month after new stable versions of Whonix templates are released, older
  versions of Whonix templates will no longer be supported. This means that
  users who wish to continue using Whonix templates on Qubes must always
  upgrade to the latest stable Whonix template versions within one month of
  their release.

We aim to announce both types of events one month in advance in order to remind
users to upgrade.
