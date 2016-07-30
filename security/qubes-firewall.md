---
layout: doc
title: Qubes Firewall
permalink: /doc/qubes-firewall/
redirect_from:
- /en/doc/qubes-firewall/
- /doc/QubesFirewall/
- /wiki/QubesFirewall/
---

Understanding Qubes networking and firewall
===========================================

Understanding firewalling in Qubes
----------------------------------

Every VM in Qubes is connected to the network via a FirewallVM, which is used to
enforce network-level policies. By default there is one default Firewall VM, but
the user is free to create more, if needed.

For more information, see the following:

-   [https://groups.google.com/group/qubes-devel/browse\_thread/thread/9e231b0e14bf9d62](https://groups.google.com/group/qubes-devel/browse_thread/thread/9e231b0e14bf9d62)
-   [http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html](http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html)

How to edit rules
-----------------

In order to edit rules for a given domain, select this domain in the Qubes
Manager and press the "firewall" button:

![r2b1-manager-firewall.png](/attachment/wiki/QubesFirewall/r2b1-manager-firewall.png)

Note that if you specify a rule by DNS name it will be resolved to IP(s)
*at the moment of applying the rules*, and not on the fly for each new
connection. This means it will not work for servers using load balancing. More
on this in the message quoted below.

Alternatively, one can use the `qvm-firewall` command from Dom0 to edit the
firewall rules by hand. The firewall rules for each VM are saved in an XML file
in that VM's directory in dom0:

    /var/lib/qubes/appvms/<vm-name>/firewall.xml

Reconnecting VMs after a NetVM reboot
----------------------------------------

Normally Qubes doesn't let the user to stop a NetVM if there are other VMs
running which use it as their own NetVM. But in case the NetVM stops for
whatever reason (e.g. it crashes, or the user forces its shutdown via qvm-kill
via terminal in Dom0), then there is an easy way to restore the connection to
the netvm by issuing:

` qvm-prefs <vm> -s netvm <netvm> `

Normally VMs do not connect directly to the actual NetVM which has networking
devices, but rather to the default FirewallVM first, and in most cases it would
be the NetVM that would crash, e.g. in response to S3 sleep/restore or other
issues with WiFi drivers. In that case it is necessary to just issue the above
command once, for the FirewallVM (this assumes default VM-naming used by the
default Qubes installation):

` qvm-prefs firewallvm -s netvm netvm `

Enabling networking between two VMs
--------------------------------------

Normally any networking traffic between VMs is prohibited for security reasons.
However, in special situations, one might want to selectively allow specific VMs
to be able to establish networking connectivity between each other. For example,
this might come useful in some development work, when one wants to test
networking code, or to allow file exchange between HVM domains (which do not
have Qubes tools installed) via SMB/scp/NFS protocols.

In order to allow networking between VM A and B follow those steps:

* Make sure both A and B are connected to the same firewall vm (by default all
  VMs use the same firewall VM).
* Note the Qubes IP addresses assigned to both VMs. This can be done using the
  `qvm-ls -n` command, or via the Qubes Manager preferences pane for each VM.
* Start both VMs, and also open a terminal in the firewall VM
* In the firewall VM's terminal enter the following iptables rule:

~~~
sudo iptables -I FORWARD 2 -s <IP address of A> -d <IP address of B> -j ACCEPT
~~~

* In VM B's terminal enter the following iptables rule:

~~~
sudo iptables -I INPUT -s <IP address of A> -j ACCEPT
~~~

* Now you should be able to reach the VM B from A -- test it using e.g. ping
  issued from VM A. Note however, that this doesn't allow you to reach A from
  B -- for this you would need two more rules, with A and B swapped.
* If everything works as expected, then the above iptables rules should be
  written into firewall VM's `qubes-firewall-user-script` script which is run
  on every firewall update, and A and B's `rc.local` script which is run when
  the vm is launched. The `qubes-firewall-user-script` is necessary because Qubes
  orders every firewall VM to update all the rules whenever new VM is started in
  the system. If we didn't enter our rules into this "hook" script, then shortly
  our custom rules would disappear and inter-VM networking would stop working.
  Here's an example how to update the script (note that, by default, there is no
  script file present, so we likely will be creating it, unless we had some other
  custom rules defines earlier in this firewallvm):

~~~
[user@sys-firewall ~]$ sudo bash
[root@sys-firewall user]# echo "iptables -I FORWARD 2 -s 10.137.2.25 -d 10.137.2.6 -j ACCEPT" >> /rw/config/qubes-firewall-user-script
[root@sys-firewall user]# chmod +x /rw/config/qubes-firewall-user-script
~~~

* Here is an example how to update `rc.local`:

~~~
[user@B ~]$ sudo bash
[root@B user]# echo "iptables -I INPUT -s 10.137.2.25 -j ACCEPT" >> /rw/config/rc.local
[root@B user]# chmod +x /rw/config/rc.local
~~~

Port forwarding to a VM from the outside world
--------------------------------------------------

In order to allow a service present in a VM to be exposed to the outside world
in the default setup (where the VM has the Firewall VM as network VM, which in
turn has the Net VM as network VM)
the following needs to be done:

 * In the sys-net VM:
    * Route packets from the outside world to the sys-firewall VM
    * Allow packets through the sys-net VM firewall
 * In the sys-firewall VM:
    * Route packets from the sys-net VM to the VM
    * Allow packets through the sys-firewall VM firewall
 * In the VM:
    * Allow packets in the VM firewall to reach the service

As an example we can take the use case of a web server listening on port 443
that we want to expose on our physical interface eth0, but only to our local
network 192.168.x.0/24.

**1. Route packets from the outside world to the FirewallVM**

From a Terminal window in sys-net VM, take note of the 'Interface name' and
'IP address' on which you want to expose your service (i.e. eth0, 192.168.x.x)

` ifconfig | grep -i cast `

> Note: The vifx.0 interface is the one connected to your sys-firewall VM so it
  is _not_ an outside world interface...

From a Terminal window in sys-firewall VM, take note of the 'IP address' for
interface Eth0

` ifconfig | grep -i cast `

Back into the sys-net VM's Terminal, code a natting firewall rule to route
traffic on the outside interface for the service to the sys-firewall VM

` iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 192.168.x.x -j DNAT --to-destination 10.137.1.x `

Code the appropriate new filtering firewall rule to allow new connections for
the service

` iptables -I FORWARD 2 -i eth0 -d 10.137.1.x -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT `

> Note: If you want to expose the service on multiple interfaces, repeat the
  steps described in part 1 for each interface

Verify you are cutting through the sys-net VM firewall by looking at its
counters (column 2)

` iptables -t nat -L -v -n `

` iptables -L -v -n `

Try to connect to the service from an external device

` telnet 192.168.x.x 443 `

Once you have confirmed that the counters increase, store these command in
'/rw/config/rc.local'

` sudo nano /rw/config/rc.local `

~~~
#!/bin/sh


####################
# My service routing

# Create a new firewall natting chain for my service
if iptables -t nat -N MY-HTTPS; then

# Add a natting rule if it did not exit (to avoid cluter if script executed multiple times)
  iptables -t nat -A MY-HTTPS -j DNAT --to-destination 10.137.1.x

fi


# If no prerouting rule exist for my service
if ! iptables -t nat -n -L PREROUTING | grep --quiet MY-HTTPS; then

# add a natting rule for the traffic (same reason)
  iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 192.168.0.x -j MY-HTTPS
fi


######################
# My service filtering

# Create a new firewall filtering chain for my service
if iptables -N MY-HTTPS; then

# Add a filtering rule if it did not exit (to avoid cluter if script executed multiple times)
  iptables -A MY-HTTPS -s 192.168.x.0/24 -j ACCEPT

fi

# If no prerouting rule exist for my service
if ! iptables -n -L FORWARD | grep --quiet MY-HTTPS; then

# add a natting rule for the traffic (same reason)
  iptables -I FORWARD 2 -d 10.137.1.x -p tcp --dport 443 -m conntrack --ctstate NEW -j MY-HTTPS

fi
~~~

Finally make this file executable, so it runs at each boot

` sudo chmod +x /rw/config/rc.local `

**2. Route packets from the FirewallVM to the VM**

From a Terminal window in the VM, take note of the 'IP address' for
interface Eth0 (i.e. 10.137.2.x)

` ifconfig | grep -i cast `

Back into the sys-firewall VM's Terminal, code a natting firewall rule to route
traffic on its outside interface for the service to the VM

` iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 10.137.1.x -j DNAT --to-destination 10.137.2.y `

Code the appropriate new filtering firewall rule to allow new connections for
the service

` iptables -I FORWARD 2 -i eth0 -s 192.168.0.0/24 -d 10.137.2.y -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT `

> Note: If you do not wish to limit the IP addresses connecting to the service,
  remove the ` -s 192.168.0.1/24 `

Once you have confirmed that the counters increase, store these command in
'/rw/config/qubes-firewall-user-script'

~~~
#!/bin/sh


####################
# My service routing

# Create a new firewall natting chain for my service
if iptables -t nat -N MY-HTTPS; then

# Add a natting rule if it did not exit (to avoid cluter if script executed multiple times)
  iptables -t nat -A MY-HTTPS -j DNAT --to-destination 10.137.2.x

fi


# If no prerouting rule exist for my service
if ! iptables -t nat -n -L PREROUTING | grep --quiet MY-HTTPS; then

# add a natting rule for the traffic (same reason)
  iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 10.137.1.x -j MY-HTTPS
fi


######################
# My service filtering

# Create a new firewall filtering chain for my service
if iptables -N MY-HTTPS; then

# Add a filtering rule if it did not exit (to avoid cluter if script executed multiple times)
  iptables -A MY-HTTPS -s 192.168.x.0/24 -j ACCEPT

fi

# If no prerouting rule exist for my service
if ! iptables -n -L FORWARD | grep --quiet MY-HTTPS; then

# add a natting rule for the traffic (same reason)
  iptables -I FORWARD 4 -d 10.137.2.x -p tcp --dport 443 -m conntrack --ctstate NEW -j MY-HTTPS

fi
~~~

Finally make this file executable (so it runs at every Firewall VM update)

~~~
sudo chmod +x /rw/config/qubes-firewall-user-script
~~~

**3. Allow packets into the VM to reach the service**

Here no routing is required, only filtering. Proceed in the same way as above
but store the filtering rule in the '/rw/config/rc.local' script.

~~~
######################
# My service filtering

# Create a new firewall filtering chain for my service
if iptables -N MY-HTTPS; then

# Add a filtering rule if it did not exit (to avoid cluter if script executed multiple times)
  iptables -A MY-HTTPS -s 192.168.x.0/24 -j ACCEPT

fi

# If no prerouting rule exist for my service
if ! iptables -n -L FORWARD | grep --quiet MY-HTTPS; then

# add a natting rule for the traffic (same reason)
  iptables -I INPUT 5 -d 10.137.2.x -p tcp --dport 443 -m conntrack --ctstate NEW -j MY-HTTPS

fi
~~~

This time testing should allow connectivity to the service as long as the
service is up :-)

Where to put firewall rules
---------------------------

Implicit in the above example [scripts](/doc/config-files/), but worth 
calling attention to: for all VMs *except* ProxyVMs, iptables commands 
should be added to the `/rw/config/rc.local` script. For ProxyVMs 
(`sys-firewall` inclusive), iptables commands should be added to 
`/rw/config/qubes-firewall-user-script`. This is because a ProxyVM is 
constantly adjusting its firewall, and therefore initial settings from 
`rc.local` do not persist.

