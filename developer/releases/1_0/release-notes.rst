========================
Qubes R1.0 release notes
========================


Detailed release notes in `this blog post <https://blog.invisiblethings.org/2012/09/03/introducing-qubes-10.html>`__.

Known issues
------------


- Installer might not support some USB keyboards (#230). This seems to include all the Mac Book keyboards (most PC laptops have PS2 keyboards and are not affected).

- If you don’t enable Composition (System Setting -> Desktop -> Enable desktop effects), which you really should do, then the KDE task bar might get ugly (e.g. half of it might be black). This is some KDE bug that we don’t plan to fix.

- Some keyboard layout set by KDE System Settings can cause `keyboard not working at all <https://groups.google.com/group/qubes-devel/browse_thread/thread/77d076b65dda7226>`__. If you hit this issue, you can switch to console (by console login option) and manually edit ``/etc/X11/xorg.conf.d/00-system-setup-keyboard.conf`` (and ``/etc/sysconfig/keyboard``) and place correct keyboard layout settings (details in linked thread). You can check if specific keyboard layout settings are proper using ``setxkbmap`` tool.

- On systems with more than 8GB of RAM there is problem with DisposableVM. To fix it, limit maximum memory allocation for DispVM to 3GB

  .. code:: console

        $ qvm-prefs -s fedora-17-x64-dvm maxmem 3072
        $ qvm-create-default-dvm --default-template --default-script



- On some systems the KDE Window Manager might freeze upon resuming from S3 sleep when compositing is enabled (and the only method to log in to the system if this happens is to switch to a text console, enter your user’s password, kill the kwin process, go back to the Xorg console, log in, and start a new instance of kwin using Konsole application :) If you experience such problems, make sure to disable compositing before putting the system into sleep by pressing Alt-Ctrl-F12 (and then enabling it back once you log in after resume) – this way you should never see this problem again.



Downloads
---------


See :website:`Qubes Downloads <downloads/>`.

Installation instructions
-------------------------


See :doc:`Installation Guide </user/downloading-installing-upgrading/installation-guide>`.

Upgrading
---------


From Qubes 1.0-rc1
^^^^^^^^^^^^^^^^^^


If you’re already running Qubes 1.0-rc1, you don’t need to reinstall, it’s just enough to update the packages in your Dom0 and the template VM(s). The easiest way for doing this is to click on the Update Button in the Qubes Manger – one click when you selected Dom0, and one click for each of your template VM (by default there is just one template).

From Qubes 1.0 Beta 3
^^^^^^^^^^^^^^^^^^^^^


If you have Qubes Beta 3 currently installed on your system, you must reinstall from scratch, as we offer no direct upgrade option in the installer (sorry). However, we do offer tools for smooth migration of your AppVMs. In order to do that, please backup your AppVMs using the ``qvm-backup`` tool :doc:`as usual </user/how-to-guides/how-to-back-up-restore-and-migrate>`. Then, after you install Qubes 1.0 rc1, you can restore them using ``qvm-backup-restore`` tool. However, because we have changed the default template in RC1, you should tell qvm-back-restore about that by passing ``--replace-template`` option:

.. code:: console

      $ qvm-backup-restore <backup_dir> --replace-template=fedora-15-x64:fedora-17-x64


