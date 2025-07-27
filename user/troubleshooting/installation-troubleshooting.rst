============================
Installation troubleshooting
============================


"An unknown error has occurred" error during installation
---------------------------------------------------------


Some people have encountered this error message when trying to install Qubes on drives that already have data on them. The solution is to exit the installer, wipe all data or delete all partitions, then restart the Qubes installation.

Trouble installing from USB stick
---------------------------------


If you are facing issues when booting using UEFI mode, see the :doc:`UEFI troubleshooting guide </user/troubleshooting/uefi-troubleshooting>`.

There are a variety of other problems that could arise when using a USB installation medium, and some of the issues can be fixed by doing one or more of the following:

- **Use a different USB drive:** If possible, try several drives of different sizes and formats. This determines whether the problem stems from the flash drive or Qubes installer. Some laptops cannot read from an external boot device larger than 8GB. If you encounter a black screen when performing an installation from a USB stick, ensure you are using a USB drive less than 8GB, or a partition on that USB less than 8GB and of format FAT32. Note that the Qubes installation image is over 4GB, so it may not fit on a smaller USB. If a machine can not boot from a bigger USB, it may be too old to run Qubes.

- **Verify your Qubes ISO:** Errors will occur if the Qubes installer is corrupted. Ensure that the installer is correct and complete before writing it to a flash drive by :doc:`verifying the ISO </project-security/verifying-signatures>`.

- **Change the method you used to** :ref:`write your ISO to a USB key <user/downloading-installing-upgrading/installation-guide:copying the iso onto the installation medium>` **:** Some people use the ``dd`` command (recommended), others use tools like Rufus, balenaEtcher or the GNOME Disk Utility. If installation fails after using one tool, try a different one. For example, if you are facing trouble installing Qubes after writing the ISO using Rufus, then try using other tools like balenaEtcher or the ``dd`` command. In case the boot partition is not set to “active” after copying the ISO, you can use some other tool like ``gparted`` on a Linux system to activate it.



"**Warning:** dracut-initqueue timeout - starting timeout scripts" during installation
--------------------------------------------------------------------------------------


This error message is related to the faulty creation of the USB installation medium. If you receive this error message during installation, please make sure you have followed the instructions on :ref:`how to write your ISO to a USB key <user/downloading-installing-upgrading/installation-guide:copying the iso onto the installation medium>`. Specifically, the ``dd`` command listed on that page has been verified to solve this issue on multiple Qubes installation versions.

.. code:: bash

      $ sudo dd if=Qubes-RX-x86_64.iso of=/dev/sdY status=progress bs=1048576 && sync



See :issue:`here <6447>` for a discussion of this error message.

Boot screen does not appear / system does not detect your installation medium
-----------------------------------------------------------------------------


If the boot screen does not appear, there are several options to troubleshoot. First, try rebooting your computer. If it still loads your currently installed operating system or does not detect your installation medium, make sure the boot order is set up appropriately.

The process to change the boot order varies depending on the currently installed system and the motherboard manufacturer.

If **Windows 10** is installed on your machine, you may need to follow specific instructions to change the boot order. This may require an `advanced reboot <https://support.microsoft.com/en-us/help/4026206/windows-10-find-safe-mode-and-other-startup-settings>`__.

"Not asking for VNC because we don't have a network" / "X startup failed, aborting installation" / "Pane is dead" error during installation
-------------------------------------------------------------------------------------------------------------------------------------------


The boot mode in use may be causing these error messages. Try to install after enabling both UEFI and legacy boot modes. If that doesn’t help, then disable one and try the other. Visit the :doc:`UEFI Troubleshooting guide </user/troubleshooting/uefi-troubleshooting>` if other errors arise during UEFI booting.

These errors may also occur due to an incompatible Nvidia graphics card. If you have one, follow the following instructions:

1. Disable secure/fast boot and use legacy mode

2. Enter GRUB, move the selection to the first choice, and then press the Tab key.

3. Now, you are in edit mode. Move the text cursor with your arrow key and after ``kernel=`` line, add:



.. code:: bash

      nouveau.modeset=0 rd.driver.blacklist=nouveau video=vesa:off


If the above code doesn’t fix the problem, replace it with:

.. code:: bash

      noexitboot=1 modprobe.blacklist=nouveau rd.driver.blacklist=nouveau --- intitrd.img


For more information, look at the :topic:`Nvidia Troubleshooting guide <19021#disabling-nouveau>`.

Installation freezes at "Setting up Networking"
-----------------------------------------------


If you are facing this problem on an Apple computer, check out the :topic:`Macbook Troubleshooting guide <19020>`.

If you are installing Qubes 4.0 on an external storage device, you may have forgotten to disable ``sys-usb`` during the :ref:`initial setup <user/downloading-installing-upgrading/installation-guide:initial setup>`, which is generally required for that setup to work.

This issue occurs due to the network card, which may be missing some drivers or is incompatible with Qubes.

First, install all available drivers for the card. You can install the drivers without internet access by first downloading them on another machine, then transferring them over to the current machine (e.g., with a USB drive).

If installing the available drivers does not help, disable the network card in the BIOS and perform the installation before re-enabling the card. If this solves the issue, it confirms the PCI card is incompatible with Qubes. In this case, you may want to consider replacing it with a network card of a different brand. Broadcom cards are notoriously problematic with Qubes.

"Unsupported Hardware Detected" error
-------------------------------------


During Qubes installation, you may come across the error message which reads “Unsupported Hardware Detected. Missing features: IOMMU/VT-d/AMD-Vi, Interrupt Remapping. Without these features, Qubes OS will not function normally”.

This error message indicates that IOMMU-virtualization hasn’t been activated in the BIOS. Return to the :ref:`hardware requirements <user/downloading-installing-upgrading/installation-guide:hardware requirements>` section to learn how to activate it. If the setting is not configured correctly, it means that your hardware won’t be able to leverage some Qubes security features, such as a strict isolation of the networking and USB hardware.

In Qubes 4.0, the default installation won’t function properly without IOMMU, as default sys-net and sys-usb qubes require IOMMU. It is possible to configure them to reduce isolation and not use IOMMU by changing virtualization mode of these two VMs to “PV”.

In Qubes 4.1, the default sys-net and sys-usb qubes need additional configuration to be usable without an IOMMU. Otherwise they will fail to start with this error message:

.. code:: bash

      Start failed: internal error: libxenlight failed to create new domain 'sys-net', see /var/log/libvirt/libxl/libxl-driver.log for details



To confirm that a missing IOMMU is causing this problem, check for the following error message in ``/var/log/libvirt/libxl/libxl-driver.log``:

.. code:: bash

      2022-03-01 13:27:17.117+0000: libxl: libxl_create.c:1146:libxl__domain_config_setdefault: passthrough not supported on this platform



Here are the steps to fix this. Note that this allows sys-net and sys-usb to take complete control of the system, as described in the :ref:`FAQ here <introduction/faq:why is vt-d\/amd-vi\/amd iommu important?>`:

1. Change the virtualization mode of sys-net and sys-usb to “PV”

2. Add ``qubes.enable_insecure_pv_passthrough`` to ``GRUB_CMDLINE_LINUX`` in ``/etc/default/grub``

3. Run ``sudo grub2-mkconfig -o /boot/efi/EFI/qubes/grub.cfg``. If you are using a non-UEFI BIOS (where ``/boot/efi/EFI`` doesn’t exist), use the command ``sudo grub-mkconfig -o /boot/grub2/grub.cfg`` instead.

4. Reboot


