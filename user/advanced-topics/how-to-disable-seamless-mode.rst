============================
How to disable seamless mode
============================

By default, vm applications are seamlessly integrated into dom0's desktop environment. This guide explains how to disable this seamless mode in order to get separate desktop inside of an otherwise integrated vm.

Visually, it turns this:

.. TODO: add conventional window on dom0 desktop screenshot

Into this:

.. TODO: add vm with a full desktop screenshot

VNC is better
-------------

While it is possible to disable seamless desktop integration, at the moment of writing (2026-02) different approach is often considered superior: setting up VNC server and client in the same vm. It also provides you with a separate desktop in a vm, but doesn't require setting specific properties, behaves better than the default qubes vm viewer, and doesn't reduce integration (such as ability to transfer files among qubes) in any way.

See the following topics on using VNC:

- `original instruction by unman <https://forum.qubes-os.org/t/automatic-startup-of-gnome-environement/26526/25>`__
- `most recent discussion containing information about this <https://forum.qubes-os.org/t/rejecting-hard-work-of-qubes-os-developers-gui-integration/38817/7>`__

Disable seamless mode on Debian guest
-------------------------------------

In command line, with :code:`full_desktop` as the name of the targeted qube:

  .. code:: console

    [user@dom0 ~]$ qvm-run -u root full_desktop -- mv /etc/X11/xorg-qubes.conf /etc/X11/xorg-qubes.conf.backup
    [user@dom0 ~]$ qvm-prefs full_desktop debug true
    [user@dom0 ~]$ qvm-prefs full_desktop virt_mode hvm
    [user@dom0 ~]$ qvm-prefs full_desktop kernelopts "systemd.unit=graphical.target"
    [user@dom0 ~]$ qvm-service full_desktop lightdm on
    [user@dom0 ~]$ qvm-shutdown full_desktop

Revert to seamless mode on Debian guest
---------------------------------------

Disable seamless mode on Fedora guest
-------------------------------------

Revert to seamless mode on Fedora guest
---------------------------------------

