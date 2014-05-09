---
layout: wiki
title: SourceCode
permalink: /wiki/SourceCode/
---

Qubes Source Code Repositories
==============================

All the Qubes code is kept in GIT repositories. We divided the project into several components, each of which has its own separate repository, some of them:

-   `core-admin.git` -- the core Qubes infrastructure responsible for VM management, VM templates, fs sharing, etc.
-   `gui-daemon.git` -- GUI virtualization, Dom0 side.
-   `gui-agent-linux.git` -- GUI virtualization, Linux VM side.
-   `linux-template-builder.git` - scripts and other files used to create Qubes templates images.

You can browse the repositories [​on line via GitWeb](http://git.qubes-os.org/gitweb/). The Qubes official repositories are in the `qubes-rX` directory, where X is release number (1, 2, etc).

To clone a repository:

``` {.wiki}
git clone git://git.qubes-os.org/qubes-r2/<repo_name>.git <repo_name>
```

e.g.:

``` {.wiki}
git clone git://git.qubes-os.org/qubes-r2/core-admin.git core-admin
```

Currently the preferred way of contributing to the project is by [sending a patch](/wiki/DevelFaq#Q:HowdoIsubmitapatch) via the project's mailing list (`git format-patch`).
