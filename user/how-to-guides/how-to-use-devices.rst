==================
How to use devices
==================

This is an overview of device handling in Qubes OS. For specific devices (:doc:`block </user/how-to-guides/how-to-use-block-storage-devices>`, :doc:`USB </user/how-to-guides/how-to-use-usb-devices>` and :doc:`PCI </user/how-to-guides/how-to-use-pci-devices>` devices), please visit their respective pages.

**Important security warning:** Device handling comes with many security implications. Please make sure you carefully read and understand the :doc:`security considerations </user/security-in-qubes/device-handling-security>`.

Introduction
------------

The interface to deal with devices of all sorts was unified in Qubes 4.0 with the ``qvm-device`` command and the Qubes Devices Widget. In Qubes 3.X, the Qubes VM Manager dealt with attachment as well. This functionality was moved to the Qubes Device Widget, the tool tray icon with a yellow square located in the top right of your screen by default.

There are currently four categories of devices Qubes understands:

- Microphones
- Block devices
- USB devices
- PCI devices

Microphones, block devices and USB devices can be attached with the GUI-tool. PCI devices can be attached using the Qube Settings, but require a VM reboot.

General Qubes Device Widget Behavior And Handling
-------------------------------------------------

.. figure:: /attachment/doc/qubes-devices.svg
   :alt:
   :align: center

   Qubes Devices Widget tray icon 

When clicking on the tray icon, several device-classes separated by lines are displayed as tooltip. Block devices are displayed on top, microphones one below and USB-devices at the bottom.

On most laptops, integrated hardware such as cameras and fingerprint-readers are implemented as USB-devices and can be found here.

Attaching Using The Widget
^^^^^^^^^^^^^^^^^^^^^^^^^^

Click the tray icon. Hover on a device you want to attach to a VM. A list of running VMs (except dom0) appears. Click on one and your device will be attached!

Detaching Using The Widget
^^^^^^^^^^^^^^^^^^^^^^^^^^

To detach a device, click the Qubes Devices Widget icon again. Attached devices are displayed in bold. Hover the one you want to detach. A list of VMs appears, one showing the eject symbol: |eject icon|

Attaching a Device to Several VMs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Only ``mic`` should be attached to more than one running VM. You may *assign* a device to more than one VM (using the :option:`--persistent <qvm-device attach --persistent>` option), however, only one of them can be started at the same time.

General ``qvm-device`` Command Line Tool Behavior
-------------------------------------------------

All devices, including PCI-devices, may be attached from the commandline using the ``qvm-device`` tools.

Device Classes
^^^^^^^^^^^^^^

.. program:: qvm-device

``qvm-device`` expects :option:`DEVICE_CLASS` as first argument. 

.. option:: DEVICE_CLASS

   can be one of the following

.. option:: pci
.. option:: usb
.. option:: block
.. option:: mic

Actions overview
^^^^^^^^^^^^^^^^

``qvm-device`` supports three actions:

.. option:: list, ls, l

   list all devices of :option:`DEVICE_CLASS`

.. option:: attach, at, a

   attach a specific device of :option:`DEVICE_CLASS`

.. option:: detach, dt, d

   detach a specific device of :option:`DEVICE_CLASS`

Global Options
^^^^^^^^^^^^^^

These three options are always available:

.. option:: --help, -h

   show help message and exit

.. option:: --verbose, -v

   increase verbosity

.. option:: --quiet, -q

   decrease verbosity


A full command consists of one :option:`DEVICE_CLASS` and one action. If no action is given, list is implied. :option:`DEVICE_CLASS` however is required.

**SYNOPSIS**::

   qvm-device DEVICE_CLASS {action} [action-specific arguments] [options]


Actions
-------

Actions are applicable to every :option:`DEVICE_CLASS` and expose some additional options.

Listing Devices
^^^^^^^^^^^^^^^

The :option:`list` action lists known devices in the system. :option:`list` accepts VM-names to narrow down listed devices. Devices available in, as well as attached to the named VMs will be listed.

:option:`qvm-device list` takes two options:

.. program:: qvm-device list

.. option:: --all

   equivalent to specifying every VM name after :option:`qvm-device list`. No VM-name implies :option:`--all`.

.. option::  --exclude
   
   exclude VMs from :option:`--all`. Requires :option:`--all`.

**SYNOPSIS**::

        qvm-device DEVICE_CLASS {list|ls|l} [--all [--exclude VM [VM [...]]] | VM [VM [...]]]

Attaching Devices
^^^^^^^^^^^^^^^^^

The :option:`qvm-device attach` action assigns an exposed device to a VM. This makes the device available in the VM it’s attached to. **Required argument are**:

.. program:: qvm-device attach

.. option:: targetVM

.. option:: sourceVM:deviceID

   :option:`sourceVM:deviceID` can be determined from :option:`qvm-device list` output

:option:`qvm-device attach` accepts two options:

.. option:: --persistent 

   attach device on :option:`targetVM`-boot. If the device is unavailable (physically missing or ``sourceVM`` not started), booting the :option:`targetVM` fails.

.. option:: --option, -o

   set additional options specific to :option:`DEVICE_CLASS <qvm-device DEVICE_CLASS>`.


**SYNOPSIS**::

   qvm-device DEVICE_CLASS {attach|at|a} targetVM sourceVM:deviceID [options]

Detaching Devices
^^^^^^^^^^^^^^^^^

The :option:`qvm-device detach` action removes an assigned device from a :option:`targetVM`. It won’t be available afterwards anymore. Though it tries to do so gracefully, beware that data-connections might be broken unexpectedly, so close any transaction before detaching a device!

If no specific :option:`sourceVM:deviceID` combination is given, *all devices of that* `DEVICE_CLASS <qvm-device DEVICE_CLASS>` will be detached.

:option:`qvm-device detach` accepts no options.

**SYNOPSIS**::

   qvm-device DEVICE_CLASS {detach|dt|d} targetVM [sourceVM:deviceID]

.. |eject icon| image:: /attachment/doc/media-eject.png
