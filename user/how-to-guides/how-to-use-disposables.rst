======================
How to use disposables
======================

A :term:`disposable` is a stateless :term:`qube`, it does not save data for the next boot. These qubes can serve various uses cases that require a pristine environment:

- View untrusted files without other trusted files on the same system;
- Visit untrusted websites in a web browser without authentication cookies from previous session;
- Sanitize untrusted PDFs or images and retrieve a safe-to-view image;
- Connect untrusted devices without other trusted devices or files on the same system;
- Fresh environment for build systems (for technical users).

Disposables can be launched either directly from :term:`GUI domain`'s app menu or terminal window, or from within app qubes. Disposables are generated with names like :samp:`disp{1234}`, where :samp:`{1234}` is a random number. Below is an example of disposable workflow benefits:

.. figure:: /attachment/doc/disposablevm-example.png
   :alt:

   Example of how disposables can be used to safely open untrusted links and attachments in disposables

   In the ``work-email`` qube, the user clicks on a link. This link is opened in a new disposable through the qrexec protocol (:program:`qubes.OpenURL`). The link contains some kind of malware that infects the disposable qube, but it is harmless for the ``work-email`` qube, as the links was opened in a separate environment from the mail client, the mail box is safe. The disposable is later destroyed.

   In that same *work-email* qube, the user now opens a PDF attachment. Using the qrexec protocol (:program:`qubes.OpenInVM`), the PDF is opened as in a new disposable qube, this time, the file looks clean, but as we can never be sure, the user prefers to default to open files in disposables. The disposable is later destroyed.

This diagram provides a general example of how disposables can be used to safely open untrusted links and attachments in disposables. You may find more on why one would want to use a disposable on the `first disposable qube article <https://blog.invisiblethings.org/2010/06/01/disposable-vms.html>`__. Please note that the blog post is dated and some of the information it presents are not accurate anymore.

Disposable types
----------------


Disposable template
^^^^^^^^^^^^^^^^^^^


:term:`Disposable template <disposable template>` is not a disposable in itself, but a special template that can create different disposable types: normal :term:`disposables <disposable>` and :term:`named disposables <named disposable>`. If you need to have a persistent changes in disposable files (e.g. configuration files), do them in the disposable template. If you need certain programs to be available in the disposable, you can install them in the disposable template's own template. By default, Qubes OS creates the ``default-dvm`` disposable template. It will be used it as an example on this page. You can create as many disposable templates as you'd prefer. :doc:`Disposable customization </user/advanced-topics/disposable-customization>` is outside of the scope of this page.


Named disposable
^^^^^^^^^^^^^^^^


:term:`Named disposables<named disposable>` are built upon disposable templates, but they have a fixed name. The named disposable seems to behave like an ordinary app qube, it doesn't shutdown when you close the initial application, every application you open will start in the same qube, and you need to manually shut it down. However, when it is shutdown, *any changes you made in the named disposable will be lost*.

If you have selected during installation to use disposable :term:`service qubes<service qube>`, your ``sys-net``, ``sys-usb`` and ``sys-firewall`` are examples of named disposables based on the ``default-dvm`` disposable template.


How to create disposables
-------------------------

How to launch new disposables based on existing template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Disposables can be started with |qubes-logo-icon|:menuselection:`Qubes App Menu (Q icon) --> APPS --> default-dvm`. Select the application you wish to launch in a new disposable, and one will be created for you. Notice that the application was not opened in the disposable template ``default-dvm``: instead, it opens in a :samp:`disp{1234}` qube. This is because applications from a disposable template listed in the :guilabel:`APPS` tab will open in a new disposable.

After the qube is created, you can access it via other tools using its :samp:`disp{1234}` name, for example in :ref:`Qubes Domains widget <introduction/getting-started:user interface>`, :ref:`Qubes Manager <introduction/getting-started:qube manager>`, |qubes-logo-icon|:menuselection:`Qubes App Menu (Q icon) --> APPS --> disp1234`, :guilabel:`qvm-copy`, :program:`qvm-ls` etc.


How to create named disposables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Named disposables can be created with |qubes-logo-icon|:menuselection:`Qubes App Menu (Q icon) --> Settings (icon) --> Qubes Tools --> Create New Qube --> Named disposable`, choose a name, configure according to your needs and click on :guilabel:`Create`.

If you create the qube with the name ``test-disp``, you can open applications on it using |qubes-logo-icon|:menuselection:`Qubes App Menu (Q icon) --> APPS --> test-disp` and selecting the application you wish to open in the named disposable.


In action
---------


Open an application in a disposable (from GUI domain)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Sometimes it is desirable to open an instance of Firefox in a new fresh disposable. This can be done easily using the app menu: just go to |qubes-logo-icon|:menuselection:`Qubes App Menu (Q icon) --> APPS --> default-dvm --> Firefox`. Wait a few seconds until the web browser starts.

.. image:: /attachment/doc/r4.3-dom0-menu-disp-firefox.png
   :alt: Application menu being used to open an Firefox from the ``default-dvm`` in a disposable qube.

.. image:: /attachment/doc/r4.3-dom0-menu-disp-firefox-open.png
   :alt: Firefox opened in a disposable qube in the default page.

It is possible to do the same as above using the command line:

.. code:: console

      user@dom0:~$ qvm-run --dispvm=default-dvm --service -- qubes.StartApp+firefox

The browser is opened from a disposable based on the ``default-dvm`` qube.

Open a file in a disposable (from app qube)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


In an app qube's file manager, right click on the file you wish to open in a disposable, then choose :guilabel:`Edit/View in disposable qube`. Wait a few seconds and the default application for this file type should appear displaying the file content. This app is running in its own dedicated qube, a disposable created for the purpose of viewing or editing this very file. If you have edited the file and saved the changes, the changed file will be saved back to the original app qube, overwriting the original.

.. image:: /attachment/doc/r4.3-domU-filemanager-disp-pdfviewer.png
   :alt: App qube file manager context menu being used to edit a PDF in a disposable qube.

.. image:: /attachment/doc/r4.3-domU-filemanager-disp-pdfviewer-open.png
   :alt: PDF viewer opened in a disposable qube with the PDF the user selected to edit.


It is also possible to do the same from the command line using :program:`qvm-open-in-dvm`:

.. code:: console

      [user@work ~]$ qvm-open-in-dvm -- 'apple-sandbox.pdf'
      [user@work ~]$ qvm-open-in-dvm --view-only -- 'apple-sandbox.pdf'

The PDF viewer is opened in a disposable based on the ``work`` qube default disposable template.

Sanitize a file in a disposable (from app qube)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


There is a nice security property in the system that allows transforming untrusted files into trusted files, this process is called sanitization. A sanitized file, presumably, leaves no room to malicious code, therefore, you can safely open the sanitized file in the qube itself (doesn't need to view in disposable anymore), in a viewer outside of :term:`Qubes OS`, or send the sanitized file to someone that doesn't use :term:`Qubes OS` and can't make the conversion themselves without compromising them..

Only supported file types for conversions are images and PDFs. The untrusted files will be converted to :abbr:`RGBA bitmap (A raster image where pixels are stored in Red, Green, Blue and Alpha)`. On conversion, the original untrusted files will be moved to :file:`~/QubesUntrustedPDFs` or :file:`image.png-untrusted` (location depends on the file type) while the sanitized file will be created with the same location and name by reconstructing the received data. As the output is an image, the sanitized files are a bit bigger, searching strings without :abbr:`OCR (Optical Character Recognition)` will not be possible anymore.

If you'd like to sanitize a file, in an app qube's file manager, right click on the file (image or PDF) you wish to sanitize in a disposable, then choose :guilabel:`Convert in disposable qube`. Wait a few seconds for the conversion. This conversion runs on its own dedicated qube, a disposable created for the sole purpose of sanitizing this very file.

It is also possible to do the same on the command line using :program:`qvm-convert-img` and :program:`qvm-convert-pdf`.

Connect a device to an disposable (from GUI domain)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Sometimes you have a device which you don't trust, therefore you decide to leverage disposables for the task. To attach a device to a disposable, go to :menuselection:`Qubes Devices widget --> <DEVICE> --> Attach to new disposable qube --> default-dvm`.

.. note:: No application will launch by default and the disposable will continue running, that is expected, no application request was made. Also notice that opening and closing the first (or any other) application opened in the disposable will not turn it off, this is also expected, you must shutdown disposables created by the Qubes Devices widget manually.


The same can be done from the command line, although more difficult:

..
   Python Admin API was preferred because each shell has a different way to read null bytes (qubesd-query).
   The escaped backslash is used to have indented blocks for readability.

.. code:: console

      user@dom0:~$ disp_template="default-dvm"
      user@dom0:~$ disp="$(python3 -c "import qubesadmin; \
          app = qubesadmin.Qubes(); \
          appvm = app.domains['$disp_template']; \
          disp = qubesadmin.vm.DispVM.from_appvm(qubesadmin.Qubes(), appvm); \
          disp.start(); \
          print(disp.name)
      ")"
      user@dom0:~$ qvm-device <DEVICE_CLASS> attach <ATTACH_OPTIONS> -- "$disp" <BACKEND:DEVICE_ID>
      user@dom0:~$ # Do your tasks.
      user@dom0:~$ qvm-device <DEVICE_CLASS> detach <ATTACH_OPTIONS> -- "$disp"
      user@dom0:~$ qvm-kill -- "$disp"

Call to the application succeeds but disposable exits too soon
--------------------------------------------------------------


When the main process of the initial application used to start the disposable exits, the disposable is removed. Some applications, such as GNOME Terminal (show on the app menu as :guilabel:`Terminal`, `do not wait for the application to close before the main process exits <https://github.com/QubesOS/qubes-issues/issues/2581#issuecomment-272664009>`__.

These cases requires wrappers to keep the application running. Qubes provides a wrapper for this particular case, :program:`qubes-run-gnome-terminal`, which will be used automatically by :program:`qubes-run-terminal` or application :guilabel:`Run Terminal` if GNOME Terminal happens to be the preferred terminal for the disposable template
