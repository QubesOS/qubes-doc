==============
Xfce templates
==============


If you would like to use Xfce (more lightweight compared to GNOME desktop environment) Linux distribution in your qubes, you can install one of the available Xfce templates for :doc:`Fedora </user/templates/fedora/fedora>`, :doc:`Debian </user/templates/debian/debian>`, :topic:`Gentoo <19007>` or :topic:`CentOS* <19006>`.

\* *The CentOS version used by this template reached* :wikipedia:`End-of-Life in June 2024 <CentOS_Stream#Release_history>` *and is no longer receiving updates. Due to a lack of specific interest at this time a proposal to create a new CentOS 10 template was* :issue:`declined <9716>` *.*

Installation
------------


The Fedora Xfce templates can be installed with the following command (where ``X`` is your desired distro and version number):

.. code:: bash

      [user@dom0 ~]$ sudo qubes-dom0-update qubes-template-X-xfce


If your desired version is not found, it may still be in :doc:`testing </user/downloading-installing-upgrading/testing>`. You may wish to try again with the testing repository enabled:

.. code:: bash

      [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-itl-testing qubes-template-X-xfce


If you would like to install a community distribution such as Gentoo, try the install command by enabling the community repository:

.. code:: bash

      [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community qubes-template-X-xfce


If your desired version is not found, it may still be in :doc:`testing </user/downloading-installing-upgrading/testing>`. You may wish to try again with the testing repository enabled:

.. code:: bash

      [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community-testing qubes-template-X-xfce


The download may take a while depending on your connection speed.

To reinstall a Xfce template that is already installed in your system, see :doc:`How to Reinstall a template </user/how-to-guides/how-to-reinstall-a-template>`.
