============================
How to enable a qube service
============================

To enable a :doc:`service </user/advanced-topics/qubes-service>` in a qube there are two options:

* use the :program:`Settings` of the qube
* use `qvm-service <https://dev.qubes-os.org/projects/core-admin-client/en/latest/manpages/qvm-service.html>`__

You might have to restart the qube for changes to be reflected.

How to enable a service in the :program:`Settings`
---------------------------------------------------

1. Open the qube's :program:`Settings`, you can use :program:`Qubes Application menu`, select the qube and click on :guilabel:`Settings`.

2. Go to the :guilabel:`Services` tab

3. You have two options, depending on the current list of the services:

   * If the qube is listed, you just have to check the box if front of the name.

   * If the qube is not listed:

     1. select it in the :guilabel:`Select a service` drop-down.

        If that service is not present in the drop-down, select the last item, called :guilabel:`(custom...)`

     2. click on :guilabel:`Add`

        If you have previously selected :guilabel:`(custom...)`, a pop-up will ask you the name of the service

4. Use :guilabel:`Apply` of :guilabel:`&OK` to validate the change.

How to enable a service with :program:`qvm-service`
---------------------------------------------------

In a terminal, enter the following command, replacing :samp:`{<QUBE_NAME>}` by the name of the qube and :samp:`{<SERVICE_NAME>}` by the name of the service:

.. code:: console

   [user@dom0] $ qvm-service -e <QUBE_NAME> <SERVICE_NAME>

This is equivalent to:

.. code:: console

   [user@dom0] $ qvm-service <QUBE_NAME> <SERVICE_NAME> on

You can check the current status of the services of one qube with the following command:

.. code:: console

   [user@dom0] $ qvm-service <QUBE_NAME>

Or you can check only the current status of one service with the following command:

.. code:: console

   [user@dom0] $ qvm-service <QUBE_NAME> <SERVICE_NAME>
