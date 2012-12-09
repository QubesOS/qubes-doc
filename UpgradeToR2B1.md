---
layout: wiki
title: UpgradeToR2B1
permalink: /wiki/UpgradeToR2B1/
---

Upgrading Qubes R1 to R2 (beta)
===============================

**Note: Qubes R2 Beta has not been release yet, DO NOT follow those instructions before R2 Beta is released**

Existing users of Qubes R1 (but not R1 betas!) can upgrade their systems to the latest R2 beta release by following the procedure below. As usual, it is advisable to backup the system before proceeding with the upgrade

Upgrade all Template and Standalone VM(s)
-----------------------------------------

By default, in Qubes R1, there is only one Template VM, however users are free to create more Template VMs for special purposes, as well as Standalone VMs. More information on using multiple Template VMs, as well as Standalone VMs, can be found [SoftwareUpdateVM here]. The steps described in this section should be repeated in *all* user's Template and Standalone VMs.

1.  Open terminal in the template VM (or standalone VM). E.g. use the Qubes Manager's right-click menu and choose Run Command in VM and type `gnome-terminal` there.
2.  Install `qubes-upgrade-vm` package (this package brings in R2 repo definitions and R2 keys)

    ``` {.wiki}
    sudo yum install qubes-upgrade-vm
    ```

3.  Proceed with normal update in the template (this should bring in also the R2 packages for the VMs):

    ``` {.wiki}
    sudo yum update
    ```

    The installer (yum) will prompt to accept the new Qubes R2 signing key:

    ``` {.wiki}
    Importing GPG key 0x0A40E458:
     Userid     : "Qubes OS Release 2 Signing Key"
     Fingerprint: 3f01 def4 9719 158e f862 66f8 0c73 b9d4 0a40 e458
     Package    : qubes-upgrade-vm-1.0-1.fc17.x86_64 (@qubes-vm-current)
     From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-upgrade-qubes-2-primary
    Is this ok [y/N]:
    ```

    If you see (as is the case on the "screenshot" above) that the new key was imported from a local filesystem (`/etc/pki/rpm-gpg/...`) you can safely accept the key, without checking its fingerprint. This is because there were only two ways for such a key to make it to your Template VM's filesystem:

-   via a legitimate RPM package previously installed (in our case it was the `qubes-upgrade-vm` RPM). Such an RPM must have been signed by one of the keys you decided to trust previously, by default this would be either via the Qubes R1 signing key, or Fedora 17 signing key.
-   via system compromise or via some illegal RPM package (e.g. Fedora released package pretending to bring new Firefox). In that case, however, your VM is already compromised, and it careful checking of the new R2 key would not change this situation to any better one. The game is lost for this VM anyway (and all VMs based on this template).

1.  Shut down the VM.

