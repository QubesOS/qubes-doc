---
lang: en
layout: doc
permalink: /doc/volume-backup-revert/
redirect_from:
- /en/doc/volume-backup-revert/
- /doc/VolumeBackupRevert/
- /wiki/VolumeBackupRevert/
ref: 206
title: Volume backup and revert
---

With Qubes, it is possible to revert one of a VM's storage volumes to a previous
state using the automatic snapshot that is normally saved every time a VM is
shutdown. (Note that this is a different, lower level activity than the
[Backup, Restoration, and Migration](/doc/backup-restore/) process.)

In Qubes, when you create a new VM, it's volumes are stored in one of the
system's [Storage Pools](/doc/storage-pools/). On pool creation, a
`revisions_to_keep` default value is set for the entire pool. (For a pool creation
example, see [Storing app qubes on Secondary Drives](/doc/secondary-storage/).)
Thereafter, each volume associated with a VM that is stored in this pool
inherits the pool default `revisions_to_keep`.

For the private volume associated with a VM named *vmname*, you may inspect the
value of `revisions_to_keep` from the dom0 CLI as follows:

```
qvm-volume info vmname:private
```

The output of the above command will also display the "Available revisions
(for revert)" at the bottom. For a very large volume in a small pool,
`revisions_to_keep` should probably be set to the maximum value of 1 to minimize
the possibility of the pool being accidentally filled up by snapshots. For a
smaller volume for which you would like to have the future option of reverting,
`revisions_to_keep` should probably be set to at least 2. To set
`revisions_to_keep` for this same VM / volume example:

```
qvm-volume config vmname:private revisions_to_keep 2
```

With the VM stopped, you may revert to an older snapshot of the private volume
from the above list of "Available revisions (for revert)", where the last
item on the list with the largest integer is the most recent snapshot:

```
qvm-volume revert vmname:private <revision>
```
