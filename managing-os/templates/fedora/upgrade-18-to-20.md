---
layout: doc
title: Upgrading the Fedora 18 Template to Fedora 20
permalink: /doc/template/fedora/upgrade-18-to-20/
redirect_from:
- /doc/fedora-template-upgrade-18/
- /en/doc/fedora-template-upgrade-18/
- /doc/FedoraTemplateUpgrade18/
- /wiki/FedoraTemplateUpgrade/
---

Upgrading the Fedora 18 Template
================================

(**Note:** There is a [newer version of this page for upgrading from Fedora 20 to Fedora 21](/doc/fedora-template-upgrade-20/).)

This instruction in simplified version of [official Fedora instruction](https://fedoraproject.org/wiki/Upgrading_Fedora_using_yum). Note that only "yum" method will work in Qubes template VM (if you are curious why: mostly because template VM does not have own bootloader).

Upgrading Fedora 18 to Fedora 20
--------------------------------

Commands to run in dom0 console (you can do the same from Qubes Manager):

~~~
qvm-clone fedora-18-x64 fedora-20-x64
qvm-run -a fedora-20-x64 gnome-terminal
~~~

Commands to run in new fedora-20-x64 template:

~~~
sudo yum --releasever=20 distro-sync
poweroff
~~~

If you have installed a lot of software in your template, it may happen that you don't have enough disk space for upgrade. Yum will tell you this just after confirming the operation (before it change anything to your system). In that case you need to provide some "external" place for yum cache (uses about 2GB during upgrade). For example attach virtual disk stored in some file. Prepare the file in dom0:

~~~
truncate -s 5GB /var/tmp/template-upgrade-cache.img
qvm-block -A fedora-20-x64 dom0:/var/tmp/template-upgrade-cache.img
~~~

Then use it in template:

~~~
sudo mkfs.ext4 /dev/xvdi
sudo mount /dev/xvdi /mnt/removable
sudo yum --releasever=20 --setopt=cachedir=/mnt/removable distro-sync
~~~

After upgrade is finished, you can remove /var/tmp/template-upgrade-cache.img file.

Compacting templates root.img
-----------------------------

fstrim, nor "discard" mount option do not work on template root fs, so when some file is removed in the template, space isn't freed in dom0. This means that template will use about twice a space that is really need after upgrade.

**If you have at least `qubes-core-dom0-2.1.68` installed, you can use `qvm-trim-template` tool. Otherwise use instructions below.**

You can compact root.img in the "old way", you'll need about 15GB (template's max size + really used space there) in dom0 for this operation: Start the template, fill all the free space with zeros, for example with:

~~~
dd if=/dev/zero of=/var/tmp/zero
(wait for "No space left on device" error)
rm -f /var/tmp/zero
~~~

Then shutdown template and all VMs based on it. Go into template directory in dom0 (/var/lib/qubes/vm-templates/fedora-20-x64 or so) and issue:

~~~
cp --sparse=always root.img root.img.new
mv root.img.new root.img
~~~

Done.
