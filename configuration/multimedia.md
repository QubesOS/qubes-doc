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
Note: This Howto has been written and was tested under Qubes 4rc4

You can consolidate most of your media streaming tasks into one "multimedia" App-VM. This howto explains how to create a multimedia temmplate which can be used to play multimedia content.
This includes:

- Spotify
- Amazon Prime
- Netflix
- DVDs

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

Become the root user to run all following command without the need to use sudo in the multimedia template VM

`sudo -i`


Installation of Spotify
-----------------------

Import GPG-Key for spotify
As the template VM can't connect to internet you need to get the public key file from another AppVM and copy it to the template VM. The easiest way is to use the Qubes Clipboard to copy the keys from the AppVM where you get the key to the Template VM.

In an AppVM which has Internet access:
- Open http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0xEFDC8610341D9410
- Copy content of page to the Qubes Clipboard (Ctrl+C and then Shift+Ctrl+C)

Switch to the gnome terminal in the Multimedia Template VM

`nano spotify.pubkey`

Paste the content from the Qubes Clipboard into nano (Shift+Ctrl+V and then Paste)
Save the file (Ctrl+O <Enter> Ctrl+X)

Add the public key to the repository keyring
`apt-key add spotify.pubkey`

Verify Fingerprint with
`apt-key finger spotify`
You can (and should) lookup the fingerprint on the keyserver:
http://keyserver.ubuntu.com:11371/pks/lookup?op=vindex&search=0xEFDC8610341D9410&fingerprint=on

Add the Spotify repository to your list of package sources:
`echo deb http://repository.spotify.com stable non-free > /etc/apt/sources.list.d/spotify.list`

Update the list of all known packages
`apt-get update`

Install Spotify
`apt-get install -y spotify-client`

Create a spotify desktop-entry

`cp -p /usr/share/spotify/spotify.desktop /usr/share/applications/`
`cp /usr/share/spotify/icons/spotify-linux-16.png /usr/share/icons/hicolor/16x16/apps/spotify.png`

Installation of VLC
-------------------

To play DVDs you can install VLC with the needed Codecs

Download the public key which signs the VLC package repositories
In an AppVM which has Internet access:
- Open http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x6BCA5E4DB84288D9
- Copy content of page to the Qubes Clipboard (Ctrl+C and then Shift+Ctrl+C)

Switch to the gnome terminal in the Multimedia Template VM

`nano vlc.pubkey`

Paste the content from the Qubes Clipboard into nano (Shift+Ctrl+V and then Paste)
Save the file (Ctrl+O <Enter> Ctrl+X)

Add the public key to the repository keyring
`apt-key add vlc.pubkey`

Verify Fingerprint with
`apt-key finger VideoLAN`
You can (and should) lookup the fingerprint on the keyserver:
http://keyserver.ubuntu.com/pks/lookup?op=vindex&search=0xB84288D9&fingerprint=on

Add the new VLC package repositories to your list of sources 
`echo "deb http://download.videolan.org/pub/debian/stable/ /" > /etc/apt/sources.list.d/vlc.list`
`echo "deb-src http://download.videolan.org/pub/debian/stable/ /" >> /etc/apt/sources.list.d/vlc.list`

Update package repositories
`apt-get update`

Install libdvdcss and VLC
`apt-get install -y libdvdcss2 vlc`

Installation Google Chrome
--------------------------

To play Videos with Netflix, Amazon Prime & Co using Chrome is a good option as it has all needed codecs included.
Hint: Using Chromium will not work for some reasons.


Download the public key which signs the Google package repositories
In an AppVM which has Internet access:
- Open http://keys.gnupg.net/pks/lookup?op=get&search=0x7721F63BD38B4796
- Copy content of page to the Qubes Clipboard (Ctrl+C and then Shift+Ctrl+C)

Switch to the gnome terminal in the Multimedia Template VM

`nano google.pubkey`

Paste the content from the Qubes Clipboard into nano (Shift+Ctrl+V and then Paste)
Save the file (Ctrl+O <Enter> Ctrl+X)

Add the public key to the repository keyring
`apt-key add google.pubkey`

Verify Fingerprint with
`apt-key finger Google`
You can (and should) lookup the fingerprint on the keyserver:
http://keys.gnupg.net/pks/lookup?search=0x7721F63BD38B4796&fingerprint=on
or https://www.google.com/linuxrepositories/

Add the Google package repositories to your list of sources 
echo "deb http://dl.google.com/linux/chrome/deb/ stable main"> /etc/apt/sources.list.d/google.list

Update package repositories
`apt-get update`

Install Chrome 
`apt-get install google-chrome-stable`


