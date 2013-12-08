---
layout: wiki
title: UpgradeToR2B3
permalink: /wiki/UpgradeToR2B3/
---

Upgrading Qubes R2 beta2 to R2 beta3
====================================

Existing users of Qubes R2 beta2 can upgrade their systems to the latest R2 beta release by following the procedure below. As usual, it is advisable to backup the system before proceeding with the upgrade. While it is possible to upgrade the system **it is strongly recommended to reinstall it**. You will preserve all your data and settings thanks to [backup and restore tools](/wiki/BackupRestore).

Upgrade all Template and Standalone VM(s)
-----------------------------------------

By default, in Qubes R2, there is only one Template VM, however users are free to create more Template VMs for special purposes, as well as Standalone VMs. More information on using multiple Template VMs, as well as Standalone VMs, can be found [here](/wiki/SoftwareUpdateVM). The steps described in this section should be repeated in *all* user's Template and Standalone VMs.

It is critical to complete this step **before** proceeding to dom0 upgrade. Otherwise you will most likely ends with unusable system.

1.  Open terminal in the template VM (or standalone VM). E.g. use the Qubes Manager's right-click menu and choose Run Command in VM and type `gnome-terminal` there.
2.  Proceed with normal update in the template:

    ``` {.wiki}
    sudo yum update
    ```

3.  Ensure that you've got qubes-core-vm package version 2.1.13-3.fc18:

    ``` {.wiki}
    rpm -q qubes-core-vm
    ```

4.  Update the system to R2 beta3 packages:

    ``` {.wiki}
    sudo yum --enablerepo=qubes-vm-r2b3-current update
    ```

5.  **Do not** shutdown the VM.

Upgrading dom0
--------------

Be sure to do steps described in this section after *all* your template and standalone VMs got updated as described in the section above. Also make sure you haven't shutdown any of: netvm, firewallvm, fedora-18-x64 (or to be more precise: template which your netvm and firewallvm is based on).

1.  Open terminal in Dom0. E.g. Start-\>System Settings-\>Konsole.
2.  Upgrade the `qubes-release` package to the latest version which brings in new repo definitions and R2 signing keys:

    ``` {.wiki}
    sudo qubes-dom0-update qubes-release
    ```

    This should install `qubes-release-2-3.1` in your Dom0.

3.  Upgrade dom0 to R2 beta3:

    ``` {.wiki}
    sudo qubes-dom0-update --enablerepo=qubes-dom0-r2b3-current
    ```

4.  If above step completed successfully you should have qubes-core-dom0 at least 2.1.34. If not, repeat above step with additional `--clean` option.
5.  Now is the time to shutdown all the VMs:

    ``` {.wiki}
    qvm-shutdown --all --wait
    ```

6.  Reboot the system.

Please note that if you use Anti Evil Maid, then it won't be able to unseal the passphrase this time, because the Xen, kernel, and initramfs binaries have changed. Once the system boots up again, you could reseal your Anti Evil Maid's passphrase to the new configuration. Please consult Anti Evil Maid documentation for explanation on how to do that.
