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
risk of snooping the password. This can also slightly improve security when you have [USB keyboard](/doc/device-handling-security/#security-warning-on-usb-input-devices).

There (at least) two possible configurations: using OTP mode and using challenge-response mode.

OTP mode
--------

This can be configured using
[app-linux-yubikey](https://github.com/adubois/qubes-app-linux-yubikey)
package. This package does not support sharing the same key slot with other
applications (it will deny further authentications if you try).

Contrary to instruction there, currently there is no binary package in the Qubes
repository and you need to compile it yourself. This might change in the future.

Challenge-response mode
----------------------

In this mode, your YubiKey will generate a response based on the secret key, and
random challenge (instead of counter). This means that it isn't possible to
generate a response in advance even if someone gets access to your YubiKey. This
makes it reasonably safe to use the same YubiKey for other services (also in
challenge-response mode).

Same as in the OTP case, you will need to set up your YubiKey, choose a separate
password (other than your login password!) and apply the configuration.

To use this mode you need to:

1. Install yubikey personalization the packages in your TemplateVM on which your USB VM is based.

   For Fedora.

       sudo dnf install ykpers yubikey-personalization-gui

   For Debian.

       sudo apt-get install yubikey-personalization yubikey-personalization-gui

   Shut down your TemplateVM. Then reboot your USB VM (so changes inside the TemplateVM take effect
   in your TemplateBased USB VM or install the packages inside your USB VM if you would like to avoid
   rebooting your USB VM.

2. Configure your YubiKey for challenge-response `HMAC-SHA1` mode, for example
   [following this
   tutorial](https://www.yubico.com/products/services-software/personalization-tools/challenge-response/).

   On Debian, you can run the graphical user interface `yubikey-personalization-gui` from the command line.

   - Choose `configuration slot 2`.
   - It is recommended to enable `Require user input (button press)` but this is optional.
   - Note: Different from the above video, use the following settings select
   `HMAC-SHA1 mode`: `fixed 64 bit input`.
   - We will refer the `Secret Key (20 bytes hex)` as `AESKEY`.
      - It is recommended to keep a backup of your `AESKEY` in an offline VM used as vault.
      - Consider to keep a backup of your `AESKEY` on paper and store it in a safe place.
      - In case you have multiple YubiKeys for backup purposes (in case a yubikey gets lost, stolen or breaks) you can write the same settings into other YubiKeys.

3. Install [qubes-app-yubikey](https://github.com/QubesOS/qubes-app-yubikey) in dom0.

       sudo qubes-dom0-update qubes-yubikey-dom0

4. Adjust USB VM name in case you are using something other than the default
   `sys-usb` by editing `/etc/qubes/yk-keys/yk-vm` in dom0.

5. Paste your `AESKEY` from step 2 into `/etc/qubes/yk-keys/yk-secret-key.hex` in dom0.

6. Paste your hashed password (other than your standard Qubes password)  into
`/etc/qubes/yk-keys/yk-login-pass-hashed.hex` in dom0.

   You can calculate your hashed password using the following two commands.
   First run the following command to store your password in a temporary variable `password`.
   (This way your password will not leak to the terminal command history file.)

       read password
       
   Now run the following command to calculate your hashed password.
       
       echo -n "$password" | openssl dgst -sha1

7. Edit `/etc/pam.d/login` in dom0. Add this line at the beginning:

       auth include yubikey

8. Edit `/etc/pam.d/xscreensaver` (or appropriate file if you are using other
   screen locker program) in dom0. Add this line at the beginning:

        auth include yubikey

9. Edit `/etc/pam.d/lightdm` (or appropriate file if you are using other
   display manager) in dom0. Add this line at the beginning:

        auth include yubikey

### Usage

When you want to unlock your screen...

1) Plug YubiKey into USB slot.
2) Enter password associated with YubiKey.
3) Press Enter.
4) If you configured so, YubiKey will request confirmation by pressing button on it (it will blink).

When everything is ok, your screen will be unlocked.

In any case you can still use your login password, but do it in a secure location
where no one can snoop your password.

### Mandatory YubiKey Login

Edit `/etc/pam.d/yubikey` (or appropriate file if you are using other screen locker program)
and remove `default=ignore` so the line looks like this.

    auth [success=done] pam_exec.so expose_authtok quiet /usr/bin/yk-auth

Locking the screen when YubiKey is removed
------------------------------------------

You can setup your system to automatically lock the screen when you unplug your
YubiKey. This will require creating a simple qrexec service which will expose
the ability to lock the screen to your USB VM, and then adding a udev hook to
actually call that service.

In dom0:

1. First configure the qrexec service. Create `/etc/qubes-rpc/custom.LockScreen`
  with a simple command to lock the screen. In the case of xscreensaver (used in Xfce)
  it would be:

        DISPLAY=:0 xscreensaver-command -lock

2. Allow your USB VM to call that service. Assuming that it's named `sys-usb` it
would require creating `/etc/qubes-rpc/policy/custom.LockScreen` with:

        sys-usb dom0 allow

In your USB VM:

3. Create udev hook. Store it in `/rw/config` to have it
persist across VM restarts. For example name the file
`/rw/config/yubikey.rules`. Add the following line:

        ACTION=="remove", SUBSYSTEM=="usb", ENV{ID_SECURITY_TOKEN}=="1", RUN+="/usr/bin/qrexec-client-vm dom0 custom.LockScreen"

4. Ensure that the udev hook is placed in the right place after VM restart. Append to `/rw/config/rc.local`:

        ln -s /rw/config/yubikey.rules /etc/udev/rules.d/
        udevadm control --reload

5. Then make `/rw/config/rc.local` executable.

        sudo chmod +x /rw/config/rc.local

6. For changes to take effect, you need to call this script manually for the first time.

        sudo /rw/config/rc.local

If you use KDE, the command(s) in first step would be different:

        # In the case of USB VM being autostarted, it will not have direct access to D-Bus
        # session bus, so find its address manually:
        kde_pid=`pidof kdeinit4`
        export `cat /proc/$kde_pid/environ|grep -ao 'DBUS_SESSION_BUS_ADDRESS=[[:graph:]]*'`
        qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock
