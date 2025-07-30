====================
Disk troubleshooting
====================


"Out of disk space" error
-------------------------


If the disk is completely full, you will get an ``Out of disk space`` error that may crash your system because Dom0 does not have enough disk space to work. So it’s good practice to regularly check disk space usage. Running the ``df -h`` command in dom0 terminal will show some information, but not include all the relevant details. The Qubes user interface provides a disk space widget. If you are unable to access the interface, the command line version is running ``sudo lvs | head`` and looking at top entry for LVM pool. For example:

.. code:: text

      LV                                            VG         Attr       LSize   Pool   Origin                                        Data%  Meta%  Move Log Cpy%Sync Convert
       pool00                                        qubes_dom0 twi-aotz-- 453.17g                                                      89.95  69.78
       root                                          qubes_dom0 Vwi-aotz-- 453.17g pool00                                               5.87
       swap                                          qubes_dom0 -wi-ao----   7.57g



If you run ``df -h``, it only shows the information in the ``root`` line (which is already included in the ``pool00`` line). As you can see, the ``sudo lvs | head`` command includes additional important columns ``Data%`` and ``Meta%``, shown in the above example to have the values 89% and 69% respectively.

If your system is able to boot, but cannot load a desktop environment, it is possible to login to dom0 terminal with Alt + Ctrl + F2.

If this does not work, check the size of ``/var/lib/qubes/qubes.xml``. If it is zero, you’ll need to use one of the file backup (stored in ``/var/lib/qubes/backup``), hopefully you have the current data there. Find the most recent one and place in ``/var/lib/qubes/qubes.xml`` instead of the empty file.

In any case you’ll need some disk space to start the VM. Check ``df -h`` output if you have some. If not, here are some hints how to free some disk space:

1. Clean yum cache.

   .. code:: console

         sudo dnf clean all



2. Delete ``.img`` files of a less important VM, which can be found in ``/var/lib/qubes/appvms/``. Then, when the system is working again, clean up the rest.

   .. code:: console

         qvm-remove <VMname>


   With this method, you lose the data of one VM, but it’ll work more reliably.

3. Decrease the filesystem safety margin (5% by default).

   .. code:: console

         sudo tune2fs -m 4 /dev/mapper/vg_dom0-lv_root



4. Remove some unneeded files in dom0 home (if you have any, most likely not). Also look for unneeded files in ``/var/log`` in dom0, and ``/var/log/qubes``.



The above steps applies to old VM disks format. These steps may work on Qubes 4.0, but are not default anymore. By default, Qubes 4.0 now uses LVM. The equivalent steps are:

1. Get a list of VM disks using ``sudo lvs``.

2. Use ``sudo lvremove qubes_dom0/<name>`` to remove backup copies of some less important VMs – entries with ``-back`` in their name.

3. If that isn’t enough, remove actual disks of less important VMs. NOTE: You will lose the data of that VM, but your system will resume working.



For example:

.. code:: console

      $ sudo lvs
        LV                                            VG         Attr       LSize   Pool   Origin                                        Data%  Meta%  Move Log Cpy%Sync Convert
        pool00                                        qubes_dom0 twi-aotz-- 453.17g                                                      89.95  69.78
        root                                          qubes_dom0 Vwi-aotz-- 453.17g pool00                                               5.87
        swap                                          qubes_dom0 -wi-ao----   7.57g
      (...)
        vm-d10test-private                            qubes_dom0 Vwi-a-tz--   2.00g pool00 vm-d10test-private-1600961860-back            29.27
        vm-d10test-private-1600961860-back            qubes_dom0 Vwi-a-tz--   2.00g pool00                                               4.87
        vm-d10test-standalone-private                 qubes_dom0 Vwi-a-tz--   2.00g pool00 vm-d10test-standalone-private-1580772439-back 4.90
        vm-d10test-standalone-private-1580772439-back qubes_dom0 Vwi-a-tz--   2.00g pool00                                               4.87
        vm-d10test-standalone-root                    qubes_dom0 Vwi-a-tz--  10.00g pool00 vm-d10test-standalone-root-1580772439-back    43.37
        vm-d10test-standalone-root-1580772439-back    qubes_dom0 Vwi-a-tz--  10.00g pool00                                               42.05
        vm-debian-10-my-private                       qubes_dom0 Vwi-a-tz--   2.00g pool00                                               4.96
        vm-debian-10-my-root                          qubes_dom0 Vwi-a-tz--  10.00g pool00 vm-debian-10-my-root-1565013689-back          57.99
        vm-debian-10-my-root-1565013689-back          qubes_dom0 Vwi-a-tz--  10.00g pool00                                               56.55
        vm-debian-10-private                          qubes_dom0 Vwi-a-tz--   2.00g pool00                                               4.94
        vm-debian-10-root                             qubes_dom0 Vwi-a-tz--  10.00g pool00 vm-debian-10-root-1601126126-back             93.44
        vm-debian-10-root-1601126126-back             qubes_dom0 Vwi-a-tz--  10.00g pool00                                               88.75
      (...)
      $ sudo lvremove qubes_dom0/vm-d10test-standalone-root-1580772439-back
      Do you really want to remove and DISCARD active logical volume qubes_dom0/vm-d10test-standalone-root-1580772439-back? [y/n]: y
        Logical volume "vm-d10test-standalone-root-1580772439-back" successfully removed



After freeing some initial space, it may be possible to recover more space by deleting files in a userVM after connecting to the userVM terminal:

.. code:: console

      qvm-start <VMname>
      qvm-console-dispvm <VMname>



Since ``qvm-console-dispvm`` requires working graphical user interface login, you must first free enough space to be able to start a VM and login to graphical UI.

Can't resize VM storage / "resize2fs: Permission denied" error
--------------------------------------------------------------


:doc:`Resizing a volume </user/advanced-topics/resize-disk-image>` in the Qubes interface should be a straightforward process. But sometimes, an attempt to resize will look like it worked, when it in fact fails silently. If you then try the same operation in the dom0 console using the ``qvm-volume extend`` command, it fails with the error message: ``resize2fs: Permission denied to resize filesystem``. This error indicates that a ``resize2fs`` will not work, unless ``fsck`` is run first. Qubes OS utilities cannot yet handle this case.

To fix this issue:

1. In the dom0 terminal get a root console on the vm (eg. sys-usb) with:

   .. code:: console

         qvm-console-dispvm sys-usb



2. Unmount everything mounted on the private volume ``/dev/xvdb partition``. There are typically several mounts listed in ``/etc/mtab``.

3. When you attempt to unmount the ``/home`` directory using the ``umount /home`` command, you will encounter an error because there are processes using the ``/home`` directory. You can view a list of these processes with the ``fuser`` command:

   .. code:: console

         fuser -m /home





Kill these process until they are all gone using ``kill <process ID>``.

4. Finally, run:

   .. code:: console

         umount /home
         fsck /dev/xvdb
         resize2fs /dev/xvdb







After restarting your VM, everything should now work as expected. The private volume size shown externally in the VM’s settings interface is the same as that seen within the VM.
