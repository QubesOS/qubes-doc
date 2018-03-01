---
layout: doc
title: Anonymizing your MAC Address
permalink: /doc/anonymizing-your-mac-address/
redirect_from:
- /doc/randomizing-your-mac-address/
---

Anonymizing your MAC Address
============================

Although it is not the only metadata broadcast by network hardware, changing the default [MAC Address](https://en.wikipedia.org/wiki/MAC_address) of your hardware could be [an important step in protecting privacy](https://tails.boum.org/contribute/design/MAC_address/#index1h1).
Currently, Qubes OS *does not* automatically "anonymize" or spoof the MAC Address, so unless this is implemented by default you can randomize your MAC Address with the following.
The procedure should work under Qubes R3.2 and R4.0.

## Upgrading and configuring Network Manager in Qubes

Newer versions of Network Manager have a robust set of options for randomizing MAC addresses, and can handle the entire process across reboots, sleep/wake cycles and different connection states.
In particular, versions 1.4.2 and later should be well suited for Qubes.

Network Manager 1.4.2 or later is available from the Fedora 25 repository as well as the Debian 9 repository, which you can install by [upgrading a Debian 8 template to version 9.](/doc/debian-template-upgrade-8/) 

In the Debian 9 or Fedora 25 template you intend to use as a NetVM, check that Network Manager version is now at least 1.4.2:

~~~
$ sudo NetworkManager -V
1.4.2
~~~

Write the settings to a new file in the `/etc/NetworkManager/conf.d/` directory, such as `mac.conf`.
The following example enables Wifi and Ethernet MAC address randomization while scanning (not connected), and uses a randomly generated but persistent MAC address for each individual Wifi and Ethernet connection profile.

~~~
[device]
wifi.scan-rand-mac-address=yes

[connection]
wifi.cloned-mac-address=stable
ethernet.cloned-mac-address=stable
connection.stable-id=${CONNECTION}/${BOOT}
~~~

* `stable` in combination with `${CONNECTION}/${BOOT}` generates a random address that persists until reboot.
* `random` generates a random address each time a link goes up.

To see all the available configuration options, refer to the man page: `man nm-settings`

Next, create a new NetVM using the new template and assign network devices to it.

Finally, shutdown all VMs and change the settings of sys-firewall, etc. to use the new NetVM.

You can check the MAC address currently in use by looking at the status pages of your router device(s), or in the NetVM with the command `sudo ip link show`.

