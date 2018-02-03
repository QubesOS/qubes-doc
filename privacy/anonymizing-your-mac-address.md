---
layout: doc
title: Anonymizing your MAC Address
permalink: /doc/anonymizing-your-mac-address/
redirect_from:
- /doc/randomizing-your-mac-address/
---

Anonymizing your MAC Address
============================

Although it is not the only metadata broadcast by network hardware, changing the default [MAC Address](https://en.wikipedia.org/wiki/MAC_address) of your hardware could be [an important step in protecting 
privacy](https://tails.boum.org/contribute/design/MAC_address/#index1h1). Currently, Qubes OS *does not* automatically "anonymize" or spoof the MAC Address, so until this is implemented by default you can randomize your MAC Address with one of the following guides using either Network Manager or macchanger...

## Upgrading and configuring Network Manager in Qubes

Newer versions of Network Manager have a robust set of options for randomizing MAC addresses, and can handle the entire process across reboots, sleep/wake cycles and different connection states. In particular, versions 1.4.2 and later should be well suited for Qubes.

Network Manager 1.4.2 or later is available from the Fedora 25 repository as well as the Debian 9 repository, which you can install by [upgrading a Debian 8 template to version 9.](/doc/debian-template-upgrade-8/) 

In the Debian 9 or Fedora 25 template you intend to use as a NetVM, check that Network Manager version is now at least 1.4.2:

~~~
$ sudo NetworkManager -V
1.4.2
~~~

Write the settings to a new file in the `/etc/NetworkManager/conf.d/` directory, such as `mac.conf`. The following example enables Wifi and Ethernet MAC address randomization while scanning (not connected), and uses a randomly generated but persistent MAC address for each individual Wifi and Ethernet connection profile.

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


## Configuring Qubes with macchanger and scripts

First thing you need to do is install **macchanger** package by opening your `fedora-23` TemplateVM and typing

~~~
sudo dnf install macchanger
~~~

Then create the file `macspoof@.service` in `fedora-23` located at `/etc/systemd/system/` directory using a text editor such as `vim`, `emacs`, or `gedit`

~~~
sudo gedit /etc/systemd/system/macspoof@.service
~~~

Paste the following inside of that newly created file

~~~
[Unit]
Description=macchanger on %I
# Hack since macspoof@%i contains @ which is not allowed yet
ConditionPathExists=/var/run/qubes-service/macspoof-%i
Wants=network-pre.target
Before=network-pre.target
BindsTo=sys-subsystem-net-devices-%i.device
After=sys-subsystem-net-devices-%i.device

[Service]
ExecStart=/usr/bin/macchanger -e %I
Type=oneshot

[Install]
WantedBy=multi-user.target
~~~

**How random do you want your MAC address?**

Note in the above line `ExecStart=/usr/bin/macchanger -e %I` we recommend the use of `macchanger` with the `-e` flag which randomizes the MAC address to an address by the same device vendor/manufacturer. There a [number of other flags](http://manpages.ubuntu.com/manpages/xenial/en/man1/macchanger.1.html) you could use instead, such as `-r` which makes a totally random MAC address, which may map to a non-existent device vendor/manufacturer and make it obvious you are spoofing your MAC address. Some reasons why we have recommended `-e` rather than `-r` are in these resources:

* <https://tails.boum.org/contribute/design/MAC_address/#index5h2>
* <https://tails.boum.org/contribute/design/MAC_address/#limitation-only-spoof-nic-part>
* <https://help.ubuntu.com/community/AnonymizingNetworkMACAddresses#Fully_Random>

**Get the right iface names**

It's crucial to get the correct **iface name** for the devices (ethernet and wifi) you want to randomize. To get this,
open your `sys-net` (or wherever your device drivers are) and type in `terminal` the command `ifconfig` the printout 
will look like:

~~~
enp0s0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
	ether 9e:d6:53:02:4b:b6  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 52  memory 0xe1200000-e1220000  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 0  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlp0s1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.2.121  netmask 255.255.255.0  broadcast 192.168.2.255
        inet6 fe80::3602:86ff:fe1f:a7cf  prefixlen 64  scopeid 0x20<link>
	ether 06:6d:70:a8:7b:35  txqueuelen 1000  (Ethernet)
        RX packets 41  bytes 5138 (5.0 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 32  bytes 3712 (3.6 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
~~~

The **iface name** values you're interested in are `enp0s0` and `wlp0s1` as those represent your ethernet and wifi 
devices, respectively.

Also, in this printout is your **actual MAC addresses** which are needed to verify the randomizing is working correctly.  
In this example, the ethernet and wifi addresses are `ether 9e:d6:53:02:4b:b6` and `ether 06:6d:70:a8:7b:35` 
respectively.  *Copy these MAC addresses down somewhere for later.*

Now, go back to your `fedora-23` TemplateVM and use the `touch` command to create service files in the appropriate 
place, note that the `iface name` values at the end:

~~~
cd /var/run/qubes-service/
sudo touch macspoof-enp0s0
sudo touch macspoof-wlp0s1
~~~

Verify the correct files exist in the directory

~~~
[user@fedora-23 qubes-service]$ ls
cups             macspoof-wlp0s1  qubes-update-check
macspoof-enp0s0  meminfo-writer   updates-proxy-setup
~~~

Now, also within the TemplateVM, type the following commands for each hardware device that you want to randomize a MAC 
addresses for

~~~
sudo systemctl enable macspoof@wlp0s1
Created symlink from /etc/systemd/system/multi-user.target.wants/macspoof@wlp0s1.service to /etc/systemd/system/macspoof@.service.
sudo systemctl enable macspoof@enp0s0
Created symlink from /etc/systemd/system/multi-user.target.wants/macspoof@enp0s0.service to /etc/systemd/system/macspoof@.service.
~~~

Now you can do the following:
- Stop your `fedora-23` VM
- Stop your `sys-net` VM

Open your VM settings for `sys-net`, navigate to Services, and add the new services:
- macspoof-wlp0s1
- macspoof-enp0s0

Alternatively, you can enable these services for `sys-net` from the command line by opening up Terminal in `dom0` and running the following:

~~~
qvm-service -e sys-net macspoof-wlp0s1
qvm-service -e sys-net macspoof-enp0s0
~~~

Now restart `sys-net`.

**Verify it works**

Go back to your `sys-net` VM terminal, type `ifconfig` and as before look at the values starting with `ether` such as  `ether 9e:d6:53:02:4b:b6` which should now look different from the previous values.

Your MAC address should now randomize each time you restart your computer or restart the `sys-net` VM.

---

## Usage Notes - Macchanger

This approach to MAC Randomizing has been tested and used by some users as well as some of the Qubes team. Observations that are to be expected are:

- This does not randomize your MAC Address on sleep and wake state (only on restarting the `sys-net` VM)
- The `sys-net` networking VM takes longer for device drivers to start up than usual, this delayed startup may cause the first attempt of `sys-whonix` to connect to Tor to fail

## Disabling / Uninstalling Macchanger

To disable MAC Randomizing if you find that a network connecting to does not like changing MAC Addresses, you can disable temporarily or if you want to permanently remove this solution, do the following:

**Disable Temporarily**

- Go to the `Services` pane on your `sys-net` and uncheck all services starting with `macspoof-`

**Uninstall Permanently**

- Go to the `Services` pane on your `sys-net` and highlight the services starting with `macspoof-`
- Now click the `-` minus button to remove the service
- In your `fedora-23` type `sudo systemctl disable macspoof@wlp0s1`
- Also in `fedora-23` type `sudo systemctl disable macspoof@enp0s0`
- Remove the service file `sudo rm /etc/systemd/system/macspoof@.service` in TemplateVM
- Delete the package `sudo dnf remove macchanger`
