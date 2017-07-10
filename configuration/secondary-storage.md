---
layout: doc
title: Secondary Storage
permalink: /doc/secondary-storage/
redirect_from:
- /en/doc/secondary-storage/
- /doc/SecondaryStorage/
- /wiki/SecondaryStorage/
---

Storing AppVMs on Secondary Drives
==================================

Suppose you have a fast but small primary SSD and a large but slow secondary
HDD.  You want to store a subset of your AppVMs on the HDD. In dom0:

1. `# mv /var/lib/qubes/appvms/my-new-appvm
/path/to/secondary/drive/my-new-appvm`

2. `# ln -s /path/to/secondary/drive/my-new-appvm /var/lib/qubes/appvms/`

Now, `my-new-appvm` will behave as if it were still stored on the primary SSD
(except that it will probably be slower, since it's actually stored on the
secondary HDD).

Known Issues
------------

 * The above procedure does **not** interfere with [Qubes Backup][]. However,
   attempting to symlink a `private.img` file (rather than the whole AppVM
   directory) is known to prevent the `private.img` file from being backed up.
   The same problem may occur if the above procedure is attempted on a
   [TemplateVM][]. [[1]]

 * This issue applies only to R3.1, not R3.2 or later:
   After implementing the above procedure, starting `my-new-appvm` will cause
   dom0 notifications to occur stating that loop devices have been attached to
   dom0. This is normal. (No untrusted devices are actually being mounted to
   dom0.) Do not attempt to detach these disks. (They will automatically be
   detached when you shut down the AppVM.) [[2]]

[Qubes Backup]: https://www.qubes-os.org/doc/BackupRestore/
[TemplateVM]: https://www.qubes-os.org/doc/Templates/
[1]: https://groups.google.com/d/topic/qubes-users/EITd1kBHD30/discussion
[2]: https://groups.google.com/d/topic/qubes-users/nDrOM7dzLNE/discussion
