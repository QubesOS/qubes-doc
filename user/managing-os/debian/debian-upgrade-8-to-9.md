---
layout: doc
title: Upgrading the Debian 8 Template to Debian 9
permalink: /doc/template/debian/upgrade-8-to-9/
redirect_from:
- /doc/debian-template-upgrade-8/
- /en/doc/debian-template-upgrade-8/
- /doc/DebianTemplateUpgrade8/
- /wiki/DebianTemplateUpgrade8/
---

Upgrading the Debian 8 Template
===============================

Please note that if you installed packages from one of the testing repositories you must make sure that the repository is enabled in `/etc/apt/sources.list.d/qubes-r3.list` before attempting the upgrade. 
Otherwise, your upgrade will [break](https://github.com/QubesOS/qubes-issues/issues/2418).

Summary: Upgrading a Debian 8 Template to Debian 9
--------------------------------------------------

        [user@dom0 ~]$ qvm-clone debian-8 debian-9
        [user@dom0 ~]$ qvm-run -a debian-9 gnome-terminal
        [user@debian-9 ~]$ sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list
        [user@debian-9 ~]$ sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list.d/qubes-r3.list
        [user@debian-9 ~]$ sudo apt-get update && sudo apt-get dist-upgrade -y
        [user@debian-9 ~]$ sudo apt-get autoremove
	
    (Shut down TemplateVM by any normal means.)

        [user@dom0 ~]$ qvm-trim-template debian-9

    (Done.)

Detailed: Upgrading the Standard Debian 8 Template to Debian 9
--------------------------------------------------------------

These instructions will show you how to upgrade the standard Debian 8
TemplateVM to Debian 9. The same general procedure may be used to upgrade
any template based on the standard Debian 8 template. 

 1. Ensure the existing template is not running. 

        [user@dom0 ~]$ qvm-shutdown debian-8
 
 2. Clone the existing template and start a terminal in the new template.

        [user@dom0 ~]$ qvm-clone debian-8 debian-9
        [user@dom0 ~]$ qvm-run -a debian-9 gnome-terminal

 3. Update your apt repositories to use stretch instead of jessie
    (This can be done manually with a text editor, but sed can be used to
    automatically update the files.)

        [user@debian-9 ~]$ sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list
        [user@debian-9 ~]$ sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list.d/qubes-r3.list

 4. Update the package lists and upgrade to Debian 9. During the process,
    it will likely prompt to overwrite two files, qubes-r3.list and
    pulse/client.conf. qubes-r3.list can be overwritten, while pulse/client.conf
    need to left as the currently installed version.
 
        [user@debian-9 ~]$ sudo apt-get update && sudo apt-get dist-upgrade -y

 5. Remove unnecessary packages that were previously installed

        [user@debian-9 ~]$ sudo apt-get autoremove

 6. Shutdown the new TemplateVM via dom0 command line or Qubes VM Manager;

        [user@dom0 ~]$ qvm-shutdown debian-9
        
 7. Trim the new template (see **Compacting the Upgraded Template** for details
    and other options).

        [user@dom0 ~]$ qvm-trim-template debian-9

 8. (Recommended) [Switch everything that was set to the old template to the new
    template.](/doc/templates/#how-to-switch-templates)

 9. (Optional) Remove the old default template.

        [user@dom0 ~]$ sudo yum remove qubes-template-debian-8
	

Compacting the Upgraded Template
--------------------------------

Neither `fstrim` nor the `discard` mount option works on the TemplateVM's root
filesystem, so when a file is removed in the template, space is not freed in
dom0. This means that the template will use about twice as much space as is
really necessary after upgrading.

If you have at least `qubes-core-dom0-2.1.68` installed or are on Qubes R3.0,
you can use the `qvm-trim-template` tool:

        [user@dom0 ~]$ qvm-trim-template debian-9

If you do not have `qubes-core-dom0-2.1.68` or are on older Qubes version, you can
compact the `root.img` manually. To do this, you will need about 15GB (the
TemplateVM's max size + the actually used space there) free space in dom0.

 1. Start the template and fill all the free space with zeros, for example
    with:

        [user@debian-9 ~]$ dd if=/dev/zero of=/var/tmp/zero

 2. Wait for the "No space left on device" error. Then:

        [user@debian-9 ~]$ rm -f /var/tmp/zero

 3. Shut down the template and all VMs based on it. Then:

        [user@dom0 ~]$ cd /var/lib/qubes/vm-templates/debian-9
        [user@dom0 ~]$ cp --sparse=always root.img root.img.new
        [user@dom0 ~]$ mv root.img.new root.img

Additional Information
----------------------

Debian Stretch packages were first made available in the Qubes R3.1 repositories.

If sound is not working, you may need to enable the Qubes testing repository to get the testing version of qubes-gui-agent. 
This can be done by editing the /etc/apt/sources.list.d/qubes-r3.list file and uncommenting the Qubes Updates Candidates repo.

User-initiated updates/upgrades may not run when a templateVM first starts. 
This is due to a new Debian config setting that attempts to update automatically; it should be disabled with:  
`sudo systemctl disable apt-daily.{service,timer}`.

Relevant Discussions
--------------------
 * [Stretch Template Installation](https://groups.google.com/forum/#!topicsearchin/qubes-devel/debian$20stretch/qubes-devel/4rdayBF_UTc)
 * [Stretch availability in 3.2](https://groups.google.com/forum/#!topicsearchin/qubes-devel/debian$20stretch/qubes-devel/cekPfBqQMOI)
 * [Fixing sound in Debian Stretch](https://groups.google.com/forum/#!topic/qubes-users/JddCE54GFiU)
 * [User apt commands blocked on startup](https://github.com/QubesOS/qubes-issues/issues/2621)

