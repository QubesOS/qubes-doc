---
lang: en
layout: doc
redirect_from:
- /doc/upgrade-to-r3.0/
- /en/doc/upgrade-to-r3.0/
- /doc/UpgradeToR3.0/
- /doc/UpgradeToR3.0rc1/
ref: 159
title: Upgrading to R3.0
---

# Upgrading Qubes R2 to R3.0

**This instruction is highly experimental, the official way to upgrade from R2 is to backup the data and reinstall the system. Use at your own risk!**

Current Qubes R3.0 (R3.0) systems can be upgraded in-place to the latest R3.0 by following the procedure below. However, upgrading in-place is riskier than performing a clean installation, since there are more things which can go wrong. For this reason, **we strongly recommended that users perform a [clean installation](/doc/installation-guide/) of Qubes R3.0**.

**Before attempting either an in-place upgrade or a clean installation, we strongly recommend that users back up the system by using the built-in [backup tool](/doc/backup-restore/).**

Experienced users may be comfortable accepting the risks of upgrading in-place. Such users may wish to first attempt an in-place upgrade. If nothing goes wrong, then some time and effort will have been saved. If something does go wrong, then the user can simply perform a clean installation, and no significant loss will have occurred (as long as the user [backed up](/doc/backup-restore/) correctly!).

## Upgrade all Template and Standalone VM(s)

By default, in Qubes R2, there is only one Template VM, however users are free to create more Template VMs for special purposes, as well as Standalone VMs. More information on using multiple Template VMs, as well as Standalone VMs, can be found [here](/doc/software-update-vm/). The steps described in this section should be repeated in **all** user's Template and Standalone VMs.

It is critical to complete this step **before** proceeding to dom0 upgrade. Otherwise you will most likely end with unusable system.

### Upgrade Fedora template:

1. Open terminal in the template VM (or standalone VM). E.g. use the Qubes Manager's right-click menu and choose Run Command in VM and type `gnome-terminal` there.
2. Install `qubes-upgrade-vm` package:

    ```
    sudo yum install qubes-upgrade-vm
    ```

3. Proceed with normal update in the template:

    ```
    sudo yum update
    ```

    You'll need to accept "Qubes Release 3 Signing Key" - it is delivered by signed qubes-upgrade-vm package (verify that the message is about local file), so you don't need to manually verify it.

4. Shutdown the template VM.

### Upgrade Debian template:

1. Open terminal in the template VM (or standalone VM). E.g. use the Qubes Manager's right-click menu and choose Run Command in VM and type `gnome-terminal` there.
2. Update repository definition:

    ```
    sudo cp /etc/apt/sources.list.d/qubes-r2.list
    /etc/apt/sources.list.d/qubes-r3-upgrade.list
    sudo sed -i 's/r2/r3.0/' /etc/apt/sources.list.d/qubes-r3-upgrade.list
    ```

3. Proceed with normal update in the template:

    ```
    sudo apt-get update
    sudo apt-get dist-upgrade
    ```

    There will be some error messages during the process, but our tests does
    not revealed any negative consequences.
    Update of `qubesdb-vm` package will restart the service, which will fail
    (after 3min timeout), but you can ignore this problem for now. After
    completing the whole upgrade the service will be properly restarted.

4. Shutdown the template VM.

## Upgrading dom0

Be sure to do steps described in this section after *all* your template and standalone VMs got updated as described in the section above. Also make sure you haven't shutdown any of: netvm, firewallvm - you will not be able to start them again.

1. Open terminal in Dom0. E.g. Start-\>System Settings-\>Konsole.
2. Upgrade the `qubes-release` package to the latest version which brings in new repo definitions and R2 signing keys:

    ```
    sudo qubes-dom0-update qubes-release
    ```

    This should install `qubes-release-2-12` in your Dom0.

3. Upgrade dom0 to R3.0:

    ```
    sudo qubes-dom0-update --releasever=3.0
    ```

    After this step, until you reboot the system, most of the qvm-* tools will not work.

4. If above step completed successfully you should have `qubes-core-dom0` at least 3.0.8. If not, repeat above step with additional `--clean` option.

5. Enable Xen services:

    ```      
    sudo systemctl enable xenconsoled.service xenstored.service
    ```

6. Reboot the system.
    
    It may happen that the system hang during the reboot. Hard reset the system in such case, all the filesystems are unmounted at this stage.

Please note that if you use Anti Evil Maid, then it won't be able to unseal the passphrase this time, because the Xen, kernel, and initramfs binaries have changed. Once the system boots up again, you could reseal your Anti Evil Maid's passphrase to the new configuration. Please consult Anti Evil Maid documentation for explanation on how to do that.

Now, when you have dom0 upgraded, you can install new templates from Qubes R3.0 repositories. Especially Fedora 21 - default Qubes R3.0 template:

```
sudo qubes-dom0-update qubes-template-fedora-21
```

## Upgrading template on already upgraded dom0

If for some reason you did not upgrade all the templates and standalone VMs before upgrading dom0, you can still do this, but it will be more complicated. This can be the case when you restore backup done on Qubes R2.

When you start R2 template/standalone VM on R3.0, there will be some limitations:

1. qrexec will not connect (you will see an error message during VM startup)
2. GUI will not connect - you will not see any VM window
3. VM will not be configured - especially it will not have network access

Because of above limitations, you will need to configure some of those manually. The instruction assumes the VM name is `custom-template`, but the same instructions can be applied to a standalone VM.

1. Check the VM network parameters, you will need them later:

    ```shell_session
    [user@dom0 ~]$ qvm-ls -n custom-template
    -------------------+----+--------+-------+------+-------------+-------+-------------+---------+-------------+
                  name | on |  state | updbl | type |       netvm | label |          ip | ip back | gateway/DNS |
    -------------------+----+--------+-------+------+-------------+-------+-------------+---------+-------------+
     [custom-template] |    | Halted |   Yes |  Tpl | *firewallvm | black | 10.137.1.53 |     n/a |  10.137.1.1 |
    ```

2. Start the VM from command line:

    ```shell_session
    [user@dom0 ~]$ qvm-start custom-template
    --> Loading the VM (type = TemplateVM)...
    --> Starting Qubes DB...
    --> Setting Qubes DB info for the VM...
    --> Updating firewall rules...
    --> Starting the VM...
    --> Starting the qrexec daemon...
    Waiting for VM's qrexec agent.............................................................Cannot connect to 'custom-template' qrexec agent for 60 seconds, giving up
    ERROR: Cannot execute qrexec-daemon!
    ```

    You can interrupt with Ctrl-C that qrexec waiting process.

3. Access VM console:

    ```
    [user@dom0 ~]$ virsh -c xen:/// console custom-template
    ```

4. Configure network according to parameters retrieved in first step:

    ```
    ip addr add 10.137.1.53/32 dev eth0
    ip route add 10.137.1.1/32 dev eth0
    ip route add via 10.137.1.1
    echo nameserver 10.137.1.1 > /etc/resolv.conf
    ```

5. Proceed with normal upgrade instruction described on this page.
