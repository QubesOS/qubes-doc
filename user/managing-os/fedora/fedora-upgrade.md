---
layout: doc
title: Upgrading Fedora TemplateVMs
permalink: /doc/template/fedora/upgrade/
redirect_from:
- /doc/template/fedora/upgrade-26-to-27/
- /doc/fedora-template-upgrade-26/
- /en/doc/fedora-template-upgrade-26/
- /doc/FedoraTemplateUpgrade26/
- /wiki/FedoraTemplateUpgrade26/
- /doc/template/fedora/upgrade-27-to-28/
- /doc/fedora-template-upgrade-27/
- /en/doc/fedora-template-upgrade-27/
- /doc/FedoraTemplateUpgrade27/
- /wiki/FedoraTemplateUpgrade27/
- /doc/template/fedora/upgrade-28-to-29/
- /doc/fedora-template-upgrade-28/
- /en/doc/fedora-template-upgrade-28/
- /doc/FedoraTemplateUpgrade28/
- /wiki/FedoraTemplateUpgrade28/
- /doc/template/fedora/upgrade-29-to-30/
---

# Upgrading Fedora TemplateVMs

This page provides instructions for performing an in-place upgrade of an installed [Fedora TemplateVM].
If you wish to install a new, unmodified Fedora TemplateVM instead of upgrading a template that is already installed in your system, please see the [Fedora TemplateVM] page instead.


## Summary instructions for standard Fedora TemplateVMs

**Note:** The prompt on each line indicates where each command should be entered: `dom0`, `fedora-<old>`, or `fedora-<new>`, where `<old>` is the Fedora version number *from* which you are upgrading, and `<new>` is the Fedora version number *to* which you are upgrading.

    [user@dom0 ~]$ qvm-clone fedora-<old> fedora-<new>
    [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
    [user@dom0 ~]$ qvm-run -a fedora-<new> gnome-terminal
    [user@dom0 ~]$ dev=$(sudo losetup -f --show /var/tmp/template-upgrade-cache.img)
    [user@dom0 ~]$ qvm-block attach fedora-<new> dom0:${dev##*/}
    [user@fedora-<new> ~]$ sudo mkfs.ext4 /dev/xvdi
    [user@fedora-<new> ~]$ sudo mount /dev/xvdi /mnt/removable
    [user@fedora-<new> ~]$ sudo dnf clean all
    [user@fedora-<new> ~]$ sudo dnf --releasever=<new> --setopt=cachedir=/mnt/removable --best --allowerasing distro-sync
    [user@dom0 ~]$ qvm-shutdown fedora-<new>
    [user@dom0 ~]$ sudo losetup -d $dev
    [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

**Recommended:** [Switch everything that was set to the old template to the new template.][switch]


## Detailed instructions for standard Fedora TemplateVMs

These instructions will show you how to upgrade the standard Fedora TemplateVM.
The same general procedure may be used to upgrade any template based on the standard Fedora TemplateVM.

**Note:** The prompt on each line indicates where each command should be entered: `dom0`, `fedora-<old>`, or `fedora-<new>`, where `<old>` is the Fedora version number *from* which you are upgrading, and `<new>` is the Fedora version number *to* which you are upgrading.

 1. Ensure the existing template is not running.

        [user@dom0 ~]$ qvm-shutdown fedora-<old>

 2. Clone the existing template and start a terminal in the new template.

        [user@dom0 ~]$ qvm-clone fedora-<old> fedora-<new>
        [user@dom0 ~]$ qvm-run -a fedora-<new> gnome-terminal

 3. Attempt the upgrade process in the new template.

        [user@fedora-<new> ~]$ sudo dnf clean all
        [user@fedora-<new> ~]$ sudo dnf --releasever=<new> distro-sync --best --allowerasing

    **Note:** `dnf` might ask you to approve importing a new package signing key.
    For example, you might see a prompt like this one:

        warning: /mnt/removable/updates-0b4cc238d1aa4ffe/packages/example-package.fc<new>.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID XXXXXXXX: NOKEY
        Importing GPG key 0xXXXXXXXX:
         Userid     : "Fedora <new> (<new>) <fedora-<new>@fedoraproject.org>"
         Fingerprint: XXXX XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX XXXX
         From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-<new>-x86_64
        Is this ok [y/N]: y

    This key was already checked when it was installed (notice that the "From" line refers to a location on your local disk), so you can safely say yes to this prompt.

    **Note:** If you encounter no errors, proceed to step 4.
    If you do encounter errors, see the next two points first.

     * If `dnf` reports that you do not have enough free disk space to proceed
       with the upgrade process, create an empty file in dom0 to use as a cache
       and attach it to the template as a virtual disk.

           [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
           [user@dom0 ~]$ dev=$(sudo losetup -f --show /var/tmp/template-upgrade-cache.img)
           [user@dom0 ~]$ qvm-block attach fedora-<new> dom0:${dev##*/}

       Then reattempt the upgrade process, but this time use the virtual disk as a cache.

           [user@fedora-<new> ~]$ sudo mkfs.ext4 /dev/xvdi
           [user@fedora-<new> ~]$ sudo mount /dev/xvdi /mnt/removable
           [user@fedora-<new> ~]$ sudo dnf clean all
           [user@fedora-<new> ~]$ sudo dnf --releasever=<new> --setopt=cachedir=/mnt/removable --best --allowerasing distro-sync

       If this attempt is successful, proceed to step 4.

     * `dnf` may complain:

           At least X MB more space needed on the / filesystem.

       In this case, one option is to [resize the TemplateVM's disk image][resize-disk-image] before reattempting the upgrade process.
       (See [Additional Information] below for other options.)

 4. Check that you are on the correct (new) Fedora release.
 
        [user@fedora-<new> ~]$ cat /etc/fedora-release

 5. (Optional) Trim the new template.
    (This should [no longer be necessary][template-notes], but it does not hurt.
    Some users have [reported][5055] that it makes a difference.)

        [user@fedora-<new> ~]$ sudo fstrim -av
        [user@dom0 ~]$ qvm-shutdown fedora-<new>
        [user@dom0 ~]$ qvm-start fedora-<new>
        [user@fedora-<new> ~]$ sudo fstrim -av

 6. Shut down the new TemplateVM.

        [user@dom0 ~]$ qvm-shutdown fedora-<new>

 7. Remove the cache file, if you created one.

        [user@dom0 ~]$ sudo losetup -d $dev
        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

 8. (Recommended) [Switch everything that was set to the old template to the new template.][switch]

 9. (Optional) Make the new template the global default.

        [user@dom0 ~]$ PedOS-prefs --set fedora-<new>

10. (Optional) Remove the old template.
    (Make sure to type the name of the old template, not the new one.)

        [user@dom0 ~]$ sudo dnf remove PedOS-template-fedora-<old>


## Summary instructions for Fedora Minimal TemplateVMs

**Note:** The prompt on each line indicates where each command should be entered: `dom0`, `fedora-<old>`, or `fedora-<new>`, where `<old>` is the Fedora version number *from* which you are upgrading, and `<new>` is the Fedora version number *to* which you are upgrading.

    [user@dom0 ~]$ qvm-clone fedora-<old>-minimal fedora-<new>-minimal
    [user@dom0 ~]$ qvm-run -u root -a fedora-<new>-minimal xterm
    [root@fedora-<new>-minimal ~]# dnf clean all
    [user@fedora-<new>-minimal ~]# dnf --releasever=<new> --best --allowerasing distro-sync
    [user@fedora-<new>-minimal ~]# fstrim -v /

    (Shut down TemplateVM by any normal means.)

(If you encounter insufficient space issues, you may need to use the methods described for the standard template above.)


## StandaloneVMs

The procedure for upgrading a Fedora [StandaloneVM] is the same as for a TemplateVM.


## Release-specific notes

This section contains notes about upgrading to specific releases.


### Fedora 30

If your RPM Fusion repositories are **disabled** when you upgrade a TemplateVM to 30, all RPM Fusion packages and RPM Fusion repo definitions will be removed from that TemplateVM.
If your RPM Fusion repositories are **enabled** when upgrading, all RPM Fusion packages and repo definitions will be retained and updated as expected.
For most users, this behavior should not cause a problem, since a TemplateVM in which the RPM Fusion repos are disabled is probably a TemplateVM in which you never wish to use them.
However, if you wish to have the RPM Fusion repo definitions after upgrading in a TemplateVM in which they are currently disabled, you may wish to temporarily enable them prior to upgrading or manually create, copy, or download them after upgrading.


### End-of-life (EOL) releases

We strongly recommend against using any Fedora release that has reached [end-of-life (EOL)].


## Additional information

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
    [Marek](https://groups.google.com/d/msg/PedOS-users/mCXkxlACILQ/dS1jbLRP9n8J) and
    [Jason M](https://groups.google.com/d/msg/PedOS-users/mCXkxlACILQ/5PxDfI-RKAsJ).


[Fedora TemplateVM]: /doc/templates/fedora/
[resize-disk-image]: /doc/resize-disk-image/
[Additional Information]: #additional-information
[switch]: /doc/templates/#switching
[DispVM]: /doc/dispvm/
[end-of-life (EOL)]: https://fedoraproject.org/wiki/End_of_life
[StandaloneVM]: /doc/standalone-and-hvm/
[template-notes]: /doc/templates/#important-notes
[5055]: https://github.com/PedOS/PedOS-issues/issues/5055

