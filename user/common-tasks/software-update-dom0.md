---
layout: doc
title: Installing and updating software in dom0
permalink: /doc/software-update-dom0/
redirect_from:
- /en/doc/software-update-dom0/
- /doc/SoftwareUpdateDom0/
- /wiki/SoftwareUpdateDom0/
---

Installing and updating software in dom0
========================================

Why would one want to install or update software in dom0?
---------------------------------------------------------

Normally, there should be few reasons for installing or updating software in dom0.
This is because there is no networking in dom0, which means that even if some bugs are discovered e.g. in the dom0 Desktop Manager, this really is not a problem for Qubes, because none of the third-party software running in dom0 is accessible from VMs or the network in any way.
Some exceptions to this include: Qubes GUI daemon, Xen store daemon, and disk back-ends.
(We plan move the disk backends to an untrusted domain in a future Qubes release.) Of course, we believe this software is reasonably secure, and we hope it will not need patching.

However, we anticipate some other situations in which installing or updating dom0 software might be necessary or desirable:

-   Updating drivers/libs for new hardware support
-   Correcting non-security related bugs (e.g. new buttons for qubes manager)
-   Adding new features (e.g. GUI backup tool)

How is software installed and updated securely in dom0?
-------------------------------------------------------

The install/update process is split into two phases: "resolve and download" and "verify and install." The "resolve and download" phase is handled by the "UpdateVM." (The role of UpdateVM can be assigned to any VM in the Qubes VM Manager, and there are no significant security implications in this choice.
By default, this role is assigned to the firewallvm.) After the UpdateVM has successfully downloaded new packages, they are sent to dom0, where they are verified and installed.
This separation of duties significantly reduces the attack surface, since all of the network and metadata processing code is removed from the TCB.

Although this update scheme is far more secure than directly downloading updates in dom0, it is not invulnerable.
For example, there is nothing that the Qubes project can feasibly do to prevent a malicious RPM from exploiting a hypothetical bug in GPG's `--verify` operation.
At best, we could switch to a different distro or package manager, but any of them could be vulnerable to the same (or a similar) attack.
While we could, in theory, write a custom solution, it would only be effective if Qubes repos included all of the regular TemplateVM distro's updates, and this would be far too costly for us to maintain.

How to install and update software in dom0
------------------------------------------

### How to update dom0

In the Qube Manager, simply select dom0 in the VM list, then click the **Update VM system** button (the blue, downward-pointing arrow).
In addition, updating dom0 has been made more convenient: You will be prompted on the desktop whenever new dom0 updates are available and given the choice to run the update with a single click.

Alternatively, command-line tools are available for accomplishing various update-related tasks (some of which are not available via Qubes VM Manager).
In order to update dom0 from the command line, start a console in dom0 and then run one of the following commands:

To check and install updates for dom0 software:

    $ sudo qubes-dom0-update

### How to install a specific package

To install additional packages in dom0 (usually not recommended):

    $ sudo qubes-dom0-update anti-evil-maid

You may also pass the `--enablerepo=` option in order to enable optional repositories (see yum configuration in dom0).
However, this is only for advanced users who really understand what they are doing.
You can also pass commands to `dnf` using `--action=...`.

### How to downgrade a specific package

**WARNING:** Downgrading a package can expose your system to security vulnerabilities.

1.  Download an older version of the package:

    ~~~
    sudo qubes-dom0-update package-version
    ~~~

    Dnf will say that there is no update, but the package will nonetheless be downloaded to dom0.

2.  Downgrade the package:

    ~~~
    sudo dnf downgrade package-version
    ~~~

### How to re-install a package

You can re-install in a similar fashion to downgrading.

1.  Download the package:

    ~~~
    sudo qubes-dom0-update package
    ~~~

    Dnf will say that there is no update, but the package will nonetheless be downloaded to dom0.

2.  Re-install the package:

    ~~~
    sudo dnf reinstall package
    ~~~

    Note that `dnf` will only re-install if the installed and downloaded versions match.
    You can ensure they match by either updating the package to the latest version, or specifying the package version in the first step using the form `package-version`.

### How to uninstall a package

If you've installed a package such as anti-evil-maid, you can remove it with the following command:

    sudo dnf remove anti-evil-maid
    
### Testing repositories

There are three Qubes dom0 testing repositories:

* `qubes-dom0-current-testing` -- testing packages that will eventually land in the stable
  (`current`) repository
* `qubes-dom0-security-testing` -- a subset of `qubes-dom0-current-testing` that contains packages
  that qualify as security fixes
* `qubes-dom0-unstable` -- packages that are not intended to land in the stable (`qubes-dom0-current`)
  repository; mostly experimental debugging packages

To temporarily enable any of these repos, use the `--enablerepo=<repo-name>` option.
Example commands:

~~~
sudo qubes-dom0-update --enablerepo=qubes-dom0-current-testing
sudo qubes-dom0-update --enablerepo=qubes-dom0-security-testing
sudo qubes-dom0-update --enablerepo=qubes-dom0-unstable
~~~

To enable or disable any of these repos permanently, change the corresponding `enabled` value to `1` in
`/etc/yum.repos.d/qubes-dom0.repo`.

### Kernel Upgrade ###

Install newer kernel for dom0 and VMs.
The package `kernel` is for dom0 and the package `kernel-qubes-vm`
is needed for the VMs.
(Note that the following example enables the unstable repo.)

~~~
sudo qubes-dom0-update --enablerepo=qubes-dom0-unstable kernel kernel-qubes-vm
~~~

If the update process does not automatically do it (you should see it mentioned in the CLI output
from the update command), you may need to manually rebuild the EFI or grub config depending on which
your system uses.

EFI: Replace the example version numbers with the one you are upgrading to.
~~~
sudo dracut -f /boot/efi/EFI/qubes/initramfs-4.14.35-1.pvops.qubes.x86_64.img 4.14.35-1.pvops.qubes.x86_64
~~~

Grub2
~~~
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
~~~

Reboot required.

If you wish to upgrade to a kernel that is not available from the repos, then
there is no easy way to do so, but [it may still be possible if you're willing
to do a lot of work yourself](https://groups.google.com/d/msg/qubes-users/m8sWoyV58_E/HYdReRIYBAAJ).

### Upgrading over Tor ###

Requires installed [Whonix](/doc/privacy/whonix/).

Go to Qubes VM Manager -> System -> Global Settings.
See the UpdateVM setting.
Choose your desired Whonix-Gateway ProxyVM from the list.
For example: sys-whonix.

    Qubes VM Manager -> System -> Global Settings -> UpdateVM -> sys-whonix

