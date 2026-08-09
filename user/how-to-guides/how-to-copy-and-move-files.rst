===================================
How to transfer files between qubes
===================================

Qubes OS supports various operations on files and directories (or "folders") between qubes:

* **copying or moving files and directories** from a qube to another
* **viewing or editing a file** from a qube in another, then potentially keeping the changes
* **convert untrusted files** into trusted files (i.e.: a PDF)

Some of those operations rely on :term:`disposables <disposable>`.

.. seealso::

   :doc:`/user/how-to-guides/how-to-copy-and-paste-text`
      If you wish to simply copy and paste text

   :doc:`/user/how-to-guides/how-to-copy-from-dom0`
      If you wish to copy from dom0

   :ref:`Open <open-file-in-disposable>` or :ref:`Sanitize a file in a disposable <sanitize-file-in-disposable>`
      To open or convert an untrusted file in a disposable

How to start a transfer to another qube with a file manager
-----------------------------------------------------------

1. **Open a file manager in the source qube** (i.e.: *work*): the qube containing the file you wish to use.

   .. hint:: In the following examples, the *work* qube will be our source qube and *personal* our target qube.

2. **Open the context menu** of the file you wish to use, using right-click, :kbd:`Menu` or :kbd:`Shift` + :kbd:`F10`.

3. Select one of:

   * :guilabel:`Copy to other qube` (possible with multiple files and folders, recursively)
   * :guilabel:`Move to other qube` (possible with multiple files and folders, recursively)
   * :guilabel:`Open in other qube`
   * :guilabel:`Convert in disposable qube` (only for pictures and PDF files)
   * :guilabel:`Edit in disposable qube`
   * :guilabel:`View in disposable qube`

   .. figure:: /attachment/doc/move-file-context-menu.svg

      In *work*, open the context menu of our :file:`test.txt` file

4. **(optional)** A dialog box will appear in dom0 asking for the name of the target qube (i.e.:*personal*). Enter or select the desired destination qube name and click on :guilabel:`Ok`.

   .. figure:: /attachment/doc/move-file-popup.svg

      The dialog of *dom0* waits for confirmation

      There is a reminder of the :guilabel:`Source` qube (here: *work*), the operation (here: :ref:`qubes.Filecopy <qubes.Filecopy>`, but it could be :ref:`qubes.OpenInVM <qubes.OpenInVM>`, :ref:`qubes.PdfConvert <qubes.PdfConvert>` or :ref:`qubes.GetImageRGBA <qubes.GetImageRGBA>`) and a dropdown selector to choose the :guilabel:`Target` qube (here: *personal*)

5. **(optional)** If the target qube is not already running, it will be started automatically

6. The operation on the file will be run on the target qube

.. danger::

   Keep in mind that performing a transfer from a *less trusted* qube to a *more trusted* qube is :ref:`always potentially insecure <qfilecopy-security>` if the data will be parsed in the target qube.

Result of the different operations
----------------------------------

Depending on the selected operation and qube, the result is different. For operations involving disposable qubes, see:

* :ref:`open-file-in-disposable`
* :ref:`sanitize-file-in-disposable`

After a copy
^^^^^^^^^^^^

After a **copy**: the file will be present in both qubes. It will show up in a defined directory: :file:`/home/user/QubesIncoming/{<SOURCE_QUBE>}/{<FILENAME>}`. This directory will automatically be created if it does not already exist.

.. figure:: /attachment/doc/moved-files-qubesincoming.svg

   The file is in :file:`/home/user/QubesIncoming/{work}/{test.txt}`

.. note::

   The operation will fail if you try to copy a file called :file:`text.txt` from a *work* qube and if the file (:file:`/home/user/QubesIncoming/{work}/{text.txt}`) already exists in the destination qube (i.e.: *personal*).

If you wish, you may now move the file in the target qube to a different directory. The directory :file:`/home/user/QubesIncoming/{work}` will be automatically deleted if empty. If you wish, you may now delete the :file:`QubesIncoming/` directory.

After a move
^^^^^^^^^^^^

A move operation is almost like a copy. Moving a file is equivalent to copying the file, then deleting the original. So, after moving the file successfully, it will be deleted from the source qube.

.. figure:: /attachment/doc/moved-file-check.svg

   After a move operation, :file:`test.txt` is deleted from *work*

After opening in other qube
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have opened the file in another qube, it will be copied in a temporary directory (:file:`/tmp/{<SOURCE_QUBE>}-{<RANDOM_SUFFIX>}/{<FILENAME>}`) on the target qube.

Once the file is closed, it will be removed from the target qube. If you have used :guilabel:`Open in other qube` or :guilabel:`Edit in disposable qube`, the file will be transferred back to the source qube once closed, keeping editions if you have saved the file.

If you have edited the file in the target qube, while using the :guilabel:`View in disposable qube` option, it will be lost because the disposable will be closed.

.. danger::

   Keep in mind that performing a transfer from a *less trusted* qube to a *more trusted* qube is :ref:`always potentially insecure <qfilecopy-security>` if the data will be parsed in the target qube.

How to copy or move a file in another qube in a terminal
--------------------------------------------------------

The same operations are also available via these command-line tools, replace :samp:`{<PATH_OF_THE_FILE>}` by something like :samp:`{test.txt}` and :samp:`{<TARGET_QUBE>}` by :samp:`{personal}` or the desired qube name.

To copy a file
   .. code:: console

         [user@SOURCE_QUBE] $ qvm-copy <PATH_OF_THE_FILE>
         Sent 1234/1234KB

To move two files
   .. code:: console

         [user@SOURCE_QUBE] $ qvm-move <PATH_OF_THE_FILE1> <PATH_OF_THE_FILE2>
         Sent 1234/1234KB

To open a file in a qube
   .. code:: console

         [user@SOURCE_QUBE] $ qvm-open-in-vm <TARGET_QUBE> <PATH_OF_THE_FILE>

   .. hint::

      Instead of :samp:`<PATH_OF_THE_FILE>` you can use a URL, like ``https://qubes-os.org``.

.. seealso::

   :ref:`open-file-in-disposable`
       Like `qvm-open-in-vm` with disposables

   :ref:`sanitize-file-in-disposable`
       Some files can be converted to trusted files, using disposables.

.. _automatically-open-file-type-in-other-qube:

How to open a file type automatically in another qube
-----------------------------------------------------

One of the main :ref:`feature <introduction/intro:Features>` of Qubes OS is the isolation of each software and qube. So, you might want to open some specific file types in another qube or a disposable. There are plenty of ways to achieve this, so we will just quickly treat how to do that in the default Xfce templates. For disposable qubes, refer to :ref:`open-file-type-in-disposable` and :ref:`make-application-open-everything-in-disposable`.

.. warning::

   The mechanisms described here and in the :doc:`/user/advanced-topics/disposable-customization` section might be ignored by some applications.

Set the default app for a file with a file manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Using the file manager, you can open the context menu of a file and select :menuselection:`Ope&n With --> Set Defa&ult Application`.
2. Then, in the :guilabel:`Set Default Application` window, choose :guilabel:`QubesOS Edit In DisposableVM`

Next time you try to open that file in that qube, it should be opened in a new disposable qube instead.

Set the default app(s) with Xfce4 Settings Manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open :program:`Settings Manager` (or :program:`xfce4-settings-manager`). You can add it to the app menu, using the settings of the qube, in the :guilabel:`Application` tab
2. Select :guilabel:`Default Applications`
3. You can change the default browser and mail reader in the very first tab, so that the links you click will open in another qube:

   1. click on the selection widget
   2. select :guilabel:`Other`
   3. click on the folder icon
   4. in the file selector, check that you are in :file:`/usr/bin`, select the file ``qvm-open-in-dvm`` and confirm

4. You can change any default application for all kinds of files in the :guilabel:`Others` tab:

   1. You have to know the "MIME Type", select it and click on :guilabel:`Open with`

      .. hint:: It is also possible to make all files open in a disposable.

   2. Select :guilabel:`QubesOS Edit In Disposable VM` and confirm

.. seealso::

   :ref:`manage-file-operations-policies`
      To restrict some operations between qubes

   :ref:`make-application-open-everything-in-disposable`
      Use of the :option:`!app.dispvm.*` service
