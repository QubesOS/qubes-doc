---
layout: doc
title: Updating Whonix in Qubes
permalink: /doc/privacy/updating-whonix/
---

Updating Whonix in Qubes
========================

It is important to keep your Whonix templates current as to get important security updates.

### Configure Whonix TemplateVM proxy settings


![TemplateVM Proxy Settings](/attachment/wiki/Whonix/Qubes-Whonix-Gateway_TemplateVM_Qubes_VM_Manager_Settings.png)

### Open the Whonix Terminals

Launch `Terminal` for both `whonix-gw` and `whonix-ws` TemplateVMs and then perform the following steps to both TemplateVMs

~~~
sudo apt-get update && sudo apt-get dist-upgrade
~~~

The output should look similar to this.

~~~
Hit http://security.debian.org jessie/updates Release.gpg

Hit http://security.debian.org jessie/updates Release

Hit http://deb.torproject.org jessie Release.gpg

Hit http://ftp.us.debian.org jessie Release.gpg

Hit http://security.debian.org jessie/updates/main i386 Packages
Hit http://deb.torproject.org jessie Release
Hit http://security.debian.org jessie/updates/contrib i386 Packages
Hit http://ftp.us.debian.org jessie Release
Hit http://security.debian.org jessie/updates/non-free i386 Packages
Hit http://deb.torproject.org jessie/main i386 Packages
Hit http://security.debian.org jessie/updates/contrib Translation-en
Hit http://ftp.us.debian.org jessie/main i386 Packages
Hit http://security.debian.org jessie/updates/main Translation-en

Hit http://ftp.us.debian.org jessie/contrib i386 Packages

Hit http://security.debian.org jessie/updates/non-free Translation-en

Hit http://ftp.us.debian.org jessie/non-free i386 Packages

Ign http://ftp.us.debian.org jessie/contrib Translation-en

Ign http://ftp.us.debian.org jessie/main Translation-en

Ign http://ftp.us.debian.org jessie/non-free Translation-en

Ign http://deb.torproject.org jessie/main Translation-en_US

Ign http://deb.torproject.org jessie/main Translation-en

Reading package lists... Done
~~~

  However, if what you see is different or you see the word `WARNING:` you should look at our troubleshooting documentation for [Debian and Whonix](/doc/troubleshooting/debian-and-whonix/).

### Restart Services after Upgrading

After upgrading either (easy) reboot.

~~~
sudo reboot
~~~


### Restart after Kernel Upgrades

When `linux-image-...` was upgraded, reboot is required to profit from security updates.


Operating System Updates

Shutdown Whonix TemplateVM

~~~
Qubes VM Manager -> right clock on TemplateVM -> Shutdown VM
~~~

### Restart / Update Whonix VMs

If new updates were available and installed, you will need to either simply restart your running Whonix-Gateway ProxyVMs and running Whonix-Workstation AppVMs for them to be updated -- or alternatively apply this same update process again to your running VMs if not wanting to restart them right away.
