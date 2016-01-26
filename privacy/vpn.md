---
layout: doc
title: VPN
permalink: /doc/privacy/vpn/
redirect_from:
- /en/doc/vpn/
- /doc/VPN/
- /wiki/VPN/
---

How To make a VPN Gateway in Qubes
----------------------------------

The simplest case if you set up a VPN connection using the Network Manager inside one of your VMs. Setting up such a connection is really not Qubes specific and it is documented in Your operating system documentation. If you using the Qubes default Guest OS (Fedora): [Establishing a VPN Connection](https://docs.fedoraproject.org/en-US/Fedora/23/html/Networking_Guide/sec-Establishing_a_VPN_Connection.html)

The Qubes specific part is to choose the right VM for the VPN client:

### NetVM

The simplest case is to set up a VPN connection using the Network Manager inside your NetVM. Because the NetworkManager already started you are ready to set up your VPN connection. However this has some disadvantages:

-   You have to place (and probably save) Your VPN credentials inside the NetVM which is directly connected to the outside world
-   All your AppVMs which are connected to the NetVM will be connected to the VPN (by default)

### AppVM

While the Network Manager is not started here (for a good reason), you can configure any kind of VPN client in your AppVM as well, however it is only suggested if you have to use a special VPN client.

### ProxyVM

**WARNING:** *You need to use Qubes 3.1-rc2 (or later)! In the previous releases the NetworkManager was not working in ProxyVMs as expected.* ([#1052](https://github.com/QubesOS/qubes-issues/issues/1052))

One of the best thing in Qubes that you can use a special type of VMs called ProxyVM (or FirewallVM). The special thing is that your AppVMs see this as a NetVM, and the NetVMs see it as an AppVM. Because of that You can place a ProxyVM between your AppVMs and Your NetVM. This is how the default firewall VM is working.

Using a ProxyVM to set up a VPN client gives you the ability to:

-   Separate your VPN credentials from Your NetVM
-   Separate your VPN credentials from Your AppVM data.
-   Easily control which of your AppVMs are connected to your VPN by simply setting it as a NetVM of the desired AppVM.

**To setup a ProxyVM as a VPN gateway you should:**

1.  Create a new VM and check the ProxyVM radio button.

    ![Create\_New\_VM.png](/attachment/wiki/VPN/Create_New_VM.png)

2.  Add the `network-manager` service to this new VM.

    ![Settings-services.png](/attachment/wiki/VPN/Settings-services.png)

3.  Wet up your VPN as described in the Network Manager documentation linked above.

4.  Connect your AppVMs to use the new VM as a NetVM.

    ![Settings-NetVM.png](/attachment/wiki/VPN/Settings-NetVM.png)

5. Optionaly you can install some [custom icons](https://github.com/Zrubi/qubes-artwork-proxy-vpn) for your VPN
