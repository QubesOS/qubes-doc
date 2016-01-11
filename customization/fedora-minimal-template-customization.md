---
layout: doc
title: Fedora Minimal Template Customization
permalink: /doc/fedora-minimal-template-customization/
redirect_from: /en/doc/fedora-minimal-template-customization/
---

FEDORA Packages Recommendations
======================

(starting from a minimal template)

Template installation
------------------------------

> [dom0]#qubes-dom0-update qubes-template-fedora-21-minimal

*Note*: the template may not start in Qubes R3 when using kernel 3.19 (unstable). In this case, switch the AppVM or TemplateVM to the kernel 3.18.

*Note*: If you have doubts about a set of tool or package you want to install, start installing and testing it in an AppVM. You can then reproduce it later in your TemplateVM if you are satisfied. That the (QubesOS?) template philosophy.

Standard tools installation
================

Administration (documented)
---------------------------------------------

sudo pciutils vim-minimal less tcpdump telnet psmisc nmap nmap-ncat usbutils

*Notes*: nmap can be used to discover a network (nmap -sP [network]), especially if you are inside a Microsoft network, because your AppVM will be protected/NATted behind Qubes firewall (microsoft / home network are heavily using autodiscovery technologies which require to be in the same local network (no firewall/no NAT), eg: your printer.

Some recommendation here: check your current network using the Network manager applet (eg: 192.168.1.65). Then run nmap in your current AppVM/TemplateVM to search for the selected printer/equipement: nmap -sP 192.168.1.-. Don't forget to allow temporarily the Qubes Firewall if you are inside a TemplateVM.

Administration (undocumented)
-------------------------------------------------

openssh keepassx openssl gnome-keyring man

Dependency note: keepassx rely on qt which takes ~30MB

Network VM (documented)
----------------------------------------

NetworkManager NetworkManager-wifi network-manager-applet wireless-tools dbus-x11 tar tinyproxy

Network VM (undocumented)
--------------------------------------------

which dconf dconf-editor

*Notes*: which is required for autostart scripts

*Notes*: dconf is required to remember the VM settings that are changed (the gsetting backend will be in memory only if gconf is not installed).

Network VM (manual operations - documented)
------------------------------------------------------------------------

Search for a wireless firmware matching your wireless card (to be launched in network VM)

> lspci; yum search firmware

ProxyVM/NetworkVM for 3G Modems
=====================

ModemManager NetworkManager-wwan usb_modeswitch modem-manager-gui

Dependency note: modem-manager-gui rely on webkit-gtk and is optional (NetworkManager can handle the modem alone)

Source: [3GMODEM]

ProxyVM for VPNs
==========

Search for a VPN package for your particular vpn solution

> yum search NetworkManager [openconnect|openswat|...]

OR

For manual handling of VPN (and because NetworkManager is not available in proxyVMs, check the Qubes-users mail threads on google group

(cprise started a good one on openvpn: [OPENVPNSETUP] "[qubes-users] OpenVPN Setup, Revisited Again!")

Printer Setup
========

system-config-printer system-config-printer-applet cups

Dependency Note: depends on python3 + python3 additional libraries which takes more than 40 M once installed.

Dependency Note: cups depends on ghostscript and require installing additional printing fonts (not documented here), so it can takes several dozen of MB

Manual operations
---------------------------

- Don't forget to restart your TemplateVM or only the cups service when you installed cups (systemctl start cups)

- First you need to search for your printer. If you don't know its name or IP, search for it using nmap: check your current network using the Network manager applet (eg: 192.168.1.65). Then run nmap in your current AppVM/TemplateVM to search for the selected printer/equipement: nmap -sP 192.168.1.-. Don't forget to allow temporarily the Qubes Firewall if you are inside a TemplateVM.

- Once you identified your printer, run system-config-printer GUI to install your printer

- You man need to cancel the operation to install more adapted printer drivers (eg: if the driver cannot be found automatically). Use yum search printername to find potential drivers (eg yum search photosmart)

GUI recommendations
=============

Lightweight packages recommendations
---------------------------------------------------------------

lxterminal dejavu-sans-mono-fonts dejavu-sans-fonts gnome-settings-daemon

*Note*: You need to install sans-mono fonts for the terminal or it will be unreadable (overlapping characters....), while the sans fonts are just to get nicer GUI menus.

*Scite* is a nice notepad that can also highlight scripts with very light dependencies

scite

*Meld* allow comparing two text files/ two configuration files easily.

meld

*Thunar* is a light file manager usually used by xfce

thunar thunar-volman ntfs-3g

Dependency Note: xfce4 dependencies (but still quite light ~1.4M downloads)

GUI themes
-----------------

Managing GUI theme / appearance is often complex because when you do not want to depends on a specific desktop system.

For this reason, we need to customize themes for each GUI framework that our application depends on.

This often includes GTK2, GTK3 (which us a different configuration/themes than GTK2), QT.

The apparance of Windows can only be changed in dom0, however, the appearance of all buttons, menus, icons, widgets are specific to each AppVM.

### Packages

Choose theme packages for each framework. I recommend the following documentation [THEMEPACKAGES]

clearlooks-phenix-gtk2-theme clearlooks-phenix-gtk3-theme

You can search for other themes using yum search theme gtk

You can check your currently installed theme packages (to eventually remove them) using rpm -qa | grep theme

### Tweaking theme and appearance

First you can get an insight of installed Gtk theme and see how it will appears using lxappearance.

I recommend not applying settings using lxappearance (do not click on apply) because it will create multiple configuration files.

To remove these files, follow cleanup notes.

#### Cleanup notes

~~~
rm ~/.gtkrc-2.0
rm ~/.icons/default/index.theme
rm ~/.config/gtk-3.0/settings.ini
rm ~/.config/Trolltech.conf
~~~

Cleaning the whole dconf settings is also possible by removing the following file. Please note that it will remove all preferences set for gnome application (not only the themes)

~~~
rm ~/.config/dconf/user
~~~

*Note*: lxappearance only have effect on gtk3 theme so it won't work to change gtk2 themes (used by Firefox, Thunderbird ...).
             However, it is very lightweight and can be used to identify the name and look of themes you are interested in.
             Once you have the name, you can apply it using gsetting command line or gconf-editor.

*Note*: if you really want a GUI theme editor, you can install gnome-tweak-tools, but this tool have a lot
            of gnome dependencies (~150MB of dependencies). Eventually install it and uninstall it as soon as you changed your theme.

#### Testing notes

The following programs can be used to see if theme has been correctly applied:

* GTK2 program: scite, thunderbird, firefox
* GTK3 program: lxterminal
* QT program: keepassx

*Note*: testing in a TemplateVM will not work as expected because gnome-settings-daemon is not started in TemplateVM.
             so test your themes in an AppVM and then update the TemplateVM accordingly.

### Forcing theme change for all AppVM depending on a TemplateVM

This can be done for gtk themes by creating dconf global settings. I recommend reading these articles:

[DCONF1]

[DCONF2]

#### Creating global file

 * Setup global config file:

   > mkdir /etc/dconf/db/qubes.d

   Edit/Create the following file: /etc/dconf/db/qubes.d/10-global-theme-settings:

   ~~~
   [org/gnome/desktop/interface]
   cursor-theme="Adwaita"
   gtk-theme="Clearlooks-Phenix"
   icon-theme="Adwaita"
   font-name="Cantarell 11"
   monospace-font-name="Monospace 11"
   ~~~

 * Generate global config database

   > dconf update

 * Configure default user profile

    Edit/Create the following file: /etc/dconf/profile/user:

   ~~~
   user-db:user
   system-db:qubes
   ~~~

#### Locking configuration

It should be noted that the user dconf settings stored in ~/.config/dconf/user always takes precedence over the global dconf settings.

User dconf settings can be browsed using dconf-editor GUI.

If you want to force specific settings to be applied for all user (so in our case for all AppVMs depending on the template), you need to create locks:

> mkdir /etc/dconf/db/qubes.d/locks

Edit/Create the following file: /etc/dconf/db/qubes.d/locks/theme.lock:

~~~
/org/gnome/desktop/interface/gtk-theme
~~~

Finally, regenerate the dconf database
> dconf update

### Uniform look for QT & GTK

Getting an uniform look for QT & GTK is not achieved yet. A good source is on the following link [UNIFORMTHEME]

Two case:

1. You installed packages of the theme you selected both for Qt, GTK2 and GTK3.
    (eg: Adwaita which is the default theme. I did not found another cross framework theme on fedora default packages).

2. You want to use the GTK theme you selected for Qt but there is no qt package.
    In this case QGtkStyle will take precedence and convert the style automatically.
    You can verify if it is enabled by searching for "style=GTK+" in /etc/xdg/Trolltech.conf.
    If style is changed to another name, it will be used instead of your GTK theme.

*Note*: check that ~/.config/Trolltech.conf in your AppVMs is not defining another "style=" because it will take precedence over your global QT theme.


[3GMODEM]: https://www.codeenigma.com/community/blog/installing-3g-usb-modems-linux

[OPENVPNSETUP]: https://groups.google.com/forum/#!searchin/qubes-users/openvpn$20setup/qubes-users/UbY4-apKScE/lhB_ouTnAwAJ

[THEMEPACKAGES]: https://groups.google.com/forum/#!search/appvm$20theme/qubes-users/RyVeDiEZ6D0/YR4ITjgdYX0J

[DCONF1]: http://www.mattfischer.com/blog/?p=431

[DCONF2]: https://wiki.gnome.org/Projects/dconf/SystemAdministrators

[UNIFORMTHEME]: https://wiki.archlinux.org/index.php/Uniform_look_for_Qt_and_GTK_applications
