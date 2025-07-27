=======================
How to install software
=======================


When you wish to install software in Qubes OS, you should generally install it in a :ref:`template <user/reference/glossary:template>`. For installing templates themselves, see :ref:`how to install a template <user/templates/templates:installing>`. Advanced users may also be interested in learning how to install software in :doc:`standalones </user/advanced-topics/standalones-and-hvms>` and :doc:`dom0 </user/advanced-topics/how-to-install-software-in-dom0>`.

Qubes OS is effectively a “meta” operating system (OS) that can run almost any arbitrary OS inside of itself. For example, the way software is normally installed in a Linux distribution (“distro”) is quite different from the way software is normally installed in Windows. This isn’t up to Qubes. Qubes is just the framework in which you’re running these other OSes. Therefore, if you want to install software in a Linux template, for example, you should do so in whatever way is normal for that Linux distro. Most Linux software is distributed via `packages <https://en.wikipedia.org/wiki/Package_format>`__, which are stored in `software repositories <https://en.wikipedia.org/wiki/Software_repository>`__ (“repos”). `Package managers <https://en.wikipedia.org/wiki/Package_manager>`__ handle downloading, installing, updating, and removing packages. (Again, none of this is Qubes-specific.) If you’re not familiar with how software is normally installed in Linux distros via package managers or the software you want doesn’t seem to be available in your distro’s repos (or you’re in another situation not covered on this page), please read this `community guide to installing software in Qubes <https://forum.qubes-os.org/t/9991/>`__.

The following instructions explain how to permanently install new software in a template. There are different instructions for software from the default repositories and all other software. (If you’re not sure, try the default repositories first.)

Installing software from default repositories
---------------------------------------------


1. Start the template.

2. Start either a terminal (e.g. ``gnome-terminal``) or a dedicated software management application, such as ``gpk-application``.

3. Install software as normally instructed inside that operating system, e.g.:

   - Fedora: ``sudo dnf install <PACKAGE_NAME>``

   - Debian: ``sudo apt install <PACKAGE_NAME>``



4. Shut down the template.

5. Restart all qubes based on the template.

6. (Recommended) In the relevant qubes’ **Settings > Applications** tab, select the new application(s) from the list, and press **OK**. These new shortcuts will appear in the Applications Menu. (If you encounter problems, see :doc:`here </user/troubleshooting/app-menu-shortcut-troubleshooting>` for troubleshooting.)



.. figure:: /attachment/doc/r4.1-dom0-appmenu-select.png
   :alt: The Applications tab in Qube Settings

 

Installing software from other sources
--------------------------------------


Some software is not available from the default repositories and must be downloaded and installed from another source. Depending on the installation method, you may either use the updates proxy or direct networking.

Using the updates proxy
^^^^^^^^^^^^^^^^^^^^^^^


If you are still using the distribution package manager, updates will likely still work over the updates proxy without needing to give the TemplateVM direct network access.

If you are using another installation method fetching remote resources, you might still be able to use the updates proxy by making the tools aware of the proxy. For many tools, it is enough to export the following environment variables in your shell session before proceeding:

.. code:: console

      $ export HTTP_PROXY=http://127.0.0.1:8082 http_proxy=$HTTP_PROXY \
               HTTPS_PROXY=$HTTP_PROXY https_proxy=$HTTPS_PROXY \
               ALL_PROXY=$HTTP_PROXY all_proxy=$ALL_PROXY \
               NO_PROXY=127.0.0.1 no_proxy=$NO_PROXY


Using direct networking
^^^^^^^^^^^^^^^^^^^^^^^


**Warning:** This method gives your template direct network access, which is `risky <#why-dont-templates-have-normal-network-access>`__. This method is **not** recommended for trusted templates. Moreover, depending on how you install this software, it may not get updated automatically when you :doc:`update Qubes normally </user/how-to-guides/how-to-update>`, which means you may have to update it manually yourself.

This method assumes that you are trying to follow instructions to install some piece of software in a normal operating system, except *that* operating system is running as a template in Qubes OS.

1. (Recommended) Clone the desired template (since this new template will probably be less trusted than the original).

2. (Recommended) In the new template’s **Settings > Basic** tab, change the color label from black to red (or another color that signifies to you that the template is less trusted).

3. In the new template’s **Settings > Basic** tab, change the **Networking** value from ``default (none) (current)`` to ``sys-firewall`` (or whichever network-providing qube you wish to use).

4. (Recommended) In the new template’s **Settings > Firewall rules** tab, select “Limit outgoing Internet connections to…” and tick “Allow full access for 5 min.” (This can help in case you forget to remove network access later.)

5. Follow the normal instructions for installing your software in the new template. For example, open a terminal and enter the commands as instructed. **Warning:** If you don’t fully understand the commands you’re entering, then this can be extremely risky, and the template should be regarded as *completely untrusted*.

6. (Recommended) In the new template’s **Settings > Basic** tab, change the **Networking** value from ``sys-firewall (current)`` (or whichever network-providing qube you chose) back to ``default (none)``.

7. Shut down the new template.

8. Create or assign your desired app qubes to use the new template. If any app qubes were already assigned to the new template, restart them.

9. (Recommended) In the relevant qubes’ **Settings > Applications** tab, select the new application(s) from the list, and press **OK**. These new shortcuts will appear in the Applications Menu. (If you encounter problems, see :doc:`here </user/troubleshooting/app-menu-shortcut-troubleshooting>` for troubleshooting.)



.. figure:: /attachment/doc/r4.1-dom0-appmenu-select.png
   :alt: The Applications tab in Qube Settings

 

Troubleshooting
---------------


If things are still not working as expected:

- Review the instructions very carefully, making sure you follow each step.

- Make sure you **shut down the template after installing your software**.

- Make sure you **restart your app qube after shutting down your template**.

- Make sure your app qube is assigned to the right template.

- If your software requires special files or directories to be persistent, and you’re an advanced user, see :doc:`standalones and HVMs </user/advanced-topics/standalones-and-hvms>` and :doc:`how to make any file persistent (bind-dirs) </user/advanced-topics/bind-dirs>`.

- :doc:`Ask for help. </introduction/support>`



How to update software
----------------------


Please see :doc:`How to Update </user/how-to-guides/how-to-update>`.

Why don't templates have normal network access?
-----------------------------------------------


In order to protect you from performing risky activities in templates, they do not have normal network access by default. Instead, templates use an `updates-proxy <#updates-proxy>`__ which allows you to install and update software using the distribution’s package manager over the proxy connection. **The updates proxy is already set up to work automatically out-of-the-box and requires no special action from you.** Most users should simply follow the normal instructions for `installing software from default repositories <#installing-software-from-default-repositories>`__ and :doc:`updating </user/how-to-guides/how-to-update>` software. If your software is not available in the default repositories, see `installing software from other sources <#installing-software-from-other-sources>`__.

Advanced
--------


The following sections cover advanced topics pertaining to installing and updating software in qubes.

Testing repositories
^^^^^^^^^^^^^^^^^^^^


If you wish to install updates that are still in :doc:`testing </user/downloading-installing-upgrading/testing>`, you must enable the appropriate testing repositories.

**Note:** The following repos are in templates and standalones. For dom0 testing repos, see :ref:`here <user/advanced-topics/how-to-install-software-in-dom0:testing repositories>`. For testing new templates, please see :ref:`here <user/downloading-installing-upgrading/testing:templates>`.

Fedora
^^^^^^


There are three Qubes VM testing repositories (where ``*`` denotes the Release):

- ``qubes-vm-*-current-testing`` – testing packages that will eventually land in the stable (``current``) repository

- ``qubes-vm-*-security-testing`` – a subset of ``qubes-vm-*-current-testing`` that contains packages that qualify as security fixes

- ``qubes-vm-*-unstable`` – packages that are not intended to land in the stable (``qubes-vm-*-current``) repository; mostly experimental debugging packages



To temporarily enable any of these repos, use the ``--enablerepo=<repo-name>`` option. Example commands:

.. code:: bash

      sudo dnf upgrade --enablerepo=qubes-vm-*-current-testing
      sudo dnf upgrade --enablerepo=qubes-vm-*-security-testing
      sudo dnf upgrade --enablerepo=qubes-vm-*-unstable



To enable or disable any of these repos permanently, change the corresponding ``enabled`` value to ``1`` in ``/etc/yum.repos.d/qubes-*.repo``.

Debian
^^^^^^


Debian also has three Qubes VM testing repositories (where ``*`` denotes the Release):

- ``*-testing`` – testing packages that will eventually land in the stable (``current``) repository

- ``*-securitytesting`` – a subset of ``*-testing`` that contains packages that qualify as security fixes

- ``*-unstable`` – packages that are not intended to land in the stable repository; mostly experimental debugging packages



To enable or disable any of these repos permanently, uncomment the corresponding ``deb`` line in ``/etc/apt/sources.list.d/qubes-r*.list``.

Standalones
^^^^^^^^^^^


The process for installing and updating software in :ref:`standalones <user/reference/glossary:standalone>` is the same as described above for templates, except no qubes are based on standalones, so there are no other qubes to restart.

RPMFusion for Fedora templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If you would like to enable the `RPM Fusion <https://rpmfusion.org/>`__ repositories, open a Terminal of the template and type the following commands, depending on which RPM Fusion repositories you wish to enable (see `RPM Fusion <https://rpmfusion.org/>`__ for details):

.. code:: bash

      sudo dnf config-manager setopt rpmfusion-free.enabled=1
      sudo dnf config-manager setopt rpmfusion-free-updates.enabled=1
      sudo dnf config-manager setopt rpmfusion-nonfree.enabled=1
      sudo dnf config-manager setopt rpmfusion-nonfree-updates.enabled=1
      sudo dnf upgrade --refresh



This will permanently enable the RPM Fusion repos. If you install software from here, it’s important to keep these repos enabled so that you can receiving future updates. If you only enable these repos temporarily to install a package the Qubes update mechanism may persistently notify you that updates are available, since it cannot download them.

Reverting changes to a template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Perhaps you’ve just updated your template, and the update broke your template. Or perhaps you’ve made a terrible mistake, like accidentally confirming the installation of an unsigned package that could be malicious. If you want to undo changes to a template, there are three basic methods:

1. **Root revert.** This is appropriate for misconfigurations, but not for security concerns. It will preserve your customizations.

2. **Reinstall the template.** This is appropriate for both misconfigurations and security concerns, but you will lose all customizations.

3. **Full revert.** This is appropriate for both misconfigurations and security concerns, and it can preserve your customizations. However, it is a bit more complex.



Root revert
^^^^^^^^^^^


**Important:** This command will roll back any changes made *during the last time the template was run, but* **not** *before.* This means that if you have already restarted the template, using this command is unlikely to help, and you’ll likely want to reinstall it from the repository instead. On the other hand, if the template is already broken or compromised, it won’t hurt to try reverting first. Just make sure to **back up** all of your data and changes first!

1. Shut down ``<template>``. If you’ve already just shut it down, do **not** start it again (see above).

2. In a dom0 terminal:

   .. code:: bash

         qvm-volume revert <template>:root





Reinstall the template
^^^^^^^^^^^^^^^^^^^^^^


Please see :doc:`How to Reinstall a template </user/how-to-guides/how-to-reinstall-a-template>`.

Full revert
^^^^^^^^^^^


This is like the simple revert, except:

- You must also revert the private volume with ``qvm-volume revert   <template>:private``. This requires you to have an old revision of the private volume, which does not exist with the current default config. However, if you don’t have anything important in the private volume (likely for a template), then you can work around this by just resetting the private volume with ``qvm-volume import --no-resize <template>:private /dev/null``.

- The saved revision of the volumes must be uncompromised. With the default ``revisions_to_keep=1`` for the root volume, you must **not** have started the template since the compromising action.



Updates proxy
^^^^^^^^^^^^^


Updates proxy is a service which allows access from package managers configured to use the proxy by default, but can be used by any other program that accepts proxy arguments. The purpose of the proxy, instead of direct network access, is meant to mitigate user errors of using applications such as the browser in the template. Not necessarily what part of the network they can access, but only to applications trusted by the user, configured to use the proxy. The http proxy (tinyproxy) does not filter traffic because it is hard to list all the repository mirrors and keep that list up to date). it also does not cache anything.

The proxy is running in selected VMs (by default all the NetVMs (1)) and intercepts traffic directed to 127.0.0.1:8082. Thanks to such configuration all the VMs can use the same proxy address. If the VM is configured to have access to the updates proxy (2), the startup scripts will automatically configure dnf/apt to really use the proxy (3). Also access to updates proxy is independent of any other firewall settings (VM will have access to updates proxy, even if policy is set to block all the traffic).

There are two services (``qvm-service``, :doc:`service framework </user/advanced-topics/qubes-service>`):

1. ``qubes-updates-proxy`` (and its deprecated name: ``qubes-yum-proxy``) - a service providing a proxy for templates - by default enabled in NetVMs (especially: sys-net)

2. ``updates-proxy-setup`` (and its deprecated name: ``yum-proxy-setup``) - use a proxy provided by another VM (instead of downloading updates directly), enabled by default in all templates



Both the old and new names work. The defaults listed above are applied if the service is not explicitly listed in the services tab.

Technical details
^^^^^^^^^^^^^^^^^


The updates proxy uses RPC/qrexec. The proxy is configured in qrexec policy in dom0: ``/etc/qubes-rpc/policy/qubes.UpdatesProxy``. By default this is set to sys-net and/or sys-whonix, depending on firstboot choices. This new design allows for templates to be updated even when they are not connected to any NetVM.

Example policy file in R4.1 (with Whonix installed, but not set as default UpdateVM for all templates):

.. code:: bash

      # any VM with tag `whonix-updatevm` should use `sys-whonix`; this tag is added to `whonix-gw` and `whonix-ws` during installation and is preserved during template clone
      @tag:whonix-updatevm @default allow,target=sys-whonix
      @tag:whonix-updatevm @anyvm deny
      
      # other templates use sys-net
      @type:TemplateVM @default allow,target=sys-net
      @anyvm @anyvm deny


Installing Snap Packages
^^^^^^^^^^^^^^^^^^^^^^^^


Snap packages do not use the normal update channels for Debian and Fedora (apt and dnf) and are often installed as the user rather than as root. To support these in an app qube you need to take the following steps:

1. In the **template** you must install ``snapd`` and ``qubes-snapd-helper``. Open a terminal in the template and run:

   .. code:: console

         [user@fedora-36-snap-demo ~]$ sudo dnf install snapd qubes-snapd-helper
         Last metadata expiration check: 0:33:05 ago on Thu 03 Nov 2022 04:34:06.
         Dependencies resolved.
         ========================================================================================================
          Package                       Arch    Version                             Repository              Size
         ========================================================================================================
         Installing:
          snapd                        x86_64   2.56.2-4.fc36                       updates                 14 M
          qubes-snapd-helper           noarch   1.0.4-1.fc36                        qubes-vm-r4.1-current   10 k
         Installing dependencies:
         [...]
         
         Transaction Summary
         ========================================================================================================
         Install  19 Packages
         
         Total download size: 27 M
         Installed size: 88 M
         Is this ok [y/N]: y
         
         Downloading Packages:
         [..]
         Failed to resolve booleanif statement at /var/lib/selinux/targeted/tmp/modules/200/snappy/cil:1174
         /usr/sbin/semodule:  Failed!
         [...]
         Last metadata expiration check: 0:33:05 ago on Thu 03 Nov 2022 04:34:06.
         Notifying dom0 about installed applications
         
         Installed:
           snapd-2.56.2-4.fc36.x86_64                                              qubes-snapd-helper-1.0.4-1.fc36.noarch
         [...]
         Complete!

   You may see the following message:

   .. code:: bash

         Failed to resolve booleanif statement at /var/lib/selinux/targeted/tmp/modules/200/snappy/cil:1174
         /usr/sbin/semodule:  Failed!


   This is expected and you can safely continue.
   Shutdown the template:

   .. code:: console

         [user@fedora-36-snap-demo ~]$ sudo shutdown -h now


2. Now open the **app qube** in which you would like to install the Snap application and run a terminal:

   .. code:: console

         [user@snap-demo-app qube ~]$ snap install <package>

   When the install is complete you can close the terminal window.

3. Refresh the Applications list for the app qube. In the Qubes Menu for the **app qube** launch the Qube Settings. Then go to the Applications tab and click “Refresh Applications”

   - The refresh will take a few minutes; after it’s complete the Snap app will appear in the app qube’s list of available applications. At this point the snap will be persistent within the app qube and will receive updates when the app qube is running.





Autostarting Installed Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If you want a desktop app to start automatically every time a qube starts you can create a link to it in the ``~/.config/autostart`` directory of the **app qube**. This might be useful for Qubes that you set to automatically start on boot or for Qubes that have a set of apps you typically use all day, such as a chat app.

1. Open a terminal in the **app qube** where you would like the app to launch.

2. List the names of the available desktop shortcuts by running the command ``ls /usr/share/applications`` and find the exact name of the shortcut to the app you want to autostart:

   .. code:: console

         [user@example-app qube ~]$ ls /usr/share/applications/
         bluetooth-sendto.desktop
         eog.desktop
         firefox.desktop
         ...
         xterm.desktop
         yelp.desktop


3. Create the autostart directory:

   .. code:: console

         [user@example-app qube ~]$ mkdir -p ~/.config/autostart



4. Make a link to the desktop app file you’d like to start in the autostart directory. For example, the command below will link the Thunderbird app into the autostart directory:

   .. code:: console

         [user@example-app qube ~]$ ln -s /usr/share/applications/mozilla-thunderbird.desktop ~/.config/autostart/mozilla-thunderbird.desktop





Note that the app will autostart only when the app qube starts. If you would like the app qube to autostart, select the “Start qube automatically on boot” checkbox in the app qube’s Qube Settings.
