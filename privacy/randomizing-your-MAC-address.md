---
layout: doc
title: Randomizing your MAC Address
permalink: /doc/randomizing-your-mac-address/
---

Randomizing your MAC Address
============================

Changing the default [MAC Address](https://en.wikipedia.org/wiki/MAC_address) of your hardware is crucial in protecting 
privacy. Currently, Qubes OS *does not* "randomize" or spoof the MAC Address, so until this is implemented by default 
you can randomize your MAC Address by the following.

## Configuring Qubes

 
First thing you need to do is install **macchanger** package by opening your `fedora-23` TemplateVM and typing

```
sudo dnf install macchanger
```

Then create the file `macspoof@.service` in `fedora-23` located at `/etc/systemd/system/` directory

```
vim /etc/systemd/system/macspoof@.service
```

Paste the following inside of that newly created file

```
[Unit]
Description=macchanger on %I
# Hack since macspoof@%i contains @ which is not allowed yet
ConditionPathExists=/var/run/qubes-service/macspoof-%i
Wants=network-pre.target
Before=network-pre.target
BindsTo=sys-subsystem-net-devices-%i.device
After=sys-subsystem-net-devices-%i.device

[Service]
ExecStart=/usr/bin/macchanger -r %I
Type=oneshot

[Install]
WantedBy=multi-user.target
```

**Get the right iface names**

It's crucial to get the correct **iface name** for the devices (ethernet and wifi) you want to randomize. To get this,
open your `sys-net` (or wherever your device drivers are) and type in `terminal` the command `ifconfig` the printout 
will look like:

```
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
```

The **iface name** values you're interested in are `enp0s0` and `wlp0s1` as those represent your ethernet and wifi 
devices, respectively.

Also, in this prinout is your **actual MAC addresses** which are needed to verify the randomizing is working correctly.  
In this example, the ethernet and wifi addresses are `ether 9e:d6:53:02:4b:b6` and `ether 06:6d:70:a8:7b:35` 
respectively.  *Copy these MAC addresses down somewhere for later.*

Now, go back to your `fedora-23` TemplateVM and use the `touch` command to create service files in the appropriate 
place, note that the `iface name` values at the end:

```
cd /var/run/qubes-service/
sudo touch macspoof-enp0s0
sudo touch macspoof-wlp0s1
```

Verify the correct files exist in the directory

```
[user@fedora-23 qubes-service]$ ls
cups             macspoof-wlp0s1  qubes-update-check
macspoof-enp0s0  meminfo-writer   updates-proxy-setup
```

Now, also within the TemplateVM, type the following commands for each hardware device that you want to randomize a MAC 
addresses for

```
sudo systemctl enable macspoof@wlp0s1
Created symlink from /etc/systemd/system/multi-user.target.wants/macspoof@wlp0s1.service to /etc/systemd/system/macspoof@.service.
sudo systemctl enable macspoof@enp0s0
Created symlink from /etc/systemd/system/multi-user.target.wants/macspoof@enp0s0.service to /etc/systemd/system/macspoof@.service.
```

Then open up Terminal for `dom0` and enable the Qubes services for your `sys-net` VM by doing the following for each 
device

```
qubes-service -e sys-net macspoof-wlp0s1
qubes-service -e sys-net macspood-enp0s0
```

Now do the following and you should be ready to go

- Stop your `fedora-23` VM
- Stop your `sys-net` VM and restart it

To verify this worked corectly, look at the `Services` pane of your VM Settings window, which should look like

![sys-net Services Pane](/attachment/wiki/QubesScreenshots/r3rc1-sys-net-services.png)

**Verify it works**

Go back to your `sys-net` VM terminal, type `ifconfig` and look at the values starting with `ether` such as  `ether 
9e:d6:53:02:4b:b6` which should now look different from the previous values.

Your MAC address should now randomize each time you restart your computer or restart the `sys-net` VM.

---

## Usage Notes

This approach to MAC Randomizing has been tested and used by some users as well as some of the Qubes team. Observations 
that are to be expected are:

- This does not randomize your MAC Address on sleep and wake state (only on restarting the `sys-net` VM)
- The `sys-net` networking VM takes longer for device drivers to start up than usual
- Delayed startup causes connecting to wifi and makes `sys-whonix` first attempt connecting to Tor to fail
- You can configure `macchanger` to use the `-e` flag which randomizes address by same device vendor/manufacturer, 
instead of our example (which uses `-r` to make a totally random MAC address). Alter the following line:

```
ExecStart=/usr/bin/macchanger -e %I
```

## Disabling / Uninstalling

To disable MAC Randomizing if you find that a network connecting to does not like changing MAC Addresses, you can 
disable temporarily or if you want to permanently remove this solution, do the following:

**Disable Temporarily**

- Go to the `Services` pane on your `sys-net` and uncheck all services starting with `macspoof-`

**Uninstall Permanently**

- Go to the `Services` pane on your `sys-net` and highlight the services starting with `macspoof-`
- Now click the `-` minus button to remove the service
- In your `fedora-23` type `sudo systemctl disable macspoof@wlp0s1`
- Also in `fedora-23` type `sudo systemctl disable macspoof@enp0s0`
- Remove the service file `sudo rm /etc/systemd/system/macspoof@.service` in TemplateVM
- Delete the package `sudo dnf remove macchanger`
