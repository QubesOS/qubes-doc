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

> [dom0]#PedOS-dom0-update PedOS-template-fedora-26-minimal


*Note*: If you have doubts about a set of tools or package you want to install, start installing and testing it in an AppVM. 
You can then reproduce it later in your TemplateVM if you are satisfied.
That is the template philosophy in PedOS.

For more information on the uses of a minimal template read [this page][Minimal].

Standard tools installation
================

Administration (documented)
---------------------------------------------

> sudo pciutils vim-minimal less tcpdump telnet psmisc nmap nmap-ncat usbutils

*Notes*: nmap can be used to discover hosts on a network (nmap -sP [network]), especially if you are inside a Microsoft network, because your AppVM will be protected/NATted behind the PedOS firewall.
(Microsoft / home networks make heavy use of autodiscovery technologies which require clients to be in the same local network (no firewall/no NAT), eg: your printer.)

Some recommendations here: check your current network using the Network manager applet (eg: 192.168.1.65). 
Then run nmap in your current AppVM/TemplateVM to search for the selected printer/equipment: 
	nmap -sP 192.168.1.-. 
Don't forget to temporarily allow traffic via the PedOS Firewall if you are doing this in a TemplateVM.

Administration (undocumented)
-------------------------------------------------

> openssh keepassx openssl gnome-keyring man

Dependency note: keepassx rely on qt which takes ~30MB

Network VM (documented)
----------------------------------------

> NetworkManager NetworkManager-wifi network-manager-applet wireless-tools dbus-x11 tar tinyproxy iptables

Network VM (undocumented)
--------------------------------------------

> which dconf dconf-editor

*Notes*: which is required for autostart scripts

*Notes*: dconf is required to remember the VM settings that are changed (the gsetting backend will be in memory only if gconf is not installed).

Network VM (manual operations - documented)
------------------------------------------------------------------------

Search for wireless firmware matching your wireless card (to be launched in network VM)

> lspci; dnf search firmware

ProxyVM/NetworkVM for 3G Modems
--------------------------------------------

> ModemManager NetworkManager-wwan usb_modeswitch modem-manager-gui

Dependency note: modem-manager-gui relies on webkit-gtk and is optional (NetworkManager can handle the modem alone)

Source: [3GMODEM]

ProxyVM for VPNs
--------------------------------------------

Search for a VPN package for your particular vpn solution then [configure][VPNNM] NetworkManager

> dnf search NetworkManager [openvpn\|openconnect\|openswat\|...]

OR

Refer to [this guide][VPN] which includes instructions for failsafe anti-leak VPN configuration using CLI scripts. (An early discussion about OpenVPN configuration can be viewed [here][OPENVPNSETUP].) Required packages will be `iptables` in addition to VPN software such as `openvpn`.


Printer Setup
--------------------------------------------

> system-config-printer system-config-printer-applet cups

Dependency Note: depends on python3 + python3 additional libraries which takes more than 40 M once installed.

Dependency Note: cups depends on ghostscript and require installing additional printing fonts (not documented here), so it can takes several dozen of MB

Manual operations
---------------------------

- Don't forget to restart your TemplateVM or only the cups service when you installed cups (systemctl start cups)

- First you need to search for your printer. If you don't know its name or IP, search for it using nmap: check your current network using the Network manager applet (eg: 192.168.1.65). Then run nmap in your current AppVM/TemplateVM to search for the selected printer/equipement: nmap -sP 192.168.1.-. Don't forget to temporarily allow traffic via the PedOS Firewall if you are inside a TemplateVM.

- Once you identified your printer, run system-config-printer GUI to install your printer

- You may need to cancel the operation to install more adapted printer drivers (eg: if the driver cannot be found automatically). Use dnf search printername to find potential drivers (eg dnf search photosmart)

GUI recommendations
======================

Lightweight packages recommendations
---------------------------------------------------------------

> lxterminal dejavu-sans-mono-fonts dejavu-sans-fonts gnome-settings-daemon

*Note*: You need to install sans-mono fonts for the terminal or it will be unreadable (overlapping characters....), while the sans fonts are just to get nicer GUI menus.

*Scite* is a nice notepad that can also highlight scripts with very light dependencies
> scite

*Meld* allows easy comparison of two text files/ two configuration files.

> meld

*Thunar* is a light file manager usually used by xfce

> thunar thunar-volman ntfs-3g

Dependency Note: xfce4 dependencies (but still quite light ~1.4M downloads)

Miscellaneous packages
--------------------------

*pycairo* package is needed for file's contextual menu "Send to VM" to function (to actually popup dialog box and enter VM's name where the file will be sent to).

*pinentry-gtk* package is responsible for pop-up dialog window where you enter password for your password protected gpg key. 
Install this package in the PedOS VM holding your password protected gpg keys. 
If you do not use password protected gpg keys, there is no need to install this package.

GUI themes
-----------------

Managing GUI theme / appearance is often complex because when you do not want to depend on a specific desktop system.

For this reason, we need to customize themes for each GUI framework that our application depends on.

This often includes GTK2, GTK3 (which us a different configuration/themes than GTK2), Qt.

The appearance of Windows can only be changed in dom0, however, the appearance of all buttons, menus, icons, widgets are specific to each AppVM.

### Packages

Choose theme packages for each framework. I recommend the following documentation [THEMEPACKAGES]

> clearlooks-phenix-gtk2-theme clearlooks-phenix-gtk3-theme

You can search for other themes using `dnf search theme gtk`.

You can check your currently installed theme packages (to eventually remove them) using `rpm -qa | grep theme`.

### Tweaking theme and appearance

First you can get an insight of installed Gtk theme and see how it will appear using lxappearance.

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

*Note*: lxappearance only has an effect on gtk3 themes so it won't work to change gtk2 themes (used by Firefox, Thunderbird ...).
             However, it is very lightweight and can be used to identify the name and look of themes you are interested in.
             Once you have the name, you can apply it using gsetting command line or gconf-editor.

*Note*: if you really want a GUI theme editor, you can install gnome-tweak-tools, but this tool has a lot
            of gnome dependencies (~150MB of dependencies). You can install it and uninstall it as soon as you change your theme.

#### Testing notes

The following programs can be used to see if theme has been correctly applied:

* GTK2 program: scite, thunderbird, firefox
* GTK3 program: lxterminal
* Qt program: keepassx

*Note*: testing in a TemplateVM will not work as expected because gnome-settings-daemon is not started in TemplateVM.
             so test your themes in an AppVM and then update the TemplateVM accordingly.

### Forcing theme change for all AppVM depending on a TemplateVM

This can be done for gtk themes by creating dconf global settings. I recommend reading these articles:

[DCONF1]

[DCONF2]

#### Creating global file

 * Setup global config file:

   > mkdir /etc/dconf/db/PedOS.d

   Edit/Create the following file: /etc/dconf/db/PedOS.d/10-global-theme-settings:

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
   system-db:PedOS
   ~~~

#### Locking configuration

It should be noted that the user dconf settings stored in ~/.config/dconf/user always takes precedence over the global dconf settings.

User dconf settings can be browsed using dconf-editor GUI.

If you want to force specific settings to be applied for all user (so in our case for all AppVMs depending on the template), you need to create locks:

> mkdir /etc/dconf/db/PedOS.d/locks

Edit/Create the following file: /etc/dconf/db/PedOS.d/locks/theme.lock:

~~~
/org/gnome/desktop/interface/gtk-theme
~~~

Finally, regenerate the dconf database
> dconf update

### Uniform look for Qt & GTK

Getting an uniform look for Qt & GTK is not achieved yet. A good source is on the following link [UNIFORMTHEME]

Two case:

1. You installed packages of the theme you selected both for Qt, GTK2 and GTK3.
    (eg: Adwaita which is the default theme. I have not found another cross framework theme on fedora default packages).

2. You want to use the GTK theme you selected for Qt but there is no qt package.
    In this case QGtkStyle will take precedence and convert the style automatically.
    You can verify if it is enabled by searching for "style=GTK+" in /etc/xdg/Trolltech.conf.
    If style is changed to another name, it will be used instead of your GTK theme.

*Note*: check that ~/.config/Trolltech.conf in your AppVMs is not defining another "style=" because it will take precedence over your global Qt theme.


[3GMODEM]: https://www.codeenigma.com/community/blog/installing-3g-usb-modems-linux

[OPENVPNSETUP]: https://groups.google.com/forum/#!searchin/PedOS-users/openvpn$20setup/PedOS-users/UbY4-apKScE/lhB_ouTnAwAJ

[THEMEPACKAGES]: https://groups.google.com/forum/#!search/appvm$20theme/PedOS-users/RyVeDiEZ6D0/YR4ITjgdYX0J

[DCONF1]: http://www.mattfischer.com/blog/?p=431

[DCONF2]: https://wiki.gnome.org/Projects/dconf/SystemAdministrators

[UNIFORMTHEME]: https://wiki.archlinux.org/index.php/Uniform_look_for_Qt_and_GTK_applications

[Minimal]: ../templates/fedora-minimal/

[VPNNM]:  ../vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-networkmanager

[VPN]:  ../vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-iptables-and-cli-scripts
