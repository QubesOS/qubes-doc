---
layout: doc
title: Mount LVM image
redirect_from:
- /doc/mount-lvm-image/
---

# How to mount LVM image

You want to read your LVM image (ex: you did some errors and can't start the VM ). 
 
1: make the image available for qubesdb.

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
```
[user@dispXXXX]$ umount /mnt/
```

6: Remove the image from qubesdb
```
[user@dom0]$ qubesdb-rm /qubes-block-devices/$dev/
```

# References

https://github.com/QubesOS/qubes-issues/issues/4687#issuecomment-451626625
