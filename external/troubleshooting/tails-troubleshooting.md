---
layout: doc
title: Tails Troubleshooting
permalink: /doc/tails-troubleshooting/
---

# Tails Troubleshooting Guide #

## Black screen during startup

This was reported with earlier versions of Tails -- the problem should now be fixed.
If you do encounter a black screen during Tails startup, you can try to constrain display settings by appending vga codes to the Tails boot parameters.
If you do not know the codes, append `vga=999`, and a helpful prompt will appear.

Note: Tails 2.3 does not appear to honour the vga code.

## Window extends beyond the bottom of the screen

This problem seems to arise because Tails sizes to the height of the screen, but there is a title bar at the top of the window.
Either remove the title bar altogether, or move the window upwards using ALT+drag.

## Persistent tools do not work
The persistence tools, such as persistent volume, may not work because Tails has not been launched from USB. 
The HVM disk(s) can be configured and mounted from within Tails to provide persistent storage.
If you want to use an existing USB persistent volume: 
1. Interrupt the Tails vm boot process with arrow-up when the grub boot menu appears. 
2. In dom0 attach the USB drive containing the persistent volume to the Tails VM. 
3. Continue booting Tails. Tails-greeter will detect the encrypted partition on the attached USB. 
4. Unlock the persistent volume in Tails-greeter and use it as normal.

## Tails qube doesn't shut down cleanly
If the Tails qube will not shut down cleanly, you can kill it from the GUI Manager or enter ```qvm-kill Tails``` in the console.

