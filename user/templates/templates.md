---
lang: en
layout: doc
permalink: /doc/templates/
redirect_from:
- /doc/template/
- /en/doc/templates/
- /doc/Templates/
- /wiki/Templates/
ref: 131
title: Templates
---

In [Getting Started](/doc/getting-started/), we covered the distinction
in Qubes OS between where you *install* your software and where you *run* your
software. Software that you use in most everyday tasks, is installed within [templates](/doc/glossary/#template).
When using Qubes OS, you normally work in [app qubes](/doc/glossary/#app-qube).
App qubes are based on a *template* qube (or more simply, just *a template*).
They inherit most of the ["root filesystem"](https://opensource.com/life/16/10/introduction-linux-filesystems), from the template.
Changes you make to the root filesystem are not written back to the template: if you install an application in an app qube it will disappear when you shut down the qube. (You may be able to work round this by using Flatpak or snap packages, which install to the user's home directory.)
The user home directory *is* specific to the app qube, and changes there are kept.
There is a full explanation of this [below](#inheritance-and-persistence).

If you use a [Standalone](/doc/glossary/#standalone), the **whole filesystem** is specific to the standalone, and every change you make will be kept after shutdown.

The template system has significant benefits:

* **Security:** Each qube has read-only access to the template on which it's
  based, so if a qube is compromised, it cannot infect its template or any of
  the other qubes based on that template.

* **Storage:** Each qube based on a template uses only the disk space required
  to store its own data (i.e., your files in its home directory), which
  dramatically saves on disk space.

* **Speed:** It is extremely fast to create new app qubes, since the root
  filesystem already exists in the template.

* **Updates:** Updates are naturally centralized, since updating a template
  means that all qubes based on it will automatically use those updates after
  they're restarted.

An important side effect of this system is that any software installed in an
app qube (rather than in the template on which it is based) will disappear
when the app qube shuts down (see [Inheritance and
Persistence](#inheritance-and-persistence)). For this reason, we recommend
installing most of your software in templates, not app qubes.

The default template in Qubes is based on Fedora, but there are additional
templates based on other Linux distributions. There are also templates
available with or without certain software preinstalled. You may find it useful
to have multiple templates installed in order to provide:

* Different security levels (e.g., more or less trusted software installed)
* Different environments (e.g., Fedora, Debian, Whonix)
* Different tools (e.g., office, media, development, hardware drivers)

## Official

These are the official Qubes OS Project templates. We build and release updates
for these templates. We guarantee that the binary updates are compiled from
exactly the same source code as we publish.

* [Fedora](/doc/templates/fedora/) (default)
* [Fedora Minimal](/doc/templates/minimal/)
* [Fedora Xfce](/doc/templates/xfce)
* [Debian](/doc/templates/debian/)
* [Debian Minimal](/doc/templates/minimal/)
* [Debian Xfce](/doc/templates/xfce)

You can see the current supported versions [here](/doc/supported-releases#templates).

## Community

These templates are supported by the Qubes community. Some of them are
available in ready-to-use binary package form (built by the Qubes developers),
while others are available only in source code form. In all cases, the Qubes OS
Project does not provide updates for these templates. However, such updates may
be provided by the template maintainer.

By installing these templates, you are trusting not only the Qubes developers
and the distribution maintainers, but also the template maintainer. In
addition, these templates may be somewhat less stable, since the Qubes
developers do not test them.

* [Whonix](/doc/templates/whonix/)
* [Ubuntu](/doc/templates/ubuntu/)
* [Arch Linux](/doc/building-archlinux-template/)
* [Gentoo](/doc/templates/gentoo/)
* [Gentoo Minimal](/doc/templates/minimal/)
* [CentOS*](/doc/templates/centos)

*\* The CentOS version used by this template reached 
[End-of-Life in June 2024](https://en.wikipedia.org/wiki/CentOS_Stream#Release_history) 
and is no longer receiving updates. Due to a lack of specific interest 
at this time a proposal to create a new CentOS 10 template was 
[declined](https://github.com/QubesOS/qubes-issues/issues/9716).*

## Windows

Windows templates are constructed differently from Linux-based templates as
Windows is a closed source system that can be modified only after installing.
So it is not possible to provide preconfigured Windows templates for Qubes.
The process of installing a Windows qube and connecting it to the Qubes
environment via installing Qubes Windows Tools (QWT) is described in several
chapters in [Windows qubes](/doc/templates/windows/).

## Installing

Certain templates come preinstalled with Qubes OS. However, there may be times
when you wish to install a fresh template from the Qubes repositories, e.g.:

* When a template version you're using reaches
  [end-of-life](/doc/how-to-update/#upgrading-to-avoid-eol).
* When a new version of a template that you wish to use becomes
  [supported](/doc/supported-releases/).
* When you suspect your template has been compromised.
* When you have made modifications to your template that you no longer want.

You can manage your templates using the `Qubes Template Manager`, a GUI tool available from the Qube menu.
You can also use a command line tool in dom0 - `qvm-template`.

At the command line in dom0, `qvm-template list --available` will show available templates. To install a template, use:
```
$ qvm-template install  <template_name>
```
You can also use `qvm-template` to upgrade or reinstall templates.

Repository (repo) definitions are stored in dom0 in `/etc/qubes/repo-templates` and associated keys in `/etc/qubes/repo-templates/keys`.
There are additional repos for testing releases and community templates.
To temporarily enable any of these repos, use the `--enablerepo=<repo-name>` option. E.g. :
```
$ qvm-template  --enablerepo qubes-templates-community install <template_name>
```
To permanently enable a repo, set the line `enabled = 1` in the repo definition in `/etc/qubes/repo-templates`.  
To permanently disable, set the line to `enabled = 0`.

If you wish to install a template that is in testing, please see
[here](/doc/testing/#templates).

## After Installing

After installing a fresh template, we recommend performing the following steps:

1. [Update the template](#updating).

2. [Switch any app qubes that are based on the old template to the new
   one](#switching).

3. If desired, [uninstall the old template](#uninstalling).

## Network access

For information about how templates access the network, please see [Why don’t
templates have network
access?](/doc/how-to-install-software/#why-dont-templates-have-normal-network-access)
and the [Updates proxy](/doc/how-to-install-software/#updates-proxy).

## Updating

Please see [How to Update](/doc/how-to-update/).

## Installing Software

Please see [How to Install Software](/doc/how-to-install-software).

## Uninstalling

To remove a template, the graphical `Qube Manager` (Qubes Menu > Qubes Tools > Qube Manager) may be used. Right-click the template to be uninstalled and click "Delete qube" to begin removal. If no issues are found, a dialog box will request the template's name be typed as a final confirmation. Upon completion, the template will be deleted.

Alternatively, to remove a template via the command line in dom0:
```
$ qvm-template remove <TEMPLATE_NAME>
```

\<TEMPLATE_NAME> is the first column from the output of:
```
$ qvm-template list --installed
```

In either case, issues with template removal may be raised. If an issue is raised, the template will remain installed and a list of concerns displayed. "Global property default_template" requires [switching](#switching) the default_template property to another template. "Template for" can be resolved by [switching](#switching) the dependent qubes' template. Once the issues are addressed, attempt the removal again.

If the template's entry in the Qubes Menu is not removed with its uninstallation, consult the [troubleshooting page](/doc/app-menu-shortcut-troubleshooting/#what-if-a-removed-application-is-still-in-the-app-menu).

## Reinstalling

Please see [How to Reinstall a Template](/doc/reinstall-template/).

## Switching

When you install a new template or
[upgrade](/doc/how-to-update/#upgrading-to-avoid-eol) a template, it is
recommended that you switch everything that was using the old template to the
new template:

1. **Make the new template the default template.** In the App Menu, go
   to Qubes Tools, then click on Qubes Global Settings. In the Qube Defaults
   section, next to Template, select the new template from the
   drop-down list. Press OK.

2. **Base your [disposable templates](/doc/glossary/#disposable-template) on
   the new template.**

   - If your only keyboard and mouse are *not* connected through a [USB
     qube](/doc/usb-qubes/), or that USB qube is *not* a disposable, then shut
     down all disposables. In the App Menu, go to Qubes Tools, then click on
     Qube Manager. In the Qube Manager, find your disposable template(s). (By
     default, they end in `-dvm`.) Right click, hover over Template, then click
     on the new template. Repeat for each disposable template.

   - If your only keyboard or mouse *are* connected through a USB qube, and
     that USB qube *is* a disposable, then you will have to enter a special
     command that shuts down all of your qubes, switches the USB qube's
     disposable template to the new template, then starts the USB qube again.
     In order to avoid being locked out of your system, you must be very
     careful to enter this command without typos and with the correct
     substitutions.

     In the App Menu, click on Terminal Emulator. Type the command below,
     substituting `<SYS_USB_DISPOSABLE_TEMPLATE>` with the name of the
     disposable template on which `sys-usb` is based, `<NEW_TEMPLATE>` with the
     name of the new template, and `<USB_QUBE>` with the name of your USB qube.
     Other than these substitutions, make sure to enter the command exactly as
     written.

     ```
     qvm-shutdown --wait --all; qvm-prefs <SYS_USB_DISPOSABLE_TEMPLATE> template <NEW_TEMPLATE>; qvm-start <USB_QUBE>
     ```

     With substitutions, your command should look similar to this example.
     (Warning: This is just an example. Do not attempt to use it.)

     ```
     qvm-shutdown --wait --all; qvm-prefs fedora-01-dvm template fedora-02; qvm-start sys-usb
     ```

3. **Base your app qubes on the new template.** In the Qube Manager, click on
   the Template heading to sort by template. Select all the qubes based on the
   old template by clicking on the first one, holding shift, then clicking on
   the last one. With multiple qubes selected, right-click on any of them,
   hover your cursor over Template, then click on the new template.
    Or in the `System` menu select `Manage templates for qubes`, select
    any qubes using the old template and update them to the new template
    using the drop down menu.

4. **Change the template for the default-mgmt-dvm** If the old template
    was used for management qubes, then you should change the template.
    This is an *internal* qube which does not appear by default in the Qube manager.
    In the `System` menu select `Manage templates for qubes`, and you will see the *default-mgmt-dvm* qube.
    Change the template used for this disposable template to the new template.

## Advanced

The following sections cover advanced topics pertaining to templates.

### Inheritance and persistence

Whenever an app qube is created, the contents of the `/home` directory of its
parent template are *not* copied to the child app qube's `/home`. The child app
qube's `/home` is always independent from its parent template's `/home`, which
means that any subsequent changes to the parent template's `/home` will not
affect the child app qube's `/home`.

Once an app qube has been created, any changes in its `/home`, `/usr/local`, or
`/rw/config` directories will be persistent across reboots, which means that
any files stored there will still be available after restarting the app qube.
No changes in any other directories in app qubes persist in this manner. If you
would like to make changes in other directories which *do* persist in this
manner, you must make those changes in the parent template.

| Qube Type                                       | Inheritance<sup>1</sup>                                   | Persistence<sup>2</sup>                                 |
|-------------------------------------------------|-----------------------------------------------------------|---------------------------------------------------------|
| [template](/doc/glossary/#template)             | N/A (templates cannot be based on templates)              | everything                                              |
| [app qube](/doc/glossary/#app-qube)<sup>3</sup> | `/etc/skel` to `/home`; `/usr/local.orig` to `/usr/local` | `/rw` (includes `/home`, `/usr/local`, and `bind-dirs`) |
| [disposable](/doc/glossary/#disposable)         | `/rw` (includes `/home`, `/usr/local`, and `bind-dirs`)   | nothing                                                 |

<sup>1</sup>Upon creation  
<sup>2</sup>Following shutdown  
<sup>3</sup>Includes [disposable templates](/doc/glossary/#disposable-template)

### Trusting your templates

As the template is used for creating filesystems for other app qubes where you
actually do the work, it means that the template is as trusted as the most
trusted app qube based on this template. In other words, if your template gets
compromised, e.g. because you installed an application, whose *installer's
scripts* were malicious, then *all* your app qubes (based on this template)
will inherit this compromise.

There are several ways to deal with this problem:

* Only install packages from trusted sources -- e.g. from the pre-configured
  Fedora repositories. All those packages are signed by Fedora, and we expect
  that at least the package's installation scripts are not malicious. This is
  enforced by default (at the [firewall qube level](/doc/firewall/)), by not
  allowing any networking connectivity in the default template, except for
  access to the Fedora repos.

* Use [standalones](/doc/glossary/#standalone) (see below) for installation of
  untrusted software packages.

* Use multiple templates (see below) for different classes of domains, e.g. a
  less trusted template, used for creation of less trusted app qubes, would get
  various packages from less trusted vendors, while the template used for more
  trusted app qubes will only get packages from the standard Fedora repos.

Some popular questions:

> So, why should we actually trust Fedora repos -- it also contains large
> amount of third-party software that might be buggy, right?

As far as the template's compromise is concerned, it doesn't really matter
whether `/usr/bin/firefox` is buggy and can be exploited, or not. What matters
is whether its *installation* scripts (such as %post in the rpm.spec) are
benign or not. A template should be used only for installation of packages, and
nothing more, so it should never get a chance to actually run
`/usr/bin/firefox` and get infected from it, in case it was compromised. Also,
some of your more trusted app qubes would have networking restrictions enforced
by the [firewall qube](/doc/firewall/), and again they should not fear this
proverbial `/usr/bin/firefox` being potentially buggy and easy to compromise.

> But why trust Fedora?

Because we chose to use Fedora as a vendor for the Qubes OS foundation (e.g.
for dom0 packages and for app qube packages). We also chose to trust several
other vendors, such as Xen.org, kernel.org, and a few others whose software we
use in dom0. We had to trust *somebody* as we are unable to write all the
software from scratch ourselves. But there is a big difference in trusting all
Fedora packages to be non-malicious (in terms of installation scripts) vs.
trusting all those packages are non-buggy and non-exploitable. We certainly do
not assume the latter.

> So, are the templates as trusted as dom0?

Not quite. Dom0 compromise is absolutely fatal, and it leads to Game
Over<sup>TM</sup>. However, a compromise of a template affects only a subset of
all your app qubes (in case you use more than one template, or also some
standalones). Also, if your app qubes are network disconnected, even though
their filesystems might get compromised due to the corresponding template
compromise, it still would be difficult for the attacker to actually leak out
the data stolen in an app qube. Not impossible (due to existence of covert
channels between VMs on x86 architecture), but difficult and slow.

### Note on treating app qubes' root filesystem non-persistence as a security feature

Any app qube that is based on a template has its root filesystem non-persistent
across qube reboots. In other words, whatever changes the qube makes (or the
malware running in this qube makes) to its root filesystem, are automatically
discarded whenever one restarts the qube.

This might seem like an excellent anti-malware mechanism to be used inside the
qube. However, one should be careful with treating this property as a reliable
way to keep the qube malware-free. This is because the non-persistence, in the
case of normal qubes, applies only to the root filesystem and not to the user
filesystem (on which the `/home`, `/rw`, and `/usr/local` are stored) for
obvious reasons. It is possible that malware, especially malware that could be
specifically written to target Qubes, could install its hooks
inside the user home directory files only. Examples of obvious places for such
hooks could be: `.bashrc`, the Firefox profile directory which contains the
extensions, or some PDF or DOC documents that are expected to be opened by the
user frequently (assuming the malware found an exploitable bug in the PDF or
DOC reader), and surely many others places, all in the user's home directory.

One advantage of the non-persistent rootfs though, is that the malware is still
inactive before the user's filesystem gets mounted and "processed" by
system/applications, which might theoretically allow for some scanning programs
(or a skilled user) to reliably scan for signs of infections of the app qube.
But, of course, the problem of finding malware hooks in general is hard, so
this would work likely only for some special cases (e.g. an app qube which
doesn't use Firefox, as otherwise it would be hard to scan the Firefox profile
directory reliably to find malware hooks there). Also note that the user
filesystem's metadata might got maliciously modified by malware in order to
exploit a hypothetical bug in the app qube kernel whenever it mounts the
malformed filesystem. However, these exploits will automatically stop working
(and so the infection might be cleared automatically) after the hypothetical
bug got patched and the update applied (via template update), which is an
exceptional feature of Qubes OS.

Also note that disposable qubes do not have persistent user filesystem, and so
they start up completely "clean" every time. Note the word "clean" means in
this context: the same as their template filesystem, of course.

### Important Notes

* `qvm-trim-template` is no longer necessary or available in Qubes 4.0 and
  higher. All qubes are created in a thin pool and trimming is handled
  automatically. No user action is required. See [Disk Trim](/doc/disk-trim)
  for more information.

* RPM-installed templates are "system managed" and therefore cannot be backed
  up using Qubes' built-in backup function. In order to ensure the preservation
  of your custom settings and the availability of a "known-good" backup
  template, you may wish to clone the default system template and use your
  clone as the default template for your app qubes.

* Some templates are available in ready-to-use binary form, but some of them
  are available only as source code, which can be built using the [Qubes
  Builder](https://github.com/QubesOS/qubes-builderv2/). In particular, some
  template "flavors" are  available in source code form only. For the
  technical details of the template
  system, please see [Template Implementation](/doc/template-implementation/).
  Take a look at the [Qubes Builder](/doc/qubes-builder-v2/) documentation for
  instructions on how to compile them.
