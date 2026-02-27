============================
How to disable seamless mode
============================

.. warning::

      This page is intended for advanced users.

.. note::

  This document is about Linux virtual machines integrated into QubesOS. For Windows refer to :ref:`Qubes Windows Tools documentation <user/templates/windows/qubes-windows-tools:Using Windows AppVMs in seamless mode>`

By default, vm applications are seamlessly integrated into dom0's desktop environment. This article explains how to disable seamless mode in order to get separate desktop inside of an otherwise integrated vm.

Visually, it turns this:

|seamless_mode|


Into this:

|non-seamless_mode|


VNC is better
-------------

While it is possible to disable seamless desktop integration, at the moment of writing (2026-02) different approach is often considered superior: setting up VNC server and client in the same vm. It also provides a separate desktop in a vm, but doesn't require setting specific properties, behaves better than the default qubes vm viewer, and doesn't reduce integration (such as inter-qube clipboard) in any way.

See the following topics on using VNC:

- `original instruction by unman <https://forum.qubes-os.org/t/automatic-startup-of-gnome-environement/26526/25>`__
- `most recent discussion containing information about this <https://forum.qubes-os.org/t/rejecting-hard-work-of-qubes-os-developers-gui-integration/38817/7>`__

Overview
--------

In its simplest form disabling seamless mode is done by disabling or stopping :code:`qubes-gui-agent` service of a qube, but it doesn't provide any graphical interface as a replacement.

Graphical viewer window for a qube is displayed when the feature :code:`gui` is unset and virtualization mode set to :code:`hvm`. This defaults to using emulated VGA output. To explicitly tell QubesOS to use VGA output, set :code:`gui-emulated` to 1.

.. note::

   For more detailed explanation of this behavior see :code:`gui` and :code:`gui-emulated` features in the "LIST OF KNOWN FEATURES" section of :code:`qvm-features` manual.

Moreover, debian and fedora hosts don't run desktop environment unless they are configured to do so, for example by setting :code:`graphical.target` as the default for systemd to boot into.

.. hint::

   You might need to provision more initial memory to your qubes in order for them to boot.

Limitations
^^^^^^^^^^^

Inter-qube clipboard feature relies on :code:`qubes-gui-agent`. It does not work when seamless mode is off.

Following procedures of handling seamless mode are nothing more than examples, working with default xfce templates provided by Qubes. Actual workflow can differ depending on your configuration and personal preferences. Be prepared to troubleshoot display manager and X server if something goes wrong.

Disable seamless mode on Debian guest
-------------------------------------

In terminal, with :code:`full_desktop` as the name of the targeted qube:

1. Configure qube preferences

  .. code:: console

    [user@dom0 ~]$ qvm-features full_desktop gui-emulated 1
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

    [user@dom0 ~]$ qvm-features --unset full_desktop gui-emulated
    [user@dom0 ~]$ qvm-prefs -D full_desktop virt_mode
    [user@dom0 ~]$ qvm-prefs -D full_desktop kernelopts
    [user@dom0 ~]$ qvm-service -D full_desktop lightdm


Fedora guest
------------

Qubes 4.2
^^^^^^^^^

Disable seamless mode
"""""""""""""""""""""

In terminal, with :code:`full_desktop` as the name of the targeted qube:

1. Set a password:

  .. code:: console

    [root@full_desktop ~]# passwd user
    New password: 
    Retype new password: 
    passwd: password updated successfully

  Set any non-empty password. It is required to log in. Alternatively, configure lightdm autologin.

  .. hint::

    If your goal is non-seamless mode in an AppVM with no template modification, you might be interested in persisting configuration changes using :doc:`bind-dirs </user/advanced-topics/bind-dirs>` or :doc:`adding a script to rc.local.d </user/advanced-topics/config-files>`

2. Note kernel cmdline of :code:`full_desktop` qube, you will need them in the next step:

  .. code:: console

    [user@full_desktop ~]$ cat /proc/cmdline
    root=/dev/mapper/dmroot ro nomodeset console=hvc0 rd_NO_PLYMOUTH rd.plymouth.enable=0 plymouth.enable=0 clocksource=tsc xen_scrub_pages=0 swiotlb=2048 selinux=1 security=selinux

2. Configure qube preferences:

  Replace :code:`$kernel_options` with the options you have acquired from :code:`/proc/cmdline`, but omit :code:`nomodeset`

  .. code:: console

    [user@dom0 ~]$ qvm-features full_desktop gui-emulated 1
    [user@dom0 ~]$ qvm-features full_desktop no-default-kernelopts 1
    [user@dom0 ~]$ qvm-prefs full_desktop virt_mode hvm
    [user@dom0 ~]$ qvm-prefs full_desktop memory 1000
    [user@dom0 ~]$ qvm-prefs full_desktop kernelopts "$kernel_options systemd.unit=graphical.target"
    [user@dom0 ~]$ qvm-service full_desktop lightdm on

  Lightdm service disables seamless mode by preventing qubes-gui-agent from starting and starts lightdm display manager.

  Kernel option :code:`systemd.unit` overrides the default boot target.

3. Restart the qube for changes to take effect

Revert back to seamless mode
""""""""""""""""""""""""""""

To revert, simply undo the configuration changes:

  .. code:: console

    [user@dom0 ~]$ qvm-features --unset full_desktop gui-emulated
    [user@dom0 ~]$ qvm-features --unset full_desktop no-default-kernelopts
    [user@dom0 ~]$ qvm-prefs -D full_desktop virt_mode
    [user@dom0 ~]$ qvm-prefs -D full_desktop kernelopts
    [user@dom0 ~]$ qvm-service -D full_desktop lightdm


Qubes 4.3
^^^^^^^^^

Disable seamless mode
"""""""""""""""""""""

In terminal, with :code:`full_desktop` as the name of the targeted qube:

1. Set a password:

  .. code:: console

    [root@full_desktop ~]# passwd user
    New password: 
    Retype new password: 
    passwd: password updated successfully

  Set any non-empty password. It is required to log in. Alternatively, configure lightdm autologin.

  .. hint::

    If your goal is non-seamless mode in an AppVM with no template modification, you might be interested in persisting configuration changes using :doc:`bind-dirs </user/advanced-topics/bind-dirs>` or :doc:`adding a script to rc.local.d </user/advanced-topics/config-files>`

2. Configure qube preferences:

  .. code:: console

    [user@dom0 ~]$ qvm-features full_desktop gui-emulated 1
    [user@dom0 ~]$ qvm-features full_desktop no-nomodeset 1
    [user@dom0 ~]$ qvm-prefs full_desktop virt_mode hvm
    [user@dom0 ~]$ qvm-prefs full_desktop memory 1000
    [user@dom0 ~]$ qvm-prefs full_desktop kernelopts "systemd.unit=graphical.target"
    [user@dom0 ~]$ qvm-service full_desktop lightdm on

  Lightdm service disables seamless mode by preventing qubes-gui-agent from starting and starts lightdm display manager.

  Kernel option :code:`systemd.unit` overrides the default boot target.

3. Restart the qube for changes to take effect

Revert back to seamless mode
""""""""""""""""""""""""""""

To revert, simply undo the configuration changes:

  .. code:: console

    [user@dom0 ~]$ qvm-features --unset full_desktop gui-emulated
    [user@dom0 ~]$ qvm-features --unset full_desktop no-nomodeset
    [user@dom0 ~]$ qvm-prefs -D full_desktop virt_mode
    [user@dom0 ~]$ qvm-prefs -D full_desktop kernelopts
    [user@dom0 ~]$ qvm-service -D full_desktop lightdm


.. |seamless_mode| image:: /attachment/doc/seamless_mode.png
  :alt: VM applications in seamless mode - vm applications displayed as separate windows in dom0's desktop environment
.. |non-seamless_mode| image:: /attachment/doc/non-seamless_mode.png
  :alt: VM in non-seamless mode - running its own xfce desktop environment
