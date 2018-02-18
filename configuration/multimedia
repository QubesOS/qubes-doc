---
layout: doc
title: Multimedia
permalink: /doc/multimedia/
redirect_from:
- /en/doc/multimedia/
- /doc/Multimedia/
- /wiki/Multimedia/
---

Multimedia
==========

In order to choose Qubes OS as your primary OS it must be able to do all tasks, including playing multimedia content.
This howto explains how to create a multimedia temmplate which can be used to play multimedia content.
This includes:

- Spotify
- Amazon Prime
- Netflix
- DVDs

Hint: This first draft of this howto was written under Qubes OS 3.2 but it should also work for Qubes 4rc4.


Installation
------------

Start by cloning the default debian template in dom0.
Hint:
t-multimedia is just the template VM where we will install all packages.
In the last step we will create an AppVM from this template.

`qvm-clone debian-9 t-multimedia`

As we need to install some package outside of the regular repositories you need to enable networking for the Template VM.

`qvm-prefs --set t-multimedia netvm sys-firewall`

Launch a Terminal in the new template VM:

`qvm-run --auto t-multimedia gnome-terminal`

Important:
Enter all the following commands in the terminal of the template VM

Become the root user to run all follwoing command without the need to use sudo

`sudo -i`

Installation of Spotify
-----------------------

Import GPG-Key for spotify

`apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0DF731E45CE24F27EEEB1450EFDC8610341D9410`

> http://keyserver.ubuntu.com:11371/pks/lookup?op=vindex&search=0xEFDC8610341D9410&fingerprint=on
> UUID: Spotify Public Repository Signing Key <tux@spotify.com>
> Key-ID: 0x341D9410
> Fingerprint=0DF7 31E4 5CE2 4F27 EEEB  1450 EFDC 8610 341D 9410 

Add Spotify repository to package list

`echo deb http://repository.spotify.com stable non-free | tee /etc/apt/sources.list.d/spotify.list`

Update package list

`apt-get update`

Install Spotify from the repositories

`apt-get install -y spotify-client`

Create a spotify desktop-entry

`cp -p /usr/share/spotify/spotify.desktop /usr/share/applications/`
`cp /usr/share/spotify/icons/spotify-linux-16.png /usr/share/icons/hicolor/16x16/apps/spotify.png`


Installation of VLC
-------------------

To play DVDs you can install VLC with the needed Codecs

Add Repository for libdvdcss
(See also: http://www.videolan.org/developers/libdvdcss.html)

Add GPG-Key
`apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8F0845FE77B16294429A79346BCA5E4DB84288D9`

> Public-Key: http://keyserver.ubuntu.com/pks/lookup?op=vindex&search=0xB84288D9&fingerprint=on
> Fingerprint: 8F08 45FE 77B1 6294 429A  7934 6BCA 5E4D B842 88D9 

Add repositories to install VLC and libdvdcss
`echo "deb http://download.videolan.org/pub/debian/stable/ /" >> /etc/apt/sources.list`
`echo "deb-src http://download.videolan.org/pub/debian/stable/ /" >> /etc/apt/sources.list`

Update package repositories
`apt-get update`

Install libdvdcss and VLC
`apt-get install -y libdvdcss2 vlc` 


 
Installation Google Chrome
--------------------------

To play Videos with Netflix, Amazon Prime & Co using Chrome is a good option as it has all needed codecs included.
Hint: Using Chromium will not work for some reasons.


Download Google Chrome package from the Google Debian repository

`wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`

FIXME: Howto verify the debian package or better adding a Google Debian package repository?
Link: https://www.google.com/linuxrepositories/

1st attempt to install the downloaded package

`dpkg -i google-chrome-stable_current_amd64.deb`

Installer will quit with an error message as not all dependencies are met (yet):

> dpkg: dependency problems prevent configuration of google-chrome-stable:
> google-chrome-stable depends on fonts-liberation; however:
> Package fonts-liberation is not installed.
> google-chrome-stable depends on libappindicator1; however:
> Package libappindicator1 is not installed.
> dpkg: error processing package google-chrome-stable (--install):
> dependency problems - leaving unconfigured
> (...)
> Errors were encountered while processing:
> google-chrome-stable

Install the missing dependencies for Google Chrome

`apt-get -f upgrade`

(This will install: fonts-liberation libappindicator1 libdbusmenu-glib4 libdbusmenu-gtk4 libindicator7 libxss1)

After the dependencies are installed rerun package installation of Chrome

`dpkg -i google-chrome-stable_current_amd64.deb`

Clean up the mess and shutdown your multimedia template VM

`rm google-chrome-stable_current_amd64.deb && shutdown -h now`


Create a Multimedia AppVM
-------------------------

After you have created the multimedia AppVM template you can create an AppVM for daily use based on it

`qvm-create --template=t-multimedia --label=orange multimedia`

Add Google Chrome, VLC and Spotify to the AppVM Menu via "add/remove app shortcuts"
