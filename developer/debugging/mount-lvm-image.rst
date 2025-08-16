=======================
How to mount LVM images
=======================


You want to read your LVM image (e.g., there is a problem where you can’t start any VMs except dom0).

1: make the image available for qubesdb. From dom0 terminal:

.. code:: console

      # Example: /dev/qubes_dom0/vm-debian-9-tmp-root
      [user@dom0]$ dev=$(basename $(readlink /dev/YOUR_LVM_VG/YOUR_LVM_IMAGE))
      [user@dom0]$ qubesdb-write /qubes-block-devices/$dev/desc "YOUR_LVM_IMAGE"


2: Create a new disposable VM

.. code:: console

      [user@dom0]$ qvm-run -v --dispvm=YOUR_DVM_TEMPLATE --service qubes.StartApp+xterm &


3: Attach the device to your newly created disp VM

From the GUI, or from the command line:

.. code:: console

      [user@dom0]$ qvm-block attach NEWLY_CREATED_DISPVM dom0:$dev


4: Mount the partition you want to, and do what you want with it

.. code:: console

      [user@dispXXXX]$ mount /dev/xvdiX /mnt/


5: Umount and kill the VM

.. code:: console

      [user@dispXXXX]$ umount /mnt/


6: Remove the image from qubesdb

.. code:: console

      [user@dom0]$ qubesdb-rm /qubes-block-devices/$dev/


References
----------


Please consult this issue’s `comment <https://github.com/QubesOS/qubes-issues/issues/4687#issuecomment-451626625>`__.
