---
lang: en
layout: doc
permalink: /doc/development-workflow/
redirect_from:
- /en/doc/development-workflow/
- /doc/DevelopmentWorkflow/
- /wiki/DevelopmentWorkflow/
ref: 66
title: Development workflow
---

A workflow for developing Qubes OS+

First things first, setup [QubesBuilder](/doc/qubes-builder/). This guide
assumes you're using qubes-builder to build Qubes.

## Repositories and committing Code

Qubes is split into a bunch of git repos. These are all contained in the
`qubes-src` directory under qubes-builder. Subdirectories there are separate
components, stored in separate git repositories.

The best way to write and contribute code is to create a git repo somewhere
(e.g., github) for the repo you are interested in editing (e.g.,
`qubes-manager`, `core-agent-linux`, etc). To integrate your repo with the rest
of Qubes, cd to the repo directory and add your repository as a remote in git

**Example:**

~~~
$ cd qubes-builder/qubes-src/qubes-manager
$ git remote add abel git@github.com:abeluck/qubes-manager.git
~~~

You can then proceed to easily develop in your own branches, pull in new
commits from the dev branches, merge them, and eventually push to your own repo
on github.

When you are ready to submit your changes to Qubes to be merged, push your
changes, then create a signed git tag (using `git tag -s`). Finally, send a
letter to the Qubes the [qubes-devel](/support/#qubes-devel) mailing list
describing the changes and including the link to
your repository. You can also create pull request on github. Don't forget to
include your public PGP key you use to sign your tags.

### Kernel-specific notes

#### Prepare fresh version of kernel sources, with Qubes-specific patches applied

In qubes-builder/qubes-src/linux-kernel:

~~~
make prep
~~~

The resulting tree will be in kernel-\<VERSION\>/linux-\<VERSION\>:

~~~
ls -ltrd kernel*/linux*
~~~

~~~
drwxr-xr-x 23 user user 4096 Nov  5 09:50 kernel-3.4.18/linux-3.4.18
drwxr-xr-x  6 user user 4096 Nov 21 20:48 kernel-3.4.18/linux-obj
~~~

#### Go to the kernel tree and update the version

In qubes-builder/qubes-src/linux-kernel:

~~~
cd kernel-3.4.18/linux-3.4.18
~~~

#### Changing the config

In kernel-3.4.18/linux-3.4.18:

~~~
cp ../../config .config
make oldconfig
~~~

Now change the configuration. For example, in kernel-3.4.18/linux-3.4.18:

~~~
make menuconfig
~~~

Copy the modified config back into the kernel tree:

~~~
cp .config ../../../config
~~~

#### Patching the code

TODO: describe the workflow for patching the code, below are some random notes, not working well

~~~
ln -s ../../patches.xen
export QUILT_PATCHES=patches.xen
export QUILT_REFRESH_ARGS="-p ab --no-timestamps --no-index"
export QUILT_SERIES=../../series-pvops.conf

quilt new patches.xen/pvops-3.4-0101-usb-xen-pvusb-driver-bugfix.patch
quilt add drivers/usb/host/Kconfig drivers/usb/host/Makefile \
        drivers/usb/host/xen-usbback/* drivers/usb/host/xen-usbfront.c \
        include/xen/interface/io/usbif.h

*edit something*

quilt refresh
cd ../..
vi series.conf
~~~

#### Building RPMs

TODO: Is this step generic for all subsystems?

Now it is a good moment to make sure you have changed kernel release name in
rel file. For example, if you change it to '1debug201211116c' the
resulting RPMs will be named
'kernel-3.4.18-1debug20121116c.pvops.qubes.x86\_64.rpm'. This will help
distinguish between different versions of the same package.

You might want to take a moment here to review (git diff, git status), commit
your changes locally.

To actually build RPMs, in qubes-builder:

~~~
make linux-kernel
~~~

RPMs will appear in qubes-src/linux-kernel/pkgs/fc20/x86\_64:

~~~
-rw-rw-r-- 1 user user 42996126 Nov 17 04:08 kernel-3.4.18-1debug20121116c.pvops.qubes.x86_64.rpm
-rw-rw-r-- 1 user user 43001450 Nov 17 05:36 kernel-3.4.18-1debug20121117a.pvops.qubes.x86_64.rpm
-rw-rw-r-- 1 user user  8940138 Nov 17 04:08 kernel-devel-3.4.18-1debug20121116c.pvops.qubes.x86_64.rpm
-rw-rw-r-- 1 user user  8937818 Nov 17 05:36 kernel-devel-3.4.18-1debug20121117a.pvops.qubes.x86_64.rpm
-rw-rw-r-- 1 user user 54490741 Nov 17 04:08 kernel-qubes-vm-3.4.18-1debug20121116c.pvops.qubes.x86_64.rpm
-rw-rw-r-- 1 user user 54502117 Nov 17 05:37 kernel-qubes-vm-3.4.18-1debug20121117a.pvops.qubes.x86_64.rpm
~~~

### Useful [QubesBuilder](/doc/qubes-builder/) commands

1. `make check` - will check if all the code was committed into repository and
if all repository are tagged with signed tag.
2. `make show-vtags` - show version of each component (based on git tags) -
mostly useful just before building ISO. **Note:** this will not show version
for components containing changes since last version tag.
3. `make push` - push change from **all** repositories to git server. You must
set proper remotes (see above) for all repositories first.
4. `make prepare-merge` - fetch changes from remote repositories (can be
specified on commandline via GIT\_SUBDIR or GIT\_REMOTE vars), (optionally)
verify tags and show the changes. This do not merge the changes - there are
left for review as FETCH\_HEAD ref. You can merge them using `git merge
FETCH_HEAD` (in each repo directory). Or `make do-merge` to merge all of them.

## Copying Code to dom0

When developing it is convenient to be able to rapidly test changes. Assuming
you're developing Qubes on Qubes, you should be working in a special VM for
Qubes and occasionally you will want to transfer code or RPMs back to dom0 for
testing.

Here are some handy scripts Marek has shared to facilitate this.

You may also like to run your [test environment on separate
machine](/doc/test-bench/).

### Syncing dom0 files

TODO: edit this script to be more generic

~~~
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
sudo cp aux-tools/qubes-dom0-updates.cron /etc/cron.daily/
# FIXME(Abel Luck): I hope to
~~~

### Apply qvm-tools

TODO: make it more generic

~~~
#!/bin/sh

BAK=qvm-tools.bak$$
mkdir -p $BAK
cp -a /usr/bin/qvm-* /usr/bin/qubes-* $BAK/
sudo cp qvm-tools/qvm-* qvm-tools/qubes-* /usr/bin/
~~~

### Copy from dom0 to an appvm

~~~
#/bin/sh
#
# usage ./cp-domain <vm_name> <file_to_copy>
#
domain=$1
file=$2
fname=`basename $file`

qvm-run $domain 'mkdir /home/user/incoming/dom0 -p'
cat $file| qvm-run --pass-io $domain "cat > /home/user/incoming/dom0/$fname"
~~~

## Git connection between VMs

Sometimes it's useful to transfer git commits between VMs. You can use `git
format-patch` for that and simply copy the files. But you can also setup
custom qrexec service for it.

Below example assumes that you use `builder-RX` directory in target VM to
store sources in qubes-builder layout (where `X` is some number). Make sure that
all the scripts are executable.

Service file (save in `/usr/local/etc/qubes-rpc/local.Git` in target VM):

~~~
#!/bin/sh

exec 2>/tmp/log2

read service rel repo
echo "Params: $service $rel $repo" >&2
# Adjust regexps if needed
echo "$repo" | grep -q '^[A-Za-z0-9-]\+$' || exit 1
echo "$rel" | grep -q '^[0-9.]\+$' || exit 1
path="/home/user/builder-R$rel/qubes-src/$repo"
if [ "$repo" = "builder" ]; then
    path="/home/user/builder-R$rel"
fi
case $service in
    git-receive-pack|git-upload-pack)
        echo "starting $service $path" >&2
        exec $service $path
        ;;
    *)
        echo "Unsupported service: $service" >&2
        ;;
esac
~~~

Client script (save in `~/bin/git-qrexec` in source VM):

~~~
#!/bin/sh

VMNAME=$1

(echo $GIT_EXT_SERVICE $2 $3; exec cat) | qrexec-client-vm $VMNAME local.Git
~~~

You will also need to setup qrexec policy in dom0 (`/etc/qubes-rpc/policy/local.Git`).

Usage:

~~~
[user@source core-agent-linux]$ git remote add testbuilder "ext::git-qrexec testbuilder 3 core-agent-linux"
[user@source core-agent-linux]$ git push testbuilder master
~~~

You can create `~/bin/add-remote` script to ease adding remotes:

~~~
#!/bin/sh

[ -n "$1" ] || exit 1

if [ "$1" = "tb" ]; then
    git remote add $1 "ext::git-qrexec testbuilder 3 `basename $PWD`"
    exit $?
fi

git remote add $1 git@github.com:$1/qubes-`basename $PWD`
~~~

It should be executed from component top level directory. This script takes one
argument - remote name. If it is `tb`, then it creates qrexec-based git remote
to `testbuilder` VM. Otherwise it creates remote pointing at github account of
the same name. In any case it points at repository matching current directory
name.

## Sending packages to different VM

Other useful script(s) can be used to setup local package repository hosted in
some VM. This way you can keep your development VM behind firewall, while
having an option to expose some yum/apt repository to the local network (to
have them installed on test machine).

To achieve this goal, a dummy repository can be created, which instead of
populating metadata locally, will upload the packages to some other VM and
trigger repository update there (using qrexec). You can use `unstable`
repository flavor, because there is no release managing rules bundled (unlike
current and current-testing).

### RPM packages - yum repo

In source VM, grab [linux-yum](https://github.com/QubesOS/qubes-linux-yum) repository (below is assumed you've made it in
`~/repo-yum-upload` directory) and replace `update_repo.sh` script with:

~~~
#!/bin/sh

VMNAME=repo-vm

set -e
qvm-copy-to-vm $VMNAME $1
# remove only files, leave directory structure
find -type f -name '*.rpm' -delete
# trigger repo update
qrexec-client-vm $VMNAME local.UpdateYum
~~~

In target VM, setup actual yum repository (also based on [linux-yum](https://github.com/QubesOS/qubes-linux-yum), this time
without modifications). You will also need to setup some gpg key for signing
packages (it is possible to force yum to install unsigned packages, but it
isn't possible for `qubes-dom0-update` tool). Fill `~/.rpmmacros` with
key description:

~~~
%_gpg_name Test packages signing key
~~~

Then setup `local.UpdateYum` qrexec service (`/usr/local/etc/qubes-rpc/local.UpdateYum`):

~~~
#!/bin/sh

if [ -z "$QREXEC_REMOTE_DOMAIN" ]; then
    exit 1
fi

real_repository=/home/user/linux-yum
incoming=/home/user/QubesIncoming/$QREXEC_REMOTE_DOMAIN

find $incoming -name '*.rpm' |xargs rpm -K |grep -iv pgp |cut -f1 -d: |xargs -r setsid -w rpm --addsign 2>&1

rsync -lr --remove-source-files $incoming/ $real_repository
cd $real_repository
export SKIP_REPO_CHECK=1
if [ -d $incoming/r3.1 ]; then
    ./update_repo-unstable.sh r3.1
fi

if [ -d $incoming/r3.0 ]; then
    ./update_repo-unstable.sh r3.0
fi

if [ -d $incoming/r2 ]; then
    ./update_repo-unstable.sh r2
fi
find $incoming -type d -empty -delete
exit 0
~~~

Of course you will also need to setup qrexec policy in dom0
`/etc/qubes-rpc/policy/local.UpdateYum`.

If you want to access the repository from network, you need to setup HTTP
server serving it, and configure the system to let other machines actually
reach this HTTP server. You can use for example using [port
forwarding](/doc/firewall/#port-forwarding-to-a-qube-from-the-outside-world) or setting up Tor hidden service. Configuration
details of those services are outside of the scope of this page.

Usage: setup `builder.conf` in source VM to use your dummy-uploader repository:

~~~
LINUX_REPO_BASEDIR = ../../repo-yum-upload/r3.1
~~~

Then use `make update-repo-unstable` to upload the packages. You can also
specify selected components on command line, then build them and upload to the
repository:

~~~
make COMPONENTS="core-agent-linux gui-agent-linux linux-utils" qubes update-repo-unstable
~~~

On the test machine, add yum repository (`/etc/yum.repos.d`) pointing at just
configured HTTP server. For example:

~~~
[local-test]
name=Test
baseurl=http://local-test.lan/linux-yum/r$releasever/unstable/dom0/fc20
~~~

Remember to also import gpg public key using `rpm --import`.

### Deb packages - Apt repo

Steps are mostly the same as in the case of yum repo. The only details that differ:

- use [linux-deb](https://github.com/QubesOS/qubes-linux-deb) instead of [linux-yum](https://github.com/QubesOS/qubes-linux-yum) as a base - both in source and target VM
- use different `update_repo.sh` script in source VM (below)
- use `local.UpdateApt` qrexec service in target VM (code below)
- in target VM additionally place `update-local-repo.sh` script in repository dir (code below)

`update_repo.sh` script:

~~~
#!/bin/sh

set -e

current_release=$1
VMNAME=repo-vm

qvm-copy-to-vm $VMNAME $1
find $current_release -type f -name '*.deb' -delete
rm -f $current_release/vm/db/*
qrexec-client-vm $VMNAME local.UpdateApt
~~~

`local.UpdateApt` service code (`/usr/local/etc/qubes-rpc/local.UpdateApt` in repo-serving VM):

~~~
#!/bin/sh

if [ -z "$QREXEC_REMOTE_DOMAIN" ]; then
    exit 1
fi

incoming=/home/user/QubesIncoming/$QREXEC_REMOTE_DOMAIN

rsync -lr --remove-source-files $incoming/ /home/user/linux-deb/
cd /home/user/linux-deb
export SKIP_REPO_CHECK=1
if [ -d $incoming/r3.1 ]; then
    for dist in `ls r3.1/vm/dists`; do
        ./update-local-repo.sh r3.1/vm $dist
    done
fi

if [ -d $incoming/r3.0 ]; then
    for dist in `ls r3.0/vm/dists`; do
        ./update-local-repo.sh r3.0/vm $dist
    done
fi

if [ -d $incoming/r2 ]; then
    for dist in `ls r2/vm/dists`; do
        ./update-local-repo.sh r2/vm $dist
    done
fi
find $incoming -type d -empty -delete
exit 0
~~~

`update-local-repo.sh`:

~~~
#!/bin/sh

set -e

# Set this to your local repository signing key
SIGN_KEY=01ABCDEF

[ -z "$1" ] && { echo "Usage: $0 <repo> <dist>"; exit 1; }

REPO_DIR=$1
DIST=$2

if [ "$DIST" = "wheezy-unstable" ]; then
    DIST_TAG=deb7
elif [ "$DIST" = "jessie-unstable" ]; then
    DIST_TAG=deb8
elif [ "$DIST" = "stretch-unstable" ]; then
    DIST_TAG=deb9
fi

pushd $REPO_DIR
mkdir -p dists/$DIST/main/binary-amd64
dpkg-scanpackages --multiversion --arch "*$DIST_TAG*" . > dists/$DIST/main/binary-amd64/Packages
gzip -9c dists/$DIST/main/binary-amd64/Packages > dists/$DIST/main/binary-amd64/Packages.gz
cat > dists/$DIST/Release <<EOF
Label: Test repo
Suite: $DIST
Codename: $DIST
Date: `date -R`
Architectures: amd64
Components: main
SHA1:
EOF
function calc_sha1() {
    f=dists/$DIST/$1
    echo -n " "
    echo -n `sha1sum $f|cut -d' ' -f 1` ""
    echo -n `stat -c %s $f` ""
    echo $1
}
calc_sha1 main/binary-amd64/Packages >> dists/$DIST/Release

rm -f $DIST/Release.gpg
rm -f $DIST/InRelease
gpg -abs -u "$SIGN_KEY" \
    < dists/$DIST/Release > dists/$DIST/Release.gpg
gpg -a -s --clearsign -u "$SIGN_KEY" \
    < dists/$DIST/Release > dists/$DIST/InRelease
popd

if [ `id -u` -eq 0 ]; then
    chown -R --reference=$REPO_DIR $REPO_DIR
fi
~~~

Usage: add this line to `/etc/apt/sources.list` on test machine (adjust host and path):

~~~
deb http://local-test.lan/linux-deb/r3.1 jessie-unstable main
~~~
