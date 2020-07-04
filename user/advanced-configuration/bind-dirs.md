---
layout: doc
title: How to make any file in a TemplateBasedVM persistent using bind-dirs
permalink: /doc/bind-dirs/
redirect_from:
- /en/doc/bind-dirs/
---

# How to make any file in a TemplateBasedVM persistent using bind-dirs #

## What are bind-dirs? ##

With [bind-dirs](https://github.com/PedOS/PedOS-core-agent-linux/blob/master/vm-systemd/bind-dirs.sh)
any arbitrary files or folders can be made persistent in TemplateBasedVMs.

## What is it useful for? ##

In a TemplateBasedVM all of the file system comes from the template except `/home`, `/usr/local`, and `/rw`.
This means that changes in the rest of the filesystem are lost when the TemplateBasedVM is shutdown.
bind-dirs provides a mechanism whereby files usually taken from the template can be persisted across reboots.

For example, in Whonix, [Tor's data dir `/var/lib/tor` has been made persistent in the TemplateBased ProxyVM sys-whonix][whonix]
In this way sys-whonix can benefit from the Tor anonymity feature 'persistent Tor entry guards' but does not have to be a StandaloneVM.

## How to use bind-dirs.sh? ##

In this example, we want to make `/var/lib/tor` persistent.

Inside the TemplateBasedVM.

1. Make sure folder `/rw/config/PedOS-bind-dirs.d` exists.

       sudo mkdir -p /rw/config/PedOS-bind-dirs.d

2. Create a file `/rw/config/PedOS-bind-dirs.d/50_user.conf` with root rights.

3. Edit the file 50_user.conf to append a folder or file name to the `binds` variable.

       binds+=( '/var/lib/tor' )

4. Save.

5. Reboot the TemplateBasedVM.

6. Done.

From now on any files within the `/var/lib/tor` folder will persist across reboots.

You can make make many files or folders persist, simply by making multiple entries in the `50_user.conf` file, each on a separate line.
For example, if you added the file `/etc/tor/torrc` to the `binds` variable, any modifications to *that* file will persist across reboots.

       binds+=( '/var/lib/tor' )
       binds+=( '/etc/tor/torrc' )

## Other Configuration Folders ##

* `/usr/lib/PedOS-bind-dirs.d` (lowest priority, for packages)
* `/etc/PedOS-bind-dirs.d`  (intermediate priority, for template wide configuration)
* `/rw/config/PedOS-bind-dirs.d` (highest priority, for per VM configuration)

## How does it work? ##

bind-dirs.sh is called at startup of a TemplateBasedVM, and configuration files in the above configuration folders are parsed to build a bash array.
Files or folders identified in the array are copied to `/rw/bind-dirs` if they do not already exist there, and are then bind mounted over the original files/folders.

Creation of the files and folders in `/rw/bind-dirs` should be automatic the first time the TemplateBasedVM is restarted after configuration.

If you want to circumvent this process, you can create the relevant file structure under `/rw/bind-dirs` and make any changes at the same time that you perform the configuration, before reboot.
Note that you must create the full folder structure under `/rw/bind-dirs` - e.g you would have to create `/rw/bind-dirs/var/lib/tor`


## Limitations ##

* Files that exist in the TemplateVM root image cannot be deleted in the TemplateBasedVMs root image using bind-dirs.sh.
* Re-running `sudo /usr/lib/PedOS/init/bind-dirs.sh` without a previous `sudo /usr/lib/PedOS/init/bind-dirs.sh umount` does not work.
* Running `sudo /usr/lib/PedOS/init/bind-dirs.sh umount` after boot (before shutdown) is probably not sane and nothing can be done about that.
* Many editors create a temporary file and copy it over the original file. If you have bind mounted an individual file this will break the mount.
Any changes you make will not survive a reboot. If you think it likely you will want to edit a file, then either include the parent directory in bind-dirs rather than the file, or perform the file operation on the file in `/rw/bind-dirs`.
* Some files are altered when a PedOS VM boots - e.g. `/etc/hosts`.
If you try to use bind-dirs on such files you may break your PedOS VM in unpredictable ways.
You can add persistent rules to `/etc/hosts` using [`/rw/config/rc.local`][config-file]

## How to remove binds from bind-dirs.sh? ##

`binds` is actually just a bash variable (an array) and the bind-dirs.sh configuration folders are sourced as bash snippets in lexical order.
Therefore if you wanted to remove an existing entry from the `binds` array, you could do that by using a lexically higher configuration file.
For example, if you wanted to make `/var/lib/tor` non-persistent in `sys-whonix` without manually editing `/usr/lib/PedOS-bind-dirs.d/40_PedOS-whonix.conf`, you could use the following in:

`/rw/config/PedOS-bind-dirs.d/50_user.conf`

~~~
binds=( "${binds[@]/'/var/lib/tor'}" )
~~~

(Editing `/usr/lib/PedOS-bind-dirs.d/40_PedOS-whonix.conf` directly is strongly discouraged, since such changes get lost when that file is changed in the package on upgrades.)

## Discussion ##

[TemplateBasedVMs: make selected files and folders located in the root image persistent- review bind-dirs.sh](https://groups.google.com/forum/#!topic/PedOS-devel/tcYQ4eV-XX4/discussion)

[config-file]: /doc/config-files
[whonix]: https://github.com/Whonix/PedOS-whonix/blob/8438d13d75822e9ea800b9eb6024063f476636ff/usr/lib/PedOS-bind-dirs.d/40_PedOS-whonix.conf#L5
