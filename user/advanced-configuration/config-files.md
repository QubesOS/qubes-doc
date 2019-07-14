---
layout: doc
title: Config Files
permalink: /doc/config-files/
redirect_from:
- /en/doc/config-files/
- /doc/ConfigFiles/
- "/doc/UserDoc/ConfigFiles/"
- "/wiki/UserDoc/ConfigFiles/"
---

Configuration Files
===================

Qubes-specific VM config files
------------------------------

These files are placed in /rw, which survives a VM restart.
That way, they can be used to customize a single VM instead of all VMs based on the same template. 
The scripts here all run as root.

-   `/rw/config/rc.local` - script runs at VM startup.
    Good place to change some service settings, replace config files with its copy stored in /rw/config, etc.
    Example usage:

    ~~~
    # Store bluetooth keys in /rw to keep them across VM restarts
    rm -rf /var/lib/bluetooth 
    ln -s /rw/config/var-lib-bluetooth /var/lib/bluetooth
    ~~~

    ~~~
    # Add entry to /etc/hosts
    echo '127.0.0.1 example.com >> /etc/hosts
    ~~~

-   `/rw/config/qubes-ip-change-hook` - script runs in NetVM after every external IP change and on "hardware" link status change.

-   In ProxyVMs (or AppVMs with `qubes-firewall` service enabled), scripts placed in the following directories will be executed in the listed order followed by `qubes-firewall-user-script` after each firewall update.
    Good place to write own custom firewall rules.

    ~~~
    /etc/qubes/qubes-firewall.d
    /rw/config/qubes-firewall.d
    /rw/config/qubes-firewall-user-script
    ~~~

-   `/rw/config/suspend-module-blacklist` - list of modules (one per line) to be unloaded before system goes to sleep.
    The file is used only in a VM with PCI devices attached.
    Intended for use with problematic device drivers.

- In NetVMs/ProxyVMs, scripts placed in `/rw/config/network-hooks.d` will be ran when configuring Qubes interfaces. For each script, the `command`, `vif`, `vif_type` and `ip` is passed as arguments (see `/etc/xen/scripts/vif-route-qubes`). For example, consider an PV AppVM `work` with IP `10.137.0.100` and `sys-firewall` as NetVM. Assuming it's Xen domain id is arbitrary `12` then, the following script located at `/rw/config/network-hooks.d/hook-100.sh` in `sys-firewall`:
    ~~~
    #!/bin/bash

    command="$1"
    vif="$2"
    vif_type="$3"
    ip="$4"

    if [ "$ip" == '10.137.0.100' ]; then
        case "$command" in
            online)
                ip route add 192.168.0.100 via 10.137.0.100
                ;;
            offline)
                ip route del 192.168.0.100
                ;;
        esac
    fi
    ~~~

  will be executed with arguments `online vif12.0 vif 10.137.0.100` when starting `work`. Please note that in case of HVM, the script will be called twice - once with vif_type `vif`, then with vif_type `vif_ioemu` (and different interface names). As long as the ioemu interface exists, it should be preferred (up to the hook script). When VM decide to use PV interface (vif_type `vif`), the ioemu one will be unplugged.

Note that scripts need to be executable (chmod +x) to be used.

Also, take a look at [bind-dirs](/doc/bind-dirs) for instructions on how to easily modify arbitrary system files in an AppVM and have those changes persist.


GUI and audio configuration in dom0
-----------------------------------

The GUI configuration file `/etc/qubes/guid.conf` in one of a few not managed by qubes-prefs or the Qubes Manager tool.
Sample config (included in default installation):

~~~
# Sample configuration file for Qubes GUI daemon
#  For syntax go http://www.hyperrealm.com/libconfig/libconfig_manual.html

global: {
  # default values
  #allow_fullscreen = false;
  #allow_utf8_titles = false;
  #secure_copy_sequence = "Ctrl-Shift-c";
  #secure_paste_sequence = "Ctrl-Shift-v";
  #windows_count_limit = 500;
  #audio_low_latency = false;
  #screen
  #root_win
  #root_width
  #root_height
  #context
  #frame_gc
  #tray_gc
  #tint_h
  #inter_appviewer_lock_fd
  #domid
  #target_domid
  #agent_version
  #cmdline_color
  #label_color_rgb
  #cmdline_icon
  #icon_data
  #icon_data_len
  #label_index
  #screen_window
  #clipboard_requested
  #windows_count
  #log_level
  #nofork
  #invisible
  #kill_on_connect
  #allow_utf8_titles
  #allow_fullscreen
  #copy_seq_mask
  #paste_seq_mask
  #qrexec_clipboard
  #use_kdialog
  #audio_low_latency
  #prefix_titles
  #trayicon_mode
  #trayicon_border
  #trayicon_tint_reduce_saturation
  #trayicon_tint_whitehack
};

# most of setting can be set per-VM basis

VM: {
  work: {
    #allow_utf8_titles = true;
  };
  video-vm: {
    #allow_fullscreen = true;
  };
};
~~~

Currently supported settings:

-   `allow_fullscreen` - allow VM to request its windows to go fullscreen (without any colorful frame).

    **Note:** Regardless of this setting, you can always put a window into fullscreen mode in Xfce4 using the trusted window manager by right-clicking on a window's title bar and selecting "Fullscreen".
    This functionality should still be considered safe, since a VM window still can't voluntarily enter fullscreen mode.
    The user must select this option from the trusted window manager in dom0.
    To exit fullscreen mode from here, press `alt` + `space` to bring up the title bar menu again, then select "Leave Fullscreen".

-   `allow_utf8_titles` - allow the use of UTF-8 in window titles; otherwise, non-ASCII characters are replaced by an underscore.

-   `secure_copy_sequence` and `secure_paste_sequence` - key sequences used to trigger secure copy and paste.

-   `windows_count_limit` - limit on concurrent windows.

-   `audio_low_latency` - force low-latency audio mode (about 40ms compared to 200-500ms by default).
    Note that this will cause much higher CPU usage in dom0.

- `screen` - Points on default screen

- `root_win` - Root attributes

- `root_width` - Size of root window

- `context` - context for pixmap operations

- `frame_gc` - graphics context for painting window frame

- `tray_gc` - graphic context for painting tray background, only in
	TRAY_BACKGROUND mode

- `tint_h` - precomputed H and S for tray coloring - only in TRAY_TINT mode

- `inter_appviewer_lock_fd` - FD of lock file used to synchronize shared memory
	access

- `domid` - Xen domain id (GUI)

- `target_domid` - Xen domain id (VM) - can differ from domid when GUI is
	stubdom

- `cmdline_color` - color of frame

- `label_color_rgb` - color of the frame in RGB

- `cmdline_icon` - icon hint for WM

- `icon_data` - loaded icon image, ready for \_NEW\_WM\_ICON property

- `icon_data_len` - size of icon\_data, in sizeof(\*icon\_data) units

- `label_index` - label (frame color) hint for WM

- `screen_window` - window of whole VM screen

- `clipboard_requested` - if clippoard content was requested by dom0

- `clipboard_xevent_time` -  timestamp of keypress which triggered last
	copy/paste

- `windows_count` - created window count

- `nofork` - do not fork into background - used during guid restart 

- `invisible` - do not show any VM window

- `kill_on_connect` - pid to kill when connection to gui agent is established

- `allow_utf8_titles` - allow UTF-8 chars in window title

- `copy_seq_mask` - modifiers mask for secure-copy key sequence

- `paste_seq_mask` - modifiers mask for secure-paste key sequence

- `qrexec_clipboard` - 0: use GUI protocol to fetch/put clipboard, 1: use qrexec

- `use_kdialog` - use kdialog for prompts (default on KDE) or zenity (default on
	non-KDE)

- `trayicon_mode` - trayicon coloring mode

- `trayicon_border` - position of trayicon border - 0 - no border, 1 - at the
	edges, 2 - 1px from the edges

- `trayicon_tint_reduce_saturation` - trayicon\_tint\_reduce\_saturation

- `trayicon_tint_whitehack` - replace white pixels with almost-white 0xfefefe
	(available only for "tint" mode)

