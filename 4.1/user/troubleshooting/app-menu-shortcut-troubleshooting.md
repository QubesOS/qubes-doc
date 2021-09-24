---
lang: en
layout: doc
permalink: /doc/4.1/app-menu-shortcut-troubleshooting/
redirect_from:
- /doc/managing-appvm-shortcuts/
- /en/doc/managing-appvm-shortcuts/
- /doc/ManagingAppVmShortcuts/
- /wiki/ManagingAppVmShortcuts/
ref: 202
title: App menu shortcut troubleshooting
---

For ease of use Qubes aggregates shortcuts to applications that are installed in app qubes and shows them in one application menu (aka "app menu" or "start menu") in dom0.
Clicking on such shortcut runs the assigned application in its app qube.

![dom0-menu.png"](/attachment/doc/r4.0-dom0-menu.png)

To make applications newly installed via the OS's package manager show up in the menu, use the `qvm-sync-appmenus` command (Linux VMs do this automatically):

`qvm-sync-appmenus vmname`

After that, select the *Add more shortcuts* entry in the VM's submenu to customize which applications are shown:

![dom0-appmenu-select.png"](/attachment/doc/r4.0-dom0-appmenu-select.png)

The above image shows that Windows HVMs are also supported (provided that Qubes Tools are installed).

What if my application has not been automatically included in the list of available apps?
-----------------------------------------------------------------------------------------

Some times applications may not have included a `.desktop` file and may not be detected by `qvm-sync-appmenus`.
Other times, you may want to make a web shortcut available from the Qubes start menu.

You can manually create new entries in the "available applications" list of shortcuts for all app qubes based on a template.
To do this:

1. Open a terminal window to the template.
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

3. In dom0, run `qvm-sync-appmenus <templateName>`.
4. Go to VM Settings of the app qube(s) to which you want to add the new shortcut, then the Applications tab.
   Move the newly created shortcut to the right under selected.

If you only want to create a shortcut for a single app qube, you can create a custom menu entry instead:

1. Open a terminal window to Dom0.
2. Create a custom `.desktop` file in `~/.local/share/applications`.
   Look in the same directory for existing examples, or see the full [file specification](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html).
   You may use `qvm-run` inside the `.desktop` file; see [Behind the scenes](/doc/app-menu-shortcut-troubleshooting/#behind-the-scenes) for more details.
3. Edit the `~/.config/menus/applications-merged/<vmname>-vm.menu` file for the app qube.
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

[See here](/doc/disposable-customization/).

Fixing shortcuts
----------------

First, try this in dom0:

```
$ qvm-appmenus --update --force <vm_name>
```

If that doesn't work, you can manually modify the files in `~/.local/share/applications/` or `/usr/local/share/applications/`.

For example, suppose you've deleted `my-old-vm`, but there is a leftover Application Menu shortcut, and you find a related file in `~/.local/share/applications/`.
In dom0:

```
$ rm -i ~/.local/share/applications/my-old-vm-*
```

Behind the scenes
-----------------

`qvm-sync-appmenus` works by invoking *GetAppMenus* [Qubes service](/doc/qrexec/) in the target domain.
This service enumerates installed applications and sends formatted info back to the dom0 script (`/usr/libexec/qubes-appmenus/qubes-receive-appmenus`) which creates .desktop files in the app qube/template directory.

For Linux VMs the service script is in `/etc/qubes-rpc/qubes.GetAppMenus`.
In Windows it's a PowerShell script located in `c:\Program Files\Invisible Things Lab\Qubes OS Windows Tools\qubes-rpc-services\get-appmenus.ps1` by default.

The list of installed applications for each app qube is stored in dom0's `~/.local/share/qubes-appmenus/<vmname>/apps.templates`.
Each menu entry is a file that follows the [.desktop file format](https://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html) with some wildcards (*%VMNAME%*, *%VMDIR%*).
Applications selected to appear in the menu are stored in `~/.local/share/qubes-appmenus/<vmname>/apps`.

Actual command lines for the menu shortcuts involve `qvm-run` command which starts a process in another domain.
Examples: `qvm-run -q -a --service -- %VMNAME% qubes.StartApp+7-Zip-7-Zip_File_Manager` or `qvm-run -q -a --service -- %VMNAME% qubes.StartApp+firefox`

Note that you can create a shortcut that points to a .desktop file in your app qube with e.g. `qvm-run -q -a --service -- personal qubes.StartApp+firefox`.
