=========
USB qubes
=========

.. warning::

      This page is intended for advanced users.

A USB qube acts as a secure handler for potentially malicious USB devices, preventing them from coming into contact with dom0 (which could otherwise be fatal to the security of the whole system). It thereby mitigates some of the :ref:`security risks of using USB devices <user/security-in-qubes/device-handling-security:usb security>`. Nonetheless, we strongly recommend carefully reading the :ref:`security warning on USB input devices <user/security-in-qubes/device-handling-security:security warning on usb input devices>` before proceeding.

With a USB qube, every time you connect an untrusted USB device to a USB port managed by that USB controller, you will have to attach it to the qube in which you wish to use it (if different from the USB qube itself).

If you opted to allow the Qubes installer to create a USB qube for you during the installation process, then you should already have a working USB qube, and no further action should be required. However, if you do not have a USB qube, wish to remove the one you have, or have run into some other related problem, this page can help.

USB keyboards
-------------


If you use a USB keyboard, there is a high risk of locking yourself out of your system when experimenting with USB qubes. For example, if a USB qube takes over your sole USB controller (to which your USB keyboard is connected), then your keyboard will no longer be able to control dom0. This will prevent you from performing many essential tasks, such as entering your decryption and login passphrases, rendering your system unusable until you reinstall. This section covers various options for addressing this problem.

In general, PS/2 keyboards are preferable to USB keyboards. However, many newer computer models lack PS/2 ports. Moreover, while most laptops use PS/2 connections for the keyboard internally, some use USB. (Check yours by examining the output of the ``lsusb`` command.) If you have a PS/2 port but still wish to use a USB keyboard, then having a backup PS/2 keyboard handy can be useful in case you accidentally lock yourself out of your system.

How to create a USB qube for use with a USB keyboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If you’re reading this section, it’s likely because the installer did not allow you to create a USB qube automatically because you’re using a USB keyboard. This section will explain how to create a USB qube that you can use with your USB keyboard. This section assumes that you have only a single USB controller. If you have more than one USB controller, see `how to enable a USB keyboard on a separate USB controller <#qubes-4-1-how-to-enable-a-usb-keyboard-on-a-separate-usb-controller>`__.

First, make sure you have the latest ``qubes-mgmt-salt-dom0-virtual-machines`` package by :ref:`updating dom0 <user/advanced-topics/how-to-install-software-in-dom0:how to update dom0>`. Then, enter the following command in dom0:

.. code:: console

      $ sudo qubesctl state.sls qvm.usb-keyboard



This command will take care of all required configuration, including creating a USB qube if not already present. Note, however, that this setup will expose dom0 to USB devices while you are entering your LUKS passphrase. While only input devices (keyboards, mice, etc.) are initialized at this stage, users are advised to physically disconnect other devices from the system during this vulnerable window in order to minimize the risk.

To undo these changes, see `how to remove a USB qube <#how-to-remove-a-usb-qube>`__.

If you wish to perform only a subset of this configuration (for example, you do not wish to enable the USB keyboard during boot), see the manual instructions below.

Manual setup for USB keyboards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


In order to use a USB keyboard, you must first attach it to a USB qube, then give that qube permission to pass keyboard input to dom0. Edit the ``qubes.InputKeyboard`` policy file in dom0, which is located here:

.. code:: text

      /etc/qubes-rpc/policy/qubes.InputKeyboard



Add a line like this one to the top of the file:

.. code:: text

      sys-usb dom0 allow



(Change ``sys-usb`` to your desired USB qube.)

You can now use your USB keyboard to log in to your dom0 user account (after LUKS decryption).

You can set up your system so that there’s a confirmation prompt each time the USB keyboard is connected. However, this will effectively disable your USB keyboard for dom0 user account login and the screen locker, so **don’t do this if you want to log into and unlock your device with a USB keyboard!** If you’re sure you wish to proceed, change the previous line to:

.. code:: text

      sys-usb dom0 ask,default_target=dom0



If you wish to use a USB keyboard to enter your LUKS passphrase, you cannot `hide its USB controller from dom0 <#how-to-hide-usb-controllers-from-dom0>`__. If you’ve already hidden that USB controller from dom0, you must revert the procedure by removing the ``rd.qubes.hide_all_usb`` option and employ an alternative strategy for protecting your system by physically disconnecting other devices during startup.

**Qubes 4.1 only:** You should also add the ``usbcore.authorized_default=0`` option, which prevents the initialization of non-input devices. (Qubes ships with a USBGuard configuration that allows only input devices when ``usbcore.authorized_default=0`` is set.)

Qubes 4.1: How to enable a USB keyboard on a separate USB controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


When using a USB keyboard on a system with multiple USB controllers, we recommend that you designate one of them exclusively for the keyboard (and possibly the mouse) and keep other devices connected to the other controller(s). This is often an option on desktop systems, where additional USB controllers can be plugged in as PCIe cards. In this case, the designated controller for input devices should remain in dom0 but be limited to input devices only. To set it up:

1. :ref:`Find the controller used for input devices <user/how-to-guides/how-to-use-usb-devices:finding the right usb controller>`.

2. Open the file ``/etc/default/grub`` in dom0.

3. Find the line that begins with ``GRUB_CMDLINE_LINUX``.

4. Add ``usbcore.authorized_default=0`` and ``rd.qubes.dom0_usb=<BDF>`` to that line, where ``<BDF>`` is the USB controller identifier.

5. Save and close the file.

6. Run the command ``grub2-mkconfig -o /boot/grub2/grub.cfg`` (legacy boot) or ``grub2-mkconfig -o /boot/efi/EFI/qubes/grub.cfg`` (EFI) in dom0.

7. Reboot.

8. Proceed with `creating a USB qube <#how-to-create-a-usb-qube>`__ normally. The selected USB controller will remain in dom0.



These options can be added during installation. (When the installer prompts for a reboot, you can switch to tty2 and perform the steps from there, after using the ``chroot /mnt/sysimage`` command.) In that case, the initial setup will create a USB qube automatically, even when a USB keyboard is in use (as long as it is connected to the designated controller).

USB mice
--------


Handling a USB mouse isn’t as critical as handling a keyboard, since you can log in and proceed through confirmation prompts using the keyboard alone.

If you want to attach the USB mouse automatically anyway, you have to edit the ``qubes.InputMouse`` policy file in dom0, located at:

.. code:: text

      /etc/qubes-rpc/policy/qubes.InputMouse



The first line should read similar to:

.. code:: text

      sys-usb dom0 ask,default_target=dom0



There will now be a confirmation prompt each time a USB mouse is attached.

If the file is empty or does not exist, something might have gone wrong during setup. Try to rerun ``qubesctl state.sls qvm.sys-usb`` in dom0.

In case you are absolutely sure you do not want to confirm mouse access from ``sys-usb`` to ``dom0``, you may add the following line to the top of the file:

.. code:: text

      sys-usb dom0 allow



(Change ``sys-usb`` to your desired USB qube.)

How to create a USB qube
------------------------


If `automatically creating a USB qube for use with a USB keyboard <#how-to-create-a-usb-qube-for-use-with-a-usb-keyboard>`__ does not apply to your situation, then you may be interested in more general methods for creating USB qubes.

You can create a USB qube using the management stack by executing the following command as root in dom0:

.. code:: console

      $ sudo qubesctl state.sls qvm.sys-usb



Manual creation
^^^^^^^^^^^^^^^


You can create a USB qube manually as follows:

1. Read the :doc:`PCI devices </user/how-to-guides/how-to-use-pci-devices>` page to learn how to list and identify your USB controllers. Carefully check whether you have a USB controller that would be appropriate to assign to a USB qube. Note that it should be free of input devices, programmable devices, and any other devices that must be directly available to dom0. If you find a free controller, note its name and proceed to the next step.

2. Create a new qube. Give it an appropriate name and color label (recommended: ``sys-usb``, red).

3. In the qube’s settings, go to the “Devices” tab. Find the USB controller that you identified in step 1 in the “Available” list. Move it to the “Selected” list by highlighting it and clicking the single arrow ``>`` button. (**Warning:** By assigning a USB controller to a USB qube, it will no longer be available to dom0. This can make your system unusable if, for example, you have only one USB controller, and you are running Qubes off of a USB drive.)

4. Click ``OK``. Restart the qube.

5. Recommended: Check the box on the “Basic” tab that says “Start VM automatically on boot.” (This will help to mitigate attacks in which someone forces your system to reboot, then plugs in a malicious USB device.)



If the USB qube will not start, please have a look at :ref:`this FAQ entry <introduction/faq:i created a usb vm and assigned usb controllers to it. now the usb vm won't boot.>`.

How to hide USB controllers from dom0
-------------------------------------


USB controllers are automatically hidden from dom0 if you opt to create a USB qube during installation. This also occurs automatically if you choose to `create a USB qube <#how-to-create-a-usb-qube>`__ using the ``qubesctl`` method. However, if you create a USB qube manually and do not hide USB controllers from dom0, there will be a brief period of time during the boot process when dom0 will be exposed to your USB controllers (and any attached devices). This is a potential security risk, since even brief exposure to a malicious USB device could result in dom0 being compromised. There are two approaches to this problem:

1. Physically disconnect all USB devices whenever you reboot the host.

2. Hide (i.e., blacklist) all USB controllers from dom0.



**Warning:** If you use a USB keyboard, hiding your USB controllers from dom0 could lock you out of your system. See `USB keyboards <#usb-keyboards>`__ for more information.

**Warning:** Using a USB AEM device requires dom0 to have access to the USB controller to which your USB AEM device is attached. If dom0 cannot read your USB AEM device, AEM will hang.

The following procedure will hide all USB controllers from dom0.

GRUB2 (legacy boot or EFI)
^^^^^^^^^^^^^^^^^^^^^^^^^^


1. Open the file ``/etc/default/grub`` in dom0.

2. Find the line that begins with ``GRUB_CMDLINE_LINUX``.

3. Add ``rd.qubes.hide_all_usb`` to that line.

4. Save and close the file.

5. Run the command ``grub2-mkconfig -o /boot/grub2/grub.cfg`` (legacy boot) or ``grub2-mkconfig -o /boot/efi/EFI/qubes/grub.cfg`` (EFI) in dom0.

6. Reboot.



How to remove a USB qube
------------------------


**Warning:** This procedure will result in your USB controller(s) being attached directly to dom0.

GRUB2
^^^^^


1. Shut down the USB qube.

2. In Qubes Manager, right-click on the USB qube and select “Remove VM.”

3. Open the file ``/etc/default/grub`` in dom0.

4. Find the line(s) that begins with ``GRUB_CMDLINE_LINUX``.

5. If ``rd.qubes.hide_all_usb`` appears anywhere in those lines, remove it.

6. Save and close the file.

7. Run the command ``grub2-mkconfig -o /boot/grub2/grub.cfg`` in dom0.

8. Reboot.



Qubes 4.0: EFI
^^^^^^^^^^^^^^


1. Shut down the USB qube.

2. In Qubes Manager, right-click on the USB qube and select “Remove VM.”

3. Open the file ``/boot/efi/EFI/qubes/xen.cfg`` in dom0.

4. Find the line(s) that begins with ``kernel=``.

5. If ``rd.qubes.hide_all_usb`` appears anywhere in those lines, remove it.

6. Save and close the file.

7. Reboot.


