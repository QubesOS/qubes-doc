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

For ease of use Qubes aggregates shortcuts to applications that are installed in AppVMs and shows them in one "start menu" in dom0. Clicking on such shortcut runs the assigned application in its AppVM.

![dom0-menu.png"](/attachment/wiki/ManagingAppVmShortcuts/dom0-menu.png)

To make newly installed applications show up in the menu, use the **qvm-sync-appmenus** command (Linux VMs does this automatically):

`qvm-sync-appmenus vmname`

After that, select the *Add more shortcuts* entry in VM's submenu to customize which applications are shown:

![dom0-appmenu-select.png"](/attachment/wiki/ManagingAppVmShortcuts/dom0-appmenu-select.png)

The above image shows that Windows HVMs are also supported (provided that Qubes Tools are installed).

What about applications in DispVMs?
-----------------------------------

[See here](/doc/dispvm-customization/#adding-arbitrary-programs-to-disposable-vm-application-menu).

Behind the scenes
-----------------

`qvm-sync-appmenus` works by invoking *GetAppMenus* [Qubes service](/doc/qrexec/) in the target domain. This service enumerates installed applications and sends formatted info back to the dom0 script (`/usr/libexec/qubes-appmenus/qubes-receive-appmenus`) which creates .desktop files in the AppVM/TemplateVM directory.

For Linux VMs the service script is in `/etc/qubes-rpc/qubes.GetAppMenus`. In Windows it's a PowerShell script located in `c:\Program Files\Invisible Things Lab\Qubes OS Windows Tools\qubes-rpc-services\get-appmenus.ps1` by default.

 * R4.0
 
   The list of installed applications for each AppVM is stored in dom0's `/home/user/.local/share/qubes-appmenus/vmname/apps.templates`. Each menu entry is a file that follows the [.desktop file format](https://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html) with some wildcards (*%VMNAME%*, *%VMDIR%*). Applications selected to appear in the menu are stored in `/var/lib/qubes/appvms/vmname/apps`.
    
   Actual command lines for the menu shortcuts involve `qvm-run` command which starts a process in another domain. Examples: `qvm-run -q -a --service -- %VMNAME% qubes.StartApp+7-Zip-7-Zip_File_Manager` or
   `qvm-run -q -a --service -- %VMNAME% qubes.StartApp+firefox`

   Note that you can create a shortcut that points to a .desktop file in your AppVM with e.g. `qvm-run -q -a --service -- personal qubes.StartApp+firefox`

 * R3.2

   The list of installed applications for each AppVM is stored in dom0's `/var/lib/qubes/vm-templates/templatename/apps.templates` (or in case of StandaloneVM: `/var/lib/qubes/appvms/vmname/apps.templates`). Each menu entry is a file that follows the [.desktop file format](https://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html) with some wildcards (*%VMNAME%*, *%VMDIR%*). Applications selected to appear in the menu are stored in `/var/lib/qubes/appvms/vmname/apps`.
    
   Actual command lines for the menu shortcuts involve `qvm-run` command which starts a process in another domain. Examples: `qvm-run -q --tray -a w7s 'cmd.exe /c "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Calculator.lnk"'` or `qvm-run -q --tray -a untrusted 'firefox %u'`

   Note that you can create a shortcut that points to a .desktop file in your AppVM with e.g. `qvm-run -q --tray -a personal -- 'qubes-desktop-run /home/user/application.desktop'`

What if my application has not been automatically included in the list of available apps?
-----------------------------------------------------------------------------------------

You can manually create new entries in the "available applications" list of shortcuts. See [Signal](/doc/signal/) for a worked example of creating a new menu item for a Chrome .desktop shortcut.
