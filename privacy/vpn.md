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

Setting up a VPN connection is really not Qubes specific and is documented in your operating system documentation. The relevant documentation for the Qubes default Guest OS (Fedora) is [Establishing a VPN Connection](https://docs.fedoraproject.org/en-US/Fedora/23/html/Networking_Guide/sec-Establishing_a_VPN_Connection.html)

The Qubes specific part is to choose the right VM for the VPN client:

### NetVM

The simplest case is to set up a VPN connection using the NetworkManager service inside your NetVM. Because the NetworkManager service is already started, you are ready to set up your VPN connection. However this has some disadvantages:

-   You have to place (and probably save) your VPN credentials inside the NetVM, which is directly connected to the outside world
-   All your AppVMs which are connected to the NetVM will be connected to the VPN (by default)

### AppVM

While the NetworkManager service is not started here (for a good reason), you can configure any kind of VPN client in your AppVM as well. However this is only suggested if your VPN client has special requirements.

### ProxyVM

**WARNING:** *You need to use Qubes 3.1-rc2 (or later)! In the previous releases the NetworkManager service was not working in ProxyVMs as expected.* ([#1052](https://github.com/QubesOS/qubes-issues/issues/1052))

One of the best thing in Qubes is that you can use a special type of VM called a ProxyVM (or FirewallVM). The special thing is that your AppVMs see this as a NetVM, and your NetVMs see it as an AppVM. Because of this, you can place a ProxyVM between your AppVMs and your NetVM. This is how the default FirewallVM functions.

Using a ProxyVM to set up a VPN client gives you the ability to:

-   Separate your VPN credentials from Your NetVM
-   Separate your VPN credentials from Your AppVM data.
-   Easily control which of your AppVMs are connected to your VPN by simply setting it as a NetVM of the desired AppVM.

**To setup a ProxyVM as a VPN gateway you should:**

1.  Create a new VM and check the ProxyVM radio button.

    ![Create\_New\_VM.png](/attachment/wiki/VPN/Create_New_VM.png)

2.  Add the `network-manager` service to this new VM.

    ![Settings-services.png](/attachment/wiki/VPN/Settings-services.png)

3.  Set up your VPN as described in the NetworkManager documentation linked above.

4.  Configure your AppVMs to use the new VM as a NetVM.

    ![Settings-NetVM.png](/attachment/wiki/VPN/Settings-NetVM.png)

5. Optionally, you can install some [custom icons](https://github.com/Zrubi/qubes-artwork-proxy-vpn) for your VPN
