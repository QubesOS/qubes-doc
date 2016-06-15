---
layout: doc
title: How to create a Kali Linux VM
permalink: /doc/kali/
---

How to Create a Kali Linux VM
=============================

This guide will explain how to create your own [Kali] Linux VM as a VM
template. The basic idea is to personalize the template with the tools you need
and then spin up isolated appVMs based on the template.

The steps can be summarised as:

1. Customize a Debian template with the Kali sources
3. Install the Kali tools
4. Use the template to build appVM so that you can maintain isolation between
   e.g. pentesting jobs


**IMPORTANT NOTE** Following the instructions below and in particular installing kali-linux-full will **BREAK YOUR VM**. Don't do it. It needs further investigation. The problem is:

 * Pinning down xorg doesn't allow installing kali-desktop (or something) which prevents kali-*


Steps to build a Kali template
------------------------------


### Get the GPG key

1. You'll need to fetch the Kali GPG key from a dispVM as the template you'll
   build won't have direct internet connectivity unless you enable it from the
   firewall:

        # in the dispVM
        gpg --keyserver hkp://keys.gnupg.net --recv-key 7D8D0BF6
        gpg --list-keys --with-fingerprint 7D8D0BF6 
        gpg --export --armor 7D8D0BF6 > kali.asc

2. Make sure the key ID is the valid one listed on the [Kali website]. Ideally,
   verify the fingerprint through other channels.

Once you have the key, keep the dispVM on as you'll need to copy the key over
to the Kali template.

### Customize the template

1. Install [the debian-8 template] (if not already installed)

2. Clone the debian template and start a terminal in it:

        # from dom0:
        qvm-clone debian-8 kali

3. Add this line to the `/etc/apt/sources.list` file in the template:

        # in the 'kali' template
        sudo -s
        echo 'deb http://http.kali.org/kali kali-rolling main non-free contrib' >> /etc/apt/sources.list

4. Copy the Kali key from the dispVM into the template:

        # in the dispVM
        qvm-copy-to-vm kali kali.asc

        # in the kali template:
        sudo -s
        cat /home/user/QubesIncoming/kali/kali-key.asc | apt-key add -

    The last command should return `OK` on a line by itself.

5. **Pin the X server** into the preferences file: this prevents Kali to installing
   a new X.org server, for which there would be no qubes-tools available:

        # add the following lines  to /etc/apt/preferences (you might have to
        create it)

        Package: xserver-xorg*
        Pin: release a=jessie
        Pin-Priority: 900

        Package: xorg*
        Pin: release a=jessie
        Pin-Priority: 900

5. Update the system:

        sudo apt-get update

6. Now is a good time to stop the template, clone it and see if restarting it
   allows you to run a terminal:

        # from dom0
        qvm-clone kali kali-tools

### Install the Kali tools

At this point you should have a working template and you can install the tools you need.

Don't forget to [resize the template] if you plan on installing the full Kali distribution. For example to install `kali-linux-full` you must **grow** the size of the VM system from 10Gb to at least 20Gb.

1. Install your tools of choice, for example:

        # in the kali-tools template
        sudo apt-get install kali-linux-full

2. If the update process went well, give it a try: shut down the `kali-tools`
   template and create an appVM from it.

3. When you are happy you can probably remove the `kali` template and its
   backup copies; then use only `kali-tools` as a template.


Don't forget to back up your appVMs as [audio CDs].


Troubleshooting
---------------

If the template doesn't start, give it a peek with the console:

    # from dom0
    sudo xl console kali


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



[kali]: https://www.kali.org/
[kali website]: https://docs.kali.org/introduction/download-official-kali-linux-images.
[KATOOLIN]: http://www.tecmint.com/install-kali-linux-tools-using-katoolin-on-ubuntu-debian/ 
[the debian-8 template]: https://www.qubes-os.org/doc/templates/debian/
[PTF]: https://www.trustedsec.com/may-2015/new-tool-the-pentesters-framework-ptf-released/
[audio CDs]: https://www.reddit.com/r/Nirvana/comments/3hmra1/the_main_character_in_the_tv_show_mr_robot_has_a/
[resize the template]: https://www.qubes-os.org/doc/resize-disk-image/
