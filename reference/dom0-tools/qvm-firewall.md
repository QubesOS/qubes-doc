---
layout: doc
title: qvm-firewall
permalink: /doc/dom0-tools/qvm-firewall/
redirect_from:
- /en/doc/dom0-tools/qvm-firewall/
- /doc/Dom0Tools/QvmFirewall/
- /wiki/Dom0Tools/QvmFirewall/
---

qvm-firewall
============

NAME
----

qvm-firewall

SYNOPSIS
--------

qvm-firewall [-n] \<vm-name\> [action] [rule spec]

Rule specification can be one of:  
1.  address|hostname[/netmask] tcp|udp port[-port]
2.  address|hostname[/netmask] tcp|udp service\_name
3.  address|hostname[/netmask] any

OPTIONS
-------

-h, --help  
Show this help message and exit

-l, --list  
List firewall settings (default action)

-a, --add  
Add rule

-d, --del  
Remove rule (given by number or by rule spec)

-P SET\_POLICY, --policy=SET\_POLICY  
Set firewall policy (allow/deny)

-i SET\_ICMP, --icmp=SET\_ICMP  
Set ICMP access (allow/deny)

-D SET\_DNS, --dns=SET\_DNS  
Set DNS access (allow/deny)

-Y SET\_YUM\_PROXY, --yum-proxy=SET\_YUM\_PROXY  
Set access to Qubes yum proxy (allow/deny). *Note:* if set to "deny", access will be rejected even if policy set to "allow"

-n, --numeric  
Display port numbers instead of services (makes sense only with --list)

AUTHORS
-------

Joanna Rutkowska \<joanna at invisiblethingslab dot com\>
Rafal Wojtczuk \<rafal at invisiblethingslab dot com\>
Marek Marczykowski \<marmarek at invisiblethingslab dot com\>
