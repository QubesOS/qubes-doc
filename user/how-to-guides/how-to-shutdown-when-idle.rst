================================
How to shutdown a qube when idle
================================

:program:`Qubes shutdown idle` allows you to automatically shut down a qube when idle for more than 15 minutes.

.. note::

   At the moment, only checking for visible windows is supported - when a VM has no visible windows for more than 15 minutes, it's going to be shut down.

1. **In the template of your qube**, :ref:`install the software <installing-software-from-default-repositories>` called ``qubes-app-shutdown-idle``.

2. Then you can either:

  * open the qube's :program:`Settings`, i.e.: in the :program:`Qubes Application menu`, select the qube and click on :guilabel:`Settings`. Then, tick the box :guilabel:`Shut down when idle for more than 15 minutes`.
  * or :doc:`enable the service </user/how-to-guides/how-to-enable-a-service>` called ``shutdown-idle``
