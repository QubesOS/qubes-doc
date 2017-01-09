---
layout: doc
title: How to create a Kali Linux VM
permalink: /doc/kali/
---

How to Create a Kali Linux VM
=============================

This guide will explain how to create your own [Kali] Linux VM as a VM
template. The basic idea is to personalize the template with the tools you need
and then spin up isolated AppVMs based on the template.

This has been tested on Qubes OS 3.2.

The steps can be summarised as:

1. Install Qubes' Debian 8.0 (Jessie) template
2. Upgrade the template to Debian 9.0 (Stretch)
3. Install kali through the ``kali-linux-full`` package
4. Use the template to build appVM so that you can maintain isolation between
   e.g. pentesting jobs


Steps to build a Kali template
------------------------------

### Get the GPG key

1. You'll need to fetch the Kali GPG key from a dispVM as the template you'll
   build won't have direct internet connectivity unless you enable it from the
   firewall:

        # in a dispVM
        gpg --keyserver hkp://keys.gnupg.net --recv-key 7D8D0BF6
        gpg --list-keys --with-fingerprint 7D8D0BF6 
        gpg --export --armor 7D8D0BF6 > kali.asc

2. **DO NOT TURN OFF** the dispVM

3. Make sure the key ID is the valid one listed on the [Kali website]. Ideally,
   verify the fingerprint through other channels.

Once you have the key, keep the dispVM on as you'll need to copy the key over
to the Kali template.

### Customize the template

1. Install [the debian-8 template] (if not already installed)

2. Clone the debian template and start a terminal in it:

        # in dom0:
        qvm-clone debian-8 debian-9
        qvm-run -a debian-9 gnome-terminal

        # in the debian-9 template terminal:
        # substitute jessie for stretch in
        sudo -s
        sensible-editor /etc/apt/sources.list
        sensible-editor /etc/apt/sources.list.d/qubes-r3.list
        apt-get update && apt-get dist-upgrade
        # (hat tip: [the Debian wiki])

    Restart the template when done and make sure you can open a terminal.

3. Prepare the kali template:

        # in dom0:
        qvm-shutdown debian-9
        qvm-clone debian-9 kali-tpl
        qvm-run -a kali-tpl gnome-terminal

3. Add the sources to install Kali linux to the `kali-tpl` template:

        # in kali-tpl:
        sudo -s
        echo 'deb http://http.kali.org/kali kali-rolling main non-free contrib' >> /etc/apt/sources.list

4. Copy the Kali key from the dispVM into the template:

        # in the dispVM:
        qvm-copy-to-vm kali-tpl kali.asc

        # in kali-tpl:
        cat /home/user/QubesIncoming/dispXXX/kali-key.asc | sudo apt-key add -

    The last command should return `OK` on a line by itself.

5. Update the system:

        # in kali-tpl:
        sudo -s
        apt-get update && apt-get dist-upgrade

6. Shut down the `kali-tpl` template:

        # in dom0:
        qvm-shutdown kali-tpl

### Install the Kali tools

At this point you should have a working template and you can install the tools you need.

1. [resize the template] if you plan on installing the full Kali distribution. For example to install `kali-linux-full` you must **grow** the size of the VM system from 10Gb to at least 20Gb.

1. Install Kali linux:

        # in kali-tpl:
        sudo apt-get install kali-linux-full

2. Enjoy and don't forget to back up your appVMs as [audio CDs].


Installing via third-party scripts: Katoolin
--------------------------------------------

If you do not want to modify the `sources.list` file and add the signing keys
yourself, alternatively you can use [KATOOLIN] after cloning the Debian
Template.

You should probably inspect the script and make sure it does what you want
before trusting it blindly.


Alternative Options to Kali
===========================

 * PenTester Framework: [PTF]

Notes
-----

Thanks to the people in [the discussion thread].


[kali]: https://www.kali.org/
[kali website]: https://docs.kali.org/introduction/download-official-kali-linux-images.
[KATOOLIN]: http://www.tecmint.com/install-kali-linux-tools-using-katoolin-on-ubuntu-debian/ 
[the debian-8 template]: https://www.qubes-os.org/doc/templates/debian/
[PTF]: https://www.trustedsec.com/may-2015/new-tool-the-pentesters-framework-ptf-released/
[audio CDs]: https://www.reddit.com/r/Nirvana/comments/3hmra1/the_main_character_in_the_tv_show_mr_robot_has_a/
[resize the template]: https://www.qubes-os.org/doc/resize-disk-image/
[the Debian wiki]: https://wiki.debian.org/Qubes#Install_Debian_Templates
[the discussion thread]: https://github.com/QubesOS/qubes-issues/issues/1981
