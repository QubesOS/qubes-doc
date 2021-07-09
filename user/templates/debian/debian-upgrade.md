---
advanced: true
lang: en
layout: doc
permalink: /doc/template/debian/upgrade/
redirect_from:
- /doc/template/debian/upgrade-8-to-9/
- /doc/debian-template-upgrade-8/
- /en/doc/debian-template-upgrade-8/
- /doc/DebianTemplateUpgrade8/
- /wiki/DebianTemplateUpgrade8/
ref: 133
title: How to upgrade a Debian template in-place
---

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> This page is intended for advanced users only. Most users seeking to upgrade should instead <a href="/doc/templates/debian/#installing">install a new Debian template</a>. Learn more about the two options <a href="/doc/templates/debian/#upgrading">here</a>.
</div>


This page provides instructions for performing an in-place upgrade of an installed [Debian Template](/doc/templates/debian/).
If you wish to install a new, unmodified Debian template instead of upgrading a template that is already installed in your system, please see the [Debian Template](/doc/templates/debian/) page instead. ([Learn more about the two options.](/doc/templates/debian/#upgrading))

In general, upgrading a Debian template follows the same process as [upgrading a native Debian system](https://wiki.debian.org/DebianUpgrade).

## Summary instructions for Debian templates

**Note:** The prompt on each line indicates where each command should be entered: `dom0`, `debian-<old>`, or `debian-<new>`, where `<old>` is the Debian version number *from* which you are upgrading, and `<new>` is the Debian version number *to* which you are upgrading.

```
[user@dom0 ~]$ qvm-clone debian-<old> debian-<new>
[user@dom0 ~]$ qvm-run -a debian-<new> gnome-terminal
[user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list
[user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list.d/qubes-r4.list
[user@debian-<new> ~]$ sudo apt update
[user@debian-<new> ~]$ sudo apt upgrade
[user@debian-<new> ~]$ sudo apt dist-upgrade
[user@dom0 ~]$ qvm-shutdown debian-<new>
```

**Recommended:** [Switch everything that was set to the old template to the new template.](/doc/templates/#switching)

## Detailed instructions for Debian templates

These instructions will show you how to upgrade Debian templates.
The same general procedure may be used to upgrade any template based on the standard Debian template.

**Note:** The prompt on each line indicates where each command should be entered: `dom0`, `debian-<old>`, or `debian-<new>`, where `<old>` is the Debian version number *from* which you are upgrading, and `<new>` is the Debian version number *to* which you are upgrading.

1. Ensure the existing template is not running.

    ```
    [user@dom0 ~]$ qvm-shutdown debian-<old>
    ```

2. Clone the existing template and start a terminal in the new template.

    ```
    [user@dom0 ~]$ qvm-clone debian-<old> debian-<new>
    [user@dom0 ~]$ qvm-run -a debian-<new> gnome-terminal
    ```

3. Update your `apt` repositories to use the new release's code name instead of the old release's code name.
   (This can be done manually with a text editor, but `sed` can be used to automatically update the files.)

    ```
    [user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list
    [user@debian-<new> ~]$ sudo sed -i 's/<old-name>/<new-name>/g' /etc/apt/sources.list.d/qubes-r4.list
    ```

4. Update the package lists and upgrade.
   During the process, it may prompt you to overwrite the file `qubes-r4.list`.
   You should overwrite this file.

    ```
    [user@debian-<new> ~]$ sudo apt update
    [user@debian-<new> ~]$ sudo apt upgrade
    [user@debian-<new> ~]$ sudo apt dist-upgrade
    ```

5. (Optional) Remove unnecessary packages that were previously installed.

    ```
    [user@debian-<new> ~]$ sudo apt-get autoremove
    ```

6. (Optional) Clean cached packages from `/var/cache/apt`.

    ```
    [user@debian-<new> ~]$ sudo apt-get clean
    ```

7. (Optional) Trim the new template.
    (This should [no longer be necessary](/doc/templates/#important-notes), but it does not hurt.
    Some users have [reported](https://github.com/QubesOS/qubes-issues/issues/5055) that it makes a difference.)

    ```
    [user@debian-<new> ~]$ sudo fstrim -av
    [user@dom0 ~]$ qvm-shutdown debian-<new>
    [user@dom0 ~]$ qvm-start debian-<new>
    [user@debian-<new> ~]$ sudo fstrim -av
    ```

8. Shut down the new template.

    ```
    [user@dom0 ~]$ qvm-shutdown debian-<new>
    ```

9. (Recommended) [Switch everything that was set to the old template to the new template.](/doc/templates/#switching)

10. (Optional) Make the new template the global default.

    ```
    [user@dom0 ~]$ qubes-prefs --set debian-<new>
    ```

11. (Optional) [Uninstall the old template.](/doc/templates/#uninstalling)
    Make sure that the template you're uninstalling is the old one, not the new one!

## Standalones

The procedure for upgrading a Debian [standalone](/doc/standalone-and-hvm/) is the same as for a template.

## Release-specific notes

This section contains notes about upgrading to specific releases.

### Debian 10 ("Buster")

Please see [Debian's Buster upgrade instructions](https://www.debian.org/releases/buster/amd64/release-notes/ch-upgrading.en.html).

### Debian 9 ("Stretch")

* The upgrade process may prompt you to overwrite two files: `qubes-r4.list` and `pulse/client.conf`.
  `qubes-r4.list` can be overwritten, but `pulse/client.conf` must be left as the currently-installed version.

* If sound is not working, you may need to enable the Qubes testing repository to get the testing version of `qubes-gui-agent`.
  This can be done by editing the `/etc/apt/sources.list.d/qubes-r4.list` file and uncommenting the `Qubes Updates Candidates` repo.

* User-initiated updates/upgrades may not run when a template first starts.
  This is due to a new Debian config setting that attempts to update automatically; it should be disabled with `sudo systemctl disable apt-daily.{service,timer}`.

Relevant discussions:

* [Stretch Template Installation](https://groups.google.com/forum/#!topicsearchin/qubes-devel/debian$20stretch/qubes-devel/4rdayBF_UTc)
* [Stretch availability in 3.2](https://groups.google.com/forum/#!topicsearchin/qubes-devel/debian$20stretch/qubes-devel/cekPfBqQMOI)
* [Fixing sound in Debian Stretch](https://groups.google.com/forum/#!topic/qubes-users/JddCE54GFiU)
* [User apt commands blocked on startup](https://github.com/QubesOS/qubes-issues/issues/2621)

Also see [Debian's Stretch upgrade instructions](https://www.debian.org/releases/stretch/amd64/release-notes/ch-upgrading.en.html).

### Debian 8 ("Jessie")

Please see [Debian's Jessie upgrade instructions](https://www.debian.org/releases/jessie/amd64/release-notes/ch-upgrading.en.html).

### End-of-life (EOL) releases

We strongly recommend against using any Debian release that has reached [end-of-life (EOL)](https://wiki.debian.org/DebianReleases#Production_Releases).

## Additional information

* Please note that, if you installed packages from one of the testing repositories, you must make sure that the repository is enabled in `/etc/apt/sources.list.d/qubes-r4.list` before attempting the upgrade.
  Otherwise, your upgrade will [break](https://github.com/QubesOS/qubes-issues/issues/2418).

* By default, Qubes uses code names in the `apt` sources files, although the templates are referred to by release number.
  Check the code names for the templates, and ensure you are aware of any changes you have made in the repository definitions.
