---
layout: doc
title: QubesService
permalink: /en/doc/qubes-service/
redirect_from:
- /doc/QubesService/
- /wiki/QubesService/
---

Usage documentation is on [qvm-service manual page](/en/doc/dom0-tools/qvm-service/). There are also described predefined services.

Under the hood enabled service in VM is signaled by file in /var/run/qubes-service. This can be used to implement almost enable/disable **per-VM** switch controlled by dom0. Adding support for systemd services is pretty simple:

1.  Disable old service: `systemctl disable <service name>`
2.  Create `/etc/systemd/system/<service name>.service` file containing:

    ~~~
    .include /lib/systemd/system/<service name>.service
    [Unit]
    ConditionPathExists=/var/run/qubes-service/<service name>
    ~~~

3.  Enable new service: `systemctl enable <service name>`.

This will cause service to be started only when you enable it with qvm-service for given VM.
