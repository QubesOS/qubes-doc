============================
How to disable seamless mode
============================

.. warning::

      This page is intended for advanced users.

.. note::

  This document is about Linux qubes integrated into Qubes OS. For Windows refer to :ref:`Qubes Windows Tools documentation <user/templates/windows/qubes-windows-tools:Using Windows AppVMs in seamless mode>`

By default, qube applications are seamlessly integrated into dom0's desktop environment. This article explains how to disable seamless mode in order to get separate desktop inside of an otherwise integrated qube.

Visually, it turns this:

|seamless_mode|


Into this:

|non-seamless_mode|


VNC is better
-------------

While it is possible to disable seamless desktop integration, at the moment of writing (2026-02) different approach is often considered superior: setting up VNC server and client in the same qube. It also provides a separate desktop in a qube, but doesn't require setting specific properties, behaves better than the default qube viewer, and doesn't reduce integration (such as inter-qube clipboard) in any way.

Consult qube's OS and VNC distribution documentation on using VNC:

- `Fedora user documentation <https://docs.fedoraproject.org/en-US/fedora/f36/install-guide/advanced/VNC_Installations/>`__
- `Debian community wiki <https://wiki.debian.org/?action=fullsearch&value=vnc&titlesearch=Titles>`__
- `Manual page of a vnc server at manpages.debian.org <https://manpages.debian.org/trixie/tightvncserver/Xtightvnc.1.en.html>`__


Overview
--------

In its simplest form disabling seamless mode is done by disabling or stopping :code:`qubes-gui-agent` service of a qube, but it doesn't provide any graphical interface as a replacement.

Graphical viewer window for a qube is displayed when the feature `gui <https://dev.qubes-os.org/projects/core-admin-client/en/latest/manpages/qvm-features.html#gui>`__ is unset and virtualization mode set to :code:`hvm`. This defaults to using emulated VGA output. To explicitly tell Qubes OS to use VGA output, set `gui-emulated <https://dev.qubes-os.org/projects/core-admin-client/en/latest/manpages/qvm-features.html#gui-emulated>`__ to 1.

Moreover, Debian and Fedora hosts don't run desktop environment unless they are configured to do so, for example by setting :code:`graphical.target` as the default for systemd to boot into.

.. hint::

   You might need to provision more initial memory to your qubes in order for them to boot.

Limitations
^^^^^^^^^^^

Inter-qube clipboard feature relies on :code:`qubes-gui-agent`. It does not work when seamless mode is off.

Following procedures of handling seamless mode are nothing more than examples, working with default xfce templates provided by Qubes. Actual workflow can differ depending on your configuration and personal preferences. Be prepared to troubleshoot display manager and X server if something goes wrong.

Disable seamless mode on Debian guest
-------------------------------------

In terminal, with :code:`FULL_DESKTOP` as the name of the targeted qube:

1. Configure qube preferences

  .. code:: console

    [user@dom0 ~]$ qvm-features FULL_DESKTOP gui-emulated 1
    [user@dom0 ~]$ qvm-prefs FULL_DESKTOP virt_mode hvm
    [user@dom0 ~]$ qvm-prefs FULL_DESKTOP memory 1000
    [user@dom0 ~]$ qvm-prefs FULL_DESKTOP kernelopts "systemd.unit=graphical.target"
    [user@dom0 ~]$ qvm-service FULL_DESKTOP lightdm on

  Lightdm service disables seamless mode by preventing qubes-gui-agent from starting and starts LightDM display manager.

  Kernel option :code:`systemd.unit` overrides the default boot target.

2. Restart the qube for changes to take effect

Revert to seamless mode on Debian guest
---------------------------------------

To revert, simply undo the configuration changes:

  .. code:: console

    [user@dom0 ~]$ qvm-features --unset FULL_DESKTOP gui-emulated
    [user@dom0 ~]$ qvm-prefs -D FULL_DESKTOP virt_mode
    [user@dom0 ~]$ qvm-prefs -D FULL_DESKTOP kernelopts
    [user@dom0 ~]$ qvm-service -D FULL_DESKTOP lightdm


Fedora guest
------------

Qubes 4.2
^^^^^^^^^

Disable seamless mode
"""""""""""""""""""""

In terminal, with :code:`FULL_DESKTOP` as the name of the targeted qube:

1. Set a password:

  .. code:: console

    [root@FULL_DESKTOP ~]# passwd user
    New password: 
    Retype new password: 
    passwd: password updated successfully

  Set any non-empty password. It is required to log in. Alternatively, `configure LightDM autologin <https://wiki.archlinux.org/title/LightDM#Enabling_autologin>`__.

  .. hint::

    If your goal is non-seamless mode in an app qube with no template modification, you might be interested in persisting configuration changes using :doc:`bind-dirs </user/advanced-topics/bind-dirs>` or :doc:`adding a script to rc.local.d </user/advanced-topics/config-files>`

2. Note kernel cmdline of :code:`FULL_DESKTOP` qube, you will need them in the next step:

  .. code:: console

    [user@FULL_DESKTOP ~]$ cat /proc/cmdline
    root=/dev/mapper/dmroot ro nomodeset console=hvc0 rd_NO_PLYMOUTH rd.plymouth.enable=0 plymouth.enable=0 clocksource=tsc xen_scrub_pages=0 swiotlb=2048 selinux=1 security=selinux

2. Configure qube preferences:

  Replace :code:`$kernel_options` with the options you have acquired from :code:`/proc/cmdline`, but omit :code:`nomodeset`

  .. code:: console

    [user@dom0 ~]$ qvm-features FULL_DESKTOP gui-emulated 1
    [user@dom0 ~]$ qvm-features FULL_DESKTOP no-default-kernelopts 1
    [user@dom0 ~]$ qvm-prefs FULL_DESKTOP virt_mode hvm
    [user@dom0 ~]$ qvm-prefs FULL_DESKTOP memory 1000
    [user@dom0 ~]$ qvm-prefs FULL_DESKTOP kernelopts "$kernel_options systemd.unit=graphical.target"
    [user@dom0 ~]$ qvm-service FULL_DESKTOP lightdm on

  Lightdm service disables seamless mode by preventing qubes-gui-agent from starting and starts LightDM display manager.

  Kernel option :code:`systemd.unit` overrides the default boot target.

3. Restart the qube for changes to take effect

Revert back to seamless mode
""""""""""""""""""""""""""""

To revert, simply undo the configuration changes:

  .. code:: console

    [user@dom0 ~]$ qvm-features --unset FULL_DESKTOP gui-emulated
    [user@dom0 ~]$ qvm-features --unset FULL_DESKTOP no-default-kernelopts
    [user@dom0 ~]$ qvm-prefs -D FULL_DESKTOP virt_mode
    [user@dom0 ~]$ qvm-prefs -D FULL_DESKTOP kernelopts
    [user@dom0 ~]$ qvm-service -D FULL_DESKTOP lightdm


Qubes 4.3
^^^^^^^^^

Disable seamless mode
"""""""""""""""""""""

In terminal, with :code:`FULL_DESKTOP` as the name of the targeted qube:

1. Set a password:

  .. code:: console

    [root@FULL_DESKTOP ~]# passwd user
    New password: 
    Retype new password: 
    passwd: password updated successfully

  Set any non-empty password. It is required to log in. Alternatively, `configure LightDM autologin <https://wiki.archlinux.org/title/LightDM#Enabling_autologin>`__.

  .. hint::

    If your goal is non-seamless mode in an app qube with no template modification, you might be interested in persisting configuration changes using :doc:`bind-dirs </user/advanced-topics/bind-dirs>` or :doc:`adding a script to rc.local.d </user/advanced-topics/config-files>`

2. Configure qube preferences:

  .. code:: console

    [user@dom0 ~]$ qvm-features FULL_DESKTOP gui-emulated 1
    [user@dom0 ~]$ qvm-features FULL_DESKTOP no-nomodeset 1
    [user@dom0 ~]$ qvm-prefs FULL_DESKTOP virt_mode hvm
    [user@dom0 ~]$ qvm-prefs FULL_DESKTOP memory 1000
    [user@dom0 ~]$ qvm-prefs FULL_DESKTOP kernelopts "systemd.unit=graphical.target"
    [user@dom0 ~]$ qvm-service FULL_DESKTOP lightdm on

  Lightdm service disables seamless mode by preventing qubes-gui-agent from starting and starts lightdm display manager.

  Kernel option :code:`systemd.unit` overrides the default boot target.

3. Restart the qube for changes to take effect

Revert back to seamless mode
""""""""""""""""""""""""""""

To revert, simply undo the configuration changes:

  .. code:: console

    [user@dom0 ~]$ qvm-features --unset FULL_DESKTOP gui-emulated
    [user@dom0 ~]$ qvm-features --unset FULL_DESKTOP no-nomodeset
    [user@dom0 ~]$ qvm-prefs -D FULL_DESKTOP virt_mode
    [user@dom0 ~]$ qvm-prefs -D FULL_DESKTOP kernelopts
    [user@dom0 ~]$ qvm-service -D FULL_DESKTOP lightdm


.. |seamless_mode| image:: /attachment/doc/seamless_mode.png
  :alt: Qube applications in seamless mode - qube applications displayed as separate windows in dom0's desktop environment
.. |non-seamless_mode| image:: /attachment/doc/non-seamless_mode.png
  :alt: Qube in non-seamless mode - running its own xfce desktop environment
