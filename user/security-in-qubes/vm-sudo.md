---
lang: en
layout: doc
permalink: /doc/vm-sudo/
redirect_from:
- /en/doc/vm-sudo/
- /doc/VMSudo/
- /wiki/VMSudo/
ref: 165
title: Passwordless root access in qubes
---

Background (`/etc/sudoers.d/qubes` in VM):

Undocumented. See github issue [Automate vm sudo authorization setup](https://github.com/QubesOS/qubes-issues/issues/2695) for history and future plans.

Below is a complete list of configuration made according to the above statement, with (not necessary complete) list of mechanisms depending on each of them:

1. sudo (`/etc/sudoers.d/qubes`):

    ```
    user ALL=(ALL) NOPASSWD: ALL
    (...)
    ```

    - Easy user -> root access (main option for the user).
    - `qvm-usb` (not really working, as of R2).

2. PolicyKit (`/etc/polkit-1/rules.d/00-qubes-allow-all.rules`):

    ```
    //allow any action, detailed reasoning in sudoers.d/qubes
    polkit.addRule(function(action,subject) { return polkit.Result.YES; });
    ```

    and `/etc/polkit-1/localauthority/50-local.d/qubes-allow-all.pkla`:

    ```
    [Qubes allow all]
    Identity=*
    Action=*
    ResultAny=yes
    ResultInactive=yes
    ResultActive=yes
    ```

    - NetworkManager configuration from normal user (`nm-applet`).
    - Updates installation (`gpk-update-viewer`).
    - User can use pkexec just like sudo Note: above is needed mostly because Qubes user GUI session isn't treated by PolicyKit/logind as "local" session because of the way in which X server and session is started.
      Perhaps we will address this issue in the future, but this is really low priority.
      Patches welcomed anyway.

3. Empty root password:
    - Used for access to 'root' account from text console (`qvm-console-dispvm`) - the only way to access the VM when GUI isn't working.
    - Can be used for easy 'su -' from user to root.

Replacing passwordless root access with Dom0 user prompt
--------------------------------------------------------

While the Qubes developers support the statement above, some Qubes users may wish to enable user/root isolation in VMs anyway.
We do not support this in any of our packages, but of course nothing is preventing a user from modifying his or her own system.
A list of steps to do so is provided in the [Qubes community guide, Replacing passwordless root with a dom0 prompt
](https://forum.qubes-os.org/t/replacing-passwordless-root-with-a-dom0-prompt/19074) **without any guarantee of safety, accuracy, or completeness.
Proceed at your own risk.
Do not rely on this for extra security.**

Dom0 passwordless root access
-----------------------------

There is also passwordless user->root access in dom0.
As stated in the comment in sudo configuration there (which is different from the one in individual qubes), there is really no point in user/root isolation, because all the user data (and VM management interface) is already accessible from dom0 user level, so there is nothing more to get from dom0 root account.
