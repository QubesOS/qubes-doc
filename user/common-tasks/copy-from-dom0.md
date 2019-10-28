---
layout: doc
title: Copying from (and to) dom0
permalink: /doc/copy-from-dom0/
redirect_from:
- /doc/copy-to-dom0/
- /en/doc/copy-to-dom0/
- /doc/CopyToDomZero/
- /wiki/CopyToDomZero/
---

Copying from (and to) dom0
==========================

Copying **from** dom0
---------------------

To copy a file from dom0 to a VM (domU), simply use `qvm-copy-to-vm`:

~~~
qvm-copy-to-vm <dest-vm> <file>
~~~

The file will arrive in your destination VM in the `~/QubesIncoming/dom0/` directory.

### Copying logs from dom0 ###

In order to easily copy/paste the contents of logs from dom0 to the inter-VM clipboard, you can simply:

1.  Right-click on the desired VM in the Qubes VM Manager.
2.  Click "Logs."
3.  Click on the desired log.
4.  Click "Copy to Qubes clipboard."

You may now paste the log contents to any VM as you normally would (i.e., Ctrl-Shift-V, then Ctrl-V).

### Copy/paste from dom0 ###

For data other than logs, there are several options:

1.  Use the **Qubes Clipboard** widget:
    - Copy text to the clipboard normally in dom0.
    - Click the **Qubes Clipboard** icon in the Notification Area.
    - Click "Copy dom0 clipboard".
    - Receive a notification that text has been copied to the inter-qube clipboard.
    - Press Ctrl + Shift + V in a qube to paste into the desired qube's clipboard.
    - Paste normally within that qube.
2.  Copy it as a file (see above)
3.  Write the data you wish to copy into `/var/run/qubes/qubes-clipboard.bin`, then `echo -n dom0 > /var/run/qubes/qubes-clipboard.bin.source`.
    Then use Ctrl-Shift-V to paste the data to the desired VM.

Copying **to** dom0
-------------------

Copying anything into dom0 is not advised, since doing so can compromise the security of your Qubes system.
For this reason, there is no simple means of copying anything into dom0, unlike [copying from dom0](#copying-from-dom0) and [copying files between VMs](/doc/copying-files/).

There should normally be few reasons for the user to want to copy anything from VMs to dom0, as dom0 only acts as a "thin trusted terminal", and no user applications run there.
One possible use-case for this is if we want to use a desktop wallpaper in dom0 we have located in one of our AppVMs (e.g. in the 'personal' AppVM where we got the wallpaper from our camera or downloaded it from the Internet).
While this use-case is understandable, imagine what would happen if the wallpaper (e.g. a JPEG file) was somehow malformed or malicious and attempted to exploit a hypothetical JPEG parser bug in dom0 code (e.g. in the dom0's Xorg/KDE code that parses the wallpaper and displays it).

If you are determined to copy some files to dom0 anyway, you can use the following method.
(If you want to copy text, first save it into a text file.)
Run this command in a dom0 terminal:

~~~
qvm-run --pass-io <src-vm> 'cat /path/to/file_in_src_domain' > /path/to/file_name_in_dom0
~~~

Note that you can use the same method to copy files from dom0 to VMs (if, for some reason, you don't want to use `qvm-copy-to-vm`):

~~~
cat /path/to/file_in_dom0 | qvm-run --pass-io <dest-vm> 'cat > /path/to/file_name_in_appvm'
~~~

