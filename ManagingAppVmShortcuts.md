---
layout: wiki
title: ManagingAppVmShortcuts
permalink: /wiki/ManagingAppVmShortcuts/
---

Managing shortcuts to applications in AppVms
============================================

For ease of use Qubes aggregates shortcuts to applications that are installed in AppVms and shows them in one "start menu" in dom0. Clicking on such shortcut runs the assigned application in its AppVm.

To make newly installed applications show up in the menu, use the **qvm-sync-appmenus** command:

`qvm-sync-appmenus vmname`

After that, select the *Add more shortcuts* entry in VM's submenu to customize which applications are shown:

The above image shows that Windows HVMs are also supported (provided that Qubes Tools are installed).

Behind the scenes
-----------------

List of installed applications for each AppVm is stored in `/var/lib/qubes/appvms/vmname/apps.templates`. Each menu entry is a file that follows the [​.desktop file format](http://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html) with some wildcards (*%VMNAME%*, *%VMDIR%*). Applications selected to appear in the menu are stored in `/var/lib/qubes/appvms/vmname/apps`.

Actual command lines for the menu shortcuts involve `qvm-run` command which starts a process in another domain. Example: `qvm-run -q --tray -a w7s 'cmd.exe /c "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Calculator.lnk"'`

`qvm-sync-appmenus` works by invoking *GetAppMenus* [Qubes service](/wiki/Qrexec) in the target domain. This service enumerates installed applications and sends formatted info back to the dom0 script which creates .desktop files in the AppVm directory.

For Linux VMs the service script is in `/etc/qubes-rpc/qubes.GetAppMenus`. In Windows it's a PowerShell script located in `c:\Program Files\Invisible Things Lab\Qubes OS Windows Tools\qubes-rpc-services\get-appmenus.ps1` by default.
