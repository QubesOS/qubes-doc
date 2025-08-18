===============================
How to install software in dom0
===============================

.. warning::

      This page is intended for advanced users.

**Warning:** Installing software in dom0 is for advanced users only. Doing so has the potential to compromise your entire Qubes OS installation. Exercise extreme caution.

Security
--------


Since there is no networking in dom0, any bugs discovered in dom0 desktop components (e.g., the window manager) are unlikely to pose a problem for Qubes, since none of the third-party software running in dom0 is accessible from VMs or the network in any way. Nonetheless, since software running in dom0 can potentially exercise full control over the system, it is important to install only trusted software in dom0.

The install/update process is split into two phases: *resolve and download* and *verify and install*. The *resolve and download* phase is handled by the UpdateVM. (The role of UpdateVM can be assigned to any VM in the Qube Manager, and there are no significant security implications in this choice. By default, this role is assigned to the FirewallVM.) After the UpdateVM has successfully downloaded new packages, they are sent to dom0, where they are verified and installed. This separation of duties significantly reduces the attack surface, since all of the network and metadata processing code is removed from the TCB.

Although this update scheme is far more secure than directly downloading updates in dom0, it is not invulnerable. For example, there is nothing that the Qubes OS Project can feasibly do to prevent a malicious RPM from exploiting a hypothetical bug in the cryptographic signature verification operation. At best, we could switch to a different distro or package manager, but any of them could be vulnerable to the same (or a similar) attack. While we could, in theory, write a custom solution, it would only be effective if Qubes repos included all of the regular template distro’s updates, and this would be far too costly for us to maintain.

How to update dom0
------------------


See :doc:`How to Update </user/how-to-guides/how-to-update>`.

How to install a specific package
---------------------------------


To install additional packages in dom0 (usually not recommended):

.. code:: console

      $ sudo qubes-dom0-update anti-evil-maid



You may also pass the ``--enablerepo=`` option in order to enable optional repositories (see yum configuration in dom0). However, this is only for advanced users who really understand what they are doing. You can also pass commands to ``dnf`` using ``--action=...``.

How to downgrade a specific package
-----------------------------------


**WARNING:** Downgrading a package can expose your system to security vulnerabilities.

To downgrade a specific package in dom0:

.. code:: console

      $ sudo qubes-dom0-update --action=downgrade package-version



How to re-install a package
---------------------------


To re-install a package in dom0:

.. code:: console

      $ sudo qubes-dom0-update --action=reinstall package



How to uninstall a package
--------------------------


If you’ve installed a package such as anti-evil-maid, you can remove it with the following command:

.. code:: console

      $ sudo dnf remove anti-evil-maid



Testing repositories
--------------------


If you wish to install updates that are still in :doc:`testing </user/downloading-installing-upgrading/testing>`, you must enable the appropriate testing repositories.

**Note:** The following repos are in dom0. For template testing repos, see :ref:`here <user/how-to-guides/how-to-install-software:testing repositories>`.

- ``qubes-dom0-current-testing`` – testing packages that will eventually land in the stable (``current``) repository

- ``qubes-dom0-security-testing`` – a subset of ``qubes-dom0-current-testing`` that contains packages that qualify as security fixes

- ``qubes-dom0-unstable`` – packages that are not intended to land in the stable (``qubes-dom0-current``) repository; mostly experimental debugging packages



To temporarily enable any of these repos, use the ``--enablerepo=<repo-name>`` option. Example commands:

.. code:: console

      $ sudo qubes-dom0-update --enablerepo=qubes-dom0-current-testing
      $ sudo qubes-dom0-update --enablerepo=qubes-dom0-security-testing
      $ sudo qubes-dom0-update --enablerepo=qubes-dom0-unstable



To enable or disable any of these repos permanently, change the corresponding ``enabled`` value to ``1`` in ``/etc/yum.repos.d/qubes-dom0.repo``.

For testing new templates, please see :ref:`here <user/downloading-installing-upgrading/testing:templates>`.

Contributed package repository
------------------------------


Please see :doc:`installing contributed packages </user/advanced-topics/installing-contributed-packages>`.

Kernel upgrade
--------------


This section describes upgrading the kernel in dom0 and domUs.

dom0
^^^^


The packages ``kernel`` and ``kernel-latest`` are for dom0.

In the ``current`` repository:

- ``kernel``: an older LTS kernel that has passed Qubes :doc:`testing </user/downloading-installing-upgrading/testing>` (the default dom0 kernel)

- ``kernel-latest``: the latest release from kernel.org that has passed Qubes :doc:`testing </user/downloading-installing-upgrading/testing>` (useful for :doc:`troubleshooting newer hardware </user/troubleshooting/hardware-troubleshooting>`)



In the ``current-testing`` repository:

- ``kernel``: the latest LTS kernel from kernel.org at the time it was built.

- ``kernel-latest``: the latest release from kernel.org at the time it was built.



domU
^^^^


The packages ``kernel-qubes-vm`` and ``kernel-latest-qubes-vm`` are for domUs. See :doc:`Managing VM kernel </user/advanced-topics/managing-vm-kernels>` for more information.

Example
^^^^^^^


(Note that the following example enables the unstable repo.)

.. code:: console

      $ sudo qubes-dom0-update --enablerepo=qubes-dom0-unstable kernel kernel-qubes-vm



If the update process does not automatically do it (you should see it mentioned in the CLI output from the update command), you may need to manually rebuild the EFI or grub config depending on which your system uses.

EFI
^^^


Replace the example version numbers with the one you are upgrading to.

.. code:: console

      $ sudo dracut -f /boot/efi/EFI/qubes/initramfs-4.14.35-1.pvops.qubes.x86_64.img 4.14.35-1.pvops.qubes.x86_64



Grub2
^^^^^


.. code:: console

      $ sudo grub2-mkconfig -o /boot/grub2/grub.cfg



Reboot required.

If you wish to upgrade to a kernel that is not available from the repos, then there is no easy way to do so, but `it may still be possible if you’re willing to do a lot of work yourself <https://groups.google.com/d/msg/qubes-users/m8sWoyV58_E/HYdReRIYBAAJ>`__.

Changing default kernel
-----------------------


This section describes changing the default kernel in dom0. It is sometimes needed if you have upgraded to a newer kernel and are having problems booting, for example. On the next kernel update, the default will revert to the newest.


.. code:: console

      $ sudo nano /etc/default/grub


Update the following two lines, add if needed:

.. code:: bash

      GRUB_DISABLE_SUBMENU=false
      GRUB_SAVEDEFAULT=true


Save and exit nano. Regenerate the GRUB 2 configuration. 

.. code:: console

      $ sudo grub2-mkconfig -o /boot/grub2/grub.cfg



Then, reboot. Once the grub menu appears, choose “Advanced Options for Qubes (with Xen hypervisor)”. Next, the top menu item (for example, “Xen hypervisor, version 4.8.5-9.fc25”). Select the kernel you want as default, and it will be remembered for next boot.

Updating over Tor
-----------------


Requires installed :topic:`Whonix <19014>`.

Go to Qubes VM Manager -> System -> Global Settings. See the UpdateVM setting. Choose your desired Whonix-Gateway ProxyVM from the list. For example: sys-whonix.

:menuselection:`Qubes VM Manager --> System --> Global Settings --> UpdateVM --> sys-whonix`


