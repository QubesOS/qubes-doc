qubes-doc---
layout: doc
title: Mesh networking / Cjdns / Hyperboria
permalink: /doc/cjdns/
redirect_from:
- /doc/privacy/cjdns/
- /en/doc/cjdns/
- /doc/CJDNS/
- /wiki/CJDNS/qubes-docqubes-docqubes-docqubes-docqubes-doc
---

How to setup a Service VM (ProxyVM) for Cjdns and Hyperboria mesh-networking
============================================================================
Starting with release 4.0, Qubes has opt-in support for IPv6 forwarding. This allows to setup a ProxyVM for [Cjdns](https://github.com/cjdelisle/cjdns/), similar to the 
Whonix proxy (sys-whonix). This allows any AppVM to have transparent mesh-networking access to other Cjdns devices in your 
local network or even accessing [Hyperboria](https://github.com/hyperboria/docs) resources.

### What is Cjdns?
> **Networking Reinvented**  
>  
> Cjdns implements an encrypted IPv6 network using public-key cryptography for address allocation and a distributed hash table for 
routing. This provides near-zero-configuration networking, and prevents many of the security and scalability issues that plague 
existing networks.  
>  
>[ *Source: https://github.com/cjdelisle/cjdns/* ]

### What is Hyperboria?
> Hyperboria is based on the Cjdns routing protocol where people connect their local meshnets via the traditional Internet to
create a global "Super Meshnet". Think of it as a new, secure Internet where everybody can create their own IPv6 addresses using
cryptography instead of buying/leasing them from central authorities like [IANA](https://en.wikipedia.org/wiki/Internet_Assigned_Numbers_Authority).  
This makes Hyperboria addresses similar to [I2P addresses](https://geti2p.net/en/docs/naming) or [Tor Onion addresses](https://www.torproject.org/docs/onion-services), but without the anonymization layer. While Cjdns/Hyperboria traffic is end-to-end encrypted, it protects against [Man-in-the-middle attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)) doesn't hide the location of the endpoints.

### Why should I use Cjdns/Hyperboria with Qubes OS?
1. For local networks, you get end-to-end encryption with near-zero-configuration.
2. For Internet applications/use cases that don't require anonymity you get a 'static' IPv6 address which never changes and nobody can take away from you. No need for DynDNS services when you are hosting something. You'll also get end-to-end encryption and protection from Man-in-the-middle attacks, so no need for the rigged SSL/TLS infrastructure of the traditional Internet. And if anonymity is not required, you'll get better performance/throughput than with I2P services or Onion services.

## Setup of a Cjdns ProxyVM
While you could install the Cjdns routing software in any AppVM, the benefit of a ProxyVM is that you can provide Cjdns and Hyperboria connectivity transparently to any AppVM without additional installation.

##### Limitations:
- The Cjdns-ProxyVM acts as a NAT-Gateway, so the Cjdns traffic between the ProxyVM and an AppVM is not encrypted. However, since this traffic is only within Qubes, it's probably acceptable for you. See https://github.com/cjdelisle/cjdns/blob/master/doc/nat-gateway.md for details.
- Since the Cjdns-ProxyVM itself is also behind a NAT (of `sys-firewall` or `sys-net` VM), the Cjdns router won't connect to other Cjdns routers in your local network `automagically` (for details regarding `beacon mode` see: https://github.com/cjdelisle/cjdns/blob/master/doc/configure.md). So no 'zero-configuration' unfortunately and some additional `manual configuration` is required. However, not everybody needs this anyway and if so, this needs to be done only once for the ProxyVM and not every AppVM. 

### 1. Create a TemplateVM (cjdns-gw)
We'll build Cjdns from the GitHub sources, which requires some additional packages. Best is if you `Clone` any of the default TemplateVMs that come with Qubes 4.0. This How-To uses `Debian 9 (stretch)` template to build Cjdns and run the ProxyVM.

So `clone` the `debian-9` TemplateVM via the Qubes Manager and assign the name **cjdns-gw**. Why? The Whonix TemplateVM (whonix-gw) has the same naming, so let's keep some consistency.

Note: You might want to change the `Networking` of the `cjdns-gw` TemplateVM to `sys-whonix`.

### 2. Install required software in the TemplateVM (cjdns-gw)
The [Cjdns installation instructions for Debian jessie](https://github.com/cjdelisle/cjdns/blob/master/doc/install/debian-jessie.md) work for *stretch (Debian 9)* as well:

Launch the `cjdns-gw` TemplateVM and allow outbound network connections for 5 minutes via `Edit qube firewall rules` in the Qubes Manager.

Install the required packages to build Cjdns:
```
user@cjdns-gw:~$ sudo apt-get install nodejs git build-essential
```
### 3. Checkout and build Cjdns
This can be done in the home directory of the `user` in the `cjdns-gw` TemplateVM.
```
user@cjdns-gw:~$ cd
user@cjdns-gw:~$ pwd
/home/user
user@cjdns-gw:~$ git clone https://github.com/cjdelisle/cjdns.git
...
user@cjdns-gw$ cd cjdns
user@cjdns-gw:~/cjdns$ ./do
...
```

### 4. Install Cjdns as a system service
If the previous step completed without errors, install Cjdns as as system service (`systemd`).

While you're still in the Cjdns directory, type:
```
user@cjdns-gw:~/cjdns$ sudo cp cjdroute /usr/bin
user@cjdns-gw:~/cjdns$ sudo cp contrib/systemd/cjdns*.service /etc/systemd/system/
user@cjdns-gw:~/cjdns$ sudo systemctl enable cjdns
user@cjdns-gw:~/cjdns$ sudo systemctl start cjdns
```
Verify that Cjdns is running:
1. Check that `/etc/cjdroute.conf` was created with:
```
user@cjdns-gw:~/cjdns$ ls /etc/cjdroute.conf
/etc/cjdroute.conf
```
If your terminal says:
`stat: cannot stat ‘cjdroute.conf’: No such file or directory`
Then it doesn't exist and delete the qube/start over. Otherwise move on.

2. Check that Cjdns service is running: `sudo systemctl status cjdns`

### 5. Make Cjdns router configuration persistent
To make sure that any instances (aka Service VMs) of the Cjdns TemplateVM have their own, persistent Cjdns router configuration, we need a [bind-dir](https://www.qubes-os.org/doc/bind-dirs/). 

Create the a file `/etc/qubes-bind-dirs.d/10_cjdns.conf` by typing:
```
user@cjdns-gw:~/cjdns$ sudo mkdir /etc/qubes-bind-dirs.d
user@cjdns-gw:~/cjdns$ echo "binds+=( '/etc/cjdroute.conf' )" | sudo tee /etc/qubes-bind-dirs.d/10_cjdns.conf
```
Verify the content:
```
user@cjdns-gw:~/cjdns$ cat /etc/qubes-bind-dirs.d/10_cjdns.conf 
binds+=( '/etc/cjdroute.conf' )
```
### 6. Move Cjdns directory to /opt and shutdown the TemplateVM (cjdns-gw)
Move the whole `cjdns` directory to `/opt`, because it contains quite a few tools which might be helpful later in the ProxyVM. If we keep it in the home directory, it would only be available in the TemplateVM.
```
user@cjdns-gw:~/cjdns$ cd ..
user@cjdns-gw:~$ sudo mv cjdns /opt
```
The TemplateVM should be all set now. Shut it down via the *Qubes Manager*.

### 7. Create a ProxyVM (sys-cjdns)
Actually, *ProxyVM* is an old term from Qubes 3.2. We'll create an *AppVM* which provides networking to other VMs. (See https://github.com/tasket/Qubes-vpn-support for an explanation)

Create a new AppVM in Qubes manager with the following settings:
```
Name: sys-cjdns
Type: AppVM
Template: cjdns-gw
Networking: default (sys-firewall)
Advanced: check 'provides network'
```
### 8. Enable IPv6 forwarding for ProxyVM (sys-cjdns)
This feature is only available since Qubes 4.0 and a *must-requirement* for a Cjdns-ProxyVM. (See https://www.qubes-os.org/doc/networking/#ipv6 for details)

Launch a terminal in `dom0` and type:
```
[user@dom0 ~]$ qvm-features sys-cjdns ipv6 1
```

###  9. Launch and setup Cjdns-ProxyVM (sys-cjdns)
Launch a terminal in the `sys-cjdns` ProxyVM.

Verify that the `bind-dir` configuration worked:
```
user@sys-cjdns:~$ sudo cat /proc/mounts | grep /etc/cjdroute.conf
/dev/xvdb /etc/cjdroute.conf ext4 rw,relatime,discard,data=ordered 0 0
``` 

However, since this `cjdroute.conf` file contains the *private key* from the Cjdns-TemplateVM, we have to re-generate it for the ProxyVM. To do this, we have to stop cjdns first and unmount the `bind-dir`:
```
user@sys-cjdns:~$ sudo systemctl stop cjdns
user@sys-cjdns:~$ sudo umount /etc/cjdroute.conf
user@sys-cjdns:~$ sudo rm /etc/cjdroute.conf
user@sys-cjdns:~$ sudo systemctl start cjdns
user@sys-cjdns:~$ sudo cp /etc/cjdroute.conf /rw/bind-dirs/etc/
user@sys-cjdns:~$ sudo reboot
```

After reboot, the `cjdroute.conf` in `sys-cjdns` should have a different *privateKey* (and therefore different *publicKey* and *ipv6 address*) than the `cjdroute.conf` in the `cjdns-gw` TemplateVM.

### 10. Verify Cjdns Proxy
Now you should be able to `ping6` the Cjdns router in the ProxyVM from an AppVM. For example configure your `personal` VM to use the `sys-cjdns` VM as the network.

Next, let's find out the cjdns address of your `sys-cjdns` VM. Cjdns addresses are IPv6 addresses which always begin with `fc`. Launch a  terminal in the `sys-cjdns` VM and type:
```
user@sys-cjdns:~$ sudo ifconfig | grep -B1 "inet6 fc"
tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1304
        inet6 fc3e:c29a:0166:4c38:2243:b62f:3cb4:693f  prefixlen 8  scopeid 0x0<global>
```
In this example, you can see that Cjdns creates a `tun0` interface with the IPv6 address `fc3e:c29a:0166:4c38:2243:b62f:3cb4:693f`.

Now launch a terminal in the AppVM you wired with `sys-cjdns` (e.g. the `personal` VM) and type:
```
[user@personal ~]$ ping6 -c3 fc3e:c29a:0166:4c38:2243:b62f:3cb4:693f
PING fc3e:c29a:0166:4c38:2243:b62f:3cb4:693f(fc3e:c29a:0166:4c38:2243:b62f:3cb4:693f) 56 data bytes
64 bytes from fc3e:c29a:0166:4c38:2243:b62f:3cb4:693f: icmp_seq=1 ttl=41 time=4.85 ms
64 bytes from fc3e:c29a:0166:4c38:2243:b62f:3cb4:693f: icmp_seq=2 ttl=41 time=4.33 ms
64 bytes from fc3e:c29a:0166:4c38:2243:b62f:3cb4:693f: icmp_seq=3 ttl=41 time=5.74 ms

--- fc3e:c29a:0166:4c38:2243:b62f:3cb4:693f ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 4.334/4.975/5.743/0.587 ms
```
You should see 3 successful pings, which means the new Qubes 4.0 IPv6 feature was correctly enabled for `sys-cjdns` and is working.

### 11. Optional: Connect to other Cjdns peers in your local network
If you have other Cjdns nodes running in your local network, you can add them to `/etc/cjdroute.conf` in the `sys-cjdns` ProxyVM now. As mentioned previously Cjdns zero-configuration doesn't work with Qubes, as `sys-cjdns` is behind a NAT as well and not connected directly to your local network.

Just copy the example template from your other nodes `/etc/cjdroute.conf` that looks like:
```javascript
// my other peer: fc0d:378f:a61e:5223:6dd1:bd72:ad03:62fd
"your.external.ip.goes.here:19264": {
    "login": "default-login",
    "password":"13yj3nk85myvt5r8pb8x5140n4x4cfg",
    "publicKey":"tr459vnqfby0hrwc40ucnqbvg04snvfy1r3g9y61911t3b6hu910.k",
    "peerName":"my-other-peer"
}
```
Adjust *"your.external.ip.goes.here"* with the local IPv4 or IPv6 address of that other node and give it a meaningful *"peerName"*. Now add that snippet to `/etc/cjdroute.conf` of your `sys-cjdns` ProxyVM, precisely to the section *"interfaces" > "UDPInterface" > "connectTo"*. Be careful, this is a JSON-like syntax, so add a comma after the previous item when you add something. Else Cjdns won't start anymore. 

Now restart Cjdns service in the `sys-cjdns` VM:
```
user@sys-cjdns:~$ sudo systemctl restart cjdns
```

If everything went well and you didn't destroy the JSON syntax, Cjdns should be running again and you should now be able to `ping6` your other node from within the `personal` VM:
```
[user@personal ~]$ ping6 -c3 fc0d:378f:a61e:5223:6dd1:bd72:ad03:62fd
```

You can also check in a terminal of the `sys-cjdns` VM all the directly connected peers via the following Python script:
```
user@sys-cjdns:~$ /opt/cjdns/contrib/python/peerStats
fc0d:378f:a61e:5223:6dd1:bd72:ad03:62fd	v20	0000.0000.0000.0013	in 402436	out 357712	ESTABLISHED	dup 0 los 6 oor 0	'your-name-goes-here'
```

You don't need to add all your peers to the config. One peer is sufficient if all your other peers connect each other via the `beacon mode` (zero-configuration). You should be able to `ping6` your other peers already. However, adding a 2nd or 3rd peer in the config makes your Qubes `sys-cjdns` proxy more resilient and better connected in your local meshnet.

### 12. Optional: Connect your Cjdns-ProxyVM to Hyperboria
This step is almost identical with the previous step (connecting to local peers). The only difference is, that you add peers via their public Internet address (IPv4 or IPv6). Either you know somebody who's connected to Hyperboria already and ask them if they give you access credentials, or you may have a look at the following repository: https://github.com/hyperboria/peers

Once your `sys-cjdns` VM is connected to at least one Hyperboria peer, you should be able to access Hyperboria resources from within your AppVMs.

#### Here are a few Hyperboria websites you can test:
*Note: IPv6 addresses must be wrapped in square brackets `http://[fc::]` for a web browser to load them.*

**fc00::/8 - A graphical mapping of Hyperboria**  
`http://[fc53:dcc5:e89d:9082:4097:6622:5e82:c654]`  
  
**IPFS website**  
http://h.ipfs.io  
`http://[fc8f:dcbf:74b9:b3b9:5305:7816:89ac:53f3]`
  
**Don't Sell.Me - cloud services**  
http://mesh.dontsell.me  
`http://[fc81:7e39:ae21:1d67:e89c:9ff0:3f7e:5e5c]`  

**ansuz's website**  
http://h.transitiontech.ca/public  
`http://[fc6a:30c9:53a1:2c6b:ccbf:1261:2aef:45d3]`  

### 13. Optional: Start ProxyVM automatically with Qubes
You might want to start the Cjdns-ProxyVM automatically when Qubes starts. Just like the `sys-whonix` ProxyVM. Just go to the *Qubes Manager* and open the `Qube settings` of the `sys-cjdns` VM. Activate the checkbox `Start qube automatically on boot` in the `Basic` tab.
