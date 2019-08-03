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
Currently, Qubes OS *does not* automatically "anonymize" or spoof the MAC Address, so unless this gets implemented by default you can randomize your MAC Address with the following guide.


## Upgrading and configuring Network Manager in Qubes

Newer versions of Network Manager have options for randomizing MAC addresses, and can handle the entire process across reboots, sleep/wake cycles and different connection states.
In particular, versions 1.4.2 and later should be well suited for Qubes. Qubes R4.0's default sys-net should have 1.8.2-4 by default.  
However, use of the NetworkManager GUI to set these options is **unreliable** - there are numerous reports of changes not being saved for particular cards or interfaces.
You should check carefully that any settings you make in the GUI are saved, before relying on this method.
If the settings are not saved, you can use the method described below using a config file.


Network Manager 1.4.2 or later is available from the Fedora 25 repository as well as the Debian 10 repository.

Check that Network Manager version is now at least 1.4.2:

~~~
$ sudo NetworkManager -V
1.4.2
~~~

## Randomize a single connection

Right click on the Network Manager icon of your NetVM in the tray and click 'Edit Connections..'.

Select the connection to randomize and click Edit.

Select the Cloned MAC Address drop down and set to Random or Stable.
Stable will generate a random address that persists until reboot, while Random will generate an address each time a link goes up.
![Edit Connection](/attachment/wiki/RandomizeMAC/networkmanager-mac-random.png)

Save the change and reconnect the connection (click on Network Manager tray icon and click disconnect under the connection, it should automatically reconnect).

## Randomize all Ethernet and Wifi connections

These steps should be done inside a template to be used to create a NetVM as it relies on creating a config file that would otherwise be deleted after a reboot due to the nature of AppVMs.

Write the settings to a new file in the `/etc/NetworkManager/conf.d/` directory, such as `00-macrandomize.conf`.
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

Next, create a new NetVM using the edited template and assign network devices to it.

Finally, shutdown all VMs and change the settings of sys-firewall, etc. to use the new NetVM.

You can check the MAC address currently in use by looking at the status pages of your router device(s), or inside the NetVM with the command `sudo ip link show`.

