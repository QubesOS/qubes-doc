---
layout: doc
title: ManagingAppVmShortcuts
permalink: /doc/ManagingAppVmShortcuts/
redirect_from: /wiki/ManagingAppVmShortcuts/
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

Behind the scenes
-----------------

List of installed applications for each AppVM is stored in its template's `/var/lib/qubes/vm-templates/templatename/apps.templates` (or in case of StandaloneVM: `/var/lib/qubes/appvms/vmname/apps.templates`). Each menu entry is a file that follows the [.desktop file format](http://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html) with some wildcards (*%VMNAME%*, *%VMDIR%*). Applications selected to appear in the menu are stored in `/var/lib/qubes/appvms/vmname/apps`.

Actual command lines for the menu shortcuts involve `qvm-run` command which starts a process in another domain. Example: `qvm-run -q --tray -a w7s 'cmd.exe /c "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Calculator.lnk"'` or `qvm-run -q --tray -a untrusted 'firefox %u'`

`qvm-sync-appmenus` works by invoking *GetAppMenus* [Qubes service](/wiki/Qrexec) in the target domain. This service enumerates installed applications and sends formatted info back to the dom0 script (`/usr/libexec/qubes-appmenus/qubes-receive-appmenus`) which creates .desktop files in the AppVM/TemplateVM directory.

For Linux VMs the service script is in `/etc/qubes-rpc/qubes.GetAppMenus`. In Windows it's a PowerShell script located in `c:\Program Files\Invisible Things Lab\Qubes OS Windows Tools\qubes-rpc-services\get-appmenus.ps1` by default.
