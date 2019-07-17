---
layout: doc
title: GUI Configuration and Troubleshooting
permalink: /doc/gui-configuration/
---

GUI Configuration and Troubleshooting
=====================================

Video RAM adjustment for high-resolution displays
-------------------------------------------------

**Problem:** You have a 4K external display, and when you connect it, you can't click on anything but a small area in the upper-right corner.

When a qube starts, a fixed amount of RAM is allocated to the graphics buffer called video RAM.
This buffer needs to be at least as big as the whole desktop, accounting for all displays that are or will be connected to the machine.
By default, it is as much as needed for the current display and an additional full HD (FHD) display (1920×1080 8 bit/channel RGBA).
This logic fails when the machine has primary display in FHD resolution and, after starting some qubes, a 4K display is connected.
The buffer is too small, and internal desktop resize fails.

**Solution:** Increase the minimum size of the video RAM buffer.

```sh
qvm-features dom0 gui-videoram-min $(($WIDTH * $HEIGHT * 4 / 1024))
qvm-features dom0 gui-videoram-overhead 0
```

Where `$WIDTH`×`$HEIGHT` is the maximum desktop size that you anticipate needing.
For example, if you expect to use a 1080p display and a 4k display side-by-side, that is `(1920 + 3840) × 2160 × 4 / 1024 = 48600`, or slightly more than 48 MiB per qube.
After making these adjustments, the qubes need to be restarted.

The amount of memory allocated per qube is the maximum of:
- `gui-videoram-min`
- current display + `gui-videoram-overhead`

Default overhead is about 8 MiB, which is enough for a 1080p display (see above).
So, the `gui-videoram-overhead` zeroing is not strictly necessary; it only avoids allocating memory that will not be used.
