---
lang: en
layout: doc
permalink: /doc/vpn-troubleshooting/
ref: 240
title: VPN troubleshooting
---

## Tips

* If using qubes-vpn, check the VPN service's log in the VPN VM by running:

    ~~~
    sudo journalctl -u qubes-vpn-handler
    ~~~

* Always test your basic VPN connection before adding scripts.

* Test DNS: Ping a familiar domain name from an appVM. It should print the IP address for the domain.

* Use `iptables -L -v` and `iptables -L -v -t nat` to check firewall rules. The latter shows the critical PR-QBS chain that enables DNS forwarding.

## VPN does not reconnect after suspend

This applies when using OpenVPN.

After suspend/resume, OpenVPN may not automatically reconnect. In order to get it to work, you must kill the OpenVPN process and restart it.

## VPN stuck at "Ready to start link"

After setting up OpenVPN and restarting the VM, you may be repeatedly getting the popup "Ready to start link", but the VPN isn't connected.

To figure out the root of the problem, check the VPN logs in `/var/logs/syslog`. The log may reveal issues like missing OpenVPN libraries, which you can then install.

## `notify-send` induced failure
[Some VPN guides](https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md) use complex scripts that by themselves include call of `notify-send`, yet some images may not contain this tool or may not have it working properly.
For instance calling `notify-send` on `fedora-36` template VM gives:
```
Failed to execute child process “dbus-launch” (No such file or directory)
```

To check this tool is working properly run:
```bash
sudo notify-send "$(hostname): Test notify-send OK" --icon=network-idle
```
You should see `info` message appear on the top of your scree.
If that is the case then, `notify-send` is not the issue.
If it is not, and you have an error of some sort you can:
1. Remove all calls of `notify-send` from scripts you are using to start VPN
2. Use other template VM that have `notify-send` working or find proper guide and make your current template VM run `notify-send` work properly.
