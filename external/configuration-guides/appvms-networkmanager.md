---
layout: doc
title: NetworkManager in AppVMs
permalink: /doc/appvms-networkmanager/
---

NetworkManager configuration in AppVMs
======================================

System connections
------------------

In NetVMs and in VMs where the service `network-manager` is enabled, `/etc/NetworkManager/system-connections` is a symlink to /rw/config/NM-system-connections.

So any modification you make in /etc/NetworkManager/system-connections is persistent.

You CANNOT configure Xen provided network interfaces.

Implementation
--------------

Everything explained here is based on `/usr/lib/qubes/network-manager-prepare-conf-dir`, which is executed from `/usr/lib/systemd/system/NetworkManager.service.d/30_qubes.conf`.

This service is only executed if `/var/run/qubes-service/network-manager` exists, which is created by `qubes-sysinit.sh`, executed by `/usr/lib/systemd/system/qubes-sysinit.service`
