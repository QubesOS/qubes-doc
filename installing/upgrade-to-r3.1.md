---
layout: doc
title: Upgrading to R3.1
permalink: /doc/upgrade-to-r3.1/
redirect_from:
- /en/doc/upgrade-to-r3.1/
- /doc/UpgradeToR3.1/
- /doc/UpgradeToR3.1rc1/
---

Upgrading Qubes R3.0 to R3.1
======================================

Current Qubes R3.1 (R3.1) systems can be upgraded in-place to the latest R3.1
by following the procedure below.

**Before attempting either an in-place upgrade or a clean installation, we
strongly recommend that users back up the system by using the built-in [backup
tool](/doc/backup-restore/).**

Upgrade all Template and Standalone VM(s)
-----------------------------------------

By default, in Qubes R3.0, there is only one Template VM, however users are
free to create more Template VMs for special purposes, as well as Standalone
VMs. More information on using multiple Template VMs, as well as Standalone
VMs, can be found [here](/doc/software-update-vm/). The steps described in this
section should be repeated in **all** user's Template and Standalone VMs.

### Upgrade Fedora template:

1.  Open terminal in the template VM (or standalone VM). E.g. use the Qubes
Manager's right-click menu and choose Run Command in VM and type
`gnome-terminal` there.
2.  Install `qubes-upgrade-vm` package:

        sudo yum install qubes-upgrade-vm

3.  Proceed with normal update in the template:

        sudo yum update

4.  Shutdown the template VM.

### Upgrade Debian template:

1.  Open terminal in the template VM (or standalone VM). E.g. use the Qubes
Manager's right-click menu and choose Run Command in VM and type
`gnome-terminal` there.
2.  Update repository definition:

        sudo cp /etc/apt/sources.list.d/qubes-r3.list /etc/apt/sources.list.d/qubes-r3-upgrade.list
        sudo sed -i 's/r3.0/r3.1/' /etc/apt/sources.list.d/qubes-r3-upgrade.list

3.  Proceed with normal update in the template:

        sudo apt-get update
        sudo apt-get dist-upgrade

    There will be some error messages during the process, but our tests does
    not revealed any negative consequences.

4.  Shutdown the template VM.

Upgrading dom0
--------------

Be sure to do steps described in this section after *all* your template and
standalone VMs got updated as described in the section above. Also make sure
you haven't shutdown any of: netvm, firewallvm - you will not be able to start
them again.

1.  Open terminal in Dom0. E.g. Start-\>System Settings-\>Konsole.
2.  Upgrade dom0 to R3.1:

        sudo qubes-dom0-update --releasever=3.1

3.  If above step completed successfully you should have `qubes-core-dom0` at
least 3.1.4. If not, repeat above step with additional `--clean` option.

4.  Reboot the system.
    
    It may happen that the system hang during the reboot. Hard reset the system
    in such case, all the filesystems are unmounted at this stage.

Please note that if you use Anti Evil Maid, then it won't be able to unseal the
passphrase this time, because the Xen, kernel, and initramfs binaries have
changed. Once the system boots up again, you could reseal your Anti Evil Maid's
passphrase to the new configuration. Please consult Anti Evil Maid
documentation for explanation on how to do that.

Now, when you have dom0 upgraded, you can install new templates from Qubes R3.1
repositories. Especially Fedora 23 - default Qubes R3.1 template:

    sudo qubes-dom0-update qubes-template-fedora-23

