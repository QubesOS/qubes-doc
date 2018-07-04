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
| Release 3.2   | 2016-09-29 | TBA        | Old, [extended support] |
| Release 3.2.1 | TBA        | 2019-03-28 | In development          |
| Release 4.0   | 2018-03-28 | TBA        | Current, supported      |


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
| Release 3.2.1 | Fedora 23 |
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

| Qubes OS      | Fedora                     | Debian                                        | Whonix |
| ------------- | -------------------------- | --------------------------------------------- | ------ |
| Release 1     | 18, 20                     | None                                          | None   |
| Release 2     | 21                         | None                                          | None   |
| Release 3.0   | 21, 22\*, 23               | 7 ("wheezy")\*, 8 ("jessie")                  | None   |
| Release 3.1   | 21, 22\*, 23               | 7 ("wheezy")\*, 8 ("jessie"), 9 ("stretch")\* | None   |
| Release 3.2   | 23\*, 24\*, 25, 26, 27, 28 | 8 ("jessie"), 9 ("stretch")                   | 13     |
| Release 3.2.1 | 26, 27, 28                 | 8 ("jessie"), 9 ("stretch")                   | 13     |
| Release 4.0   | 26, 27, 28                 | 8 ("jessie"), 9 ("stretch")                   | 13     |

\* Denotes versions for which we have published the packages but have not done
extensive testing.


[Version Scheme]: /doc/version-scheme/
[Downloads]: /downloads/
[download mirrors]: /downloads/#mirrors
[security-critical]: /doc/security-critical-code/
[TemplateVM]: /doc/templates/
[extended support]: /news/2018/03/28/qubes-40/#the-past-and-the-future

