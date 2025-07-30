=================================
App menu shortcut troubleshooting
=================================


For ease of use Qubes aggregates shortcuts to applications that are installed in app qubes and shows them in one application menu (aka “app menu” or “start menu”) in dom0. Clicking on such shortcut runs the assigned application in its app qube.

|image1|

How-to add a shortcut
---------------------


With the graphical user interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


To make applications newly installed show up in the menu, you can use the qube’s *Settings*. Under the *Applications* tab, use the *Refresh Applications* button. Linux qubes do this automatically, if the *Settings* are opened after the installation of the package.

|image2|

After that, use the directional buttons (``>``, ``>>``, ``<`` or ``<<``) to customize which applications are shown, by moving them to the *Applications shown in App Menu* part (on the right side). Use the *Apply* (or *Ok*) button to see the changes in the app menu.

With the command-line interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


To update the list of available applications, use the ``qvm-sync-appmenus`` command in dom0, replacing ``<QUBE_NAME>`` by the qube name:

.. code:: console

      $ qvm-sync-appmenus <QUBE_NAME>



When using the *Refresh Applications* button in a qube’s settings, the command ``qvm-sync-appmenus`` is used at least one time. When refreshing an AppVM application, it is also run against the template. So the console equivalent of clicking the *Refresh button* is the following (always in dom0):

.. code:: console

      $ qvm-sync-appmenus <APPVM_NAME>
      $ qvm-sync-appmenus <TEMPLATE_NAME>



In dom0, the ``qvm-appmenus`` tool allows the user to see the list of available applications (unstable feature), the whitelist of currently show application (unstable feature) and to change this list:

.. code:: console

      $ qvm-appmenus --set-whitelist <FILE_PATH> <QUBE_NAME>



To change the whitelist shown in app menu, you need to provide a list of the desktop entries. Each line contains a desktop entry name, with its ``.desktop`` extension, like this:

.. code:: console

      qubes-open-file-manager.desktop
      qubes-run-terminal.desktop
      [...]



You can replace the file path by a single hyphen (``-``) to read it from standard input.

What if my application has not been automatically included in the list of available apps?
-----------------------------------------------------------------------------------------


Missing desktop entry
^^^^^^^^^^^^^^^^^^^^^


Sometimes applications may not have included a ``.desktop`` file and may not be detected by ``qvm-sync-appmenus``. Other times, you may want to make a web shortcut available from the Qubes start menu.

You can manually create new entries in the “available applications” list of shortcuts for all app qubes based on a template. To do this:

1. Open a terminal window to the template.

2. Create a custom ``.desktop`` file in ``/usr/share/applications`` (you may need to first create the subdirectory). Look in ``/usr/share/applications`` for existing examples, or see the full `file specification <https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html>`__. It will be something like:

   .. code:: desktop

         [Desktop Entry]
         Type=Application
         Name=VueScan
         Exec=vuescan



3. Follow the instructions in `How-to add a shortcut <#how-to-add-a-shortcut>`__



If you only want to create a shortcut for a single app qube:

1. Open a terminal window to the template.

2. Create a custom ``.desktop`` file in either ``~/.local/share/applications`` or ``/usr/local/share/applications`` (you may need to first create the subdirectory). See the previous instructions about the desktop entry format.

3. Follow the instructions in `How-to add a shortcut <#how-to-add-a-shortcut>`__



To add a custom menu entry instead:

1. Open a terminal window to Dom0.

2. Create a custom ``.desktop`` file in ``~/.local/share/applications``. Look in the same directory for existing examples, or see the full `file specification <https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html>`__. You may use ``qvm-run`` inside the ``.desktop`` file; see :ref:`Behind the scenes <user/troubleshooting/app-menu-shortcut-troubleshooting:behind the scenes>` for more details.

3. Edit the ``~/.config/menus/applications-merged/<vmname>-vm.menu`` file for the app qube.

4. Add a custom menu entry referring to your newly created ``.desktop`` file.

   .. code:: xml

         <Menu>
              <Name>Webmail</Name>
              <Include>
                      <Filename>custom.desktop</Filename>
              </Include>
         </Menu>





Unavailable desktop entry
^^^^^^^^^^^^^^^^^^^^^^^^^


If you created a desktop entry but it doesn’t show up, there are some steps to run inside the qube, to identify the problem:

1. make sure the name is a valid name (only ASCII letters, numbers, hyphens and point)

2. if this program is available, run ``desktop-file-validate <DESKTOP_FILE_PATH>``

3. run it through ``gtk-launch``

4. run ``/etc/qubes-rpc/qubes.GetAppmenus`` and check that your desktop entry is listed in the output



What about applications in disposables?
---------------------------------------


See :ref:`Adding programs to the app menu in Disposable customization <user/advanced-topics/disposable-customization:adding programs to the app menu>`.

What if a removed application is still in the app menu?
-------------------------------------------------------


First, try this in dom0:

.. code:: console

      $ qvm-appmenus --update --force <QUBE_NAME>



You can also try:

.. code:: console

      $ qvm-appmenus --remove <QUBE_NAME>



If that doesn’t work, you can manually modify the files in ``~/.local/share/applications/`` or in ``~/.local/share/qubes-appmenus/<QUBE_NAME>``.

For example, suppose you’ve deleted ``my-old-vm``, but there is a leftover Application Menu shortcut, and you find a related file in ``~/.local/share/applications/``, try to delete it. The hyphens in the name of the qube are replaced by an underscore and the letter, so instead of looking for ``my-old-vm``, try ``my_dold_dvm``.

What if my application is shown in app menu, but doesn't run anything?
----------------------------------------------------------------------


First, check in the corresponding ``.desktop`` file in ``~/.local/share/qubes-appmenus/<QUBE_NAME>/``, inside dom0.

The line starting with ``Exec=`` points out the exact command run by dom0 to start the application. It should be something like:

.. code:: desktop

      Exec=qvm-run -q -a --service -- <QUBE_NAME> qubes.StartApp+<APPLICATION_NAME>



It’s possible to run the command to check the output, by copying this line without ``Exec=``, and remove ``-q`` (quiet option). But it could be more useful to run it in the qube, with the ``qubes.StartApp`` service:

.. code:: console

      $ /etc/qubes-rpc/qubes.StartApp <APPLICATION_NAME>



Behind the scenes
-----------------


``qvm-sync-appmenus`` works by invoking the *GetAppMenus* :doc:`Qubes service </developer/services/qrexec>` in the target domain. This service enumerates applications installed in that qube and sends formatted info back to dom0 which creates ``.desktop`` files in the app qube/template directory of dom0.

For Linux qubes the service script is in ``/etc/qubes-rpc/qubes.GetAppMenus``. In Windows it’s a PowerShell script located in ``c:\Program Files\Invisible Things Lab\Qubes OS Windows Tools\qubes-rpc-services\get-appmenus.ps1`` by default.

The list of installed applications for each app qube is stored in dom0’s ``~/.local/share/qubes-appmenus/<QUBE_NAME>/apps.templates``. Each menu entry is a file that follows the `.desktop file format <https://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html>`__ with some wildcards (*%VMNAME%*, *%VMDIR%*). Applications selected to appear in the menu are stored in ``~/.local/share/qubes-appmenus/<QUBE_NAME>/apps`` and in ``~/.local/share/applications/``.

The whitelist given to ``qvm-appmenu --set-whitelist`` is stored as a feature called ``menu-items``, where each desktop entry is separated by a space.

Actual command lines for the menu shortcuts involve the ``qvm-run`` command which starts a process in another domain. Examples:

.. code:: console

      qvm-run -q -a --service -- %VMNAME% qubes.StartApp+firefox
      qvm-run -q -a --service -- %VMNAME% qubes.StartApp+7-Zip-7-Zip_File_Manager



Note that you can create a shortcut that points to a ``.desktop`` file in your app qube with e.g.:

.. code:: console

      qvm-run -q -a --service -- personal qubes.StartApp+firefox



While this works well for standard applications, creating a menu entry for Windows applications running under *wine* may need an additional step in order to establish the necessary environment in *wine*. Installing software under *wine* will create the needed ``.desktop`` file in the target Linux qube in the directory ``~/.local/share/applications/wine/Programs/`` or a subdirectory thereof, depending on the Windows menu structure seen under *wine*. If the name of this file contains spaces, it will not be found, because the ``qvm-run`` command is falsely seen as terminating at this space. The solution is to remove these spaces by renaming the ``.desktop`` file accordingly, e.g. by renaming ``Microsoft Excel.desktop`` to ``Excel.desktop``. Refreshing the menu structure will then build working menu entries.

**Note:** Applications installed under *wine* are installed in AppVMs, not in the template on which these AppVMs are based, as the file structure used by *wine* is stored under ``~/.wine``, which is part of the persistent data of the AppVM and not inherited from its template.

.. |image1| image:: /attachment/doc/r4.0-dom0-menu.png


.. |image2| image:: /attachment/doc/r4.0-dom0-appmenu-select.png

