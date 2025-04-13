---
lang: en
layout: doc
permalink: /doc/qubes-builder-v2/
redirect_from:
- /en/doc/qubes-builder-v2/
- /doc/QubesBuilder2/
- /wiki/QubesBuilder2/
ref: 311
title: Qubes builder v2
---

This is a brief introduction of using Qubes Builder v2 to work with Qubes OS
sources. It will walk you through installing and configuring Builder v2 and
using it to fetch and build Qubes OS packages.

For details and customization, use [Qubes OS v2 builder documentation](https://github.com/QubesOS/qubes-builderv2/).

# Overview

In the second generation of Qubes OS builder, container or disposable qube
isolation is used to perform every stage of the build and release process.
From fetching sources to building, everything is executed inside an isolated
*cage* (either a disposable or a container) using an *executor*. For every
command that needs to perform an action on sources, like cloning and
verifying Git repos, rendering a SPEC file, generating SRPM or Debian
source packages, a new cage is used. Only the signing, publishing, and
uploading stages are executed locally outside a cage.


# Setup

This is a simple setup for using a docker executor (a good default choice,
if you don't know which executor to use, use docker).

1. First, decide what qube are you going to use for working with Qubes
   Builder v2. It can be an AppVM or a Standalone qube, with some steps
   different between the two.

2. Then, clone the qubes-builder v2 repository into a location of your
   choice:
    ```shell
    git clone https://github.com/QubesOS/qubes-builderv2
    cd qubes-builderv2/
    ```

3. Installing dependencies

   Dependencies need to be installed for the qube you want to be developing
   using Qubes Builder v2 - either in its template, or in the qube itself,
   if it's a standalone.
    Dependencies are specified in `dependencies-*.
   txt` files in the main builder directory, and you can install them easily
   in the following ways:
   1. for Fedora, use:
    ```shell
    $ sudo dnf install $(cat dependencies-fedora.txt)
    $ test -f /usr/share/qubes/marker-vm && sudo dnf install qubes-gpg-split
   ```
   2. for Debian (note: some Debian packages require Debian version 13 or
      later), use:
    ```shell
    $ sudo apt install $(cat dependencies-debian.txt)
    $ test -f /usr/share/qubes/marker-vm && sudo apt install qubes-gpg-split
   ```

4. If you haven't used docker in the current qube, you need also to set up
   some permissions. In particular, the user has to be added to the `docker`
   group:
    ```shell
   $ sudo usermod -aG docker user
    ```
    Next, **restart the qube**.

5. Finally, you need to generate a docker image:
    ```shell
   $ tools/generate-container-image.sh docker
    ```

   In an AppVM, as `/var/lib/docker` is not persistent by default, you also
   need to use bind-dirs to avoid repeating this step after reboot, adding
   the following to the `/rw/config/qubes-bind-dirs.d/docker.conf` file in
   this qube:

   ```
   binds+=( '/var/lib/docker' )
   ```

# Configuration

To use Qubes OS Builder v2, you need to have a `builder.yml` configuration file.
You can use one of the sample files from the `example-configs/` directory; for a
more readable `builder.yml`, you can also include one of the files from that
directory in your `builder.yml`. An example `builder.yml` is:

```yaml
# include configuration relevant for the current release
include:
- example-configs/qubes-os-r4.2.yml

# which repository to use to fetch sources
use-qubes-repo:
  version: 4.2
  testing: true

# each package built will have local build number appended to package release
# number. It makes it easier to update in testing environment
increment-devel-versions: true

# reduce output
debug: false

# this can be set to true if you do not want sources to be automatically
# fetched from git
skip-git-fetch: false

# executor configuration
executor:
  type: docker
  options:
    image: "qubes-builder-fedora:latest"

```


# Using Builder v2

To fetch sources - in this example, for the `core-admin-client` package, you
can use the following command:

```shell
$ ./qb -c core-admin-client package fetch
```

This will fetch the sources for the listed package and place them in
`artifacts/sources` directory.

To build a package (from sources in the `artifacts/sources` directory), use:

```shell
$ ./qb -c core-admin-client package fetch prep build
```

or, if you want to build for a specific target (`host-fc37` is a `dom0`
using Fedora 37, `vm-fc40` would be a qube using Fedora 40 etc.), use:

```shell
$ ./qb -c core-admin-client -d host-fc37 package fetch prep build
```

If you want to fetch entire Qubes OS sources (caution: some repositories might
have additional requirements; you can disable repositories that are not
needed in the `example-configs/*.yml` file you are using by commenting them
out. In particular, `python-fido2`, `lvm` and `windows`-related repositories
have
special requirements), use the following:

```shell
$ ./qb package fetch
```
