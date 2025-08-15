===================
PCI troubleshooting
===================


DMA errors
----------


VMs with attached PCI devices in Qubes have allocated a small buffer for DMA operations (called swiotlb). By default, it is 2MB, but some devices (such as the `Realtek RTL8111DL Gigabit Ethernet Controller <https://groups.google.com/group/qubes-devel/browse_thread/thread/631c4a3a9d1186e3>`__) need a larger DMA buffer size. Without a larger buffer, you will face DMA errors such as ``Failed to map TX DMA``.

To change this allocation, edit VM’s kernel parameters (this is expressed in 512B chunks) by running the following in a dom0 terminal:

.. code:: console

      # qvm-prefs netvm |grep kernelopts
      kernelopts       : iommu=soft swiotlb=2048 (default)
      # qvm-prefs -s netvm kernelopts "iommu=soft swiotlb=8192"



The ``8192`` value is the default value and some devices may require a larger value (like ``16384``).

PCI Passthrough Issues
----------------------


Sometimes the PCI arbitrator is too strict, which may cause errors such as ``Unable to reset PCI device`` and other PCI-related errors. There is a way to enable permissive mode for it. See also: `this thread <https://groups.google.com/forum/#!topic/qubes-users/Fs94QAc3vQI>`__ and the Xen wiki’s `PCI passthrough <https://wiki.xen.org/wiki/Xen_PCI_Passthrough>`__ page. Other times, you may instead need to disable the FLR requirement on a device.

Both can be achieved during attachment with ``qvm-pci`` as described :ref:`PCI Devices documentation <user/how-to-guides/how-to-use-pci-devices:additional attach options>`.

"Unable to reset PCI device" errors
-----------------------------------


libvirt.libvirtError: internal error: Unable to reset PCI device […]: internal error: Active […] devices on bus with […], not doing bus reset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


After running ``qvm-start sys-net``, you may encounter an error message which begins with ``libvirt.libvirtError: internal error: Unable to reset PCI device``.

This issue is likely to occur if you have the same device assigned to more than one VM. When you try to start sys-net with the ``qvm-start sys-net`` command, there is already a VM running (e.g., auto-starting) with one or more of the same devices as those assigned to sys-net.

To fix the error, remove the offending PCI device.

Using the Qubes interface
^^^^^^^^^^^^^^^^^^^^^^^^^


From the “Selected” panel in sys-net, navigate to VM Settings, then Devices. There, you can remove the offending PCI device(s) and keep the desired PCI device.

Using the command line
^^^^^^^^^^^^^^^^^^^^^^


1. To see all the PCI available devices, enter the ``lspci`` command into the dom0 terminal. Each device will be listed on a line, for example:

   .. code:: output

         0000:03:00.0 Audio device: Intel Corporation Haswell-ULT HD Audio Controller (rev 0b)


   In the above output, the BDF (Bus Device Function) of the device is ``0000:03:00.0``

2. Now that you can see all the PCI devices and their BDFs, you can decide which to remove and which to keep. Imagine we faced the following error message:

   .. code:: output

         libvirt.libvirtError: internal error: Unable to reset PCI device 0000:03:00.1: internal error: Active 0000:03:00.0 devices on bus with 0000:03:00.1, not doing bus reset


   In the above case, the device ``0000:03:00.1`` is the device which we want to use. But we are facing the ``Unable to reset PCI device`` error because another device, ``0000:03:00.0``, is active. To fix this error and get device ``0000:03:00.1`` to work, we must first remove the offending device ``0000:03:00.0``.

   .. code:: console

         $ sudo su
         $ echo -n "1" > /sys/bus/pci/devices/0000:03:00.0/remove



3. In order to make this change persistent, create a file ``/etc/systemd/system/qubes-pre-netvm.service`` and add the following:

   .. code:: systemd

         [Unit]
         Description=Netvm fixup
         Before=qubes-netvm.service

         [Service]
         ExecStart=/bin/sh -c 'echo -n "1" > /sys/bus/pci/devices/0000:03:00.0/remove'
         Type=oneshot
         RemainAfterExit=yes

         [Install]
         WantedBy=multi-user.target


   Finally, run ``systemctl enable qubes-pre-netvm.service`` and it will now persist between reboots.



Domain […] has failed to start: internal error: Unable to reset PCI device […]: no FLR, PM reset or bus reset available
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


This is a :ref:`PCI passthrough issue <user/troubleshooting/pci-troubleshooting:pci passthrough issues>`, which occurs when PCI arbitrator is too strict. There is a way to enable permissive mode for it. Sometimes, you may instead need to disable the FLR requirement on a device. Both can be achieved during attachment with ``qvm-pci`` as described below.

NOTE: The ``permissive`` flag increases attack surface and possibility of `side channel attacks <https://en.wikipedia.org/wiki/Side-channel_attack>`__. While using the ``no-strict-reset`` flag, do not require PCI device to be reset before attaching it to another VM. This may leak usage data even without malicious intent. Both ``permissive`` and ``no-strict-reset`` options may not be necessary and you should try one first, then the other, before using both.

.. code:: console

      $ qvm-pci attach --persistent --option permissive=true --option no-strict-reset=true sys-usb dom0:<BDF_OF_DEVICE>



Be sure to replace ``<BDF_OF_DEVICE>`` with the BDF of your PCI device, which can be obtained from running ``qvm-pci``.

You can also configure strict reset directly from the Qubes interface by following these steps:

1. Go to the sys-net VM settings

2. Go to Devices

3. Make sure the device is in the right field

4. Click “Configure strict reset for PCI devices”

5. Select the device, click OK and apply



Broadcom BCM43602 Wi-Fi card causes system freeze
-------------------------------------------------


You may face the problem where the BCM43602 Wi-Fi chip causes a system freeze whenever it is attached to a VM. To fix this problem on a Macbook, follow the steps in `Macbook Troubleshooting <https://forum.qubes-os.org/t/19020#system-freezes-after-attaching-broadcom-bcm43602-wi-fi-card>`__.

For other non-Macbook machines, it is advisable to replace the Broadcom BCM43602 with one known to work on Qubes, such as the Atheros AR9462.

Note that your computer manufacturer may have added a Wi-Fi card whitelist in your BIOS, which will prevent booting your computer if you have a non-listed wireless card. It is possible bypass this limitation by removing the whitelist, disabling a check for it or modifying the whitelist to replace device ID of a whitelisted WiFi card with device ID of your new WiFi card.

Wireless card stops working after dom0 update
---------------------------------------------


There have been many instances where a Wi-Fi card stops working after a dom0 update. If you run ``sudo dmesg`` in sys-net, you may see errors beginning with ``iwlwifi``. You can fix the problem by going to the sys-net VM’s settings and changing the VM kernel to the previous version.

Attached devices in Windows HVM stop working on suspend/resume
--------------------------------------------------------------


After the whole system gets suspended into S3 sleep and subsequently resumed, some attached devices may stop working. Refer to :ref:`Suspend/Resume Troubleshooting <user/troubleshooting/resume-suspend-troubleshooting:attached devices in windows hvm stop working on suspend\/resume>` for a solution.

PCI device not available in dom0 after being unassigned from a qube
-------------------------------------------------------------------


After you assign a PCI device to a qube, then unassign it/shut down the qube, the device is not available in dom0. This is an intended feature. A device which was previously assigned to a less trusted qube could attack dom0 if it were automatically reassigned there. Look at the :ref:`FAQs <introduction/faq:i assigned a pci device to a qube, then unassigned it\/shut down the qube. why isn't the device available in dom0?>` to learn how to re-enable the device in dom0.

Network adapter does not work
-----------------------------


You may have an adapter (wired, wireless), that is not compatible with open-source drivers shipped by Qubes. You may need to install a binary blob, which provides drivers, from the linux-firmware package.

Open a terminal and run ``sudo dnf install linux-firmware`` in the template upon which your NetVM is based. You have to restart the NetVM after the template has been shut down.
