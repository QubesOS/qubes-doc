---
layout: doc
title: Setting default applications; using `qvm-open-in-(d)vm` as a default application
permalink: /doc/default-applications/
redirect_from:
- /en/doc/default-applications/
- /doc/default-applications/
- /wiki/default-applications/
---

# Setting default applications; using `qvm-open-in-(d)vm` as a default application

This how-to contains instructions for setting default applications for different file types and URLs and for opening them by default in a new DispVM or existing VM (by setting `qvm-open-in-(d)vm` as a default application).

These instructions have been tested in Qubes R3.2 running i3 and using Debian-based VMs. It might be easier to accomplish for users of xfce and Thunar. The instructions may need to be modified to work in Fedora-based VMs.

Related documentation: [Using Disposable VMs](https://www.qubes-os.org/doc/dispvm/), [Tips and Tricks: Opening links in your preferred AppVM](https://www.qubes-os.org/doc/tips-and-tricks/#opening-links-in-your-preferred-appvm).



## Setting default applications in Debian-based VMs.

Some default applications can be set (system-wide) with the [Debian Alternatives System](https://wiki.debian.org/DebianAlternatives), noticeably the editor, terminal emulator and (sometimes) the web browser. You do this by running `sudo update-alternatives --config name` with `name` being e.g. `editor`, `x-terminal-alternatives`, (sometimes) `x-www-browser`, `vi`, etc. Other things you can set the default applications for are listed in the directory `/etc/alternatives/`. See `man update-alternatives` for more information about the command.

Since the changes are not saved in the home directory, these changes must be set in a TemplateVM, or they will be reset when the AppVM ist shut down. (Confused? See [Get Started](https://www.qubes-os.org/getting-started/).) All of the following settings are saved to the home directory.

You can also set the default application according to [media (or MIME) types](https://en.wikipedia.org/wiki/Media_type).

Run `mimetype filename` to get the MIME type of that file type. Example:

	$ mimetype some_document.pdf
	some_document.pdf: application/pdf

Run `xdg-mime query default mime-type` to see which application opens this MIME type by default. Example:

	$ xdg-mime query default application/pdf
	evince.desktop

To open a file in its default application run `xdg-open filename`.

**Note:** If `xdg-mime` and/or `xdg-open` is not working as expected [you might need](https://askubuntu.com/questions/779717/xdg-open-stopped-working-since-16-04-upgrade) to install `qvfs-bin`. (This has happend in a debian-8 template updated to debian-unstable. It does not seem to happen in debian-minimal templates.)

To set a new default application for a filetype run `xdg-mime default application.desktop mime-type`. `application.desktop` has to be a [Desktop entry](https://wiki.archlinux.org/index.php/Desktop_entries) in `/usr/source/applications/` or `~/.local/share/applications`. Example:

	$ xdg-mime default zathura-pdf-poppler.desktop application/pdf

`xdg-mime` confirms:

	$ xdg-mime query default application/pdf
	zathura-pdf-poppler.desktop

This setting is usually effective immediately and is written to `~/.local/share/mimeapps.list`, i.e.:

	[Default Applications]
	application/pdf=zathura-pdf-poppler.pdf

See below for a more extensive `mimeapps.list` file.

(If you want to apply this setting for every AppVM of a TemplateVM you need to copy `mimeapps.list` to `/usr/share/applications/` in the TemplateVM)


## Setting `qvm-open-in-(d)vm` as a default application for file types/URLs

Desktop entry files contain, in essence, instructions for executing a command. This turns out to be quite useful in combination with Qubes' [`qvm-open-in-dvm`](https://www.qubes-os.org/doc/vm-tools/qvm-open-in-vm/) and [`qvm-open-in-dvm`](https://www.qubes-os.org/doc/vm-tools/qvm-open-in-dvm/), which open a specified file (or URL) in a new DispVM or in a specific VM, respectively.

By creating a Desktop entry file and setting it as the standard application for one or more MIME types you can configure a VM to open these kind of files in either a DispVM or a specified VM. (Substitute `qvm-open-in-dvm` with  `qvm-open-in-vm vmname` [e.g. `qvm-open-in-vm work`] in any command, file or example below if that is what you want to achieve.)

In the VM(s) you want to run `qvm-open-in-dvm` from (not in the VM you want the file/URL to be opened): Add or edit entries in `~/.local/share/applications/mimeapps.list` so that `qvm-open-in-dvm.desktop` is the default application for the MIME types you specify. You cannot use wildcards in MIME types. Example:

	
	[Default Applications]
	x-scheme-handler/unknown=qvm-open-in-dvm.desktop
	x-scheme-handler/about=qvm-open-in-dvm.desktop
	x-scheme-handler/http=qvm-open-in-dvm.desktop
	x-scheme-handler/https=qvm-open-in-dvm.desktop
	text/html=qvm-open-in-dvm.desktop
	text/xml=qvm-open-in-dvm.desktop
	image/gif=qvm-open-in-dvm.desktop
	image/jpeg=qvm-open-in-dvm.desktop
	image/png=qvm-open-in-dvm.desktop
	application/xhtml+xml=qvm-open-in-dvm.desktop
	application/xml=qvm-open-in-dvm.desktop
	application/vnd.mozilla.xul+xml=qvm-open-in-dvm.desktop
	application/rss+xml=qvm-open-in-dvm.desktop
	application/rdf+xml=qvm-open-in-dvm.desktop
	application/msword=qvm-open-in-dvm.desktop
	application/vnd.oasis.opendocument.spreadsheet=qvm-open-in-dvm.desktop
	application/vnd.oasis.opendocument.text=qvm-open-in-dvm.desktop
	application/pdf=qvm-open-in-dvm.desktop

Still in the VM(s) you want to run `qvm-open-in-dvm` from: You need to create a corresponding `.desktop` file and save it in `/usr/share/applications/` or `~/.local/share/applications/`, depending on what you prefer. Every MIME type assigned to this application in `mimeapps.list` must be listed in the `.desktop` file, but fortunately wildcards can be used for subtypes. Example:

	[Desktop Entry]
	Encoding=UTF-8
	Name=QvmOpenInDVM
	Exec=qvm-open-in-dvm %u
	Terminal=false
	X-MultipleArgs=false
	Type=Application
	Categories=Qubes
	MimeType=x-scheme-handler/*;text/*;application/*;image/*;

Now, whenever a file (or URL) of these MIME types is opened, the will be opened in a new DispVM (unless they are explicitly opened with another application, of course). You can open any such file in a DispVM by executing `xdg-open filename`.

 `qvm-open-in-dvm filename` tells dom0 *that* the file be opened in a new DispVM; `mimeapps.list` on the DispVM determines *how* the file is handled internally by the DispVM. To have these files open in your preferred application *in the DispVM* set up a `mimeapps.list` in that VM like you would in any other VM.
 
 (To apply this setting for every AppVM of a TemplateVM just copy `mimeapps.list` and the `.desktop` file to `/usr/share/applications/` in the TemplateVM. But if your DispVMs are based on the same TemplateVM make sure you override the settings in the DispVM.)
