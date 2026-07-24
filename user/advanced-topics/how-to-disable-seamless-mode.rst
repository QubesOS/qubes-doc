============================
How to disable seamless mode
============================

.. warning::

      This page is intended for advanced users.

.. note::

  This document is about Linux qubes integrated into Qubes OS. For Windows refer to :ref:`Qubes Windows Tools documentation <user/templates/windows/qubes-windows-tools:Using Windows AppVMs in seamless mode>`.

By default, qube applications are seamlessly integrated into dom0's desktop environment. This article explains how to disable seamless mode in order to get separate desktop inside of an otherwise integrated qube.

Visually, it turns this:

|seamless_mode|


Into this:

|non-seamless_mode|


.. admonition:: Consider VNC as an alternative

    While it is possible to disable seamless desktop integration, depending on your circumstance setting up VNC server and client in the same qube might turn out to be a better approach. It also provides a separate desktop, but doesn't require setting specific properties, behaves better than the default qube viewer, and doesn't reduce integration (such as inter-qube clipboard) in any way.

    Consult the operating system of the qube and VNC distribution documentation on using VNC.


Overview
--------

In its simplest form disabling seamless mode is done by disabling or stopping :code:`qubes-gui-agent` service of a qube, but it doesn't provide any graphical interface as a replacement.

Graphical viewer window for a qube is displayed when the feature `gui <https://dev.qubes-os.org/projects/core-admin-client/en/latest/manpages/qvm-features.html#gui>`__ is unset and virtualization mode set to :code:`hvm`. This defaults to using emulated VGA output. To explicitly tell Qubes OS to use VGA output, set `gui-emulated <https://dev.qubes-os.org/projects/core-admin-client/en/latest/manpages/qvm-features.html#gui-emulated>`__ to 1.

Moreover, Debian and Fedora hosts don't run desktop environment unless they are configured to do so, for example by setting :code:`graphical.target` as the default for systemd to boot into.

Limitations
^^^^^^^^^^^

Inter-qube clipboard feature relies on :code:`qubes-gui-agent`. It does not work when seamless mode is off.

Disable seamless mode
---------------------

Following procedure of handling seamless mode is nothing more than an example, working with qubes derived from xfce and gnome templates provided by Qubes. Actual workflow can differ depending on your configuration and personal preferences. Be prepared to troubleshoot display manager and X server if something goes wrong.

Regardless of what qubes you use you also need the desktop environment you want to run installed on the system. This may seem obvious at first, but can turn out out tricky in reality. For example, Fedora 43 template doesn't actually come with Gnome installed, just certain Gnome applications.

You might need to set a user password as most desktop environments are not designed to work without one. Alternatively, you could configure autologin. Consult relevant documentation if you choose to do this instead.

.. hint::

    If your goal is non-seamless mode in an app qube with no template modification, you might be interested in persisting configuration changes using :doc:`bind-dirs </user/advanced-topics/bind-dirs>` or :doc:`adding a script to rc.local.d </user/advanced-topics/config-files>`.

In terminal, with :code:`full-desktop-qube` as the name of the targeted qube:

1. In targeted qube terminal (or relevant template if your target is AppVM or DispVM), set a password:

  .. code:: console

    [root@full-desktop-qube ~]# passwd user
    New password: 
    Retype new password: 
    passwd: password updated successfully

2. In dom0 terminal, configure qube preferences:

  .. code:: console

    [user@dom0 ~]$ qvm-features full-desktop-qube gui-emulated 1
    [user@dom0 ~]$ qvm-features full-desktop-qube no-nomodeset 1
    [user@dom0 ~]$ qvm-prefs full-desktop-qube virt_mode hvm
    [user@dom0 ~]$ qvm-prefs full-desktop-qube kernelopts "systemd.unit=graphical.target"
    [user@dom0 ~]$ qvm-service full-desktop-qube lightdm on

  :code:`lightdm` service disables seamless mode by preventing :code:`qubes-gui-agent` from starting and starts a display manager.

  Kernel option :code:`systemd.unit` overrides the default boot target.

  .. hint::

   You might need to provision more initial memory in this step in order for :code:`full-desktop-qube` to boot.

3. Restart the qube for changes to take effect

Revert to seamless mode
-----------------------

To revert, simply undo relevant configuration changes in dom0 terminal:

  .. code:: console

    [user@dom0 ~]$ qvm-features --unset full-desktop-qube gui-emulated
    [user@dom0 ~]$ qvm-features --unset full-desktop-qube no-nomodeset
    [user@dom0 ~]$ qvm-prefs -D full-desktop-qube virt_mode
    [user@dom0 ~]$ qvm-prefs -D full-desktop-qube kernelopts
    [user@dom0 ~]$ qvm-service -D full-desktop-qube lightdm

.. |seamless_mode| image:: /attachment/doc/seamless_mode.png
  :alt: Qube applications in seamless mode - qube applications displayed as separate windows in dom0's desktop environment
.. |non-seamless_mode| image:: /attachment/doc/non-seamless_mode.png
  :alt: Qube in non-seamless mode - running its own xfce desktop environment

Troubleshooting
---------------

You can access CLI of qubes with broken GUI using :code:`qvm-console-dispvm`.

Failures to start display managers and X server are logged, see:

- X server: :code:`/var/log/Xorg.*.log`
- LightDM: :code:`/var/log/lightdm/`
- GDM: :code:`/var/log/gdm/`

Common failures and solutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Graphical viewer window does not appear
"""""""""""""""""""""""""""""""""""""""

Ensure :code:`gui-emulated` feature is enabled and :code:`virt_mode` is set to :code:`hvm`.

Viewer window appears, but there in no desktop / login window
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Ensure :code:`no-nomodeset` feature is enabled.

Make sure you are using a kernel provided by Qubes. Qubes kernel preferences do not affect distribution kernels. Alternatively, set required kernel options inside qube using conventional methods.
        
Make sure the operating system of the qube is configured to start a desktop environment.

Check display manager status. Replace :code:`$service` with :code:`lightdm` on xfce and :code:`gdm` on gnome:

.. code:: console

    [user@full-desktop-qube ~]$ systemctl status $service

If it reports problems or exits soon after starting inspect relevant logs for errors. Common log file locations:

- X server: :code:`/var/log/Xorg.*.log`
- LightDM: :code:`/var/log/lightdm/`
- GDM: :code:`/var/log/gdm/`

Qube failed to start: Cannot connect to qrexec agent...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

Try to provision more memory to the qube. Default 400 MiB might not be enough.


.. code:: console

    [user@dom0 ~]$ qvm-prefs full-desktop-qube memory 1000

LightDM autologin does not work on fedora xfce qubes
""""""""""""""""""""""""""""""""""""""""""""""""""""

Set a password if you haven't and log in via lightdm graphical interface. Autologin starts working after you log in manually at least once.
