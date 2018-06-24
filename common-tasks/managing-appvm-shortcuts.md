---
layout: doc
title: Managing AppVm Shortcuts
permalink: /doc/managing-appvm-shortcuts/
redirect_from:
- /en/doc/managing-appvm-shortcuts/
- /doc/ManagingAppVmShortcuts/
- /wiki/ManagingAppVmShortcuts/
---

Managing shortcuts to applications in AppVMs
============================================

For ease of use Qubes aggregates shortcuts to applications that are installed in AppVMs and shows them in one "start menu" in dom0.
Clicking on such shortcut runs the assigned application in its AppVM.

![dom0-menu.png"](/attachment/wiki/ManagingAppVmShortcuts/dom0-menu.png)

To make applications newly installed via the OS's package manager show up in the menu, use the `qvm-sync-appmenus` command (Linux VMs do this automatically):

`qvm-sync-appmenus vmname`

After that, select the *Add more shortcuts* entry in the VM's submenu to customize which applications are shown:

![dom0-appmenu-select.png"](/attachment/wiki/ManagingAppVmShortcuts/dom0-appmenu-select.png)

The above image shows that Windows HVMs are also supported (provided that Qubes Tools are installed).

What if my application has not been automatically included in the list of available apps?
-----------------------------------------------------------------------------------------

Some times applications may not have included a `.desktop` file and may not be detected by `qvm-sync-appmenus`.
Other times, you may want to make a web shortcut available from the Qubes start menu.

You can manually create new entries in the "available applications" list of shortcuts for all AppVMs based on a TemplateVM.
To do this:

1. Open a terminal window to the TemplateVM.
2. Create a custom `.desktop` file in `/usr/share/applications` (you may need to first create the subdirectory).
   Look in `/usr/share/applications` for existing examples, or see the full [file specification](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html).
   It will be something like:
   ```
   [Desktop Entry]
   Version=1.0
   Type=Application
   Terminal=false
   Icon=/usr/share/icons/Adwaita/256x256/devices/scanner.png
   Name=VueScan
   GenericName=Scanner
   Comment=Scan Documents
   Categories=Office;Scanning;
   Exec=vuescan
   ```
3. In dom0, run `qvm-sync-appmenus <TemplateVMName>`.
4. Go to VM Settings of the AppVM(s) to which you want to add the new shortcut, then the Applications tab.
   Move the newly created shortcut to the right under selected.

If you only want to create a shortcut for a single AppVM, you can create a custom menu entry instead:

1. Open a terminal window to Dom0.
2. Create a custom `.desktop` file in `~/.local/share/applications`.
   Look in the same directory for existing examples, or see the full [file specification](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html).
   You may use `qvm-run` inside the `.desktop` file; see [Behind the scenes](/doc/managing-appvm-shortcuts/#behind-the-scenes) for more details.
3. Edit the `~/.config/menus/applications-merged/<vmname>-vm.menu` file for the AppVM.
4. Add a custom menu entry referring to your newly created `.desktop` file.

   ~~~
   <Menu>
        <Name>Webmail</Name>
        <Include>
                <Filename>custom.desktop</Filename>
        </Include>
   </Menu>
   ~~~

What about applications in DispVMs?
-----------------------------------

[See here](/doc/dispvm-customization/#adding-arbitrary-programs-to-disposable-vm-application-menu).

Behind the scenes
-----------------

`qvm-sync-appmenus` works by invoking *GetAppMenus* [Qubes service](/doc/qrexec/) in the target domain.
This service enumerates installed applications and sends formatted info back to the dom0 script (`/usr/libexec/qubes-appmenus/qubes-receive-appmenus`) which creates .desktop files in the AppVM/TemplateVM directory.

For Linux VMs the service script is in `/etc/qubes-rpc/qubes.GetAppMenus`. 
In Windows it's a PowerShell script located in `c:\Program Files\Invisible Things Lab\Qubes OS Windows Tools\qubes-rpc-services\get-appmenus.ps1` by default.

 * R4.0
 
   The list of installed applications for each AppVM is stored in dom0's `~/.local/share/qubes-appmenus/<vmname>/apps.templates`.
   Each menu entry is a file that follows the [.desktop file format](https://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html) with some wildcards (*%VMNAME%*, *%VMDIR%*).
   Applications selected to appear in the menu are stored in `~/.local/share/qubes-appmenus/<vmname>/apps`.
    
   Actual command lines for the menu shortcuts involve `qvm-run` command which starts a process in another domain. 
   Examples: `qvm-run -q -a --service -- %VMNAME% qubes.StartApp+7-Zip-7-Zip_File_Manager` or `qvm-run -q -a --service -- %VMNAME% qubes.StartApp+firefox`

   Note that you can create a shortcut that points to a .desktop file in your AppVM with e.g. `qvm-run -q -a --service -- personal qubes.StartApp+firefox`.

 * R3.2

   The list of installed applications for each AppVM is stored in dom0's `/var/lib/qubes/vm-templates/<templatename>/apps.templates` (or in case of StandaloneVM: `/var/lib/qubes/appvms/<vmname>/apps.templates`). 
   Each menu entry is a file that follows the [.desktop file format](https://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html) with some wildcards (*%VMNAME%*, *%VMDIR%*). 
   Applications selected to appear in the menu are stored in `/var/lib/qubes/appvms/<vmname>/apps`.
    
   Actual command lines for the menu shortcuts involve `qvm-run` command which starts a process in another domain. 
   Examples: `qvm-run -q --tray -a w7s 'cmd.exe /c "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Calculator.lnk"'` or `qvm-run -q --tray -a untrusted 'firefox %u'`

   Note that you can create a shortcut that points to a .desktop file in your AppVM with e.g. `qvm-run -q --tray -a personal -- 'qubes-desktop-run /home/user/application.desktop'`.

