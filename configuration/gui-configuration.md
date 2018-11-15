---
layout: doc
title: GUI Configuration and Troubleshooting
permalink: /doc/gui-configuration/
---

GUI Configuration and Troubleshooting
=====================================

Video RAM adjustment for big displays
-------------------------------------

Symptom: I have 4K external display and I when I connect it, I can't click on
anything but an small area in upper-right corner.

When a qube starts, fixed amount of RAM is allocated for graphics buffer called
Video RAM. This buffer needs to be at least as big as whole desktop, accounting
for all displays that are or will be connected to the machine. So by default it
is as big as needed for current display and an additional Full HD display
(1920×1080 8 bit/channel RGBA). This logic fails when the machine has primary
display in FHD resolution, but after starting the VMs a 4K display is connected.
The buffer is too small and internal desktop resize fails.

Solution: Adjust minimum size of Video RAM buffer.

```sh
qvm-features dom0 gui-videoram-min $(($WIDTH * $HEIGHT * 4 / 1024))
qvm-features dom0 gui-videoram-overhead 0
```

Where `$WIDTH`×`$HEIGHT` is maximum desktop size the user anticipates. For
example, if user needs 1080p and 4k display side-by-side, that is
`(1920 + 3840) × 2160 × 4 / 1024 = 48600`, or slightly above 48 MiB per-qube.
After adjustment, the VMs need to be restarted.

The amount of memory allocated per-qube is the maximum of:
- `gui-videoram-min`
- current display + `gui-videoram-overhead`.

Default overhead is about 8 MiB, which is enough for 1080p display (see above).
So the `gui-videoram-overhead` zeroing is not strictly necessary, it only avoids
allocating memory that will not be used.
