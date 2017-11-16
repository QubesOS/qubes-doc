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
risk of snooping the password. This can also slightly improve security when you have [USB keyboard](https://www.qubes-os.org/doc/usb/#security-warning-about-usb-input-devices).

There (at least) two possible configurations: using OTP mode and using challenge-response mode.

OTP mode
--------

This can be configured using
[app-linux-yubikey](https://github.com/adubois/qubes-app-linux-yubikey)
package. This package does not support sharing the same key slot with other
applications (it will deny further authentications if you try).

Contrary to instruction there, currently there is no binary packages in Qubes
repository and you need to compile it yourself. This can change in the future.

Challenge-reponse mode
----------------------

In this mode, your YubiKey will generate response based on secret key, and
random challenge (instead of counter). This means that it isn't possible to
generate response in advance even when someone get access to your YubiKey. This
makes reasonably safe to use the same YubiKey for other services (also in
challenge-response mode).

Same as in OTP case, you will need to setup your YubiKey, choose separate
password (other than your login password!) and apply the configuration.

To use this mode you need:
   
1. Install yubikey personalization the packages in your TemplateVM on which your USB VM is based.

   For Fedora.

       sudo dnf install ykpers yubikey-personalization-gui

   For Debian.

       sudo apt-get install yubikey-personalization yubikey-personalization-gui
       
   Shut down your TempalteVM. Then reboot your USB VM (so changes inside the TemplateVM take effect
   in your TemplateBased USB VM or install the packages inside your USB VM if you would like to avoid
   rebooting your USB VM.
       
2. Configure your YubiKey for challenge-reponse `HMAC-SHA1` mode, for example
   [following this
   tutorial](https://www.yubico.com/products/services-software/personalization-tools/challenge-response/).
   
   On Debian, you can run the graphical user interface `yubikey-personalization-gui` from the command line.
   
   - Choose `configuration slot 2`.
   - It is recommended to enable `Require user input (button press)` but this is optional.
   - Note: Derivating from the above video, use the following settings select
   `HMAC-SHA1 mode`: `fixed 64 bit input`. 
   - We will refer the `Secret Key (20 bytes hex)` as `AESKEY`. It is recommended to keep a backup of
   your `AESKEY` in an offline VM used as vault. In case you have multiple yubikeys for backup purposes
   (in case a yubikey gets lost, stolen or breaks) you can write the same settings into other yubikeys.

3. Install [qubes-app-yubikey](https://github.com/QubesOS/qubes-app-yubikey) in dom0.

       sudo qubes-dom0-update qubes-dom0-yubikey

4. Adjust USB VM name in case you are using something other than the default
   `sys-usb` by editing `/etc/qubes/yk-keys/yk-vm` in dom0.

5. Paste your `AESKEY` from step 2 into `/etc/qubes/yk-keys/yk-secret-key.hex` in dom0.

6. Paste your hashed password (other than your standard Qubes password)  into
`/etc/qubes/yk-keys/yk-login-pass-hashed.hex` in dom0.

   You can calculate your hashed password using this command:

       echo -n "PASSWORD" | openssl dgst -sha1
       
   (Replace `PASSWORD` with your actual password.)

7. Create `/etc/pam.d/yubikey` (or appropriate file if you are using other
   screen locker program) in dom0. Add this line at the beginning:

       auth [success=done default=ignore] pam_exec.so expose_authtok quiet /usr/bin/yk-auth

9. Edit `/etc/pam.d/login` in dom0. Add this line at the beginning:

       auth include yubikey

10. Edit `/etc/pam.d/xscreensaver` (or appropriate file if you are using other
   screen locker program) in dom0. Add this line at the beginning:

       auth include yubikey

11. Edit `/etc/pam.d/lightdm` (or appropriate file if you are using other
   display manager) in dom0. Add this line at the beginning:

       auth include yubikey

### Usage

When you want to unlock your screen...

1) Plug YubiKey into USB slot.
2) Enter password associated with YubiKey.
3) Press Enter.
4) If you configured so, YubiKey will request confirmation by pressing button on it (it will blink).

When everything is ok, your screen will be unlocked.

In any case you can still use your login password, but do it in secure location
where no one can snoop your password.

### Mandatory YubiKey Login

Edit `/etc/pam.d/yubikey` (or appropriate file if you are using other screen locker program)
and remove `default=ignore` so the line looks like this.

    auth [success=done] pam_exec.so expose_authtok quiet /usr/bin/yk-auth

Locking the screen when YubiKey is removed
------------------------------------------

You can setup your system to automatically lock the screen when you unplug
YubiKey. This will require creating simple qrexec service which will expose
ability to lock the screen to your USB VM, and then adding udev hook to
actually call that service.

In dom0:

1. First configure the qrexec service. Create `/etc/qubes-rpc/custom.LockScreen`
  with simple command to lock the screen. In case of xscreensaver (used in Xfce)
  it would be:

        DISPLAY=:0 xscreensaver-command -lock

2. Allow your USB VM to call that service. Assuming that its named `sys-usb` it
would require creating `/etc/qubes-rpc/policy/custom.LockScreen` with:

        sys-usb dom0 allow

In your USB VM:

3. Create udev hook. Store it in `/rw/config` to have it
persistent across VM restarts. For example name the file
`/rw/config/yubikey.rules`. Write there single line:

        ACTION=="remove", SUBSYSTEM=="usb", ENV{ID_SECURITY_TOKEN}=="1", RUN+="/usr/bin/qrexec-client-vm dom0 custom.LockScreen"

4. Ensure that the udev hook is placed in the right place after VM restart. Append to `/rw/config/rc.local`:

        ln -s /rw/config/yubikey.rules /etc/udev/rules.d/
        udevadm control --reload

5. Then make `/rw/config/rc.local` executable.

        sudo chmod +x /rw/config/rc.local
  
6. For changes to take effect, you need to call this script manually for the first time.

        sudo /rw/config/rc.local

If you use KDE, the command(s) in first step would be different:

        # In case of USB VM being autostarted, it will not have direct access to D-Bus
        # session bus, so find its address manually:
        kde_pid=`pidof kdeinit4`
        export `cat /proc/$kde_pid/environ|grep -ao 'DBUS_SESSION_BUS_ADDRESS=[[:graph:]]*'`
        qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock
