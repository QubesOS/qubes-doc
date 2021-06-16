---
lang: en
layout: doc
permalink: /doc/qubes-service/
redirect_from:
- /en/doc/qubes-service/
- /doc/QubesService/
- /wiki/QubesService/
ref: 138
---

Usage documentation is in the `qvm-service` man page. There are also described predefined services.

Under the hood, an enabled service in a VM is signaled by a file in `/var/run/qubes-service`.
This can be used to implement an almost enable/disable **per-VM** switch controlled by dom0.

Adding support for systemd services is pretty simple. In the VM, create the following file (and directory, if needed): `/etc/systemd/system/<service name>.service.d/30_qubes.conf`. It should contain the following:

~~~
[Unit]
ConditionPathExists=/var/run/qubes-service/<service name>
~~~

This will cause the service to be started only when you enable it with `qvm-service` for this VM.
