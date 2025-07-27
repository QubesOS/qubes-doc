========================
How to use optical discs
========================


Passthrough reading and recording (a.k.a., “burning”) are not supported by Qubes OS. This is not a limitation of Xen, which provides scsiback and scsifront drivers, but of Qubes OS. It will be fixed in the future.

Currently, the only options for reading and recording optical discs (e.g., CDs, DVDs, BRDs) in Qubes are:

1. Use a USB optical drive.

2. Attach a SATA optical drive to a secondary SATA controller, then assign this secondary SATA controller to a VM.

3. Use a SATA optical drive attached to dom0. (**Caution:** This option is :topic:`potentially dangerous <19075#dom0-precautions>`.)



To access an optical disc via USB follow the :ref:`typical procedure for attaching a USB device <user/how-to-guides/how-to-use-usb-devices:with the command line tool>`, then check with the **Qubes Devices** widget to see what device in the target qube the USB optical drive was attached to. Typically this would be ``sr0``. For example, if ``sys-usb`` has device ``3-2`` attached to the ``work`` qube’s ``sr0``, you would mount it with ``mount /dev/sr0 /mnt/removable``. You could also write to a disc with ``wodim -v dev=/dev/sr0 -eject /home/user/Qubes.iso``.
