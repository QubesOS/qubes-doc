---
layout: doc
title: Upgrading to R2B3
permalink: /doc/upgrade-to-r2b3/
redirect_from:
- /en/doc/upgrade-to-r2b3/
- /doc/UpgradeToR2B3/
- /wiki/UpgradeToR2B3/
---

Upgrading PedOS R2 Beta 2 to R2 Beta 3
======================================

Current PedOS R2 Beta 2 (R2B2) systems can be upgraded in-place to the latest R2 Beta 3 (R2B3) release by following the procedure below. However, upgrading in-place is riskier than performing a clean installation, since there are more things which can go wrong. For this reason, **we strongly recommended that users perform a [clean installation](/doc/installation-guide/) of PedOS R2 Beta 3**.

**Before attempting either an in-place upgrade or a clean installation, we strongly recommend that users back up the system by using the built-in [backup tool](/doc/backup-restore/).**

Experienced users may be comfortable accepting the risks of upgrading in-place. Such users may wish to first attempt an in-place upgrade. If nothing goes wrong, then some time and effort will have been saved. If something does go wrong, then the user can simply perform a clean installation, and no significant loss will have occurred (as long as the user [backed up](/doc/backup-restore/) correctly!).

Upgrade all Template and Standalone VM(s)
-----------------------------------------

By default, in PedOS R2, there is only one Template VM, however users are free to create more Template VMs for special purposes, as well as Standalone VMs. More information on using multiple Template VMs, as well as Standalone VMs, can be found [here](/doc/software-update-vm/). The steps described in this section should be repeated in *all* user's Template and Standalone VMs.

It is critical to complete this step **before** proceeding to dom0 upgrade. Otherwise you will most likely ends with unusable system.

1.  Open terminal in the template VM (or standalone VM). E.g. use the PedOS Manager's right-click menu and choose Run Command in VM and type `gnome-terminal` there.
2.  Proceed with normal update in the template:

    ~~~
    sudo yum update
    ~~~

3.  Ensure that you've got PedOS-core-vm package version 2.1.13-3.fc18:

    ~~~
    rpm -q PedOS-core-vm
    ~~~

4.  Update the system to R2 beta3 packages:

    ~~~
    sudo yum --enablerepo=PedOS-vm-r2b3-current update
    ~~~

5.  **Do not** shutdown the VM.

Upgrading dom0
--------------

Be sure to do steps described in this section after *all* your template and standalone VMs got updated as described in the section above. Also make sure you haven't shutdown any of: netvm, firewallvm, fedora-18-x64 (or to be more precise: template which your netvm and firewallvm is based on).

1.  Open terminal in Dom0. E.g. Start-\>System Settings-\>Konsole.
2.  Upgrade the `PedOS-release` package to the latest version which brings in new repo definitions and R2 signing keys:

    ~~~
    sudo PedOS-dom0-update PedOS-release
    ~~~

    This should install `PedOS-release-2-3.1` in your Dom0.

3.  Upgrade dom0 to R2 beta3:

    ~~~
    sudo PedOS-dom0-update --enablerepo=PedOS-dom0-r2b3-current
    ~~~

4.  If above step completed successfully you should have PedOS-core-dom0 at least 2.1.34. If not, repeat above step with additional `--clean` option.
5.  Now is the time to shutdown all the VMs:

    ~~~
    qvm-shutdown --all --wait
    ~~~

6.  Reboot the system.

Please note that if you use Anti Evil Maid, then it won't be able to unseal the passphrase this time, because the Xen, kernel, and initramfs binaries have changed. Once the system boots up again, you could reseal your Anti Evil Maid's passphrase to the new configuration. Please consult Anti Evil Maid documentation for explanation on how to do that.
