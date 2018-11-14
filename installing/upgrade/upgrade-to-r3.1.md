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

**Before attempting either an in-place upgrade or a clean installation, we
strongly recommend that users [back up their systems](/doc/backup-restore/).**

Current Qubes R3.0 systems can be upgraded in-place to the latest R3.1
by following the procedure below.


Upgrade all Template and Standalone VM(s)
-----------------------------------------

By default, in Qubes R3.0, there is only one TemplateVM. However, users are
free to create more TemplateVMs for special purposes, as well as StandaloneVMs.
More information on using multiple TemplateVMs, as well as StandaloneVMs, can be
found [here](/doc/software-update-vm/). The steps described in this
section should be repeated in **all** the user's Template and Standalone VMs.


### Upgrade Fedora templates: ###

1.  Open a terminal in the TemplateVM (or StandaloneVM). (E.g., use Qubes VM
    Manager's right-click menu, choose "Run Command in VM," and type
    `gnome-terminal` there.)

2.  Install the `qubes-upgrade-vm` package:

        sudo yum install qubes-upgrade-vm

3.  Proceed with a normal upgrade in the template:

        sudo yum upgrade

4.  Shut down the template VM.


### Upgrade Debian (and Whonix) templates: ###

1.  Open a terminal in the TemplateVM (or StandaloneVM). (E.g., use Qubes VM
    Manager's right-click menu, choose "Run Command in VM," and type
    `gnome-terminal` there.)

2.  Update repository definition:

        sudo cp /etc/apt/sources.list.d/qubes-r3.list /etc/apt/sources.list.d/qubes-r3-upgrade.list
        sudo sed -i 's/r3.0/r3.1/' /etc/apt/sources.list.d/qubes-r3-upgrade.list

3.  Proceed with a normal update in the template:

        sudo apt-get update
        sudo apt-get dist-upgrade

4.  Remove unnecessary now file:

        sudo rm -f /etc/apt/sources.list.d/qubes-r3-upgrade.list

5.  Shut down the template VM.


Upgrading dom0
--------------

**Important:** Do not perform the steps described in this section until **all**
your Template and Standalone VMs have been upgraded as described in the previous
section. Also, do not shut down `sys-net` or `sys-firewall`, since you will not
be able to start them again until after the entire in-place upgrade procedure is
complete.

1.  Open a terminal in Dom0. (E.g., Start -\> System Settings -\> Konsole.)

2.  Upgrade dom0 to R3.1:

        sudo qubes-dom0-update --releasever=3.1

    At this point, most of the `qvm-*` tools will stop working until after you
    reboot the system.

3.  If the previous step completed successfully, your `qubes-core-dom0` version
    should be `3.1.4` or higher. If it's not, repeat the previous step with the
    `--clean` option.

4.  Reboot dom0.
    
    The system may hang during the reboot. If that happens, do not panic. All
    the filesystems will have already been unmounted at this stage, so you can
    simply perform a hard reboot (e.g., hold the physical power button down
    until the machine shuts off, wait a moment, then press it again to start it
    back up).

Please note that if you use [Anti Evil Maid](/doc/anti-evil-maid), it won't be
able to unseal the passphrase the first time the system boots after performing
this in-place upgrade procedure since the Xen, kernel, and initramfs binaries
will have changed. Once the system boots up again, you can reseal your Anti Evil
Maid passphrase to the new configuration. Please consult the Anti Evil Maid
[documentation](/doc/anti-evil-maid) for instructions on how to do that.

If you use USB VM, you may encounter problem with starting it on updated Xen
version (because of strict default settings). Take a look at 
[User FAQ](/faq/#i-created-a-usbvm-and-assigned-usb-controllers-to-it-now-the-usbvm-wont-boot)
for details.

Once you have upgraded dom0, you can install new templates from Qubes R3.1
repositories, in particular the new default Fedora 23 template:

    sudo qubes-dom0-update qubes-template-fedora-23

