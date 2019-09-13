---
layout: doc
title: Building Archlinux Template
redirect_from:
- /doc/building-archlinux-template/
- /en/doc/building-archlinux-template/
- /doc/BuildingArchlinuxTemplate/
- /wiki/BuildingArchlinuxTemplate/
---

# Archlinux template building instructions

**These are the instructions for Qubes 3.2. They will take you step by step through the entire process start to finish**

*Note: These instructions have not been tested for Qubes 3.1. However they could be working.*

*Note: No binary package for the archlinux template exists for Qubes 3.1.*

## 1:   Create and configure VM to use for template building

*   The VM should be based on a Fedora template. It's best to use a standalone VM. I created a standalone VM based on
    the Fedora 23 template. I named the VM “**development**”. These instructions assume a standalone VM based on a       Fedora template is being used.
<br>
<br>
![arch-template-01](/attachment/wiki/ArchlinuxTemplate/arch-template-01.png)
<br>
<br>
*   Ensure there is at least 25GB preferably 30GB of free space in the private storage. I made the private storage 30GB to be safe.
<br>
<br>
![arch-template-02](/attachment/wiki/ArchlinuxTemplate/arch-template-02.png)
<br>
<br>

*Note: Unless otherwise noted,  all commands are from within the “development” VM or whatever you named your standalone VM used for building the template.*

## 2:   Create GitHub Account (optional)

*   It can be helpful. Creating only a basic account is all that is needed. This will allow you to help, going           forward, with the Qubes project. You could be help edit errors in documentation. It can also be of use building      other templates.

*   Create user account here https://github.com
<br>
<br>
![arch-template-03](/attachment/wiki/ArchlinuxTemplate/arch-template-03.png)
<br>
<br>

## 3:   Install necessary packages to 'development' VM for "Qubes Automated Build System"

*   Necessary packages to install:

    *   git

    *   createrepo

    *   rpm-build

    *   make

    *   rpmdevtools

    *   python2-sh

    *   dialog

    *   rpm-sign

    *	gnupg


*   The tools can usually be installed all together with the following terminal command string:

    *   **$ sudo dnf install git createrepo rpm-build make wget rpmdevtools python2-sh dialog rpm-sign gnupg**
<br>
<br>
![arch-template-04](/attachment/wiki/ArchlinuxTemplate/arch-template-04.png)
<br>
<br>

## 4: Downloading and verifying the integrity of the "Qubes Automated Build System"

* Import the Qubes master key

      gpg --keyserver pgp.mit.edu --recv-keys 0xDDFA1A3E36879494

* Verify its fingerprint, set as 'trusted'. [This is described here](/doc/VerifyingSignatures).

* Download the Qubes developers' keys.

      wget https://keys.qubes-os.org/keys/qubes-developers-keys.asc
      gpg --import qubes-developers-keys.asc

* Download the latest stable qubes-builder repository:

      git clone git://github.com/QubesOS/qubes-builder.git qubes-builder

  ![arch-template-05](/attachment/wiki/ArchlinuxTemplate/arch-template-05.png)

* Copy your gpg keyrings to your local copy of the repository. (Otherwise you will be asked to download the keys again.)

      # Execute the following commands in your home directory.
      # It is assumed that the path to the repository is '~/qubes-builder'.
      mkdir -p qubes-builder/keyrings/git 
      cp -t qubes-builder/keyrings/git/ .gnupg/pubring.gpg .gnupg/trustdb.gpg

* Verify the integrity of the downloaded repository. The last line should read `gpg: Good signature from`...

      cd qubes-builder
      git tag -v `git describe`


## 5:   Configuring setup script to create builder.conf file

*   You will be creating the builder.conf file which tells where and what to use.   The most automated, and in this case the easiest, way to create this is to use the script that is provided in Qubes Builder.  Its named '**setup**'.  Before running the script you need to edit one file it uses.

    *In the future this should not be needed once a change is made to the 'setup' script.*

    *   Edit the '**qubes-os-r3.2.conf**' which is found in **/home/user/qubes-builder/example-configs**  Use the text editor of your choice.

        *   **$ cd /home/user/qubes-builder/example-configs/**

        *   **$ nano -W qubes-os-r3.2.conf** or **$ gedit qubes-os-r3.2.conf** or etc….
<br>
<br>
![arch-template-06](/attachment/wiki/ArchlinuxTemplate/arch-template-06.png)
<br>
<br>
        *   Go to the first line containing '**DISTS_VM ?= fc23**' it will be preceeded by line '**DIST_DOM0 ?= fc20**'.  Remove '**fc23**' or whatever is listed there leaving only '**DISTS_VM ?=**'. Then save the file and close the text editor.
<br>
<br>
![arch-template-07](/attachment/wiki/ArchlinuxTemplate/arch-template-07.png)
<br>
<br>
<br>

## 6:   Run the 'setup' script to build the builder.conf file

*   Run the 'setup' script located in '**/home/user/qubes-builder/**' Make sure you are in directory '**qubes-builder**'

    *   **$ cd /home/user/qubes-builder/**

    *   **$ ./setup**
<br>
<br>
![arch-template-08](/attachment/wiki/ArchlinuxTemplate/arch-template-08.png)
<br>
<br>
        *   First screen will ask you to import 'Qubes-Master-Signing-key.asc'.  The 'setup' script not only downloads but confirms the key to that of the key on Qubes-OS website.

            *   Select '**YES**'
            *   Select '**OK**' Press '**Enter**'
<br>
<br>
![arch-template-09](/attachment/wiki/ArchlinuxTemplate/arch-template-09.png)
<br>
<br>

        *   Next screen will ask you to import Marek Marczykowski-Goracki (Qubes OS signing key).  Again 'setup' will confirm this key to the fingerprint.

            *   Select '**YES**'
            *   Select '**OK**' Press '**Enter**'
<br>
<br>
![arch-template-10](/attachment/wiki/ArchlinuxTemplate/arch-template-10.png)
<br>
<br>

        *   This screen will give you the choice of which Qubes Release to build the template for.

            *   Select '**Qubes Release 3.2**'
            *   Select '**OK**' Press '**Enter**'
<br>
<br>
![arch-template-11](/attachment/wiki/ArchlinuxTemplate/arch-template-11.png)
<br>
<br>

        *   Screen "**Choose Repos To Use To Build Packages**"

            *   Select 'QubesOS/qubes- Stable - Default Repo'
            *   Select '**OK**' Press '**Enter**'
<br>
<br>
![arch-template-12](/attachment/wiki/ArchlinuxTemplate/arch-template-12.png)
<br>
<br>

        *   Screen "**Build Template Only?**"

            *   Select '**Yes**' Press '**Enter**'
<br>
<br>
![arch-template-12](/attachment/wiki/ArchlinuxTemplate/arch-template-12a.png)
<br>
<br>

        *   Screen '**Builder Plugin Selection**' will give choices of builder plugins to use for the build.

            *   Deselect '**Fedora**'

            *   Deselect '**mgmt_salt**'

            *   Select '**builder-archlinux**'

            *   Select '**OK**' Press **Enter**
<br>
<br>
![arch-template-13](/attachment/wiki/ArchlinuxTemplate/arch-template-13.png)
<br>
<br>

        *   Screen '**Get sources**' wants to download additional packages needed for the choosen plugin/s.

            *   Select '**Yes**' Press '**Enter**'
<br>
<br>
![arch-template-14](/attachment/wiki/ArchlinuxTemplate/arch-template-14.png)
<br>
<br>

        *   Then wait for download to finish and press '**OK**'
<br>
<br>
![arch-template-14](/attachment/wiki/ArchlinuxTemplate/arch-template-15.png)
<br>
<br>

        *   Screen '**Template Distribution Selection**' allows you to choose the actual template/s you wish to build.

            *   Scroll Down to the very bottom (it is off the screen at first)

            *   Select '**archlinux**'

            *   Select '**OK**' Press '**Enter**'
<br>
<br>
![arch-template-16](/attachment/wiki/ArchlinuxTemplate/arch-template-16.png)
<br>
<br>

            *Note: 'Setup' will close and will output the text of the created build.conf file as well as the needed                    **make** commands to build the template*
<br>
<br>
![arch-template-17](/attachment/wiki/ArchlinuxTemplate/arch-template-17.png)
<br>
<br>

## 7:   Install all the dependencies

*Note: make sure you are in the “qubes-builder” directory to run the following cmds*

*   **$ make install-deps**
<br>
<br>
![arch-template-18](/attachment/wiki/ArchlinuxTemplate/arch-template-18.png)
<br>
<br>

## 8:   Get all the require sources for the build: (Note: this may take some time)

*   **$ make get-sources**
<br>
<br>
![arch-template-19](/attachment/wiki/ArchlinuxTemplate/arch-template-19.png)
<br>
<br>
<br>

## 9:   Make all the require Qubes Components

*   **Note:** You can run a single command to build all the Qubes components or you can run them each individually.
     Both ways below:

    *   Single command to build all Qubes components together: (this command can take a long time to process depending of your pc proccessing power)

        *   **$ make qubes-vm**
        <br>
        <br>
![arch-template-20](/attachment/wiki/ArchlinuxTemplate/arch-template-20.png)
        <br>
        <br>


            *   These are the indivual component 'make' commands:

                *   **$ make vmm-xen-vm**

                *   **$ make core-vchan-xen-vm**

                *   **$ make core-qubesdb-vm**

                *   **$ make linux-utils-vm**

                *   **$ make core-agent-linux-vm**

                *   **$ make gui-common-vm**

                *   **$ make gui-agent-linux-vm**
<br>
<br>


## 10:   Make the actual Archlinux template

*   **$ make template**
<br>
<br>
![arch-template-21](/attachment/wiki/ArchlinuxTemplate/arch-template-21.png)
<br>
<br>

## 11:   Transfer Template into Dom0

*   You need to ensure these two files are in the '**noarch**' directory

    *   **$ cd /home/user/qubes-builder/qubes-src/linux-template-builder/rpm/**

    *   **$ ls**   *(confirm the below two files are there)*

        *   **install-templates.sh**   (script to install template in dom0)

    *   **$ cd noarch**

    *   **$ ls**

        *   **qubes-template-archlinux-X.X.X-XXXXXXXXXXXX.noarch.rpm**  (this is the template package 'X' replaces version and build digits)
<br>
<br>
![arch-template-22](/attachment/wiki/ArchlinuxTemplate/arch-template-22.png)
<br>
<br>

*   **Transfer the install-templates.sh script file into Dom0**
  *Note: as there is not a typical file transfer method for Dom0, for security reasons, this less than simple transfer function has to be used*

    *   Switch to Domo and open a terminal window.

    **Note:** Take care when entering these cmd strings.  They are very long and have a number of characters that are easy to mix '**-**' vs '**.**' '**<u>T</u>emplates** (correct) vs **<u>t</u>emplates** (wrong) or **Template_**'(also wrong)  This script will also take care of transfering the actual template.rpm to Dom0 as well.

       *   **$ qvm-run --pass-io development 'cat /home/user/qubes-builder/qubes-src/linux-template-builder/rpm/install-templates.sh' > install-templates.sh**
       
       *   **$ chmod +x install-templates.sh**
       
       *   **$ ./install-templates.sh**

<br>
<br>
![arch-template-23](/attachment/wiki/ArchlinuxTemplate/arch-template-23.png)
<br>
<br>
![arch-template-24](/attachment/wiki/ArchlinuxTemplate/arch-template-24.png)
<br>
<br>

* If everything went correct there should be a Archlinux template listed in your Qubes VM Manager *


# Known problems in building with Qubes R3.X

## Build fails when fetching qubes-mgmt-salt

The `qubes-mgmt-salt` repo is not currently forked under the marmarek user on
GitHub, to whom the above instructions set the `GIT_PREFIX`.  As Archlinux is
not yet supported by mgmt-salt, simply leave it out of the build (when building
the Archlinux template on its own) by appending the following to your `override.conf` file:

`BUILDER_PLUGINS := $(filter-out mgmt-salt,$(BUILDER_PLUGINS))`

## The nm-applet (network manager icon) fails to start when archlinux is defined as a template-vm

In fact /etc/dbus-1/system.d/org.freedesktop.NetworkManager.conf does not allow a standard user to run network manager clients. To allow this, one need to change inside \<policy context="default"\>:

`<deny send_destination="org.freedesktop.NetworkManager"/>`

to

`<allow send_destination="org.freedesktop.NetworkManager"/>`

## DispVM, Yum proxy and most Qubes addons (thunderbird ...) have not been tested at all

## Error when building the gui-agent-linux with pulsecore error

```
module-vchan-sink.c:62:34: fatal error: pulsecore/core-error.h: No such file or directory
 #include <pulsecore/core-error.h>
```

This error is because Archlinux update package too quickly. Probably, a new version of pulseaudio has been released, but the qubes team has not imported the new development headers yet.

You can create fake new headers just by copying the old headers:
```
cd qubes-builder/qubes-src/gui-agent-linux/pulse
ls
cp -r pulsecore-#lastversion pulsecore-#archlinuxversion
```

You can check the current archlinux pulseaudio version like this:

`sudo chroot chroot-archlinux/ pacman -Qi pulseaudio`

## chroot-archlinux/dev/pts has not been unmounted

This is a known problem when there are errors during building. Check what is mounted using the command mount (with no parameters). Just unmount what you can (or reboot your vm if you are too lazy :) )

# Known problems in building with Qubes R2-B2

## xen-vmm-vm fail to build with a PARSETUPLE related error (FIXED)

Commenting out "\#define HAVE\_ATTRIBUTE\_FORMAT\_PARSETUPLE" from chroot\_archlinux/usr/include/python2.7/pyconfig.h fixes the problem, but it isn't the right solution [1]...

A better fix is planned for the next python release (the bug is considered release blocking), and will be updated in archlinux chroot as soon as available.

[1] [https://bugs.python.org/issue17547](https://bugs.python.org/issue17547)

## The boot process fails without visible errors in the logs, but spawn a recovery shell

The problem is new conflict between systemd and the old sysvinit style. To fix this, you can change the master xen template in dom0 to remove sysvinit remains: Edit **INSIDE DOM0** /usr/share/qubes/vm-template.conf, and change the variable 'extra' that contains the kernel variables: from:

`extra="ro nomodeset 3 console=hvc0 rd_NO_PLYMOUTH {kernelopts}"`

to:

`extra="ro nomodeset console=hvc0 rd_NO_PLYMOUTH {kernelopts}"`

## Qubes-OS is now using different xenstore variable names, which makes to archlinux VM failing to boot

Apply the following fix in the template to revert the variable name to the old Qubes version.

You can edit the template the following way:

```
sudo mkdir /mnt/vm
sudo mount /var/lib/qubes/vm-templates/archlinux-x64/root.img /mnt/vm
sudo chroot /mnt/vm
```

Then apply the fix:

```
sudo sed 's:qubes-keyboard:qubes_keyboard:g' -i /etc/X11/xinit/xinitrc.d/qubes-keymap.sh

sudo sed 's:qubes-netvm-domid:qubes_netvm_domid:g' -i /etc/NetworkManager/dispatcher.d/30-qubes-external-ip
sudo sed 's:qubes-netvm-external-ip:qubes_netvm_external_ip:g' -i /etc/NetworkManager/dispatcher.d/30-qubes-external-ip

sudo sed 's:qubes-netvm-network:qubes_netvm_network:g' -i /usr/lib/qubes/init/network-proxy-setup.sh
sudo sed 's:qubes-netvm-gateway:qubes_netvm_gateway:g' -i /usr/lib/qubes/init/network-proxy-setup.sh
sudo sed 's:qubes-netvm-netmask:qubes_netvm_netmask:g' -i /usr/lib/qubes/init/network-proxy-setup.sh
sudo sed 's:qubes-netvm-secondary-dns:qubes_netvm_secondary_dns:g' -i /usr/lib/qubes/init/network-proxy-setup.sh

sudo sed 's:qubes-vm-type:qubes_vm_type:g' -i /usr/lib/qubes/init/qubes-sysinit.sh

sudo sed 's:qubes-ip:qubes_ip:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-netmask:qubes_netmask:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-gateway:qubes_gateway:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-secondary-dns:qubes_secondary_dns:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-netvm-network:qubes_netvm_network:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-netvm-gateway:qubes_netvm_gateway:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-netvm-netmask:qubes_netvm_netmask:g' -i /usr/lib/qubes/setup-ip
sudo sed 's:qubes-netvm-secondary-dns:qubes_netvm_secondary_dns:g' -i /usr/lib/qubes/setup-ip

sudo sed 's:qubes-iptables-domainrules:qubes_iptables_domainrules:g' -i /usr/bin/qubes-firewall
sudo sed 's:qubes-iptables-header:qubes_iptables_header:g' -i /usr/bin/qubes-firewall
sudo sed 's:qubes-iptables-error:qubes_iptables_error:g' -i /usr/bin/qubes-firewall
sudo sed 's:qubes-iptables:qubes_iptables:g' -i /usr/bin/qubes-firewall

sudo sed 's:qubes-netvm-domid:qubes_netvm_domid:g' -i /usr/bin/qubes-netwatcher
sudo sed 's:qubes-netvm-external-ip:qubes_netvm_external_ip:g' -i /usr/bin/qubes-netwatcher
sudo sed 's:qubes-vm-updateable:qubes_vm_updateable:g' -i /usr/lib/qubes/qubes_trigger_sync_appmenus.sh

sudo sed 's:qubes-vm-type:qubes_vm_type:g' -i /usr/bin/qubes-session
sudo sed 's:qubes-vm-updateable:qubes_vm_updateable:g' -i /usr/bin/qubes-session
```

Do not forgot to unmount the VM:

`umount /mnt/vm`

## Installing the template in dom0 fails because of a missing dependency (qubes-core-dom0-linux)

Again you built a template based on a recent Qubes API which has not been released yet. So skip the dependency for now

`sudo rpm -U --nodeps yourpackage.rpm`


# Qubes Mailing List Threads on the Archlinux build process

*   [Qubes-Devel](https://groups.google.com/forum/#!forum/qubes-devel): [Qubes Builder failed Archlinux repository is missing](https://groups.google.com/forum/#!topic/qubes-devel/tIFkS-rPVx8)

*   [Qubes-Users](https://groups.google.com/forum/#!forum/qubes-users): [Trying to compile archlinux template](https://groups.google.com/forum/#!topic/qubes-users/7wuwr3LgkQQ)

<br>
