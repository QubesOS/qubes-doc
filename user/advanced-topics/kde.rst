=========================
KDE (desktop environment)
=========================


Installation
------------


Prior to R3.2, KDE was the default desktop environment in Qubes.
Beginning with R3.2, however, :doc:`XFCE is the new default desktop environment </developer/releases/3_2/release-notes>`. Nonetheless, it is
still possible to install KDE by issuing this command in dom0:

.. code:: bash

      $ sudo qubes-dom0-update kde-settings-qubes


You can also change your default login manager (lightdm) to the new KDE
default: sddm

- first you need to edit the ``/etc/sddm.conf`` to make sure if the
  custom X parameter is set according to Qubes needs:

  .. code:: bash

        [XDisplay]
        ServerArguments=-nolisten tcp -background none



- disable the lightdm service:

  .. code:: bash

        $ sudo systemctl disable lightdm



- enable the sddm service:

  .. code:: bash

        $ sudo systemctl enable sddm



- reboot



If you encounter performance issues with KDE, try switching back to
LightDM.

Window Management
-----------------


You can set each window’s position and size like this:

.. code:: python

      Right click title bar --> More actions --> Special window settings...
      
        Window matching tab
          Window class (application): Exact Match: <vm_name>
          Window title: Substring Match: <partial or full program name>
      
        Size & Position tab
          [x] Position: Apply Initially: x,y
          [x] Size: Apply Initially: x,y


You can also use ``kstart`` to control virtual desktop placement like
this:

.. code:: bash

      kstart --desktop 3 --windowclass <vm_name> -q --tray -a <vm_name> '<run_program_command>'



(Replace “3” with whichever virtual desktop you want the window to be
on.)

This can be useful for creating a simple shell script which will set up
your workspace the way you like.

Removal
-------


If you decide to remove KDE do **not** use
``dnf remove @kde-desktop-qubes``. You will almost certainly break your
system.

The safest way to remove (most of) KDE is:

.. code:: bash

      sudo dnf remove kdelibs plasma-workspace


