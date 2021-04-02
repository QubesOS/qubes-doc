---
lang: en
layout: doc
permalink: /doc/secondary-storage/
redirect_from:
- /en/doc/secondary-storage/
- /doc/SecondaryStorage/
- /wiki/SecondaryStorage/
ref: 187
title: Secondary Storage
---

# Storing AppVMs on Secondary Drives

Suppose you have a fast but small primary SSD and a large but slow secondary HDD.
You want to store a subset of your AppVMs on the HDD.

## Instructions

Qubes 4.0 is more flexible than earlier versions about placing different VMs on different disks.
For example, you can keep templates on one disk and AppVMs on another, without messy symlinks.

You can query qvm-pool to list available storage drivers.

``` shell_session
qvm-pool --help-drivers
```
qvm-pool driver explaination :
```shell_session
<file> refers to using a simple file for image storage and lacks a few features.
<file-reflink> refers to storing images on a filesystem supporting copy on write.
<linux-kernel> refers to a directory holding kernel images.
<lvm_thin> refers to LVM managed pools.
```
In theory, you can still use file-based disk images ("file" pool driver), but it lacks some features such as you won't be able to do backups without shutting down the qube.

Additionnal storage can also be added on a Btrfs filesystem. A unique feature of Btrfs over LVM is that data can be compressed transparently. The subvolume can also be backuped using snapshots for an additionnal layer of protection; Btrfs supports differents level of redundancy; it has parity checksum; it is able to be expanded/shrinked. Starting/stoping a VM has less impact and less chances of causing slowdown of the system as some have noted with LVM. Revelant information for general btrfs configuration will be provided after LVM section.

### LVM storage

These steps assume you have already created a separate [volume group](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/logical_volume_manager_administration/vg_admin#VG_create) and [thin pool](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/logical_volume_manager_administration/thinly_provisioned_volume_creation) (not thin volume) for your HDD.
See also [this example](https://www.linux.com/blog/how-full-encrypt-your-linux-system-lvm-luks) if you would like to create an encrypted LVM pool (but note you can use a single logical volume if preferred, and to use the `-T` option on `lvcreate` to specify it is thin). You can find the commands for this example applied to Qubes at the bottom of this R4.0 section.

First, collect some information in a dom0 terminal:

```shell_session
sudo pvs
sudo lvs
```

Take note of the VG and thin pool names for your HDD, then register it with Qubes:

```shell_session
# <pool_name> is a freely chosen pool name
# <vg_name> is LVM volume group name
# <thin_pool_name> is LVM thin pool name
qvm-pool --add <pool_name> lvm_thin -o volume_group=<vg_name>,thin_pool=<thin_pool_name>,revisions_to_keep=2
```

### BTRFS storage
Theses steps assume you have already created a separate Btrfs filesystem for your HDD, that it is encrypted with LUKS and it is mounted. It is recommended to use a subvolume as it enables compression and excess storage can be use for other things.


It is possible to use already available Btrfs storage if it is configured. In dom0, available Btrfs storage can be displayed using :
```shell_session
mount -t btrfs
btrfs show filesystem
```
To register the storage to qubes :

```shell_session
# <pool_name> is a freely chosen pool name
# <dir_path> is the mounted path to the second btrfs storage
qvm-pool --add <pool_name> file-reflink -o dir_path=<dir_path>,revisions_to_keep=2
```

#### Using the new pool

Now, you can create qubes in that pool:

```shell_session
qvm-create -P <pool_name> --label red <vmname>
```

It isn't possible to directly migrate an existing qube to the new pool, but you can clone it there, then remove the old one:

```shell_session
qvm-clone -P <pool_name> <sourceVMname> <cloneVMname>
qvm-remove <sourceVMname>
```

If that was a template, or other qube referenced elsewhere (NetVM or such), you will need to adjust those references manually after moving.
For example:

```shell_session
qvm-prefs <appvmname_based_on_old_template> template <new_template_name>
```

#### Example HDD setup

Assuming the secondary hard disk is at /dev/sdb (it will be completely erased), you can set it up for encryption by doing in a dom0 terminal (use the same passphrase as the main Qubes disk to avoid a second password prompt at boot):

```shell_session
sudo cryptsetup luksFormat --hash=sha512 --key-size=512 --cipher=aes-xts-plain64 --verify-passphrase /dev/sdb
sudo blkid /dev/sdb
```

Note the device's UUID (in this example "b209..."), we will use it as its luks name for auto-mounting at boot, by doing:

```shell_session
sudo nano /etc/crypttab
```

And adding this line (change both "b209..." for your device's UUID from blkid) to crypttab:

```shell_session
luks-b20975aa-8318-433d-8508-6c23982c6cde UUID=b20975aa-8318-433d-8508-6c23982c6cde none
```

Reboot the computer so the new luks device appears at /dev/mapper/luks-b209... and we can then create its pool, by doing this on a dom0 terminal (substitute the b209... UUIDs with yours):

##### For LVM

First create the physical volume

```shell_session
sudo pvcreate /dev/mapper/luks-b20975aa-8318-433d-8508-6c23982c6cde
```

Then create the LVM volume group, we will use for example "qubes" as the <vg_name>:

```shell_session
sudo vgcreate qubes /dev/mapper/luks-b20975aa-8318-433d-8508-6c23982c6cde
```

And then use "poolhd0" as the <thin_pool_name> (LVM thin pool name):

```shell_session
sudo lvcreate -T -n poolhd0 -l +100%FREE qubes
```

Finally we will tell Qubes to add a new pool on the just created thin pool

```shell_session
qvm-pool --add poolhd0_qubes lvm_thin -o volume_group=qubes,thin_pool=poolhd0,revisions_to_keep=2
```
#### For Btrfs

First create the physical volume

```shell_session
# <label> Btrfs Label
sudo mkfs.btrfs -L <label> /dev/mapper/luks-b20975aa-8318-433d-8508-6c23982c6cde
```

Then mount the new Btrfs to a temporary path

```shell_session
sudo mount /dev/mapper/luks-b20975aa-8318-433d-8508-6c23982c6cde /mnt/new_qube_storage
```
Create a subvolume to hold the data. 
```
sudo btrfs subvolume create /mnt/new_qube_storage/qubes
```
Unmount the temporary Btrfs filesystem
```shell_session
sudo umount /mnt/new_qube_storage
```
Mount the subvolume with compression enabled if desired
```shell_session
# <compression> zlib|lzo|zstd
# <subvol> btrfs subvolume "qubes" in this example
sudo mount /dev/mapper/luks-b20975aa-8318-433d-8508-6c23982c6cde /var/lib/qubes_newpool -o compress=<compression>,subvol=qubes
```

Finally we will tell Qubes to add a new pool on the just created Btrfs subvolume

```shell_session
qvm-pool --add poolhd0_qubes file-reflink -o dir_path=/var/lib/qubes_newpool,revisions_to_keep=2
```

By default VMs will be created on the main Qubes disk (i.e. a small SSD), to create them on this secondary HDD do the following on a dom0 terminal:

```shell_session
qvm-create -P poolhd0_qubes --label red unstrusted-hdd
```

Verify that corresponding lines to /etc/fstab and /etc/cryptab where added to enable auto mounting of the new pool.


[Qubes Backup]: /doc/BackupRestore/
[TemplateVM]: /doc/Templates/
