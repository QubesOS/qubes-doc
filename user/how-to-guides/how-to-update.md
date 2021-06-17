---
lang: en
layout: doc
permalink: /doc/how-to-update/
redirect_from:
 - /doc/updating-qubes-os/
ref: 200
title: How to Update
---

*This page is about updating your system while staying on the same [supported version of Qubes OS](/doc/supported-versions/#qubes-os).
If you're instead looking to upgrade from your current version of Qubes OS to a newer version, see the [Upgrade Guides](/doc/upgrade/).*

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> Updating with direct commands such as <code>qubes-dom0-update</code>, <code>dnf update</code>, and <code>apt update</code> is <b>not</b> recommended, since these bypass built-in Qubes OS update security measures.
  Instead, we strongly recommend using the <b>Qubes Update</b> tool or its command-line equivalents, as described below.
  (By contrast, <a href="/doc/software-update-domu/#installing-software-in-templatevms">installing</a> packages using direct package manager commands is fine.)
</div>

## Security updates

Security updates are an extremely important part of keeping your Qubes installation secure.
When there is an important security issue, we will issue a [Qubes Security Bulletin (QSB)](/security/bulletins/) via the [Qubes Security Pack (`qubes-secpack`)](/security/pack/).
It is very important to read each new QSB and follow any user instructions it contains.
Most of the time, simply [updating your system normally](#routine-updates) will be sufficient to obtain security updates.
However, in some cases, special action may be required on your part, which will be explained in the QSB.

## Routine updates

It is important to keep your Qubes OS system up-to-date to ensure you have the latest [security updates](#security-updates), as well as the latest non-security enhancements and bug fixes.

Fully updating your Qubes OS system means updating:

- [Dom0](/doc/software-update-dom0/)
- [TemplateVMs](/doc/software-update-domu/#updating-software-in-templatevms)
- [StandaloneVMs](/doc/software-update-domu/#standalonevms) (if you have any)

You can accomplish this using the **Qubes Update** tool.

[![Qubes Update](/attachment/wiki/QubesScreenshots/r4.0-software-update.png)](/attachment/wiki/QubesScreenshots/r4.0-software-update.png)

By default, the Qubes Update tool will appear as an icon in the Notification Area when updates are available.

[![Qube Updates Available](/attachment/wiki/QubesScreenshots/r4.0-qube-updates-available.png)](/attachment/wiki/QubesScreenshots/r4.0-qube-updates-available.png)

However, you can also start the tool manually by selecting it in the Applications Menu under "System Tools."
Even if no updates have been detected, you can use this tool to check for updates manually at any time by selecting "Enable updates for qubes without known available updates," then selecting all desired items from the list and clicking "Next."

<div class="alert alert-info" role="alert">
  <i class="fa fa-info-circle"></i>
  <b>Advanced users and developers:</b> For the command-line equivalents of using the <b>Qubes Update</b> tool, see the Salt formulae <a href="/doc/salt/#updatequbes-dom0"><code>update.qubes-dom0</code></a> and <a href="/doc/salt/#updatequbes-vm"><code>update.qubes-vm</code></a>. For enabling testing repos, see <a href="/doc/testing/">Testing new releases and updates</a>.
</div>

## Upgrading to stay on a supported release

The above covers updating *within* a given operating system release.
Eventually, however, most operating system releases will reach [end-of-life (EOL)](https://fedoraproject.org/wiki/End_of_life), after which point they will no longer be supported.
This applies to [Qubes OS itself](/doc/supported-versions/#qubes-os) as well as operating systems used for TemplateVMs and StandaloneVMs, such as [Fedora](/doc/templates/fedora/) and [Debian](/doc/templates/debian/).
It is very important to use only supported releases, since generally only supported releases receive security updates.
This means that you must periodically upgrade to a newer release before your current release reaches EOL.

In the case of Qubes OS itself, we will always [announce](/news/categories/#releases) when a given Qubes OS release is approaching and has reached EOL, and we will provide [instructions for upgrading to the next stable supported Qubes OS release](/doc/upgrade/).
Again, you can always see the current support status for all Qubes OS releases [here](/doc/supported-versions/#qubes-os).

Periodic upgrades are also important for TemplateVMs and StandaloneVMs.
For example, you might be using a [Fedora TemplateVM](/doc/templates/fedora/).
The [Fedora Project](https://getfedora.org/) is independent of the Qubes OS Project.
They set their own [schedule](https://fedoraproject.org/wiki/Fedora_Release_Life_Cycle#Maintenance_Schedule) for when each Fedora release reaches EOL.
You can always find out when an operating system reaches EOL from the upstream project that maintains it, but we also make EOL [announcements](/news/categories/#announcements) and publish guides for official TemplateVM operating systems as a convenience to Qubes users.
When this happens, you should make sure to follow the guide to upgrade to a supported version of that operating system (see the [Fedora upgrade guides](/doc/templates/fedora/#upgrading) and the [Debian upgrade guides](/doc/templates/debian/#upgrading)).

The one exception to all this is the specific release used for dom0 (not to be confused with Qubes OS as a whole), which [doesn't have to be upgraded](/doc/supported-versions/#note-on-dom0-and-eol).

