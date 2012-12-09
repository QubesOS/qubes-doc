---
layout: wiki
title: UpgradeToR2B1
permalink: /wiki/UpgradeToR2B1/
---

Upgrading Qubes R1 to R2 (beta)
===============================

**Note: Qubes R2 Beta has not been release yet, DO NOT follow those instructions before R2 Beta is released**

Existing users of Qubes R1 (but not R1 betas!) can upgrade their systems to the latest R2 beta release by following the procedure below. As usual, tt is advisable to backup the system before proceeding with the upgrade

Upgrade all Template and Standalone VM(s)
-----------------------------------------

By default, in Qubes R1, there is only one Template VM, however users are free to create more Template VMs for special purposes, as well as Standalone VMs. More information on using multiple Template VMs, as well as Standalone VMs, can be found [SoftwareUpdateVM here]. The steps described in this section should be repeated in *all* user's Template and Standalone VMs.

1.  Open terminal in the template VM (or standalone VM). E.g. use the Qubes Manager's right-click menu and choose Run Command in VM and type **gnome-terminal** there.
2.  Install **qubes-upgrade-vm** package (this package brings in R2 repo definitions and R2 keys)

    ``` {.wiki}
    sudo yum install qubes-upgrade-vm
    ```

3.  Proceed with normal update in the template (this should bring in also the R2 packages for the VMs):

    ``` {.wiki}
    sudo yum update
    ```

4.  Shut down the VM.

