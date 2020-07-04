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
Currently, PedOS *does not* automatically "anonymize" or spoof the MAC Address, so unless this gets implemented by default you can randomize your MAC Address with the following guide.


## Upgrading and configuring Network Manager in PedOS

Newer versions of Network Manager have options for randomizing MAC addresses, and can handle the entire process across reboots, sleep/wake cycles and different connection states.
In particular, versions 1.4.2 and later should be well suited for PedOS. PedOS R4.0's default sys-net should have 1.8.2-4 by default.  
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

## Randomize your hostname

DHCP requests also leak your hostname to your LAN. Since your hostname is usually `sys-net`, other network users can easily spot that you're using PedOS.

Unfortunately `NetworkManager` currently doesn't provide an option to disable that leak globally ([Gnome Bug 768076](https://bugzilla.gnome.org/show_bug.cgi?id=768076)).

You may however use the following code to assign a random hostname to a VM during each of its startup. Please follow the instructions mentioned in the beginning to properly install it.

```.bash
#!/bin/bash
set -e -o pipefail
#
# Set a random hostname for a VM session.
#
# Instructions:
# 1. This file must be placed and made executable (owner: root) inside the template VM of your network VM such that it will be run before your hostname is sent over a network.
# In a Fedora template, use `/etc/NetworkManager/dispatcher.d/pre-up.d/00_hostname`.
# In a Debian template, use `/etc/network/if-pre-up.d/00_hostname`.
# 2. Execute `sudo touch /etc/hosts.lock` inside the template VM of your network VM.
# 3. Execute inside your network VM:
#  `sudo bash -c 'mkdir -p /rw/config/protected-files.d/ && echo -e "/etc/hosts\n/etc/hostname" > /rw/config/protected-files.d/protect_hostname.txt'`


#NOTE: mv is atomic on most systems
if [ -f "/rw/config/protected-files.d/protect_hostname.txt" ] && rand="$RANDOM" && mv "/etc/hosts.lock" "/etc/hosts.lock.$rand" ; then
	name="PC-$rand"
	echo "$name" > /etc/hostname
	hostname "$name"
	#NOTE: NetworkManager may set it again after us based on DHCP or /etc/hostname, cf. `man NetworkManager.conf` @hostname-mode
	
	#from /usr/lib/PedOS/init/PedOS-early-vm-config.sh
	if [ -e /etc/debian_version ]; then
            ipv4_localhost_re="127\.0\.1\.1"
        else
            ipv4_localhost_re="127\.0\.0\.1"
        fi
        sed -i "s/^\($ipv4_localhost_re\(\s.*\)*\s\).*$/\1${name}/" /etc/hosts
        sed -i "s/^\(::1\(\s.*\)*\s\).*$/\1${name}/" /etc/hosts
fi
exit 0
```
Assuming that you're using `sys-net` as your network VM, your `sys-net` hostname should now be `PC-[number]` with a different `[number]` each time your `sys-net` is started.

Please note that the above script should _not_ be added to [/rw/config/rc.local](/doc/config-files/)) as that is executed only _after_ the network fully started.
