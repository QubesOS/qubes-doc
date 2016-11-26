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

Archlinux Template
===============

Archlinux template is one of the templates made by Qubes community. It should
be considered experimental as Qubes developers team use mainly Fedora-based VMs
to test new features/updates.

Main maintainer of this template is [Olivier Médoc](mailto:o_medoc@yahoo.fr).

<br>

## Instructions ##

<br>
**These are the instructions for Qubes 3.2. They will take you step by step through the entire process start to finish**

*Note: Currently there are no binary packages and it must be compiled from source using the instructions below.*

<br>
<br>
<br>

#### **1:   Create and configure VM to use for template building:** ####

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
<br>
<br>
<br>

##### **2:   Create GitHub Account (optional):** #####

*   It can be helpful. Creating only a basic account is all that is needed. This will allow you to help, going           forward, with the Qubes project. You could be help edit errors in documentation. It can also be of use building      other templates.
    
*   Create user account here https://github.com
<br>
<br>
![arch-template-03](/attachment/wiki/ArchlinuxTemplate/arch-template-03.png)    
<br>
<br>
<br>

##### **3:   Install necessary packages to 'development' VM for "Qubes Automated Build System":** #####

*   Necessary packages to install:

    *   git
    
    *   createrepo
    
    *   rpm-build
    
    *   make
    
    *   rpmdevtools

    *   python-sh

    *   dailog

    *   rpm-sign
<br>


*   The tools can usually be installed all together with the following terminal command string:

    *   **$ sudo dnf install git createrepo rpm-build make wget rpmdevtools python-sh dialog rpm-sign**
<br>
<br>
![arch-template-04](/attachment/wiki/ArchlinuxTemplate/arch-template-04.png)
<br>
<br>
<br>

##### **4:   Installing the "Qubes Automated Build System":** #####

*   Download the latest stable qubes-builder repository:

    *   $ **git clone https://github.com/QubesOS/qubes-builder.git**
<br>
<br>
![arch-template-05](/attachment/wiki/ArchlinuxTemplate/arch-template-05.png)
<br>
<br>


*   You will now have the Qubes Builder System environment installed in the directory below:

    *   **/home/user/qubes-builder/**
<br>
<br>

##### **5:   Configuring setup script to create builder.conf file:** #####

*   You will be creating the builder.conf file which tells where and what to use.   The most automated, and in this case the easiest, way to create this is to use the script that is provided in Qubes Builder.  Its named '**setup**'.  Before running the script you need to edit one file it uses.
   
    *In the future this should not be needed once a change is made to the 'setup' script.*

    *   Edit the '**qubes-os-r3.2.conf**' which is found in **/home/user/qubes-builder/example-configs**  Use the text editor of your choice.
    
        *   **$ cd /home/user/qubes-builder/example-config/**
    
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

##### **6:   Run the 'setup' script to build the builder.conf file** #####

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

##### **7:   Install all the dependencies:** ##### 

*Note: make sure you are in the “qubes-builder” directory to run the following cmds*

*   **$ make install-deps**
<br>
<br>
![arch-template-18](/attachment/wiki/ArchlinuxTemplate/arch-template-18.png)
<br>
<br>
<br>

##### **8:   Get all the require sources for the build: (Note: this may take some time)** #####

*   **$ make get-sources**
<br>
<br>
![arch-template-19](/attachment/wiki/ArchlinuxTemplate/arch-template-19.png)
<br>
<br>
<br>

##### **9:   Make all the require Qubes Components:** #####

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


##### **10:   Make the actual Archlinux template:** #####

*   **$ make template**  
<br>
<br>
![arch-template-21](/attachment/wiki/ArchlinuxTemplate/arch-template-21.png)
<br>
<br>
<br>


##### **11:   Transfer Template into Dom0** #####

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

    *   Swtich to Domo and open a terminal window.

    **Note:** Take care when entering these cmd strings.  They are very long and have a number of characters that are easy to mix '**-**' vs '**.**' '**<u>T</u>emplates** (correct) vs **<u>t</u>emplates** (wrong) or **Template_**'(also wrong)  This script will also take care of transfering the actual template.rpm to Dom0 as well.


        *   **$ cd /**

        *   **$ sudo qvm-run --pass-io development 'cat /home/user/qubes-builder/qubes-src/linux-template-builder/rpm/install-templates.sh' > install-templates.sh**

<br>
<br>
![arch-template-23](/attachment/wiki/ArchlinuxTemplate/arch-template-23.png)
<br>
<br>
![arch-template-24](/attachment/wiki/ArchlinuxTemplate/arch-template-24.png)
<br>
<br>
<br>
<br>

##### **If everything went correct there should be a Archlinux template listed in your Qubes VM Manager** #####

<br>
<br>
<br>
---------------

## **Package Manager Proxy Setup Section** ##


One last thing to setup to have a "PROPERLY" functioning archlinux template.

Archlinux package manager Pacman is  a fine package mangers except that we could not find a way to configure it to use the Qubes Update Proxy Service (QUPS) that would comply with Qubes QUPS usage policy.

*If someone does find a way please post to the Qubes-Users or Devel google groups mailing list.*

Powerpill is a full Pacman wrapper that not only give easy proxy configuration but further offers numerous other advantages.

Please check out:

[Archlinux Powerpill](https://wiki.archlinux.org/index.php/powerpill)

[XYNE's (dev) Powerpill](http://xyne.archlinux.ca/projects/powerpill/)


**Important Note:** Until Powerpill is configured you will have to open network access to the template to get the initial packages etc downloaded.  You can use the "allow full access for" a given time period in the FW settings of the template in the VMM or open up the various services through the same window.  Remember to change it back if you choose the later route.  Actions needing network access will be noted with (needs network access)

<br>
<br>

##### **1:  Editing Pacman's configuration file (pacman.conf)** #####

*   Open archlinux terminal app

*   edit /etc/pacman.conf

*   **$ sudo nano -w /etc/pacman.conf**
        
* Below is the output of a correct pacman.conf file  Make the changes so your file matches this one or rename the original and create a new one and copy and paste this text into it.  Text should be justified left in the file.  The changes from your default are to make gpg sig signing mandatory for packages but not required for DBs for the archlinux repos.  Also to add the repo (at the end) for the Powerpill package.


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

##### **3:  Install Powerpill (Pacman wrapper)** (needs network access) #####

*   **$ sudo pacman -S powerpill**

<br>
<br>

##### **4:  Install Reflector** (needs network access) #####

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

#### **Known Issues:** ####

*   If there is an Arch upgrade of Pulse Audio it will require rebuilding and installing  Qubes component: gui-agent-linux 

*   There May also be a similar issue of dependencies with Xorg.
   
*   Upgrade Relfector functionality to allow its use through the QUPS

*   Pacman functionality changes and allows it to be directly configured to work through QUPS.

<br>

#### **Qubes Mailing List Threads on the Archlinux build process:** ####

*   [Qubes-Devel](https://groups.google.com/forum/#!forum/qubes-devel): [Qubes Builder failed Archlinux repository is missing](https://groups.google.com/forum/#!topic/qubes-devel/tIFkS-rPVx8)

*   [Qubes-Users](https://groups.google.com/forum/#!forum/qubes-users): [Trying to compile archlinux template](https://groups.google.com/forum/#!topic/qubes-users/7wuwr3LgkQQ)    

<br>

#### **Want to contribute?** ####

*   [How can I contribute to the Qubes Project?](/doc/contributing/)

*   [Guidelines for Documentation Contributors](/doc/doc-guidelines/)

<br>
