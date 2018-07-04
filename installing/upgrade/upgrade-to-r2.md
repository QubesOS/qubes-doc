---
layout: doc
title: Upgrading to R2
permalink: /doc/upgrade-to-r2/
redirect_from:
- /en/doc/upgrade-to-r2/
- /doc/UpgradeToR2/
- /doc/UpgradeToR2rc1/
- /wiki/UpgradeToR2rc1/
---

Upgrading Qubes R2 Beta 3 to R2
===================================

Current Qubes R2 Beta 3 (R2B3) systems can be upgraded in-place to the latest R2 (R2) release by following the procedure below.

**Before attempting either an in-place upgrade or a clean installation, we strongly recommend that users back up the system by using the built-in [backup tool](/doc/backup-restore/).**

Upgrade Template and Standalone VM(s)
-------------------------------------

-   Qubes R2 comes with new template based on Fedora 20. You can upgrade existing template according to procedure described [here](/doc/fedora-template-upgrade-20/).

-   **It also possible to download a new Fedora 20-based template from our repositories**. To do this please first upgrade the Dom0 distro as described in the section below.

While technically it is possible to use old Fedora 18 template on R2, it is strongly recommended to upgrade all the Template VMs and Standalone VMs, because Fedora 18 no longer receive security updates.

By default, in Qubes R2, there is only one Template VM, however users are free to create more Template VMs for special purposes, as well as Standalone VMs. If more than one template and/or Standalone VMs are used, then it is recommended to upgrade/replace all of them. More information on using multiple Template VMs, as well as Standalone VMs, can be found [here](/doc/software-update-vm/).

Upgrading dom0
--------------

Note that dom0 in R2 is based on Fedora 20, in contrast to Fedora 18 in previous release, so this operation will upgrade a lot of packages.

1.  Open terminal in Dom0. E.g. Start-\>System Settings-\>Konsole.

1.  Install all the updates for Dom0:

    ~~~
    sudo qubes-dom0-update
    ~~~

After this step you should have `qubes-release-2-5` in your Dom0. Important: if you happen to have `qubes-release-2-6*` then you should downgrade to `qubes-release-2-5`! The `qubes-release-2-6*` packages have been uploaded to the testing repos and were kept there for a few hours, until we realized they bring incorrect repo definitions and so we removed them and also have changed the update procedure a bit (simplifying it).

1.  Upgrade dom0 to R2:

Note: be sure that the VM used as a update-downloading-vm (by default its the firewallvm based on the default template) has been updated to the latest Qubes packages, specifically `qubes-core-vm-2.1.33` or later. This doesn't imply that the VM must already be upgraded to fc20 -- for Dom0 upgrade we could still use an fc18-based VM (updatevm) it is only important to install the latest Qubes packages there.

~~~
sudo qubes-dom0-update qubes-dom0-dist-upgrade
sudo qubes-dom0-update
~~~

1.  If above step completed successfully you should have `qubes-release-2-9` or later. If not, repeat above step with additional `--clean` option.

4a. If you chose not to upgrade your fc18 templates, but instead to download our new fc20-based template you should now be able to do that by simply typing:

~~~
sudo qubes-dom0-update qubes-template-fedora-20-x64
~~~

1.  Reboot the system.

Please note that if you use Anti Evil Maid, then it won't be able to unseal the passphrase this time, because the Xen, kernel, and initramfs binaries have changed. Once the system boots up again, you could reseal your Anti Evil Maid's passphrase to the new configuration. Please consult Anti Evil Maid documentation for explanation on how to do that.
