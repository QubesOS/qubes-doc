---
layout: doc
title: Upgrading the Fedora 21 Template
permalink: /doc/fedora-template-upgrade-21/
redirect_from:
- /en/doc/fedora-template-upgrade-21/
- /doc/FedoraTemplateUpgrade21/
- /wiki/FedoraTemplateUpgrade21/
---

Upgrading the Fedora 21 Template
================================

Summary: Upgrading the Standard Fedora 21 Template to Fedora 23
---------------------------------------------------------------

        [user@dom0 ~]$ qvm-clone fedora-21 fedora-23
        [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-run -a fedora-23 gnome-terminal
        [user@dom0 ~]$ qvm-block -A fedora-23 dom0:/var/tmp/template-upgrade-cache.img
        [user@fedora-23 ~]$ sudo mkfs.ext4 /dev/xvdi
        [user@fedora-23 ~]$ sudo mount /dev/xvdi /mnt/removable
        [user@fedora-23 ~]$ sudo mkdir /mnt/removable/modules 
        [user@fedora-23 ~]$ sudo cp -rp /usr/lib/modules /mnt/removable/modules
        [user@fedora-23 ~]$ sudo mount --bind /mnt/removable/modules /usr/lib/modules
        [user@fedora-23 ~]$ sudo yum clean all
        [user@fedora-23 ~]$ sudo yum --releasever=23 --enablerepo=qubes*current-testing --setopt=cachedir=/mnt/removable distro-sync

    (Shut down TemplateVM by any normal means.)

        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-trim-template fedora-23

    (Done.)

Detailed: Upgrading the Standard Fedora 21 Template to Fedora 23
----------------------------------------------------------------

These instructions will show you how to upgrade the standard Fedora 21
TemplateVM to Fedora 23. The same general procedure may be used to upgrade any
template based on the standard Fedora 21 template. 

 1. Ensure the existing template is not running. 

        [user@dom0 ~]$ qvm-shutdown fedora-21
 
 2. Clone the existing template and start a terminal in the new template.

        [user@dom0 ~]$ qvm-clone fedora-21 fedora-23
        [user@dom0 ~]$ qvm-run -a fedora-23 gnome-terminal

 2. Attempt the upgrade process in the new template. For now you need to enable testing repository to do that.

        [user@fedora-23 ~]$ sudo yum clean all
        [user@fedora-23 ~]$ sudo yum --releasever=23 --enablerepo=qubes*current-testing distro-sync

    (Shut down TemplateVM via Qubes VM Manager; may need to be killed.)

    If you encounter no errors, proceed to step 7.

 3. If `yum` reports that you do not have enough free disk space to proceed with
    the upgrade process, create an empty file in dom0 to use as a cache and
    attach it to the template as a virtual disk.

        [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-block -A fedora-23 dom0:/var/tmp/template-upgrade-cache.img

    Then reattempt the upgrade process, but this time using the virtual disk as
    a cache.

        [user@fedora-23 ~]$ sudo mkfs.ext4 /dev/xvdi
        [user@fedora-23 ~]$ sudo mount /dev/xvdi /mnt/removable
        [user@fedora-23 ~]$ sudo yum clean all
        [user@fedora-23 ~]$ sudo yum --releasever=23 --enablerepo=qubes*current-testing --setopt=cachedir=/mnt/removable distro-sync

    (Poweroff via Qubes VM Manager. May need to be killed.)

 4. If `yum` complains that there is not enough free space in `/usr/lib/modules`,
    do this before reattempting the upgrade:

        [user@fedora-23 ~]$ sudo mkdir /mnt/removable/modules 
        [user@fedora-23 ~]$ sudo cp -rp /usr/lib/modules /mnt/removable/modules
        [user@fedora-23 ~]$ sudo mount --bind /mnt/removable/modules /usr/lib/modules

 5. `yum` may complain:

        At least X MB more space needed on the / filesystem.

    In this case, one option is to [resize the TemplateVM's disk
    image](/doc/ResizeDiskImage/) before reattempting the upgrade process. 
    (See **Additional Information** below for other options.)

 6. After the upgrade process is finished, remove the cache file, if you
    created one.

        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

 7. Trim the new template (see **Compacting the Upgraded Template** for details
    and other options).

        [user@dom0 ~]$ qvm-trim-template fedora-23

 8. (Optional) Remove the old default template.

        [user@dom0 ~]$ sudo yum remove qubes-template-fedora-21


Summary: Upgrading the Minimal Fedora 21 Template to Fedora 23
--------------------------------------------------------------

        [user@dom0 ~]$ qvm-clone fedora-21-minimal fedora-23-minimal
        [user@dom0 ~]$ qvm-run -a fedora-23-minimal xterm
        [user@fedora-23-minimal ~]$ su -
        [root@fedora-23-minimal ~]# yum clean all
        [user@fedora-23-minimal ~]# yum --releasever=23 --enablerepo=qubes*current-testing distro-sync

    (Shut down TemplateVM by any normal means.)

        [user@dom0 ~]$ qvm-trim-template fedora-23-minimal

(If you encounter insufficient space issues, you may need to use the methods
described for the standard template above.)


Differences Between the Standard and Minimal Upgrade Procedures
---------------------------------------------------------------

The procedure for upgrading the minimal template (or any template based on the
minimal template) is the same as the procedure for the standard template above,
**with the following exceptions**:

 1. `gnome-terminal` is not installed by default. Unless you've installed it
    (or another terminal emulator), use `xterm`. (Of course, you can also use
    `xterm` for the standard template, if you prefer.)
 2. `sudo` is not installed by default. Unless you've installed it, use `su` as
    demonstrated above. (Of course, you can also use `su` for the standard
    template, if you prefer.)


Compacting the Upgraded Template
================================

Neither `fstrim` nor the `discard` mount option works on the TemplateVM's root
filesystem, so when a file is removed in the template, space is not freed in
dom0. This means that the template will use about twice as much space as is
really necessary after upgrading.

If you have at least `qubes-core-dom0-2.1.68` installed or are on Qubes R3.0,
you can use the `qvm-trim-template` tool:

        [user@dom0 ~]$ qvm-trim-template fedora-23

If you do not have `qubes-core-dom0-2.1.68` or are on older Qubes version, you can
compact the `root.img` manually. To do this, you will need about 15GB (the
TemplateVM's max size + the actually used space there) free space in dom0.

 1. Start the template and fill all the free space with zeros, for example
    with:

        [user@fedora-23 ~]$ dd if=/dev/zero of=/var/tmp/zero

 2. Wait for the "No space left on device" error. Then:

        [user@fedora-23 ~]$ rm -f /var/tmp/zero

 3. Shut down the template and all VMs based on it. Then:

        [user@dom0 ~]$ cd /var/lib/qubes/vm-templates/fedora-23
        [user@dom0 ~]$ cp --sparse=always root.img root.img.new
        [user@dom0 ~]$ mv root.img.new root.img


Additional Information
======================

As mentioned above, you may encounter the following `yum` error:

    At least X MB more space needed on the / filesystem.

In this case, you have several options:

 1. [Increase the TemplateVM's disk image size](/doc/resize-disk-image/).
    This is the solution mentioned in the main instructions above.
 2. Delete files in order to free up space. One way to do this is by
    uninstalling packages. You may then reinstalling them again after you
    finish the upgrade process, if desired). However, you may end up having to
    increase the disk image size anyway (see previous option).
 3. Increase the `root.img` size with `qvm-grow-root`. It should be easy to
    extend the `qvm-grow-root` tool in order to support PV (and not only HVM)
    VMs. This is already done in R3.1.
 4. Do the upgrade in parts, e.g., by using package groups. (First upgrade
    `@core` packages, then the rest.)
 5. Do not perform an in-place upgrade. Instead, simply download and install a
    new template package, then redo all desired template modifications.

With regard to the last option, here are some useful messages from the mailing
list which also apply to TemplateVM management and migration in general:

 * [Marek](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/dS1jbLRP9n8J)
 * [Jason M](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/5PxDfI-RKAsJ)

Upgrading to Fedora 22
======================

You may choose to upgrade to Fedora 22 instead of Fedora 23. In that case,
simply replace version "23" with "22" in all above commands.

Known issues with Fedora 23
===========================

* [Graphical update tools (using PackageKit) does not work](https://github.com/QubesOS/qubes-issues/issues/982).
* [Dnf (new Fedora package manager) needs a lot of time to process repository metadata](https://bugzilla.redhat.com/show_bug.cgi?id=1227014), you may want to use `yum-deprecated` for now
* ["Terminal" shortcuts do not work because the desktop file in the VM has been renamed](https://github.com/QubesOS/qubes-issues/issues/1428). See the issue report for how to update your configuration to match.
