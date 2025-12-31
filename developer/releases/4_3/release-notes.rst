==========================
Qubes OS 4.3 release notes
==========================


Major features and improvements since Qubes 4.2
===============================================

- Dom0 upgraded to Fedora 41
  (`#9402 <https://github.com/QubesOS/qubes-issues/issues/9402>`__).

- Xen upgraded to version 4.19
  (`#9420 <https://github.com/QubesOS/qubes-issues/issues/9420>`__).

- Default Fedora template upgraded to Fedora 42 (Fedora TemplateVMs and
  StandaloneVMs with version lower than 41 are not supported).

- Default Debian template upgraded to Debian 13 (Debian TemplateVMs and
  StandaloneVMs with version lower than 12 are not supported).

- Default Whonix templates upgraded to Whonix 18 (Whonix TemplateVMs
  and StandaloneVMs with version lower than 18 are not supported).

- Preloaded disposables
  (`#1512 <https://github.com/QubesOS/qubes-issues/issues/1512>`__,
  `#9907 <https://github.com/QubesOS/qubes-issues/issues/9907>`__,
  `#9917 <https://github.com/QubesOS/qubes-issues/issues/9917>`__,
  `#9918 <https://github.com/QubesOS/qubes-issues/issues/9918>`__ &
  `#10026 <https://github.com/QubesOS/qubes-issues/issues/10026>`__).

  **See:** :ref:`preloaded-disposables`

- Device “self-identity oriented” assignment (a.k.a New Devices API)
  (`#9325 <https://github.com/QubesOS/qubes-issues/issues/9325>`__).

  **See:** :option:`core-admin-client:qvm-device --assignments`, ``qvm-device assign`` and ``qvm-device unassign``

- :doc:`/user/templates/windows/qubes-windows-tools` reintroduction with improved features
  (`#1861 <https://github.com/QubesOS/qubes-issues/issues/1861>`__).

  |Screenshot of QWT, Welcome page|

  |Screenshot of QWT, Windows 11|

UI/UX
-----

- New Device UX workflow to allow users easy utilization of new Devices API.
  A dedicated ``Device Assignments`` page is added to Global Config.
  Qubes Devices widget is completely redesigned.
  (`#8537 <https://github.com/QubesOS/qubes-issues/issues/8537>`__).

  |Screenshot of Device UX assignments|

  |Screenshot of Device UX deny attachment|

  |Screenshot of Device UX edit assignment|

  |Screenshot of Device UX required devices|

  |Screenshot of Device UX Qubes Devices widget|

- New and improved flat icons for GUI tools (`#5657 <https://github.com/QubesOS/qubes-issues/issues/5657>`__).

   .. list-table::
      :widths: 10 10
      :align: center
      :header-rows: 1

      * - 4.3
        - 4.2
      * - |Screenshot of Qube Manager in 4.3|
        - |Screenshot of Qube Manager in 4.2|

- In :program:`Qube Manager`, the icons from the far-left column are removed (`#6776 <https://github.com/QubesOS/qubes-issues/issues/6776>`__).

- Improved :program:`Qubes Template Manager` graphical interface

- In the :program:`Settings` of a qube:

  - the :guilabel:`Application` tab now provides a search bar.

  - and Application icons are displayed (`#9829 <https://github.com/QubesOS/qubes-issues/issues/9829>`__).

  .. list-table::
     :widths: 10 10
     :align: center
     :header-rows: 1

     * - 4.3
       - 4.2
     * - |Screenshot of Qube Settings Applications in 4.3|
       - |Screenshot of Qube Settings Applications in 4.2|

- Option to add Qubes video Companion to AppMenu
  (`#9761 <https://github.com/QubesOS/qubes-issues/issues/9761>`__).

- Improved AppMenu navigation with keyboard
  (`#9006 <https://github.com/QubesOS/qubes-issues/issues/9006>`__).

- Better wording to clarify updater settings and actions
  (`#8096 <https://github.com/QubesOS/qubes-issues/issues/8096>`__).

- Centralized Tray Notifications
  (`#889 <https://github.com/QubesOS/qubes-issues/issues/889>`__).

- Options to launch root terminal or `console terminal <https://dev.qubes-os.org/projects/core-admin-client/en/latest/manpages/qvm-features.html#expert-mode>`__ from :program:`Qubes Domains widget` (`#9788 <https://github.com/QubesOS/qubes-issues/issues/9788>`__).

  Holding the shift key changes the :guilabel:`Run Terminal` command into a :guilabel:`Run Root Terminal` action.

- Option to open Global Config at a selected section for user
  convenience
  (`#9530 <https://github.com/QubesOS/qubes-issues/issues/9530>`__).

- A ``Saving changes...`` dialog is added to Global Config
  (`#9926 <https://github.com/QubesOS/qubes-issues/issues/9926>`__).

GUI Daemon/Agent improvements
-----------------------------

- Allowing the GUI Daemon background color to be configurable, mostly
  useful for people with dark themes
  (`#9304 <https://github.com/QubesOS/qubes-issues/issues/9304>`__).

- Audio daemon does not connect to recording stream unless recording is
  explicitly enabled
  (`#9999 <https://github.com/QubesOS/qubes-issues/issues/9999>`__).

- Legacy X11 App icons (e.g. Xterm) are properly displayed
  (`#9973 <https://github.com/QubesOS/qubes-issues/issues/9973>`__).

- Labeling virtual pointing device as absolute and not relative
  (`#228 <https://github.com/QubesOS/qubes-issues/issues/228>`__).

- Improved global clipboard notifications & configurable global clipboard size
  (`#9296 <https://github.com/QubesOS/qubes-issues/issues/9296>`__ &
  `#9978 <https://github.com/QubesOS/qubes-issues/issues/9978>`__).

- Supporting Windows qubes in systems with ``sys-gui*``
  (`#7565 <https://github.com/QubesOS/qubes-issues/issues/7565>`__).

Hardware support improvements
-----------------------------

- Support for `Advanced Format
  (AF) <https://en.wikipedia.org/wiki/Advanced_Format>`__ drives better known
  as 4K sector
  (`#4974 <https://github.com/QubesOS/qubes-issues/issues/4974>`__).

- Replacing bus/slot/function with full PCI paths for device assignments
  (`#8681 <https://github.com/QubesOS/qubes-issues/issues/8681>`__
  & `#8127 <https://github.com/QubesOS/qubes-issues/issues/8127>`__).

- Ability to filter input devices with udev rules.
  (`#3604 <https://github.com/QubesOS/qubes-issues/issues/3604>`__).

- Fix for graceful rebooting on some (U)EFI systems with buggy firmware
  (`#6258 <https://github.com/QubesOS/qubes-issues/issues/6258>`__).

- Better support for Bluetooth and external hot-pluggable audio devices
  with dynamic AudioVM switching
  (`#7750 <https://github.com/QubesOS/qubes-issues/issues/7750>`__).

Security features
-----------------

- Templates could request custom kernel command line parameters;
  currently used for Kicksecure and Whonix templates ``user-sysmaint-split``
  (`#9750 <https://github.com/QubesOS/qubes-issues/issues/9750>`__).

  - Allow VMs to specify boot modes as being only intended for AppVMs or
    templates
    (`#9920 <https://github.com/QubesOS/qubes-issues/issues/9920>`__).

- Shipping GRUB2 from Fedora with all security patches and Bootloader
  Specification support
  (`#9471 <https://github.com/QubesOS/qubes-issues/issues/9471>`__).

- SSL client certificate and GPG key support for private template repositories
  (`#9850 <https://github.com/QubesOS/qubes-issues/issues/9850>`__).

- Preventing unsafe practice of 3rd party template installation with rpm/dnf
  (`#9943 <https://github.com/QubesOS/qubes-issues/issues/9943>`__).

- Ability to `prohibit start <https://dev.qubes-os.org/projects/core-admin-client/en/latest/manpages/qvm-features.html#prohibit-start>`__ of specific qubes
  (`#9622 <https://github.com/QubesOS/qubes-issues/issues/9622>`__).

- UUID support for qubes and support for addressing them by UUID in policies
  (`#8862 <https://github.com/QubesOS/qubes-issues/issues/8862>`__ &
  `#8510 <https://github.com/QubesOS/qubes-issues/issues/8510>`__).

- `Custom persist feature <https://dev.qubes-os.org/projects/core-admin-client/en/latest/manpages/qvm-features.html#custom-persist>`__ to avoid unwanted data to persist as much as possible
  (`#1006 <https://github.com/QubesOS/qubes-issues/issues/1006>`__).

Anonymity improvements
----------------------

- Disallowing files, URLs, or any application from Whonix-Workstation
  qubes to be opened in non-Whonix disposable
  (`#10051 <https://github.com/QubesOS/qubes-issues/issues/10051>`__).

- Preventing users from changing their Whonix Workstation qubes’ netvm
  to ``sys-firewall`` (or other clearnet netvms) to avoid IP leaks
  (`#8551 <https://github.com/QubesOS/qubes-issues/issues/8551>`__).

- kloak: Keystroke-level online anonymization kernel
  (`#1850 <https://github.com/QubesOS/qubes-issues/issues/1850>`__).

Performance optimizations
-------------------------

- Option to use volumes directly without snapshots
  (`#8767 <https://github.com/QubesOS/qubes-issues/issues/8767>`__).

- Retiring ``qubes-rpc-multiplexer`` and directly executing the command from c
  (`#9062 <https://github.com/QubesOS/qubes-issues/issues/9062>`__).

- Caching "system info" structure for qrexec policy evaluation
  (`#9362 <https://github.com/QubesOS/qubes-issues/issues/9362>`__).

- Minimal state qubes to make NetVM and USBVM to consume as little RAM as
  possible.

Updating & upgrading
--------------------

- Ability to always hide specific TemplateVMs and StandaloneVMs from
  update tools
  (`#9029 <https://github.com/QubesOS/qubes-issues/issues/9029>`__).

- pacman hook to notify dom0 about successful manual Archlinux upgrades
  (`#9233 <https://github.com/QubesOS/qubes-issues/issues/8307>`__),

- Improved R4.2 -> R4.3 upgrade tool
  (`#9317 <https://github.com/QubesOS/qubes-issues/issues/9317>`__),

  - Using `lvmdevices` feature instead of device filter
    (`#9421 <https://github.com/QubesOS/qubes-issues/issues/9421>`__).

New/Improved experimental features
----------------------------------

- Support for Ansible
  (`#10004 <https://github.com/QubesOS/qubes-issues/issues/10004>`__).

- Support for `Qubes
  Air <https://www.qubes-os.org/news/2018/01/22/qubes-air/>`__
  (`#9015 <https://github.com/QubesOS/qubes-issues/issues/9015>`__).

  - qrexec protocol extension to support sending source information to
    destination
    (`#9475 <https://github.com/QubesOS/qubes-issues/issues/9475>`__).

- Better support for GUIVM.

  - GUI/Admin domain splitting
    (`#833 <https://github.com/QubesOS/qubes-issues/issues/833>`__).

  - Automatically removing ‘nomodeset’ boot option when GPU is attached
    (`#9792 <https://github.com/QubesOS/qubes-issues/issues/9792>`__).

- Initial basic steps to support Wayland session only in GUIVM (but not GUI
  daemon/agent intra-communication)
  (`#8515 <https://github.com/QubesOS/qubes-issues/issues/8515>`__ &
  `#8410 <https://github.com/QubesOS/qubes-issues/issues/8410>`__).

Other
-----

- Allowing user to add free-form text to qubes (for descriptions, notes,
  comments, remarks, reminders, etc.)
  (`#899 <https://github.com/QubesOS/qubes-issues/issues/899>`__).

  |Screenshot of Qube Settings Notes|

- Automatically clean up `QubesIncoming` directory if empty
  (`#8307 <https://github.com/QubesOS/qubes-issues/issues/8307>`__).

- `vm-config.* <https://dev.qubes-os.org/projects/core-admin-client/en/latest/manpages/qvm-features.html#vm-config>`__ features to pass external configuration to inside the qube (`#9837 <https://github.com/QubesOS/qubes-issues/issues/9837>`__).

- Admin API for reading/writing denied device-interface list
  (`#9674 <https://github.com/QubesOS/qubes-issues/issues/9674>`__).

- New Devices API for salt
  (`#9753 <https://github.com/QubesOS/qubes-issues/issues/9753>`__).

Dropped or replaced features
----------------------------

- Default screen locker is changed from :program:`XScreenSaver` to :program:`xfce4-screensaver`

- :program:`Create Qubes VM` is retired in favor of the improved :program:`Create New Qube` (`#6561 <https://github.com/QubesOS/qubes-issues/issues/6561>`__).

- Windows 7 support is dropped from QWT.

For a full list, including more detailed descriptions, please see
`here <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue%20label%3Atargets-4.3>`__.

Known issues
============

- Templates restored in 4.3 from a pre-4.3 backup continue to target
  their original Qubes OS release repos. If you are using fresh
  templates on a clean 4.3 installation, or if you performed an
  :ref:`in-place upgrade from 4.2 to 4.3 <user/downloading-installing-upgrading/upgrade/4_3:in-place upgrade>`,
  then this does not affect you. (For more information, see issue
  `#8701 <https://github.com/QubesOS/qubes-issues/issues/8701>`__.)

Also see the `full list of open bug reports affecting Qubes
4.3 <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue%20label%3Aaffects-4.3%20is%3Aopen%20type%3ABug>`__.

We strongly recommend :doc:`updating Qubes OS </user/how-to-guides/how-to-update>`
immediately after installation in order to apply all available bug fixes.

Notes
=====

- Additional notes for future release candidates will be added here

Download
========

All Qubes ISOs and associated :doc:`verification files </project-security/verifying-signatures>`
are available on the `downloads <https://www.qubes-os.org/downloads/>`__ page.

Installation instructions
=========================

See the :doc:`installation guide </user/downloading-installing-upgrading/installation-guide>`.

Upgrading
=========

Please see :doc:`how to upgrade to Qubes 4.3 </user/downloading-installing-upgrading/upgrade/4_3>`.

.. |Screenshot of QWT, Welcome page| image:: /attachment/doc/4-3_qwt-hi.png
   :alt: Windows 11 welcome page after installation in an HVM
   :width: 100%

.. |Screenshot of QWT, Windows 11| image:: /attachment/doc/4-3_qwt-win11.png
   :alt: Windows 11 within an HVM qube showing file explorer
   :width: 100%

.. |Screenshot of Device UX assignments| image:: /attachment/doc/4-3_device-ux-assignments.png
   :alt: Device Assignments page in Global Config
   :width: 100%

.. |Screenshot of Device UX deny attachment| image:: /attachment/doc/4-3_device-ux-deny-attachment.png
   :alt: Deny device attachment config in Global Config
   :width: 100%

.. |Screenshot of Device UX edit assignment| image:: /attachment/doc/4-3_device-ux-edit-assignment.png
   :alt: Editing device assignment for a network interface in Global Config
   :width: 100%

.. |Screenshot of Device UX required devices| image:: /attachment/doc/4-3_device-ux-required-device.png
   :alt: Editing a required device in Global Config
   :width: 100%

.. |Screenshot of Device UX Qubes Devices widget| image:: /attachment/doc/4-3_qui-devices.png
   :alt: Redesigned Qubes Devices widget
   :width: 100%

.. |Screenshot of Qube Manager in 4.3| image:: /attachment/doc/4-3_manager.png
   :alt: Qube Manager with improved flat icons in 4.3
   :width: 100%

.. |Screenshot of Qube Manager in 4.2| image:: /attachment/doc/4-2_manager.png
   :alt: Qube Manager with improved flat icons in 4.2
   :width: 100%

.. |Screenshot of Qube Settings Applications in 4.3| image:: /attachment/doc/4-3_vmsettings-applications.png
   :alt: Qube settings showing icons of Apps in 4.3
   :width: 100%

.. |Screenshot of Qube Settings Applications in 4.2| image:: /attachment/doc/4-2_vmsettings-applications.png
   :alt: Qube settings showing icons of Apps in 4.2
   :width: 100%

.. |Screenshot of Qube Settings Notes| image:: /attachment/doc/4-3_notes.png
   :alt: Qube settings showing qube notes
   :width: 100%

