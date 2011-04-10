---
layout: wiki
title: CopyingFiles
permalink: /wiki/CopyingFiles/
---

Copying files between domains
=============================

Qubes also supports secure file coping between domains. In order to copy file(s) from domain A to domain B, follow those steps:

1.  Open file manager in the source domain (domain A), choose file(s) that you wish to copy, and right click on the selection, and choose [Scripts/Copy?](/wiki/Scripts/Copy) to another AppVM...

1.  A dialog box will appear asking for the name of the destination domain (domain B). Ensure the domain B is running (start it by pressing the Play button in the manager if needed)

1.  You will get now a confirmation dialog box (this will be displayed by Dom0, so none of the domains can fake your consent). After you click ok, the file copy operation will start, and the files will be copied into the following folder in domain B:

-   ```/home/user/incoming/from-<srcdomain>```

1.  You can now move them whenever you like in the domain B filesystem using the file manager there.

On inter-domain file copy security
----------------------------------

-   Usual warning
-   How Qubes is better than air-gapped systems

