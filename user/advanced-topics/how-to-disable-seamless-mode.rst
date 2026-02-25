============================
How to disable seamless mode
============================

By default, vm applications are seamlessly integrated into dom0's desktop environment. This article explains how to disable seamless mode in order to get separate desktop inside of an otherwise integrated vm.

Visually, it turns this:

.. TODO: add conventional window on dom0 desktop screenshot

Into this:

.. TODO: add vm with a full desktop screenshot

VNC is better
-------------

While it is possible to disable seamless desktop integration, at the moment of writing (2026-02) different approach is often considered superior: setting up VNC server and client in the same vm. It also provides you with a separate desktop in a vm, but doesn't require setting specific properties, behaves better than the default qubes vm viewer, and doesn't reduce integration (such as inter-qube clipboard) in any way.

See the following topics on using VNC:

- `original instruction by unman <https://forum.qubes-os.org/t/automatic-startup-of-gnome-environement/26526/25>`__
- `most recent discussion containing information about this <https://forum.qubes-os.org/t/rejecting-hard-work-of-qubes-os-developers-gui-integration/38817/7>`__

Overview
--------

In its simplest form disabling seamless mode is done by disabling or stopping :code:`qubes-gui-agent` service, but it doesn't provide any graphical interface as a replacement.

Graphical viewer window for a qube is displayed when it has feature :code:`gui` unset with virtualization mode set to :code:`hvm`.

.. note::

   For more detailed explanation of this behaviour see :code:`gui` and :code:`gui-emulated` features in the "LIST OF KNOWN FEATURES" section of :code:`qvm-features` manual.

Moreover, debian and fedora hosts don't run desktop environment unless they are configured to do so, for example by setting :code:`graphical.target` as the default for systemd to boot into.

.. warning::

   You might need to provision more initial memory to your qubes in order for them to boot.

Limitations
^^^^^^^^^^^

Inter-qube clipboard feature relies on :code:`qubes-gui-agent`. It does not work when seamless mode is off.

Disable seamless mode on Debian guest
-------------------------------------

In terminal, with :code:`full_desktop` as the name of the targeted qube:

1. Configure qube preferences

  .. code:: console

    [user@dom0 ~]$ qvm-features --unset full_desktop gui
    [user@dom0 ~]$ qvm-prefs full_desktop virt_mode hvm
    [user@dom0 ~]$ qvm-prefs full_desktop memory 1000
    [user@dom0 ~]$ qvm-prefs full_desktop kernelopts "systemd.unit=graphical.target"
    [user@dom0 ~]$ qvm-service full_desktop lightdm on

  Lightdm service disables seamless mode by preventing qubes-gui-agent from starting and starts lightdm display manager.

  Kernel option :code:`systemd.unit` overrides the default boot target.

2. Restart the qube for changes to take effect

Revert to seamless mode on Debian guest
---------------------------------------

To revert, simply undo the configuration changes:

  .. code:: console

    [user@dom0 ~]$ qvm-run -u root full_desktop -- mv /etc/X11/xorg-qubes.conf /etc/X11/xorg-qubes.conf.backup
    [user@dom0 ~]$ qvm-features full_desktop gui 1
    [user@dom0 ~]$ qvm-prefs -D full_desktop virt_mode
    [user@dom0 ~]$ qvm-prefs -D full_desktop kernelopts
    [user@dom0 ~]$ qvm-service full_desktop lightdm off


Disable seamless mode on Fedora guest
-------------------------------------

In terminal, with :code:`full_desktop` as the name of the targeted qube:

1. Disable qubes os xorg config, set a password:

  .. code:: console

    [user@dom0 ~]$ qvm-run -u root full_desktop -- 'echo "user" | passwd --stdin user'
    [user@dom0 ~]$ qvm-run -u root full_desktop -- systemctl set-default graphical.target

  .. TODO: try fixing fedora autologin

2. Configure qube preferences

  .. code:: console

    [user@dom0 ~]$ qvm-features --unset full_desktop gui
    [user@dom0 ~]$ qvm-prefs full_desktop virt_mode hvm
    [user@dom0 ~]$ qvm-prefs full_desktop kernel ''
    [user@dom0 ~]$ qvm-prefs full_desktop memory 1000
    [user@dom0 ~]$ qvm-service full_desktop lightdm on

  Lightdm service disables seamless mode by preventing qubes-gui-agent from starting and starts lightdm display manager.

  Kernel option :code:`systemd.unit` overrides the default boot target.

3. Restart the qube for changes to take effect

Revert to seamless mode on Fedora guest
---------------------------------------
