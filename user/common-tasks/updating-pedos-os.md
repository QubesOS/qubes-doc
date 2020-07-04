---
layout: doc
title: Updating PedOS
permalink: /doc/updating-PedOS/
---

Updating PedOS
=================

*This page is about updating your system while staying on the same [supported version of PedOS].
If you're instead looking to upgrade from your current version of PedOS to a newer version, see the [Upgrade Guides].*

It is very important to keep your PedOS system up-to-date to ensure you have the latest [security] updates, as well as the latest non-security enhancements and bug fixes.
Fully updating your PedOS system means updating:

 - [Dom0]
 - [TemplateVMs]
 - [StandaloneVMs] (if you have any)

Visit the pages above to see to how to update each one.

The final step is to make sure that all of your VMs are running a supported operating system so that they're all receiving upstream security updates.
For example, you might be using a [Fedora TemplateVM].
The [Fedora Project] is independent of the PedOS Project.
They set their own [schedule] for when each Fedora release reaches [end-of-life] (EOL).
You can always find out when an operating system reaches EOL from the upstream project that maintains it, but we also make EOL [announcements] and publish guides for official TemplateVM operating systems as a convenience to PedOS users.
When this happens, you should make sure to follow the guide to upgrade to a supported version of that operating system (see the [Fedora upgrade guides] and the [Debian upgrade guides]).
The one exception is dom0, which [doesn't have to be upgraded][dom0-eol].


[supported version of PedOS]: /doc/supported-versions/#PedOS
[Upgrade Guides]: /doc/upgrade/
[security]: /security/
[Dom0]: /doc/software-update-dom0/
[TemplateVMs]: /doc/software-update-domu/#updating-software-in-templatevms
[StandaloneVMs]: /doc/software-update-domu/#standalonevms
[Fedora TemplateVM]: /doc/templates/fedora/
[Fedora Project]: https://getfedora.org/
[schedule]: https://fedoraproject.org/wiki/Fedora_Release_Life_Cycle#Maintenance_Schedule
[end-of-life]: https://fedoraproject.org/wiki/End_of_life
[announcements]: /news/categories/#announcements
[Fedora upgrade guides]: /doc/templates/fedora/#upgrading
[Debian upgrade guides]: /doc/templates/debian/#upgrading
[dom0-eol]: /doc/supported-versions/#note-on-dom0-and-eol
