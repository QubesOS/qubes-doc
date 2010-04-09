---
layout: wiki
title: InstallationGuide
permalink: /wiki/InstallationGuide/
---

Installation Guide (for Release 1 Alpha 1)
==========================================

At this stage we don't have a standalone automatic installer, so the installation process is currently a bit complicated and requires some knowledge of Linux. The installation consists of a few stages that are described in detail below...

I. Installing Fedora 12 Linux
-----------------------------

First we need to install a minimal Linux distribution that would later become our Dom0 system. We strongly recommend choosing a 64-bit Fedora 12 distribution.

1.  Download the 64-bit version of Fedora 12 installation DVD ISO:

[​http://fedoraproject.org/en/get-fedora-all](http://fedoraproject.org/en/get-fedora-all)

...and burn it on a DVD. Proceed with the default installation...

While it is not absolutely necessary, you might want to enable the Fedora 12 'Updates' repository during the installation to have the updated versions of the packages installed. This requires a network connection (wired, not wireless) during the installation, of course.

1.  When asked about packages to install, choose

none, and choose "Customize now"...

[![](http://www.qubes-os.org/files/screenshots/release-1-alpha-1/installation-software-selection.png "http://www.qubes-os.org/files/screenshots/release-1-alpha-1/installation-software-selection.png")](http://www.qubes-os.org/files/screenshots/release-1-alpha-1/installation-software-selection.png)

1.  ...in the next screen choose only the following groups of packages:

(i.e. uncheck all the other groups)

-   Desktop Environments/KDE
-   Applications/Editors
-   Base System/Base
-   Base System/Fonts
-   Base System/Hardware Support
-   Base System/X Window System

You really won't need anything more in Dom0 (even this is too much).

Complete the installation, reboot, verify you have X Window System working, complete the post-installation setup in which you create an unprivileged user account, that will be used for logging into the X system.

If you can't get your X Window System working at this time, it means you have have a graphics card not supported by a mainstream Linux distribution. This really should happen only in case of some very exotic hardware. In any case, this is nothing Qubes or Xen, related, so please do not ask about the solution on Qubes or Xen mailing lists.

II. Installing Xen
------------------

1.  Change to root:

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
rpm --import qubes-release-signing-key.asc
```

1.  Configure Qubes repository:

    ``` {.wiki}
    wget http://qubes-os.org/yum/qubes.repo
    mv qubes.repo /etc/yum.repos.d/
    ```

1.  Install Xen and Dom0 kernel using the Qubes repository (Fedora 12 doesn't

have support for Xen Dom0 kernel, and the Xen it provides is too old for the Dom0 kernel that Qubes uses, that's why we install Xen and Dom0 kernel from Qubes repository):

``` {.wiki}
yum install kernel-qubes-dom0
```

1.  Reboot (but first read this whole paragraph) and verify that the X Window

System still works fine.

NOTE: Before rebooting you might consider changing the `timeout=` line in your `/boot/grub.conf` file to something like `3` to give you some time to choose a filesafe boot in GRUB menu in case your normal boot would not work.

If you can't get your X Window System working at this time, it suggests your graphics card driver is incompatible with Xen, which is a polite way of saying that the driver is most likely broken, as any decently written driver should be Xen compatible (when used in Dom0). The Xen mailing list might be a proper place to report the problem, but we would also be interested in learning about ~~broken~~ Xen-incompatible cards, so please also copy your report to the Qubes mailing list.

NOTE:

-   If you have an NVidia graphics card, read the [NVidia Troubleshooting Guide](/wiki/NvidiaTroubleshooting)
-   If you have ATI/Radeon you might want to check this [​thread](http://groups.google.com/group/qubes-devel/browse_thread/thread/d63f673d6286387e#) at qubes-devel.

III. Installing Qubes
---------------------

1.  Install the Qubes Dom0 packages:

    ``` {.wiki}
    yum install qubes-core-dom0 qubes-gui-dom0 qubes-dom0-cleanup
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

IV. Installing Qubes Virtual Machine Templates
----------------------------------------------

1.  Now you can install a template image, which will be used for creating all

your AppVMs, and netvm image, used to isolate all your networking in an unprivileged VM

``` {.wiki}
yum install qubes-template-linux-x64 qubes-servicevm-netvm
```

This will probably take some time...

1.  Now, lets create some AppVMs to see if this all works...

NOTE: you should now work as normal user, i.e. the same you use for logging into your X system, and the same you added to the qubes 'group' in the previous step, or you will not be able to star this VM as a normal user!

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

3) Wait a few seconds and see if icons have been created and added to the "Start" menu in your Dom0 Window Manager.

Try running some applications, e.g. Firefox from the random machine. When you run an application for the first time, and the corresponding AppVM has not yet been started, it might take some time (15-30 seconds) for it to start. Subsequent apps from the same AppVM will be starting much faster.

V. Switching to NetVM
---------------------

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

1.  Add `iommu=pv` option to Xen boot argument by editing the `/boot/grub.conf` file. Reboot.

1.  Verify that Xen uses IOMMU/VT-d indeed by looking into `xm dmesg` output

NOTE: Xen can use IOMMU/VT-d only if you have hardware with IOMMU/VT-d support and a non-broken BIOS that also supports VT-d (specifically BIOS should expose a correct ACPI DMAR table)
