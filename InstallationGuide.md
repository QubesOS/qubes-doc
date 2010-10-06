---
layout: wiki
title: InstallationGuide
permalink: /wiki/InstallationGuide/
---

Installation Guide (for Release 1 Alpha 3)
==========================================

**We're currently upgrading the repo for Qubes Alpha 3 -- please refrain from installing for a while**

**NOTE:** You can only install Qubes on a **64-bit** CPU! (most recent laptops have 64-bit CPUs)

**NOTE:** Do not try to install Qubes in a VM, e.g. VMWare. Qubes has its own bare-metal hypervisor, and, as the name suggests, it should be installed on a bare-metal, not in some VM. Even if you somehow succeed installing it inside some other VMM system, you will likely get horrible performance and perhaps even some strange crashes, caused by the outer VMM, that is obviously not prepared for running a nested hypervisor in its VMs.

At this stage we don't have a standalone automatic installer, so the installation process is currently a bit complicated and requires some knowledge of Linux. The installation consists of a few stages that are described in detail below...

I. Installing Fedora 13 Linux
-----------------------------

**NOTE:** If you're migrating from **Qubes Alpha 1**, and want to preserve your AppVMs (specifically your data), you should use ```qvm-backup``` tool to make a backup (Qubes Alpha 2 will let you automatically restore it later).

**NOTE:** Do not try to install Qubes Alpha 3 on top of an already installed **Qubes Alpha 1** -- you should reinstall everything from scratch!

**NOTE:** If you're migrating from **Qubes Alpha 2**, however, then ```yum update``` executed in Dom0 konsole should do the work, and you could skip this guide.

First we need to install a minimal Linux distribution that would later become our Dom0 system. We strongly recommend choosing a **64-bit Fedora 13 distribution**.

1.  Download the 64-bit version of Fedora 13 installation DVD ISO:

[​http://fedoraproject.org/en/get-fedora-all](http://fedoraproject.org/en/get-fedora-all)

...and burn it on a DVD. Proceed with the default installation...

1.  When asked about type of installation, choose

**Graphical Workstation** (this is selected by default), and choose **Customize now**...

1.  ...in the next screen choose only the following groups of packages:

(i.e. uncheck all the other groups)

-   Desktop Environments/KDE
-   Applications/Editors
-   Base System/Base
-   Base System/Fonts
-   Base System/Hardware Support
-   Base System/X Window System

You really won't need anything more in Dom0 (even this is too much).

Note: This might look unnecessary that we install Fedora KDE packages now, only to remove them in one of the next steps and install Qubes KDE packages instead. However, most users will find it easier to proceed this way.

Complete the installation, reboot, verify you have X Window System working, complete the post-installation setup in which you create an unprivileged user account, that will be used for logging into the X system.

If you can't get your X Window System working at this time, it means you have have a graphics card not supported by a mainstream Linux distribution. This really should happen only in case of some very exotic hardware (or very new). In any case, this is nothing Qubes or Xen, related, so please do not ask about the solution on Qubes or Xen mailing lists.

II. Configuring Qubes repository and Key verification
-----------------------------------------------------

1.  Login into KDE, start a *konsole*, and change to root:

    ``` {.wiki}
    su -
    ```

1.  Download the Qubes Master and "Release 1" signing keys:

    ``` {.wiki}
    wget http://qubes-os.org/keys/qubes-master-signing-key.asc
    wget http://qubes-os.org/keys/qubes-release-1-signing-key.asc
    ```

[Verify the keys](/wiki/VerifyingSignatures) and then install the key in the rpm database:

``` {.wiki}
rpm --import qubes-release-1-signing-key.asc
```

1.  Configure Qubes repository:

    ``` {.wiki}
    wget http://qubes-os.org/yum/qubes-r1-dom0.repo
    mv qubes-r1-dom0.repo /etc/yum.repos.d/
    ```

III. Installing Qubes KDE packages for Dom0
-------------------------------------------

1.  First remove all the Fedora KDE packages:

    ``` {.wiki}
    yum remove 'kde*'
    ```

1.  Now, install the Qubes-customized KDE packages:

    ``` {.wiki}
    yum install qubes-kde-dom0
    yum install knetworkmanager
    ```

The last package (*knetworkmanager*) is needed only if one intends to use networking in Dom0, rather than in NetVM. However, as we're currently having problems with the NetVM working with our new Dom0 kernel in Alpha 2, we have decided to temporary withhold the release of a new NetVM package for Alpha 2, and so you must currently use networking in Dom0, and it's recommended to install this package. Rest assured, we will be working on getting NetVM back in the next version.

1.  Via the KDE "Start Menu", go to: Computer/System Settings/Appearance/Windows, and then choose **Plastik for Qubes** Window decoration plugin.

1.  You might also want to install the ```kdebase-workspace-wallpapers``` package to get some nice wallpapers :)

1.  **Reboot**

IV. Installing Xen and Dom0 kernel
----------------------------------

1.  Install Xen and Dom0 kernel:

``` {.wiki}
yum install kernel-qubes-dom0
```

1.  Reboot and verify that the X Window System still works fine.

If you can't get your X Window System working at this time, it suggests your graphics card driver is incompatible with Xen, which is a polite way of saying that the driver is most likely broken, as any decently written driver should be Xen compatible (when used in Dom0). The Xen mailing list might be a proper place to report the problem, but we would also be interested in learning about ~~broken~~ Xen-incompatible cards, so please also copy your report to the Qubes mailing list.

V. Installing Qubes
-------------------

1.  Install the Qubes Dom0 packages:

    ``` {.wiki}
    yum install qubes-core-dom0 qubes-gui-dom0
    yum install qubes-manager
    ```

1.  Add the user account you use to log into the system to the 'qubes' group:

    ``` {.wiki}
    usermod -a -G qubes <username>
    ```

1.  Set default NetVM (for now we will use dom0):

    ``` {.wiki}
    qvm-set-default-netvm dom0
    ```

1.  Reboot your system.

VI. Installing Qubes AppVM Template
-----------------------------------

1.  Now you can install a template image, which will be used for creating all

your AppVMs, and netvm image, used to isolate all your networking in an unprivileged VM

``` {.wiki}
yum install qubes-template-linux-x64
```

This will probably take some time...

1.  Now, lets create some AppVMs to see if this all works...

**NOTE:** If you're migrating from a previous system (e.g. Alpha 1), and want to restore your previous AppVMs from a backup, use the [qvm-backup-restore](/wiki/BackupRestore) tool.

NOTE: you should now work as **normal user**, i.e. the same you use for logging into your X system, and the same you added to the qubes 'group' in the previous step, or you will not be able to star this VM as a normal user!

NOTE: You can also use the graphical Qubes Manager to create/remove AppVMs -- just click on the Qubes Manager icon in the tray!

``` {.wiki}
qvm-create personal --label yellow
qvm-create work --label green
qvm-create shopping --label orange
qvm-create bank --label green
qvm-create random --label red
```

You can verify if new AppVMs have indeed been created by using qvm-ls:

``` {.wiki}
qvm-ls
```

... and you can remove them using qvm-remove (be careful not to remove your data accidentally!).

There are much more `qvm-*` tools in the `/usr/bin` -- most of them should be self-explanatory.

1.  Wait a few seconds and see if icons have been created and added to the

"Start" menu in your Dom0 Window Manager.

Try running some applications, e.g. Firefox from the random machine. When you run an application for the first time, and the corresponding AppVM has not yet been started, it might take some time (15-30 seconds) for it to start. Subsequent apps from the same AppVM will be starting much faster.

VII. Switching to NetVM
-----------------------

1.  First shut down all the VMs in the system, e.g.:

    ``` {.wiki}
    qvm-run --all --wait -uroot poweroff
    ```

1.  Now as a root user do:

    ``` {.wiki}
    /etc/init.d/qubes_netvm stop
    qvm-set-default-netvm netvm
    /etc/init.d/qubes_netvm start
    ```

1.  Add `iommu=pv` option to Xen boot argument by editing the `/boot/grub/grub.conf` file. Reboot.

1.  Verify that Xen uses IOMMU/VT-d indeed by looking into `xm dmesg` output

NOTE: Xen can use IOMMU/VT-d only if you have hardware with IOMMU/VT-d support and a non-broken BIOS that also supports VT-d (specifically BIOS should expose a correct ACPI DMAR table)

Read more about Qubes networking [here](/wiki/QubesNet).

VIII. Known Issues and Workarounds for Qubes Alpha 3
----------------------------------------------------

1.  If you use full disk encryption via LUKS (default if you chose "Encrypt disk" in Fedora installer), and if you have a Core i5/i7 processor that supports the new AESNI instruction, you should pass the following argument to your kernel (by editing your ```/boot/grub/grub.conf``` file):

    ``` {.wiki}
    rdblacklist=aesni-intel
    ```

This should be appended the ```kernel``` line in ```grub.conf```. This will disable use of kernel module with AESNI support, which apparently is buggy.

1.  If you have Nvidia graphics card, be sure to update your ```xorg-x11-drv-nouveau```, at least to version 0.0.16-7.20100423, otherwise you might have problems with the suspend/resume operation:

    ``` {.wiki}
    yum update 'xorg-*'
    ```

1.  If you have Nvidia graphics card, you can experience strange icon distortions after resume from suspend. Hopefully some new xorg driver will resolve this issue.

1.  If you have Intel HD graphics card on Core i5/i7 processor, do **not** enable desktop effects right after installation (or at least do not choose OpenGL engine). There is a known problem with those cards drivers that causes the original X shipped with F13 to crash every few minutes, when OpenGL is used. This happens on standard Fedora installation, even without Xen and without Qubes. This problem vanishes when one upgrades to xorg-x11-server 1.8.2, OpenGL and composition works flawlessy then.

