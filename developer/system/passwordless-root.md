---
lang: en
layout: doc
permalink: /doc/passwordless-root/
redirect_from:
- /doc/vm-sudo/
- /en/doc/vm-sudo/
- /doc/VMSudo/
- /wiki/VMSudo/
ref: 165
title: Passwordless root
---

In certain parts of Qubes OS, root access (such as the use of the `sudo` command) can be obtained without having to provide a password. This is an intentional design decision. This page explains the rationale for that decision, as well as technical aspects associated with it.

## Background

Historically, there was a file called `/etc/sudoers.d/qubes` in Qubes VMs with the following content:

```
user ALL=(ALL) NOPASSWD: ALL

# WTF?! Have you lost your mind?!
#
# In Qubes VMs there is no point in isolating the root account from
# the user account. This is because all the user data is already
# accessible from the user account, so there is no direct benefit for
# the attacker if she could escalate to root (there is even no benefit
# in trying to install some persistent rootkits, as the VM's root
# filesystem modifications are lost upon each start of a VM).
#
# One might argue that some hypothetical attacks against the
# hypervisor or the few daemons/backends in Dom0 (so VM escape
# attacks) most likely would require root access in the VM to trigger
# the attack.
#
# That's true, but mere existence of such a bug in the hypervisor or
# Dom0 that could be exploited by a malicious VM, no matter whether
# requiring user, root, or even kernel access in the VM, would be
# FATAL. In such situation (if there was such a bug in Xen) there
# really is no comforting that: "oh, but the mitigating factor was
# that the attacker needed root in VM!" We're not M$, and we're not
# gonna BS our users that there are mitigating factors in that case,
# and for sure, root/user isolation is not a mitigating factor.
#
# Because, really, if somebody could find and exploit a bug in the Xen
# hypervisor -- as of 2016, there have been only three publicly disclosed
# exploitable bugs in the Xen hypervisor from a VM -- then it would be
# highly unlikely if that person couldn't also found a user-to-root
# escalation in VM (which as we know from history of UNIX/Linux
# happens all the time).
#
# At the same time allowing for easy user-to-root escalation in a VM
# is simply convenient for users, especially for update installation.
#
# Currently this still doesn't work as expected, because some idotic
# piece of software called PolKit uses own set of policies. We're
# planning to address this in Beta 2. (Why PolKit is an idiocy? Do a
# simple experiment: start 'xinput test' in one xterm, running as
# user, then open some app that uses PolKit and asks for root
# password, e.g.  gpk-update-viewer -- observe how all the keystrokes
# with root password you enter into the "secure" PolKit dialog box can
# be seen by the xinput program...)
#
# joanna.
```

## Configuration changes

Below is a complete list of configuration changes made according to the above statement, with a (not necessarily complete) list of mechanisms depending on each of them:

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


## Replacing passwordless root with a dom0 prompt

See [here](https://github.com/Qubes-Community/Contents/blob/master/docs/security/replacing-passwordless-root-with-dom0-prompt.md).


## Passwordless root in dom0

There is also passwordless root access in dom0. As explained in the comment in dom0's sudo configuration (in `/etc/sudoers.d/qubes`, which is different from the one in domUs), there is really no point to having user/root separation in dom0, because all the user data (and VM management interface) is already accessible from the user level in dom0, so there is nothing more to be obtained from gaining root access in dom0.
