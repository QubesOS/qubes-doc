---
layout: doc
title: Archlinux Template
permalink: /doc/templates/archlinux/
redirect_from:
- /doc/archlinux/
- /en/doc/templates/archlinux/
- /doc/Templates/Archlinux/
- /wiki/Templates/Archlinux/
---

# Archlinux Template

Archlinux template is one of the templates made by Qubes community. It should
be considered experimental as Qubes developers team use mainly Fedora-based VMs
to test new features/updates.

Main maintainer of this template is [Olivier Médoc](mailto:o_medoc@yahoo.fr).

Updates for this template are provided by [Olivier Médoc](mailto:o_medoc@yahoo.fr) and are signed by the following key:


    pub   2048R/2043E7ACC1833B9C 2014-03-27 [expires: 2018-03-29]
          Key fingerprint = D85E E12F 9678 51CC F433  515A 2043 E7AC C183 3B9C
    uid                          Olivier MEDOC (Qubes-OS signing key) <o_medoc@yahoo.fr>

## Installation

A prebuilt template is available only for Qubes 3.2. Before Qubes 3.2, it should be compiled from source as described in [building-archlinux-template](/doc/building-archlinux-template/).

    [user@dom0 ~]$ sudo qubes-dom0-update --enablerepo=qubes-templates-community qubes-template-archlinux

## Binary packages activation

The Qubes update repository is disabled by default in the Archlinux template. You can however choose to trust it by registering it into pacman.

Since November 2017, an activation package is present in the template. The update repository can thus be activated by running the following command inside the template:

    # pacman -sU /etc/pacman.d/qubes-vm-keyring*.pkg.tar.xz
    
It should be noted to this command will create a trust for packages provided by [Olivier Médoc](mailto:o_medoc@yahoo.fr) and signed by the PGP key above.

If the qubes-vm-keyring package is not present in `/etc/pacman.d/`, please refer to the section #Activating binary packages manually.

## Optional Qubes packages

Several Qubes packages are not necessarily installed by default in the Archlinux Template. These packages can be installed to add additional functionnalities to the template:
* `qubes-vm-networking`: Contains Qubes tools and dependencies required to use the template as a NetVM/ProxyVM
* `qubes-vm-pulseaudio`: Contains `Pulseaudio` agent enabling sound support in the template

## Default template packages

In order to keep the template as small and simple as possible, default installed package have been arbitrarily selected based on multiple subjective criterias that however essentially include libraries dependencies. This packages are:
* Some font packages to keep good user experience
* leafpad: a note pad
* xfce4-terminal: a terminal
* thunar: a file browser that supports mounting usb keys
* firefox: web browser
* thunderbird: a mail browser
* evince: a document viewer

Note that Archlinux does not install GUI packages by default as this decision is left to users. These packages have only been selected to have a usable template.

## Activating binary packages manually

Enable the repository by running the following command:

    # rm /etc/pacman.d/99-qubes-repository-3.2.conf
    # ln -s /etc/pacman.d/99-qubes-repository-3.2.disabled /etc/pacman.d/99-qubes-repository-3.2.conf

Then you need to install and sign the public GPG key of the package maintainer (note that accessing to GPG servers requires to temporarily disable the firewall in your template):

    # pacman-key --recv-key 2043E7ACC1833B9C
    # pacman-key --finger 2043E7ACC1833B9C
 
If the fingerprint is correct, you can then sign the key:

    # pacman-key --lsign-key 2043E7ACC1833B9C

## Updating a Qubes-3.2 Archlinux Template

Because of changes in the Qubes-4.0 partition layout, and usage of XEN HVMs instead of pv-guests. It is not straightforward to update a Qubes-3.2 template to Qubes-4.0.

For this reason, it is recommended to start from a new template in Qubes-4.0.

## Updating a Qubes-3.1 Archlinux Template

If you decide to use binary packages but that you were using a Qubes-3.1 Template, you can follow these instructions to enable Qubes 3.2 agents.

You can use a template that you built for Qubes 3.1 in Qubes 3.2. The qrexec and gui agent functionalities should still be working so that you can at least open a terminal.

In order to enable binary packages for Qubes 3.2, add the following lines to the end of /etc/pacman.conf

```
[qubes-r3.2]
Server = http://olivier.medoc.free.fr/archlinux/current/
```

You should then follow the instruction related to pacman-key in order to sign the binary packages PGP key. With the key enabled, a pacman update will update qubes agents:
` # pacman -Suy `

The two lines that have just been added to /etc/pacman.conf should then be removed as they have been included in the qubes-vm-core update in the file `/etc/pacmand.d/99-qubes-repository-3.2.conf`

## Known Issues

### Package cannot be updated because of errors related to xorg-server or pulseaudio versions

The Qubes GUI agent must be rebuilt whenever xorg-server or pulseaudio make major changes.
If an update of one of these packages causes your template to break, simply [revert it](https://www.qubes-os.org/doc/software-update-vm/#reverting-changes-to-a-templatevm) and wait for corresponding Qubes package updates to be available (or attempt to build them yourself, if you're so inclined).
This should not happen frequently.

### qubes-vm is apparently starting properly (green dot) however graphical applications do not appear to work

They are multiple potential reasons. Some of them are described in the following issue:
* https://github.com/QubesOS/qubes-issues/issues/2612

In issue 2612, check that the option `noauto` is present for all lines in /etc/fstab related to /rw or /home. This bug can appear if you come from an old Archlinux Template (pre February 2017).

## Debugging a broken VM

In order to identify the issue, you should start by getting a console access to the VM:

* Either by running in dom0 `qvm-run --pass-io --nogui yourbrokenvm 'your command here'`

* Or by running in dom0 `sudo xl console yourbrokenvm`

Start by trying to run a GUI application such as xfce4-terminal in order to identify any error message.

Then you can check potential broken systemd service by running the following command inside the broken vm: `systemctl | grep fail`.

If you identified a broken service check `journalctl -la -u yourbrokenservice`. If not check `journalctl -b` for errors.

Finally, errors related to the GUI agent can be found inside the VM in `/home/user/.xsession-errors`

## Packages manager wrapper

Powerpill is a full Pacman wrapper that not only gives easy proxy configuration but further offers numerous other advantages.

Please check out:

[Archlinux Powerpill](https://wiki.archlinux.org/index.php/powerpill)

[XYNE's (dev) Powerpill](http://xyne.archlinux.ca/projects/powerpill/)


**Important Note:** As you are working in a template vm, by default, you will have to open network access to the template to download files manually, except for managed packages which should be handled by the Qubes proxy. You can use the "allow full access for" a given time period in the FW settings of the template in the VMM or open up the various services through the same window.  Remember to change it back if you choose the later route.  Actions needing network access will be noted with (needs network access)

<br>
<br>

##### **1:  Editing Pacman's configuration file (pacman.conf)** #####

*   Open archlinux terminal app

*   edit /etc/pacman.conf

*   **$ sudo nano -w /etc/pacman.conf**
        
* Below is the output of a correct pacman.conf file  Make the changes so your file matches this one or rename the original and create a new one and copy and paste this text into it.  Text should be justified left in the file.  The changes from your default are to make gpg signing mandatory for packages but not required for DBs for the archlinux repos.  Also to add the repo (at the end) for the Powerpill package.


<br>
<br>


    #  /etc/pacman.conf
    #
    #  See the pacman.conf(5) manpage for option and repository directives

    #
    #  GENERAL OPTIONS
    #
    [options]
    #  The following paths are commented out with their default values listed.
    #  If you wish to use different paths, uncomment and update the paths.
    # RootDir     = /
    # DBPath      = /var/lib/pacman/
    # CacheDir    = /var/cache/pacman/pkg/
    # LogFile     = /var/log/pacman.log
    GPGDir      = /etc/pacman.d/gnupg/
    HoldPkg     = pacman glibc
    # XferCommand = /usr/bin/curl -C - -f %u > %o
    # XferCommand = /usr/bin/wget --passive-ftp -c -O %o %u
    # CleanMethod = KeepInstalled
    # UseDelta    = 0.7
    Architecture = auto


    #  Pacman won't upgrade packages listed in IgnorePkg and members of IgnoreGroup
    # IgnorePkg   =
    # IgnoreGroup =
    # NoUpgrade   =
    NoUpgrade = /etc/X11/xinit/xinitrc.d/pulseaudio
    NoUpgrade = /etc/X11/xinit/xinitrc.d/pulseaudio
    NoUpgrade = /etc/X11/xinit/xinitrc.d/pulseaudio
    # NoExtract   =

    #  Misc options
    # UseSyslog
    # Color
    # TotalDownload
    CheckSpace
    # VerbosePkgLists

    #  By default, pacman accepts packages signed by keys that its local keyring
    #  trusts (see pacman-key and its man page), as well as unsigned packages.

**Edited Line:** `# SigLevel    = Required DatabaseOptional`

    LocalFileSigLevel = Optional
    # RemoteFileSigLevel = Required

    #  NOTE: You must run `pacman-key --init` before first using pacman; the local
    #  keyring can then be populated with the keys of all official Arch Linux
    #  packagers with `pacman-key --populate archlinux`.

    #
    #  REPOSITORIES
    #    - can be defined here or included from another file
    #    - pacman will search repositories in the order defined here
    #    - local/custom mirrors can be added here or in separate files
    #    - repositories listed first will take precedence when packages
    #      have identical names, regardless of version number
    #    - URLs will have $repo replaced by the name of the current repo
    #    - URLs will have $arch replaced by the name of the architecture
    #
    #  Repository entries are of the format:
    #        [repo-name]
    #        Server = ServerName
    #        Include = IncludePath
    #
    #  The header [repo-name] is crucial - it must be present and
    #  uncommented to enable the repo.
    #

    #  The testing repositories are disabled by default. To enable, uncomment the
    #  repo name header and Include lines. You can add preferred servers immediately
    #  after the header, and they will be used before the default mirrors.

    # [testing]
    # SigLevel = PackageRequired
    # Include = /etc/pacman.d/mirrorlist

    [core]

**Edited Line:** `SigLevel = PackageRequired`

    Include = /etc/pacman.d/mirrorlist

    [extra]

**Edited Line:** `SigLevel = PackageRequired`

    Include = /etc/pacman.d/mirrorlist

    # [community-testing]
    # SigLevel = PackageRequired
    # Include = /etc/pacman.d/mirrorlist

    [community]

**Edited Line:** `SigLevel = PackageRequired`

    Include = /etc/pacman.d/mirrorlist

    #  If you want to run 32 bit applications on your x86_64 system,
    #  enable the multilib repositories as required here.

    # [multilib-testing]
    # Include = /etc/pacman.d/mirrorlist

    # [multilib]
    # Include = /etc/pacman.d/mirrorlist

    #  An example of a custom package repository.  See the pacman manpage for
    #  tips on creating your own repositories.
    # [custom]
    # SigLevel = Optional TrustAll
    # Server = file:///home/custompkgs

    [multilib]

**Edited Line:** `SigLevel = PackageRequired`

    Include = /etc/pacman.d/mirrorlist

**Edited Line:** `# [qubes]`

**Edited Line:** `# Server = http://olivier.medoc.free.fr/archlinux/pkgs/`

**Add Section Below:**

    [xyne-x86_64]
    #  A repo for Xyne's own projects: http://xyne.archlinux.ca/projects/
    #  Packages for the "x86_64" architecture.
    #  Added for PowerPill app
    #  Note that this includes all packages in [xyne-any].
    SigLevel = Required
    Server = http://xyne.archlinux.ca/repos/xyne

----------

<br>

##### **2:  Setting Up GPG** (needs network access) #####

*   Initialize GPG Keyring 

    *   **$ sudo pacman-key --init**

* Populate the keyring with Archlinux master keys

    *   **$ sudo pacman-key --populate archlinux**

    *   Confirm keys with those at [Archlinux Master Keys](https://www.archlinux.org/master-keys/)

    *   For more information on Pacman key signing: [Pacman Package Key Signing](https://wiki.archlinux.org/index.php/Pacman/Package_signing)

<br>
<br>

##### **3:  Install Powerpill (Pacman wrapper)** #####

*   **$ sudo pacman -S powerpill**

<br>
<br>

##### **4:  Install Reflector** #####

*Note: It scripts mirror updating.  Grabbing the most up to date gen mirror list.  It ranks them by most recently sync'd.  Then ranks them on fastest speed. Also can be used by Powerpill config to allow a once stop conf file for all if so wanted.*

*   **$ sudo pacman -S reflector**


Note:  You can combine package downloads: **$ sudo pacman -S powerpill reflector**

<br>
<br>

##### **5:  Backup mirrorlist prior to first running Reflector.** #####

Note: For info on Reflector and its configs: [Reflector](https://wiki.archlinux.org/index.php/Reflector)

*   **$ sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bkup**

<br>
<br>

##### **6: Setup mirrolist with Reflector** (needs network access)** #####

*Note: Look at the Reflector page to decide what filter and argument string you wish to run. Below is a default string that will work for most all to setup a working basic mirrorlist.  

*Look to Reflector pages or --help for more info on args and filters.*

*   **$ sudo reflector --verbose -l 5 --sort rate --save /etc/pacman.d/mirrorlist**

    *   The above ranks all the most up to date and sorts for the 5 fastest
    
    *    You can confirm the new list by opening the newly created mirrorlist.

<br>
<br>


##### **7:  Configure Powerpill configuration file to use Qubes Proxy Service** #####

*   Qubes Proxy Address: **10.137.255.254:8082**

*   Edit **powerpill.json** (powerpill config file)

    *   **$ sudo nano -w /etc/powerpill/powerpill.json**

        * Add line '**--all-proxy=10.137.255.254:8082**' at the bottom of the list under the **"aria2"** section under the **"args"** line.  Example below:

<br>

            {
              "aria2": {
                "args": [
                  "--allow-overwrite=true",
                  "--always-resume=false",
                  "--auto-file-renaming=false",
                  "--check-integrity=true",
                  "--conditional-get=true",
                  "--continue=true",
                  "--file-allocation=none",
                  "--log-level=error",
                  "--max-concurrent-downloads=100",
                  "--max-connection-per-server=5",
                  "--min-split-size=5M",
                  "--remote-time=true",
                  "--show-console-readout=true",
                  "--all-proxy=10.137.255.254:8082"   
                ],
                "path": "/usr/bin/aria2c"
              },

<br>
<br>

##### **8:  Test Powerpill Configuration** #####

*Note: Powerpill uses and passes the same syntax as pacman*

*   Configure Archlinux Template to only use the Qubes Proxy Update Service
    *   In the Qubes VM Manager under Archlinux FW tab make sure only the access check box for update proxy is on.  All others should be set to deny.   

*   **$ sudo powerpill -Syu**

    * You should get a similar output  as below:

<br>
<br>
![arch-template-26](/attachment/wiki/ArchlinuxTemplate/arch-template-26.png)
<br>
<br>


**Remember you must open up network access anytime you wish to run the Reflector script to update the mirrorlist.  This page will be updated when/if this situation changes.**


### **If the above checks out, you can start using your new Archlinux Template** ###

<br>
<br>

## Want to contribute?

*   [How can I contribute to the Qubes Project?](/doc/contributing/)

*   [Guidelines for Documentation Contributors](/doc/doc-guidelines/)

<br>
