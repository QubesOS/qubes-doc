---
layout: doc
title: Updating Qubes OS
permalink: /doc/updating-qubes-os/
---

Updating Qubes OS
=================

This page is about updating your system while staying on the same [supported version of Qubes OS].
If you're instead looking to upgrade from your current version of Qubes OS to a newer version, see the [Upgrade Guides].

Fully updating your Qubes OS system means updating:

 - [Dom0]
 - [TemplateVMs]
 - [StandaloneVMs] (if you have any)

Visit the pages above to see to how to update each one.

The final step is to make sure that all of your VMs are running a supported operating system so that they're all receiving security updates.
For example, you might be using a [Fedora TemplateVM].
The [Fedora Project] is independent of the Qubes OS Project.
They set their own [schedule] for when each Fedora release reaches [end-of-life] (EOL).
You can always find out when an operating system reaches EOL from the upstream project that maintains it, but we also make EOL [announcements] and publish guides for official TemplateVM operating systems as a convenience to Qubes users.
When this happens, you should make sure to follow the guide to upgrade to a supported version of that operating system (see the [Fedora upgrade guides] and the [Debian upgrade guides]).
The one exception is dom0, which [doesn't have to be upgraded][dom0-eol].


[supported version of Qubes OS]: /doc/supported-versions/#qubes-os
[Upgrade Guides]: /doc/upgrade/
[Dom0]: /doc/software-update-dom0/
[TemplateVMs]: /doc/software-update-vm/#installing-or-updating-software-in-the-templatevm
[StandaloneVMs]: /doc/software-update-vm/#standalone-vms
[Fedora TemplateVM]: /doc/templates/fedora/
[Fedora Project]: https://getfedora.org/
[schedule]: https://fedoraproject.org/wiki/Fedora_Release_Life_Cycle#Maintenance_Schedule
[end-of-life]: https://fedoraproject.org/wiki/End_of_life
[announcements]: /news/categories/#announcements
[Fedora upgrade guides]: /doc/templates/fedora/#upgrading
[Debian upgrade guides]: /doc/templates/debian/#upgrading
[dom0-eol]: /doc/supported-versions/#note-on-dom0-and-eol
