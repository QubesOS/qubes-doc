---
lang: en
release: 4.0
reviewed: yes
layout: doc
permalink: /doc/qfileexchgd/
redirect_from:
- /en/doc/qfileexchgd/
- /doc/Qfileexchgd/
- /wiki/Qfileexchgd/
ref: 40
title: Qfileexchgd (deprecated)
---

**This mechanism is obsolete as of Qubes Beta 1!**

Please see this [page](/doc/qfilecopy/) instead.


Overview
--------

*qfilexchgd* is a dom0 daemon responsible for managing exchange of block devices ("virtual pendrives") between VMs. It is used for

- copying files between AppVMs
- copying a single file between an AppVM and a DisposableVM

*qfilexchgd* is started after first *qubes\_guid* has been started, so that it has access to X display in dom0 to present dialog messages.

*qfilexchgd* is event driven. The sources of events are:

- trigger of xenstore watch for the changes in `/local/domain` xenstore hierarchy - to detect start/stop of VMs, and maintain vmname-\>vm\_xid dictionary
- trigger of xenstore watch for a change in `/local/domain/domid/device/qpen` key - VMs write to this key to request service from *qfilexchgd*

Copying files between AppVMs
----------------------------

1. AppVM1 user runs *qvm-copy-to-vm* script (accessible from Dolphin file manager by right click on a "file(s)-\>Actions-\>Send to VM" menu). It calls */usr/lib/qubes/qubes\_penctl new*, and it writes "new" request to its `device/qpen` xenstore key. *qfilexchgd* creates a new 1G file, makes vfat fs on it, and does block-attach so that this file is attached as `/dev/xvdg` in AppVM1.
2. AppVM1 mounts `/dev/xvdg` on `/mnt/outgoing` and copies requested files there, then unmounts it.
3. AppVM1 writes "send DestVM" request to its `device/qpen` xenstore key (calling */usr/lib/qubes/qubes\_penctl send DestVM*). After getting confirmation by displaying a dialog box in dom0 display, *qfilexchgd* detaches `/dev/xvdg` from AppVM1, attaches it as `/dev/xvdh` to DestVM.
4. In DestVM, udev script for `/dev/xvdh` named *qubes\_add\_pendrive\_script* (see `/etc/udev/rules.d/qubes.rules`) mounts `/dev/xvdh` on `/mnt/incoming`, and then waits for `/mnt/incoming` to become unmounted. A file manager running in DestVM shows a new volume, and user in DestVM may copy files from it. When user in DestVM is done, then user unmounts `/mnt/incoming`. *qubes\_add\_pendrive*\_script then tells *qfilexchgd* to detach `/dev/xvdh` and terminates.

Copying a single file between AppVM and a DisposableVM
------------------------------------------------------

In order to minimize attack surface presented by necessity to process virtual pendrive metadata sent by (potentially compromised and malicious) DisposableVM, AppVM\<-\>DisposableVM file exchange protocol does not use any filesystem.

1. User in AppVM1 runs *qvm-open-in-dvm* (accessible from Dolphin file manager by right click on a "file-\>Actions-\>Open in DisposableVM" menu). *qvm-open-in-dvm*
    1. gets a new `/dev/xvdg` (just as described in previous paragraph)
    2. computes a new unique transaction seq SEQ by incrementing `/home/user/.dvm/seq` contents,
    3. writes the requested file name (say, /home/user/document.txt) to `/home/user/.dvm/SEQ`
    4. creates a dvm\_header (see core.git/appvm/dvm.h) on `/dev/xvdg`, followed by file contents
    5. writes the "send disposable SEQ" command to its `device/qpen` xenstore key.

2. *qfilexchgd* sees that "send" argument=="disposable", and creates a new DisposableVM by calling */usr/lib/qubes/qubes\_restore*. It adds the new DisposableVM to qubesDB via qvm\_collection.add\_new\_disposablevm. Then it attaches the virtual pendrive (previously attached as `/dev/xvdg` at AppVM1) as `/dev/xvdh` in DisposableVM.
3. In DisposableVM, *qubes\_add\_pendrive\_script* sees non-zero `qubes_transaction_seq` key in xenstore, and instead processing the virtual pendrive as in the case of normal copy, treats it as DVM transaction (a request, because we run in DisposableVM). It retrieves the body of the file passed in `/dev/xvdh`, copies to /tmp, and runs *mime-open* utility to open appropriate executable to edit it. When *mime-open* returns, if the file was modified, it is sent back to AppVM1 (by writing "send AppVM1 SEQ" to `device/qpen` xenstore key). Then DisposableVM destroys itself.
4. In AppVM1, a new `/dev/xvdh` appears (because DisposableVM has sent it). *qubes\_add\_pendrive\_script* sees non-zero `qubes_transaction_seq` key, and treats it as DVM transaction (a response, because we run in AppVM, not DisposableVM). It retrieves the filename from `/home/user/.dvm/SEQ`, and copies data from `/dev/xvdh` to it.
