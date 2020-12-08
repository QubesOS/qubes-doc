---
layout: doc
title: Dark Theme in Dom0 and DomU
redirect_to: https://github.com/Qubes-Community/Contents/blob/master/docs/customization/dark-theme.md
redirect_from:
- /doc/dark-theme/
---

Dark Theme in Dom0
==================

Dark KDE in Dom0
----------------

The following text describes how to change the default light theme to a dark theme. This is just an example, feel free to adjust the appearance to your taste.

The image below shows the default light theme after installation.
![begin light theme](/attachment/wiki/Dark-Theme/kde-fresh-installed-standard.png)

This is the result after applying the steps described here.
![end result dark theme](/attachment/wiki/Dark-Theme/kde-end-result.png)

1. Change `Workspace Appearance`

    1. Open the `Workspace Appearance` window

            Qubes Menu -> System Tools -> System Settings -> Workspace Appearance

        ![Workspace Appearance](/attachment/wiki/Dark-Theme/kde-app-appearance-menu-style.png)

    2. Go to `Desktop Theme`

        ![Desktop Menu](/attachment/wiki/Dark-Theme/kde-appearance-settings-desktop-theme-oxygen.png)

    3. Select `Oxygen` and `Apply` the change

2. (Optional) Remove blue glowing task items

    ![blue glowing task bar items](/attachment/wiki/Dark-Theme/kde-taskbar-blue-glowing-border.png)

    1. Adjust Oxygen `Details`

            Qubes Menu -> System Tools -> System Settings -> Workspace Appearance -> Desktop Theme -> Details (Tab)

    2. Select `Oxygen`

    3. Change `Theme Item -> Task Items` from `Oxygen Task Items` to `Air Task Items`

        ![Change Task items look](/attachment/wiki/Dark-Theme/kde-desktop-theme-details.png)

    4. Apply changes

        ![task bar items blue glowing removed](/attachment/wiki/Dark-Theme/kde-taskbar-blue-glowing-removed.png)

3. Change `Application Appearance`

    1. Open the `Application Appearance` window

            Qubes Menu -> System Tools -> System Settings -> Application Appearance

    2. Go to `Colors`

        ![colors tab](/attachment/wiki/Dark-Theme/kde-app-appearance-menu-colors.png)

    3. Select `Obsidian Coast`

        ![set to Obsidian Coast](/attachment/wiki/Dark-Theme/kde-app-appearance-menu-colors-set.png)

    4. Apply Changes

            Qubes VM Manager should now look like the image below.

        ![result black Qubes Manager](/attachment/wiki/Dark-Theme/kde-black-qubes-manager.png)

**Note:** Changing the `Window Decorations` from `Plastik for Qubes` will remove the border color and the VM name. The problem with `Plastik for Qubes` is that it does not overwrite the background and text color for Minimize, Maximize and Close buttons. The three buttons are therefore hard to read.

Dark XCFE in Dom0
-----------------

The following text describes how to change the default light theme to a dark theme. This is just an example, feel free to adjust the appearance to your taste.

The image below shows the default light theme after installation.
![begin light theme](/attachment/wiki/Dark-Theme/xfce-fresh-installed.png)

This is the result after applying the steps described here.
![end result dark theme](/attachment/wiki/Dark-Theme/xfce-end-result.png)

1. Change Appearance

    1. Open the `Appearance` dialog

            Qubes Menu -> System Tools -> Appearance

        ![appearance dialog](/attachment/wiki/Dark-Theme/xfce-appearance-dialog.png)

    2. Change Style to `Albatross`

    **Note:** The black appearance theme `Xfce-dusk` makes the VM names in the `Qubes OS Manager` unreadable.

2. *(Optional)* Change Window Manager Style

    1. Open the `Window Manager` dialog

            Qubes Menu -> System Tools -> Appearance

        ![window manager dialog](/attachment/wiki/Dark-Theme/xfce-window-manager-theme.png)

    2. Change the Theme in the `Style` Tab (e. g. Defcon-IV). All available themes work.


Dark App VM, Template VM, Standalone VM, HVM (Linux Gnome)
==========================================================

Almost all Qubes VMs use default applications based on the GTK toolkit. Therefore the description below is focused on tools from the Gnome Desktop Environment.

Using "Gnome-Tweak-Tool"
------------------------

The advantage of creating a dark themed Template VM is, that each AppVM which is derived from the Template VM will be dark themed by default.

**Note:** Gnome-Tweak-Tool crashes under Archlinux. A workaround is to assign the AppVM to another TemplateVM (Debian, Fedora) which has Gnome-Tweak-Tool installed. Start the AppVM and configure the settings. Shutdown the machine and switch the TemplateVM back to Archlinux.

1. Start VM

    **Note:** Remember that if you want to make the change persistent, the change needs to be made in the TemplateVM, not the AppVM.

2. Install `Gnome-Tweak-Tool`

    - Fedora

            sudo dnf install gnome-tweak-tool

    - Debian

            sudo apt-get install gnome-tweak-tool

3. *(Only AppVM)* Stop TemplateVM and start AppVM

4. Add `Gnome-Tweak-Tool` to the Application Menu

    1. `Right-click` on VM entry in `Qubes VM Manager` select `Add/remove app shortcuts`

    2. Select `Tweak Tool` and press the `>` button to add it

        ![Application Dialog](/attachment/wiki/Dark-Theme/dialog-add-gnome-tweak-tool.png)

5. Enable `Global Dark Theme`

    1. *Debian only*

            cd ~/.config/
            mkdir gtk-3.0
            cd gtk-3.0/
            touch settings.ini

    2. Start `Tweak Tool` from the VM application menu and set the `Global Dark Theme` switch to `on`

        ![Global Dark Theme enabled](/attachment/wiki/Dark-Theme/gnome-tweak-tool.png)

6. *(Optional)* Modify Firefox

    **Note:** Firefox uses GTK style settings by default. This can create side effects such as unusable forms or search fields. One way to avoid this is to add the following line to `/rw/config/rc.local`:

            sed -i.bak "s/Exec=firefox %u/Exec=bash -c 'GTK_THEME=Adwaita:light firefox %u'/g" /usr/share/applications/firefox.desktop

7. Restart VM or all applications

Manually
--------

Manually works for Debian, Fedora and Archlinux.

1. Start VM

    **Note:** Remember that if you want to make the change persistent, the change needs to be made in the TemplateVM, not the AppVM.

2. Enable `Global Dark Theme`

        cd ~/.config/
        mkdir gtk-3.0
        cd gtk-3.0/
        touch settings.ini

    Add the following lines to `settings.ini`

        [Settings]
        gtk-application-prefer-dark-theme=1

3. Follow steps 6 and 7 in: Using `Gnome-Tweak-Tool`
