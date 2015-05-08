---
layout: doc
title: QubesFirewall
permalink: /doc/QubesFirewall/
redirect_from: /wiki/QubesFirewall/
---

Understanding Qubes networking and firewall
===========================================

Understanding firewalling in Qubes
----------------------------------

Every AppVM in Qubes is connected to the network via a FirewallVM, which is used to enforce network-level policies. By default there is one default Firewall VM, but the user is free to create more, if needed.

For more information, see the following:

-   [https://groups.google.com/group/qubes-devel/browse\_thread/thread/9e231b0e14bf9d62](https://groups.google.com/group/qubes-devel/browse_thread/thread/9e231b0e14bf9d62)
-   [http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html](http://theinvisiblethings.blogspot.com/2011/09/playing-with-qubes-networking-for-fun.html)

How to edit rules
-----------------

In order to edit rules for a given domain, select this domain in the Qubes Manager and press the "firewall" button:

![r2b1-manager-firewall.png](/attachment/wiki/QubesFirewall/r2b1-manager-firewall.png)

Note that if you specify a rule by DNS name it will be resolved to IP(s) *at the moment of applying the rules*, and not on the fly for each new connection. This means it will not work for serves using load balancing. More on this in the message quoted below.

Alternatively, one can use the `qvm-firewall` command from Dom0 to edit the firewall rules by hand:

Reconnecting AppVMs after a NetVM reboot
----------------------------------------

Normally Qubes doesn't let the user to stop a NetVM if there are other AppVMs running which use it as their own NetVM. But in case the NetVM stops for whatever reason (e.g. it crashes, or the user forces its shutdown via qvm-kill via terminal in the netvm), then there is an easy way to restore the connection to the netvm by issuing:

{% highlight trac-wiki %}
qvm-prefs <appvm> -s netvm <netvm>
{% endhighlight %}

Normally AppVMs do not connect directly to the actual NetVM which has networking devices, but rather to the default FirewallVM first, and in most cases it would be the NetVM that would crash, e.g. in response to S3 sleep/restore or other issues with [WiFi?](/wiki/WiFi) drivers. In that case it is necessary to just issue the above command once, for the FirewallVM (this assumes default VM-nameing used by the default Qubes installation):

{% highlight trac-wiki %}
qvm-prefs firewallvm -s netvm netvm
{% endhighlight %}

Enabling networking between two AppVMs
--------------------------------------

Normally any networking traffic between VMs is prohibited for security reasons. However, in special situations, one might one to selectively allow specific AppVMs to be able to establish networking connectivity between each other. For example, this might come useful in some development work, when one wants to test networking code, or to allow file exchange between HVM domains (which do not have Qubes tools installed) via SMB/scp/NFS protocols.

In order to allow networking between AppVM A and B follow those steps:

-   Make sure both A and B are connected to the same firewall vm (by default all AppVMs use the same firewall VM).
-   Note the Qubes IP addresses assigned to both AppVMs. This can be done using the `qvm-ls -n` command, or via the Qubes Manager preferences pane for each AppVM.
-   Start both AppVMs, and also open a terminal in the firewall VM
-   In the firewall VM's terminal enter the following iptables rule:

    {% highlight trac-wiki %}
    sudo iptables -I FORWARD 2 -s <IP address of A> -d <IP address of B> -j ACCEPT
    {% endhighlight %}

-   Now you should be able to reach the AppVM B from A -- test it using e.g. ping issues from AppVM A. Note however, that this doesn't allow you to reach A from B -- for this you would need another rule, with A and B addresses swapped.
-   If everything works as expected, then the above iptables rule(s) should be written into firewall VM's `qubes_firewall_user_script` script which is run on every firewall update. This is necessary, because Qubes orders every firewall VM to update all the rules whenever new VM is started in the system. If we didn't enter our rules into this "hook" script, then shortly our custom rules would disappear and inter-VM networking would stop working. Here's an example how to update the script (note that, by default, there is no script file present, so we likely will be creating it, unless we had some other custom rules defines earlier in this firewallvm):

    {% highlight trac-wiki %}
    [user@firewallvm ~]$ sudo bash
    [root@firewallvm user]# echo "iptables -I FORWARD 2 -s 10.137.2.25 -d 10.137.2.6 -j ACCEPT" >> /rw/config/qubes_firewall_user_script
    [root@firewallvm user]# chmod +x /rw/config/qubes_firewall_user_script
    {% endhighlight %}

Port forwarding to an AppVM from the outside world
--------------------------------------------------

In order to allow a service present in an AppVM to be exposed to the outside world in the default setup (where the AppVM has the FirewallVM as network VM, which in turn has the NetVM as network VM) the following needs to be done:

-   In the NetVM, allow packets to be routed from the outside world to the FirewallVM and allow packets through the NetVM firewall
-   In the FirewallVM, allow packets to be routed from the NetVM to the AppVM and allow packets through the FirewallVM firewall
-   In the AppVM, allow packets into the AppVM firewall to reach the service

As an example we can take the use case of a web server listenning on port 443 that we want to expose on our physical interface eth0, but only to our local network 192.168.0.0/24.

**1. Allow packets to be routed from the outside world for the exposed service to the FirewallVM**

In System Tools (Dom0) / Terminal, take note of the firewallVM IPAddress to which packet will be routed using ` qvm-ls -n `

In NetVM terminal, take note of the interface name and IPAddress on which you want to expose your service (i.e. eth0, 192.168.0.10) using ` ifconfig | grep -i cast `

> Note: The vifx.0 interface is the one connected to your firewallVM so it is not an outside world interface...

Still in NetVM terminal, code the appropriate natting firewall rule to intercept traffic on the inbound interface for the service and nat the destination IP address to the one of the firewallVM for the traffic to be routed there:

{% highlight trac-wiki %}
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 192.168.0.10 -j DNAT --to-destination 10.137.1.x
{% endhighlight %}

Code the appropriate new filtering firewall rule to allow new connections for the service:

{% highlight trac-wiki %}
iptables -I FORWARD 2 -i eth0 -d 10.137.1.x -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT
{% endhighlight %}

Note: If you want to expose the service on multiple interfaces, repeat the steps described in part 1 for each interface.

That's it for the netVM. You can verify you are cutting through the netVM by looking at the counters for your firewall rules:

` iptables -t nat -L -v -n `

` iptables -L -v -n `

... issue some test packets trying to connect... Obviously we have not reached the service yet but the counters should increase.

In order to ensure your set-up survive a reboot we need in the NetVM to:

Store these commands in ` /rw/config/rc.local `:

{% highlight trac-wiki %}
sudo nano /rw/config/rc.local
{% endhighlight %}

{% highlight trac-wiki %}
#!/bin/sh

/sbin/iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 192.168.0.10 -j DNAT --to-destination 10.137.1.x

/sbin/iptables -I FORWARD 2 -s 192.168.0.0/24 -d 10.137.1.x -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT
{% endhighlight %}

Make this file executable:

{% highlight trac-wiki %}
sudo chmod +x /rw/config/rc.local 
{% endhighlight %}

**2. Allow packets to be routed from the firewallVM to the appVM**

In System Tools (Dom0) / Terminal, take note of the appVM (on which the service is exposed) IPAddress using the command ` qvm-ls -n `

In FirewallVM Terminal, take note of the IPAddress for interface eth0 using the command ` ifconfig | grep -i cast `

Still in FirewallVM terminal, code the appropriate natting firewall rule to intercept traffic on the inbound interface for the service and nat the destination IP address to the one of the AppVM for the traffic to be routed there:

{% highlight trac-wiki %}
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 10.137.1.x -j DNAT --to-destination 10.137.2.y
{% endhighlight %}

Code the appropriate new filtering firewall rule to allow new connections for the service:

{% highlight trac-wiki %}
iptables -I FORWARD 2 -i eth0 -s 192.168.0.0/24 -d 10.137.2.y -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT
{% endhighlight %}

> Note: If you do not wish to limit the IP addresses connecting to the service, remove the ` -s 192.168.0.1/24 `

FirewallVM is now done. You can verify you are cutting through it in the same way as above.

This time in order to ensure your set-up survive a reboot we need in the firewallVM to:

Store these commands in ` /rw/config/qubes_firewall_user_script `:

{% highlight trac-wiki %}
#!/bin/sh

/sbin/iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -d 10.137.1.x -j DNAT --to-destination 10.137.2.y

/sbin/iptables -I FORWARD 4 -i eth0 -s 192.168.0.0/24 -d 10.137.2.y -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT
{% endhighlight %}

And again make this file executable:

{% highlight trac-wiki %}
sudo chmod +x /rw/config/qubes_firewall_user_script
{% endhighlight %}

**3. Allow packets into the AppVM to reach the service**

Here no routing is required, only filtering. Proceed in the same way as above but store the filtering rule in the `/rw/config/rc.local` script.

{% highlight trac-wiki %}
#!/bin/sh

/sbin/iptables -I INPUT 5 -p tcp --dport 443 -m conntrack --ctstate NEW -j ACCEPT
{% endhighlight %}

This time testing should allow connectivity to the service.
