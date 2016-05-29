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

### sys-net

The simplest case is to set up a VPN connection using the NetworkManager service inside sys-net. Because the NetworkManager service is already started, you are ready to set up your VPN connection. However this has some disadvantages:

-   You have to place (and probably save) your VPN credentials inside the sys-net qube, which is directly connected to the outside world
-   All your qubes which are connected to sys-net will be connected to the VPN (by default)

### ordinary qube

While the NetworkManager service is not started here (for a good reason), you can configure any kind of VPN client in a qube as well. However this is only suggested if your VPN client has special requirements.

### ProxyVM

You can also use a type of VM called a ProxyVM [needs Qubes 3.1-rc2 (or later)](https://github.com/QubesOS/qubes-issues/issues/1052). You can place a ProxyVM between your qubes and sys-net, (like the default FirewallVM). We recommend using a dedicated qube for this purpose.

Using a ProxyVM to set up a VPN client gives you the ability to:

-   Separate your VPN credentials from Your NetVM
-   Separate your VPN credentials from your other qubes.
-   Easily control which of your qubes are connected to the VP. You do this by setting the Proxy as the NetVM of the desired qube.

#### To setup a ProxyVM as a VPN gateway:

1.  Create a new qube and check the ProxyVM radio button.

    ![Create\_New\_VM.png](/attachment/wiki/VPN/Create_New_VM.png)

2.  Add the `network-manager` service to this new qube.

    ![Settings-services.png](/attachment/wiki/VPN/Settings-services.png)

3.  Set up your VPN as described in the NetworkManager documentation linked above.



**This configuration will not guarantee that the vpn fails closed and that there will be no leakage though clearnet.**
See the discussion [here](https://github.com/QubesOS/qubes-issues/issues/1941).

You can achieve **this** by setting up the VPN Proxy like this:

(These instructions refer to openvpn, but are equally applicable to any VPN.)

No outbound traffic is allowed from the ProxyVM other than the vpn control connection, and all traffic is forwarded down the vpn tunnel.

These instructions use the following settings - adjust accordingly to match your set-up.
- Remote server at X.X.X.X, with openvpn udp port 1194. (You need to have IP address for remote server.)
- DNS server provided by the VPN provider, or reachable through the VPN. IP address Y.Y.Y.Y
- Openvpn configured with tun0, remote 10.9.0.1, client 10.9.0.2

1. Set up openvpn on the proxyVM to connect to the remote server.
2. Edit /rw/config/rc.local to delete the default gateway and add a static route to X.X.X.X via dev eth0.

        sudo ip route delete default
        sudo ip route add X.X.X.X/32 via 10.9.0.2
3. Add the following iptables rules:

        iptables -P OUTPUT DROP
        iptables -F OUTPUT
        iptables -I OUTPUT -o lo -j ACCEPT
        iptables -A OUTPUT -o eth0 -d X.X.X.X -p udp --dport 1194
        iptables -A OUTPUT -o tun0 -j ACCEPT
        iptables -I FORWARD 1 -o eth0 -j DROP
        iptables -I FORWARD 2 -i eth0 -j DROP

  The 2nd rule restricts outbound eth0 to the openvpn server and vpn port.

  The 3rd allows all traffic down the tunnel.

  The policy is to drop outbound traffic.
  
4. Add the following rules in the nat table:

        iptables -t nat -I PR-QBS -p udp --dport 53 -j DNAT --to-destination Y.Y.Y.Y:53
        iptables -t nat -I PR-QBS -p tcp --dport 53 -j DNAT --to-destination Y.Y.Y.Y:53

5. Save the rc.local file and make it executable.

        chmod +x /rw/config/rc.local

6. Add the *same* rules as in 3 and 4 above to /rw/config/qubes-user-firewall-script, and make *that* file executable.
  
    This is needed because when you add a qube downstream of the ProxyVM the default firewall rules for INPUT and OUTPUT chains will be reinstated.
7. Either use *redirect-gateway def1* in the openvpn client config file, or manually add the gateway when the tunnel comes up:

        sudo ip route add default via 10.9.0.2 dev tun0 proto static


If the tunnel drops the gateway route disappears, so there is no leakage. 

Rule 2 in the OUTPUT chain blocks any traffic except to the openvpn port.

#### Using the VPN Proxy

1. Start the ProxyVM and confirm that routing and iptables are set up correctly.

2. Configure a qube to use the VPN Proxy as a NetVM.

    ![Settings-NetVM.png](/attachment/wiki/VPN/Settings-NetVM.png)
    
    To stop using the VPN simply move the qube to another NetV, or set netvm to None.
    
    Using a ProxyVM in this way, any firewall rules you have configured for a qube will remain in place whether the qube is connected to the VPN or not.

3. Optionally, you can install some [custom icons](https://github.com/Zrubi/qubes-artwork-proxy-vpn) in the VPN Proxy
4. You *can* set up DNS access in the VPN Proxy if absolutely necessary. Read the discussion [here](https://github.com/QubesOS/qubes-issues/issues/1941).
