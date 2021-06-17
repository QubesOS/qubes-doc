---
lang: en
layout: doc
permalink: /doc/test-bench/
redirect_from:
- /en/doc/test-bench/
- /doc/TestBench/
- /wiki/TestBench/
ref: 44
title: How to Set Up a Test Bench
---


This guide shows how to set up simple test bench that automatically test your code you're about to push. It is written especially for `core3` branch of `core-admin.git` repo, but some ideas are universal.

We will set up a spare machine (bare metal, not a virtual) that will be hosting our experimental Dom0. We will communicate with it via Ethernet and SSH. This tutorial assumes you are familiar with [QubesBuilder](/doc/qubes-builder/) and you have it set up and running flawlessly.

## Setting up the machine

First, do a clean install from ISO you built or grabbed elsewhere.

You have to fix network, because it is intentionally broken. This script should reenable your network card without depending on anything else.

```bash
#!/bin/sh

# adjust this for your NIC (run lspci)
BDF=0000:02:00.0

prog=$(basename $0)

pciunbind() {
    local path
    path=/sys/bus/pci/devices/${1}/driver/unbind
    if ! [ -w ${path} ]; then
        echo "${prog}: Device ${1} not bound"
        return 1
    fi
    echo -n ${1} >${path}
}

pcibind() {
    local path
    path=/sys/bus/pci/drivers/${2}/bind
    if ! [ -w ${path} ]; then
        echo "${prog}: Driver ${2} not found"
        return 1
    fi
    echo ${1} >${path}
}

pciunbind ${BDF}
pcibind ${BDF} e1000e

dhclient
```

TODO: describe how to run this at every startup

Now configure your DHCP server so your testbench gets static IP and connect your machine to your local network. You should ensure that your testbench can reach the Internet.

Install `openssh-server` on your testbench:

~~~
yum install openssh-server
~~~

Ensure that sudo works without password from your user account (it should by default).

## Development VM

### SSH

Arrange firewall so you can reach the testbench from your `qubes-dev` VM. Generate SSH key in `qubes-dev`:

~~~
ssh-keygen -t ecdsa -b 521
~~~

Add the following section in `.ssh/config` in `qubes-dev`:

~~~
Host testbench
    # substitute username in testbench
    User user
    # substitute address of your testbench
    HostName 192.168.123.45
~~~

Then connect to your testbench and paste newly generated `id_ecdsa.pub` to `.ssh/authorized_keys` on testbench so you can log in without entering password every time.

### Scripting

This step is optional, but very helpful. Put these scripts somewhere in your `${PATH}`, like `/usr/local/bin`.

`qtb-runtests`:

```bash
#!/bin/sh

ssh testbench python -m qubes.tests.run
```

`qtb-install`:

```bash
#!/bin/sh

TMPDIR=/tmp/qtb-rpms

if [ $# -eq 0 ]; then
        echo "usage: $(basename $0) <rpmfile> ..."
        exit 2
fi

set -e

ssh testbench mkdir -p "${TMPDIR}"
scp "${@}" testbench:"${TMPDIR}"

while [ $# -gt 0 ]; do
        ssh testbench sudo rpm -i --replacepkgs --replacefiles "${TMPDIR}/$(basename ${1})"
        shift
done
```

`qtb-iterate`:

```bash
#!/bin/sh

set -e

# substitute path to your builder installation
pushd ${HOME}/builder >/dev/null

# the following are needed only if you have sources outside builder
#rm -rf qubes-src/core-admin
#make COMPONENTS=core-admin get-sources

make core-admin
qtb-install qubes-src/core-admin/rpm/x86_64/qubes-core-dom0-*.rpm
qtb-runtests
```

### Hooking git

I (woju) have those two git hooks. They ensure tests are passing (or are marked as expected failure) when committing and pushing. For committing it is only possible to run tests that may be executed from git repo (even if the rest were available, I probably wouldn't want to do that). For pushing, I also install RPM and run tests on testbench.

`core-admin/.git/hooks/pre-commit`: (you may retain also the default hook, here omitted for readability)

```bash
#!/bin/sh

set -e

python -c "import sys, qubes.tests.run; sys.exit(not qubes.tests.run.main())"
```

`core-admin/.git/hooks/pre-push`:

```bash
#!/bin/sh

exec qtb-iterate
```
