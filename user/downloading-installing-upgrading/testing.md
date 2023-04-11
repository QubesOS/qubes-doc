---
advanced: true
lang: en
layout: doc
permalink: /doc/testing/
ref: 147
title: Testing new releases and updates
---

Testing new Qubes OS releases and updates is one of the most helpful ways in
which you can [contribute](/doc/contributing/) to the Qubes OS Project. If
you're interested in helping with this, please [join the testing
team](https://forum.qubes-os.org/t/joining-the-testing-team/5190). There are
several different types of testing, which we'll cover below.

**Warning:** Software testing is intended for advanced users and developers.
You should only attempt to do this if you know what you're doing. Never rely on
code that is in testing for critical work!

## Releases

How to test upcoming Qubes OS releases:

* Use [qubes-builder](/doc/qubes-builder/) to build the latest release.
* Test the latest release candidate (RC), if one is currently available.
* Try the [signed weekly builds](https://qubes.notset.fr/iso/). ([Learn
  more](https://forum.qubes-os.org/t/16929) and [track their
  status](https://github.com/fepitre/updates-status-iso/issues).)
* (No support) Experiment with devel alpha ISOs found from time to time at
  [Qubes OpenQA](https://openqa.qubes-os.org/).

Please make sure to [report any bugs you encounter](/doc/issue-tracking/).

See [Version Scheme](/doc/version-scheme/) for details about release versions
and schedules. See [Release Checklist](/doc/releases/todo/) for details about
the RC process.

## Updates

How to test updates:

* Enable [dom0 testing
  repositories](/doc/how-to-install-software-in-dom0/#testing-repositories).
* Enable [template testing
  repositories](/doc/how-to-install-software/#testing-repositories).

Every new update is first uploaded to the `security-testing` repository if it
is a security update or `current-testing` if it is a normal update. The update
remains in `security-testing` or `current-testing` for a minimum of one week.
On occasion, an exception is made for a particularly critical security update,
which is immediately pushed to the `current` stable repository. In general,
however, security updates remain in `security-testing` for two weeks before
migrating to `current`. Normal updates generally remain in `current-testing`
until they have been sufficiently tested by the community, which can last weeks
or even months, depending on the amount of feedback received (see [Providing
feedback](#providing-feedback)).

"Sufficient testing" is, in practice, a fluid term that is up the developers'
judgment. In general, it means either that no negative feedback and at least
one piece of positive feedback has been received or that the package has been
in `current-testing` for long enough, depending on the component and the
complexity of the changes.

A limitation of the current testing setup is that it is only possible to
migrate the *most recent version* of a package from `current-testing` to
`current`. This means that, if a newer version of a package is uploaded to
`current-testing`, it will no longer be possible to migrate any older versions
of that same package from `current-testing` to `current`, even if one of those
older versions has been deemed stable enough. While this limitation can be
inconvenient, the benefits outweigh the costs, since it greatly simplifies the
testing and reporting process.

## Templates

How to test [templates](/doc/templates/):

* For official templates, enable the `qubes-templates-itl-testing` repository,
  then [install](/doc/templates/#installing) the desired template.
* For community templates, enable the `qubes-templates-community-testing`
  repository, then [install](/doc/templates/#installing) the desired template.

To temporarily enable any of these repos, use the `--enablerepo=<repo-name>`
option. Example commands:

```
sudo qubes-dom0-update --enablerepo=qubes-templates-itl-testing
sudo qubes-dom0-update --enablerepo=qubes-templates-community-testing
```

To enable or disable any of these repos permanently, change the corresponding
`enabled` value to `1` in `/etc/yum.repos.d/qubes-templates.repo`.

## Providing feedback

Since the whole point of testing software is to discover and fix bugs, your
feedback is an essential part of this process.

We use an [automated build
process](https://github.com/QubesOS/qubes-infrastructure/blob/master/README.md).
For every package that is uploaded to a testing repository, a GitHub issue is
created in the
[updates-status](https://github.com/QubesOS/updates-status/issues) repository
for tracking purposes. We welcome any kind of feedback on any package in any
testing repository. Even a simple <span class="fa fa-thumbs-up" title="Thumbs
Up"></span> or <span class="fa fa-thumbs-down" title="Thumbs Down"></span> on
the package's associated issue would help us to decide whether the package is
ready to be migrated to a stable repository. If you [report a
bug](/doc/issue-tracking/) in a package that is in a testing repository, please
reference the appropriate issue in
[updates-status](https://github.com/QubesOS/updates-status/issues).
