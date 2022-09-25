---
lang: en
layout: doc
permalink: /doc/version-scheme/
redirect_from:
- /en/doc/version-scheme/
- /doc/VersionScheme/
- /wiki/VersionScheme/
ref: 151
title: Version scheme
---

The Qubes OS Project uses the [semantic versioning](https://semver.org/)
standard. Version numbers are written as `<major>.<minor>.<patch>`. When
`<patch>` is omitted (e.g., `4.1`), it is usually either because `<patch>` is
zero (as in `4.1.0`) or because we are referring to a specific minor release
irrespective of any particular patch release within it. Similarly, the major
release number alone (e.g., `R4`) is sometimes used to refer to an entire
release series inclusive of all minor and patch releases within it.

In general, patch releases are for backward-compatible bug fixes, minor
releases are for backward-compatible enhancements and new features, and major
release are for any backward-incompatible changes. This means that, in general,
one should *not* try to introduce features or enhancements in patch releases or
any backward-incompatible changes in patch or minor releases. (Templates are a
notable exception, as upstream OSes almost always have their own release
schedules.) Bug fixes are allowed in all releases, and backward-compatible
changes are allowed in all major and minor releases.

Following standard practice, **version** refers to any build that has been
assigned a version name or number, e.g., `3.2-rc2`, `4.0.4`, `4.1-beta1`. By
contrast, **release** refers to any version that is intended for consumption by
the general userbase. For example, `4.0.4` was both a **version** and a
**release**, since it was stable and intended for general public use, while
`4.1-beta1` was a **version** but *not* a **release**, since it was not stable
and was intended only for [testing](/doc/testing/). All releases are
versions, but not all versions are releases.

The letter **R**, as in `R4.1`, stands for **release**. The abbreviation **RC**,
as in `3.2-rc2`, stands for **release candidate**.

## Qubes distributions and products

We intend to make it easy to make a remix of Qubes, targeting another
hypervisor or isolation provider. We may also create commercial products
intended for specific circumstances. There is one distinguished distribution
called **Qubes OS**. All source code for it is available for download under a
[free and open-source license](/doc/license/) and is openly developed on
[GitHub](https://github.com/QubesOS) and our [mailing lists](https://www.qubes-os.org/support/). The rest of this document discusses
Qubes OS. Another remix may have its own version series.

## Release versioning

Qubes OS as a whole is released from time to time. When preparing a new
release, we decide on the `<major>.<minor>` numbers (e.g., `3.0`). We then
publish the first release candidate, `3.0-rc1`. When we feel that enough
progress has been made, we'll release `3.0-rc2` and so on. All these versions
(not yet releases) are considered unstable and not for production use. You are
welcome to [help us test](/doc/testing/) these versions.

When enough progress has been made, we announce the first stable release, e.g.
`3.0.0`. This not only a version but an actual release. It is considered stable
and we commit to supporting it according to our [support schedule](/doc/supported-releases/). Core components are branched at this
moment and bug fixes are backported from the master branch. Please see [help, support, mailing lists, and forum](/support/) for places to ask questions about
stable releases. No major features and interface incompatibilities are to be
included in this release. We release bug fixes as patch releases (`3.0.1`,
`3.0.2`, and so on), while backward-compatible enhancements and new features
are introduced in the next minor release (e.g., `3.1`). Any
backward-incompatible changes are introduced in the next major release (e.g.,
`4.0`).

Issues in our [issue tracker](/doc/issue-tracking/) are sorted by release
[milestones](/doc/issue-tracking/#milestones).

## Release schedule

There is no specific schedule for releases other that more general roadmap.
When time comes, Supreme Committee declares feature freeze and tags `-rc1` and
releases ISO image. From this time on, no new features are accepted. Also a
strict time schedule kicks in.

Each release candidate period is as follows. For the first two weeks we accept
and assign bug reports to be fixed before next release candidate. For the next
two weeks we generally focus on fixing assigned bug reports, so issues
discovered during this time may be postponed until later RC. Finally after that
there is one week of current-testing freeze, during which time no new packages
are released, in hope that they will be installed by wider user base and
tested.

The next RC is released five weeks after the former. All packets are published
in `current` repository and the cycle starts over. There should be no less than
1 and no more than 3 release candidates before final release.

| Stage                    | Duration  |
| ------------------------ | --------- |
| initial testing          | two weeks |
| bug fixing               | two weeks |
| `current-testing` freeze | one week  |

Starting with second cycle (that is, after `-rc1`) two weeks into the cycle
(after primary bug-reporting period) the Supreme Committee decides whether
there should be another RC. If, based on remaining issues, the Committee
decides to release final, then the Committee agrees upon the release date,
which should be no later than a week after.

[![Release cycle](/attachment/doc/release-cycle.svg)](/attachment/doc/release-cycle.svg)

## Bug priorities

When deciding whether the current release candidate is the final one, the
Committee takes bug [priorities](/doc/issue-tracking/#priority) into
consideration. The meaning of them is as follows:

- `blocker` --- when any such bug is present in the current release candidate,
  it can't be considered final release. Bugs with this priority must be fixed
  before the next release candidate, even if that means delaying its release
  (which should be considered only last resort option).

- `critical` --- when any such bug is present in the current release candidate,
  it can't be considered final release. But such bugs are not qualified to
  delay next release candidate release.

- `major` --- existence of such bugs do not strictly prevent the current
  release candidate be considered final (but of course we should try hard to
  not have them there). Fixing bugs of this priority can be delayed and
  qualified as updates to the final stable release.

- `default` and `minor` --- existence of such bugs do not prevent the current
  release candidate be considered final. Fixing such bugs can be delayed to the
  next Qubes OS release. Eventually such fixes might be backported as an update
  to the stable release(s). (`default` should really be assigned a more
  specific priority, but in practice there are too many issues and not enough
  time, so `default` ends up staying on many issues.)

All above is about bugs, no features should be assigned to the current release
after first `-rc`. Supreme Committee is free to adjust priorities
appropriately.

## Component version

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

## Git tags and branches

We mark each component version in the repository by tag containing
`v<version>`. Likewise, each Qubes OS release is marked by `R<release>` tag.

At the release of some release we create branches named like `release2`. Only
bug fixes and compatible improvements are backported to these branches. These
branches should compile. All new development is done in `master` branch. This
branch is totally unsupported and may not even compile depending on maintainer
of repository.

All version and release tags should be made and signed by someone from ITL
staff. Public keys are included in `qubes-builder` and available at
<https://keys.qubes-os.org/keys/>.

## Check installed version

If you want to know which version you are running, for example to report an
issue, you can either check in the Qubes Manager menu under `About > Qubes OS`
or in the file `/etc/qubes-release` in dom0. For the latter you can use a
command like `cat /etc/qubes-release` in a dom0 terminal.
