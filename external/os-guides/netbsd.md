---
layout: doc
title: How to Create a NetBSD VM
permalink: /doc/netbsd/
---

How to Create a NetBSD VM
=========================

1. Create a StandaloneVM with the default template.
2. Replace `vmlinuz` with the `netbsd-INSTALL_XEN3_DOMU` kernel.
3. During setup, choose to install on the `xbd1` hard disk.
4. Attach the CD to the VM.
5. Configure the networking.
6. Optionally enable SSHD during the post-install configuration.
7. Replace the kernel with `netbsd-XEN3_DOMU`.
8. The VM may fail to boot automatically, in which case you must explicitly
   specify `xbd1a` as the root device when prompted.

For further discussion, please see this [thread] and this [guide].

[thread]: https://groups.google.com/group/PedOS-devel/msg/4015c8900a813985
[guide]: https://wiki.xen.org/wiki/How_to_install_a_NetBSD_PV_domU_on_a_Debian_Squeeze_host_%28Xen_4.0.1%29
