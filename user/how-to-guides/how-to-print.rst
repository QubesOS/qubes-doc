============
How to print
============

The print service, CUPS, is off in every qube. Turn it on only in the qube you print from. :guilabel:`Print to File` (PDF) works without it.

CUPS and printer drivers handle data from the network and the printer. Don't print from your most trusted qubes: :doc:`copy the files </user/how-to-guides/how-to-copy-and-move-files>` to the printing qube.

Turn on CUPS
------------

1. :doc:`Enable the service </user/how-to-guides/how-to-enable-a-service>` ``cups`` in the qube. In dom0:

   .. code:: console

      [user@dom0] $ qvm-service -e <QUBE_NAME> cups

   If ``cups`` is not in the :guilabel:`Services` drop-down, :ref:`install <installing-software-from-default-repositories>` the ``cups`` package in the template.

2. Printers you add are lost when the qube restarts. To keep them, add ``/etc/cups`` to :doc:`bind-dirs </user/advanced-topics/bind-dirs>`. In the qube:

   .. code:: console

      [user@<QUBE_NAME>] $ sudo mkdir -p /rw/config/qubes-bind-dirs.d
      [user@<QUBE_NAME>] $ echo "binds+=( '/etc/cups' )" | sudo tee -a /rw/config/qubes-bind-dirs.d/50_user.conf

3. Restart the qube.

Add the printer
---------------

1. Install the printer driver, if needed, in the template.

2. For a USB printer, :doc:`attach it </user/how-to-guides/how-to-use-usb-devices>` to the qube.

3. In the qube, run:

   .. code:: console

      [user@<QUBE_NAME>] $ sudo system-config-printer

   Without ``sudo``, adding a printer asks for a password. Fedora templates don't include ``system-config-printer``: install it in the template.
