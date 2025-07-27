========================
Disposable customization
========================

.. warning::

      This page is intended for advanced users.

Introduction
------------


A :doc:`disposable </user/how-to-guides/how-to-use-disposables>` can be based on any :ref:`app qube <user/reference/glossary:app qube>`. You can also choose to use different :ref:`disposable templates <user/reference/glossary:disposable template>` for different disposables. To prepare an app qube to be a disposable template, you need to set the ``template_for_dispvms`` property:

.. code:: console

      [user@dom0 ~]$ qvm-prefs <DISPOSABLE_TEMPLATE> template_for_dispvms True


Additionally, if you want to have menu entries for starting applications in disposables based on this app qube (instead of in the app qube itself), you can achieve that with the ``appmenus-dispvm`` feature:

.. code:: console

      [user@dom0 ~]$ qvm-features <DISPOSABLE_TEMPLATE> appmenus-dispvm 1


**Note:** Application shortcuts that existed before setting this feature will not be updated automatically. Please go the “Applications” tab in the qube’s “Settings” dialog and unselect all existing shortcuts by clicking “«”, then click “OK” and close the dialog. Give it a few seconds time and then reopen and re-select all the shortcuts you want to see in the menu. See :doc:`this page </user/troubleshooting/app-menu-shortcut-troubleshooting>` for background information.

Security
--------


If a disposable template becomes compromised, then any disposable based on that disposable template could be compromised. Therefore, you should not make any risky customizations (e.g., installing untrusted browser plugins) in important disposable templates. In particular, the *default* disposable template is important because it is used by the “Open in disposable” feature. This means that it will have access to everything that you open with this feature. For this reason, it is strongly recommended that you base the default disposable template on a trusted template and refrain from making any risky customizations to it.

Creating a new disposable template
----------------------------------


In Qubes 4.0, you’re no longer restricted to a single disposable template. Instead, you can create as many as you want. Whenever you start a new disposable, you can choose to base it on whichever disposable template you like. To create a new disposable template:

.. code:: console

      [user@dom0 ~]$ qvm-create --template <TEMPLATE> --label red <DISPOSABLE_TEMPLATE>
      [user@dom0 ~]$ qvm-prefs <DISPOSABLE_TEMPLATE> template_for_dispvms True
      [user@dom0 ~]$ qvm-features <DISPOSABLE_TEMPLATE> appmenus-dispvm 1


Optionally, set it as the default disposable template:

.. code:: console

      [user@dom0 ~]$ qubes-prefs default_dispvm <DISPOSABLE_TEMPLATE>


The above default is used whenever a qube request starting a new disposable and do not specify which one (for example ``qvm-open-in-dvm`` tool). This can be also set in qube settings and will affect service calls from that qube. See :ref:`qrexec documentation <developer/services/qrexec:specifying vms: tags, types, targets, etc.>` for details.

If you wish to use a :doc:`minimal template </user/templates/minimal-templates>` as a disposable template, please see the :doc:`minimal template </user/templates/minimal-templates>` page.

Customization of disposable
---------------------------


**Note:** *If you are trying to customize Tor Browser in a Whonix disposable, please consult the* `Whonix documentation <https://www.whonix.org/wiki/Tor_Browser/Advanced_Users#disposable_Template_Customization>`__ *.*

It is possible to change the settings for each new disposable. This can be done by customizing the disposable template on which it is based:

1. Start a terminal in the ``<DISPOSABLE_TEMPLATE>`` qube (or another disposable template) by running the following command in a dom0 terminal. (If you enable ``appmenus-dispvm`` feature (as explained at the top), applications menu for this VM (``<DISPOSABLE_TEMPLATE>``) will be “Disposable: ” (instead of “Domain: ”) and entries there will start new disposable based on that VM (``<DISPOSABLE_TEMPLATE>``). Not in that VM (``<DISPOSABLE_TEMPLATE>``) itself).

   .. code:: console

         [user@dom0 ~]$ qvm-run -a <DISPOSABLE_TEMPLATE> gnome-terminal


2. Change the qube’s settings and/or applications, as desired. Some examples of changes you may want to make include:

   - Changing Firefox’s default startup settings and homepage.

   - Changing default editor, image viewer. In Debian-based templates this can be done with the ``mimeopen`` command.

   - Changing the disposable’s default NetVM. For example, you may wish to set the NetVM to “none.” Then, whenever you start a new disposable, you can choose your desired ProxyVM manually (by changing the newly-started disposables settings). This is useful if you sometimes wish to use a disposable with a Whonix Gateway, for example. It is also useful if you sometimes wish to open untrusted files in a network-disconnected disposable.



3. Shutdown the qube (either by ``poweroff`` from qube’s terminal, or ``qvm-shutdown`` from dom0 terminal).



Using named disposables for service qubes
-----------------------------------------


You can use a :ref:`named disposable <user/reference/glossary:named disposable>` for service qubes (such as those with the ``sys-*`` naming scheme) as long as they are stateless. For example, a ``sys-net`` using DHCP or ``sys-usb`` will work. In most cases ``sys-firewall`` will also work, even if you have configured app qube firewall rules. The only exception is if you require something like VM to VM communication and have manually edited ``iptables`` or other items directly inside the firewall app qube.

To create one that has no PCI devices attached, such as for ``sys-firewall``:

.. code:: bash

      qvm-create -C DispVM -l green <SERVICE_QUBE>
      qvm-prefs <SERVICE_QUBE> autostart true
      qvm-prefs <SERVICE_QUBE> netvm <NET_QUBE>
      qvm-prefs <SERVICE_QUBE> provides_network true
      qvm-features <SERVICE_QUBE> appmenus-dispvm ''



Next, set the old ``sys-firewall`` autostart to false, and update any references to the old one to instead point to the new, for example, with ``qvm-prefs work netvm sys-firewall2``.

To create one with a PCI device attached such as for ``sys-net`` or ``sys-usb``, use the additional commands as follows.

**Note:** You can use ``qvm-pci`` to :ref:`determine <user/how-to-guides/how-to-use-pci-devices:\`\`qvm-pci\`\` usage>` the ``<BDF>``. Also, you will often need to include the ``-o no-strict-reset=True`` :ref:`option <user/how-to-guides/how-to-use-pci-devices:no-strict-reset>` with USB controllers.

.. code:: bash

      qvm-create -C DispVM -l red <SERVICE_QUBE>
      qvm-prefs <SERVICE_QUBE> virt_mode hvm
      qvm-service <SERVICE_QUBE> meminfo-writer off
      qvm-pci attach --persistent <SERVICE_QUBE> dom0:<BDF>
      qvm-prefs <SERVICE_QUBE> autostart true
      qvm-prefs <SERVICE_QUBE> netvm ''
      qvm-features <SERVICE_QUBE> appmenus-dispvm ''



Optionally, if this disposable will also provide network access to other qubes:

.. code:: bash

      qvm-prefs <SERVICE_QUBE> provides_network true



Next, set the old service qube’s autostart to false, and update any references to the old one, e.g.:

.. code:: bash

      qvm-prefs sys-firewall netvm <SERVICE_QUBE>



Also make sure to update any :doc:`RPC policies </user/advanced-topics/rpc-policy>`, if needed.

Here is an example of a complete ``sys-net`` replacement:

.. code:: bash

      qvm-create -C DispVM -l red sys-net2
      qvm-prefs sys-net2 virt_mode hvm
      qvm-service sys-net2 meminfo-writer off
      qvm-pci attach --persistent sys-net2 dom0:00_1a.0
      qvm-prefs sys-net2 autostart true
      qvm-prefs sys-net2 netvm ''
      qvm-features sys-net2 appmenus-dispvm ''
      qvm-prefs sys-net2 provides_network true
      qvm-prefs sys-net autostart false
      qvm-prefs sys-firewall netvm sys-net2
      qubes-prefs clockvm sys-net2



Adding programs to the app menu
-------------------------------


For added convenience, arbitrary programs can be added to the app menu of the disposable.

In order to do that, select “Qube settings” entry in selected base app qube, go to “Applications” tab and select desired applications as for any other qube.

Note that currently only applications whose main process keeps running until you close the application (i.e. do not start a background process instead) will work. One of known examples of incompatible applications is GNOME Terminal (shown on the list as “Terminal”). Choose different terminal emulator (like XTerm) instead.

Deleting disposables
--------------------


While working in a disposable, you may want to open a document in another disposable. For this reason, the property ``default_dispvm`` may be set to the name of your disposable in a number of qubes:

.. code:: console

      [user@dom0 ~]$ qvm-prefs <QUBE> | grep default_dispvm
      default_dispvm        -  <DISPOSABLE_TEMPLATE>


This will prevent the deletion of the disposable template. In order to fix this, you need to unset the ``default_dispvm`` property:

.. code:: console

      [user@dom0 ~]$ qvm-prefs <QUBE> default_dispvm ""


You can then delete the disposable template:

.. code:: console

      [user@dom0 ~]$ qvm-remove <DISPOSABLE_TEMPLATE>
      This will completely remove the selected VM(s)
        <DISPOSABLE_TEMPLATE>


If you still encounter a problem, you may have forgotten to clean an entry. Looking at the system logs will help you:

.. code:: console

      [user@dom0 ~]$ journalctl | tail

