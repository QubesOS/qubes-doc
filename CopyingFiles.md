---
layout: doc
title: CopyingFiles
permalink: /doc/CopyingFiles/
redirect_from: /wiki/CopyingFiles/
---

Copying files between domains
=============================

Qubes also supports secure file coping between domains. In order to copy file(s) from domain A to domain B, follow those steps:

GUI
---

1.  Open file manager in the source domain (domain A), choose file(s) that you wish to copy, and right click on the selection, and choose `Copy to another AppVM`

1.  A dialog box will appear asking for the name of the destination domain (domain B). Ensure the domain B is running (start it by pressing the Play button in the manager if needed)

1.  You will get now a confirmation dialog box (this will be displayed by Dom0, so none of the domains can fake your consent). After you click ok, the file copy operation will start, and the files will be copied into the following folder in domain B:

-   `/home/user/QubesIncoming/<srcdomain>`

1.  You can now move them whenever you like in the domain B filesystem using the file manager there.

CLI
---

[qvm-copy-to-vm](/wiki/VmTools/QvmCopyToVm)

On inter-domain file copy security
----------------------------------

The scheme is *secure* because it doesn't allow other domains to steal the files that are being copying, and also doesn't allow the source domain to overwrite arbitrary file on the destination domain. Also, Qubes file copy scheme doesn't use any sort of virtual block devices for file copy -- instead we use Xen shared memory, which eliminates lots of processing of untrusted data. For example, the receiving domain is *not* forced to parse untrusted partitions or file systems. In this respect our files copy mechanism provides even more security than file copy between two physically separated (air-gapped) machines!

However, one should keep in mind that performing a data transfer from *less trusted* to *more trusted* domain can always be potentially insecure, because the data that we insert might potentially try to exploit some hypothetical bug in the destination VM (e.g. a seemingly innocent JPEG that we copy from untrusted domain, might turned out to be specially craft exploit for some hypothetical bug in JPEG parsing application in the destination domain). This is a general problem and applies to any data transfer between *less trusted to more trusted* domain. It even applies to the scenario of copying files between air-gapped machines. So, you should always copy data only from *more trusted* to *less trusted* domains.

See also [this article](http://theinvisiblethings.blogspot.com/2011/03/partitioning-my-digital-life-into.html) for more information on this topic, and some ideas of how we might solve this problem in some future version of Qubes.

You may also want to read how to [revoke "Yes to All" authorization](/wiki/Qrexec#RevokingYestoAllauthorization)
