---
layout: doc
title: VersionScheme
permalink: /doc/VersionScheme/
redirect_from: /wiki/VersionScheme/
---

Version Scheme
==============

Beginning with R3 release, we change (and formalise) the versioning scheme. From now on, it will be as follows.

Qubes distributions and products
--------------------------------

We intend to make it easy to make a remix of qubes, targetting another hypervisor or isolation provider. We may also create commercial products intended for specific circumstances. There is one distinguished distribution called **Qubes OS**. All source code for it is available for download under GPL licence and is openly developed on the mailing lists. The rest of this document discusses Qubes OS. Another remix may have its own version series.

Release version
---------------

Qubes OS as a whole is released from time to time. Version scheme for all releases is modelled after Linux kernel version numbers. When announcing new release, we decide on the major.minor version (like `3.0`) and release `3.0-rc1`. When we feel that enough progress has been made, we put `3.0-rc2` and so on. All these versions are considered unstable and not ready for production. You may ask for support on mailing lists (specifically **qubes-devel**), but it is not guaranteed (you may for example get answer „update to newer `-rc`”). Public ISO image may or may not be available.

When enough development has been made, we announce the first stable version, like e.g. `3.0.0` (i.e. without `-rc`). This version is considered stable and we support it for some period. Core components are branched at this moment and bugfixes are backported from master branch. Questions about stable release should be directed to the **qubes-users** mailing list. No major features and interface incompatibilities are to be included in this release. We release bugfixes as `3.0.1`, `3.0.2` and so on, while new features come into the next release e.g. `3.1-rcX`.

Tickets in the tracker are sorted out by release major.minor, such as `3.0`, `3.1` (trac calls this „milestone”).

Component version
-----------------

Qubes release is defined as specific versions of components, which are developed more or less separately. Their versions are composed of major and minor version of target Qubes OS release followed by third component which is just incremented. There is no apparent indication that given version is stable or not.

There are some non-essential components like `qubes-apps-*` that are shared between releases. Their versions indicate oldest qubes-release that is supported. We try hard to support multiple releases by one branch to ease code maintenance.

Different Qubes releases remixes may comprise of different components and version are not guaranteed to be monotonic between releases. We may decide that for newer release some component should be downgraded. There is no guarantee that arbitrary combination of different versions of random components will yield usable (or even install-able) compilation.

Git tags and branches
---------------------

We mark each component version in the repository by tag containing `v<version>`. Likewise, each Qubes OS release is marked by `R<release>` tag.

At the release of some release we create branches named like `release2`. Only bugfixes and compatible improvements are backported to these branches. These branches should compile. All new development is done in `master` branch. This branch is totally unsupported and may not even compile depending on maintainer of repository.

All version and release tags should be made and signed by someone from ITL staff. Public keys are included in `qubes-builder` and available at [http://keys.qubes-os.org/keys/](http://keys.qubes-os.org/keys/).
