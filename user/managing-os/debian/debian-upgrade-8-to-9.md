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

Please note that if you installed packages from one of the testing repositories you must make sure that the repository is enabled in `/etc/apt/sources.list.d/qubes-r4.list` before attempting the upgrade. 
Otherwise, your upgrade will [break](https://github.com/QubesOS/qubes-issues/issues/2418).

Summary: Upgrading a Debian 8 Template to Debian 9
--------------------------------------------------

    [user@dom0 ~]$ qvm-clone debian-8 debian-9
    [user@dom0 ~]$ qvm-run -a debian-9 gnome-terminal
    [user@debian-9 ~]$ sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list
    [user@debian-9 ~]$ sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list.d/qubes-r4.list
    [user@debian-9 ~]$ sudo apt-get update && sudo apt-get dist-upgrade -y
    [user@debian-9 ~]$ sudo apt-get autoremove

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
        [user@debian-9 ~]$ sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list.d/qubes-r4.list

 4. Update the package lists and upgrade to Debian 9. During the process,
    it will likely prompt to overwrite two files, qubes-r4.list and
    pulse/client.conf. qubes-r4.list can be overwritten, while pulse/client.conf
    need to left as the currently installed version.
 
        [user@debian-9 ~]$ sudo apt-get update && sudo apt-get dist-upgrade -y

 5. Remove unnecessary packages that were previously installed

        [user@debian-9 ~]$ sudo apt-get autoremove

 6. Shutdown the new TemplateVM via dom0 command line or Qubes VM Manager;

        [user@dom0 ~]$ qvm-shutdown debian-9
        
 7. (Recommended) [Switch everything that was set to the old template to the new
    template.](/doc/templates/#how-to-switch-templates)

 8. (Optional) Remove the old default template.

        [user@dom0 ~]$ sudo yum remove qubes-template-debian-8

Additional Information
----------------------

Debian Stretch packages were first made available in the Qubes R3.1 repositories.

If sound is not working, you may need to enable the Qubes testing repository to get the testing version of qubes-gui-agent. 
This can be done by editing the /etc/apt/sources.list.d/qubes-r4.list file and uncommenting the Qubes Updates Candidates repo.

User-initiated updates/upgrades may not run when a templateVM first starts. 
This is due to a new Debian config setting that attempts to update automatically; it should be disabled with:  
`sudo systemctl disable apt-daily.{service,timer}`.

Relevant Discussions
--------------------
 * [Stretch Template Installation](https://groups.google.com/forum/#!topicsearchin/qubes-devel/debian$20stretch/qubes-devel/4rdayBF_UTc)
 * [Stretch availability in 3.2](https://groups.google.com/forum/#!topicsearchin/qubes-devel/debian$20stretch/qubes-devel/cekPfBqQMOI)
 * [Fixing sound in Debian Stretch](https://groups.google.com/forum/#!topic/qubes-users/JddCE54GFiU)
 * [User apt commands blocked on startup](https://github.com/QubesOS/qubes-issues/issues/2621)

