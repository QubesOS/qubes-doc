---
layout: wiki
title: OutOfmemory
permalink: /wiki/OutOfmemory/
---

This is about disk memory, not RAM.

VMs specially templates use disk space. Also default private storage max size is 2 GB, but it is very easy to increase it as required. In case you use all disk memory you get the Out of memory error that may crash your system because also Dom0 does not have enough disk space to work.

So it is a good practice to regularly check disk memory usage with command

``` {.wiki}
df
```

in dom0 terminal.

A system in out of memory condition should be able to boot, but may be unable to load a desktop manager. In this case it is possible to login to dom0 terminal with Alt + Ctrl + F2. To recover disk space
