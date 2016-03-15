---
layout: doc
title: Upgrading to R2B1
permalink: /doc/upgrade-to-r2b1/
redirect_from:
- /en/doc/upgrade-to-r2b1/
- /doc/UpgradeToR2B1/
- /wiki/UpgradeToR2B1/
---

Upgrading Qubes R1 to R2 Beta 1
===============================

**Note: Qubes R2 Beta 1 is no longer supported! Please install or upgrade to a newer Qubes R2.**

**Note: This page is kept for historical reasons only! Do not follow the instructions below'''**

Existing users of Qubes R1 (but not R1 betas!) can upgrade their systems to the latest R2 beta release by following the procedure below. As usual, it is advisable to backup the system before proceeding with the upgrade

Upgrade all Template and Standalone VM(s)
-----------------------------------------

By default, in Qubes R1, there is only one Template VM, however users are free to create more Template VMs for special purposes, as well as Standalone VMs. More information on using multiple Template VMs, as well as Standalone VMs, can be found [SoftwareUpdateVM here]. The steps described in this section should be repeated in *all* user's Template and Standalone VMs.

1.  Open terminal in the template VM (or standalone VM). E.g. use the Qubes Manager's right-click menu and choose Run Command in VM and type `gnome-terminal` there.
2.  Install `qubes-upgrade-vm` package (this package brings in R2 repo definitions and R2 keys)

    ~~~
    sudo yum install qubes-upgrade-vm
    ~~~

3.  Proceed with normal update in the template (this should bring in also the R2 packages for the VMs):

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

-   via a legitimate RPM package previously installed (in our case it was the `qubes-upgrade-vm` RPM). Such an RPM must have been signed by one of the keys you decided to trust previously, by default this would be either via the Qubes R1 signing key, or Fedora 17 signing key.
-   via system compromise or via some illegal RPM package (e.g. Fedora released package pretending to bring new Firefox). In that case, however, your VM is already compromised, and it careful checking of the new R2 key would not change this situation to any better one. The game is lost for this VM anyway (and all VMs based on this template).

1.  Shut down the VM.

Upgrade Dom0
------------

Be sure to do steps described in this section after *all* your template and standalone VMs got updated as described in the section above.

1.  Open terminal in Dom0. E.g. Start-\>System Settings-\>Konsole.
2.  Upgrade the `qubes-release` package to the latest version which brings in new repo definitions and R2 signing keys:

    ~~~
    sudo qubes-dom0-update qubes-release
    ~~~

    This should install `qubes-release-1-6` in your Dom0.

3.  Install R2 packages:

    ~~~
    sudo qubes-dom0-update --releasever=2
    ~~~

4.  Reboot your system. Please note that if you use Anti Evil Maid, then it won't be able to unseal the passphrase this time, because the Xen, kernel, and initramfs binaries have changed. Once the system boots up again, you could reseal your Anti Evil Maid's passphrase to the new configuration. Please consult Anti Evil Maid documentation for explanation on how to do that.

