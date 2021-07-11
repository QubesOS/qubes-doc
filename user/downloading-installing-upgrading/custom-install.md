---
advanced: true
lang: en
layout: doc
permalink: /doc/custom-install/
redirect_from:
- /doc/encryption-config/
ref: 152
title: Custom installation
---

In the present context, "custom installation" refers to things like manual partitioning, setting up LVM and RAID, and manual LUKS encryption configuration.

## Installer Defaults

For reference, these are the typical defaults for a single disk with legacy boot:

~~~
Mount Point: /boot
Desired Capacity: 1024 MiB
Device Type: Standard Partition
File System: ext4
Name: (none)

Mount Point: /
Desired Capacity: (your choice)
Device Type: LVM Thin Provisioning
Volume Group: qubes_dom0
File System: ext4
Name: root

Mount Point: (none)
Desired Capacity: 10 GiB
Device Type: LVM
Volume Group: qubes_dom0
File System: swap
Name: swap
~~~

~~~
SUMMARY OF CHANGES

Order   Action              Type                    Device              Mount point

1       Destroy Format      Unknown                 Disk (sda)
2       Create Format       partition table (MSDOS) Disk (sda)
3       Create Device       partition               sda1 on Disk
4       Create Format       ext4                    sda1 on Disk        /boot
5       Create Device       partition               sda2 on Disk
6       Create Format       LUKS                    sda2 on Disk
7       Create Device       luks/dm-crypt           luks-sda2
8       Create Format       physical volume (LVM)   luks-sda2
9       Create Device       lvmvg                   qubes_dom0
10      Create Device       lvmthinpool             qubes_dom0-pool00
11      Create Device       lvmthinlv               qubes_dom0-root
12      Create Device       lvmlv                   qubes_dom0-swap
13      Create Format       swap                    qubes_dom0-swap
14      Create Format       ext4                    qubes_dom0-root     /
~~~

## Typical Partition Schemes

If you want your partition/LVM scheme to look like the Qubes default but with a few tweaks, follow this example.
With a single disk, the result should look something like this:

~~~
NAME                                SIZE    TYPE    MOUNTPOINT
sda                                         disk
├──sda1                               1G    part    /boot
└──sda2                                     part
   └──luks-<UUID>                           crypt
      ├──qubes_dom0-pool00_tmeta            lvm
      ├──qubes_dom0-pool00_tdata            lvm
      └──qubes_dom0-swap                    lvm     [SWAP]
~~~

## Encryption Defaults

By default, `cryptsetup 1.7.5` will create a LUKS/dm-crypt volume as follows:

~~~
Version:            1
Cipher name:        aes
Cipher mode:        xts-plain64
Hash spec:          sha256
~~~

~~~
$ cryptsetup --help
[...]
Default compiled-in device cipher parameters:
        loop-AES: aes, Key 256 bits
        plain: aes-cbc-essiv:sha256, Key: 256 bits, Password hashing: ripdemd160
        LUKS1: aes-xts-plain64, Key: 256 bits, LUKS header hashing: sha256, RNG: /dev/urandom
~~~

This means that, by default, Qubes inherits these upstream defaults:

- AES-128 [[1]](https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions)[[2]](https://wiki.archlinux.org/index.php/dm-crypt/Device_encryption)[[3]](https://github.com/dyne/Tomb/issues/238)
- SHA-256
- `/dev/urandom`
- probably an `iter-time` of one second

If, instead, you'd like to use AES-256, SHA-512, `/dev/random`, and a longer `iter-time`, for example, you can configure encryption manually by following the instructions below.

## Example: Custom LUKS Configuration

Boot into the Qubes installer, then press `ctrl`+`alt`+`F2` to get a virtual console.

1. (Optional) Wipe the disk:

    ```
    # dd if=/dev/zero of=/dev/sda bs=1M status=progress && sync
    ```

2. Create partitions:

    ```
    # fdisk /dev/sda
    ```

   Follow the steps to create two partitions:
   
   - ~500MiB-1GiB for `/boot`
   - The rest for `/` (might want to leave some for overprovisioning if it's an SSD)

4. Create LUKS encrypted volume:

    ```
    # cryptsetup -v --hash sha512 --cipher aes-xts-plain64 --key-size 512 --use-random --iter-time 10000 --verify-passphrase luksFormat /dev/sda2
    ```

5. Open encrypted volume:

    ```
    # cryptsetup open /dev/sda2 luks
    ```

6. Create LVM volumes:

    ```
    # pvcreate /dev/mapper/luks
    # vgcreate qubes_dom0 /dev/mapper/luks
    # lvcreate -n swap -L 10G qubes_dom0
    # lvcreate -T -l +100%FREE qubes_dom0/pool00
    # lvcreate -V1G -T qubes_dom0/pool00 -n root
    # lvextend -L <size_of_pool00> /dev/qubes_dom0/root
    ```

8. Proceed with the installer. You can do that either by pressing `ctrl`+`alt`+`F6`, or by rebooting and restarting the installation.
   At the disk selection screen, select:

    ```
    [x] I will configure partitioning.
    [ ] Encrypt my data.
    ```

9. Decrypt your partition. After decrypting you may assign mount points:
   Open the Unknown list and select `qubes_dom0-root`. Check the reformat box to the right and choose `ext4` as a filesystem. Enter `/` into the Mount Point field at the top.
   Repeat the process for `sda1` and `qubes_dom0-swap`. Those should be assigned to `/boot` and `swap` respectively.
   The default file systems are ext4 for `/boot` and `/`, and swap for `swap`.
   When you are finished, the Unknown list should go away, and all three mount points should be assigned. Proceed normally with the installation from there.
