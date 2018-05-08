---
layout: doc
title: Upgrading the Fedora 26 Template to Fedora 27
permalink: /doc/template/fedora/upgrade-26-to-27/
redirect_from:
- /doc/fedora-template-upgrade-26/
- /en/doc/fedora-template-upgrade-26/
- /doc/FedoraTemplateUpgrade26/
- /wiki/FedoraTemplateUpgrade26/
---

Upgrading the Fedora 26 Template to Fedora 27
=============================================

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Notice:</b>
  Currently, the packages for Fedora 27 are available in the <code>current-testing</code> repository for both Qubes 3.2 and 4.0.
  If you wish, you can help us test these instructions by using <code>--enablerepo=qubes-vm*current-testing</code>.
  Once the packages have migrated to the stable repositories for both versions, this notice will be removed.
</div>

This page provides instructions for performing an in-place upgrade of an
installed Fedora 26 [TemplateVM] to Fedora 27. If you wish to install a new,
unmodified Fedora 27 template instead of upgrading a template that is already
installed in your system, please see the [Fedora TemplateVM] page instead.

These instructions can also be used to upgrade a Fedora 25 TemplateVM to
Fedora 27. Simply start by cloning `fedora-25` instead of `fedora-26` in the
instructions below.


Important information regarding RPM Fusion repos
------------------------------------------------

If your RPM Fusion repositories are **disabled** when you upgrade a TemplateVM from Fedora 26 to 27, all RPM Fusion packages and RPM Fusion repo definitions will be removed from that TemplateVM.
If your RPM Fusion repositories are **enabled** when upgrading, all RPM Fusion packages and repo definitions will be retained and updated as expected.
For most users, this behavior should not cause a problem, since a TemplateVM in which the RPM Fusion repos are disabled is probably a TemplateVM in which you never wish to use them.
However, if you wish to have the RPM Fusion repo definitions after upgrading in a TemplateVM in which they are currently disabled, you may wish to temporarily enable them prior to upgrading or manually create, copy, or download them after upgrading.


Qubes 3.2 Instructions
----------------------

### Summary: Upgrading the Standard Fedora 26 Template to Fedora 27 ###

**Note:** The prompt on each line indicates where each command should be entered
(`@dom0` or `@fedora-27`).

        [user@dom0 ~]$ qvm-clone fedora-26 fedora-27
        [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-run -a fedora-27 gnome-terminal
        [user@dom0 ~]$ qvm-block -A fedora-27 dom0:/var/tmp/template-upgrade-cache.img
        [user@fedora-27 ~]$ sudo mkfs.ext4 /dev/xvdi
        [user@fedora-27 ~]$ sudo mount /dev/xvdi /mnt/removable
        [user@fedora-27 ~]$ sudo dnf clean all
        [user@fedora-27 ~]$ sudo dnf --releasever=27 --setopt=cachedir=/mnt/removable --best --allowerasing distro-sync

    (Shut down TemplateVM by any normal means.)

        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-trim-template fedora-27

(Optional cleanup: Switch everything over to the new template and delete the old
one. See instructions below for details.)


### Detailed: Upgrading the Standard Fedora 26 Template to Fedora 27 ###

These instructions will show you how to upgrade the standard Fedora 26
TemplateVM to Fedora 27. The same general procedure may be used to upgrade any
template based on the standard Fedora 26 template.

**Note:** The command-line prompt on each line indicates where each command
should be entered (`@dom0` or `@fedora-27`).

 1. Ensure the existing template is not running.

        [user@dom0 ~]$ qvm-shutdown fedora-26

 2. Clone the existing template and start a terminal in the new template.

        [user@dom0 ~]$ qvm-clone fedora-26 fedora-27
        [user@dom0 ~]$ qvm-run -a fedora-27 gnome-terminal

 3. Attempt the upgrade process in the new template.

        [user@fedora-27 ~]$ sudo dnf clean all
        [user@fedora-27 ~]$ sudo dnf --releasever=27 distro-sync --best --allowerasing

    **Note:** `dnf` might ask you to approve importing a new package signing
    key. For example, you might see a prompt like this one:

        warning: /var/cache/dnf/fedora-d02ca361e1b58501/packages/python2-babel-2.3.4-1.fc27.noarch.rpm: Header V3 RSA/SHA276 Signature, key ID f5282ee4: NOKEY
        Importing GPG key 0xF5282EE4:
         Userid     : "Fedora (27) <fedora-27-primary@fedoraproject.org>"
         Fingerprint: 860E 19B0 AFA8 00A1 7518 81A6 F55E 7430 F528 2EE4
         From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-27-x86_64
        Is this ok [y/N]:

    This key was already checked when it was installed (notice that the "From"
    line refers to a location on your local disk), so you can safely say yes to
    this prompt.

    **Note:** If you encounter no errors, proceed to step 4. If you do encounter
    errors, see the next two points first.

     * If `dnf` reports that you do not have enough free disk space to proceed
       with the upgrade process, create an empty file in dom0 to use as a cache
       and attach it to the template as a virtual disk.

           [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
           [user@dom0 ~]$ qvm-block -A fedora-27 dom0:/var/tmp/template-upgrade-cache.img

       Then reattempt the upgrade process, but this time use the virtual disk
       as a cache.

           [user@fedora-27 ~]$ sudo mkfs.ext4 /dev/xvdi
           [user@fedora-27 ~]$ sudo mount /dev/xvdi /mnt/removable
           [user@fedora-27 ~]$ sudo dnf clean all
           [user@fedora-27 ~]$ sudo dnf --releasever=27 --setopt=cachedir=/mnt/removable --best --allowerasing distro-sync

       If this attempt is successful, proceed to step 4.

     * `dnf` may complain:

           At least X MB more space needed on the / filesystem.

       In this case, one option is to [resize the TemplateVM's disk
       image][resize-disk-image] before reattempting the upgrade process.
       (See [Additional Information] below for other options.)

 4. Shut down the new TemplateVM (from the command-line or Qubes VM Manager).

        [user@dom0 ~]$ qvm-shutdown fedora-27

 5. Remove the cache file, if you created one.

        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

 6. Trim the new template (see [Compacting the Upgraded Template] for details
    and other options).

        [user@dom0 ~]$ qvm-trim-template fedora-27

 7. (Recommended) Switch everything that was set to the old template to the new
    template, e.g.:

     1. Make the new template the default template:

        Qubes Manager --> Global settings --> Default template

     2. Base AppVMs on the new template. In Qubes Manager, for each VM that is
        currently based on `fedora-26` that you would like to base on
        `fedora-27`, enter its VM settings and change the Template selection:

        Qubes Manager --> (Select a VM) --> VM settings --> Template

     3. Base the [DispVM] template on the new template.

        If you have set the new template as your default template:

            [user@dom0 ~]$ qvm-create-default-dvm --default-template

        Otherwise:

            [user@dom0 ~]$ qvm-create-default-dvm fedora-27

 8. (Optional) Remove the old template. (Make sure to type `fedora-26`, not
    `fedora-27`.)

        [user@dom0 ~]$ sudo dnf remove qubes-template-fedora-26


### Compacting the Upgraded Template ###

Neither `fstrim` nor the `discard` mount option works on the TemplateVM's root
filesystem, so when a file is removed in the template, space is not freed in
dom0. This means that the template will use about twice as much space as is
really necessary after upgrading.

You can use the `qvm-trim-template` tool:

    [user@dom0 ~]$ qvm-trim-template fedora-27


### Upgrading StandaloneVMs ###

The procedure for upgrading a StandaloneVM from Fedora 26 to Fedora 27 is the
same as for a TemplateVM, except that `qvm-trim-template` does not work on
StandaloneVMs. Instead, you should run the following command inside the
StandaloneVM in order to compact it:

    $ sudo fstrim -v -a


### Summary: Upgrading the Minimal Fedora 26 Template to Fedora 27 ###

**Note:** The prompt on each line indicates where each command should be entered
(`@dom0` or `@fedora-27`).

        [user@dom0 ~]$ qvm-clone fedora-26-minimal fedora-27-minimal
        [user@dom0 ~]$ qvm-run -u root -a fedora-27-minimal xterm
        [root@fedora-27-minimal ~]# dnf clean all
        [user@fedora-27-minimal ~]# dnf --releasever=27 --best --allowerasing distro-sync

    (Shut down TemplateVM by any normal means.)

        [user@dom0 ~]$ qvm-trim-template fedora-27-minimal

(If you encounter insufficient space issues, you may need to use the methods
described for the standard template above.)


Qubes 4.0 Instructions
----------------------

### Summary: Upgrading the Standard Fedora 26 Template to Fedora 27 ###

**Note:** The prompt on each line indicates where each command should be entered
(`@dom0` or `@fedora-27`).

        [user@dom0 ~]$ qvm-clone fedora-26 fedora-27
        [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
        [user@dom0 ~]$ qvm-run -a fedora-27 gnome-terminal
        [user@dom0 ~]$ dev=$(sudo losetup -f --show /var/tmp/template-upgrade-cache.img)
        [user@dom0 ~]$ qvm-block attach fedora-27 dom0:${dev##*/}
        [user@fedora-27 ~]$ sudo mkfs.ext4 /dev/xvdi
        [user@fedora-27 ~]$ sudo mount /dev/xvdi /mnt/removable
        [user@fedora-27 ~]$ sudo dnf clean all
        [user@fedora-27 ~]$ sudo dnf --releasever=27 --setopt=cachedir=/mnt/removable --best --allowerasing distro-sync
        [user@fedora-27 ~]$ sudo fstrim -v /

    (Shut down TemplateVM by any normal means.)

        [user@dom0 ~]$ sudo losetup -d $dev
        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

(Optional cleanup: Switch everything over to the new template and delete the old
one. See instructions below for details.)


### Detailed: Upgrading the Standard Fedora 26 Template to Fedora 27 ###

These instructions will show you how to upgrade the standard Fedora 26
TemplateVM to Fedora 27. The same general procedure may be used to upgrade any
template based on the standard Fedora 26 template.

**Note:** The command-line prompt on each line indicates where each command
should be entered (`@dom0` or `@fedora-27`).

 1. Ensure the existing template is not running.

        [user@dom0 ~]$ qvm-shutdown fedora-26

 2. Clone the existing template and start a terminal in the new template.

        [user@dom0 ~]$ qvm-clone fedora-26 fedora-27
        [user@dom0 ~]$ qvm-run -a fedora-27 gnome-terminal

 3. Attempt the upgrade process in the new template.

        [user@fedora-27 ~]$ sudo dnf clean all
        [user@fedora-27 ~]$ sudo dnf --releasever=27 distro-sync --best --allowerasing

    **Note:** `dnf` might ask you to approve importing a new package signing
    key. For example, you might see a prompt like this one:

        warning: /var/cache/dnf/fedora-d02ca361e1b58501/packages/python2-babel-2.3.4-1.fc27.noarch.rpm: Header V3 RSA/SHA276 Signature, key ID f5282ee4: NOKEY
        Importing GPG key 0xF5282EE4:
         Userid     : "Fedora (27) <fedora-27-primary@fedoraproject.org>"
         Fingerprint: 860E 19B0 AFA8 00A1 7518 81A6 F55E 7430 F528 2EE4
         From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-27-x86_64
        Is this ok [y/N]:

    This key was already checked when it was installed (notice that the "From"
    line refers to a location on your local disk), so you can safely say yes to
    this prompt.

    **Note:** If you encounter no errors, proceed to step 4. If you do encounter
    errors, see the next two points first.

     * If `dnf` reports that you do not have enough free disk space to proceed
       with the upgrade process, create an empty file in dom0 to use as a cache
       and attach it to the template as a virtual disk.

           [user@dom0 ~]$ truncate -s 5GB /var/tmp/template-upgrade-cache.img
           [user@dom0 ~]$ dev=$(sudo losetup -f --show /var/tmp/template-upgrade-cache.img)
           [user@dom0 ~]$ qvm-block attach fedora-27 dom0:${dev##*/}

       Then reattempt the upgrade process, but this time use the virtual disk
       as a cache.

           [user@fedora-27 ~]$ sudo mkfs.ext4 /dev/xvdi
           [user@fedora-27 ~]$ sudo mount /dev/xvdi /mnt/removable
           [user@fedora-27 ~]$ sudo dnf clean all
           [user@fedora-27 ~]$ sudo dnf --releasever=27 --setopt=cachedir=/mnt/removable --best --allowerasing distro-sync

       If this attempt is successful, proceed to step 4.

     * `dnf` may complain:

           At least X MB more space needed on the / filesystem.

       In this case, one option is to [resize the TemplateVM's disk
       image][resize-disk-image] before reattempting the upgrade process.
       (See [Additional Information] below for other options.)

 4. Trim the new template.

        [user@fedora-27 ~]$ sudo fstrim -v /

 5. Shut down the new TemplateVM (from the command-line or Qubes VM Manager).

        [user@dom0 ~]$ qvm-shutdown fedora-27

 6. Remove the cache file, if you created one.

        [user@dom0 ~]$ sudo losetup -d $dev
        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

 7. (Recommended) Switch everything that was set to the old template to the new
    template, e.g.:

     1. Make the new template the default template:

        Applications Menu --> System Tools --> Qubes Global Settings --> Default template

     2. Base AppVMs on the new template. In Qubes Manager, for each VM that is
        currently based on `fedora-26` that you would like to base on
        `fedora-27`, enter its VM settings and change the Template selection:

        Applications Menu --> (select a VM) --> VM settings --> Template

     3. Base the [DispVM] template on the new template.

            [user@dom0 ~]$ qvm-create -l red -t fedora-27 fedora-27-dvm
            [user@dom0 ~]$ qvm-prefs fedora-27-dvm template_for_dispvms True
            [user@dom0 ~]$ qvm-features fedora-27-dvm appmenus-dispvm 1
            [user@dom0 ~]$ qubes-prefs default-dispvm fedora-27-dvm

 8. (Optional) Remove the old template. (Make sure to type `fedora-26`, not
    `fedora-27`.)

        [user@dom0 ~]$ sudo dnf remove qubes-template-fedora-26


### Upgrading StandaloneVMs ###

The procedure for upgrading a StandaloneVM from Fedora 26 to Fedora 27 is the
same as for a TemplateVM.


### Summary: Upgrading the Minimal Fedora 26 Template to Fedora 27 ###

**Note:** The prompt on each line indicates where each command should be entered
(`@dom0` or `@fedora-27`).

        [user@dom0 ~]$ qvm-clone fedora-26-minimal fedora-27-minimal
        [user@dom0 ~]$ qvm-run -u root -a fedora-27-minimal xterm
        [root@fedora-27-minimal ~]# dnf clean all
        [user@fedora-27-minimal ~]# dnf --releasever=27 --best --allowerasing distro-sync
        [user@fedora-27-minimal ~]# fstrim -v /

    (Shut down TemplateVM by any normal means.)

(If you encounter insufficient space issues, you may need to use the methods
described for the standard template above.)


Additional Information
----------------------

As mentioned above, you may encounter the following `dnf` error:

    At least X MB more space needed on the / filesystem.

In this case, you have several options:

 1. [Increase the TemplateVM's disk image size][resize-disk-image].
    This is the solution mentioned in the main instructions above.
 2. Delete files in order to free up space. One way to do this is by
    uninstalling packages. You may then reinstalling them again after you
    finish the upgrade process, if desired). However, you may end up having to
    increase the disk image size anyway (see previous option).
 3. Do the upgrade in parts, e.g., by using package groups. (First upgrade
    `@core` packages, then the rest.)
 4. Do not perform an in-place upgrade. Instead, simply download and install a
    new template package, then redo all desired template modifications.

    With regard to the last option, here are some useful messages from the
    mailing list which also apply to TemplateVM management and migration in
    general:

     * [Marek](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/dS1jbLRP9n8J)
     * [Jason M](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/5PxDfI-RKAsJ)


[TemplateVM]: /doc/templates/
[Fedora TemplateVM]: /doc/templates/fedora/
[resize-disk-image]: /doc/resize-disk-image/
[Additional Information]: #additional-information
[Compacting the Upgraded Template]: #compacting-the-upgraded-template
[DispVM]: /doc/dispvm/

