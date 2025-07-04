======================
How to use disposables
======================


A :ref:`disposable <user/reference/glossary:disposable>` is a lightweight :ref:`qube <user/reference/glossary:qube>` that can be created quickly and will self-destruct when closed. Disposables are usually created in order to host a single application, like a viewer, editor, or web browser.

From inside an app qube, choosing the ``Open in disposable`` option on a file will launch a disposable for just that file. Changes made to a file opened in a disposable are passed back to the originating qube. This means that you can safely work with untrusted files without risk of compromising your other qubes. Disposables can be launched either directly from dom0’s app menu or terminal window, or from within app qubes. Disposables are generated with names like ``disp####``, where ``####`` is random number.

|disposablevm-example.png|

This diagram provides a general example of how disposables can be used to safely open untrusted links and attachments in disposables. See `this article <https://blog.invisiblethings.org/2010/06/01/disposable-vms.html>`__ for more on why one would want to use a disposable.

Named disposables and disposable templates
------------------------------------------


There is a difference between :ref:`named disposable qubes <user/reference/glossary:named disposable>` and :ref:`disposable templates <user/reference/glossary:disposable template>`.

In a default QubesOS Installation, you would probably use the ‘whonix-ws-16-dvm’ disposable template to, for example, browse the Tor network with an disposable qube. Every time you start an application using this disposable template, a new disposable qube - named ``dispX`` (where X is a random number) starts. If you close the application window, the ``dispX`` qube shuts down and vanishes from your system. That is how disposable templates are used.

Named disposables are also built upon disposable templates, but they have a fixed name. The named disposable seems to behave like an ordinary app qube - every application you open will start in the same qube, and you need to manually shutdown the qube. But when you shutdown *any changes you made in the named disposable will be lost*. Except for this non-persistance, they feel like usual app qubes.

How to create disposable templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


First, you need to create an app qube. You can run it normally, set up any necessary settings (like browser settings) you wish to be applied to every disposable qube ran from this template. Next, go to ‘Qube Settings’ of the app qube, set it as a *Disposable template* in the *Advanced* section and apply the change.

In Qubes 4.1, the entry in the Application menu is split into ‘Disposable’ and ‘Template (disp)’. The settings for the disposable can be changed under **’Application Menu -> Template (disp) -> Template: Qubes Settings**

In Qubes 4.2, the qube will now appear in the menu as a disposable template (in the Apps section), from which you can launch new disposable qubes. To change the settings of the template itself or run programs in it, use the menu item for the disposable template located in the Templates section.

How to create named disposables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


In Qubes 4.1: named disposables can be created under **Application Menu -> Create Qubes VM**, set the qube type to be *DisposableVM*.

In Qubes 4.2: named disposables can be created by **Application Menu -> Settings -> Qubes Settings -> Create New Qube**. Set the qube type to **Named disposable**.

Security
--------


If a :ref:`disposable template <user/reference/glossary:disposable template>` becomes compromised, then any disposable based on that disposable template could be compromised. In particular, the *default* disposable template is important because it is used by the “Open in disposable” feature. This means that it will have access to everything that you open with this feature. For this reason, it is strongly recommended that you base the default disposable template on a trusted template.

Disposables and Local Forensics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


At this time, disposables should not be relied upon to circumvent local forensics, as they do not run entirely in RAM. For details, see `this thread <https://groups.google.com/d/topic/qubes-devel/QwL5PjqPs-4/discussion>`__.

When it is essential to avoid leaving any trace, consider using `Tails <https://tails.boum.org/>`__.

Disposables and Networking
--------------------------


Similarly to how app qubes are based on their underlying :ref:`template <user/reference/glossary:template>`, disposables are based on their underlying :ref:`disposable template <user/reference/glossary:disposable template>`. R4.0 introduces the concept of multiple disposable templates, whereas R3.2 was limited to only one.

On a fresh installation of Qubes, the default disposable template is called ``fedora-X-dvm`` or ``debian-X-dvm`` (where ``X`` is a release number). If you have included the Whonix option in your install, there will also be a ``whonix-ws-dvm`` disposable template available for your use.

You can set any app qube to have the ability to act as a disposable template with:

.. code:: bash

      qvm-prefs <APP_QUBE> template_for_dispvms True



The default system wide disposable template can be changed with ``qubes-prefs default_dispvm``. By combining the two, choosing ``Open in disposable`` from inside an app qube will open the document in a disposable based on the default disposable template you specified.

You can change this behavior for individual qubes: in the Application Menu, open Qube Settings for the qube in question and go to the “Advanced” tab. Here you can edit the “Default disposable” setting to specify which disposable template will be used to launch disposables from that qube. This can also be changed from the command line with:

.. code:: bash

      qvm-prefs <QUBE> default_dispvm <DISPOSABLE_TEMPLATE>



For example, ``anon-whonix`` has been set to use ``whonix-ws-dvm`` as its ``default_dispvm``, instead of the system default. You can even set an app qube that has also been configured as a disposable template to use itself, so disposables launched from within the app qube/disposable template would inherit the same settings.

Network and firewall settings for disposable templates can be set as they can for a normal qube. By default a disposable will inherit the network and firewall settings of the disposable template on which it is based. This is a change in behavior from R3.2, where disposables would inherit the settings of the app qube from which they were launched. Therefore, launching a disposable from an app qube will result in it using the network/firewall settings of the disposable template on which it is based. For example, if an app qube uses sys-net as its net qube, but the default system disposable uses sys-whonix, any disposable launched from this app qube will have sys-whonix as its net qube.

**Warning:** The opposite is also true. This means if you have changed ``anon-whonix``’s ``default_dispvm`` to use the system default, and the system default disposable uses sys-net, launching a disposable from inside ``anon-whonix`` will result in the disposable using ``sys-net``.

A disposable launched from the app menu inherits the net qube and firewall settings of the disposable template on which it is based. Note that changing the net qube setting for the system default disposable template *does* affect the net qube of disposables launched from the app menu. Different disposable templates with individual net qube settings can be added to the app menu.

**Important Notes:** Some disposable templates will automatically create a menu item to launch a disposable. If you do not see an entry and want to add one, please use the command:

.. code:: bash

      qvm-features <DISPOSABLE_TEMPLATE> appmenus-dispvm 1



To launch a disposable template from the command line, execute the following command in dom0:

.. code:: bash

      qvm-run --dispvm=<DISPOSABLE_TEMPLATE> --service qubes.StartApp+<APPLICATION>



Opening a file in a disposable via GUI
--------------------------------------


In an app qube’s file manager, right click on the file you wish to open in a disposable, then choose “View in disposable” or “Edit in disposable”. Wait a few seconds and the default application for this file type should appear displaying the file content. This app is running in its own dedicated qube – a disposable created for the purpose of viewing or editing this very file. Once you close the viewing application the whole disposable will be destroyed. If you have edited the file and saved the changes, the changed file will be saved back to the original app qube, overwriting the original.

.. figure:: /attachment/doc/r4.0-open-in-dispvm-1.png
   :alt: r4.0-open-in-dispvm-1.png



.. figure:: /attachment/doc/r4.0-open-in-dispvm-2.png
   :alt: r4.0-open-in-dispvm-2.png



Opening a fresh web browser instance in a new disposable
--------------------------------------------------------


Sometimes it is desirable to open an instance of Firefox within a new fresh disposable. This can be done easily using the app menu: just go to **Application Menu -> Disposable -> Disposable: Firefox web browser**. Wait a few seconds until a web browser starts. Once you close the viewing application the whole disposable will be destroyed.

.. figure:: /attachment/doc/r4.0-open-in-dispvm-3.png
   :alt: r4.0-open-in-dispvm-3.png



Opening a file in a disposable via command line (from app qube)
---------------------------------------------------------------


Use the ``qvm-open-in-dvm`` command from a terminal in your app qube:

.. code:: bash

      [user@work-pub ~]$ qvm-open-in-dvm Downloads/apple-sandbox.pdf



Note that the ``qvm-open-in-dvm`` process will not exit until you close the application in the disposable.

Making a particular application open everything in a disposable
---------------------------------------------------------------


You can use the ``qvm-service`` command or the services GUI to cause an application in a qube to open files and URLs in a disposable. To do this, enable a service named ``app-dispvm.X`` in that qube, where ``X`` is the application ID. For instance, to have Thunderbird open all attachments in a disposable, enable the ``app-dispvm.thunderbird`` service.

This feature is currently somewhat experimental, and only works for Linux qubes. It is known to work with Thunderbird and Wire, but it may fail to work with some applications that do not honor all XDG environment variables. If the feature does not work for you, please file a bug report.

Opening particular types of files in a disposable
-------------------------------------------------


You can set ``qvm-open-in-dvm.desktop`` as the handler for a given MIME type. This will cause all files of that type to open in a disposable. This works in disposable templates too, but be careful: if your disposable template is set to use ``qvm-open-in-dvm.desktop`` to open a certain kind of file, every disposable based on it will be as well. If the disposable template is its own default disposable template (as is often the case), this will result in a loop: ``qvm-open-in-dvm`` will execute ``qubes.OpenURL`` in a new disposable, but that will in turn execute ``qvm-open-in-dvm``. The cycle will repeat until no new disposables can be created, most likely because your system has run out of memory.

This will *not* override the internal handling of PDF documents in Web browsers. This is typically okay, though: in-browser PDF viewers have a fairly good security record, especially when compared to non-browser PDF viewers. In particular, the attack surface of PDF viewing in Firefox is usually less than that of viewing an ordinary Web page.

Starting an arbitrary program in a disposable from an app qube
--------------------------------------------------------------


Sometimes it can be useful to start an arbitrary program in a disposable. The disposable will stay running so long as the process which started the disposable has not exited. Some applications, such as GNOME Terminal, do not wait for the application to close before the process exits (details `here <https://github.com/QubesOS/qubes-issues/issues/2581#issuecomment-272664009>`__). Starting an arbitrary program can be done from an app qube by running

.. code:: bash

      [user@vault ~]$ qvm-run '@dispvm' xterm



The created disposable can be accessed via other tools (such as ``qvm-copy-to-vm``) using its ``disp####`` name as shown in the Qubes Manager or ``qvm-ls``.

Starting an arbitrary application in a disposable via command line from dom0
----------------------------------------------------------------------------


The Application Launcher has shortcuts for opening a terminal and a web browser in dedicated disposables, since these are very common tasks. The disposable will stay running so long as the process which started the disposable has not exited. Some applications, such as GNOME Terminal, do not wait for the application to close before the process exits (details `here <https://github.com/QubesOS/qubes-issues/issues/2581#issuecomment-272664009>`__). It is possible to start an arbitrary application in a disposable directly from dom0 by running:

.. code:: bash

      $ qvm-run --dispvm=<DISPOSABLE_TEMPLATE> --service qubes.StartApp+xterm



The label color will be inherited from ``<DISPOSABLE_TEMPLATE>``. (The disposable Application Launcher shortcut used for starting programs runs a very similar command to the one above.)

Opening a link in a disposable based on a non-default disposable template from a qube
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Suppose that the default disposable template for your ``email`` qube has no networking (e.g., so that untrusted attachments can’t phone home). However, sometimes you want to open email links in disposables. Obviously, you can’t use the default disposable template, since it has no networking, so you need to be able to specify a different disposable template. You can do that with this command from the ``email`` qube (as long as your RPC policies allow it):

.. code:: bash

      $ qvm-open-in-vm @dispvm:<ONLINE_DISPOSABLE_TEMPLATE> https://www.qubes-os.org



This will create a new disposable based on ``<ONLINE_DISPOSABLE_TEMPLATE>``, open the default web browser in that disposable, and navigate to ``https://www.qubes-os.org``.

Example of RPC policies to allow this behavior
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


In dom0, add the following line at the beginning of the file ``/etc/qubes-rpc/policy/qubes.OpenURL``

.. code:: bash

      @anyvm @dispvm:<ONLINE_DISPOSABLE_TEMPLATE> allow



This line means:

- FROM: Any qube

- TO: A disposable based on ``<ONLINE_DISPOSABLE_TEMPLATE>``

- WHAT: Allow sending an “Open URL” request



In other words, any qube will be allowed to create a new disposable based on ``<ONLINE_DISPOSABLE_TEMPLATE>`` and open a URL inside of that disposable.

More information about RPC policies for disposables can be found :ref:`here <developer/services/qrexec:qubes rpc administration>`.

Customizing disposables
-----------------------


You can change the template used to generate the disposables, and change settings used in the disposable savefile. These changes will be reflected in every new disposable based on that template. Full instructions can be found :doc:`here </user/advanced-topics/disposable-customization>`.

.. |disposablevm-example.png| image:: /attachment/doc/disposablevm-example.png
   
