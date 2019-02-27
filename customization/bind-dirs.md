---
layout: doc
title: How to make any file in a TemplateBasedVM persistent using bind-dirs
permalink: /doc/bind-dirs/
redirect_from:
- /en/doc/bind-dirs/
---

# How to make any file in a TemplateBasedVM persistent using bind-dirs #

## What are bind-dirs? ##

With [bind-dirs](https://github.com/QubesOS/qubes-core-agent-linux/blob/master/vm-systemd/bind-dirs.sh)
any arbitrary files or folders can be made persistent in TemplateBasedVMs.

## What is it useful for? ##

In a TemplateBasedVM all of the file system comes from the template except `/home`, `/usr/local`, and `/rw`.
This means that changes in the rest of the filesystem are lost when the TemplateBasedVM is shutdown.
bind-dirs provides a mechanism whereby files usually taken from the template can be persisted across reboots.

For example, in Whonix, [Tor's data dir /var/lib/tor has been made persistent in the TemplateBased ProxyVM sys-whonix](https://github.com/Whonix/qubes-whonix/blob/8438d13d75822e9ea800b9eb6024063f476636ff/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf#L5). 
In this way sys-whonix can benefit from the Tor anonymity feature 'persistent Tor entry guards' but does not have to be a StandaloneVM.

## Minimum Qubes Version ##

bind-dirs.sh works with Qubes R3.2 and above.

## How to use bind-dirs.sh? ##

Inside your TemplateBasedVM.

1. Make sure folder `/rw/config/qubes-bind-dirs.d` exists.

       sudo mkdir -p /rw/config/qubes-bind-dirs.d

2. Create a file `/rw/config/qubes-bind-dirs.d/50_user.conf` with root rights inside a TemplateBasedVM.

3. Edit the file 50_user.conf to append a folder or file name to the `binds` variable. (In the following example we are using folder `/var/lib/tor`. You can replace that name with a folder or file name of your choice.)

       binds+=( '/var/lib/tor' )

Multiple entries are possible, each on a separate line.

4. Save.

5. Reboot the TemplateBasedVM.

6. Done.

If you added for example folder `/var/lib/tor` to the `binds` variable, from now on any files within that folder will persist reboots. If you added for example file `/etc/tor/torrc` to the `binds` variable, from now on any modifications to that file will persist reboots.

## Other Configuration Folders ##

* `/usr/lib/qubes-bind-dirs.d` (lowest priority, for packages)
* `/etc/qubes-bind-dirs.d`  (intermediate priority, for template wide configuration)
* `/rw/config/qubes-bind-dirs.d` (highest priority, for per VM configuration)

## How does it work? ##

bind-dirs.sh is called on startup of a TemplateBasedVM, and configuration files in the configuration folders above are parsed to build a bash array.
Files or folders identified in the array are copied to /rw/bind-dirs if they do not already exist there, and are then bind mounted over the original files/folders.

Creation of the file and folders in /rw/bind-dirs should be automatic the first time the TemplateBasedVM is restarted after configuration.

If you want to circumvent this process, you can create the relevant filestructure under /rw/bind-dirs and make any changes at the same time that you perform the configuration, before reboot.

## Limitations ##

* Files that exist in the TemplateVM root image cannot be deleted in the TemplateBasedVMs root image using bind-dirs.sh.
* Re-running `sudo /usr/lib/qubes/bind-dirs.sh` without a previous `sudo /usr/lib/qubes/bind-dirs.sh umount` does not work.
* Running `sudo /usr/lib/qubes/bind-dirs.sh umount` after boot (before shutdown) is probably not sane and nothing can be done about that.
* Many editors create a temporary file and copy it over the original file. If you have bind mounted an individual file this will break the mount.
Any changes you make will not survive a reboot. If you think it likely you will want to edit a file, then either include the parent directory in bind-dirs rather than the file, or perform the file operation on the file in /rw/bind-dirs.
* Some files are altered when a qube boots - e.g. `/etc/hosts`. If you try to use bind-dirs on such files you may break your qube in unpredictable ways.

You can add persistent rules to `/etc/hosts` file using script `/rw/config/rc.local` that is designed to override configuration in /etc, starting services and etc. For example, to make software inside some TemplateBasedVM resolving the domain `example.com` as `127.0.0.1` open `/rw/config/rc.local` inside this TemplateBasedVM and add:

~~~
echo '127.0.0.1 example.com' >> /etc/hosts
~~~

After every boot of the TemplateBasedVM `rc.local` script will add line `127.0.0.1 example.com` to `/etc/hosts` file and the software inside the TemplateBasedVM will resolve domain `example.com` accordingly. You cam add several rules to `/etc/hosts` the same way.

## How to remove binds from bind-dirs.sh? ##

`binds` is actually just a bash variable (an array) and the bind-dirs.sh configuration folders are `source`d as bash snippets in lexical order. 
Therefore if you wanted to remove an existing entry from the `binds` array, you could do that by using a lexically higher configuration file. 
For example, if you wanted to make `/var/lib/tor` non-persistant in `sys-whonix` without manually editing [`/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf`](https://github.com/Whonix/qubes-whonix/blob/master/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf), you could use the following.

`/rw/config/qubes-bind-dirs.d/50_user.conf`

~~~
binds=( "${binds[@]/'/var/lib/tor'}" )
~~~

(Editing `/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf` directly is strongly discouraged, since such changes get lost when that file is changed in the package on upgrades.)

## Discussion ##

[TemplateBasedVMs: make selected files and folders located in the root image persistent- review bind-dirs.sh](https://groups.google.com/forum/#!topic/qubes-devel/tcYQ4eV-XX4/discussion)

