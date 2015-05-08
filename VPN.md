---
layout: doc
title: VPN
permalink: /doc/VPN/
redirect_from: /wiki/VPN/
---

How To make a VPN Gateway in Qubes
----------------------------------

The simplest case if you set up a VPN connection using the Network Manager inside one of your VMs. Setting up such a connection is really not Qubes specific and it is documented in Your Operating system documentation. If you using the Qubes default Guest OS (Fedora): [Establishing a VPN Connection](http://docs.fedoraproject.org/en-US/Fedora/18/html/System_Administrators_Guide/sec-Establishing_a_VPN_Connection.html)

The Qubes specific part is choose the right VM for the VPN client:

### NetVM

The simplest case if you set up a VPN connection using the Network Manager inside your NetVM. Because the [NetworkManager?](/wiki/NetworkManager) already started you are ready to set up your VPN connection. However this has some disadvantages:

-   You have to place (and probably save) Your VPN credentials inside the NetVM wich is directly connected to the outside world
-   All your AppVMs wich are connected to the NetVM will be connected to the VPN (by default)

### AppVM

While the Network Manager is not started here (for a good reason) You can configure any kind of VPN client in your AppVM as well, however it is only suggested if you have to use a special VPN client.

### ProxyVM

**WARNING:** *Currently the [NetworkManager?](/wiki/NetworkManager) is not working in ProxyVMs as expected. Actually it will mess up the routing table and because of that your packets may not be routed to the VPN tunnel. - This surely occurs if your VPN wants to be the default gateway.*

One of the best thing in Qubes that you can use a special type of VMs called ProxyVM (or FirewallVM). The special thing is that your AppVMs see this as a NetVM, and the NetVMs see it as an AppVM. Because of that You can place a ProxyVM between your AppVMs and Your NetVM. This is how the default firewall VM is working.

Using a ProxyVM to set up a VPN client will gives you the ability to:

-   Separate your VPN credentials from Your AppVM data.
-   You can easily control which of your AppVMs are connected to your VPN by simply set it as a NetVM of the desired AppVM.

**To setup a ProxyVM as a VPN gateway you should:**

1.  check (`rpm -q  qubes-core-vm`) if you have the package **qubes-core-vm** version **2.1.36** (or later)
2.  create a new VM and check the ProxyVM radio button

![Create\_New\_VM.png](/attachment/wiki/VPN/Create_New_VM.png)

1.  add the network-manager service to this new VM

![Settings-services.png](/attachment/wiki/VPN/Settings-services.png)

1.  set up Your VPN as described in the Network Manager documentation linked above.

1.  connect your AppVMs to use the new VM as a NetVM.

[![Settings-NetVM.png](/attachment/wiki/VPN/Settings-NetVM.png)
