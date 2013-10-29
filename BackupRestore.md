---
layout: wiki
title: BackupRestore
permalink: /wiki/BackupRestore/
---

Backup, Restore, Migration Tools
================================

Qubes supports easy backups and restores of your VMs, and specifically very easy migration between two systems.

There are currently two command-line tools for this: `qvm-backup` and `qvm-backup-restore`, both of which are available in Qubes Alpha 2 (qubes-core-dom0 \>= 1.1.8). Users of Qubes Alpha 1 can still download the `qvm-backup` too [​here](http://qubes-os.org/yum/misc/qvm-backup) and use it to make a full backup of their system, and later restore it on Qubes Alpha 2, using qvm-backup-restore (the latter is not available on Alpha 1).

Making a full backup of your VMs
--------------------------------

1.  Prepare an encrypted external medium to store the backup

It is strongly recommended to use encrypted media for the backup. `qvm-backup` will not encrypt the backup!

Steps to create a fully encrypted LUKS volume on the external USB hard drive /dev/sdb:

**WARNING**: Everything on your external USB drive will be deleted with this process!

``` {.wiki}
$ sudo wipefs -a /dev/sdb
$ sudo cryptsetup luksFormat /dev/sdb
$ sudo blkid /dev/sdb
$ sudo cryptsetup open --type luks UUID=the-long-UUID-you-just-got-from-blkid backup
$ sudo mkfs.ext4 -m 0 /dev/mapper/backup
```

1.  Mount the encrypted medium on which the backup will be stored

``` {.wiki}
$ sudo mkdir /backup
$ sudo blkid /dev/mapper/backup
$ sudo vi /etc/fstab
(add a line similar to this:
UUID=the-SECOND-long-UUID-you-just-got-for-the-mapper-device /mnt/backup ext4 defaults 1 2
)
$ sudo mount /mnt/backup
```

Now anything we store in /mnt/backup is stored on the encrypted LUKS volume of our external USB drive.

1.  Backup your VMs

``` {.wiki}
$ sudo qvm-backup /mnt/backup
```

The `qvm-backup` tool will take care about backing up the VMs configuration, and all your AppVMs private storages, and, if necessary, will also backup any custom templates or netvms that any of your AppVMs might be using.

1.  Lock the encrypted volume

``` {.wiki}
$ sudo umount /mnt/backup
$ sudo cryptsetup close backup
```

Restoring VMs from a backup
---------------------------

1.  Mount the media with your backups

``` {.wiki}
$ sudo mount /mnt/backup
```

1.  Restore VMs

``` {.wiki}
$ sudo qvm-backup-restore /mnt/backup/<specific_backup_dir>
```

The `qvm-backup-restore` tool will restore all the VMs (and any backed up custom template VMs), update the Qubes database and add appmenus for the restored VMs. Your existing VMs will not be removed.

If there is a name conflict, i.e. you try restoring a VM with the same name as a VM already on the host, `qvm-backup-restore` will refuse to continue and will ask you to remove (or rename) the conflicting VM from the host first.
