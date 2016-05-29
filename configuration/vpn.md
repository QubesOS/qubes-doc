---
layout: doc
title: VPN
permalink: /doc/vpn/
redirect_from:
- /doc/privacy/vpn/
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

#### Setup a ProxyVM as a VPN gateway

**Using NetworkManager**

1.  Create a new VM and check the ProxyVM radio button.

    ![Create\_New\_VM.png](/attachment/wiki/VPN/Create_New_VM.png)

2.  Add the `network-manager` service to this new VM.

    ![Settings-services.png](/attachment/wiki/VPN/Settings-services.png)

3.  Set up your VPN as described in the NetworkManager documentation linked above.

4.  Configure your AppVMs to use the new VM as a NetVM.

    ![Settings-NetVM.png](/attachment/wiki/VPN/Settings-NetVM.png)

5. Optionally, you can install some [custom icons](https://github.com/Zrubi/qubes-artwork-proxy-vpn) for your VPN

**Using iptables and openvpn**

You need an openvpn server and a DNS server accessible through the vpn (use one from your vpn provider / a public one).

1. Create a new VM and check the ProxyVM radio button.

    ![Create\_New\_VM.png](/attachment/wiki/VPN/Create_New_VM.png)

2. Setup openvpn:   
    Copy your openvpn config file to `/home/user/vpn.cfg`.

    It should have one line starting with `dev` and one starting with `proto`.
    The first describes the connection type (`tun` or `tap`) and the second the used protocol (`tcp` or `udp`).
    Depending on your connection type, openvpn will create a new network device (probably `tap0` or `tun0`).

    It also contains a line `remote X.X.X.X 1194`, where `X.X.X.X` is the ip of your openvpn server.

    If it does not contain a line `redirect-gateway def1`, add it.  
    This will route all traffic through your vpn's network device, after a connection was created.
    If the connection breaks down all traffic will be routed through the original network device (we will stop this with iptables).

    If your vpn config file contains `auth-user-pass`, change it to `auth-user-pass /home/user/auth.txt` and create a file `/home/user/auth.txt` containing the user name in the first line and the password in the second.  
    This will enable the vpn to login without requiring you to enter your username and password.
    If a different authentication method is used, set it up to require no user input.  
    The vpn should now start by calling `sudo openvpn --config /home/user/vpn.cfg` and require no additional user input.  

    In the following, we use the following placeholder:  
    `$DEV`  For the device created for the connection.  
    `$PROT` For the protocol used for connection  
    `$SVR`  For the openvpn server's ip.  
    `$DNS`  For the dns server's ip.  


3.  Setup iptables:  
    Edit `/rw/config/qubes-firewall-user-script` and add:

    `iptables -P OUTPUT DROP`  
    This blocks all outgoing traffic, if not specified otherwise.
    
    `iptables -I OUTPUT -o $DEV -j ACCEPT`  
    This allows the local system to connect through the vpn (you dont need this).
    
    `iptables -I OUTPUT -o eth0 -d $SVR -p $PROT --dport 1194 -j ACCEPT`  
    This allows your system to connect to the vpn server with the protocol `$PROT` under the port 1194.
    
    `iptables -I OUTPUT -o lo -j ACCEPT`  
    This allows connections from the system to the system.

    `iptables -I FORWARD -o eth0 -j DROP`  
    `iptables -I FORWARD -i eth0 -j DROP`  
    This blocks forwarding of connections through your plain network device (in case the vpn tunnel breaks).

    `iptables -t nat -I PR-QBS -p udp --dport 53 -j DNAT --to-destination $DNS`  
    `iptables -t nat -I PR-QBS -p tcp --dport 53 -j DNAT --to-destination $DNS`  
    This will rewrite the DNS destination, and the traffic will be routed down the vpn tunnel. (to prevent DNS leaks)

    Now save `/rw/config/qubes-firewall-user-script` and make it executable:  
    `sudo chmod +x /rw/config/qubes-firewall-user-script`
    
4.  Setup the vpn's autostart:  
   Edit to `/rw/config/rc.local`, make it executable  (`sudo chmod +x /rw/config/rc.local`) and add:  

        ln -s /home/user/vpn.cfg /etc/openvpn/vpn.conf;  
        systemctl --no-block start openvpn@vpn.service;

5.  Configure your AppVMs to use the new VM as a NetVM.

    ![Settings-NetVM.png](/attachment/wiki/VPN/Settings-NetVM.png)

6. Optionally, you can install some [custom icons](https://github.com/Zrubi/qubes-artwork-proxy-vpn) for your VPN
