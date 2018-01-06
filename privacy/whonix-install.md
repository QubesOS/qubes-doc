---
layout: doc
title: Install Whonix in Qubes
permalink: /doc/whonix/install/
redirect_from: /doc/privacy/install-whonix/
---


Install Whonix in Qubes
=======================

Installing Whonix in Qubes is simple and only requires a few simple steps.

### First Time Users

Using privacy and anonymization tools like Whonix is not a magical solution that instantly makes you anonymous online. Please consider:

* Do you know what metadata or a man-in-the-middle attack is?
* Do you think nobody can eavesdrop on your communications because you are using Tor?
* Do you know how Whonix works?

If you answered no, have a look at the [about](https://www.whonix.org/wiki/About), [warning](https://www.whonix.org/wiki/Warning) and [do not](https://www.whonix.org/wiki/DoNot) pages (on the Whonix website) to make sure Whonix is the right tool for you and you understand  it's limitations.

---

### Install Templates

Launch the `dom0` terminal `Konsole` from your Qubes App Launcher. Then enter the following command to install the Whonix-Gateway and Workstation TemplateVMs.

~~~
sudo qubesctl state.sls qvm.anon-whonix
~~~

Download will take a while and there will be no progress indicator.

After doing this, you should see two new TemplateVMs in the VM Manager called `whonix-gw` and `whonix-ws` as well as a `whonix-gw` TemplateBased ProxyVM called `sys-whonix` as well as a `whonix-ws` based AppVM called `anon-whonix`.

### Enabling AppArmor

This is an optional security enhancement (for testers-only). If you’re technical & interested, see [Enabling AppArmor](/doc/privacy/customizing-whonix/).

### Running Applications

To start an application in the **anon-whonix AppVM**, launch it like any other - open the `Qubes App Launcher` and then select an app such as `Tor Browser`.

### Advanced Information

You can learn more about [installing Whonix](https://www.whonix.org/wiki/Qubes/Install), [Qubes-Whonix](https://www.whonix.org/wiki/Qubes) or [Whonix generally](https://www.whonix.org).
