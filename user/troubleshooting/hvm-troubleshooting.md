---
layout: doc
title: HVM Troubleshooting
permalink: /doc/hvm-troubleshooting/

---

# HVM Troubleshooting #

## HVM pauses on boot, followed by kernel error ## 

The HVM may pause on boot, showing a fixed cursor.
After a while a series of warnings may be shown similar to this:

    BUG: soft lockup - CPU#0 stuck for 23s! [systemd-udevd:244]

To fix this:

1.  Kill the HVM.
1.  Start the HVM
1.  Press "e" at the grub screen to edit the boot parameters
1.  Find the /vmlinuz line, and edit it to replace "rhgb" with "modprobe.blacklist=bochs_drm"
1.  Press "Ctrl-x" to start the HVM

If this solves the problem then you will want to make the change permanent:

1.  Edit the file `/etc/default/grub`.
1.  Find the line which starts:
    ~~~
    GRUB_CMDLINE_LINUX=
    ~~~
1.  Remove this text from that line:
    ~~~
    rhgb
    ~~~
1.  Add this text to that line:
    ~~~
    modprobe.blacklist=bochs_drm
    ~~~
1.  Run this command:
    ~~~
    grub2-mkconfig --output=/boot/grub2/grub.cfg
    ~~~

The HVM should now start normally.

## Can't start an OS in an HVM / "Probing EDD (edd=off to disable!... ok" message ##

If you see a screen popup with SeaBios and 4 lines, last one being `Probing EDD (edd=off to disable!... ok`, then enter the following command from a `dom0` prompt:

    qvm-prefs <HVMname> kernel ""

## HVM crashes when booting from ISO ##
If your HVM crashes when trying to boot an ISO, first ensure that ` qvm-prefs <HVMname>` is empty, as shown above. 
If this doesn't help, then disable memory balancing and set the minimum memory to 2GB.

You can disable memory-balancing in the settings, under the “Advanced” tab.

To give the VM a RAM of 2GB, open a terminal in `dom0` and enter:

    qvm-prefs <HVMname> memory 2000

