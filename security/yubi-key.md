---
layout: doc
title: YubiKey in Qubes
permalink: /doc/yubi-key/
redirect_from:
- /en/doc/yubi-key/
- /doc/YubiKey/
---

Using YubiKey to Qubes authentication
=====================================

You can use YubiKey to enhance Qubes user authentication, for example to mitigate
risk of snooping the password. This can also slightly improve security when you have [USB keyboard](https://github.com/marmarek/qubes-app-linux-input-proxy).

There (at least) two possible configurations: using OTP mode and using challenge-response mode.

OTP mode
--------

This can be configured using
[app-linux-yubikey](https://github.com/adubois/qubes-app-linux-yubikey)
package. This package does not support sharing the same key slot with other
applications (it will deny further authentications if you try).

Contrary to instruction there, currently there is no binary packages in Qubes
repository and you need to compile it yourself. This might change in the future.

Challenge-response mode
----------------------

In this mode, your YubiKey will generate response based on secret key, and
random challenge (instead of counter). This means that it isn't possible to
generate response in advance even if someone gets access to your YubiKey. This
makes it reasonably safe to use the same YubiKey for other services (also in
challenge-response mode).

Same as in OTP case, you will need to set up your YubiKey, choose separate
password (other than your login password!) and apply the configuration.

To use this mode you need to:

1. Configure your YubiKey for challenge-response HMAC-SHA1 mode, for example
   [following this
   tutorial](https://www.yubico.com/products/services-software/personalization-tools/challenge-response/)
2. Install `ykpers` package in template on which your USB VM is based.
3. Create `/usr/local/bin/yubikey-auth` script:

       #!/bin/sh

       key="$1"

       if [ -z "$key" ]; then
           echo "Usage: $0 <AESKEY> [<PASSWORD-HASH>]"
           exit 1
       fi

       # if password has given, verify it
       if [ -n "$2" ]; then
           # PAM appends \0 at the end
           hash=`head -c -1 | openssl dgst -sha1 -r | cut -f1 -d ' '`
           if [ "x$2" != "x$hash" ]; then
               exit 1
           fi
       fi

       challenge=`head -c64 /dev/urandom | xxd -c 64 -ps`
       # You may need to adjust slot number and USB VM name here
       response=`qvm-run -u root --nogui -p sys-usb "ykchalresp -2 -x $challenge"`

       correct_response=`echo $challenge | xxd -r -ps | openssl dgst -sha1 -macopt hexkey:$key -mac HMAC -r | cut -f1 -d ' '`

       test "x$correct_response" = "x$response"
       exit $?

4. Adjust USB VM name (`sys-usb` above), and possibly YubiKey slot number (`2`
   above), then make the script executable.
5. Edit `/etc/pam.d/xscreensaver` (or appropriate file if you are using other
   screen locker program). Add this line at the beginning:

       auth [success=done default=ignore] pam_exec.so expose_authtok quiet /usr/local/bin/yubikey-auth AESKEY PASSWORD-HASH

   Replace `AESKEY` with hex-encoded key configured in the first step, then
   replace `PASSWORD-HASH` with SHA1 hash for your YubiKey-linked password (other
   than your standard Qubes password). You can calculate it using this command:

       echo -n "PASSWORD" | openssl dgst -sha1

### Usage

When you want to unlock your screen, plug YubiKey into USB slot, then enter
password associated with YubiKey. If you configured so, YubiKey will request
confirmation by pressing button on it (it will blink).
When everything is ok, your screen will be unlocked.

In any case you can still use your login password, but do it in a secure location
where no one can snoop your password.

Locking the screen when YubiKey is removed
------------------------------------------

You can setup your system to automatically lock the screen when you unplug
YubiKey. This will require creating a simple qrexec service which will expose
the ability to lock the screen to your USB VM, and then adding udev hook to
actually call that service.

1. First configure the qrexec service. Create `/etc/qubes-rpc/custom.LockScreen` (in dom0)
  with a simple command to lock the screen. In the case of xscreensaver (used in Xfce)
  it would be:

        DISPLAY=:0 xscreensaver-command -lock

2. Allow your USB VM to call that service. Assuming that it's named `sys-usb` it
would require creating `/etc/qubes-rpc/policy/custom.LockScreen` with:

        sys-usb dom0 allow

3. Create udev hook in your USB VM. Store it in `/rw/config` to have it
persistent across VM restarts. For example name the file
`/rw/config/yubikey.rules`. Write there a single line:

        ACTION=="remove", SUBSYSTEM=="usb", ENV{ID_SECURITY_TOKEN}=="1", RUN+="/usr/bin/qrexec-client-vm dom0 custom.LockScreen"

4. Ensure that the udev hook is placed in the right place after VM restart. Append to `/rw/config/rc.local`:

        ln -s /rw/config/yubikey.rules /etc/udev/rules.d/
        udevadm control --reload

  Then make `/rw/config/rc.local` executable. For changes to take effect, you
  need to call this script manually for the first time.

If you use KDE, the command(s) in first step would be different:

        # In the case of USB VM being autostarted, it will not have direct access to D-Bus
        # session bus, so find its address manually:
        kde_pid=`pidof kdeinit4`
        export `cat /proc/$kde_pid/environ|grep -ao 'DBUS_SESSION_BUS_ADDRESS=[[:graph:]]*'`
        qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock
