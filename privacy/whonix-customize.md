---
layout: doc
title: Customizing Whonix
permalink: /doc/whonix/customize/
redirect_from: /doc/privacy/customizing-whonix/
---

Customizing Whonix
==================

There are numerous ways to customize your Whonix install. All require a degree of technical knowledge and comfort with the command line.

### Enabling AppArmor

This is an optional security enhancement (for testers-only). If you're technical & interested, proceed, but do so *at your own risk!*

Note, if you want to use [Tor bridges](https://www.whonix.org/wiki/Bridges), AppArmor has been known in the past to cause problems with `obfsproxy` [see this issue](https://github.com/Whonix/Whonix/issues/67)

You will want to complete the following instructions in both the **Whonix-Gateway** referred to in Qubes VM Manager as `whonix-gw` and the **Whonix-Workstation** or  `whonix-ws`. You only need to apply these settings to the TemplateVMs before creating any template based VMs from these Whonix templates.

(This is because, [since Qubes Q3, TemplateBasedVMs inherit the kernelopts setting of their TemplateVM](https://github.com/QubesOS/qubes-issues/issues/1091).)

### Configuring Whonix-Gateway

Launch the `dom0` terminal app `Konsole` from your Qubes App Launcher. Then get a list of current kernel parameters.

~~~
qvm-prefs -l whonix-gw kernelopts
~~~

As of Qubes Q3 RC1, this will show: `nopat`

Keep those existing kernel parameters and add `apparmor=1 security=apparmor` by entering:

~~~
qvm-prefs -s whonix-gw kernelopts "nopat apparmor=1 security=apparmor"
~~~

When running the command to get a list of current kernel parameters again (just hit the arrow up key twice, so you don't have to type the command again).

~~~
qvm-prefs -l whonix-gw kernelopts
~~~

It should show the old and the new kernel parameters. For example:

~~~
nopat apparmor=1 security=apparmor
~~~

Once you started the VM, you can check if AppArmor is now active.

```
sudo aa-status --enabled ; echo $?
```

It should show: `0`

### Configuring Whonix-Workstation

In `dom0` terminal Konsole, get a list of current kernel parameters.

~~~
qvm-prefs -l whonix-ws kernelopts
~~~

In current version of Qubes, this will show `nopat` as a response. To keep those existing kernel parameters and add `apparmor=1 security=apparmor` do the following:

~~~
qvm-prefs -s whonix-ws kernelopts "nopat apparmor=1 security=apparmor"
~~~

When running the command to get a list of current kernel parameters again (just hit the arrow up key twice, so you don't have to type the command again).

~~~
qvm-prefs -l whonix-ws kernelopts
~~~

It should show the old and the new kernel parameters. For example:<br />

~~~
nopat apparmor=1 security=apparmor
~~~

Once you started the VM, you can check if AppArmor is now active by typing:

~~~
sudo aa-status --enabled ; echo $?
~~~

It should show: `0`
