=========================================
How to upgrade a Debian template in-place
=========================================

.. warning::

      This page is intended for advanced users.

.. DANGER::

      **Warning:** This page is intended for advanced users only. Most users seeking to upgrade should instead :ref:`install a new Debian template <user/templates/debian/debian:installing>`. Learn more about the two options :ref:`here <user/templates/debian/debian:upgrading>`.

This page provides instructions for performing an in-place upgrade of an installed :doc:`Debian Template </user/templates/debian/debian>`. If you wish to install a new, unmodified Debian template instead of upgrading a template that is already installed in your system, please see the :doc:`Debian Template </user/templates/debian/debian>` page instead. (:ref:`Learn more about the two options. <user/templates/debian/debian:upgrading>`) In general, upgrading a Debian template follows the same process as `upgrading a native Debian system <https://wiki.debian.org/DebianUpgrade>`__.

Summary instructions for Debian templates
-----------------------------------------


**Important:** The prompt on each line indicates where each command should be entered: ``dom0``, ``debian-<old>``, or ``debian-<new>``, where ``<old>`` is the Debian version number *from* which you are upgrading, and ``<new>`` is the Debian version number *to* which you are upgrading. The instructions may differ for certain releases. See :ref:`user/templates/debian/debian-upgrade:release-specific notes` for any instructions specific to your particular release.

.. code:: console

      [user@dom0 ~]$ qvm-clone debian-<old> debian-<new>
      [user@dom0 ~]$ qvm-run -a debian-<new> gnome-terminal
      [user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list
      [user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list.d/qubes-r4.list
      [user@debian-<new> ~]$ sudo apt update
      [user@debian-<new> ~]$ sudo apt upgrade
      [user@debian-<new> ~]$ sudo apt dist-upgrade
      [user@dom0 ~]$ qvm-shutdown debian-<new>


**Recommended:** :ref:`Switch everything that was set to the old template to the new template. <user/templates/templates:switching>`

Detailed instructions for Debian templates
------------------------------------------


These instructions will show you how to upgrade Debian templates. The same general procedure may be used to upgrade any template based on the standard Debian template.

**Important:** The prompt on each line indicates where each command should be entered: ``dom0``, ``debian-<old>``, or ``debian-<new>``, where ``<old>`` is the Debian version number *from* which you are upgrading, and ``<new>`` is the Debian version number *to* which you are upgrading. The instructions may differ for certain releases. See :ref:`user/templates/debian/debian-upgrade:release-specific notes` for any instructions specific to your particular release.

1. Ensure the existing template is not running.

   .. code:: console

         [user@dom0 ~]$ qvm-shutdown debian-<old>


2. Clone the existing template and start a terminal in the new template.

   .. code:: console

         [user@dom0 ~]$ qvm-clone debian-<old> debian-<new>
         [user@dom0 ~]$ qvm-run -a debian-<new> gnome-terminal


3. Update your ``apt`` repositories to use the new release’s code name instead of the old release’s code name. (This can be done manually with a text editor, but ``sed`` can be used to automatically update the files.)

   .. code:: console

         [user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list
         [user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list.d/qubes-r4.list



4. Update the package lists and upgrade. During the process, it may prompt you to overwrite the file ``qubes-r4.list``. You should overwrite this file.

   .. code:: console

         [user@debian-<new> ~]$ sudo apt update
         [user@debian-<new> ~]$ sudo apt upgrade
         [user@debian-<new> ~]$ sudo apt dist-upgrade



5. (Optional) Remove unnecessary packages that were previously installed.

   .. code:: console

         [user@debian-<new> ~]$ sudo apt-get autoremove



6. (Optional) Clean cached packages from ``/var/cache/apt``.

   .. code:: console

         [user@debian-<new> ~]$ sudo apt-get clean



7. (Optional) Trim the new template. (This should :ref:`no longer be necessary <user/templates/templates:important notes>`, but it does not hurt. Some users have `reported <https://github.com/QubesOS/qubes-issues/issues/5055>`__ that it makes a difference.)

   .. code:: console

         [user@debian-<new> ~]$ sudo fstrim -av
         [user@dom0 ~]$ qvm-shutdown debian-<new>
         [user@dom0 ~]$ qvm-start debian-<new>
         [user@debian-<new> ~]$ sudo fstrim -av


8. Shut down the new template.

   .. code:: console

         [user@dom0 ~]$ qvm-shutdown debian-<new>


9. (Recommended) :ref:`Switch everything that was set to the old template to the new template. <user/templates/templates:switching>`

10. (Optional) Make the new template the global default.

    .. code:: console

          [user@dom0 ~]$ qubes-prefs --set default_template debian-<new>


11. (Optional) :ref:`Uninstall the old template. <user/templates/templates:uninstalling>` Make sure that the template you’re uninstalling is the old one, not the new one!



Standalones
-----------


The procedure for upgrading a Debian :doc:`standalone </user/advanced-topics/standalones-and-hvms>` is the same as for a template.

Release-specific notes
----------------------


This section contains notes about upgrading to specific releases.

Debian 11 ("Bullseye")
^^^^^^^^^^^^^^^^^^^^^^


Please see `Debian’s Bullseye upgrade instructions <https://www.debian.org/releases/bullseye/amd64/release-notes/ch-upgrading.en.html>`__. In particular: for APT source lines referencing the security archive, the format has changed slightly along with the release name, going from buster/updates to bullseye-security; see `Section 5.1.2, “Changed security archive layout” <https://www.debian.org/releases/stable/mips64el/release-notes/ch-information.en.html#security-archive>`__.

This means that, when upgrading from Buster to Bullseye, an additional ``sed`` command is required:

.. code:: console

      [user@dom0 ~]$ qvm-clone debian-10 debian-11
      [user@dom0 ~]$ qvm-run -a debian-11 gnome-terminal
      [user@debian-<new> ~]$ sudo sed -i 's/buster/bullseye/g' /etc/apt/sources.list
      [user@debian-<new> ~]$ sudo sed -i 's/debian-security bullseye\/updates/debian-security bullseye-security/g' /etc/apt/sources.list
      [user@debian-<new> ~]$ sudo sed -i 's/buster/bullseye/g' /etc/apt/sources.list.d/qubes-r4.list
      [user@debian-<new> ~]$ sudo apt update
      [user@debian-<new> ~]$ sudo apt upgrade
      [user@debian-<new> ~]$ sudo apt dist-upgrade
      [user@dom0 ~]$ qvm-shutdown debian-11


Debian 10 ("Buster")
^^^^^^^^^^^^^^^^^^^^


Please see `Debian’s Buster upgrade instructions <https://www.debian.org/releases/buster/amd64/release-notes.en.txt>`__.

Debian 9 ("Stretch")
^^^^^^^^^^^^^^^^^^^^


- The upgrade process may prompt you to overwrite two files: ``qubes-r4.list`` and ``pulse/client.conf``. ``qubes-r4.list`` can be overwritten, but ``pulse/client.conf`` must be left as the currently-installed version.

- If sound is not working, you may need to enable the Qubes testing repository to get the testing version of ``qubes-gui-agent``. This can be done by editing the ``/etc/apt/sources.list.d/qubes-r4.list`` file and uncommenting the ``Qubes Updates Candidates`` repo.

- User-initiated updates/upgrades may not run when a template first starts. This is due to a new Debian config setting that attempts to update automatically; it should be disabled with ``sudo systemctl disable apt-daily.{service,timer}``.



Relevant discussions:

- `Stretch Template Installation <https://groups.google.com/forum/#!topicsearchin/qubes-devel/debian$20stretch/qubes-devel/4rdayBF_UTc>`__

- `Stretch availability in 3.2 <https://groups.google.com/forum/#!topicsearchin/qubes-devel/debian$20stretch/qubes-devel/cekPfBqQMOI>`__

- `Fixing sound in Debian Stretch <https://groups.google.com/forum/#!topic/qubes-users/JddCE54GFiU>`__

- `User apt commands blocked on startup <https://github.com/QubesOS/qubes-issues/issues/2621>`__



Also see `Debian’s Stretch upgrade instructions <https://www.debian.org/releases/stretch/amd64/release-notes.en.txt>`__.

Debian 8 ("Jessie")
^^^^^^^^^^^^^^^^^^^


Please see `Debian’s Jessie upgrade instructions <https://www.debian.org/releases/jessie/amd64/release-notes.en.txt>`__.

End-of-life (EOL) releases
^^^^^^^^^^^^^^^^^^^^^^^^^^


We strongly recommend against using any Debian release that has reached `end-of-life (EOL) <https://wiki.debian.org/DebianReleases#Production_Releases>`__.

Additional information
----------------------


- Please note that, if you installed packages from one of the :doc:`testing </user/downloading-installing-upgrading/testing>` repositories, you must make sure that the repository is enabled in ``/etc/apt/sources.list.d/qubes-r4.list`` before attempting the upgrade. Otherwise, your upgrade will `break <https://github.com/QubesOS/qubes-issues/issues/2418>`__.

- By default, Qubes uses code names in the ``apt`` sources files, although the templates are referred to by release number. Check the code names for the templates, and ensure you are aware of any changes you have made in the repository definitions.


