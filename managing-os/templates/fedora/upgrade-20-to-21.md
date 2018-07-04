---
layout: doc
title: Upgrading the Fedora 20 Template to Fedora 21
permalink: /doc/template/fedora/upgrade-20-to-21/
redirect_from:
- /doc/fedora-template-upgrade-20/
- /en/doc/fedora-template-upgrade-20/
- /doc/FedoraTemplateUpgrade20/
- /wiki/FedoraTemplateUpgrade20/
---

Upgrading the Fedora 20 Template
================================

Summary: Upgrading the Standard Fedora 20 Template to Fedora 21
---------------------------------------------------------------

        [user@dom0 ~]$ qvm-clone fedora-20-x64 fedora-21
        [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-run -a fedora-21 gnome-terminal
        [user@dom0 ~]$ qvm-block -A fedora-21 dom0:/var/tmp/template-upgrade-cache.img
        [user@fedora-21 ~]$ sudo mkfs.ext4 /dev/xvdi
        [user@fedora-21 ~]$ sudo mount /dev/xvdi /mnt/removable
        [user@fedora-21 ~]$ sudo mkdir /mnt/removable/modules 
        [user@fedora-21 ~]$ sudo cp -rp /usr/lib/modules /mnt/removable/modules
        [user@fedora-21 ~]$ sudo mount --bind /mnt/removable/modules /usr/lib/modules
        [user@fedora-21 ~]$ sudo yum erase nautilus-actions libcacard
        [user@fedora-21 ~]$ sudo yum clean all
        [user@fedora-21 ~]$ sudo yum --releasever=21 --setopt=cachedir=/mnt/removable distro-sync
        [user@fedora-21 ~]$ sudo cp /usr/lib/qubes/init/ip* /etc/sysconfig/

    (Shut down TemplateVM via Qubes VM Manager; may need to be killed.)

        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-run -a fedora-21 gnome-terminal
        [user@fedora-21 ~]$ sudo yum -y update

    (Shut down TemplateVM by any normal means.)

        [user@dom0 ~]$ qvm-trim-template fedora-21

Detailed: Upgrading the Standard Fedora 20 Template to Fedora 21
----------------------------------------------------------------

These instructions will show you how to upgrade the standard Fedora 20
TemplateVM to Fedora 21. The same general procedure may be used to upgrade any
template based on the standard Fedora 20 template.

 1. Clone the existing template and start a terminal in the new template.

        [user@dom0 ~]$ qvm-clone fedora-20-x64 fedora-21
        [user@dom0 ~]$ qvm-run -a fedora-21 gnome-terminal

 2. Attempt the upgrade process in the new template.

        [user@fedora-21 ~]$ sudo yum erase nautilus-actions libcacard
        [user@fedora-21 ~]$ sudo yum clean all
        [user@fedora-21 ~]$ sudo yum --releasever=21 distro-sync
        [user@fedora-21 ~]$ sudo cp /usr/lib/qubes/init/ip* /etc/sysconfig/

    (Shut down TemplateVM via Qubes VM Manager; may need to be killed.)

    If you encounter no errors, proceed to step 7.

 3. If `yum` reports that you do not have enough free disk space to proceed with
    the upgrade process, create an empty file in dom0 to use as a cache and
    attach it to the template as a virtual disk.

        [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-block -A fedora-21 dom0:/var/tmp/template-upgrade-cache.img

    Then reattempt the upgrade process, but this time using the virtual disk as
    a cache.

        [user@fedora-21 ~]$ sudo mkfs.ext4 /dev/xvdi
        [user@fedora-21 ~]$ sudo mount /dev/xvdi /mnt/removable
        [user@fedora-21 ~]$ sudo yum erase nautilus-actions libcacard
        [user@fedora-21 ~]$ sudo yum clean all
        [user@fedora-21 ~]$ sudo yum --releasever=21 --setopt=cachedir=/mnt/removable distro-sync
        [user@fedora-21 ~]$ sudo cp /usr/lib/qubes/init/ip* /etc/sysconfig/

    (Poweroff via Qubes VM Manager. May need to be killed.)

 4. If `yum` complains that there is not enough free space in `/usr/lib/modules`,
    do this before reattempting the upgrade:

        [user@fedora-21 ~]$ sudo mkdir /mnt/removable/modules 
        [user@fedora-21 ~]$ sudo cp -rp /usr/lib/modules /mnt/removable/modules
        [user@fedora-21 ~]$ sudo mount --bind /mnt/removable/modules /usr/lib/modules

 5. `yum` may complain:

        At least X MB more space needed on the / filesystem.

    In this case, one option is to [resize the TemplateVM's disk
    image](/doc/ResizeDiskImage/) before reattempting the upgrade process. 
    (See **Additional Information** below for other options.)

 6. After the upgrade process is finished, remove the cache file, if you
    created one.

        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

 7. Ensure your new template is fully updated.

        [user@dom0 ~]$ qvm-run -a fedora-21 gnome-terminal
        [user@fedora-21 ~]$ sudo yum -y update 

 8. Trim the new template (see **Compacting the Upgraded Template** for details
    and other options).

        [user@dom0 ~]$ qvm-trim-template fedora-21

 9. (Optional) Remove the old default template.

        [user@dom0 ~]$ sudo yum remove qubes-template-fedora-20-x64


Summary: Upgrading the Minimal Fedora 20 Template to Fedora 21
--------------------------------------------------------------

        [user@dom0 ~]$ qvm-clone fedora-20-x64-minimal fedora-21-minimal
        [user@dom0 ~]$ qvm-run -a fedora-21-minimal xterm
        [user@fedora-21-minimal ~]$ su -
        [root@fedora-21-minimal ~]# yum clean all
        [user@fedora-21-minimal ~]# yum --releasever=21 distro-sync
        [user@fedora-21-minimal ~]# cp /usr/lib/qubes/init/ip* /etc/sysconfig/

    (Shut down the TemplateVM via Qubes VM Manager. May need to be killed.)

        [user@dom0 ~]$ qvm-run -a fedora-21-minimal xterm
        [user@fedora-21-minimal ~]$ su -
        [root@fedora-21-minimal ~]# yum -y update

    (Shut down TemplateVM by any normal means.)

        [user@dom0 ~]$ qvm-trim-template fedora-21-minimal

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
 2. `nautilus-actions` and `libcacard` are not installed by default, so do not
    try to erase them (unless you've installed them).
 3. `sudo` is not installed by default. Unless you've installed it, use `su` as
    demonstrated above. (Of course, you can also use `su` for the standard
    template, if you prefer.)


Compacting the Upgraded Template
--------------------------------

Neither `fstrim` nor the `discard` mount option works on the TemplateVM's root
filesystem, so when a file is removed in the template, space is not freed in
dom0. This means that the template will use about twice as much space as is
really necessary after upgrading.

If you have at least `qubes-core-dom0-2.1.68` installed and are on Qubes R2,
you can use the `qvm-trim-template` tool:

        [user@dom0 ~]$ qvm-trim-template fedora-21

If you do not have `qubes-core-dom0-2.1.68` or are on Qubes R3-rc1, you can
compact the `root.img` manually. To do this, you will need about 15GB (the
TemplateVM's max size + the actually used space there) free space in dom0.

 1. Start the template and fill all the free space with zeros, for example
    with:

        [user@fedora-21 ~]$ dd if=/dev/zero of=/var/tmp/zero

 2. Wait for the "No space left on device" error. Then:

        [user@fedora-21 ~]$ rm -f /var/tmp/zero

 3. Shut down the template and all VMs based on it. Then:

        [user@dom0 ~]$ cd /var/lib/qubes/vm-templates/fedora-21
        [user@dom0 ~]$ cp --sparse=always root.img root.img.new
        [user@dom0 ~]$ mv root.img.new root.img


Additional Information
----------------------

As mentioned above, you may encounter the following `yum` error:

    At least X MB more space needed on the / filesystem.

In this case, you have several options:

 1. [Increase the TemplateVM's disk image size](/doc/resize-disk-image/).
    This is the solution mentioned in the main instructions above.
 2. Delete files in order to free up space. One way to do this is by
    uninstalling packages. You may then reinstall them again after you
    finish the upgrade process, if desired). However, you may end up having to
    increase the disk image size anyway (see previous option).
 3. Increase the `root.img` size with `qvm-grow-root`. It should be easy to
    extend the `qvm-grow-root` tool in order to support PV (and not only HVM)
    VMs.  However, someone would need to do this (patches welcome).
 4. Do the upgrade in parts, e.g., by using package groups. (First upgrade
    `@core` packages, then the rest.)
 5. Do not perform an in-place upgrade. Instead, simply download and install a
    new template package, then redo all desired template modifications.

With regard to the last option, here are some useful messages from the mailing
list which also apply to TemplateVM management and migration in general:

 * [Marek](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/dS1jbLRP9n8J)
 * [Jason M](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/5PxDfI-RKAsJ)

Known issues with Fedora 21
---------------------------

* [The "Update VM" command in Qubes Manager does not work](https://github.com/QubesOS/qubes-issues/issues/982).
