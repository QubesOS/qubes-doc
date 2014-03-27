---
layout: wiki
title: ConfigFiles
permalink: /wiki/UserDoc/ConfigFiles/
---

Qubes specific VM config files
==============================

Those files are placed in /rw, which survives VM restart, so can be used to customize single VM (not all VMs based on the same template).

-   `/rw/config/rc.local` - script run at VM startup. Good place to change some service settings, replace config files with its copy stored in /rw/config etc. Example usage:

    ``` {.wiki}
    # Store bluetooth keys in /rw to keep them across VM restarts
    rm -rf /var/lib/bluetooth 
    ln -s /rw/config/var-lib-bluetooth /var/lib/bluetooth
    ```

-   `/rw/config/qubes-ip-change-hook` - script run in NetVM after external IP change (or connection to the network)
-   `/rw/config/qubes-firewall-user-script` - script run in ProxyVM after firewall update. Good place to write own custom firewall rules
-   `/rw/config/suspend-module-blacklist` - list of modules (one per line) to be unloaded before system going to sleep. The file is used only in VM with some PCI devices attached. Supposed to be used for problematic device drivers.

Note that scripts need to be executable (chmod +x) to be used.
