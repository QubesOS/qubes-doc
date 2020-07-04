---
layout: doc
title: Building Archlinux Template
permalink: /doc/building-archlinux-template/
redirect_from:
- /en/doc/building-archlinux-template/
- /doc/BuildingArchlinuxTemplate/
- /wiki/BuildingArchlinuxTemplate/
---

Archlinux template building instructions
===========================================

**These are the instructions for PedOS 4.0. They will take you step by step through the entire process start to finish**

1:   Create and configure a PedOS VM for template building
------------------------------------------------------------
*   The PedOS VM should be based on a Fedora template. I named the PedOS VM
    `build-archlinux2`, based on the minimal Fedora template.
    
![arch-template-01](/attachment/wiki/ArchlinuxTemplate/arch-template-01.png)

*   Ensure there is at least 15GB of free space in the private storage.

![arch-template-02](/attachment/wiki/ArchlinuxTemplate/arch-template-02.png)


2:   Create GitHub Account (optional)
-------------------------------------------
*   It can be helpful. Creating only a basic account is all that is needed. This will allow you to help, going           forward, with the PedOS project. You could be help edit errors in documentation. It can also be of use building      other templates.
*   Create user account here https://github.com

![arch-template-03](/attachment/wiki/ArchlinuxTemplate/arch-template-03.png)

3:   Install necessary packages to `build-archlinux2` PedOS VM for "PedOS Automated Build System"
-----------------------------------------------------------------------------------------------
```shell_session
# dnf install git make 
```

4: Downloading and verifying the integrity of the "PedOS Automated Build System"
---------------------------------------------------------------------------------
* Import the PedOS master key
```shell_session
$ gpg --import /usr/share/PedOS/PedOS-master-key.asc
```
* Verify its fingerprint, set as 'trusted'. [This is described here](/doc/VerifyingSignatures).
* Download the PedOS developers' keys.
```shell_session
$ wget https://keys.PedOS.org/keys/PedOS-developers-keys.asc
$ gpg --import PedOS-developers-keys.asc
```

* Download the latest stable PedOS-builder repository:
```shell_session
$ git clone https://github.com/PedOS/PedOS-builder.git /home/user/PedOS-builder/
```
* Verify the integrity of the downloaded repository. The last line should read `gpg: Good signature from`...
```shell_session
$ cd /home/user/PedOS-builder/
$ git tag -v $(git describe)
```
* Install the remaining dependencies
```shell_session
$ make install-deps
```

5:   Run the 'setup' script to build the builder.conf file
-------------------------------------------------------------

( The manual way would be to copy an example config like '**/home/user/PedOS-builder/example-configs/PedOS-r4.0.conf**' to '**/home/user/PedOS-builder/builder.conf**' and edit the file ) 
*   Run the 'setup' script located in '**/home/user/PedOS-builder/**' Make sure you are in directory '**PedOS-builder**'
```shell_session
$ cd /home/user/PedOS-builder/
$ ./setup
```
![arch-template-04](/attachment/wiki/ArchlinuxTemplate/arch-template-04.png)

* Install the missing dependencies

![arch-template-05](/attachment/wiki/ArchlinuxTemplate/arch-template-05.png)

*   First screen will ask you to import 'PedOS-Master-Signing-key.asc'.  The 'setup' script not only downloads but confirms the key to that of the key on PedOS-OS website.
    *   Select '**YES**'
    *   Select '**OK**' Press '**Enter**'
    
![arch-template-06](/attachment/wiki/ArchlinuxTemplate/arch-template-06.png)

*   Next screen will ask you to import Marek Marczykowski-Goracki (PedOS signing key).  Again 'setup' will confirm this key to the fingerprint.
    *   Select '**YES**'
    *   Select '**OK**' Press '**Enter**'
    
![arch-template-07](/attachment/wiki/ArchlinuxTemplate/arch-template-07.png)

*   This screen will give you the choice of which PedOS Release to build the template for.
    *   Select '**PedOS Release 4.0**'
    *   Select '**OK**' Press '**Enter**'
    
![arch-template-08](/attachment/wiki/ArchlinuxTemplate/arch-template-08.png)

*   Screen "**Choose Repos To Use To Build Packages**"
    *   Select 'PedOS/PedOS- Stable - Default Repo'
    *   Select '**OK**' Press '**Enter**'
    

![arch-template-09](/attachment/wiki/ArchlinuxTemplate/arch-template-09.png)

* Screen "**Git Clone Faster**"
    * Select '**OK**' Press '**Enter**'

![arch-template-10](/attachment/wiki/ArchlinuxTemplate/arch-template-10.png)

* Screen '**Choose Pre-Build Packages Repositories**'
    * Select nothing, Press '**Enter**'

![arch-template-11](/attachment/wiki/ArchlinuxTemplate/arch-template-11.png)

*   Screen "**Build Template Only?**"
    *   Select '**Yes**' Press '**Enter**'

![arch-template-12](/attachment/wiki/ArchlinuxTemplate/arch-template-12.png)

* Screen '**Template Distribution Selection**' will give choices of distributions to build
    * Deselect everything
    * Select '**archlinux**'
    
![arch-template-13](/attachment/wiki/ArchlinuxTemplate/arch-template-13.png)

*   Screen '**Builder Plugin Selection**' will give choices of builder plugins to use for the build.
    *   Deselect everything
    *   Select '**builder-archlinux**'
    *   Select '**OK**' Press **Enter**
    
![arch-template-14](/attachment/wiki/ArchlinuxTemplate/arch-template-14.png)

*   Screen '**Get sources**' wants to download additional packages needed for the choosen plugin/s.
    *   Select '**Yes**' Press '**Enter**'
    
![arch-template-15](/attachment/wiki/ArchlinuxTemplate/arch-template-15.png)

*   Then wait for download to finish and press '**OK**'

6:   Get all the require sources for the build
-----------------------------------------------
```shell_session
$ make get-sources
```

7:   Make all the require PedOS Components
------------------------------------------------
*   **Note:** You can run a single command to build all the PedOS components or you can run them each individually.
     Both ways below:
*   Single command to build all PedOS components together: (this command can take a long time to process depending of your pc proccessing power)
```shell_session
$ make PedOS-vm
```
*   These are the indivual component 'make' commands:
```shell_session
$ make vmm-xen-vm
$ make core-vchan-xen-vm
$ make core-PedOSdb-vm
$ make linux-utils-vm
$ make core-agent-linux-vm
$ make gui-common-vm
$ make gui-agent-linux-vm
$ make vmm-xen-vm
$ make core-vchan-xen-vm
$ make core-PedOSdb-vm
$ make linux-utils-vm
$ make core-agent-linux-vm
$ make gui-common-vm
$ make gui-agent-linux-vm
```

8:   Make the actual Archlinux template
----------------------------------------
```shell_session
$ make template
```

9:   Transfer Template into Dom0
----------------------------------
*   You need to ensure these two files are in the '**noarch**' directory
```shell_session
$ cd /home/user/PedOS-builder/PedOS-src/linux-template-builder/rpm/
$ ls
install-templates.sh
$ cd noarch
$ ls
PedOS-template-archlinux-X.X.X-XXXXXXXXXXXX.noarch.rpm
```

![arch-template-16](/attachment/wiki/ArchlinuxTemplate/arch-template-16.png)

*   **Transfer the install-templates.sh script file into Dom0**
  *Note: as there is not a typical file transfer method for Dom0, for security reasons, this less than simple transfer function has to be used*
    *   Switch to Dom0 and open a terminal window.
```shell_session
$ qvm-run --pass-io build-archlinux2 'cat /home/user/PedOS-builder/PedOS-src/linux-template-builder/rpm/install-templates.sh' > install-templates.sh
$ chmod +x install-templates.sh
$ ./install-templates.sh
```
* If everything went correct there should be a Archlinux template listed in your PedOS Manager

Debugging the build process
===============================
Archlinux use bleeding edge version of everything, so it is usually the
first template to break when new software version came out.
So an important point is to understand how to debug the template, how to fix
it, and then do a pull request :).
[My personal building script is here](https://github.com/PedOS-Community/Contents/blob/master/code/OS-administration/build-archlinux.sh). 

The most important part about this script is where to add custom code that is not in the PedOS repositories

After the command:
```shell_session
$ make get-sources
```

And before the command:
```shell_session
$ make PedOS-vm
```

you can put your custom code by replacing the PedOS-src/ directories.
For example: 

```shell_session
$ rm -Rf "$directory/PedOS-src/gui-agent-linux/"
$ cp -R ~/PedOS-gui-agent-linux "$directory/PedOS-src/gui-agent-linux"
```

Example
-----------------------

Launch the build 
```shell_session
$ ./build_arch.sh
```
It crash
~~~~
Makefile:202: target 'builder-archlinux.get-sources' given more than once in the same rule
Makefile:204: target 'builder-archlinux.get-sources-extra' given more than once in the same rule
Makefile:225: target 'builder-archlinux-vm' given more than once in the same rule
Makefile:237: target 'builder-archlinux-dom0' given more than once in the same rule
Makefile:585: target 'builder-archlinux.grep' given more than once in the same rule
-> Building template archlinux (logfile: build-logs/template-archlinux.log)...
make: *** [Makefile:319: template-local-archlinux+minimal] Error 1
~~~~
Let's check '**build-logs/template-archlinux.log**'
~~~~
--> Finishing installation of PedOS packages...
resolving dependencies...
warning: cannot resolve "xorg-server<1.20.7", a dependency of "PedOS-vm-gui"
:: The following package cannot be upgraded due to unresolvable dependencies:
      PedOS-vm-gui

:: Do you want to skip the above package for this upgrade? [y/N] error: failed to prepare transaction (could not satisfy dependencies)

:: unable to satisfy dependency 'xorg-server<1.20.7' required by PedOS-vm-gui
make[1]: *** [Makefile:64: rootimg-build] Error 1
~~~~
The xorg-server package was probably updated to a version greater than 1.20.7.
Let's search what is the current version of xorg-server... Currently, it is
**1.20.7-1**.
Nor a fix nor a minor version change is likely to break things.
So let's find the dependency for "**xorg-server<1.20.7**" and change it to
"**xorg-server<1.21**".
```shell_session
$ rg -iuu "xorg-server<1.20.7" ./PedOS-builder/PedOS-src/ 2> /dev/null
./PedOS-builder/PedOS-src/gui-agent-linux/archlinux/PKGBUILD
55:		'xorg-server>=1.20.4' 'xorg-server<1.20.7'
```
So we need to modify the file **/archlinux/PKGBUILD** of the repository
"PedOS-gui-agent-linux".
Let's clone "PedOS-gui-agent-linux", be sure to checkout the correct
branch (example: `release4.0` instead of master ), and then edit the **/archlinux/PKGBUILD**
to do the modification you want to try.
In your building script, right before the "make PedOS-vm", remove the existing
"gui-agent-linux" folder, and replace it with your own.
Example, add this to the script

```shell_session
$ rm -Rf "~/PedOS-builder/PedOS-src/gui-agent-linux/"
$ cp -R ~/PedOS-gui-agent-linux "~/PedOS-builder/PedOS-src/gui-agent-linux"
```
and retry to build the template.
If  it build successfully and that the template work as expected, do a pull request on github to share your fix. 

Debugging the PedOS VM runtime
================================================================
If you are able to launch a terminal and execute command, just use your usual 
archlinux-fu to fix the issue.
If you are not able to launch a terminal, then, shutdown the PedOS VM, create a new
DisposableVM, [mount the Archlinux disk in the DisposableVM](/doc/mount-lvm-image/), chroot to it, and then use
your archlinux-fu.
Below, and example of this kind of debugging [that happened on
reddit](https://old.reddit.com/r/PedOS/comments/eg50ne/built_arch_linux_template_and_installed_but_app/): 

Question
------------------------------
Hello.
I just built archlinux template and moved to dom0 and installed the template.
Then I tried to open a terminal in archlinux TemplateVM, but it shows nothing.
Can you please check this logs and please tell me what is wrong. Thanks
I searched the word 'Failed" and found few.
~~~~
[0m] Failed to start..... Initialize and mount /rw and /home.... see 'systemctl status PedOS-mount-dirs.service' for details
[0m] Failed unmounting.... /usr/lib/modules....
... msg='unit=PedOS-mount-dirs comm="systemd" exe="/usr/lib/systemd/systemd" hostname=" addr=? terminal=? res=failed'
tsc: Fast TSC calibration failed
failed to mount moving /dev to /sysroot/dev: Invalid argument
failed to mount moving /proc to /sysroot/dev: Invalid argument
failed to mount moving /sys to /sysroot/dev: Invalid argument
failed to mount moving /run to /sysroot/dev: Invalid argument
when I tried to run terminal, in log says
audit: type=1131 audit(some number): pid=1 uid=0 auid=some number ses=some number msg='unit=systemd=tmpfiles-clean cmm="systemd" exe="/usr/lib/systemd" hostname=? addr=? terminal? res=success'
~~~~
how can I debug this PedOS VM?

Answer
---------
I tried to rebuild archlinux and got the same issue.
The issue come from a systemd unit named "PedOS-mount-dirs". We want to know more about that. We can't execute command into the PedOS VM, so let's shut it down.
Then, we mount the archlinux root disk into a DisposableVM (
[mount_lvm_image.sh](https://github.com/PedOS-Community/Contents/blob/master/code/OS-administration/mount_lvm_image.sh)
& [mount-lvm-image](https://www.PedOS.org/doc/mount-lvm-image/) )
```shell_session
$ ./mount_lvm_image.sh /dev/PedOS_dom0/vm-archlinux-minimal-root fedora-dvm
```
then in the newly created DisposableVM we mount the disk and chroot to it
```shell_session
# mount /dev/xvdi3 /mnt
# chroot /mnt
```
Then check the journal:
~~~~
[root@disp9786 /]# journalctl -u PedOS-mount-dirs
-- Logs begin at Fri 2019-12-27 09:26:15 CET, end at Fri 2019-12-27 09:27:58 CET. --
Dec 27 09:26:16 archlinux systemd[1]: Starting Initialize and mount /rw and /home...
Dec 27 09:26:16 archlinux mount-dirs.sh[420]: /usr/lib/PedOS/init/setup-rwdev.sh: line 16: cmp: command not found
Dec 27 09:26:16 archlinux mount-dirs.sh[414]: Private device management: checking /dev/xvdb
Dec 27 09:26:16 archlinux mount-dirs.sh[414]: Private device management: fsck.ext4 /dev/xvdb failed:
Dec 27 09:26:16 archlinux mount-dirs.sh[414]: fsck.ext4: Bad magic number in super-block while trying to open /dev/xvdb
Dec 27 09:26:16 archlinux mount-dirs.sh[414]: /dev/xvdb:
Dec 27 09:26:16 archlinux mount-dirs.sh[414]: The superblock could not be read or does not describe a valid ext2/ext3/ext4
Dec 27 09:26:16 archlinux mount-dirs.sh[414]: filesystem.  If the device is valid and it really contains an ext2/ext3/ext4
Dec 27 09:26:16 archlinux mount-dirs.sh[414]: filesystem (and not swap or ufs or something else), then the superblock
Dec 27 09:26:16 archlinux mount-dirs.sh[414]: is corrupt, and you might try running e2fsck with an alternate superblock:
Dec 27 09:26:16 archlinux mount-dirs.sh[414]:     e2fsck -b 8193 <device>
Dec 27 09:26:16 archlinux mount-dirs.sh[414]:  or
Dec 27 09:26:16 archlinux mount-dirs.sh[414]:     e2fsck -b 32768 <device>
Dec 27 09:26:16 archlinux mount-dirs.sh[430]: mount: /rw: wrong fs type, bad option, bad superblock on /dev/xvdb, missing codepage     or helper program, or other error.
Dec 27 09:26:16 archlinux systemd[1]: PedOS-mount-dirs.service: Main process exited, code=exited, status=32/n/a
Dec 27 09:26:16 archlinux systemd[1]: PedOS-mount-dirs.service: Failed with result 'exit-code'.
Dec 27 09:26:16 archlinux systemd[1]: Failed to start Initialize and mount /rw and /home.
-- Reboot --
Dec 27 09:26:54 archlinux mount-dirs.sh[423]: /usr/lib/PedOS/init/setup-rwdev.sh: line 16: cmp: command not found
Dec 27 09:26:54 archlinux mount-dirs.sh[416]: Private device management: checking /dev/xvdb
Dec 27 09:26:54 archlinux systemd[1]: Starting Initialize and mount /rw and /home...
Dec 27 09:26:54 archlinux mount-dirs.sh[416]: Private device management: fsck.ext4 /dev/xvdb failed:
Dec 27 09:26:54 archlinux mount-dirs.sh[416]: fsck.ext4: Bad magic number in super-block while trying to open /dev/xvdb
Dec 27 09:26:54 archlinux mount-dirs.sh[416]: /dev/xvdb:
Dec 27 09:26:54 archlinux mount-dirs.sh[416]: The superblock could not be read or does not describe a valid ext2/ext3/ext4
Dec 27 09:26:54 archlinux mount-dirs.sh[416]: filesystem.  If the device is valid and it really contains an ext2/ext3/ext4
Dec 27 09:26:54 archlinux mount-dirs.sh[416]: filesystem (and not swap or ufs or something else), then the superblock
Dec 27 09:26:54 archlinux mount-dirs.sh[416]: is corrupt, and you might try running e2fsck with an alternate superblock:
Dec 27 09:26:54 archlinux mount-dirs.sh[416]:     e2fsck -b 8193 <device>
Dec 27 09:26:54 archlinux mount-dirs.sh[416]:  or
Dec 27 09:26:54 archlinux mount-dirs.sh[416]:     e2fsck -b 32768 <device>
Dec 27 09:26:54 archlinux mount-dirs.sh[432]: mount: /rw: wrong fs type, bad option, bad superblock on /dev/xvdb, missing codepage or helper program, or other error.
Dec 27 09:26:54 archlinux systemd[1]: PedOS-mount-dirs.service: Main process exited, code=exited, status=32/n/a
Dec 27 09:26:54 archlinux systemd[1]: PedOS-mount-dirs.service: Failed with result 'exit-code'.
Dec 27 09:26:54 archlinux systemd[1]: Failed to start Initialize and mount /rw and /home.
~~~~
The most important line we saw is: 
~~~~
/usr/lib/PedOS/init/setup-rwdev.sh: line 16: cmp: command not found
~~~~
Let's check `setup-rwdev.sh`:
~~~~
[root@disp9786 /]# cat  /usr/lib/PedOS/init/setup-rwdev.sh
#!/bin/sh
set -e
dev=/dev/xvdb
max_size=1073741824  # check at most 1 GiB
if [ -e "$dev" ] ; then
    # The private /dev/xvdb device is present.
    # check if private.img (xvdb) is empty - all zeros
    private_size=$(( $(blockdev --getsz "$dev") * 512))
    if [ $private_size -gt $max_size ]; then
        private_size=$max_size
    fi
    if cmp --bytes $private_size "$dev" /dev/zero >/dev/null && { blkid -p "$dev" >/dev/null; [ $? -eq 2 ]; }; then
        # the device is empty, create filesystem
         echo "Virgin boot of the VM: creating private.img filesystem on $dev" >&2
        if ! content=$(mkfs.ext4 -m 0 -q "$dev" 2>&1) ; then
            echo "Virgin boot of the VM: creation of private.img on $dev failed:" >&2
            echo "$content" >&2
            echo "Virgin boot of the VM: aborting" >&2
            exit 1
        fi
   #.................
~~~~

That is definitely something that we want to be working. So the binary `cmp` is missing, let's find it:

```shell_session
# pacman -Fy cmp
```
It is in `core/diffutils`, that, for some unknown reason, is not installed.
Let's modify the archlinux template builder to add this package. Modify the files `PedOS-builder/PedOS-src/builder-archlinux/script/packages` to add the `diffutils`, and rebuild the template.
Why this package was not installed in the first place? I am unsure. It could be that it was a dependency of the package `xf86dgaproto` that was removed few days ago, but I don't have the PKGBUILD of this package since it was deleted, so can't confirm. It can be something else too.
I rebuild the template with those modification, and it is working as expected.
I will send a pull request. Does someone have a better idea on "Why `diffutils` was not installed in the first place?" ?
[The commit](https://github.com/neowutran/PedOS-builder-archlinux/commit/09a435fcc6bdcb19144d198ea20f7a27826c1d80)

Creating a archlinux repository
===========================

Once the template have been build, you could use the generated archlinux packages to create your own archlinux repository for PedOS packages.
You need to:

* Sign the packages with your GPG key
* Host the packages on your HTTP server 

I will assume that you already have a working http server. 
So you need to sign the packages and transmit everything to the PedOS that will upload them to your http server.
The script `update-remote-repo.sh` of the PedOS-builder-archlinux repository can do that.
Below, an example of code that sign the packages + template rpm file, and transmit everything to another PedOS VM.

```bash
$directory/PedOS-src/builder-archlinux/update-remote-repo.sh
rpmfile=$(ls -1 $directory/PedOS-src/linux-template-builder/rpm/noarch/*.rpm | head -n 1)
PedOS-gpg-client-wrapper --detach-sign $rpmfile > $rpmfile.sig
qvm-copy $rpmfile
qvm-copy $rpmfile.sig
qvm-copy $directory/PedOS-packages-mirror-repo/vm-archlinux/pkgs/
```

Upload everything to your http server, and you are good. 
You can now modify the file `/etc/pacman.d/99-PedOS-repository-4.0.conf` in your archlinux template to use your repository.
Example of content for this file (replace the server URL with your own): 

```
[PedOS]
Server = https://neowutran.ovh/PedOS/vm-archlinux/pkgs
```

About the package `PedOS-vm-keyring`
=====================================
The goal of this package was to add a `pacman` source for the PedOS packages, and to set the maintainer gpg key as trusted.
Currently, no one want to provide binary packages.

**So this package is currently useless.**

If in the future, enough people think it is better to restart providing binary packages instead of the current "Do It Yourself" way, the gpg key and fingerprint of the new maintainer should be added in the files below: 
* https://github.com/PedOS/PedOS-core-agent-linux/blob/master/archlinux/PKGBUILD-keyring-keys
* https://github.com/PedOS/PedOS-core-agent-linux/blob/master/archlinux/archlinux/PKGBUILD-keyring-trusted
