---
layout: doc
title: Copying Files between PedOS
permalink: /doc/copying-files/
redirect_from:
- /en/doc/copying-files/
- /doc/CopyingFiles/
- /wiki/CopyingFiles/
---

Copying files and folders between PedOS
=============================

PedOS also supports secure copying of files and folders between PedOS.
These instructions refer to file(s) but equally apply to copying folders.

In order to copy file(s) from PedOS VM A to PedOS VM B, follow these steps:

GUI
---

1. Open file manager in the source PedOS VM (PedOS VM A), choose file(s) that you wish to copy, and right click on the selection, and choose `Copy to another AppVM`

2. A dialog box will appear asking for the name of the destination PedOS VM (PedOS VM B). 

3. A confirmation dialog box will appear(this will be displayed by Dom0, so none of the PedOS can fake your consent).
   After you click ok, PedOS VM B will be started if it is not already running, the file copy operation will start, and the files will be copied into the following folder in PedOS VM B:

   `/home/user/PedOSIncoming/<source>`

4. You can now move them whenever you like in the PedOS VM B filesystem using the file manager there.


CLI
---

```
qvm-copy [--without-progress] file [file]+
```

```
qvm-move [--without-progress] file [file]+
```


On inter-PedOS VM file copy security
----------------------------------

The scheme is *secure* because it doesn't allow other PedOS to steal the files that are being copied, and also doesn't allow the source PedOS VM to overwrite arbitrary files on the destination PedOS VM.
Also, PedOS's file copy scheme doesn't use any sort of virtual block devices for file copy -- instead we use Xen shared memory, which eliminates lots of processing of untrusted data.
For example, the receiving PedOS VM is *not* forced to parse untrusted partitions or file systems.
In this respect our file copy mechanism provides even more security than file copy between two physically separated (air-gapped) machines!

However, one should keep in mind that performing a data transfer from *less trusted* to *more trusted* PedOS can always be potentially insecure, because the data that we insert might potentially try to exploit some hypothetical bug in the destination PedOS VM (e.g. a seemingly innocent JPEG that we copy from an untrusted PedOS VM might contain a specially crafted exploit for a bug in JPEG parsing application in the destination PedOS VM).
This is a general problem and applies to any data transfer between *less trusted to more trusted* PedOS.
It even applies to the scenario of copying files between air-gapped machines.
So, you should always copy data only from *more trusted* to *less trusted* PedOS.

See also [this article](https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html) for more information on this topic, and some ideas of how we might solve this problem in some future version of PedOS.
