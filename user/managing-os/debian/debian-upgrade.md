---
layout: doc
title: Upgrading the Debian Templates
permalink: /doc/template/debian/upgrade/
redirect_from:
---

Upgrading Debian Templates
===============================

In general, upgrading a Debian template follows the same process as [upgrading a native Debian system][upgrade].
You should consult the release notes for the target version. For Debian-10 see [here][release].

Please note that if you installed packages from one of the testing repositories you must make sure that the repository is enabled in `/etc/apt/sources.list.d/qubes-r4.list` before attempting the upgrade. 
Otherwise, your upgrade will [break](https://github.com/QubesOS/qubes-issues/issues/2418).

By default, Qubes uses codenames in the apt sources files, although the templates are referred to by release number.
Check the code names for the templates, and ensure you are aware of any changes you have made in the repository definitons.

In this example we are upgrading from debian-9 (stretch) to debian-10 (buster)


Summary: Upgrading a Debian Template 
--------------------------------------------------

 1. Clone the existing template.
 2. Open a terminal in the new template.
 3. Edit the sources.list files to refer to the new version.
 4. Perform the upgrade:
```
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
```
 5. Compact the template
 6. Shutdown and start using the new template.

Detailed instructions:
--------------------------------------------------------------

These instructions show you how to upgrade the standard Debian 9 TemplateVM to Debian 10.

 1. Ensure the existing template is not running. 

        [user@dom0 ~]$ qvm-shutdown debian-9
 
 2. Clone the existing template and start a terminal in the new template.

        [user@dom0 ~]$ qvm-clone debian-9 debian-10
        [user@dom0 ~]$ qvm-run -a debian-10 gnome-terminal

 3. Update your apt repositories to use buster instead of stretch
    (This can be done manually with a text editor, but sed can be used to automatically update the files.)

	```
	$ sudo sed -i 's/stretch/buster/g' /etc/apt/sources.list
	$ sudo sed -i 's/stretch/buster/g' /etc/apt/sources.list.d/qubes-r4.list
	```

4. Update the package lists and upgrade to Debian 10.
During the process, it may prompt you to overwrite the file `qubes-r4.list`.
You should overwrite this file.
 
	```
	$ sudo apt update
	$ sudo apt upgrade 
	$ sudo apt dist-upgrade 
	```
 5. (optional) Remove unnecessary packages that were previously installed

	`sudo apt-get autoremove`

 6. (optional) Clean cached packages from /var/cache/apt
	```
	$ sudo apt-get clean
	```

 7. Compact the template.

 8. Shutdown the new TemplateVM via dom0 command line or the Qube Manager.

 9. (Recommended) [Switch everything that was set to the old template to the new template.][switch]

 10. (Optional) Change the global default template to use the new template.

 11. (Optional) Remove the old template using dom0 command line or the Qube Manager.


Compacting the Upgraded Template
--------------------------------

 1. Open a terminal in the template and run:
	```
	$ sudo fstrim -av
	$ sudo shutdown -h
	```
 2. Restart the template and run step 1 again.  
This ensures that changes in the upgrade process are not stored in a difference file.
 

Additional Information
----------------------

User-initiated updates/upgrades may not run when a templateVM first starts. 
This is due to a Debian config setting that attempts to update the system automatically.
You should disable this by opening a terminal in the template and running:
```
$ sudo systemctl disable apt-daily.{service,timer}`.
```

Look [here][jessie] for notes specific to updating a jessie template.

Relevant Discussions
--------------------
 * [User apt commands blocked on startup][2621]

[upgrade]: https://wiki.debian.org/DebianUpgrade
[2621]: https://github.com/QubesOS/qubes-issues/issues/2621
[switch]: /doc/templates/#how-to-switch-templates)
[release]: https://www.debian.org/releases/buster/amd64/release-notes/ch-upgrading.en.html
[switch]: /doc/templates/#how-to-switch-templates
[jessie]: /doc/template/debian/upgrade-8-to-9/
