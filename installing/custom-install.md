---
layout: doc
title: Custom Installation
permalink: /doc/custom-install/
redirect_from:
 - /doc/encryption-config/
---

Custom Installation
===================

In the present context, "custom installation" refers to things like manual
partitioning, setting up LVM and RAID, and manual LUKS encryption configuration.


Installer Defaults (R3.2)
-------------------------

For reference, these are the defaults for a single disk:

~~~
Mount Point: `/`
Desired Capacity: (your choice)
Device Type: `LVM`
Volume Group: `qubes_dom0`
File System: `ext4`
Name: `root`

Mount Point: `/boot`
Desired Capacity: 500 MiB (recommended)
Device Type: Standard Partition
File System: `ext4`

Mount Point: (none)
Desired Capacity: 9.44 GiB (recommended)
Device Type: LVM
Volume Group: qubes_dom0
File System: `swap`
Name: `swap`
~~~


Typical Partition Schemes
-------------------------

If you want your partition/LVM scheme to look like the Qubes default but
with a few tweaks, follow these examples. With a single disk, the result
should look something like this:

~~~
    NAME                        TYPE    MOUNTPOINT
    sda                         disk
    ├──sda1                     part    /boot
    └──sda2                     part
       └──luks-<UUID>           crypt
          ├──qubes_dom0-root    lvm     /
          └──qubes_dom0-swap    lvm     [SWAP]
~~~

If you're using `mdadm` software RAID, it should look something like this:

~~~
    NAME                           TYPE    MOUNTPOINT
    sda                            disk
    ├──sda1                        part
    │  └──md0                      raid1   /boot
    └──sda2                        part
       └──md1                      raid1
          └──luks-<UUID>           crypt
             ├──qubes_dom0-root    lvm     /
             └──qubes_dom0-swap    lvm     [SWAP]
    sdb                            disk
    ├──sdb1                        part
    │  └──md0                      raid1   /boot
    └──sdb2                        part
       └──md1                      raid1
          └──luks-<UUID>           crypt
             ├──qubes_dom0-root    lvm     /
             └──qubes_dom0-swap    lvm     [SWAP]
~~~


Example: LVM on LUKS on RAID (R3.2)
-----------------------------------

Boot into the Qubes installer, then press `ctrl`+`alt`+`F2` to get a virtual
console.

1. (Optional) Wipe both disks:

        # hdparm --user-master u --security-set-pass pass /dev/sda
        # time hdparm --user-master u --security-erase-enhanced pass /dev/sda
        # hdparm --user-master u --security-set-pass pass /dev/sdb
        # time hdparm --user-master u --security-erase-enhanced pass /dev/sdb

2. Create desired partitions:

        # fdisk /dev/sda
        <create partitions>
        # fdisk /dev/sdb
        <create partitions>

3. Create RAID devices:

        # mdadm --create --verbose /dev/md0 --level=mirror --raid-devices=2 /dev/sda1 /dev/sdb1
        # mdadm --create --verbose /dev/md1 --level=mirror --raid-devices=2 /dev/sda2 /dev/sdb2

4. Create LUKS encrypted volume:

        # cryptsetup -v --hash sha512 --cipher aes-xts-plain64 --key-size 512 --use-random --iter-time 5000 --verify-passphrase luksFormat /dev/md1

5. Open encrypted volume:

        # cryptsetup open /dev/md1 luks

6. Create LVM volumes:

        # pvcreate /dev/mapper/luks
        # vgcreate qubes_dom0 /dev/mapper/luks
        # lvcreate -n swap -L 10G qubes_dom0
        # lvcreate -n root -l +100%FREE qubes_dom0

7. Proceed with installer. At the disk selection screen, select:

        [x] I will configure partitioning.
        [ ] Encrypt my data.

Continue normally from here.


Manual Encryption Configuration (R3.1)
--------------------------------------

Qubes OS uses full disk encryption (FDE) by default. If you are an advanced
user who wishes to customize your encryption parameters during installation,
this page can help.

The Qubes installer uses `cryptsetup` (LUKS/dm-crypt) under the hood. You can
configure the encryption options while installing Qubes as follows:

01. Boot into the installer. Wait for first GUI screen to appear where it asks 
    about language/localization .
02. Press `Ctrl+Alt+F2` on your keyboard to escape to a shell session. (If you
    are on a laptop, and your laptop keyboard does not work properly, you may have
    to plug in a USB keyboard.)
03. Check and adjust the partitioning on the drive you plan to install to with
    `parted`. For example, you can leave the partition table as `msdos/MBR` type,
    then create a 500 MB ext4 boot partition, a 10 GB swap partition, and use the
    rest of the drive (minus overprovisioning space for SSDs) for the root
    partition.
04. Run  to set the  LUKS options as you like and set the passphrase:

        # cryptsetup <options> luksFormat <partition>

    For example:

        # cryptsetup -v --hash sha512 --cipher aes-xts-plain64 --key-size 512 --use-random --iter-time 5000 --verify-passphrase luksFormat /dev/sda2

05. (Optional) Make sure the new container works:

        # cryptsetup open /dev/sda2 test
        # mkfs.ext4 /dev/mapper/test
        # mount /dev/mapper/test /mnt/test
        # umount /dev/mapper/test
        # cryptsetup close test

06. Everything should be set with the preparation, so press `Ctrl+Alt+F7` to go
    back to the GUI installer.
07. Continue installing as usual. When you get to the disk
    partitioning/allocation part, pay attention.
08. When you select the disk, it may complain about only having a few MB of
    space. Uncheck the "Encrypt and ask me about the passphrase later" box and
    press the "Custom" button. 
09. In this menu, you should see the unencrypted boot partition and the encrypted
    LUKS partitions you created earlier. You must unlock the LUKS partition here, 
    i.e. enter passphrases. 
10. Set the mount points on these partitions once they are decrypted. (This part
    may be a bit glitchy, but you should be able to get it working after a
    reboot.) For example, set the mount point for the primary LUKS partition as
    `/`. Make sure the "Encrypted" box stays checked and that you check the
    "Format" box (required for the root partition). Similarly, set `/boot` as
    the mount point for the unencrypted boot partition and `swap` as the mount
    point for the swap partition.
11. Now the install should complete without any other issues. When it's
    finished, you'll have LUKS-encrypted partitions with the options you chose
    above. You can verify this command in dom0:

        # cryptsetup luksDump <partition>

    For example:

        # cryptsetup luksDump /dev/sda2

