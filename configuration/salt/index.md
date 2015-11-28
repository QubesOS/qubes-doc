---
layout: doc
title: Management stack
permalink: /doc/salt/
---
# Management infrastructure

Since Qubes R3.1 release we have included `salt` (also called SaltStack)
management engine in dom0 as default with some states already configured. salt
allows administrators to easily configure their systems. In this guide we will
show how it is set up and how you can modify it for your own purpose.

In the current form the **API is provisional** and subject to change between
*minor* releases.

## Understanding `salt`

This document is not meant to be comprehensive salt documentation, however
before writing anything it is required you have at least *some* understanding of
basic salt-related vocabulary. For more exhaustive documentation, visit
[official site][salt-doc], though we must warn you that it is not easy to read
if you just start working with salt and know nothing.

Salt has client-server architecture, where server (called *master*) manages its
clients (called *minions*). In typical situation it is intended that
administrator interacts only with master and keeps the configuration there. In
Qubes OS we don't have master though, since we have only one minion, which
resides in `dom0` and manages domains from there. This is also supported by
salt.

Salt is a management engine, that enforces particular state of the system, where
minion runs. A *state* is an end effect *declaratively* expressed by the
administrator. This is the most important concept in the whole package. All
configuration (ie. the states) are written in YAML.

A *pillar* is a data backend declared by administrator. When states became
repetitive, instead of pure YAML they can be written with help of some template
engine (preferably jinja2), which can use data structures specified in pillars.

A *formula* is a ready to use, packaged solution that combines state and pillar,
possibly with some file templates and other auxiliary files. There are many of
those made by helpful people all over the Internet.

A *grain* is some data that is also available in templates, but its value is not
directly specified by administrator. For example the distribution (like
`"Debian"` or `"Gentoo"`) is a value of the grain `"os"`. It also contains other
info about kernel, hardware etc.

A *module* is a Python extension to salt that is responsible for actually
enforcing the state in a particular area. It exposes some *imperative* functions
for administrator. For example there is `system` module that has `system.halt`
function that, when issued, will immediately halt the computer. There is another
function called `state.highstate` which will synchronise the state of the system
with the administrator's will.


## Salt configuration, Qubes OS layout

All salt configuration in `/srv/` directory, as usual. The main directory is
`/srv/salt/` where all state files reside. States are contained in `*.sls`
files. However the states that are part of standard Qubes distribution are
mostly templates and the configuration is done in pillars from formulas.

The formulas are in `/srv/formulas`, including stock formula for domains in
`/srv/formulas/dom0/virtual-machines-formula/qvm`, which are used by firstboot.

Because we use some code that is not found in older versions of salt, there is
a tool called `qubesctl` that should be run instead of `salt-call --local`. It
accepts all arguments of the vanilla tool.


## Writing your own configuration

Let's start with quick example:

    my new and shiny vm:
      qvm.present:
        - name: salt-test # can be omitted then same as ID
        - template: fedora-21
        - label: yellow
        - mem: 2000
        - vcpus: 4
        - flags:
          - proxy

It uses Qubes-specific `qvm.present` state, which ensures that domain is
created. The name should be `salt-test` (and not `my new and shiny vm`),
the rest are domains properties, same as in `qvm-prefs`. `proxy` flag informs
salt that the domain should be a ProxyVM.

This should be put in `/srv/salt/my-new-vm.sls` or another `.sls` file. Separate
`*.top` file should be also written:

    base:
      dom0:
        - my-new-vm

The third line should contain the name of the previous file, without `.sls`.

Now because we use custom extension to manage top files (instead of just
enabling them all) to enable the particular top file you should issue command:

    qubesctl top.enable my-new-vm

To list all enabled tops:

    qubesctl top.enabled

And to disable one:

    qubesctl top.disable my-new-vm


To actually apply the state:

    qubesctl state.highstate


## All Qubes-specific states

### qvm.present

As in example above, it creates domain and sets its properties.

### qvm.prefs

You can set properties of existing domain:

    my preferences:
      qvm.prefs:
        - name: salt-test2
        - netvm: sys-firewall

Note that `name:` is a matcher, ie. it says the domain which properties will be
manipulated is called `salt-test2`. The implies that you currently cannot rename
domains this way.

### qvm.service

    services in my domain:
      qvm.service:
        - name: salt-test3
        - enable:
          - service1
          - service2
        - disable:
          - service3
          - service4
        - default:
          - service5

This enables, disables, or sets to default, the services as in qvm-service.

### qvm.running

Ensures the domain is running:

    domain is running:
      qvm.running:
        - name: salt-test4


[salt-doc]: https://docs.saltstack.com/en/latest/
