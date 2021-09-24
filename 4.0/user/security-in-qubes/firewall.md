---
lang: en
layout: doc
permalink: /doc/4.0/4.0/firewall/
redirect_from:
- /doc/qubes-firewall/
- /en/doc/qubes-firewall/
- /doc/QubesFirewall/
- /wiki/QubesFirewall/
ref: 166
title: Firewall
---

Understanding firewalling in Qubes
----------------------------------

Every qube in Qubes is connected to the network via a FirewallVM, which is used to enforce network-level policies.
By default there is one default FirewallVM, but the user is free to create more, if needed.

For more information, see the following:

- [https://groups.google.com/group/qubes-devel/browse\_thread/thread/9e231b0e14bf9d62](https://groups.google.com/group/qubes-devel/browse_thread/thread/9e231b0e14bf9d62)
- [https://blog.invisiblethings.org/2011/09/28/playing-with-qubes-networking-for-fun.html](https://blog.invisiblethings.org/2011/09/28/playing-with-qubes-networking-for-fun.html)

How to edit rules
-----------------

In order to edit rules for a given qube, select it in the Qube Manager and press the "firewall" button.

![r4.0-manager-firewall.png](/attachment/doc/r4.0-manager-firewall.png)

If the qube is running, you can open Settings from the Qube Popup Menu.

*R4.0 note:* ICMP and DNS are no longer accessible in the GUI, but can be changed via `qvm-firewall` described below.
Connections to Updates Proxy are not made over a network so can not be allowed or blocked with firewall rules, but are controlled using the relevant policy file (see [R4.0 Updates proxy](/doc/software-update-vm/) for more detail).

Note that if you specify a rule by DNS name it will be resolved to IP(s) *at the moment of applying the rules*, and not on the fly for each new connection.
This means it will not work for servers using load balancing, and traffic to complex web sites which draw from many servers will be difficult to control.

Instead of using the firewall GUI, you can use the `qvm-firewall` command in Dom0 to edit the firewall rules by hand.
This gives you greater control than by using the GUI.

The firewall rules for each qube are saved in an XML file in that qube's directory in dom0:

```
/var/lib/qubes/appvms/<vm-name>/firewall.xml
```

Rules are implemented on the netvm.

You can also manually create rules in the qube itself using standard firewalling controls.
See [Where to put firewall rules](#where-to-put-firewall-rules).
In complex cases, it might be appropriate to load a ruleset using `iptables-restore` called from `/rw/config/rc.local`.
if you do this, be aware that `rc.local` is called *after* the network is up, so local rules should not be relied upon to block leaks.

Reconnecting qubes after a NetVM reboot
-------------------------------------

Normally Qubes doesn't let the user stop a NetVM if there are other qubes running which use it as their own NetVM.
But in case the NetVM stops for whatever reason (e.g. it crashes, or the user forces its shutdown via qvm-kill via terminal in Dom0), Qubes R4.0 will often automatically repair the connection.
If it does not, then there is an easy way to restore the connection to the NetVM by issuing in dom0:

` qvm-prefs <vm> netvm <netvm> `

Normally qubes do not connect directly to the actual NetVM which has networking devices, but rather to the default sys-firewall first, and in most cases it would be the NetVM that will crash, e.g. in response to S3 sleep/restore or other issues with WiFi drivers.
In that case it is only necessary to issue the above command once, for the sys-firewall (this assumes default VM-naming used by the default Qubes installation):

` qvm-prefs sys-firewall netvm sys-net `

Network service qubes
---------------------

Qubes does not support running any networking services (e.g. VPN, local DNS server, IPS, ...) directly in a qube that is used to run the Qubes firewall service (usually sys-firewall) for good reasons.
In particular, if you want to ensure proper functioning of the Qubes firewall, you should not tinker with iptables or nftables rules in such qubes.

Instead, you should deploy a network infrastructure such as

~~~
sys-net <--> sys-firewall-1 <--> network service qube <--> sys-firewall-2 <--> [client qubes]
~~~

Thereby sys-firewall-1 is only needed if you have other client qubes connected there, or you want to manage the traffic of the local network service qube.
The sys-firewall-2 proxy ensures that:

1. Firewall changes done in the network service qube cannot render the Qubes firewall ineffective.
2. Changes to the Qubes firewall by the Qubes maintainers cannot lead to unwanted information leakage in combination with user rules deployed in the network service qube.
3. A compromise of the network service qube does not compromise the Qubes firewall.

If you adopt this model, you should be aware that all traffic will arrive at the `network service qube` appearing to originate from the IP address of `sys-firewall-2`.

For the VPN service please also look at the [VPN documentation](https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/vpn.md).

Enabling networking between two qubes
-------------------------------------

Normally any networking traffic between qubes is prohibited for security reasons.
However, in special situations, you might want to selectively allow specific qubes to establish networking connectivity between each other.
For example, this might be useful in some development work, when you want to test networking code, or to allow file exchange between HVM domains (which do not have Qubes tools installed) via SMB/scp/NFS protocols.

In order to allow networking between qubes A and B follow these steps:

- Make sure both A and B are connected to the same firewall vm (by default all VMs use the same firewall VM).
- Note the Qubes IP addresses assigned to both qubes.
  This can be done using the `qvm-ls -n` command, or via the Qubes Manager preferences pane for each qube.
- Start both qubes, and also open a terminal in the firewall VM
- In the firewall VM's terminal enter the following iptables rule:

~~~
sudo iptables -I FORWARD 2 -s <IP address of A> -d <IP address of B> -j ACCEPT
~~~

- In qube B's terminal enter the following iptables rule:

~~~
sudo iptables -I INPUT -s <IP address of A> -j ACCEPT
~~~

- Now you should be able to reach B from A -- test it using e.g. ping issued from A.
  Note however, that this doesn't allow you to reach A from B -- for this you would need two more rules, with A and B swapped.
- If everything works as expected, then you should write the above iptables rules into firewallVM's `qubes-firewall-user-script` script.
  This script is run when the netvm starts up.
  You should also write relevant rules in A and B's `rc.local` script which is run when the qube is launched.
  Here's an example how to update the script:

~~~
[user@sys-firewall ~]$ sudo bash
[root@sys-firewall user]# echo "iptables -I FORWARD 2 -s 10.137.2.25 -d 10.137.2.6 -j ACCEPT" >> /rw/config/qubes-firewall-user-script
[root@sys-firewall user]# chmod +x /rw/config/qubes-firewall-user-script
~~~

- Here is an example how to update `rc.local`:

~~~
[user@B ~]$ sudo bash
[root@B user]# echo "iptables -I INPUT -s 10.137.2.25 -j ACCEPT" >> /rw/config/rc.local
[root@B user]# chmod +x /rw/config/rc.local
~~~

Opening a single TCP port to other network-isolated qube
--------------------------------------------------------

In the case where a specific TCP port needs to be exposed from a qubes to another one, you do not need to enable networking between them but you can use the qubes RPC service `qubes.ConnectTCP`.

**1. Simple port binding**

Consider the following example. `mytcp-service` qube has a TCP service running on port `444` and `untrusted` qube needs to access this service.

- In dom0, add the following to `/etc/qubes-rpc/policy/qubes.ConnectTCP`:

    ~~~
    untrusted @default allow,target=mytcp-service
    ~~~

- In untrusted, use the Qubes tool `qvm-connect-tcp`:

    ~~~
    [user@untrusted #]$ qvm-connect-tcp 444:@default:444
    ~~~

> Note: The syntax is the same as SSH tunnel handler. The first `444` correspond to the localport destination of `untrusted`, `@default` the remote machine and the second `444` to the remote machine port.

The service of `mytcp-service` running on port `444` is now accessible in `untrusted` as `localhost:444`.

Here `@default` is used to hide the destination qube which is specified in the Qubes RPC policy by `target=mytcp-service`. Equivalent call is to use the tool as follow:

~~~
  [user@untrusted #]$ qvm-connect-tcp ::444
~~~

which means to use default local port of `unstrusted` as the same of the remote port and unspecified destination qube is `@default` by default in `qrexec` call.

**2. Binding remote port on another local port**

Consider now the case where someone prefers to specify the destination qube and use another port in untrusted,for example `10044`. Instead of previous case, add

~~~
untrusted mytcp-service allow
~~~

in `/etc/qubes-rpc/policy/qubes.ConnectTCP` and in untrusted, use the tool as follow:

~~~
  [user@untrusted #]$ qvm-connect-tcp 10444:mytcp-service:444
~~~

The service of `mytcp-service` running on port `444` is now accessible in `untrusted` as `localhost:10444`.

**3. Binding to different qubes using RPC policies**

One can go further than the previous examples by redirecting different ports to different qubes. For example, let assume that another qube `mytcp-service-bis` with a TCP service is running on port `445`. If someone wants `untrusted` to be able to reach this service but port `445` is reserved to `mytcp-service-bis` then, in dom0, add the following to `/etc/qubes-rpc/policy/qubes.ConnectTCP+445`:

~~~
untrusted @default allow,target=mytcp-service-bis
~~~

In that case, calling `qvm-connect-tcp` like previous examples, will still bind TCP port `444` of `mytcp-service` to `untrusted` but now, calling it with port `445`

~~~
  [user@untrusted #]$ qvm-connect-tcp ::445
~~~

will restrict the binding to only the corresponding TCP port of `mytcp-service-bis`.

**4. Permanent port binding**

For creating a permanent port bind between two qubes, `systemd` can be used. We use the case of the first example. In `/rw/config` (or any place you find suitable) of qube `untrusted`, create `my-tcp-service.socket` with content:

~~~
[Unit]
Description=my-tcp-service

[Socket]
ListenStream=127.0.0.1:444
Accept=true

[Install]
WantedBy=sockets.target
~~~

and `my-tcp-service@.service` with content:

~~~
[Unit]
Description=my-tcp-service

[Service]
ExecStart=qrexec-client-vm '' qubes.ConnectTCP+444
StandardInput=socket
StandardOutput=inherit
~~~

In `/rw/config/rc.local`, append the lines:

~~~
cp -r /rw/config/my-tcp-service.socket /rw/config/my-tcp-service@.service /lib/systemd/system/
systemctl daemon-reload
systemctl start my-tcp-service.socket
~~~

When the qube `unstrusted` has started (after a first reboot), you can directly access the service of `mytcp-service` running on port `444` as `localhost:444`.

Port forwarding to a qube from the outside world
------------------------------------------------

In order to allow a service present in a qube to be exposed to the outside world in the default setup (where the qube has sys-firewall as network VM, which in turn has sys-net as network VM) the following needs to be done:

- In the sys-net VM:
  - Route packets from the outside world to the sys-firewall VM
  - Allow packets through the sys-net VM firewall
- In the sys-firewall VM:
  - Route packets from the sys-net VM to the VM
  - Allow packets through the sys-firewall VM firewall
- In the qube:
  - Allow packets through the qube firewall to reach the service

As an example we can take the use case of a web server listening on port 443 that we want to expose on our physical interface eth0, but only to our local network 192.168.x.0/24.

> Note: To have all interfaces available and configured, make sure the 3 qubes are up and running

> Note: [Issue #4028](https://github.com/QubesOS/qubes-issues/issues/4028) discusses adding a command to automate exposing the port.

**1. Identify the IP addresses you will need to use for sys-net, sys-firewall and the destination qube.**

You can get this information from the Settings Window for the qube, or by running this command in each qube:
`ifconfig | grep -i cast `
Note the IP addresses you will need.
> Note: The vifx.0 interface is the one used by qubes connected to this netvm so it is _not_ an outside world interface.

**2. Route packets from the outside world to the FirewallVM**

In the sys-net VM's Terminal, code a natting firewall rule to route traffic on the outside interface for the service to the sys-firewall VM

```
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 192.168.x.x -j DNAT --to-destination 10.137.1.x
```

Code the appropriate new filtering firewall rule to allow new connections for the service

```
iptables -I FORWARD 2 -i eth0 -d 10.137.1.x -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT
```

> If you want to expose the service on multiple interfaces, repeat the steps described in part 1 for each interface.
> In Qubes R4, at the moment ([QubesOS/qubes-issues#3644](https://github.com/QubesOS/qubes-issues/issues/3644)), nftables is also used which imply that additional rules need to be set in a `qubes-firewall` nft table with a forward chain.

`nft add rule ip qubes-firewall forward meta iifname eth0 ip daddr 10.137.0.x tcp dport 443 ct state new counter accept`

Verify you are cutting through the sys-net VM firewall by looking at its counters (column 2)

```
iptables -t nat -L -v -n
iptables -L -v -n
```

> Note: On Qubes R4, you can also check the nft counters

```
nft list table ip qubes-firewall
```

Send a test packet by trying to connect to the service from an external device

```
telnet 192.168.x.x 443
```

Once you have confirmed that the counters increase, store these command in `/rw/config/rc.local` so they get set on sys-net start-up

```
sudo nano /rw/config/rc.local
```

~~~
#!/bin/sh


####################
# My service routing

# Create a new firewall natting chain for my service
if iptables -w -t nat -N MY-HTTPS; then

# Add a natting rule if it did not exit (to avoid cluter if script executed multiple times)
  iptables -w -t nat -A MY-HTTPS -j DNAT --to-destination 10.137.1.x

fi


# If no prerouting rule exist for my service
if ! iptables -w -t nat -n -L PREROUTING | grep --quiet MY-HTTPS; then

# add a natting rule for the traffic (same reason)
  iptables -w -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 192.168.0.x -j MY-HTTPS
fi


######################
# My service filtering

# Create a new firewall filtering chain for my service
if iptables -w -N MY-HTTPS; then

# Add a filtering rule if it did not exit (to avoid cluter if script executed multiple times)
  iptables -w -A MY-HTTPS -s 192.168.x.0/24 -j ACCEPT

fi

# If no forward rule exist for my service
if ! iptables -w -n -L FORWARD | grep --quiet MY-HTTPS; then

# add a forward rule for the traffic (same reason)
  iptables -w -I FORWARD 2 -d 10.137.1.x -p tcp --dport 443 -m conntrack --ctstate NEW -j MY-HTTPS

fi
~~~

> Note: Again in R4 the following needs to be added:

~~~
#############
# In Qubes R4

# If not already present
if nft -nn list table ip qubes-firewall | grep "tcp dport 443 ct state new"; then

# Add a filtering rule
  nft add rule ip qubes-firewall forward meta iifname eth0 ip daddr 10.137.0.x tcp dport 443 ct state new counter accept

fi
~~~

**3. Route packets from the FirewallVM to the VM**

In the sys-firewall VM's Terminal, code a natting firewall rule to route traffic on its outside interface for the service to the qube

```
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 10.137.1.x -j DNAT --to-destination 10.137.2.y
```

Code the appropriate new filtering firewall rule to allow new connections for the service

```
iptables -I FORWARD 2 -i eth0 -s 192.168.x.0/24 -d 10.137.2.y -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT
```

> Note: If you do not wish to limit the IP addresses connecting to the service, remove the ` -s 192.168.0.1/24 `

> Note: On Qubes R4

```
nft add rule ip qubes-firewall forward meta iifname eth0 ip saddr 192.168.x.0/24 ip daddr 10.137.0.y tcp dport 443 ct state new counter accept
```

Once you have confirmed that the counters increase, store these command in `/rw/config/qubes-firewall-user-script`

```
sudo nano /rw/config/qubes-firewall-user-script
```

~~~
#!/bin/sh


####################
# My service routing

# Create a new firewall natting chain for my service
if iptables -w -t nat -N MY-HTTPS; then

# Add a natting rule if it did not exit (to avoid cluter if script executed multiple times)
  iptables -w -t nat -A MY-HTTPS -j DNAT --to-destination 10.137.2.y

fi


# If no prerouting rule exist for my service
if ! iptables -w -t nat -n -L PREROUTING | grep --quiet MY-HTTPS; then

# add a natting rule for the traffic (same reason)
  iptables -w -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 10.137.1.x -j MY-HTTPS
fi


######################
# My service filtering

# Create a new firewall filtering chain for my service
if iptables -w -N MY-HTTPS; then

# Add a filtering rule if it did not exit (to avoid cluter if script executed multiple times)
  iptables -w -A MY-HTTPS -s 192.168.x.0/24 -j ACCEPT

fi

# If no forward rule exist for my service
if ! iptables -w -n -L FORWARD | grep --quiet MY-HTTPS; then

# add a forward rule for the traffic (same reason)
  iptables -w -I FORWARD 4 -d 10.137.2.y -p tcp --dport 443 -m conntrack --ctstate NEW -j MY-HTTPS

fi

################
# In Qubes OS R4

# If not already present
if ! nft -nn list table ip qubes-firewall | grep "tcp dport 443 ct state new"; then

# Add a filtering rule
  nft add rule ip qubes-firewall forward meta iifname eth0 ip saddr 192.168.x.0/24 ip daddr 10.137.0.y tcp dport 443 ct state new counter accept

fi
~~~

Finally make this file executable (so it runs at every Firewall VM update)

~~~
sudo chmod +x /rw/config/qubes-firewall-user-script
~~~

**4. Allow packets into the qube to reach the service**

Here no routing is required, only filtering.
Proceed in the same way as above but store the filtering rule in the `/rw/config/rc.local` script.

```
sudo name /rw/config/rc.local
```

~~~
######################
# My service filtering

# Create a new firewall filtering chain for my service
if iptables -w -N MY-HTTPS; then

# Add a filtering rule if it did not exit (to avoid cluter if script executed multiple times)
  iptables -w -A MY-HTTPS -j ACCEPT

fi

# If no input rule exists for my service
if ! iptables -w -n -L INPUT | grep --quiet MY-HTTPS; then

# add a forward rule for the traffic (same reason)
  iptables -w -I INPUT 5 -d 10.137.2.x -p tcp --dport 443 -m conntrack --ctstate NEW -j MY-HTTPS

fi
~~~

This time testing should allow connectivity to the service as long as the service is up :-)

Where to put firewall rules
---------------------------

Implicit in the above example [scripts](/doc/config-files/), but worth calling attention to: for all qubes *except* those supplying networking, iptables commands should be added to the `/rw/config/rc.local` script.
For app qubes supplying networking (`sys-firewall` inclusive), iptables commands should be added to `/rw/config/qubes-firewall-user-script`.

Firewall troubleshooting
------------------------

Firewall logs are stored in the systemd journal of the qube the firewall is running in (probably `sys-firewall`).
You can view them by running `sudo journalctl -u qubes-firewall.service` in the relevant qube.
Sometimes these logs can contain useful information about errors that are preventing the firewall from behaving as you would expect.
