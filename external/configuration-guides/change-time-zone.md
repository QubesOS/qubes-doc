---
layout: doc
title: Changing your Time Zone
permalink: /doc/change-time-zone/
---

# Changing your Time Zone #

## Qubes 4.0 ##

### Command line ###

If you use the i3 window manager or would prefer to change the system's time
zone in terminal you can issue the `timedatectl` command with the option
`set-timezone`.

For example, to set the system's time zone to Berlin, Germany type in a dom0
terminal:

    $ sudo timedatectl set-timezone 'Europe/Berlin'

You can list the available time zones with the option `list-timezones` and show
the current settings of the system clock and time zone with option `status`.

Example output status of `timedatectl` on a system with time zone set to
Europe/Berlin:

    [user@dom0 ~]$ timedatectl status
          Local time: Sun 2018-10-14 06:20:00 CEST
      Universal time: Sun 2018-10-14 04:20:00 UTC
            RTC time: Sun 2018-10-14 04:20:00
           Time zone: Europe/Berlin (CEST, +0200)
     Network time on: no
    NTP synchronized: no
     RTC in local TZ: no

