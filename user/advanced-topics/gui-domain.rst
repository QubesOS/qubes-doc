==========
GUI domain
==========

.. warning::

      This page is intended for advanced users.

On this page, we describe how to set up a :website:`GUI domain <news/2020/03/18/gui-domain/>`. In all the cases, the base underlying TemplateVM used is ``Fedora`` with ``XFCE`` flavor to match current desktop choice in ``dom0``. That can be adapted very easily for other desktops and templates. By default, the configured GUI domain is a management qube with global admin permissions ``rwx`` but can be adjusted to ``ro`` (see :website:`Introducing the Qubes Admin API <news/2017/06/27/qubes-admin-api/>`) in pillar data of the corresponding GUI domain to setup. For example, pillar data for ``sys-gui`` located at ``/srv/pillar/base/qvm/sys-gui.sls``. Please note that each GUI domain has no ``NetVM``.

   **Note:** The setup is done using ``SaltStack`` formulas with the ``qubesctl`` tool. When executing it, apply step can take time because it needs to download latest Fedora XFCE TemplateVM and install desktop dependencies.

Hybrid GUI domain (``sys-gui``)
-------------------------------


Here, we describe how to setup ``sys-gui`` that we call *hybrid mode* or referenced as a *compromise solution* in :website:`GUI domain <news/2020/03/18/gui-domain/>`.

|sys-gui|

In ``dom0``, enable the formula for ``sys-gui`` with pillar data:

.. code:: bash

      sudo qubesctl top.enable qvm.sys-gui
      sudo qubesctl top.enable qvm.sys-gui pillar=True


then, execute it:

.. code:: bash

      sudo qubesctl --all state.highstate


You can now disable the ``sys-gui`` formula:

.. code:: bash

      sudo qubesctl top.disable qvm.sys-gui


At this point, you need to shutdown all your running qubes as the ``default_guivm`` qubes global property has been set to ``sys-gui``. In order to use ``sys-gui`` as GUI domain, you need to logout and, in the top right corner, select ``lightdm`` session type to **GUI domain (sys-gui)**. Once logged, you are running ``sys-gui`` as fullscreen window and you can perform any operation as if you would be in ``dom0`` desktop.

   **Note:** In order to go back to ``dom0`` desktop, you need to logout and then, select ``lightdm`` session to *Session Xfce*.

GPU GUI domain (``sys-gui-gpu``)
--------------------------------


Here, we describe how to setup ``sys-gui-gpu`` which is a GUI domain with *GPU passthrough* in :website:`GUI domain <news/2020/03/18/gui-domain/>`.

   **Note:** the purpose of ``sys-gui-gpu`` is to improve Qubes OS security by detaching the GPU from dom0, this is not intended to improve GPU related performance within qubes, and this will not improve performance.

|sys-gui-gpu|

In ``dom0``, enable the formula for ``sys-gui-gpu`` with pillar data:

.. code:: bash

      sudo qubesctl top.enable qvm.sys-gui-gpu
      sudo qubesctl top.enable qvm.sys-gui-gpu pillar=True


then, execute it:

.. code:: bash

      sudo qubesctl --all state.highstate


You can now disable the ``sys-gui-gpu`` formula:

.. code:: bash

      sudo qubesctl top.disable qvm.sys-gui-gpu


One more step is needed: attaching the actual GPU to ``sys-gui-gpu``. This can be done either manually via ``qvm-pci`` (remember to enable permissive option), or via:

.. code:: bash

      sudo qubesctl state.sls qvm.sys-gui-gpu-attach-gpu


The latter option assumes Intel graphics card (it has hardcoded PCI address). If you don’t have Intel graphics card, please use the former method with ``qvm-pci`` (see :doc:`How to use PCI devices </user/how-to-guides/how-to-use-pci-devices>`).

   **Note:** Some platforms can have multiple GPU. For example on laptops, it is usual to have HDMI or DISPLAY port linked to the secondary GPU (generally called *discrete GPU*). In such case, you have to also attach the secondary GPU to ``sys-gui-gpu`` with permissive option.

At this point, you need to reboot your Qubes OS machine in order to boot into ``sys-gui-gpu``.

   **Note:** For some platforms, it can be sufficient to shutdown all the running qubes and starting ``sys-gui-gpu``. Unfortunately, it has been observed that detaching and attaching some GPU cards from ``dom0`` to ``sys-gui-gpu`` can freeze computer. We encourage reboot to prevent any data loss.

Once, ``lightdm`` is started, you can log as ``user`` where ``user`` refers to the first ``dom0`` user in ``qubes`` group and with corresponding ``dom0`` password. A better approach for handling password is currently discussed in :issue:`QubesOS/qubes-issues#6740 <6740>`.

VNC GUI domain (``sys-gui-vnc``)
--------------------------------


Here, we describe how to setup ``sys-gui-vnc`` that we call a *remote* GUI domain or referenced as *with a virtual server* in :website:`GUI domain <news/2020/03/18/gui-domain/>`.

|sys-gui-vnc|

In ``dom0``, enable the formula for ``sys-gui-vnc`` with pillar data:

.. code:: bash

      sudo qubesctl top.enable qvm.sys-gui-vnc
      sudo qubesctl top.enable qvm.sys-gui-vnc pillar=True


then, execute it:

.. code:: bash

      sudo qubesctl --all state.highstate


You can now disable the ``sys-gui-vnc`` formula:

.. code:: bash

      sudo qubesctl top.disable qvm.sys-gui-vnc


At this point, you need to shutdown all your running qubes as the ``default_guivm`` qubes global property has been set to ``sys-gui-vnc``. Then, you can start ``sys-gui-vnc``:

.. code:: bash

      qvm-start sys-gui-vnc


A VNC server session is running on ``localhost:5900`` in ``sys-gui-vnc``. In order to reach the ``VNC`` server, we encourage to not connect ``sys-gui-vnc`` to a ``NetVM`` but rather to use another qube for remote access, say ``sys-remote``. First, you need to bind port 5900 of ``sys-gui-vnc`` into a ``sys-remote`` local port (you may want to use another port than 5900 to reach ``sys-remote`` from the outside). For that, use ``qubes.ConnectTCP`` RPC service (see :doc:`Firewall </user/security-in-qubes/firewall>`. Then, you can use any ``VNC`` client to connect to you ``sys-remote`` on the chosen local port (5900 if you kept the default one). For the first connection, you will reach ``lightdm`` for which you can log as ``user`` where ``user`` refers to the first ``dom0`` user in ``qubes`` group and with corresponding ``dom0`` password.

   **Note:** ``lightdm`` session remains logged even if you disconnect your ``VNC`` client. Ensure to lock or log out before disconnecting your ``VNC`` client session.

   **WARNING**: This setup raises multiple security issues: 1) Anyone who can reach the ``VNC`` server, can take over the control of the Qubes OS machine, 2) A second client can connect even if a connection is already active and potentially get disconnected, 3) You can get disconnected by some unrelated network issues. Generally, if this ``VNC`` server is exposed to open network, it must be protected with some other (cryptographic) layer like ``VPN``. The setup as is, is useful only for purely testing machine.

Known issues
------------


Application menu lacks qubes entries in a fresh GUI domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


See :issue:`QubesOS/qubes-issues#5804 <5804>`

Cannot update dom0 from sys-gui
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


See :issue:`QubesOS/qubes-issues#8934 <8934>`

GUI of HVM qubes not visible
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


See :issue:`QubesOS/qubes-issues#9385 <9385>`

Power saving/screensaver issues
-------------------------------


See :issue:`QubesOS/qubes-issues#9033 <9033>`, :issue:`QubesOS/qubes-issues#9384 <9384>`, :issue:`QubesOS/qubes-issues#7989 <7989>`

Qube startup order (sys-usb and sys-gui)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


See :issue:`QubesOS/qubes-issues#7954 <7954>`

Other GUI domain issues
^^^^^^^^^^^^^^^^^^^^^^^


see existing issues ``QubesOS/qubes-issues`` under `C: gui-domain <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+gui-domain%22>`__ label.

Reverting sys-gui
-----------------


The following commands have to be run in ``dom0``.

   **Note:** For the case of ``sys-gui-gpu``, you need to prevent Qubes OS autostart of any qube to reach ``dom0``. For that, you need to boot Qubes OS with ``qubes.skip_autostart`` GRUB parameter.

Set ``default_guivm`` as ``dom0``:

.. code:: bash

      qubes-prefs default_guivm dom0


and for every selected qubes not using default value for GUI domain property, for example with a qube ``personal``:

.. code:: bash

      qvm-prefs personal guivm dom0


You are now able to delete the GUI domain, for example ``sys-gui-gpu``:

.. code:: bash

      qvm-remove -f sys-gui-gpu


.. |sys-gui| image:: /attachment/posts/guivm-hybrid.png
   

.. |sys-gui-gpu| image:: /attachment/posts/guivm-gpu.png
   

.. |sys-gui-vnc| image:: /attachment/posts/guivm-vnc.png
   
