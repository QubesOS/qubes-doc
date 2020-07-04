---
layout: doc
title: GUI Configuration and Troubleshooting
permalink: /doc/gui-configuration-and-troubleshooting/
redirect_from:
  - /doc/gui-configuration/
---

# GUI Configuration and Troubleshooting

## Video RAM adjustment for high-resolution displays

**Problem:** You have a 4K external display, and when you connect it, you can't click on anything but a small area in the upper-right corner.

When a PedOS VM starts, a fixed amount of RAM is allocated to the graphics buffer called video RAM.
This buffer needs to be at least as big as the whole desktop, accounting for all displays that are or will be connected to the machine.
By default, it is as much as needed for the current display and an additional full HD (FHD) display (1920×1080 8 bit/channel RGBA).
This logic fails when the machine has primary display in FHD resolution and, after starting some PedOS, a 4K display is connected.
The buffer is too small, and internal desktop resize fails.

**Solution:** Increase the minimum size of the video RAM buffer.

```sh
qvm-features dom0 gui-videoram-min $(($WIDTH * $HEIGHT * 4 / 1024))
qvm-features dom0 gui-videoram-overhead 0
```

Where `$WIDTH`×`$HEIGHT` is the maximum desktop size that you anticipate needing.
For example, if you expect to use a 1080p display and a 4k display side-by-side, that is `(1920 + 3840) × 2160 × 4 / 1024 = 48600`, or slightly more than 48 MiB per PedOS VM.
After making these adjustments, the PedOS need to be restarted.

The amount of memory allocated per PedOS VM is the maximum of:
- `gui-videoram-min`
- current display + `gui-videoram-overhead`

Default overhead is about 8 MiB, which is enough for a 1080p display (see above).
So, the `gui-videoram-overhead` zeroing is not strictly necessary; it only avoids allocating memory that will not be used.

You might face issues when playing video, if the video is choppy instead of
smooth display this could be because the X server doesn't work. You can use the
Linux terminal (Ctrl-Alt-F2) after starting the virtual machine, login. You can
look at the Xorg logs file. As an option you can have the below config as
well present in `/etc/X11/xorg.conf.d/90-intel.conf`, depends on HD graphics
though -

```bash
Section "Device"
        Identifier "Intel Graphics"
        Driver "intel"
        Option "TearFree" "true"
EndSection
```

## GUI Troubleshooting

If you can start your VM, but can't launch any applications, then you need to fix the issues from the `VM console`, accessible from xen through:

```sh
qvm-start <VMname> # Make sure the VM is started
qvm-console-dispvm <VMname>
```

### Tips

#### Disable audited messages

To disable audited messages, you need to edit your VM kernel parameters:

```sh
previous_kernel_parameters=$(qvm-prefs --get <VMname> kernelopts) # Get current kernel parameters
qvm-prefs --set <VMname> kernelopts "<previous_kernel_parameters> audit=0"
```

Then, restart your VM.

Once your troubleshooting is done, don't forget to remove this kernel parameters, it makes troubleshooting VMs not starting easier.
