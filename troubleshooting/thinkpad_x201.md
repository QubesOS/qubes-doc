---
layout: doc
title: Getting Lenovo Thinkpad X201 & X200 to work
permalink: /doc/thinkpad_x201/
redirect_from:
- /en/doc/thinkpad_x201/
- /doc/Thinkpad_X201/
- /wiki/Thinkpad_X201/
---

Instructions for getting your Lenovo Thinkpad X201 & X200 laptop working with Qubes/Linux
=========================================================================

For being able to boot the installer from USB, you have to disable VT-d in the BIOS.
Enter the BIOS by hitting F1, go to Config - CPU and then disable there VT-d.

After the installation, you have to set a startup-parameter for Xen, to be able to activate VT-d again:

1. Open a terminal in dom0
2. Edit `/etc/default/grub`
3. Add to the line `GRUB_CMDLINE_XEN_DEFAULT` the setting `iommu=no-igfx`, save and quit
4. sudo `grub2-mkconfig --output /boot/grub2/grub.cfg`

Then reboot, enter BIOS and re-enable VT-d.

Getting scrolling with the Trackpoint and the Middle Button to work
-------------------------------------------------

1. Create a script with the following content:

   ~~~
   #!/bin/sh
   xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation" 1
   xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation Button" 2
   xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation Timeout" 200
   xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation Axes" 6 7 4 5
   ~~~

2. Add the script to the startup-items of your desktop environment.
