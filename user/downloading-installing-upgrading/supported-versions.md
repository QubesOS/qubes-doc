---
layout: doc
title: Supported Versions
permalink: /doc/supported-versions/
---

Supported Versions
==================

Qubes OS
--------
Qubes OS releases are supported for **six months** after each subsequent major
or minor release (see [Version Scheme]). The current release and past major
releases are always available on the [Downloads] page, while all ISOs, including
past minor releases, are available from our [download mirrors].

| Qubes OS      | Start Date | End Date   | Status                  |
| ------------- | ---------- | ---------- | ----------------------- |
| Release 1     | 2012-09-03 | 2015-03-26 | Old, unsupported        |
| Release 2     | 2014-09-26 | 2016-04-01 | Old, unsupported        |
| Release 3.0   | 2015-10-01 | 2016-09-09 | Old, unsupported        |
| Release 3.1   | 2016-03-09 | 2017-03-29 | Old, unsupported        |
| Release 3.2   | 2016-09-29 | 2019-03-28 | Old, unsupported        |
| Release 4.0   | 2018-03-28 | TBA        | Current, supported      |
| Release 4.1   | TBA        | TBA        | [In development][4.1]   |

### Note on point releases ###

Please note that point releases, such as 3.2.1 and 4.0.1, do not designate
separate, new versions of Qubes OS. Rather, they designate their respective
major or minor releases, such as 4.0 and 3.2, inclusive of all package updates
up to a certain point. For example, installing Release 4.0 and fully updating it
results in the same system as installing Release 4.0.1. Therefore, point
releases are not displayed as separate rows on any of the tables on this page.

Dom0
----
The table below shows the OS used for dom0 in each Qubes OS release.

| Qubes OS      | Dom0 OS   |
| ------------- | --------- |
| Release 1     | Fedora 13 |
| Release 2     | Fedora 18 |
| Release 3.0   | Fedora 20 |
| Release 3.1   | Fedora 20 |
| Release 3.2   | Fedora 23 |
| Release 4.0   | Fedora 25 |

### Note on dom0 and EOL ###

Dom0 is isolated from domUs. DomUs can access only a few interfaces,
such as Xen, device backends (in the dom0 kernel and in other VMs, such as the
NetVM), and Qubes tools (gui-daemon, qrexec-daemon, etc.). These components are
[security-critical], and we provide updates for all of them (when necessary),
regardless of the support status of the base distribution. For this reason, we
consider it safe to continue using a given base distribution in dom0 even after
it has reached EOL (end-of-life).


TemplateVMs
-----------
The table below shows the [TemplateVM] versions supported by each Qubes OS
release. Currently, only Fedora, Debian, and Whonix TemplateVMs are officially supported.

| Qubes OS      | Fedora                       | Debian                                        | Whonix |
| ------------- | ---------------------------- | --------------------------------------------- | ------ |
| Release 1     | 18, 20                       | None                                          | None   |
| Release 2     | 21                           | None                                          | None   |
| Release 3.0   | 21, 22\*, 23                 | 7 ("wheezy")\*, 8 ("jessie")                  | None   |
| Release 3.1   | 21, 22\*, 23                 | 7 ("wheezy")\*, 8 ("jessie"), 9 ("stretch")\* | None   |
| Release 3.2   | 23\*, 24\*, 25\*, 26, 27, 28 | 8 ("jessie"), 9 ("stretch")                   | 13, 14 |
| Release 4.0   | 26, 27, 28, 29, 30           | 8 ("jessie"), 9 ("stretch")                   | 13, 14 |

\* Denotes versions for which we have published the packages but have not done
extensive testing.


Whonix
------

[Whonix] is an advanced feature in Qubes OS.
Those who wish to use it must stay reasonably close to the cutting edge by upgrading to new stable versions of Qubes OS and Whonix TemplateVMs within a month of their respective releases.
To be precise:

 * One month after a new stable version of Qubes OS is released, Whonix TemplateVMs will no longer be supported on any older version of Qubes OS.
   This means that users who wish to continue using Whonix TemplateVMs on Qubes must always upgrade to the latest stable Qubes OS version within one month of its release.

 * One month after new stable versions of Whonix TemplateVMs are released, older versions of Whonix TemplateVMs will no longer be supported.
   This means that users who wish to continue using Whonix TemplateVMs on Qubes must always upgrade to the latest stable Whonix TemplateVM versions within one month of their release.

We aim to announce both types of events one month in advance in order to remind users to upgrade.


[Version Scheme]: /doc/version-scheme/
[Downloads]: /downloads/
[download mirrors]: /downloads/#mirrors
[security-critical]: /doc/security-critical-code/
[TemplateVM]: /doc/templates/
[extended support]: /news/2018/03/28/qubes-40/#the-past-and-the-future
[4.1]: https://github.com/QubesOS/qubes-issues/issues?utf8=%E2%9C%93&q=is%3Aissue+milestone%3A%22Release+4.1%22+
[Whonix]: /doc/whonix/

