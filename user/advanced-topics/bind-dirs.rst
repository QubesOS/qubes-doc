===========================================
How to make any file persistent (bind-dirs)
===========================================

.. warning::

      This page is intended for advanced users.

What are bind-dirs?
-------------------


With `bind-dirs <https://github.com/QubesOS/qubes-core-agent-linux/blob/master/vm-systemd/bind-dirs.sh>`__ any arbitrary files or folders can be made persistent in app qubes.

What is it useful for?
----------------------


In an app qube all of the file system comes from the template except ``/home``, ``/usr/local``, and ``/rw``. This means that changes in the rest of the filesystem are lost when the app qube is shutdown. bind-dirs provides a mechanism whereby files usually taken from the template can be persisted across reboots.

For example, in Whonix, Tor’s data dir ``/var/lib/tor`` `has been made persistent in the TemplateBased ProxyVM sys-whonix <https://github.com/Whonix/qubes-whonix/blob/8438d13d75822e9ea800b9eb6024063f476636ff/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf#L5>`__. In this way sys-whonix can benefit from the Tor anonymity feature ‘persistent Tor entry guards’ but does not have to be a standalone.

How to use bind-dirs.sh?
------------------------


In this example, we want to make ``/var/lib/tor`` persistent. Enter all of the following commands in your app qube.

1. Make sure the directory ``/rw/config/qubes-bind-dirs.d`` exists.

   .. code:: console

         $ sudo mkdir -p /rw/config/qubes-bind-dirs.d



2. Create the file ``/rw/config/qubes-bind-dirs.d/50_user.conf`` with root permissions, if it doesn’t already exist.

   .. code:: console

         $ sudo touch /rw/config/qubes-bind-dirs.d/50_user.conf



3. Add a line to ``/rw/config/qubes-bind-dirs.d/50_user.conf`` that appends a folder or file to the ``binds`` variable.

   .. code:: bash

         binds+=( '/var/lib/tor' )



4. Save.

5. If the directory you wish to make persistent doesn’t exist in the template on which the app qube is based, you’ll need to create the directory (with its full path) under ``/rw/bind-dirs`` in the app qube. For example, if ``/var/lib/tor`` didn’t exist in the template, then you would execute the following command in your app qube:

   .. code:: console

         $ sudo mkdir -p /rw/bind-dirs/var/lib/tor



6. (optional) If the directory you want to persist across reboots (``/var/lib/tor`` in this case) needs special ownership and permissions, make sure the directory you created just under ``/rw/bind-dirs/`` has the same ones (using the commands ``chown`` and ``chmod``, respectively).

7. Reboot the app qube.

8. Done.



From now on, all files in the ``/var/lib/tor`` directory will persist across reboots.

You can make as many files or folders persist as you want simply by making multiple entries in the ``50_user.conf`` file, each on a separate line. For example, if you added the file ``/etc/tor/torrc`` to the ``binds`` variable, any modifications to *that* file would also persist across reboots.

.. code:: bash

      binds+=( '/var/lib/tor' )
      binds+=( '/etc/tor/torrc' )



Other Configuration Folders
---------------------------


- ``/usr/lib/qubes-bind-dirs.d`` (lowest priority, for packages)

- ``/etc/qubes-bind-dirs.d`` (intermediate priority, for template wide configuration)

- ``/rw/config/qubes-bind-dirs.d`` (highest priority, for per qube configuration)



How does it work?
-----------------


bind-dirs.sh is called at startup of an app qube, and configuration files in the above configuration folders are parsed to build a bash array. Files or folders identified in the array are copied to ``/rw/bind-dirs`` if they do not already exist there, and are then bind mounted over the original files/folders.

Creation of the files and folders in ``/rw/bind-dirs`` should be automatic the first time the app qube is restarted after configuration.

If you want to circumvent this process, you can create the relevant file structure under ``/rw/bind-dirs`` and make any changes at the same time that you perform the configuration, before reboot. Note that you must create the full folder structure under ``/rw/bind-dirs`` - e.g you would have to create ``/rw/bind-dirs/var/lib/tor``

Limitations
-----------


- Files that exist in the template root image cannot be deleted in the app qubes root image using bind-dirs.sh.

- Re-running ``sudo /usr/lib/qubes/init/bind-dirs.sh`` without a previous ``sudo /usr/lib/qubes/init/bind-dirs.sh umount`` does not work.

- Running ``sudo /usr/lib/qubes/init/bind-dirs.sh umount`` after boot (before shutdown) is probably not sane and nothing can be done about that.

- Many editors create a temporary file and copy it over the original file. If you have bind mounted an individual file this will break the mount. Any changes you make will not survive a reboot. If you think it likely you will want to edit a file, then either include the parent directory in bind-dirs rather than the file, or perform the file operation on the file in ``/rw/bind-dirs``.

- Some files are altered when a qube boots - e.g. ``/etc/hosts``. If you try to use bind-dirs on such files you may break your qube in unpredictable ways. You can add persistent rules to ``/etc/hosts`` using :doc:`/rw/config/rc.local </user/advanced-topics/config-files>`.



How to remove binds from bind-dirs.sh?
--------------------------------------


``binds`` is actually just a bash variable (an array) and the bind-dirs.sh configuration folders are sourced as bash snippets in lexical order. Therefore if you wanted to remove an existing entry from the ``binds`` array, you could do that by using a lexically higher configuration file. For example, if you wanted to make ``/var/lib/tor`` non-persistent in ``sys-whonix`` without manually editing ``/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf``, you could use the following in:

``/rw/config/qubes-bind-dirs.d/50_user.conf``

.. code:: bash

      binds=( "${binds[@]/'/var/lib/tor'}" )



(Editing ``/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf`` directly is strongly discouraged, since such changes get lost when that file is changed in the package on upgrades.)

.. _custom-persist:

Custom persist feature
----------------------


Custom persist is an optional advanced feature allowing the creation of minimal state qube. The purpose of such an qube is to avoid unwanted data to persist as much as possible by disabling the ability to configure persistence from the qube itself. When enabled, the following happens:

- ``/rw/config/rc.local`` is no longer executed

- ``/rw/config/qubes-firewall-user-script`` is ignored

- ``/rw/config/suspend-module-blacklist`` is ignored

- User bind dirs defined in ``/rw/config/qubes-bind-dirs.d`` are no longer read

- ``/home`` and ``/user/local`` are not persistent anymore unless explicitly configured.



Bind dirs are obviously still supported but this must be configured either in the template (``/usr/lib/qubes-bind-dirs.d`` and ``/etc/qubes-bind-dirs.d``) or from dom0 using :doc:`manpages/qvm-features`. The bind dirs declaration must be done with this kind of feature: :option:`qvm-features custom-persist.{FEATURE_NAME} <qvm-features custom-persist.*>` (where :samp:`FEATURE_NAME` is an arbitrary name). The value should be formatted like this: :samp:`[PRE-CREATION SETTINGS:]<PATH>` (where :samp:`[PRE-CREATION-SETTINGS:]` is optional and :samp:`<PATH>` is an absolute path.

To use this feature:

1. :doc:`enable the service </user/how-to-guides/how-to-enable-a-service>` called :option:`custom-persist <qvm-service custom-persist>`.

2. Then, configure a persistent directory with :doc:`qvm-features <manpages/qvm-features>` in the :term:`admin qube`:

   .. code:: console

         [user@dom0] $ qvm-features QUBE_NAME custom-persist.FEATURE_NAME PATH

   Where :samp:`FEATURE_NAME` is an arbitrary name and :samp:`PATH` is an absolute path.

Nothing will be persistent except :samp:`PATH`. To re-enable ``/home`` and ``/usr/local`` persistence, just add them to the list:

.. code:: console

      [user@dom0] $ qvm-features QUBE_NAME custom-persist.home /home
      [user@dom0] $ qvm-features QUBE_NAME custom-persist.usrlocal /usr/local

When starting the qube, declared custom-persist bind dirs are automatically added to the ``binds`` variable described above and are handled in the same way.

A user may want their bind-dirs to be automatically pre-created in ``/rw/bind-dirs``. Custom persist can do this for you by providing the type of the resource to create (file or dir), owner, group and mode. For example:

.. code:: console

      [user@dom0] $ qvm-features QUBE_NAME custom-persist.downloads dir:user:user:0755:/home/user/Downloads

Will automatically create a :file:`/home/user/Downloads` directory owned by `user` with the `0755` mode



Discussion
----------


`app qubes: make selected files and folders located in the root image persistent- review bind-dirs.sh <https://groups.google.com/forum/#!topic/qubes-devel/tcYQ4eV-XX4/discussion>`__
