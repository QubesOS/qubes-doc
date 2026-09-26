.. There are currently no release-specific notes, so related sentences and section are commented out.

=========================================
How to upgrade a Debian template in-place
=========================================

.. warning::
   This page is intended for advanced users.

   Most users will find it easier to :ref:`install a new template <user/templates/debian/debian:installing>` instead of upgrading in-place.
   If you have made customizations or installed additional packages in the current template that you want to preserve, then upgrading in-place may be the best way to go.

    
This page provides instructions for performing an in-place upgrade of an installed :doc:`Debian Template </user/templates/debian/debian>`. In general, upgrading a Debian template follows the same process as `upgrading a native Debian system <https://wiki.debian.org/DebianUpgrade>`__.

.. note::
 In what follows the prompt on each line indicates where each command should be entered: ``dom0``, ``debian-<old>``, or ``debian-<new>``, where ``<old>`` is the Debian version number *from* which you are upgrading, and ``<new>`` is the Debian version number *to* which you are upgrading. Remember to use the right template *version*: eg clone ``debian-<old>-minimal`` to ``debian-<new>-minimal``. 

 By default, Qubes uses code `names` in the apt sources files (bookworm, trixie, etc), although the templates are referred to by release number. Check the code names for the templates, and ensure you are aware of any changes you have made in the repository definitions.

Automated upgrade with qvm-template-upgrade
-------------------------------------------


The `qvm-template-upgrade <https://github.com/QubesOS/qubes-core-admin-linux/blob/main/doc/tools/qvm-template-upgrade.rst>`__ tool automates the clone-and-upgrade procedure described on this page: it clones the template, upgrades the clone to the next Debian release (including updating the ``apt`` sources to the new release's code name), and sets the ``template-name`` feature used by the Qubes updater.

.. code:: console

      [user@dom0 ~]$ qvm-template-upgrade --template=debian-<old>

By default, the clone is named by replacing the release number in the source name, e.g. ``debian-12`` becomes ``debian-13`` and ``debian-12-minimal`` becomes ``debian-13-minimal``. Use ``--new-name=<NAME>`` to choose a different name, and ``--dry-run`` to preview the planned upgrade without creating a clone.

After the upgrade completes, remember to :ref:`switch everything that was set to the old template to the new template <user/templates/templates:switching>` and, optionally, make the new template the global default and uninstall the old template, as described in the manual instructions below. Use the manual instructions if you need finer control over the upgrade process or if the automated upgrade fails.

Summary instructions for Debian templates
-----------------------------------------

.. code:: console

      [user@dom0 ~]$ qvm-clone debian-<old> debian-<new>
      [user@dom0 ~]$ qvm-run debian-<new> qubes-run-terminal &
      [user@debian-<new> ~]$ sudo apt update
      [user@debian-<new> ~]$ sudo apt upgrade
      [user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list
      [user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list.d/qubes-r4.list
      [user@debian-<new> ~]$ sudo apt update
      [user@debian-<new> ~]$ sudo apt upgrade
      [user@debian-<new> ~]$ sudo apt dist-upgrade
      [user@dom0 ~]$ qvm-shutdown debian-<new>
      [user@dom0 ~]$ qvm-features  debian-<new> template-name debian-<new>


Detailed instructions for Debian templates
------------------------------------------


These instructions will show you how to upgrade Debian templates. The same general procedure may be used to upgrade any template based on the standard Debian templates.

1. Ensure the existing template is not running.

   .. code:: console

         [user@dom0 ~]$ qvm-shutdown debian-<old>


2. Clone the existing template and start a terminal in the new template.

   .. code:: console

         [user@dom0 ~]$ qvm-clone debian-<old> debian-<new>
         [user@dom0 ~]$ qvm-run debian-<new> qubes-run-terminal

3. Update the new cloned template.

   .. code:: console

         [user@debian-<new> ~]$ sudo apt update
         [user@debian-<new> ~]$ sudo apt upgrade

4. Update your ``apt`` repositories to use the new release’s code name instead of the old release’s code name. (This can be done manually with a text editor, but ``sed`` can be used to automatically update the files.)

   .. code:: console

         [user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list
         [user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list.d/qubes-r4.list



5. Update the package lists and upgrade. During the process, it may prompt you to overwrite the file ``qubes-r4.list``. You should overwrite this file.

   .. code:: console

         [user@debian-<new> ~]$ sudo apt update
         [user@debian-<new> ~]$ sudo apt upgrade
         [user@debian-<new> ~]$ sudo apt dist-upgrade



6. (Optional) Remove unnecessary packages that were previously installed.

   .. code:: console

         [user@debian-<new> ~]$ sudo apt-get autoremove



7. (Optional) Clean cached packages from ``/var/cache/apt``.

   .. code:: console

         [user@debian-<new> ~]$ sudo apt-get clean



8. (Optional) Trim the new template. (This should :ref:`no longer be necessary <user/templates/templates:important notes>`, but it does not hurt. Some users have `reported <https://github.com/QubesOS/qubes-issues/issues/5055>`__ that it makes a difference.)

   .. code:: console

         [user@debian-<new> ~]$ sudo fstrim -av
         [user@dom0 ~]$ qvm-shutdown debian-<new>
         [user@dom0 ~]$ qvm-start debian-<new>
         [user@debian-<new> ~]$ sudo fstrim -av


9. Shut down the new template.

   .. code:: console

         [user@dom0 ~]$ qvm-shutdown debian-<new>


10. Set the template-name, which is used by the Qubes updater.

   .. code:: console

         [user@dom0 ~]$ qvm-features debian-<new> template-name debian-<new>


11. (Recommended) :ref:`Switch everything that was set to the old template to the new template. <user/templates/templates:switching>`



12. (Optional) Make the new template the global default.

    .. code:: console

          [user@dom0 ~]$ qubes-prefs --set default_template debian-<new>


12. (Optional) :ref:`Uninstall the old template. <user/templates/templates:uninstalling>` Make sure that the template you’re uninstalling is the old one, not the new one!

.. note::
 If you installed packages from one of the :doc:`testing </user/downloading-installing-upgrading/testing>` repositories, you **must** make sure that the repository is enabled in ``/etc/apt/sources.list.d/qubes-r4.list`` **before** attempting the upgrade. Otherwise, your upgrade will `break <https://github.com/QubesOS/qubes-issues/issues/2418>`__.


Standalones
-----------


The procedure for upgrading a Debian :doc:`standalone </user/advanced-topics/standalones-and-hvms>` is the same as for a template.

.. Release-specific notes
.. ----------------------

.. .. note:: This section contains notes about upgrading to specific releases.

End-of-life (EOL) releases
^^^^^^^^^^^^^^^^^^^^^^^^^^


We strongly recommend against using any Debian release that has reached `end-of-life (EOL) <https://wiki.debian.org/DebianReleases#Production_Releases>`__.

