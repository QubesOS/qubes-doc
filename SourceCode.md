---
layout: wiki
title: SourceCode
permalink: /wiki/SourceCode/
---

Qubes Source Code Repositories
==============================

All the Qubes code is kept in GIT repositories. We divided the project into several components, each of which has its own separate repository:

-   `core.git` -- the core Qubes infrastructure responsible for VM management, VM temaplates, fs sharing, etc.
-   `gui.git` -- GUI virtualization, both Dom0 and VM side.
-   `template-builder.git` - scripts and other files used to create Qubes templates and NetVM images.

You can browse the repositories [​on line via GitWeb](http://git.qubes-os.org/gitweb/). The Qubes official repositories are in the `mainstream` directory.

To clone a repository:

``` {.wiki}
git clone git://git.qubes-os.org/mainstream/<repo_name>.git <repo_name>
```

e.g.:

``` {.wiki}
git clone git://qubes-os.org/mainstream/core.git core
```

Currently the preferred way of contributing to the project is by sending a patch via the project's mailing list (`git format-patch`).
