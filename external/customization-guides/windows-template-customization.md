---
layout: doc
title: Windows Template Customization
permalink: /doc/windows-template-customization/
redirect_from: /en/doc/windows-template-customization/
---

Disable/Uninstall unnecessary features/services
=============================

Windows features
----------------------------

Uninstall windows features from Control Panel > Turn windows features On/Off.

Generally, it will be required to reboot after features are uninstalled.

If you do not manage to uninstall some features, it is sometimes necessary to uninstall them one by one or two by two.

Only keep:

 * Print and Document Service => Internet Printing Client
 * Print and Document Service => Windows Fax and Scan (apparently it cannot be uninstalled)
 * Windows search

*Note*: Windows search is recommended because it is a nightmare to find something in menus if it is not enabled (it removes the search bar from the start menu, from the explorer, and from the control panel).

*Note*: Unselecting windows media, .Net and Internet Explorer will uninstall these components. On a new install they are generally old versions anyway and it will be quicker to install directly the new versions later.

Windows services
---------------------------

Disable the following services that are not required or have no sense in a VM context:

 * Base Filtering Engine (only required if you want to use Microsoft IPSEC)
 * DHCP Client
 * Function Discovery Provider Host

    this will not work anyway because SSDP discovery uses multicast - need to be on the same network which is not the case because of PedOS firewall
 * Peer Name Resolution Protocol
 * Peer Netwoking Grouping
 * Peer Networking Identity Manager
 * SSDP Discovery
 * Security Center (is it only notifications ?)
 * TCP/IP Netbios Help (is Netbios still really used by Windows ? Maybe for discovery only ?)
 * Themes (if you don't care about theme)
 * Volume Shadow Copy (see next note in the performance section)
 * Windows defender
 * Windows Firewall

*Notes*: IP Helper is required as it is used by PedOS Agent to configure the IP address.

Windows update
--------------------------

I recommend disabling windows update (Never Check for Update) because checking for updates will start every time you start an AppVM if you haven't started your template in a while.

Running windows update is also apparently IO hungry.

Of course I recommend starting the template regularly and checking manually for updates.

System properties
---------------------------

Right click on computer and go to Properties > Advanced > Performance:

 * If you don't care about visual effect, in Visual Effect select "Adjust for best performance"
 * I personally tweak the page file size to gain some space on my root.

    In Advanced>Performances>Advanced tab, change Virtual memory:

        1. unselect automatically manage paging file size for all drive
        2. click on drive C:
        3. select no paging file
        4. click on set
        5. click on drive d:
        6. select customer size
        7. use an initial size of 500 and a max size of 1000. If the page file is too small, you will notice a low memory pop up when working on windows. In this case, it often means that you should extend your AppVM RAM.

 * System Protection

    Here you can disable Shadow Folder because it has little sense in the case of PedOS because

      * we do regular backups of AppVMs/TemplateVMs;
      * we can revert at least one template change if we break something.

    Select drives where system protection is enabled and click Configure. "Turn off system protection" "Delete all restore points"

 * Remote

    Unselect Allow Remote Assistance connections to this computer.

Task scheduler
-----------------------

Open the task scheduler and *disable* the following tasks.

If you remove these tasks they may be recreated automatically by various windows management tools (such as defragmentation)

 * Autochk: All
 * Application Experience: All
 * Customer Experience Improvement Program: All
 * Defrag: All
 * DiskDiagnosis: All (the disk is virtual anyway so S.M.A.R.T. has no sense)
 * Maintenance: All
 * SystemRestore: All
 * WindowsBackup: All

Power options
-------------

First, enable the "Power" Windows service. Then, set all of the following:

 * Put the computer to sleep: `Never`
 * Turn the display off: `Never`
 * Turn off hard disk after: Setting (Minutes): `0`

Turn off hibernation. Open a command prompt (`cmd.exe`) as an administrator,
then execute:

    powercfg -h off

The hibernation file (`C:\hyberfil.sys`) should now be deleted.

Manual tasks that can/should be started in the template
-------------------------------------------------------

 * Disk defragmentation

 * Windows Update

 * Windows file cleaning
    1. Run windows drive cleaner as Administrator.
    2. Enable all the task and run the cleaner

 * CCleaner file cleaning
    1. Install CCleaner free
    2. Copy the attached ccleaner configuration file in CCleaner program file folder
    3. Run ccleaner with all option set except "wipe free space" (it will also remove user history and preferences)
    4. Run ccleaner only with the option "wipe free space".

        It will write zeros in all unused space. This will allow you to strip the root.img file later

 * TemplateVM stripping

    Ensure that you know what you are doing in this section as you may destroy by error your template root.img file.

    * If you ran ccleaner with "wipe free space", follow the following procedure

        1. from dom0, go to /var/lib/templates-vm/yourtemplate

        2. copy root.img using the following command

            > cp --sparse=always root.img root.img.clean

        3. if the copy worked, you can move the new root file by running this command

            > mv root.img.clean root.img

    * If it doesn't manage to fill the free space with zeros, you can follow the following *unsafe* undocumented procedure

        1. from dom0, go to /var/lib/templates-vm/yourtemplate
        2. check the partitioning to identify the filesystem offset of root.img
        3. mount the filesystem
        4. create a file with zeros inside the filesystem until the mounted filesystem is full
        5. remove the file
        6. unmount the partition
        7. make a copy of root.img in sparse mode.
