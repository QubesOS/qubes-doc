---
layout: doc
title: XFCE
permalink: /doc/xfce/
redirect_from:
- /en/doc/xfce/
- /doc/XFCE/
- "/doc/UserDoc/XFCE/"
- "/wiki/UserDoc/XFCE/"
---

XFCE installtion in dom0
========================

**Disclaimer: XFCE isn't fully integrated with Qubes environment, it still require notable amount of manual configuration after install**

Requirements (as of 10/24/2012):

-   qubes-core-dom0-2.0.37 (not released yet, possible to build from "master" branch of marmarek's repo)

Installation:

    qubes-dom0-update --enablerepo=qubes-dom0-unstable @XFCE

Then you need to create /etc/sysconfig/desktop to stay with KDM, as GDM still starts invalid Xorg startup script:

    DISPLAYMANAGER=KDE

Reboot the system. At system startup, select "Xfce session" in login screen (menu on the right bottom corner of the screen).

Configuration
-------------

Things needs/recommended to be done:

-   remove some useless entries from menu and panel, especially file manager, web browser
-   create own favorites menu (currently standard XFCE menu isn't modified to use per-VM subsections, which makes it very inconvenient):
    1.  create `~/.config/menus/favorites.menu`, example content:

        ~~~
        <!DOCTYPE Menu PUBLIC "-//freedesktop//DTD Menu 1.0//EN"
                  "http://www.freedesktop.org/standards/menu-spec/1.0/menu.dtd">

        <Menu>
          <Name>Favorites</Name>
          <DefaultAppDirs/>
          <DefaultDirectoryDirs/>

          <Directory>favorites.directory</Directory>
          <Include>
            <Filename>personal-gnome-terminal.desktop</Filename>
            <Filename>personal-firefox.desktop</Filename>
            <Filename>work-gnome-terminal.desktop</Filename>
            <Filename>work-firefox.desktop</Filename>
            <Filename>mail-mozilla-thunderbird.desktop</Filename>
            <Filename>mail-gnome-terminal.desktop</Filename>
            <Filename>banking-mozilla-firefox.desktop</Filename>
            <Filename>untrusted-firefox.desktop</Filename>
          </Include>
        </Menu>
        ~~~

    2.  add it to the panel: right click on panel, "add new items", select "XFCE menu", choose custom menu file - just created one
