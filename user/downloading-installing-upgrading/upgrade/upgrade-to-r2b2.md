---
lang: en
layout: doc
redirect_from:
- /doc/upgrade-to-r2b2/
- /en/doc/upgrade-to-r2b2/
- /doc/UpgradeToR2B2/
- /wiki/UpgradeToR2B2/
ref: 160
title: Upgrading to R2B2
---


Existing users of Qubes R1 (but not R1 betas!) can upgrade their systems to the latest R2 beta release by following the procedure below. As usual, it is advisable to backup the system before proceeding with the upgrade. While it is possible to upgrade the system **it is strongly recommended to reinstall it**. You will preserve all your data and settings thanks to [backup and restore tools](/doc/backup-restore/).

Upgrade all Template and Standalone VM(s)
-----------------------------------------

**If you have already R2 Beta1 installed, follow standard template update procedure (e.g. "Update VM" button in Qubes Manager) and skip the rest of this section**

By default, in Qubes R1, there is only one Template VM, however users are free to create more Template VMs for special purposes, as well as Standalone VMs. More information on using multiple Template VMs, as well as Standalone VMs, can be found [here](/doc/templates/) and [here](/doc/standalone-and-hvm/). The steps described in this section should be repeated in *all* user's Template and Standalone VMs.

1. Open terminal in the template VM (or standalone VM). E.g. use the Qubes Manager's right-click menu and choose Run Command in VM and type `gnome-terminal` there.
2. Install `qubes-upgrade-vm` package (this package brings in R2 repo definitions and R2 keys)

    ~~~
    sudo yum install qubes-upgrade-vm
    ~~~

3. Proceed with normal update in the template (this should bring in also the R2 packages for the VMs):

    ~~~
    sudo yum update
    ~~~

    The installer (yum) will prompt to accept the new Qubes R2 signing key:

    ~~~
    Importing GPG key 0x0A40E458:
     Userid     : "Qubes OS Release 2 Signing Key"
     Fingerprint: 3f01 def4 9719 158e f862 66f8 0c73 b9d4 0a40 e458
     Package    : qubes-upgrade-vm-1.0-1.fc17.x86_64 (@qubes-vm-current)
     From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-upgrade-qubes-2-primary
    Is this ok [y/N]:
    ~~~

    If you see (as is the case on the "screenshot" above) that the new key was imported from a local filesystem (`/etc/pki/rpm-gpg/...`) you can safely accept the key, without checking its fingerprint. This is because there were only two ways for such a key to make it to your Template VM's filesystem:

- via a legitimate RPM package previously installed (in our case it was the `qubes-upgrade-vm` RPM). Such an RPM must have been signed by one of the keys you decided to trust previously, by default this would be either via the Qubes R1 signing key, or Fedora 17 signing key.
- via system compromise or via some illegal RPM package (e.g. Fedora released package pretending to bring new Firefox). In that case, however, your VM is already compromised, and it careful checking of the new R2 key would not change this situation to any better one. The game is lost for this VM anyway (and all VMs based on this template).

1. Shut down the VM.

Installing new template
-----------------------

Qubes R2 Beta2 brings new fedora-18-x64 template (based on Fedora 18). You can install it from Qubes installation DVD. Insert installation DVD into your drive and issue following commands:

~~~
$ sudo -s
# mkdir -p /mnt/cdrom
# mount /dev/cdrom /mnt/cdrom # you can also use ISO image instead of /dev/cdrom; then add -o loop option
# yum install /mnt/cdrom/Packages/q/qubes-template-fedora-18-x64*rpm
# umount /mnt/cdrom
~~~

If you already have fedora-17-x64, you can also upgrade it to fedora-18-x64 following [standard Fedora upgrade procedure](https://fedoraproject.org/wiki/Upgrading_Fedora_using_yum) (only "yum" method will work in Qubes VM).

Upgrade Dom0
------------

Be sure to do steps described in this section after *all* your template and standalone VMs got updated as described in the section above.

1. Open terminal in Dom0. E.g. Start-\>System Settings-\>Konsole.
2. Upgrade the `qubes-release` package to the latest version which brings in new repo definitions and R2 signing keys:

    ~~~
    sudo qubes-dom0-update qubes-release
    ~~~

    This should install `qubes-release-1-6` in your Dom0.

3. Install R2 upgrade package:

    ~~~
    sudo qubes-dom0-update --releasever=1 qubes-dist-upgrade
    ~~~

4. Start upgrade process:

    ~~~
    sudo qubes-dist-upgrade
    ~~~

5. Follow instructions on screen, first stage of upgrade should end up with reboot request.
6. Reboot your system, ensure that you choose "Qubes Upgrade" boot option.
7. When system starts up, login and start start

    ~~~
    sudo qubes-dist-upgrade
    ~~~

    again. This will start second stage of upgrade, here most packages will be upgraded, so this will take a while.

8. You will be prompted to install new bootloader. If you haven't changed anything in this matter from initial installation, just accept the default.
9. Reboot your system. System shutdown may hung because some running system components no longer match that installed on disk; just wait a few minutes and hard reset the system in such case.
10. This is end of upgrade process, you should now have Qubes R2 system.

Please note that if you use Anti Evil Maid, then it won't be able to unseal the passphrase this time, because the Xen, kernel, and initramfs binaries have changed. Once the system boots up again, you could reseal your Anti Evil Maid's passphrase to the new configuration. Please consult Anti Evil Maid documentation for explanation on how to do that.
