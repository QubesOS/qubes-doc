---
layout: wiki
title: UpgradeToR2rc1
permalink: /wiki/UpgradeToR2rc1/
---

**DRAFT**
=========

Upgrading Qubes R2 Beta 3 to R2 rc1
===================================

Current Qubes R2 Beta 3 (R2B3) systems can be upgraded in-place to the latest R2 rc1 (R2rc1) release by following the procedure below.

**Before attempting either an in-place upgrade or a clean installation, we strongly recommend that users back up the system by using the built-in [backup tool](/wiki/BackupRestore).**

Upgrade Template and Standalone VM(s)
-------------------------------------

By default, in Qubes R2, there is only one Template VM, however users are free to create more Template VMs for special purposes, as well as Standalone VMs. More information on using multiple Template VMs, as well as Standalone VMs, can be found [here](/wiki/SoftwareUpdateVM).

Qubes R2 rc1 comes with new template based on Fedora 20. You can upgrade existing template according to procedure described [here](/wiki/FedoraTemplateUpgrade). While technically it is possible to use old Fedora 18 template on R2 rc1, it is strongly recommended to upgrade all the Template VMs and Standalone VMs, because Fedora 18 no longer receive security updates.

Upgrading dom0
--------------

Note that dom0 in R2rc1 is based on Fedora 20, in contrast to Fedora 18 in previous release, so this operation will upgrade a lot of packages.

1.  Open terminal in Dom0. E.g. Start-\>System Settings-\>Konsole.
2.  Upgrade the `qubes-release` package to the latest version which brings in new repo definitions and R2 signing keys:

    ``` {.wiki}
    sudo qubes-dom0-update qubes-release
    ```

    This should install `qubes-release-2-5` in your Dom0.

3.  Upgrade dom0 to R2 rc1:

    ``` {.wiki}
    sudo qubes-dom0-update qubes-dom0-dist-upgrade
    sudo qubes-dom0-update
    ```

4.  If above step completed successfully you should have `qubes-release` at least 2-7. If not, repeat above step with additional `--clean` option.
5.  Reboot the system.

Please note that if you use Anti Evil Maid, then it won't be able to unseal the passphrase this time, because the Xen, kernel, and initramfs binaries have changed. Once the system boots up again, you could reseal your Anti Evil Maid's passphrase to the new configuration. Please consult Anti Evil Maid documentation for explanation on how to do that.
