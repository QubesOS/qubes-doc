=====================
How to copy from dom0
=====================


This page covers copying files and clipboard text between :ref:`dom0 <user/reference/glossary:dom0>` and :ref:`domUs <user/reference/glossary:domu>`. Since dom0 is special, the processes are different from :doc:`copying and pasting text between qubes </user/how-to-guides/how-to-copy-and-paste-text>` and :doc:`copying and moving files between qubes </user/how-to-guides/how-to-copy-and-move-files>`.

Copying *from* dom0
-------------------


Copying files from dom0
^^^^^^^^^^^^^^^^^^^^^^^


To copy a file from dom0 to a VM, simply use ``qvm-copy-to-vm``:

.. code:: bash

      qvm-copy-to-vm <target_vm> <file>



The file will arrive in the target VM in the ``/home/user/QubesIncoming/dom0/`` directory.

Copying and pasting clipboard text from dom0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Use the **Qubes Clipboard** widget:

1. Copy text to the clipboard normally in dom0 (e.g., by pressing Ctrl+C).

2. Click the **Qubes Clipboard** icon in the Notification Area.

3. Click “Copy dom0 clipboard”. This displays a notification that text has been copied to the inter-qube clipboard.

4. Press Ctrl+Shift+V in the target qube. This pastes the inter-qube clipboard contents into the target qube’s normal clipboard.

5. Paste normally within that qube (e.g., by pressing Shift+V).



Alternatively, you can put your text in a file, then `copy it as a file <#copying-files-from-dom0>`__. Or, you can write the data you wish to copy into ``/var/run/qubes/qubes-clipboard.bin``, then ``echo -n dom0 > /var/run/qubes/qubes-clipboard.bin.source``. Then use Ctrl+Shift+V to paste the data to the target qube.

Copying logs from dom0
^^^^^^^^^^^^^^^^^^^^^^


In order to easily copy/paste the contents of logs from dom0 to the inter-VM clipboard, you can simply:

1. Right-click on the desired qube in the Qube Manager.

2. Click “Logs.”

3. Click on the desired log.

4. Click “Copy to Qubes clipboard.”



You may now paste the log contents in qube as you normally would (e.g., Ctrl+Shift+V, then Ctrl+V).

Copying *to* dom0
-----------------


Copying anything into dom0 is not advised, since doing so can compromise the security of your Qubes system. For this reason, there is no simple means of copying anything into dom0, unlike `copying from dom0 <#copying-from-dom0>`__.

There should normally be few reasons for the user to want to copy anything from domUs to dom0, as dom0 only acts as a “thin trusted terminal”, and no user applications run there. Sometimes, new users feel the urge to copy a desktop wallpaper image into dom0, but that is not necessary. A safer approach is simply to display the image in :doc:`full-screen mode </user/how-to-guides/how-to-enter-fullscreen-mode>` in an app qube, then take a screenshot from dom0, which results in exactly the image needed for a wallpaper, created securely and natively in dom0.

If you are determined to copy some files to dom0 anyway, you can use the following method. (If you want to copy text, first save it into a text file.) Run this command in a dom0 terminal:

.. code:: bash

      qvm-run --pass-io <src-vm> 'cat /path/to/file_in_src_domain' > /path/to/file_name_in_dom0



Note that you can use the same method to copy files from dom0 to domUs (if, for some reason, you don’t want to use ``qvm-copy-to-vm``):

.. code:: bash

      cat /path/to/file_in_dom0 | qvm-run --pass-io <dest-vm> 'cat > /path/to/file_name_in_appvm'


