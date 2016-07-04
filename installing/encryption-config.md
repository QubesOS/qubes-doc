---
layout: doc
title: Manual Encryption Configuration
permalink: /doc/encryption-config/
---

Manual Encryption Configuration
===============================

Qubes OS uses full disk encryption (FDE) by default. If you are an advanced
user who wishes to customize your encryption parameters during installation,
this page can help.

The Qubes installer uses `cryptsetup` (LUKS/dm-crypt) under the hood. You can
configure the encryption options while installing Qubes as follows:

01. Boot into the installer. Wait for first GUI screen to appear where it asks 
    about language/localization .
02. Press `Ctrl+Alt+F2` on your keyboard to escape to a shell session. (If you
    are on a laptop, and your laptop keyboard des not work properly, you may have
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

-----

These instructions were adapted from those provided by Qubes user [Jake] on the
`qubes-users` [mailing list].

[Jake]: https://groups.google.com/d/msg/qubes-users/cykOGRa0Im0/vK7j8aQOXkYJ
[mailing list]: /mailing-lists/

