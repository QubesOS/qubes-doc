---
layout: wiki
title: BackupRestore
permalink: /wiki/BackupRestore/
---

Backup, Restore, Migration Tools
================================

Qubes supports easy backups and restores of your VMs, and specifically very easy migration between two systems.

There are currently two command-line tools for this: `qvm-backup` and `qvm-backup-restore`, both of which are available in Qubes Alpha 2 (qubes-core-dom0 \>= 1.1.8). Users of Qubes Alpha 1 can still download the `qvm-backup` too [​here](http://qubes-os.org/yum/misc/qvm-backup) and use it to make a full backup of their system, and later restore it on Qubes Alpha 2, using qvm-backup-restore (the latter is not avilable on Alpha 1).

Making a full backup of your VMs
--------------------------------

1.  Mount the external media on which to place the backup:

``` {.wiki}
mount /dev/<backup_device> /mnt/backup
```

```Note:``` It's strongly recommended to use encrypted media for the backup (`qvm-backup` will not encrypt the backup). One can use e.g. LUKS for full encryption (type: `man cryptsetup` for details), in which case the `/dev/<backup_device>` would be something like `/dev/mapper/backup` -- a diskmapper device created by cryptsetup from the actual encrypted media.

1.  Do the backup:

``` {.wiki}
qvm-backup /mnt/backup
```

The `qvm-backup` tool will take care about backing up the VMs configuration, and all your AppVMs private storages, and, if necessary, will also backup any custom templates or netvms that any of your AppVMs might be using.

Restoring VMs from a backup
---------------------------

1.  Mount the media with a backup:

1.  Do the restore:

``` {.wiki}
qvm-backup-restore /mnt/backup/<specific_backup_dir>
```

The `qvm-backup-restore` tool will restore all the VMs (and any backed up custom template VMs), update Qubes database, and will add appmenus for the restored VMs. Your existing VMs will not be removed, unless there was a name conflict, i.e. there existed a VM with the same name on the host and in the backup. In this case, `qvm-backup-restore` will refuse to continue, and will ask you to remove the conflicting VM from the host first.
