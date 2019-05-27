---
layout: doc
title: Qubes Service
permalink: /doc/qubes-service/
redirect_from:
- /en/doc/qubes-service/
- /doc/QubesService/
- /wiki/QubesService/
---

Usage documentation is on `qvm-service` man page. There are also described predefined services.

Under the hood enabled service in VM is signaled by file in `/var/run/qubes-service`.
This can be used to implement almost enable/disable **per-VM** switch controlled by dom0.
Adding support for systemd services is pretty simple:

In the VM, create `/etc/systemd/system/<service name>.service.d/30_qubes.conf` file
containing (you may need to create a directory for this file first):

~~~
[Unit]
ConditionPathExists=/var/run/qubes-service/<service name>
~~~

This will cause service to be started only when you enable it with qvm-service for this VM.

