================
Debian templates
================


The Debian :term:`template` is an officially :ref:`supported <user/downloading-installing-upgrading/supported-releases:templates>` template in Qubes OS. The Current version is Debian |debian-version| (“|debian-codename|”). It is available in 3 versions - ``debian-12``, a standard template; ``debian-12-xfce``, a larger template with more installed applications, selected for :doc:`Xfce </user/templates/xfce-templates>`; ``debian-12-minimal``. This page is about the “full” templates. For the minimal version, please see the :doc:`Minimal templates </user/templates/minimal-templates>` page.

Installing
----------


To :ref:`install <user/templates/templates:installing>` a specific Debian template that is not currently installed in your system, use the Qubes Template Manager, or use the following command in a dom0 terminal:

.. code:: console

      $ qvm-template install XX



(Replace ``XX`` with the name of the template you wish to install.)

To reinstall a Debian template that is already installed in your system, see :doc:`How to Reinstall a template </user/how-to-guides/how-to-reinstall-a-template>`.

After Installing
----------------


After installing a fresh Debian template, we recommend performing the following steps:

1. :doc:`Update the template </user/how-to-guides/how-to-install-software>`.

2. :ref:`Switch any app qubes that are based on the old template to the new one <user/templates/templates:switching>`.

3. If desired, :ref:`uninstall the old template <user/templates/templates:uninstalling>`.



Installing software
-------------------


See :doc:`How to Install Software </user/how-to-guides/how-to-install-software>`.

Updating
--------


For routine daily updates within a given release, see :doc:`How to Update </user/how-to-guides/how-to-update>`.

Upgrading
---------


There are two ways to upgrade your template to a new Debian release:

- **Recommended:** `Install a fresh template to replace the existing one. <#installing>`__ **This option may be simpler for less experienced users.** After you install the new template, redo all desired template modifications and :ref:`switch everything that was set to the old template to the new template <user/templates/templates:switching>`. You may want to write down the modifications you make to your templates so that you remember what to redo on each fresh install. In the old Debian template, see ``/var/log/dpkg.log`` and ``/var/log/apt/history.log`` for logs of package manager actions.

- **Advanced:** :doc:`Perform an in-place upgrade of an existing Debian template. </user/templates/debian/debian-upgrade>` This option will preserve any modifications you’ve made to the template, **but it may be more complicated for less experienced users.**



Release-specific notes
----------------------


This section contains notes about specific Debian releases.

Debian 12
^^^^^^^^^


The Debian-12 templates that ship with release 4.2.4 cannot be used for salting Fedora templates. You must change the template used by ``default-mgmt-dvm`` to a Fedora template. You can do this in the Qubes Template Switcher tool, or at the command line using ``qvm-prefs default-mgmt-dvm template``.

If you have a Debian template from an earlier release that you want to use for salting Qubes, you **must** stop the salt-common and salt-ssh packages from being upgraded. Do this by marking these packages on hold *before* updating the template.

.. code:: console

      $ sudo apt-mark hold salt-common salt-ssh
      $ sudo apt update
      $ sudo apt upgrade



This is a `known bug <https://github.com/QubesOS/qubes-issues/issues/9129>`__ in Salt which affects version 3006-5.

Starting services
^^^^^^^^^^^^^^^^^


The Debian way (generally) is to start daemons if they are installed. This means that if you install (say) ssh-server in a template, *all* the qubes that use that template will run a ssh server when they start. (They will, naturally, all have the same server key.) This may not be what you want.

So be very careful when installing software in Templates - if the daemon spawns outbound connections then there is a serious security risk.

In general, a reasonable approach would be, (using ssh as example):

- Install the ssh service.

- ``systemctl stop ssh``

- ``systemctl disable ssh``

- ``systemctl mask ssh``

- Close down template



Now the ssh service will **NOT** start in qubes based on this template.

Where you **DO** want the service to run, put this in ``/rw/config/rc.local``:

.. code:: bash

      systemctl unmask ssh
      systemctl start ssh



Don’t forget to make the file executable.

Unattended Upgrades
^^^^^^^^^^^^^^^^^^^


Some users have noticed that on upgrading Debian templates, the ``unattended-upgrade`` package is installed. This package is pulled in as part of a Recommend chain, and can be purged. The lesson is that you should carefully look at what is being installed to your system, particularly if you run ``dist-upgrade``.

Package installation errors in Qubes 4.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If some packages throw installation errors, see :ref:`this guide. <user/troubleshooting/vm-troubleshooting:fixing package installation errors>`
