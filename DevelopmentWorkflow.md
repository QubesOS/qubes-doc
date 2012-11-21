---
layout: wiki
title: DevelopmentWorkflow
permalink: /wiki/DevelopmentWorkflow/
---

Development Workflow
====================

A workflow for developing Qubes OS+

First things first, setup [QubesBuilder](/wiki/QubesBuilder). This guide assumes you're using qubes-builder to build Qubes.

Repositories and Committing Code
--------------------------------

Qubes is split into a bunch of git repos. This are all contained in the `qubes-src` directory under qubes-builder.

The best way to write and contribute code is to create a git repo somewhere (e.g., github) for the repo you are interested in editing (e.g., `qubes-manager`, `core`, etc). To integrate your repo with the rest of Qubes, cd to the repo directory and add your repository as a remote in git

**Example:**

``` {.wiki}
$ cd qubes-builder/qubes-src/qubes-manager
$ git remote add abel git@github.com:abeluck/qubes-manager.git
```

You can then proceed to easily develop in your own branches, pull in new commits from the dev branches, merge them, and eventually push to your own repo on github.

When you are ready to submit your changes to Qubes to be merged, push your changes, then create a signed git tag (using `git tag -s`). Finally, send a letter to the Qubes listserv describing the changes and including the link to your repository. Don't forget to include your public PGP key you use to sign your tags.

### Useful [QubesBuilder](/wiki/QubesBuilder) commands

1.  *make check* - will check if all the code was commited into repository and if all repository are tagged with signed tag.
2.  *make show-vtags* - show version of each component (based on git tags) - mostly useful just before building ISO. **Note:** this will not show version for components containing changes since last version tag
3.  *make push* - push change from **all** repositories to git server. You must set proper remotes (see above) for all repositories first.
4.  *make prepare-merge* - fetch changes from remote repositories (can be specified on commandline via GIT\_SUBDIR or GIT\_REMOTE vars), (optionally) verify tags and show the changes. This do not merge the changes - there are left for review as FETCH\_HEAD ref. You can merge them using "git merge FETCH\_HEAD" (in each repo directory).

Copying Code to dom0
--------------------

When developing it is convenient to be able to rapidly test changes. Assuming you're developing Qubes on Qubes, you should be working in a special VM for Qubes and occasionally you will want to transfer code or rpms back to dom0 for testing.

Here are some handy scripts Marek has shared to facilitate this.

### Syncing dom0 files

TODO: edit this script to be more generic

``` {.wiki}
#!/bin/sh

set -x
set -e

QUBES_PY_DIR=/usr/lib64/python2.6/site-packages/qubes
QUBES_PY=$QUBES_PY_DIR/qubes.py
QUBESUTILS_PY=$QUBES_PY_DIR/qubesutils.py

qvm-run -p qubes-devel 'cd qubes-builder/qubes-src/core/dom0; tar c qmemman/qmemman*.py qvm-core/*.py qvm-tools/* misc/vm-template-hvm.conf misc/qubes-start.desktop ../misc/block-snapshot aux-tools ../qrexec' |tar xv
cp $QUBES_PY qubes.py.bak$$
cp $QUBESUTILS_PY qubesutils.py.bak$$
cp /etc/xen/scripts/block-snapshot block-snapshot.bak$$
sudo cp qvm-core/qubes.py $QUBES_PY
sudo cp qvm-core/qubesutils.py $QUBESUTILS_PY
sudo cp qvm-core/guihelpers.py $QUBES_PY_DIR/
sudo cp qmemman/qmemman*.py $QUBES_PY_DIR/
sudo cp misc/vm-template-hvm.conf /usr/share/qubes/
sudo cp misc/qubes-start.desktop /usr/share/qubes/
sudo cp misc/block-snapshot /etc/xen/scripts/
sudo cp aux-tools/qubes-dom0-updates.cron /etc/cron.daily/I hope to 
```

### Apply qvm-tools

TODO: make it more generic

``` {.wiki}
#!/bin/sh

BAK=qvm-tools.bak$$
mkdir -p $BAK
cp -a /usr/bin/qvm-* /usr/bin/qubes-* $BAK/
sudo cp qvm-tools/qvm-* qvm-tools/qubes-* /usr/bin/
```

### Copy from dom0 to an appvm

``` {.wiki}
#/bin/sh
#
# usage ./cp-domain <vm_name> <file_to_copy>
#
domain=$1
file=$2
fname=`basename $file`

qvm-run $domain 'mkdir /home/user/incoming/dom0 -p'
cat $file| qvm-run --pass-io $domain "cat > /home/user/incoming/dom0/$fname"
```
