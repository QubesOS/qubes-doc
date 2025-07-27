==========================
Qubes OS 4.2 release notes
==========================


New features and improvements since Qubes 4.1
---------------------------------------------


- Dom0 upgraded to Fedora 37 (:issue:`6982`)

- Xen upgraded to version 4.17

- Default Debian template upgraded to Debian 12

- Default Fedora and Debian templates use Xfce instead of GNOME (:issue:`7784`)

- SELinux support in Fedora templates (:issue:`4239`)

- Several GUI applications rewritten (screenshots below), including:

  - Applications Menu (also available as preview in R4.1) (:issue:`6665`), (:issue:`5677`)

  - Qubes Global Settings (:issue:`6898`)

  - Create New Qube

  - Qubes Update (:issue:`7443`)



- New ``qubes-vm-update`` tool (:issue:`7443`)

- Unified ``grub.cfg`` location for both UEFI and legacy boot (:issue:`7985`)

- PipeWire support (:issue:`6358`)

- fwupd integration for firmware updates (:issue:`4855`)

- Optional automatic clipboard clearing (:issue:`3415`)

- Official packages built using Qubes Builder v2 (:issue:`6486`)

- Split GPG management in Qubes Global Settings

- Qrexec services use new qrexec policy format by default (but old format is still supported) (:issue:`8000`)

- Improved keyboard layout switching



For a full list, including more detailed descriptions, please see `here <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+sort%3Aupdated-desc+milestone%3A%22Release+4.2%22+label%3A%22release+notes%22+is%3Aclosed>`__. Below are some screenshots of the new and improved Qubes GUI tools.

The new Qubes OS Update tool:

|Screenshot of the Qubes OS Update tool|

The new Qubes OS Global Config tool:

|Screenshot of the Qubes OS Global Config tool| |image1|

The new Qubes OS Policy Editor tool:

|Screenshot of the Qubes OS Policy Editor tool|

Known issues
------------


- DomU firewalls have completely switched to nftables. Users should add their custom rules to the ``custom-input`` and ``custom-forward`` chains. (For more information, see issues :issue:`5031` and :issue:`6062`.)

- Templates restored in 4.2 from a pre-4.2 backup continue to target their original Qubes OS release repos. If you are using fresh templates on a clean 4.2 installation, or if you performed an :ref:`in-place upgrade from 4.1 to 4.2 <user/downloading-installing-upgrading/upgrade/4_2:in-place upgrade>`, then this does not affect you. (For more information, see issue :issue:`8701`.)



Also see the `full list of open bug reports affecting Qubes 4.2 <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aissue+label%3Aaffects-4.2+label%3A%22T%3A+bug%22+is%3Aopen>`__.

We strongly recommend :doc:`updating Qubes OS </user/how-to-guides/how-to-update>` immediately after installation in order to apply all available bug fixes.

Notes
-----


- Qubes 4.2 does not support Debian 11 templates (see :ref:`supported template releases <user/downloading-installing-upgrading/supported-releases:templates>`). Please :ref:`upgrade your Debian templates <user/templates/debian/debian:upgrading>` to Debian 12.

- Qubes 4.2.2 includes a fix for :issue:`#8332: File-copy qrexec service is overly restrictive <8332>`. As explained in the issue comments, we introduced a change in Qubes 4.2.0 that caused inter-qube file-copy/move actions to reject filenames containing, e.g., non-Latin characters and certain symbols. The rationale for this change was to mitigate the security risks associated with unusual unicode characters and invalid encoding in filenames, which some software might handle in an unsafe manner and which might cause confusion for users. Such a change represents a trade-off between security and usability.

  - After the change went live, we received several user reports indicating more severe usability problems than we had anticipated. Moreover, these problems were prompting users to resort to dangerous workarounds (such as packing files into an archive format prior to copying) that carry far more risk than the original risk posed by the unrestricted filenames. In addition, we realized that this was a backward-incompatible change that should not have been introduced in a minor release in the first place.

  - Therefore, we have decided, for the time being, to restore the original (pre-4.2) behavior by introducing a new ``allow-all-names`` argument for the ``qubes.Filecopy`` service. By default, ``qvm-copy`` and similar tools will use this less restrictive service (``qubes.Filecopy +allow-all-names``) whenever they detect any files that would be have been blocked by the more restrictive service (``qubes.Filecopy +``). If no such files are detected, they will use the more restrictive service.

  - Users who wish to opt for the more restrictive 4.2.0 and 4.2.1 behavior can do so by modifying their RPC policy rules. To switch a single rule to the more restrictive behavior, change ``*`` in the argument column to ``+`` (i.e., change “any argument” to “only empty”). To use the more restrictive behavior globally, add the following “deny” rule before all other relevant rules:

    .. code:: bash

          qubes.Filecopy    +allow-all-names    @anyvm    @anyvm    deny



  - For more information, see :doc:`RPC policies </user/advanced-topics/rpc-policy>` and :ref:`Qube configuration interface <developer/debugging/vm-interface:qubes rpc>`.



- Beginning with Qubes 4.2, the recommended way to update Qubes OS via the command line has changed. Salt is no longer the preferred method, though it is still supported. Instead, ``qubes-dom0-update`` is recommended for updating dom0, and ``qubes-vm-update`` is recommended for updating templates and standalones. (The recommended way to update via the GUI has not changed. The Qubes Update tool is still the preferred method.) For more information, see :doc:`How to update </user/how-to-guides/how-to-update>`.



Download
--------


All Qubes ISOs and associated :doc:`verification files </project-security/verifying-signatures>` are available on the :website:`downloads <downloads/>` page.

Installation instructions
-------------------------


See the :doc:`installation guide </user/downloading-installing-upgrading/installation-guide>`.

Upgrading
---------


Please see :doc:`how to upgrade to Qubes 4.2 </user/downloading-installing-upgrading/upgrade/4_2>`.

.. |Screenshot of the Qubes OS Update tool| image:: /attachment/site/4-2_update.png
   

.. |Screenshot of the Qubes OS Global Config tool| image:: /attachment/site/4-2_global-config_1.png
   

.. |image1| image:: /attachment/site/4-2_global-config_2.png
   

.. |Screenshot of the Qubes OS Policy Editor tool| image:: /attachment/site/4-2_policy-editor.png
   
