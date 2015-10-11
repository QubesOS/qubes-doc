---
layout: doc
title: ConfigFiles
permalink: /en/doc/config-files/
redirect_from:
- /doc/ConfigFiles/
- "/doc/UserDoc/ConfigFiles/"
- "/wiki/UserDoc/ConfigFiles/"
---

Qubes specific VM config files
==============================

Those files are placed in /rw, which survives VM restart, so can be used to customize single VM (not all VMs based on the same template).

-   `/rw/config/rc.local` - script run at VM startup. Good place to change some service settings, replace config files with its copy stored in /rw/config etc. Example usage:

    ~~~
    # Store bluetooth keys in /rw to keep them across VM restarts
    rm -rf /var/lib/bluetooth 
    ln -s /rw/config/var-lib-bluetooth /var/lib/bluetooth
    ~~~

-   `/rw/config/qubes-ip-change-hook` - script run in NetVM after external IP change (or connection to the network)
-   `/rw/config/qubes-firewall-user-script` - script run in ProxyVM after firewall update. Good place to write own custom firewall rules
-   `/rw/config/suspend-module-blacklist` - list of modules (one per line) to be unloaded before system going to sleep. The file is used only in VM with some PCI devices attached. Supposed to be used for problematic device drivers.

Note that scripts need to be executable (chmod +x) to be used.

GUI and audio configuration in dom0
===================================

GUI configuration file `/etc/qubes/guid.conf` in one of few not managed by qubes-prefs nor Qubes Manager tool. Sample config (included in default installation):

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

-   `allow_fullscreen` - allow VM to request its windows to go fullscreen (without any colorful frame). Regardless of this setting, you can also set window fullscreen using trusted window manager settings (right click on title bar).
-   `allow_utf8_titles` - allow to use UTF-8 in window titles, otherwise non-ASCII characters are replaced by underscore.
-   `secure_copy_sequence` and `secure_paste_sequence` - key sequences used to trigger secure copy and paste
-   `windows_count_limit` - limit on concurrent windows count.
-   `audio_low_latency` - force low-latency audio mode (about 40ms compared to 200-500ms by default). Note that this will cause much higher CPU usage in dom0.

