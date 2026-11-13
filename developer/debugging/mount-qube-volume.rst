=============================================
How to mount Qube volumes in a different Qube
=============================================

The following is for accessing data from a qube's volume in another qube.
This is useful when converting the volume's filesystem to a different
filesystem or accessing data from an unbootable qube.

The exact method for mounting a qube's volume depends on how the volume data is stored, although the steps are mostly the same. The difference is in finding or creating a block device of the volume data.


1. Create/find a block device for the volume.

  - For LVM or ZVol backed volumes, do:

    .. code:: console

          # Example: /dev/qubes_dom0/vm-debian-9-tmp-root
          [user@dom0]$ dev=$(basename $(readlink /dev/YOUR_LVM_VG/YOUR_LVM_IMAGE))

  - For file backed volumes (includes volumes on file-reflink pools), do:

    .. code:: console

          # Example: /var/lib/qubes/appvms/work/private.img
          [user@dom0]$ dev=$(basename $(sudo losetup -f --show /path/to/volume/image/file.img))


2. Make the image available for qubesdb. From dom0 terminal:

  .. code:: console

        [user@dom0]$ qubesdb-write /qubes-block-devices/$dev/desc "VOLUME DESCRIPTION"


3. Tell qubesd that the device list changed

  .. code:: console

        [user@dom0]$ qubesdb-write /qubes-block-devices ''


4. Create a new disposable VM

  .. code:: console

        [user@dom0]$ qvm-run -v --dispvm=YOUR_DVM_TEMPLATE --service qubes.StartApp+xterm &


5. Attach the device to your newly created disp VM

  From the GUI, or from the command line:

  .. code:: console

        [user@dom0]$ qvm-block attach NEWLY_CREATED_DISPVM dom0:$dev


6. Mount the partition you want to, and do what you want with it

  .. code:: console

        [user@dispXXXX]$ mount /dev/xvdiX /mnt/


7. Umount and kill the VM

  .. code:: console

        [user@dispXXXX]$ umount /mnt/ && exit


8. Remove the image from qubesdb

  .. code:: console

        [user@dom0]$ qubesdb-rm /qubes-block-devices/$dev/
        [user@dom0]$ qubesdb-write /qubes-block-devices ''


References
----------


Please consult this issue’s `comment <https://github.com/QubesOS/qubes-issues/issues/4687#issuecomment-451626625>`__.
