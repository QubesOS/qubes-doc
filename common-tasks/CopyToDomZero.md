---
layout: doc
title: CopyToDomZero
permalink: /doc/CopyToDomZero/
redirect_from: /wiki/CopyToDomZero/
---

Copying files to between VMs and Dom0
-------------------------------------

First, there should normally be few reasons for the user to want to copy files from VMs to Dom0, as Dom0 only acts as a "thin trusted terminal", and no user applications run there. However, one exception to this is if we want to copy a desktop wallpaper, that we normally have in one of the AppVMs (e.g. in the 'personal' AppVM where we got it from our camera, or downloaded from the Internet). While it's a well justified reason, one should remember, however, that copying untrusted files to Dom0 might be a fatal security problem. Imagine what would happen if the wallpaper (e.g. a JPEG file) was somehow malformed and was in fact attempting to exploit a hypothetical JPEG parser bug in Dom0 code (e.g. in the Dom0's Xorg/KDE component that parses the wallpaper and displays it).

For this reason we intentionally do not provide a convenient tool for copying files between VMs and Dom0 (while we provide a tool for copying files between VMs). However, if you're determined to copy some files to Dom0 anyway, you can use the following method (run this command from Dom0's console):

```
qvm-run --pass-io <src_domain> 'cat /path/to/file_in_src_domain' > /path/to/file_name_in_dom0
```

BTW, you can use the same method to copy files from Dom0 to VMs:

```
cat /path/to/file_in_dom0 | qvm-run --pass-io <dst_domain> 'cat > /path/to/file_name_in_appvm'
```

### Copying logs from dom0

In order to easily copy/paste the contents of logs from dom0 to the inter-VM clipboard:

1.  Right-click on the desired VM in the Qubes VM Manager.
2.  Click "Logs."
3.  Click on the desired log.
4.  Click "Copy to Qubes clipboard."

You may now paste the log contents to any VM as you normally would (i.e., Ctrl-Shift-V, then Ctrl-V).
