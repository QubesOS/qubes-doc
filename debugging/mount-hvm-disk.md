---
layout: doc
title: Mount LVM image
permalink: /doc/mount-lvm-image/
---

# How to mount LVM image

You want to read your LVM image (ex: you did some errors and can't start the VM ). 
 
1: make the image available for qubesdb. (dom0)

```bash
# Example: /dev/qubes_dom0/vm-debian-9-tmp-root
dev=$(basename $(readlink /dev/YOUR_LVM_VG/YOUR_LVM_IMAGE))
qubesdb-write /qubes-block-devices/$dev/desc "YOUR_LVM_IMAGE"
```

2: Create a new disposable VM (dom0)

```bash
qvm-run -v --dispvm=YOUR_DVM_TEMPLATE --service qubes.StartApp+xterm &
```

3: Mount the partition you want to, and do what you want with it (disp)

```bash
mount /dev/xvdiX /mnt/
```

4: Umount and kill the VM (disp)
```
umount /mnt/
```

5: Remove the image from qubesdb (dom0)
```
qubesdb-rm /qubes-block-devices/$dev/
```

# References

https://github.com/QubesOS/qubes-issues/issues/4687#issuecomment-451626625
