===========================================
How to take screenshots and set a wallpaper
===========================================

In Qubes OS, :term:`dom0` is strongly isolated from the outside world. It has no direct internet connection (for updates, a dedicated UpdateProxy is used to avoid interacting with untrusted data) and copying files into it is highly discouraged and not supported by tools such as ``qvm-copy``.

:term:`dom0` is also where the desktop environment and Qubes OS GUI tools are running (unless you are using the experimental :doc:`sys-gui</user/advanced-topics/gui-domain>`, thus, if you take a screenshot or want to set a wallpaper, you will be acting within :term:`dom0`.


Taking screenshots
------------------

In default Qubes OS installation, you can use the default XFCE screenshot tool (called Screenshot), either running it from the Qubes OS menu or using the :kbd:`PrintScreen` key.

.. figure:: /attachment/doc/howto-screenshot-1.png
   :alt: image of Qubes Menu with the page for Other tools open and the Screenshot tool highlighted
   :align: center
|
.. figure:: /attachment/doc/howto-screenshot-2.png
   :alt: image of the default XFCE screenshot tool
   :align: center

The file will be saved in :term:`dom0`, so you need to copy it out of :term:`dom0` if you want to use it in any other qube. The easiest way to do it is with the ``qvm-copy-to-vm`` tool in :term:`dom0` terminal:

.. code:: console

    $ qvm-copy-to-vm qube-name Pictures/screenshot_name.jpg

Copying files out of :term:`dom0` is generally safe for your system.

Setting a wallpaper
-------------------

As mentioned, all desktop environment tools run in :term:`dom0`, and copying files into :term:`dom0` is a big security risk and strongly discouraged. New users often ask: fine, :term:`dom0` needs to be isolated, but how do I then set my own wallpaper in Qubes OS then? The possible solutions are:

- copy a file into :term:`dom0` in a hacky way (not recommended: this breaks isolation of :term:`dom0` and exposes you to risks from a contaminated graphics file)

- use screenshots:
   - first, display an image you want in **full screen** (you can force full screen by right-clicking on the window title bar, see :doc:`how-to-enter-fullscreen-mode` for more information)
   - take a screenshot (as above, :ref:`take a screenshot <user/how-to-guides/how-to-set-a-wallpaper:Taking screenshots>`)
   - use this image as your wallpaper

To set a wallpaper in the default XFCE desktop environment, you can use the Desktop tool.

.. figure:: /attachment/doc/howto-screenshot-3.png
   :alt: image of Qubes Menu with the page for System Settings tools open and the Desktop application highlighted
   :align: center

Setting an image as wallpaper **within a normal qube** does not influence :term:`dom0` wallpaper (the one you actually see on the screen) in any way.
