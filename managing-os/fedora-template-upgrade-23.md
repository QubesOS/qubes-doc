---
layout: doc
title: Upgrading the Fedora 23 Template
permalink: /doc/fedora-template-upgrade-23/
redirect_from:
- /en/doc/fedora-template-upgrade-23/
- /doc/FedoraTemplateUpgrade23/
- /wiki/FedoraTemplateUpgrade23/
---

Upgrading the Fedora 23 Template
================================

Summary: Upgrading the Standard Fedora 23 Template to Fedora 24
---------------------------------------------------------------

        [user@dom0 ~]$ qvm-clone fedora-23 fedora-24
        [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-run -a fedora-24 gnome-terminal
        [user@dom0 ~]$ qvm-block -A fedora-24 dom0:/var/tmp/template-upgrade-cache.img
        [user@fedora-24 ~]$ sudo mkfs.ext4 /dev/xvdi
        [user@fedora-24 ~]$ sudo mount /dev/xvdi /mnt/removable
        [user@fedora-24 ~]$ sudo dnf clean all
        [user@fedora-24 ~]$ sudo dnf --releasever=24 --setopt=cachedir=/mnt/removable distro-sync

    (Shut down TemplateVM by any normal means.)

        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-trim-template fedora-24

    (Done.)

Detailed: Upgrading the Standard Fedora 23 Template to Fedora 24
----------------------------------------------------------------

These instructions will show you how to upgrade the standard Fedora 23
TemplateVM to Fedora 24. The same general procedure may be used to upgrade any
template based on the standard Fedora 23 template. 

 1. Ensure the existing template is not running. 

        [user@dom0 ~]$ qvm-shutdown fedora-23
 
 2. Clone the existing template and start a terminal in the new template.

        [user@dom0 ~]$ qvm-clone fedora-23 fedora-24
        [user@dom0 ~]$ qvm-run -a fedora-24 gnome-terminal

 2. Attempt the upgrade process in the new template.

        [user@fedora-24 ~]$ sudo dnf clean all
        [user@fedora-24 ~]$ sudo dnf --releasever=24 distro-sync

 3. Shutdown the new TemplateVM via dom0 command line or Qubes VM Manager;

        [user@dom0 ~]$ qvm-shutdown fedora-24
        
    If you encounter no errors, proceed to step 7.

 4. If `dnf` reports that you do not have enough free disk space to proceed with
    the upgrade process, create an empty file in dom0 to use as a cache and
    attach it to the template as a virtual disk.

        [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-block -A fedora-24 dom0:/var/tmp/template-upgrade-cache.img

    Then reattempt the upgrade process, but this time using the virtual disk as
    a cache.

        [user@fedora-24 ~]$ sudo mkfs.ext4 /dev/xvdi
        [user@fedora-24 ~]$ sudo mount /dev/xvdi /mnt/removable
        [user@fedora-24 ~]$ sudo dnf clean all
        [user@fedora-24 ~]$ sudo dnf --releasever=24 --setopt=cachedir=/mnt/removable distro-sync

    (Poweroff via Qubes VM Manager. May need to be killed.)

 5. `dnf` may complain:

        At least X MB more space needed on the / filesystem.

    In this case, one option is to [resize the TemplateVM's disk
    image](/doc/ResizeDiskImage/) before reattempting the upgrade process. 
    (See **Additional Information** below for other options.)

 6. After the upgrade process is finished, remove the cache file, if you
    created one.

        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

 7. Trim the new template (see **Compacting the Upgraded Template** for details
    and other options).

        [user@dom0 ~]$ qvm-trim-template fedora-24

 8. (Optional) Remove the old default template.

        [user@dom0 ~]$ sudo dnf remove qubes-template-fedora-23


Summary: Upgrading the Minimal Fedora 23 Template to Fedora 24
--------------------------------------------------------------

        [user@dom0 ~]$ qvm-clone fedora-23-minimal fedora-24-minimal
        [user@dom0 ~]$ qvm-run -a fedora-24-minimal xterm
        [user@fedora-24-minimal ~]$ su -
        [root@fedora-24-minimal ~]# dnf clean all
        [user@fedora-24-minimal ~]# dnf --releasever=24 distro-sync

    (Shut down TemplateVM by any normal means.)

        [user@dom0 ~]$ qvm-trim-template fedora-24-minimal

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
--------------------------------

Neither `fstrim` nor the `discard` mount option works on the TemplateVM's root
filesystem, so when a file is removed in the template, space is not freed in
dom0. This means that the template will use about twice as much space as is
really necessary after upgrading.

You can use the `qvm-trim-template` tool:

        [user@dom0 ~]$ qvm-trim-template fedora-24


Additional Information
----------------------

As mentioned above, you may encounter the following `dnf` error:

    At least X MB more space needed on the / filesystem.

In this case, you have several options:

 1. [Increase the TemplateVM's disk image size](/doc/resize-disk-image/).
    This is the solution mentioned in the main instructions above.
 2. Delete files in order to free up space. One way to do this is by
    uninstalling packages. You may then reinstalling them again after you
    finish the upgrade process, if desired). However, you may end up having to
    increase the disk image size anyway (see previous option).
 3. Increase the `root.img` size with `qvm-grow-root`.
 4. Do the upgrade in parts, e.g., by using package groups. (First upgrade
    `@core` packages, then the rest.)
 5. Do not perform an in-place upgrade. Instead, simply download and install a
    new template package, then redo all desired template modifications.

With regard to the last option, here are some useful messages from the mailing
list which also apply to TemplateVM management and migration in general:

 * [Marek](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/dS1jbLRP9n8J)
 * [Jason M](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/5PxDfI-RKAsJ)
