---
layout: doc
title: Storage Pools
permalink: /doc/storage-pools/
---

Storage Pools in Qubes
======================

Qubes OS R 3.2 introduced the concept of storage drivers & pools.  This feature
was a first step towards a saner storage API, which is heavily rewritten in R4.
A storage driver provides a way to store VM images in a Qubes OS system.
Currently, the default driver is `xen` which is the default way of storing
volume images as files in a directory tree like `/var/lib/qubes/`.

A pool storage driver can be identified either by the driver name with the
`driver` key or by the class name like this:
`class=qubes.storage.xen.XenStorage`. Because R3.2 doesn't use Python
`setup_hooks`, to actually use a short driver name for a custom storage driver,
you have to patch `qubes-core-admin`. You can use the `class` config key
instead, when your class is accessible by `import` in Python.

A pool (in R3.2) is a configuration information which can be referenced when
creating a new VM. Each pool is saved in `storage.conf`. It has a name, a
storage driver and some driver specific configuration attached.

When installed, the system has, as you can see from the content of
`/etc/qubes/storage.conf`, a pool named `default`. It uses the driver `xen`. The
default pool is special in R3.2. It will add `dir_path=/var/lib/qubes`
configuration value from `defaults[pool_config]`, if not overwritten.


Currently the only supported driver out of the box is `xen`. The benefit of
pools (besides that you can write an own storage driver e.g. for Btrfs) in R3.2
is that you can store your domains in multiple places.

You can add a pool to `storage.conf` like this:

```
[foo]
driver=xen
dir_path=/opt/qubes-vm
```

Now, when creating a new VM on the command-line, a you may pass the `-Pfoo`
argument to `qvm-create` to have the VM images stored in pool `foo`. See also
`qvm-create --help`.

While the current API is not as clean and beautiful as the R4 API, it allows
you to write your own storage drivers e.g. for Btrfs today. 
