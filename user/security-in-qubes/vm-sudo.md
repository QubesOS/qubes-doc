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

The background to passswordless root access is summarised in this statement, that used to be found at `/etc/sudoers.d/qubes` in each qube:

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
The core of this statement continues to reflect the views of the Qubes developers.

Passwordless root is provided by the `qubes-core-agent-passwordless-root` package.  
Details of the implementation are [here](/doc/vm-sudo-implementation).

[Minimal templates](/doc/templates/minimal/), which are intended for use by advanced users, do not have this package installed by default.

Replacing passwordless root access
----------------------------------

Some users may wish to modify their system by enabling user/root isolation in qubes.  
We do not support this in any packages, but users are free to remove the qubes-core-agent-passwordless-root package if they wish, using standard packaging tools.

Root access can then be gained from dom0 by (e.g) `qvm-run -u root QUBE qubes-run-terminal`, or `qvm-console-dispvm QUBE`.

Replacing passwordless root access with Dom0 user prompt
--------------------------------------------------------

An alternative approach is to enable user/root isolation by using a dom0 generated prompt.  
A list of steps to do so is provided in the [Qubes community guide, Replacing passwordless root with a dom0 prompt](https://forum.qubes-os.org/t/replacing-passwordless-root-with-a-dom0-prompt/19074) **without any guarantee of safety, accuracy, or completeness.
Proceed at your own risk.
Do not rely on this for extra security.**

Dom0 passwordless root access
-----------------------------

There is also passwordless user->root access in dom0.  
As stated in the comment in `/etc/sudoers.d/qubes` there is really no point in user/root isolation in dom0, because all user data (and the whole Qubes management interface) is already accessible to the user, so there is nothing more to be gained from the dom0 root account.
