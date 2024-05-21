======================
How to use USB devices
======================


*This page is part of* :doc:`device handling in qubes </user/how-to-guides/how-to-use-devices>` *.*

If you are looking to handle USB *storage* devices (thumbdrives or
USB-drives), please have a look at the :doc:`block device </user/how-to-guides/how-to-use-block-storage-devices>` page.

**Note:** Attaching USB devices to VMs requires a :doc:`USB qube </user/advanced-topics/usb-qubes>`.

**Important security warning:** USB passthrough comes with many security
implications. Please make sure you carefully read and understand the
:ref:`security considerations <user/security-in-qubes/device-handling-security:usb security>`.
Whenever possible, attach a :doc:`block device </user/how-to-guides/how-to-use-block-storage-devices>` instead.

Examples of valid cases for USB-passthrough:

- `microcontroller programming <https://www.arduino.cc/en/Main/Howto>`__

- `external audio devices <https://forum.qubes-os.org/t/18984>`__

- :doc:`optical drives </user/how-to-guides/how-to-use-optical-discs>` for recording



(If you are thinking to use a two-factor-authentication device, :doc:`there is an app for that </user/security-in-qubes/ctap-proxy>`. But it has some
`issues <https://github.com/QubesOS/qubes-issues/issues/4661>`__.)

Attaching And Detaching a USB Device
------------------------------------


With Qubes Device Manager
^^^^^^^^^^^^^^^^^^^^^^^^^


Click the device-manager-icon: |device manager icon| A list of available
devices appears. USB-devices have a USB-icon to their right: |usb icon|

Hover on one device to display a list of VMs you may attach it to.

Click one of those. The USB device will be attached to it. You’re done.

After you finished using the USB-device, you can detach it the same way
by clicking on the Devices Widget. You will see an entry in bold for
your device such as **``sys-usb:2-5 - 058f_USB_2.0_Camera``**. Hover on
the attached device to display a list of running VMs. The one to which
your device is connected will have an eject button |eject icon| next to
it. Click that and your device will be detached.

With The Command Line Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^


In dom0, you can use ``qvm-usb`` from the commandline to attach and
detach devices.

Listing available USB devices:

.. code:: bash

      [user@dom0 ~]$ qvm-usb
      BACKEND:DEVID   DESCRIPTION                    USED BY
      sys-usb:2-4     04ca:300d 04ca_300d
      sys-usb:2-5     058f:3822 058f_USB_2.0_Camera
      sys-usb:2-1     03f0:0641 PixArt_HP_X1200_USB_Optical_Mouse


Attaching selected USB device:

.. code:: bash

      [user@dom0 ~]$ qvm-usb attach work sys-usb:2-5
      [user@dom0 ~]$ qvm-usb
      BACKEND:DEVID   DESCRIPTION                    USED BY
      sys-usb:2-4     04ca:300d 04ca_300d
      sys-usb:2-5     058f:3822 058f_USB_2.0_Camera  work
      sys-usb:2-1     03f0:0641 PixArt_Optical_Mouse


Now, you can use your USB device (camera in this case) in the ``work``
qube. If you see the error
``ERROR: qubes-usb-proxy not installed in the VM`` instead, please refer
to the `Installation Section <#installation-of-qubes-usb-proxy>`__.

When you finish, detach the device.

.. code:: bash

      [user@dom0 ~]$ qvm-usb detach work sys-usb:2-5
      [user@dom0 ~]$ qvm-usb
      BACKEND:DEVID   DESCRIPTION                    USED BY
      sys-usb:2-4     04ca:300d 04ca_300d
      sys-usb:2-5     058f:3822 058f_USB_2.0_Camera
      sys-usb:2-1     03f0:0641 PixArt_Optical_Mouse


Maintenance And Customisation
-----------------------------


Creating And Using a USB qube
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If you’ve selected to install a usb-qube during system installation,
everything is already set up for you in ``sys-usb``. If you’ve later
decided to create a usb-qube, please follow :doc:`this guide </user/advanced-topics/usb-qubes>`.

Installation Of ``qubes-usb-proxy``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


To use this feature, the ``qubes-usb-proxy`` package needs to be
installed in the templates used for the USB qube and qubes you want to
connect USB devices to. This section exists for reference or in case
something broke and you need to reinstall ``qubes-usb-proxy``. Under
normal conditions, ``qubes-usb-proxy`` should already be installed and
good to go.

If you receive this error:
``ERROR: qubes-usb-proxy not installed in the VM``, you can install the
``qubes-usb-proxy`` with the package manager in the VM you want to
attach the USB device to.

- Fedora:

  .. code:: bash

        sudo dnf install qubes-usb-proxy



- Debian/Ubuntu:

  .. code:: bash

        sudo apt-get install qubes-usb-proxy





Using USB Keyboards And Other Input Devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Warning:** especially keyboards need to be accepted by default when
using them to login! Please make sure you carefully read and understood
the :ref:`security considerations <user/security-in-qubes/device-handling-security:usb security>` before
continuing!

Mouse and keyboard setup are part of :doc:`setting up a USB qube </user/advanced-topics/usb-qubes>`.

Finding The Right USB Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Some USB devices are not compatible with the USB pass-through method
Qubes employs. In situations like these, you can try to pass through the
entire USB controller to a qube as PCI device. However, with this
approach one cannot attach single USB devices but has to attach the
whole USB controller with whatever USB devices are connected to it.

If you have multiple USB controllers, you must first figure out which
PCI device is the right controller.

First, find out which USB bus the device is connected to (note that
these steps need to be run from a terminal inside your USB qube):

.. code:: bash

      lsusb



For example, I want to attach a broadband modem to the NetVM. In the
output of ``lsusb`` it may be listed as something like:

.. code:: bash

      Bus 003 Device 003: ID 413c:818d Dell Computer Corp.



(In this case, the device isn’t fully identified)

The device is connected to USB bus #3. Check which other devices are
connected to the same bus, since *all* of them will be attach to the
same VM.

To find the right controller, follow the usb bus:

.. code:: bash

      readlink /sys/bus/usb/devices/usb3



This should output something like:

.. code:: bash

      ../../../devices/pci-0/pci0000:00/0000:00:1a.0/usb3



Now you see the path and the text between ``/pci0000:00/0000:`` and
``/usb3`` i.e. ``00:1a.0`` is the BDF address. Strip the address and
pass it to the :doc:`qvm-pci tool </user/how-to-guides/how-to-use-pci-devices>` to
attach the controller to the targetVM.

For example, On R 4.0 the command would look something like

.. code:: bash

      qvm-pci attach --persistent personal dom0:00_1a.0



.. |device manager icon| image:: /attachment/doc/media-removable.png

.. |usb icon| image:: /attachment/doc/generic-usb.png

.. |eject icon| image:: /attachment/doc/media-eject.png
