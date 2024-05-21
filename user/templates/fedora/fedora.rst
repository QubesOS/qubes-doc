================
Fedora templates
================


The Fedora :doc:`template </user/templates/templates>` is the default template in
Qubes OS. This page is about the standard (or “full”) Fedora template.
For the minimal and Xfce versions, please see the :doc:`Minimal templates </user/templates/minimal-templates>` and :doc:`Xfce templates </user/templates/xfce-templates>` pages.

Installing
----------


To :ref:`install <user/templates/templates:installing>` a specific Fedora template
that is not currently installed in your system, use the following
command in dom0:

.. code:: bash

      $ sudo qubes-dom0-update qubes-template-fedora-XX



(Replace ``XX`` with the Fedora version number of the template you wish
to install.)

To reinstall a Fedora template that is already installed in your system,
see :doc:`How to Reinstall a template </user/how-to-guides/how-to-reinstall-a-template>`.

After Installing
----------------


After installing a fresh Fedora template, we recommend performing the
following steps:

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


There are two ways to upgrade your template to a new Fedora release:

- **Recommended:** `Install a fresh template to replace the existing one. <#installing>`__ **This option may be simpler for less experienced users.** After you install the new template, redo all
  desired template modifications and :ref:`switch everything that was set to the old template to the new template <user/templates/templates:switching>`.
  You may want to write down the modifications you make to your
  templates so that you remember what to redo on each fresh install. To
  see a log of package manager actions, open a terminal in the old
  Fedora template and use the ``dnf history`` command.

- **Advanced:** :doc:`Perform an in-place upgrade of an existing Fedora template. </user/templates/fedora/fedora-upgrade>` This option
  will preserve any modifications you’ve made to the template, **but it may be more complicated for less experienced users.**


