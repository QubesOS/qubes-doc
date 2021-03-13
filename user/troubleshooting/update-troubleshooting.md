---
layout: doc
title: Update Troubleshooting
permalink: /doc/update-troubleshooting/
---

# Fixing issues that arise during updating

## “Failed to synchronize cache for repo” errors when updating Fedora templates

This is general Fedora issue, not a Qubes-specific issue.
Usually, this is due to network problems (especially if downloading updates over Tor) or problems with the download mirrors.
Often, the problem can be resolved by trying again on a different connection (a different Tor circuit, if using Tor) or waiting and trying again later.
Here are some examples of non-Qubes reports about this problem:

- <https://ask.fedoraproject.org/en/question/88086/error-failed-to-synchronize-cache-for-repo-fedora/>
- <https://unix.stackexchange.com/questions/390805/repos-not-working-on-fedora-error-failed-to-synchronize-cache-for-repo-update>
- <https://www.reddit.com/r/Fedora/comments/74nldq/fedora_26_dnf_error_failed_to_synchronize_cache/>
- <https://bugzilla.redhat.com/show_bug.cgi?id=1494178>
- <https://stackoverflow.com/questions/45318256/error-failed-to-synchronize-cache-for-repo-updates>

More examples can be found by searching for "Failed to synchronize cache for repo" (with quotation marks) on your preferred search engine.

## Lost internet access after a TemplateVM update

In earlier versions of Qubes, there were situations where qubes lost internet access after a TemplateVM update. The following fix should be applied in recent versions of Qubes.

Run `systemctl enable NetworkManager-dispatcher.service` in the TemplateVM upon which your NetVM is based.
You may have to reboot afterward for the change to take effect.
(Note: This is an upstream problem. See [this Redhat ticket](https://bugzilla.redhat.com/show_bug.cgi?id=974811)).
For details, see the qubes-users mailing list threads [here](https://groups.google.com/d/topic/qubes-users/xPLGsAJiDW4/discussion) and [here](https://groups.google.com/d/topic/qubes-users/uN9G8hjKrGI/discussion).)

## Windows update is stuck

This has nothing to do with Qubes.
It's a longstanding Windows bug.
More information about this issue and solutions can be found [here](https://superuser.com/questions/951960/windows-7-sp1-windows-update-stuck-checking-for-updates).

## Dom0 and/or TemplateVM update stalls when updating via the GUI tool

This can usually be fixed by updating via the command line.

In dom0, open a terminal and run `sudo qubes-dom0-update`.

Depending on your operating system, open a terminal in the TemplateVMs and run:
* Fedora: `sudo dnf upgrade`
* Debian: `apt-get update && apt-get dist-upgrade`
