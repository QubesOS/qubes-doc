---
layout: doc
title: How to make any file in a TemplateBasedVM persistent using bind-dirs
permalink: /doc/bind-dirs/
redirect_from:
- /en/doc/bind-dirs/
---

# How to make any file in a TemplateBasedVM persistent using bind-dirs #

## What is bind-dirs.sh? ##

With [bind-dirs.sh](https://github.com/QubesOS/qubes-core-agent-linux/blob/master/vm-systemd/bind-dirs.sh)
you can make arbitrary files or folders persistent in TemplateBasedVMs.

## What is it useful for? ##

For example, it is useful for Whonix, sys-whonix, where [Tor's data dir /var/lib/tor has been made persistent in the TemplateBased ProxyVM sys-whonix](https://github.com/Whonix/qubes-whonix/blob/8438d13d75822e9ea800b9eb6024063f476636ff/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf#L5). So sys-whonix does not require to be a StandaloneVM. And therefore can benefit from the Tor anonymity feature 'persistent Tor entry guards' without the overhead of a StandaloneVM.

## Minimum Qubes Version ##

bind-dirs.sh works with Qubes R3.2 and above.

## How to use bind-dirs.sh? ##

Inside your TemplateBasedVM.

1. Make sure folder `/rw/config/qubes-bind-dirs.d` exists.

       sudo mkdir -p /rw/config/qubes-bind-dirs.d

2. Create a file `/rw/config/qubes-bind-dirs.d/50_user.conf` with root rights inside a VM.

       sudo nano /rw/config/qubes-bind-dirs.d/50_user.conf

3. Append a folder or file to the `binds` variable. In the following example we are using folder `/var/lib/tor`. You can replace that folder with a folder of your choice.

       binds+=( '/var/lib/tor' )
       
In the following example we are using file `/etc/tor/torrc`. You can replace that file with a file of your choice.
       
       binds+=( '/etc/tor/torrc' )

Multiple configuration lines, files and folders supported. For example, you could use both.

       binds+=( '/var/lib/tor' )
       binds+=( '/etc/tor/torrc' )

4. Save.

5. Reboot your TemplateBasedVM.

6. Done.

If you added for example folder `/var/lib/tor` to the `binds` variable, from now any files within that folder would persist reboots. If you added for example file `/etc/tor/torrc` to the `binds` variable, from now any modifications to that file would persist reboots.

## Other Configuration Folders ##

* `/usr/lib/qubes-bind-dirs.d` (lowest priority, for packages)
* `/etc/qubes-bind-dirs.d`  (intermediate priority, for template wide configuration)
* `/rw/config/qubes-bind-dirs.d` (highest priority, for per VM configuration)

## Limitations ##

* Files that exist in the TemplateVM root image cannot be made deleted in the TemplateBasedVMs root image using bind-dirs.sh.
* Does not work if the file / folder in question does not already exist in the root image. I.e. a file that does not exist in the root image cannot be bind mounted in the TemplateBasedVM.
* Re-running `sudo /usr/lib/qubes/bind-dirs.sh` without previous `sudo /usr/lib/qubes/bind-dirs.sh umount` does not work.
* Running `sudo /usr/lib/qubes/bind-dirs.sh umount` after boot (before shutdown) is probably not sane and nothing can be done about that.

## How to remove binds from bind-dirs.sh? ##

`binds` is actually just a bash variable (an array) and the bind-dirs.sh configuration folders are `source`d as bash snippets in lexical order. Therefore if you wanted to remove an existing entry from the `binds` array, you could do that by using a lexically higher configuration file. For example, if you wanted to make `/var/lib/tor` non-persistent in `sys-whonix` without manually editing [`/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf`](https://github.com/Whonix/qubes-whonix/blob/master/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf), you could use the following.

`/rw/config/qubes-bind-dirs.d/50_user.conf`

~~~
binds=( "${binds[@]/'/var/lib/tor'}" )
~~~

(Editing `/usr/lib/qubes-bind-dirs.d/40_qubes-whonix.conf` directly is recommended against, since such changes get lost when that file is changed in the package on upgrades.)

## Discussion ##

[TemplateBasedVMs: make selected files and folders located in the root image persistent- review bind-dirs.sh](https://groups.google.com/forum/#!topic/qubes-devel/tcYQ4eV-XX4/discussion)

