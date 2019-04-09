---
layout: doc
title: Mount HVM disk
permalink: /doc/mount-hvm-disk/
---

# How to mount HVM disk 

You want to read your HVM disk (ex: you did some errors and can't start the HVM ). 

First, read the partition table:

```bash
sudo parted /dev/YOUR_VG/YOUR_VM unit B print
```

Example:

```
$:sudo parted /dev/windows-vg/vg-game-root unit B print
Model: Linux device-mapper (thin) (dm)
Disk /dev/dm-138: 314572800000B
Sector size(logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:
Number       Start          End            Size           Type     File system  Flags
1            1048576B       105906175B     104857600B     primary  ntfs         boot
2            105906176B     314571751423B  314465845248B  primary  ntfs
```

Then mount the partition you want:

```bash
sudo mount -o loop,offset=105906176 -t ntfs /dev/windows-vg/vg-game-root /mnt/
```
