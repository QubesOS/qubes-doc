---
lang: en
layout: doc
permalink: /doc/mount-lvm-image/
ref: 46
title: How to mount lvm images
---

You want to read your LVM image (e.g., there is a problem where you can't start any VMs except dom0).

1: make the image available for qubesdb.
From dom0 terminal:

```bash
# Example: /dev/qubes_dom0/vm-debian-9-tmp-root
[user@dom0]$ dev=$(basename $(readlink /dev/YOUR_LVM_VG/YOUR_LVM_IMAGE))
[user@dom0]$ qubesdb-write /qubes-block-devices/$dev/desc "YOUR_LVM_IMAGE"
```

2: Create a new disposable VM

```bash
[user@dom0]$ qvm-run -v --dispvm=YOUR_DVM_TEMPLATE --service qubes.StartApp+xterm &
```

3: Attach the device to your newly created disp VM

From the GUI, or from the command line:

```bash
[user@dom0]$ qvm-block attach NEWLY_CREATED_DISPVM dom0:$dev
```

4: Mount the partition you want to, and do what you want with it

```bash
[user@dispXXXX]$ mount /dev/xvdiX /mnt/
```

5: Umount and kill the VM

```bash
[user@dispXXXX]$ umount /mnt/
```

6: Remove the image from qubesdb

```bash
[user@dom0]$ qubesdb-rm /qubes-block-devices/$dev/
```

# References

Please consult this issue's [comment](https://github.com/QubesOS/qubes-issues/issues/4687#issuecomment-451626625).
