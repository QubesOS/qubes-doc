================================
How to use block storage devices
================================


*This page is part of* :doc:`device handling in qubes </user/how-to-guides/how-to-use-devices>` *.*

If you don’t know what a “block device” is, just think of it as a fancy way to say “something that stores data”.

Using the Devices Widget to Attach a Drive
------------------------------------------


(**Note:** In the present context, the term “USB drive” denotes any `USB mass storage device <https://en.wikipedia.org/wiki/USB_mass_storage_device_class>`__. In addition to smaller flash memory sticks, this includes things like USB external hard drives.)

Qubes OS supports the ability to attach a USB drive (or just its partitions) to any qube easily, no matter which qube handles the USB controller.

Attaching USB drives is integrated into the Devices Widget: |device manager icon| Simply insert your USB drive and click on the widget. You will see multiple entries for your USB drive; typically, ``sys-usb:sda``, ``sys-usb:sda1``, and ``sys-usb:2-1`` for example. Entries starting with a number (e.g. here ``2-1``) are the :doc:`whole usb-device </user/how-to-guides/how-to-use-usb-devices>`. Entries without a number (e.g. here ``sda``) are the whole block-device. Other entries are partitions of that block-device (e.r. here ``sda1``).

The simplest option is to attach the entire block drive. In our example, this is ``sys-usb:sda``, so hover over it. This will pop up a submenu showing running VMs to which the USB drive can be connected. Click on one and your USB drive will be attached!

**Note:** attaching individual partitions (e.g. ``sys-usb:sda1``) can be slightly more secure because it doesn’t force the target app qube to parse the partition table. However, it often means the app qube won’t detect the new partition and you will need to manually mount it inside the app qube. See below for more detailed steps.

Block Devices in VMs
--------------------


If not specified otherwise, block devices will show up as ``/dev/xvdi*`` in a linux VM, where ``*`` may be the partition-number. If a block device isn’t automatically mounted after attaching, open a terminal in the VM and execute:

.. code:: console

      $ cd ~
      $ mkdir mnt
      $ sudo mount /dev/xvdi2 mnt



where ``xvdi2`` needs to be replaced with the partition you want to mount. This will make your drive content accessible under ``~/mnt``.

Beware that when you attach a whole block device, partitions can be identified by their trailing integer (i.e. ``/dev/xvdi2`` for the second partition, ``/dev/xvdi`` for the whole device), whereas if you attach a single partition, the partition has *no trailing integer*.

If several different block-devices are attached to a single VM, the last letter of the device node name is advanced through the alphabet, so after ``xvdi`` the next device will be named ``xvdj``, the next ``xvdk``, and so on.

To specify this device node name, you need to use the command line tool and its :ref:`frontend-dev-option <user/how-to-guides/how-to-use-block-storage-devices:frontend-dev>`.

Command Line Tool Guide
-----------------------


The command-line tool you may use to mount whole USB drives or their partitions is ``qvm-block``, a shortcut for ``qvm-device block``.

``qvm-block`` won’t recognise your device by any given name, but rather the device-node the sourceVM assigns. So make sure you have the drive available in the sourceVM, then list the available block devices (step 1.) to find the corresponding device-node.

In case of a USB-drive, make sure it’s attached to your computer. If you don’t see anything that looks like your drive, run ``sudo udevadm trigger --action=change`` in your USB-qube (typically ``sys-usb``)

1. In a dom0 console (running as a normal user), list all available block devices:

   .. code:: console

         $ qvm-block


   This will list all available block devices in your system across all VMs. The name of the qube hosting the block device is displayed before the colon in the device ID. The string after the colon is the ID of the device used within the qube, like so:

   .. code:: output

         sourceVM:sdb     Cruzer () 4GiB
         sourceVM:sdb1    Disk () 2GiB



2. Assuming your block device is attached to ``sys-usb`` and its device node is ``sdb``, we attach the device to a qube with the name ``work`` like so:

   .. code:: console

         $ qvm-block attach work sys-usb:sdb



   - This will attach the device to the qube as ``/dev/xvdi`` if that name is not already taken by another attached device, or ``/dev/xvdj``, etc.

   - You may also mount one partition at a time by using the same command with the partition number, e.g. ``sdb1``.



3. The block device is now attached to the qube. If using a default qube, you may open the Nautilus file manager in the qube, and your drive should be visible in the **Devices** panel on the left. If you’ve attached a single partition (e.g. ``sdb2`` instead of ``sdb`` in our example), you may need to manually mount before it becomes visible:

   .. code:: console

         $ cd ~
         $ mkdir mnt
         $ sudo mount /dev/xvdi mnt



4. When you finish using the block device, click the eject button or right-click and select **Unmount**.

   - If you’ve manually mounted a single partition in the above step, use:



   .. code:: console

         $ sudo umount mnt



5. In a dom0 console, detach the device

   .. code:: console

         $ qvm-block detach work sys-usb:sdb



6. You may now remove the device or attach it to another qube.



Recovering From Premature Device Destruction
--------------------------------------------


If you fail to detach the device before it’s destroyed in the sourceVM (e.g. by physically detaching the thumbdrive), `there will be problems <https://github.com/QubesOS/qubes-issues/issues/1082>`__.

To recover from this error state, in dom0 run

.. code:: console

      $ virsh detach-disk targetVM xvdi



(where ``targetVM`` is to be replaced with the VM name you attached the device to and ``xvdi`` is to be replaced with the used :ref:`frontend device node <user/how-to-guides/how-to-use-block-storage-devices:frontend-dev>`.)

However, if the block device originated in dom0, you will have to refer to the next section.

What if I removed the device before detaching it from the VM?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Currently (until issue `1082 <https://github.com/QubesOS/qubes-issues/issues/1082>`__ gets implemented), if you remove the device before detaching it from the qube, Qubes OS (more precisely, ``libvirtd``) will think that the device is still attached to the qube and will not allow attaching further devices under the same name. The easiest way to recover from such a situation is to reboot the qube to which the device was attached. If this isn’t an option, you can manually recover from the situation by following these steps:

1. Physically connect the device back. You can use any device as long as it will be detected under the same name (for example, ``sdb``).

2. Attach the device manually to the same VM using the ``xl block-attach`` command. It is important to use the same “frontend” device name (by default, ``xvdi``). You can get it from the ``qvm-block`` listing:

   .. code:: console

         [user@dom0 ~]$ qvm-block
         sys-usb:sda DataTraveler_2.0 () 246 MiB (attached to 'testvm' as 'xvdi')
         [user@dom0 ~]$ sudo xl block-attach testvm phy:/dev/sda backend=sys-usb xvdi

   In above example, all ``xl block-attach`` parameters can be deduced from the output of ``qvm-block``. In order:

   - ``testvm`` - name of target qube to which device was attached - listed in brackets by ``qvm-block`` command

   - ``phy:/dev/sda`` - physical path at which device appears in source qube (just after source qube name in ``qvm-block`` output)

   - ``backend=sys-usb`` - name of source qube, can be omitted in the case of dom0

   - ``xvdi`` - “frontend” device name (listed at the end of line in ``qvm-block`` output)



3. Now properly detach the device, either using Qubes VM Manager or the ``qvm-block -d`` command.



Attaching a File
----------------


To attach a file as block device to another qube, first turn it into a loopback device inside the sourceVM.

1. In the linux sourceVM run

   .. code:: console

         $ sudo losetup -f --show /path/to/file


   `This command <https://linux.die.net/man/8/losetup>`__ will create the device node ``/dev/loop0`` or, if that is already in use, increase the trailing integer until that name is still available. Afterwards it prints the device-node-name it found.

2. If you want to use the GUI, you’re done. Click the Device Manager |device manager icon| and select the ``loop0``-device to attach it to another qube.

   - If you rather use the command line, continue:

   - In dom0, run ``qvm-block`` to display known block devices. The newly created loop device should show up:



   .. code:: console

         ~]$ qvm-block
         BACKEND:DEVID  DESCRIPTION  USED BY
         sourceVM:loop0 /path/to/file


3. Attach the ``loop0``-device using qvm-block as usual:

   .. code:: console

         $ qvm-block a targetVM sourceVM:loop0



4. After detaching, destroy the loop-device inside the sourceVM as follows:

   .. code:: console

         $ sudo losetup -d /dev/loop0





Additional Attach Options
-------------------------


Attaching a block device through the command line offers additional customisation options, specifiable via the ``--option``/``-o`` option. (Yes, confusing wording, there’s an `issue for that <https://github.com/QubesOS/qubes-issues/issues/4530>`__.)

frontend-dev
^^^^^^^^^^^^


This option allows you to specify the name of the device node made available in the targetVM. This defaults to ``xvdi`` or, if already occupied, the first available device node name in alphabetical order. (The next one tried will be ``xvdj``, then ``xvdk``, and so on …)

usage example:

.. code:: console

      $ qvm-block a work sys-usb:sda1 -o frontend-dev=xvdz



This command will attach the partition ``sda1`` to ``work`` as ``/dev/xvdz``.

read-only
^^^^^^^^^


Attach device in read-only mode. Protects the block device in case you don’t trust the targetVM.

If the device is a read-only device, this option is forced true.

usage example:

.. code:: console

      $ qvm-block a work sys-usb:sda1 -o read-only=true



There exists a shortcut to set read-only ``true``, ``--ro``:

.. code:: console

      $ qvm-block a work sys-usb:sda1 --ro



The two commands are equivalent.

devtype
^^^^^^^


Usually, a block device is attached as disk. In case you need to attach a block device as cdrom, this option allows that.

usage example:

.. code:: console

      $ qvm-block a work sys-usb:sda1 -o devtype=cdrom



This option accepts ``cdrom`` and ``disk``, default is ``disk``.

.. |device manager icon| image:: /attachment/doc/media-removable.png
