---
layout: doc
title: Upgrading the Fedora 29 TemplateVM to Fedora 30
permalink: /doc/template/fedora/upgrade-29-to-30/
---

Upgrading the Fedora 29 TemplateVM to Fedora 30
===============================================

This page provides instructions for performing an in-place upgrade of an installed Fedora 29 [TemplateVM] to Fedora 30.
If you wish to install a new, unmodified Fedora 30 template instead of upgrading a template that is already installed in your system, please see the [Fedora TemplateVM] page instead.


Important information regarding RPM Fusion repos
------------------------------------------------

If your RPM Fusion repositories are **disabled** when you upgrade a TemplateVM from Fedora 29 to 30, all RPM Fusion packages and RPM Fusion repo definitions will be removed from that TemplateVM.
If your RPM Fusion repositories are **enabled** when upgrading, all RPM Fusion packages and repo definitions will be retained and updated as expected.
For most users, this behavior should not cause a problem, since a TemplateVM in which the RPM Fusion repos are disabled is probably a TemplateVM in which you never wish to use them.
However, if you wish to have the RPM Fusion repo definitions after upgrading in a TemplateVM in which they are currently disabled, you may wish to temporarily enable them prior to upgrading or manually create, copy, or download them after upgrading.


Summary Instructions for Standard Fedora TemplateVMs
----------------------------------------------------

**Note:** The prompt on each line indicates where each command should be entered (`@dom0` or `@fedora-30`).

    [user@dom0 ~]$ qvm-clone fedora-29 fedora-30
    [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
    [user@dom0 ~]$ qvm-run -a fedora-30 gnome-terminal
    [user@dom0 ~]$ dev=$(sudo losetup -f --show /var/tmp/template-upgrade-cache.img)
    [user@dom0 ~]$ qvm-block attach fedora-30 dom0:${dev##*/}
    [user@fedora-30 ~]$ sudo mkfs.ext4 /dev/xvdi
    [user@fedora-30 ~]$ sudo mount /dev/xvdi /mnt/removable
    [user@fedora-30 ~]$ sudo dnf clean all
    [user@fedora-30 ~]$ sudo dnf --releasever=30 --setopt=cachedir=/mnt/removable --best --allowerasing distro-sync
    [user@fedora-30 ~]$ sudo fstrim -v /

    (Shut down TemplateVM by any normal means.)

    [user@dom0 ~]$ sudo losetup -d $dev
    [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

(Optional cleanup: Switch everything over to the new template and delete the old one.
See instructions below for details.)


Detailed Instructions for Standard Fedora TemplateVMs
-----------------------------------------------------

These instructions will show you how to upgrade the standard Fedora 29 TemplateVM to Fedora 30.
The same general procedure may be used to upgrade any template based on the standard Fedora 29 template.

**Note:** The command-line prompt on each line indicates where each command should be entered (`@dom0` or `@fedora-30`).

 1. Ensure the existing template is not running.

        [user@dom0 ~]$ qvm-shutdown fedora-29

 2. Clone the existing template and start a terminal in the new template.

        [user@dom0 ~]$ qvm-clone fedora-29 fedora-30
        [user@dom0 ~]$ qvm-run -a fedora-30 gnome-terminal

 3. Attempt the upgrade process in the new template.

        [user@fedora-30 ~]$ sudo dnf clean all
        [user@fedora-30 ~]$ sudo dnf --releasever=30 distro-sync --best --allowerasing

    **Note:** `dnf` might ask you to approve importing a new package signing key.
    For example, you might see a prompt like this one:

        warning: /mnt/removable/updates-0b4cc238d1aa4ffe/packages/example-package.fc30.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID cfc659b9: NOKEY
        Importing GPG key 0xCFC659B9:
         Userid     : "Fedora 30 (30) <fedora-30@fedoraproject.org>"
         Fingerprint: F1D8 EC98 F241 AAF2 0DF6  9420 EF3C 111F CFC6 59B9
         From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-30-x86_64
        Is this ok [y/N]: y

    This key was already checked when it was installed (notice that the "From" line refers to a location on your local disk), so you can safely say yes to this prompt.

    **Note:** If you encounter no errors, proceed to step 4.
    If you do encounter errors, see the next two points first.

     * If `dnf` reports that you do not have enough free disk space to proceed
       with the upgrade process, create an empty file in dom0 to use as a cache
       and attach it to the template as a virtual disk.

           [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
           [user@dom0 ~]$ dev=$(sudo losetup -f --show /var/tmp/template-upgrade-cache.img)
           [user@dom0 ~]$ qvm-block attach fedora-30 dom0:${dev##*/}

       Then reattempt the upgrade process, but this time use the virtual disk as a cache.

           [user@fedora-30 ~]$ sudo mkfs.ext4 /dev/xvdi
           [user@fedora-30 ~]$ sudo mount /dev/xvdi /mnt/removable
           [user@fedora-30 ~]$ sudo dnf clean all
           [user@fedora-30 ~]$ sudo dnf --releasever=30 --setopt=cachedir=/mnt/removable --best --allowerasing distro-sync

       If this attempt is successful, proceed to step 4.

     * `dnf` may complain:

           At least X MB more space needed on the / filesystem.

       In this case, one option is to [resize the TemplateVM's disk image][resize-disk-image] before reattempting the upgrade process.
       (See [Additional Information] below for other options.)

 4. Check that you are on the correct (new) fedora release.
 
        [user@fedora-30 ~]$ cat /etc/fedora-release

 5. Trim the new template.

        [user@fedora-30 ~]$ sudo fstrim -v /

 6. Shut down the new TemplateVM (from the command line or the Qube Manager).

        [user@dom0 ~]$ qvm-shutdown fedora-30

 7. Remove the cache file, if you created one.

        [user@dom0 ~]$ sudo losetup -d $dev
        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

 8. (Recommended) [Switch everything that was set to the old template to the new template.][switching]

 9. (Optional) Remove the old template. (Make sure to type `fedora-29`, not `fedora-30`.)

        [user@dom0 ~]$ sudo dnf remove qubes-template-fedora-29


Summary Instructions for Fedora Minimal TemplateVMs
---------------------------------------------------

**Note:** The prompt on each line indicates where each command should be entered (`@dom0` or `@fedora-30`).

    [user@dom0 ~]$ qvm-clone fedora-29-minimal fedora-30-minimal
    [user@dom0 ~]$ qvm-run -u root -a fedora-30-minimal xterm
    [root@fedora-30-minimal ~]# dnf clean all
    [user@fedora-30-minimal ~]# dnf --releasever=30 --best --allowerasing distro-sync
    [user@fedora-30-minimal ~]# fstrim -v /

    (Shut down TemplateVM by any normal means.)

(If you encounter insufficient space issues, you may need to use the methods described for the standard template above.)


Upgrading StandaloneVMs
-----------------------

The procedure for upgrading a StandaloneVM from Fedora 29 to Fedora 30 is the same as for a TemplateVM.


Additional Information
----------------------

As mentioned above, you may encounter the following `dnf` error:

    At least X MB more space needed on the / filesystem.

In this case, you have several options:

 1. [Increase the TemplateVM's disk image size][resize-disk-image].
    This is the solution mentioned in the main instructions above.
 2. Delete files in order to free up space. One way to do this is by uninstalling packages.
    You may then reinstall them again after you finish the upgrade process, if desired).
    However, you may end up having to increase the disk image size anyway (see previous option).
 3. Do the upgrade in parts, e.g., by using package groups.
    (First upgrade `@core` packages, then the rest.)
 4. Do not perform an in-place upgrade.
    Instead, simply download and install a new template package, then redo all desired template modifications.
    Here are some useful messages from the mailing list that also apply to TemplateVM management and migration in general from
    [Marek](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/dS1jbLRP9n8J) and
    [Jason M](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/5PxDfI-RKAsJ).


[TemplateVM]: /doc/templates/
[Fedora TemplateVM]: /doc/templates/fedora/
[resize-disk-image]: /doc/resize-disk-image/
[Additional Information]: #additional-information
[Compacting the Upgraded Template]: #compacting-the-upgraded-template
[switching]: /doc/templates/#how-to-switch-templates
[DispVM]: /doc/dispvm/

