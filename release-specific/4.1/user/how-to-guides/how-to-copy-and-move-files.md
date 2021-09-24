---
lang: en
layout: doc
permalink: /doc/4.1/how-to-copy-and-move-files/
redirect_from:
- /doc/copying-files/
- /en/doc/copying-files/
- /doc/CopyingFiles/
- /wiki/CopyingFiles/
ref: 191
title: How to copy and move files
---

*This page is about copying and moving files.
If you wish to simply copy and paste text, that can be done more easily using the inter-qube clipboard.
See [copying and pasting text between qubes](/doc/how-to-copy-and-paste-text/).
For dom0, see [copying from (and to) dom0](/doc/how-to-copy-from-dom0/).*

Qubes OS supports the secure copying and moving of files and directories (folders) between qubes.

For simplicity, these instructions will refer to copying/moving a single file, but they apply equally well to groups of files and directories, which are copied recursively.

 1. Open a file manager in the qube containing the file you wish to copy (the source qube), right-click on the file you wish to copy or move, and select `Copy to Other app qube...` or `Move to Other app qube...`.

 2. A dialog box will appear in dom0 asking for the name of the target qube (qube B). 
    Enter or select the desired destination qube name.

 3. If the target qube is not already running, it will be started automatically, and the file will be copied there.
    It will show up in this directory (which will automatically be created if it does not already exist):

        /home/user/QubesIncoming/<source_qube>/<filename>

    If you selected **Move** rather than **Copy**, the original file in the source qube will be deleted.
    (Moving a file is equivalent to copying the file, then deleting the original.)

 4. If you wish, you may now move the file in the target qube to a different directory and delete the `/home/user/QubesIncoming/` directory when no longer needed.

The same operations are also available via these command-line tools:

```
qvm-copy [--without-progress] file [file]+
```

```
qvm-move [--without-progress] file [file]+
```

Security
--------

The inter-qube file copy system is secure because it doesn't allow other qubes to steal the files that are being copied, and it doesn't allow the source qube to overwrite arbitrary files on the destination qube.
Moreover, this system doesn't use any sort of virtual block device for file copy.
Instead, we use Xen shared memory, which eliminates a lot of processing of untrusted data.
For example, the receiving qube is *not* forced to parse untrusted partitions or file systems.
In this respect, the inter-qube file copy system provides even more security than file copy between two physically separated (air-gapped) machines!
(See [Software compartmentalization vs. physical separation](https://invisiblethingslab.com/resources/2014/Software_compartmentalization_vs_physical_separation.pdf) for more on this.)

However, one should keep in mind that performing a data transfer from *less trusted* to *more trusted* qubes is always potentially insecure if the data will be parsed in the target qube.
This is because the data that we copy could try to exploit some hypothetical bug in software running in the target qube.
For example, a seemingly-innocent JPEG that we copy from an untrusted qube might contain a specially-crafted exploit for a bug in a JPEG-parsing application in the target qube.
This is a general problem and applies to any data transfer from *less trusted* to *more trusted* qubes.
It even applies to the scenario of copying files between air-gapped machines.
Therefore, you should always copy data only from *more trusted* to *less trusted* qubes.

See also [this article](https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html) for more information on this topic, and some ideas of how we might solve this problem in some future version of Qubes.
