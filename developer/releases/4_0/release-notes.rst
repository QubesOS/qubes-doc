========================
Qubes R4.0 release notes
========================


New features since 3.2
----------------------


- Core management scripts rewrite with better structure and extensibility, `current API documentation <https://dev.qubes-os.org/projects/core-admin/en/latest/>`__ and the documentation API index as a `webarchive <https://web.archive.org/web/20230128102821/https://dev.qubes-os.org/projects/qubes-core-admin/en/latest/>`__

- :website:`Admin API <news/2017/06/27/qubes-admin-api/>` allowing strictly controlled managing from non-dom0

- All ``qvm-*`` command-line tools rewritten, some options have changed

- Renaming VM directly is prohibited, there is GUI to clone under new name and remove old VM

- Use :github:`PVH <QubesOS/qubes-secpack/blob/master/QSBs/qsb-037-2018.txt>` and :issue:`HVM <2185>` by default to :github:`mitigate Meltdown & Spectre <QubesOS/qubes-secpack/blob/master/QSBs/qsb-037-2018.txt>` and lower the :github:`attack surface on Xen <QubesOS/qubes-secpack/blob/master/QSBs/qsb-024-2016.txt>`

- Create USB VM by default

- :issue:`Multiple DisposableVMs templates support <2253>`

- New :doc:`backup format </user/how-to-guides/backup-emergency-restore-v4>` using scrypt key-derivation function

- Non-encrypted backups no longer supported

- :issue:`split VM packages <2771>`, for better support minimal, specialized templates

- :issue:`Qubes Manager decomposition <2132>` - domains and devices widgets instead of full Qubes Manager; devices widget support also USB

- :doc:`More flexible firewall interface </developer/debugging/vm-interface>` for ease unikernel integration

- Template VMs do not have network interface by default, :issue:`qrexec-based updates proxy <1854>` is used instead

- More flexible IP addressing for VMs - :issue:`custom IP <1477>`, :issue:`hidden from the IP <1143>`

- More flexible Qubes RPC policy - :issue:`related ticket <865>`, :ref:`documentation <developer/services/qrexec:specifying vms: tags, types, targets, etc.>`

- :issue:`New Qubes RPC confirmation window <910>`, including option to specify destination VM

- :issue:`New storage subsystem design <1842>`

- Dom0 update to Fedora 25 for better hardware support

- Kernel 4.9.x



You can get detailed description in :github:`completed github issues <QubesOS/qubes-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+4.0%22+label%3Arelease-notes+is%3Aclosed>`

Security Notes
--------------


- PV VMs migrated from 3.2 to 4.0-rc4 or later are automatically set to PVH mode in order to protect against Meltdown (see :github:`QSB #37 <QubesOS/qubes-secpack/blob/master/QSBs/qsb-037-2018.txt>`). However, PV VMs migrated from any earlier 4.0 release candidate (RC1, RC2, or RC3) are not automatically set to PVH mode. These must be set manually.

- The following steps may need to be applied in dom0 and Fedora 26 TemplateVMs in order to receive updates (see :issue:`3737`).
  Steps for dom0 updates:

  1. Open the Qubes Menu by clicking on the “Q” icon in the top-left corner of the screen.

  2. Select ``Terminal Emulator``.

  3. In the window that opens, enter this command:

     .. code:: console

           $ sudo nano /etc/yum.repos.d/qubes-dom0.repo



  4. This opens the nano text editor. Change all four instances of ``http`` to ``https``.

  5. Press ``CTRL+X``, then ``Y``, then ``ENTER`` to save changes and exit.

  6. Check for updates normally.


  Steps for Fedora 26 TemplateVM updates:

  1. Open the Qubes Menu by clicking on the “Q” icon in the top-left corner of the screen.

  2. Select ``Template: fedora-26``, then ``fedora-26: Terminal``.

  3. In the window that opens, enter the command for your version:

     .. code:: console

           [Qubes 3.2] $ sudo gedit /etc/yum.repos.d/qubes-r3.repo
           [Qubes 4.0] $ sudo gedit /etc/yum.repos.d/qubes-r4.repo



  4. This opens the gedit text editor in a window. Change all four instances of ``http`` to ``https``.

  5. Click the “Save” button in the top-right corner of the window.

  6. Close the window.

  7. Check for updates normally.

  8. Shut down the TemplateVM.





Known issues
------------


- Locale using coma as decimal separator :issue:`crashes qubesd <3753>`. Either install with different locale (English (United States) for example), or manually apply fix explained in that issue.

- In the middle of installation, :issue:`keyboard layout reset to US <3352>`. Be careful what is the current layout while setting default user password (see upper right screen corner).

- On some laptops (for example Librem 15v2), touchpad do not work directly after installation. Reboot the system to fix the issue.

- List of USB devices may contain device identifiers instead of name

- With R4.0.1, which ships kernel-4.19, you may never reach the anaconda startup and be block on an idle black screen with blinking cursor. You can try to add ``plymouth.ignore-serial-consoles`` in the grub installer boot menu right after ``quiet rhgb``. With legacy mode, you can do it directly when booting the DVD or USB key. In UEFI mode, follow the same procedure described for :ref:`disabling <user/troubleshooting/uefi-troubleshooting:installation freezes before displaying installer>` ``nouveau`` module (related :issue:`solved issue <3849>` in further version of Qubes).

- For other known issues take a look at :github:`our tickets <QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Release+4.0%22+label%3Abug>`



It is advised to install updates just after system installation to apply bug fixes for (some of) the above problems.

Downloads
---------


See :website:`Qubes Downloads <downloads/>`.

Installation instructions
-------------------------


See :doc:`Installation Guide </user/downloading-installing-upgrading/installation-guide>`.

Upgrading
---------


There is no in-place upgrade path from earlier Qubes versions. The only supported option to upgrade to Qubes R4.0 is to install it from scratch and use :doc:`qubes backup and restore tools </user/how-to-guides/how-to-back-up-restore-and-migrate>` for migrating of all of the user VMs. We also provide :doc:`detailed instruction </user/downloading-installing-upgrading/upgrade/4_0>` for this procedure.
