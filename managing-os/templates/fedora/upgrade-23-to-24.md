---
layout: doc
title: Upgrading the Fedora 23 Template to Fedora 24
permalink: /doc/template/fedora/upgrade-23-to-24/
redirect_from:
- /doc/fedora-template-upgrade-23/
- /en/doc/fedora-template-upgrade-23/
- /doc/FedoraTemplateUpgrade23/
- /wiki/FedoraTemplateUpgrade23/
---

Upgrading the Fedora 23 Template
================================

Summary: Upgrading the Standard Fedora 23 Template to Fedora 24
---------------------------------------------------------------

**Note:** The prompt on each line indicates where each command should be entered
(`@dom0` or `@fedora-24`).

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

(Optional cleanup: Switch everything over to the new template and delete the old
one. See instructions below for details.)


Detailed: Upgrading the Standard Fedora 23 Template to Fedora 24
----------------------------------------------------------------

These instructions will show you how to upgrade the standard Fedora 23
TemplateVM to Fedora 24. The same general procedure may be used to upgrade any
template based on the standard Fedora 23 template.

**Note:** The command-line prompt on each line indicates where each command
should be entered (`@dom0` or `@fedora-24`).

 1. Ensure the existing template is not running. 

        [user@dom0 ~]$ qvm-shutdown fedora-23
 
 2. Clone the existing template and start a terminal in the new template.

        [user@dom0 ~]$ qvm-clone fedora-23 fedora-24
        [user@dom0 ~]$ qvm-run -a fedora-24 gnome-terminal

 3. Attempt the upgrade process in the new template.

        [user@fedora-24 ~]$ sudo dnf clean all
        [user@fedora-24 ~]$ sudo dnf --releasever=24 distro-sync

    **Note:** `dnf` might ask you to approve importing a new package signing
    key. For example, you might see a prompt like this one:

        warning: /var/cache/dnf/fedora-d02ca361e1b58501/packages/python2-babel-2.3.4-1.fc24.noarch.rpm: Header V3 RSA/SHA256 Signature, key ID 81b46521: NOKEY
        Importing GPG key 0x81B46521:
         Userid     : "Fedora (24) <fedora-24-primary@fedoraproject.org>"
         Fingerprint: 5048 BDBB A5E7 76E5 47B0 9CCC 73BD E983 81B4 6521
         From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-24-x86_64
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
           [user@dom0 ~]$ qvm-block -A fedora-24 dom0:/var/tmp/template-upgrade-cache.img

       Then reattempt the upgrade process, but this time use the virtual disk
       as a cache.

           [user@fedora-24 ~]$ sudo mkfs.ext4 /dev/xvdi
           [user@fedora-24 ~]$ sudo mount /dev/xvdi /mnt/removable
           [user@fedora-24 ~]$ sudo dnf clean all
           [user@fedora-24 ~]$ sudo dnf --releasever=24 --setopt=cachedir=/mnt/removable distro-sync

       If this attempt is successful, proceed to step 4.

     * `dnf` may complain:

           At least X MB more space needed on the / filesystem.

       In this case, one option is to [resize the TemplateVM's disk
       image][resize-disk-image] before reattempting the upgrade process. 
       (See [Additional Information] below for other options.)

 4. Shut down the new TemplateVM (from the command-line or Qubes VM Manager).

        [user@dom0 ~]$ qvm-shutdown fedora-24

 5. Remove the cache file, if you created one.

        [user@dom0 ~]$ rm /var/tmp/template-upgrade-cache.img

 6. Trim the new template (see [Compacting the Upgraded Template] for details
    and other options).

        [user@dom0 ~]$ qvm-trim-template fedora-24

 7. (Recommended) Switch everything that was set to the old template to the new
    template, e.g.:

     1. Make the new template the default template:

        Qubes Manager --> Global settings --> Default template

     2. Base AppVMs on the new template. In Qubes Manager, for each VM that is
        currently based on `fedora-23` that you would like to base on
        `fedora-24`, enter its VM settings and change the Template selection:

        Qubes Manager --> (Select a VM) --> VM settings --> Template

     3. Base the [DispVM] template on the new template.

        If you have set the new template as your default template:

            [user@dom0 ~]$ qvm-create-default-dvm --default-template

        Otherwise:

            [user@dom0 ~]$ qvm-create-default-dvm fedora-24

 8. (Optional) Remove the old template. (Make sure to type `fedora-23`, not
    `fedora-24`.)

        [user@dom0 ~]$ sudo dnf remove qubes-template-fedora-23


Summary: Upgrading the Minimal Fedora 23 Template to Fedora 24
--------------------------------------------------------------

**Note:** The prompt on each line indicates where each command should be entered
(`@dom0` or `@fedora-24`).

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


Upgrading StandaloneVMs
-----------------------

The procedure for upgrading a StandaloneVM from Fedora 23 to Fedora 24 is the
same as for a TemplateVM, except that `qvm-trim-template` does not work on
StandaloneVMs. Instead, you should run the following command inside the
StandaloneVM in order to compact it:

    $ sudo fstrim -v -a


Additional Information
----------------------

As mentioned above, you may encounter the following `dnf` error:

    At least X MB more space needed on the / filesystem.

In this case, you have several options:

 1. [Increase the TemplateVM's disk image size][resize-disk-image].
    This is the solution mentioned in the main instructions above.
 2. Delete files in order to free up space. One way to do this is by
    uninstalling packages. You may then reinstall them again after you
    finish the upgrade process, if desired). However, you may end up having to
    increase the disk image size anyway (see previous option).
 3. Increase the `root.img` size with `qvm-grow-root`.
 4. Do the upgrade in parts, e.g., by using package groups. (First upgrade
    `@core` packages, then the rest.)
 5. Do not perform an in-place upgrade. Instead, simply download and install a
    new template package, then redo all desired template modifications.

    With regard to the last option, here are some useful messages from the
    mailing list which also apply to TemplateVM management and migration in
    general:

     * [Marek](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/dS1jbLRP9n8J)
     * [Jason M](https://groups.google.com/d/msg/qubes-users/mCXkxlACILQ/5PxDfI-RKAsJ)


[resize-disk-image]: /doc/resize-disk-image/
[Additional Information]: #additional-information
[Compacting the Upgraded Template]: #compacting-the-upgraded-template
[DispVM]: /doc/dispvm/
