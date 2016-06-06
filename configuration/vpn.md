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

One of the best thing in Qubes is that you can use a special type of VM called a ProxyVM (or FirewallVM). The special thing is that your AppVMs see this as a NetVM, and your NetVMs see it as an AppVM. Because of this, you can place a ProxyVM between your AppVMs and your NetVM. This is how the default FirewallVM functions.

Using a ProxyVM to set up a VPN client gives you the ability to:

-   Separate your VPN credentials from Your NetVM
-   Separate your VPN credentials from Your AppVM data.
-   Easily control which of your AppVMs are connected to your VPN by simply setting it as a NetVM of the desired AppVM.

#### Setup a ProxyVM as a VPN gateway...

#### Using NetworkManager

**WARNING:** *You need to use Qubes 3.1-rc2 (or later)! In the previous releases the NetworkManager service was not working in ProxyVMs as expected.* ([#1052](https://github.com/QubesOS/qubes-issues/issues/1052))


1.  Create a new VM and check the ProxyVM radio button.

    ![Create\_New\_VM.png](/attachment/wiki/VPN/Create_New_VM.png)

2.  Add the `network-manager` service to this new VM.

    ![Settings-services.png](/attachment/wiki/VPN/Settings-services.png)

3.  Set up your VPN as described in the NetworkManager documentation linked above.

4.  Configure your AppVMs to use the new VM as a NetVM.

    ![Settings-NetVM.png](/attachment/wiki/VPN/Settings-NetVM.png)

5. Optionally, you can install some [custom icons](https://github.com/Zrubi/qubes-artwork-proxy-vpn) for your VPN

#### Using iptables and openvpn

1. Create a new VM and check the ProxyVM radio button.

    ![Create\_New\_VM.png](/attachment/wiki/VPN/Create_New_VM.png)
    
    If your choice of template VM doesn't already have the `openvpn` package, you'll need to install it in the template first. You may also need to `systemctl disable` any openvpn service that comes with the package if you follow the instructions for autostart below.

2. Setup openvpn:   
    Copy your openvpn config files to `/rw/config/openvpn/` folder. The example main config file is `openvpn-client.ovpn`.

    It should have one line that reads `dev tun`.

    If it does not contain a line `redirect-gateway def1` you may wish to add it. This will route all traffic through your vpn's network device after a connection is created. However, many VPN services will push this instruction to your client automatically -- having a line that says `client` or `pull` in your openvpn config instructs your client to use parameters specified by the VPN server.
    
    NOTE: If the connection breaks down all traffic will by default be routed through the upstream network device eth0 (we will stop this with iptables in step 3).

    Also add the following to accomodate a DNS script:
    
    ```
    script-security 2
    up 'qubes-vpn-handler.sh up'
    down 'qubes-vpn-handler.sh down'
    ```

3.  Setup iptables.
    Edit the firewall script with `sudo nano /rw/config/qubes-firewall-user-script` and add:

    ```
    #!/bin/bash
    #    First, block all outgoing traffic
	iptables -P OUTPUT DROP
    iptables -F OUTPUT

	#    Add the `qvpn` group to system, if it doesn't already exist
    if ! grep -q "^qvpn:" /etc/group ; then
        groupadd -rf qvpn
        sync
    fi
    sleep 2s

	#    Allow traffic from the `qvpn` group to the uplink interface (eth0);
	#    Our openvpn will run as group `qvpn`.
    iptables -A OUTPUT -p all -o eth0 -m owner --gid-owner qvpn \
    -m state --state NEW,ESTABLISHED -j ACCEPT

	#    Allow internal system connections:
    iptables -I OUTPUT -o lo -j ACCEPT

	#    Block forwarding of connections through upstream network device
	#    (in case the vpn tunnel breaks):
    iptables -I FORWARD -o eth0 -j DROP  
    iptables -I FORWARD -i eth0 -j DROP
    ```

    Now save `/rw/config/qubes-firewall-user-script` and make it executable:  
    `sudo chmod +x /rw/config/qubes-firewall-user-script`

4.  Create the DNS-handling script.
    Use `sudo nano /rw/config/openvpn/qubes-vpn-handler.sh` to edit and add:

    ```
    #!/bin/bash
    set -e
    export PATH="$PATH:/usr/sbin:/sbin"

    case "$1" in

    up)
    # To override DHCP DNS, assign static DNS addresses with 'setenv vpn_dns' in openvpn config;
	# Format is 'X.X.X.X  Y.Y.Y.Y [...]' with quotes.
	    if [[ -z "$vpn_dns" ]] ; then
		    # Parses DHCP options from openvpn to set DNS address translation:
    		for optionname in ${!foreign_option_*} ; do
	    		option="${!optionname}"
		    	unset fops; fops=($option)
			    if [ ${fops[1]} == "DNS" ] ; then vpn_dns="$vpn_dns ${fops[2]}" ; fi
    		done
	    fi

    	iptables -t nat -F PR-QBS
	    if [[ -n "$vpn_dns" ]] ; then
    		# Set DNS address translation in firewall:
	    	for addr in $vpn_dns; do
		    	iptables -t nat -A PR-QBS -i vif+ -p udp --dport 53 -j DNAT --to $addr
			    iptables -t nat -A PR-QBS -i vif+ -p tcp --dport 53 -j DNAT --to $addr
    		done
	    	su - -c 'notify-send "$(hostname): LINK IS UP." --icon=network-idle' user
    	else
	    	su - -c 'notify-send "$(hostname): LINK UP, NO DNS!" --icon=dialog-error' user
    	fi

	    ;;
    down)
	    su - -c 'notify-send "$(hostname): LINK IS DOWN !" --icon=dialog-error' user
    	;;
    esac
    ```

    Now save the script and make it executable:  
    `sudo chmod +x /rw/config/openvpn/qubes-vpn-handler.sh`
    
5.  Setup the VPN's autostart:  
    Use `sudo nano /rw/config/rc.local` to edit and add:  

    ```
    #!/bin/bash
    groupadd -rf qvpn ; sleep 2s
    sg qvpn -c 'openvpn --cd /rw/config/openvpn/ --config openvpn-client.ovpn \
    --daemon --writepid /var/run/openvpn/openvpn-client.pid'
    ```

    Now save the script and make it executable:  
    `sudo chmod +x /rw/config/rc.local`
    
6. Restart the new VM!

7. Configure your AppVMs to use the new VM as a NetVM.

    ![Settings-NetVM.png](/attachment/wiki/VPN/Settings-NetVM.png)

8. Optionally, you can install some [custom icons](https://github.com/Zrubi/qubes-artwork-proxy-vpn) for your VPN
