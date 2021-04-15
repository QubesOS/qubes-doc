---
lang: en
layout: doc
permalink: /doc/version-scheme/
redirect_from:
- /en/doc/version-scheme/
- /doc/VersionScheme/
- /wiki/VersionScheme/
ref: 151
title: Version Scheme
---

Version Scheme
==============

Beginning with R3 release, we change (and formalise) the versioning scheme.
From now on, it will be as follows.

Qubes distributions and products
--------------------------------

We intend to make it easy to make a remix of Qubes, targeting another
hypervisor or isolation provider. We may also create commercial products
intended for specific circumstances. There is one distinguished distribution
called **Qubes OS**. All source code for it is available for download under GPL
license and is openly developed on the mailing lists. The rest of this document
discusses Qubes OS. Another remix may have its own version series.

Release version
---------------

Qubes OS as a whole is released from time to time. Version scheme for all
releases is modeled after Linux kernel version numbers. When announcing a new
release, we decide on the major.minor version (like `3.0`) and release
`3.0-rc1`. When we feel that enough progress has been made, we put `3.0-rc2`
and so on. All these versions are considered unstable and not ready for
production. You may ask for support on mailing lists (specifically
**qubes-devel**), but it is not guaranteed (you may for example get answer
“update to newer `-rc`”). Public ISO image may or may not be available.

When enough development has been made, we announce the first stable version,
like e.g. `3.0.0` (i.e. without `-rc`). This version is considered stable and
we support it for some period. Core components are branched at this moment and
bugfixes are backported from master branch. Please see [Help, Support, Mailing
Lists, and Forum](/support/) for places to ask questions about stable releases. No major
features and interface incompatibilities are to be included in this release. We
release bugfixes as `3.0.1`, `3.0.2` and so on, while new features come into the
next release e.g. `3.1-rcX`.

Tickets in the tracker are sorted out by release major.minor, such as `3.0`,
`3.1` (trac calls this “milestone”).

Release schedule
----------------

There is no specific schedule for major and minor other that more general
roadmap. When time comes, Supreme Committee declares feature freeze and tags
`-rc1` and releases ISO image. From this time on, no new features are accepted.
Also a strict time schedule kicks in.

Each release candidate period is as follows. For the first two weeks we accept
and assign bugreports to be fixed before next release candidate. For the next
two weeks we generally focus on fixing assigned bugreports, so issues discovered
during this time may be postponed until later RC. Finally after that there is
one week of current-testing freeze, during which time no new packages are
released, in hope that they will be installed by wider user base and tested.

The next RC is released five weeks after the former. All packets are published
in `current` repository and the cycle starts over. There should be no less than
1 and no more than 3 release candidates before final release.

<table>
    <thead>
        <tr><th>stage</th><th>time</th></tr>
    </thead>
    <tbody>
        <tr><td>initial testing</td><td>2 weeks</td></tr>
        <tr><td>bug fixing</td><td>2 weeks</td></tr>
        <tr><td>`current-testing` freeze</td><td>1 week</td></tr>
    </tbody>
</table>

Starting with second cycle (that is, after `-rc1`) two weeks into the cycle
(after primary bug-reporting period) the Supreme Committee decides whether there
should be another RC. If, based on remaining issues, the Committee decides to
release final, then the Committee agrees upon the release date, which should be
no later than a week after.

!["Release cycle"](/attachment/wiki/VersionScheme/release-cycle.svg)

Bug priorities
--------------

When deciding whether the current release candidate is the final one, the Committee
takes bugs priorities into consideration. The meaning of them is as follows:

* `blocker` - when any such bug is present in the current release candidate, it
can't be considered final release. Bugs with this priority must be fixed before
the next release candidate, even if that means delaying its release (which
should be considered only last resort option).

* `critical` - when any such bug is present in the current release candidate, it
can't be considered final release. But such bugs are not qualified to delay
next release candidate release.

* `major` - existence of such bugs do not strictly prevent the current release
candidate be considered final (but of course we should try hard to not have
them there). Fixing bugs of this priority can be delayed and qualified as
updates to the final stable release.

* `minor` - existence of such bugs do not prevent the current release candidate
be considered final. Fixing such bugs can be delayed to the next Qubes OS
release. Eventually such fixes might be backported as an update to the stable
release(s).

All above is about bugs, no features should be assigned to the current release
after first `-rc`. Supreme Committee is free to adjust priorities appropriately.

Component version
-----------------

Qubes release is defined as specific versions of components, which are
developed more or less separately. Their versions are composed of major and
minor version of target Qubes OS release followed by third component which is
just incremented. There is no apparent indication that given version is stable
or not.

There are some non-essential components like `qubes-apps-*` that are shared
between releases. Their versions indicate oldest qubes-release that is
supported. We try hard to support multiple releases by one branch to ease code
maintenance.

Different Qubes releases remixes may comprise of different components and
version are not guaranteed to be monotonic between releases. We may decide that
for newer release some component should be downgraded. There is no guarantee
that arbitrary combination of different versions of random components will
yield usable (or even install-able) compilation.

Git tags and branches
---------------------

We mark each component version in the repository by tag containing
`v<version>`. Likewise, each Qubes OS release is marked by `R<release>` tag.

At the release of some release we create branches named like `release2`. Only
bugfixes and compatible improvements are backported to these branches. These
branches should compile. All new development is done in `master` branch. This
branch is totally unsupported and may not even compile depending on maintainer
of repository.

All version and release tags should be made and signed by someone from ITL
staff. Public keys are included in `qubes-builder` and available at
[https://keys.qubes-os.org/keys/](https://keys.qubes-os.org/keys/).

Check installed version
-----------------

If you want to know which version you are running, for example to report
an issue, you can either check in the Qubes Manager menu under About / Qubes OS  or in the file /etc/qubes-release in dom0. For the latter you can use a command like `cat /etc/qubes-release` in a dom0 terminal.

