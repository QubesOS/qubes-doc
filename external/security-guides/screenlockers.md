---
layout: doc
title: Screenlockers
permalink: /doc/screenlockers/
---

# Custom screenlockers in Qubes OS

## Security Considerations

Most people use screenlockers on a daily basis to prevent unauthorized access to their computers during
e.g. coffee breaks. The screen lock functionality is thereby often part of a screensaver.
Qubes OS uses `xscreensaver' for that.

While screenlockers cannot be assumed to withstand serious attacks, most users likely assume that
they cannot be bypassed within very little time. They also assume that screenlockers don't tend to
fail after a while.  
Unfortunately both of these assumptions usually don't hold:

- If one of the parent processes of a screenlocker (e.g. the X server) dies or restarts unexpectedly, the
  screen locker will die and leave the screen unprotected. X server restarts may happen with various graphic
  driver bugs, e.g. on something as simple as plugging a laptop into a docking station with a monitor.
- Screenlockers [tend to have bugs](https://www.jwz.org/blog/2015/04/i-told-you-so-again/) or
  [bad/outdated design](http://blog.martin-graesslin.com/blog/2015/01/why-screen-lockers-on-x11-cannot-be-secure/).
- Other applications may request the screenlocker to be cleared or otherwise display
  information [in front of the screenlocker window](https://github.com/QubesOS/qubes-issues/issues/5908).

The default Qubes OS `xscreensaver` also suffers from these issues, but at least has high hardware coverage.
The Qubes OS design also helps to limit the scope of some of these issues (e.g. only dom0 applications can
request the screensaver to quit).

In general it is _not_ advisable to rely on screenlocker security for anything serious.

See [qubes-issues](https://github.com/QubesOS/qubes-issues/issues/1917) for further discussions.

## Configuring a custom screenlocker

Qubes OS can be configured to use whatever screenlocker you prefer.

Thanks to `xss-lock` and `xflock4` (by default started via `/etc/xdg/autostart/xfce4-xss-lock.desktop`)
the below screenlockers should work right after their installation in dom0:

- `xscreensaver-command -lock`
- `gnome-screensaver-command --lock`
- `xlock -mode blank`
- `slock`

If you have multiple screenlockers installed, you might have to remove the others first.

For other screenlockers you have to use the following dom0 command to enable them:

```
xfconf-query -c xfce4-session -p /general/LockCommand -s "[command to start your screenlocker]" --create -t string
```

Set an empty command to disable them.

## Physlock

[physlock](https://github.com/muennich/physlock) is an interesting screenlocker alternative as it simply uses the
tty logon mechanism as screen locking mechanism. It does not depend on the X server and is therefore not affected by
unexpected X server restarts.

The below instructions provide an example of how to install and configure a non-default screenlocker.

### Installation

1. Install its build dependencies in dom0: `sudo qubes-dom0-update gcc make pam-devel systemd-devel`
2. Download the [physlock source code](https://github.com/muennich/physlock), verify its tag signatures
   and copy it to dom0.
3. Follow the build and install instructions of its [README](https://github.com/muennich/physlock/blob/master/README.md).
4. In particular make sure to follow its PAM-related instructions (if you run into an endless `authentication failed`
   loop on locking later, you likely forgot this point).

### Configuration

1. physlock uses the dom0 root password for unlocking, i.e. you'll have to set one with `sudo passwd`.
2. Create a helper script at `/usr/bin/screenlock`:
   ```
   #!/bin/bash

   function isRunning {
   pgrep -a '^physlock$'
   }

   #parse args
   keep_open=1
   if [[ "$1" == "--keep-open" ]] ; then
	   keep_open=0
	   shift
   fi

   #NOTE: for some sreason the full path is required below for xss-lock
   isRunning || { /usr/local/bin/physlock -dms "$@" ; sleep 1 ; }

   #Idea:
   #make xss-lock think that it controls the screenlocker, but in fact it doesn't
   #reason: xss-lock may crash and we don't want it to take down the screen lock
   if [ $keep_open -eq 0 ] ; then
	   stime=10
	   while isRunning ; do
		   echo "Sleeping for ${stime}s..."
		   sleep $stime
	   done
   fi
   exit 0
   ```
3. Make it executable with `chmod +x /usr/bin/screenlock`.
4. Make sure `/etc/xdg/autostart/xfce4-xss-lock.desktop` exists with `xss-lock xflock4` (does exist by default in Qubes OS 4).
5. As regular user, run `xfconf-query -c xfce4-session -p /general/LockCommand -s "/usr/bin/screenlock --keep-open" --create -t string` in dom0.
6. If you need audio during the screen lock, run `sudo usermod -a -G audio [your user]`.

You can then use the command `screenlock` for custom hotkeys etc.

To set the screenlocker timeout, use the xfce GUI or `xset`.

For example you could create `/etc/xdg/autostart/xset.desktop` with the following content to set a timeout of 610s on startup:
```
[Desktop Entry]
Name=xset
Comment=Set screensaver timeout
Exec=bash -c 'sleep 60 && xset s 610'
Terminal=false
Type=Application
StartupNotify=false
```
