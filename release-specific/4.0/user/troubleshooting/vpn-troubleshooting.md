---
lang: en
layout: doc
permalink: /doc/4.0/vpn-troubleshooting/
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
