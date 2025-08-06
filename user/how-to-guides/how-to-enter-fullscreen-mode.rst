============================
How to enter fullscreen mode
============================

The easiest ways to enter fullscreen mode are:

* **With a mouse**: *right-click* on a window title, then click on :guilabel:`Fullscreen`
* **With a keyboard**: press :kbd:`Alt` + :kbd:`Space` and select :guilabel:`Fullscreen` (or type :kbd:`F`)
* **With a keyboard shortcut**: press :kbd:`Alt` + :kbd:`F11`

This page discusses the security implications of fullscreen mode and alternate solutions to allow fullscreen mode.

What is fullscreen mode?
------------------------

Normally, the Qubes GUI virtualization daemon restricts any qube from ”owning” the full screen, ensuring that there are always clearly marked decorations drawn by the trusted Window Manager around each of the qubes windows. This allows the user to easily realize to which domain a specific window belongs.

.. image:: /attachment/doc/r4.0-xfce-three-domains-at-work.png

Why is fullscreen mode potentially dangerous?
---------------------------------------------

If one allowed a qube to “own” the full screen, e.g. to show a movie on a full screen, it might not be possible for the user to know if the application or the qube really “released” the full screen, or if it has started emulating the whole desktop and is pretending to be the trusted Window Manager, drawing shapes on the screen that look like other windows, belonging to other domains (e.g. to trick the user into entering a secret passphrase into a window that looks like belonging to some trusted domain).

That's why fullscreen mode is not allowed by default, when requested from a qube.

.. _secure-use-of-fullscreen-mode:

Secure use of fullscreen mode
-----------------------------

However, it is possible to deal with fullscreen mode in a secure way assuming there are mechanisms that can be used at any time to switch between windows or show the full desktop and that cannot be intercepted by the qube. The simplest example is the use of :kbd:`Alt` + :kbd:`Tab` for switching between windows, which is a shortcut handled by dom0.

Other examples of such mechanisms are the KDE “Present Windows” and “Desktop Grid” effects, which are similar to Mac’s “Expose” effect, and which can be used to immediately detect potential “GUI forgery”, as they cannot be intercepted by any of the qube (as the GUID never passes down the key combinations that got consumed by KDE Window Manager), and so the qube cannot emulate those. Those effects are enabled by default in KDE once Compositing gets enabled in KDE (:menuselection:`System Settings --> Desktop --> Enable Desktop Effects`), which is recommended anyway. By default, they are triggered by the :kbd:`Ctrl` + :kbd:`F8` and :kbd:`Ctrl` + :kbd:`F9` key combinations, but can also be reassigned to other shortcuts.

Safely enabling fullscreen mode for a selected window
-----------------------------------------------------

You can always put a window into fullscreen mode in Xfce4 using the trusted window manager by right-clicking on a window’s title bar and selecting :guilabel:`Fullscreen` or pressing :kbd:`Alt` + :kbd:`F11`. This functionality should still be considered safe, since a qube window still can’t voluntarily enter fullscreen mode. The user must select this option from the trusted window manager in dom0. To exit fullscreen mode from here, press :kbd:`Alt` + :kbd:`Space` to bring up the title bar menu again, then select :guilabel:`Leave Fullscreen` or simply press :kbd:`Alt` + :kbd:`F11`. For :ref:`standalone HVMs <user/reference/glossary:HVM>`, you should set the screen resolution in the qube to that of the host, (or larger), *before* setting fullscreen mode in Xfce4.

Enabling fullscreen mode from a selected qube
---------------------------------------------

.. warning:: Be sure to read :ref:`secure-use-of-fullscreen-mode` first.

As an alternative to the Xfce4 method, you can enable fullscreen mode for selected qubes by using the `gui-allow-fullscreen <https://dev.qubes-os.org/projects/core-admin-client/en/latest/manpages/qvm-features.html#gui-gui-default>`__ feature of a qube.

Be sure to restart the qube after modifying this feature, for the changes to take effect.

With the qube's settings
^^^^^^^^^^^^^^^^^^^^^^^^

In the qube's settings, go to the second tab, called :guilabel:`Advanced`. Under :guilabel:`Window options`, change the value of :guilabel:`Allow fullscreen`, from :guilabel:`(use system default) (current)` to :guilabel:`disallow`.

With the command-line, targeting the qube
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In dom0, run the following command, replacing :samp:`{<QUBE_NAME>}` by the actual name of the qube:

.. code:: console

   [user@dom0] $ qvm-features <QUBE_NAME> gui-allow-fullscreen 1

Enabling fullscreen mode for every qubes
----------------------------------------

.. warning:: Be sure to read :ref:`secure-use-of-fullscreen-mode` first.

With Qubes Global Config
^^^^^^^^^^^^^^^^^^^^^^^^

Open :guilabel:`Qubes Global Config`. In the first tab (called :guilabel:`General settings`), under the :guilabel:`Window management`: section, change the value of :guilabel:`Fullscreen mode`, from :guilabel:`default (disallow)` to :guilabel:`allow`.

With the command-line, on dom0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In dom0, run the following command:

.. code:: console

   [user@dom0] $ qvm-features dom0 gui-default-allow-fullscreen 1

