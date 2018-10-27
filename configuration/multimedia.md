---
layout: doc
title: How to Make a Multimedia TemplateVM
permalink: /doc/multimedia/
redirect_from:
- /en/doc/multimedia/
- /doc/Multimedia/
- /wiki/Multimedia/
---

How to Make a Multimedia TemplateVM
===================================

Note: This Howto has been written and was tested under Qubes 4rc4

You can consolidate most of your media streaming tasks into one "multimedia" App-VM. This howto explains how to create a multimedia template which can be used to play multimedia content.
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

Launch a Terminal in the new template VM:

`qvm-run --auto t-multimedia gnome-terminal`

Important:
In order to get all applications working, You need to add additional (not trusted) repositories to your template VM.
Therefor this howto will cover how you add those repositories, check GPG signing keys and signature.
VMs which contains packages from other repositories should only be used for specific use case, like in this case beeing able to watching netflix and listen to spotify.
You should _not_ use those VMs to work with your personal data.

As the template VM has only limitied internet connection (to download packages) some files (like the GPG-keys) have to be downloaded in another AppVM and need to be transferred to the multimedia template.
To simplify this, this howto will use an additional package xclip in the template VM.
xclip can be used to copy clipboard content to a file.
You can of course skip the xclip procedure and rely on the Qubes Copy & Paste and create the files and copy the data manually.

You can install xclip via `apt-get install xclip` in the multimedia template VM. make sure to run those command via sudo or from a root terminal (`qvm-run --auto --user root t-multimedia xterm`)


Installation of Spotify
-----------------------

Short description what needs to be done:

1. Get and verify the Spotify GPG Key which is used to sign the packages
2. Add the spotify package repository
3. Install Spotify

Import GPG-Key for spotify
As the template VM can't connect to internet you need to get the public key file from another AppVM and copy it to the template VM. The easiest way is to use the Qubes Clipboard (Shift+Ctrl+C and Shift+Ctrl+V) to copy the keys from the AppVM where you get the key to the Template VM.

In an AppVM which has Internet access:
- Download Spotify GPG Signing Key <https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x931FF8E79F0876134EDDBDCCA87FF9DF48BF1C90>
- Copy content of page to the Clipboard (Ctrl+A and Ctrl+C) and then to Qubes-Clipboard (Ctrl+Shift+C)
- open a Terminal in the TemplateVM and paste the Qubes Clipboard to this VM (Ctrl+Shift+V)
- copy the content of the clipboard to a file using xclip
  `xclip -o > spotify.pubkey` to check if copying the key worked: `cat spotify.pubkey`

Check the signature of the signing key (in the multimedia Template VM):
- To create the gpg directories in a fresh template VM: `gpg --list.keys`
- Show fingerprint: `cat spotify.pubkey | gpg --with-colons --import-options import-show --dry-run --import`
- Verify the signature with other sources

Hint: depending on your installed version of GnuPG the command to show a public might slightly be different.
See [this StackExchange question](https://unix.stackexchange.com/questions/391344/gnupg-command-to-show-key-info-from-file) for more information. You can check the gpg version with `gpg --version`

You can (and should) lookup the fingerprint on at least one (or more) keyservers as the above information might be outdated.
<https://keyserver.ubuntu.com/pks/lookup?op=vindex&search=0x931FF8E79F0876134EDDBDCCA87FF9DF48BF1C90&fingerprint=on>

Add the public key to the repository keyring
`apt-key add spotify.pubkey`

Add the Spotify repository to your list of package sources:

`echo deb http://repository.spotify.com stable non-free > /etc/apt/sources.list.d/spotify.list`

Update the list of all known packages

`apt-get update`

Install Spotify
`apt-get install -y spotify-client`

Create a spotify desktop-entry

- `cp -p /usr/share/spotify/spotify.desktop /usr/share/applications/`
- `cp /usr/share/spotify/icons/spotify-linux-16.png /usr/share/icons/hicolor/16x16/apps/spotify.png`


Installation of VLC
-------------------

To play DVDs you can install VLC with the needed Codecs

Download the public key which signs the VLC package repositories
In an AppVM which has Internet access:
- Open <https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x6BCA5E4DB84288D9>
- Copy content of page to the Clipboard (Ctrl+A and Ctrl+C) and then to Qubes-Clipboard (Ctrl+Shift+C)

Open a Terminal in the TemplateVM and paste the Qubes Clipboard to this VM (Ctrl+Shift+V)
Copy the content of the clipboard to a file using xclip
`xclip -o > vlc.pubkey` to check if copying the key worked: `cat vlc.pubkey`

Check the signature of the signing key (in the multimedia Template VM):
- Show fingerprint: `cat vlc.pubkey | gpg --with-colons --import-options import-show --dry-run --import`
- Verify the signature with other sources

Add the public key to the repository keyring
`apt-key add vlc.pubkey`

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
- Open <https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x7721F63BD38B4796>
- Copy content of page to the Clipboard (Ctrl+A and Ctrl+C) and then to Qubes-Clipboard (Ctrl+Shift+C)

Open a Terminal in the TemplateVM and paste the Qubes Clipboard to this VM (Ctrl+Shift+V)
Copy the content of the clipboard to a file using xclip
`xclip -o > google.pubkey` to check if copying the key worked: `cat google.pubkey`

Check the signature of the signing key (in the multimedia Template VM):
- Show fingerprint: `cat google.pubkey | gpg --with-colons --import-options import-show --dry-run --import`
- Verify the signature with other sources and <https://www.google.com/linuxrepositories/>

Add the public key to the repository keyring
`apt-key add google.pubkey`

Add the new VLC package repositories to your list of sources 

`echo "deb http://dl.google.com/linux/chrome/deb/ stable main"> /etc/apt/sources.list.d/google.list`

Update package repositories

`apt-get update`

Install Chrome

`apt-get install google-chrome-stable`



Create a Multimedia AppVM
-------------------------

The last step is to create a multimedia AppVM (named "my-multimedia" here) based on the new multimedia template.

`qvm-create --template t-multimedia --label red my-multimedia`

