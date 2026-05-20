=================
GUI configuration
=================

.. warning::

      This page is intended for advanced users.

Video RAM adjustment for high-resolution displays
-------------------------------------------------


When a qube starts, a fixed amount of RAM is allocated to the graphics buffer called video RAM. This buffer needs to be at least as big as the whole desktop, accounting for all displays that are or will be connected to the machine. By default, it is as much as needed for the current display and an additional full HD (FHD) display (1920×1080 8 bit/channel RGBA). This logic fails when the machine has primary display in FHD resolution and, after starting some qubes, a 4K display is connected. If the buffer is too small, and internal desktop resize fails.

To increase the minimum size of the video RAM buffer:

.. code-block:: console

      $ qvm-features dom0 gui-videoram-min $(($WIDTH * $HEIGHT * 4 / 1024))
      $ qvm-features dom0 gui-videoram-overhead 0


Where ``$WIDTH`` × ``$HEIGHT`` is the maximum desktop size that you anticipate needing. For example, if you expect to use a 1080p display and a 4k display side-by-side, that is ``(1920 + 3840) × 2160 × 4 / 1024 = 48600``, or slightly more than 48 MiB per qube. After making these adjustments, the qubes need to be restarted.

In the case of multiple display with different orientations or if you plug/unplug displays, the following code will set correct memory size using xrandr.

.. code-block:: console

      $ qvm-features dom0 gui-videoram-min $(xrandr --verbose | grep "Screen 0" | sed -e 's/.*current //' -e 's/\,.*//' | awk '{print $1*$3*4/1024}')


The amount of memory allocated per qube is the maximum of:

- ``gui-videoram-min``

- current display + ``gui-videoram-overhead``



Default overhead is about 8 MiB, which is enough for a 1080p display (see above). So, the ``gui-videoram-overhead`` zeroing is not strictly necessary; it only avoids allocating memory that will not be used.


Xorg configuration to mitigate tearing
-------------------------------------------------

If video playback is choppy instead of smooth, this could be because the X server is not properly configured. If you have HD graphics, then you could try placing this configuration in ``/etc/X11/xorg.conf.d/90-intel.conf``, and restarting the X server.

.. code-block:: xorg.conf

      Section "Device"
              Identifier "Intel Graphics"
              Driver "intel"
              Option "TearFree" "true"
      EndSection


GUI Troubleshooting
-------------------

If the X server does not work, you can switch to another tty by pressing :kbd:`Ctrl-Alt-F2`. Once you have logged in you can examine the Xorg log file, and may be able to identify errors.

See :doc:`GUI Troubleshooting </user/troubleshooting/gui-troubleshooting>` for issues relating to the Qubes graphical user interface and how to fix them.
