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
==================================

Although setting up a VPN connection is not by itself Qubes specific, Qubes includes a number of tools that can make the client-side setup of your VPN more versatile and secure. This document is a Qubes-specific outline for choosing the type of VM to use, and shows how to prepare a ProxyVM for either NetworkManager or a set of fail-safe VPN scripts.

Please refer to your guest OS and VPN service documentation when considering the specific steps and parameters for your connection(s); The relevant documentation for the Qubes default guest OS (Fedora) is [Establishing a VPN Connection.](https://docs.fedoraproject.org/en-US/Fedora/23/html/Networking_Guide/sec-Establishing_a_VPN_Connection.html)

### NetVM

The simplest case is to set up a VPN connection using the NetworkManager service inside your NetVM. Because the NetworkManager service is already started, you are ready to set up your VPN connection. However this has some disadvantages:

-   You have to place (and probably save) your VPN credentials inside the NetVM, which is directly connected to the outside world
-   All your AppVMs which are connected to the NetVM will be connected to the VPN (by default)

### AppVM

While the NetworkManager service is not started here (for a good reason), you can configure any kind of VPN client in your AppVM as well. However this is only suggested if your VPN client has special requirements.

### ProxyVM

One of the best unique features of Qubes OS is its special type of VM called a ProxyVM. The special thing is that your AppVMs see this as a NetVM (or uplink), and your NetVMs see it as a downstream AppVM. Because of this, you can place a ProxyVM between your AppVMs and your NetVM. This is how the default sys-firewall VM functions.

Using a ProxyVM to set up a VPN client gives you the ability to:

-   Separate your VPN credentials from your NetVM.
-   Separate your VPN credentials from your AppVM data.
-   Easily control which of your AppVMs are connected to your VPN by simply setting it as a NetVM of the desired AppVM.

Set up a ProxyVM as a VPN gateway using NetworkManager
------------------------------------------------------

1.  Create a new VM, name it, click the ProxyVM radio button, and choose a color and template.

    ![Create\_New\_VM.png](/attachment/wiki/VPN/Create_New_VM.png)

2.  Add the `network-manager` service to this new VM.

    ![Settings-services.png](/attachment/wiki/VPN/Settings-services.png)

3.  Set up your VPN as described in the NetworkManager documentation linked above.

4.  Configure your AppVMs to use the new VM as a NetVM.

    ![Settings-NetVM.png](/attachment/wiki/VPN/Settings-NetVM.png)

5. Optionally, you can install some [custom icons](https://github.com/Zrubi/qubes-artwork-proxy-vpn) for your VPN


Set up a ProxyVM as a VPN gateway using iptables and CLI scripts
----------------------------------------------------------------

This method is more involved than the one above, but has anti-leak features that also make the connection _fail closed_ should it be interrupted. It has been tested with Fedora 23 and Debian 8 templates.
 
   If not using OpenVPN: These directions are specifically written for those wishing to use OpenVPN as their VPN client software. If you are trying to use different VPN client software, you may need to edit some of the options given for the script files (see specifically Step 5, below). If your choice of template VM doesn't already have OpenVPN or you want to use different VPN client software, you'll need to install the software in the template before proceeding. If you do install software, remember to disable any auto-starting service that comes with the software package: for example `sudo systemctl disable openvpn.service`.

   If using OpenVPN: If you wish to use openvpn as your VPN client software, then you're in luck! The default Fedora-23 template that comes with Qubes 3.2 already has openvpn client software installed.
    
   Text editor: You will need a text editor to enter the scripts below. A good text editor is `nano`. This can be done by entering `sudo dnf install nano` in terminal for Fedora users, and `sudo apt-get nano` for Debian users. Another text editor is `gedit`, which comes already installed in the Qubes default Fedora template.

1. Create a new VM, name it, click the ProxyVM radio button, and choose a color and template.

    ![Create\_New\_VM.png](/attachment/wiki/VPN/Create_New_VM.png)
    
    Note: Do not enable NetworkManager in the ProxyVM, as it can interfere with the scripts' DNS features. If you enabled NetworkManager or used other methods in a previous attempt, do not re-use the old ProxyVM... Create a new one according to this step.
  
2.  Set up and test the VPN client.

    First, make sure the VPN VM and its template VM are not running.
    
    Then, run a terminal CLI in the VPN VM (the ProxyVM just created). You can access terminal by right-clicking the VPN VM inside of Qubes VM Manager, selecting "Run command in VM", and typing `gnome-terminal` [ENTER]. 
    
    Once in terminal, make a new 'vpn' folder with `sudo mkdir /rw/config/vpn` and copy your VPN config files here (the example config filename used here is `openvpn-client.ovpn`). Files accompanying the main config such as *.crt and *.pem should also go here, and should not be referenced in the main config by absolute paths such as '/etc/...'.

    Notes about VPN config options: The VPN scripts here are intended to work with commonly used `tun` interfaces, whereas `tap` mode is untested. Also, the config should route all traffic through your VPN's interface after a connection is created; For openvpn the directive for this is `redirect-gateway def1`.
    
    Notes about logging into VPN: Once the steps outlined below are completed, the VPN client will not be able to prompt you for credentials when connecting to the server. If you are unable to connect to the VPN server after completing all the steps (but was able to before), make sure you have created a file containing your VPN login credentials, placed in the 'vpn' folder and are using a directive such as openvpn's `auth-user-pass <filename>`, in the script given below for `rc.local`.
    
    __Test your client configuration:__ Run the client from a terminal CLI prompt in the 'vpn' folder, preferably as root. For example:
    ```
    sudo openvpn --cd /rw/config/vpn --config openvpn-client.ovpn
    ```
    At this point you will likely need to enter in the username and password for your VPN service. In order to automate this, create a txt file containing your VPN login credentials with `sudo nano /rw/config/vpn/auth.txt`. Add your username and password for the VPN service into the first two lines of auth.txt
     ~~~
     Username
     Password
    ~~~
    Now save and exit.  If using Nano: [CTRL-X] [Y] [ENTER]
    
    Now you can test your connection (without having to enter in your login credentials) with `sudo openvpn --cd /rw/config/vpn --config openvpn-client.ovpn auth-user-pass auth.txt`
    
    Watch for status messages that indicate whether the connection is successful and test from another VPN VM terminal window with `ping` and `traceroute`. DNS may be tested at this point by replacing addresses in `/etc/resolv.conf` with ones appropriate for your VPN (although this file will not be used when setup is complete). Diagnose any connection problems using resources such as client documentation and help from your VPN service provider.
    
    Proceed to the next step when you're sure the basic VPN connection is working.

3.  Create the DNS-handling script.
    Use `sudo nano /rw/config/vpn/qubes-vpn-handler.sh` to edit and add:

    ~~~
    #!/bin/bash
    set -e
    export PATH="$PATH:/usr/sbin:/sbin"

    case "$1" in

    up)
	# To override DHCP DNS, assign DNS addresses to 'vpn_dns' env variable before calling this script;
	# Format is 'X.X.X.X  Y.Y.Y.Y [...]'
	if [[ -z "$vpn_dns" ]] ; then
		# Parses DHCP foreign_option_* vars to automatically set DNS address translation:
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
    ~~~

    Now save the script and make it executable:  
    `sudo chmod +x /rw/config/vpn/qubes-vpn-handler.sh`
    
4.  Configure client to use the DNS handling script. Using openvpn as an example, edit the config with `sudo nano /rw/config/vpn/openvpn-client.ovpn` and add these lines:

    ~~~
    script-security 2
    up 'qubes-vpn-handler.sh up'
    down 'qubes-vpn-handler.sh down'
    ~~~

    **Restart the client and test the connection again** ...this time from an AppVM!

5.  Set up iptables anti-leak rules.

    Edit the firewall script with `sudo nano /rw/config/qubes-firewall-user-script` then clear out the existing lines and add:

	~~~
	#!/bin/bash
	#    Block forwarding of connections through upstream network device
	#    (in case the vpn tunnel breaks):
	iptables -I FORWARD -o eth0 -j DROP
	iptables -I FORWARD -i eth0 -j DROP
	
	#    Block all outgoing traffic
	iptables -P OUTPUT DROP
	iptables -F OUTPUT
	iptables -I OUTPUT -o lo -j ACCEPT

	#    Add the `qvpn` group to system, if it doesn't already exist
    if ! grep -q "^qvpn:" /etc/group ; then
        groupadd -rf qvpn
        sync
    fi
    sleep 2s

	#    Allow traffic from the `qvpn` group to the uplink interface (eth0);
	#    Our VPN client will run with group `qvpn`.
    iptables -I OUTPUT -p all -o eth0 -m owner --gid-owner qvpn -j ACCEPT
    ~~~

    Now save the script and make it executable:  
    `sudo chmod +x /rw/config/qubes-firewall-user-script`

5.  Set up the VPN's autostart.

    Use `sudo nano /rw/config/rc.local` to clear out the existing lines and add:

    ~~~
    #!/bin/bash
    VPN_CLIENT='openvpn'
    VPN_OPTIONS='--cd /rw/config/vpn/ --config openvpn-client.ovpn --daemon'
    
    su - -c 'notify-send "$(hostname): Starting $VPN_CLIENT..." --icon=network-idle' user
    groupadd -rf qvpn ; sleep 2s
    sg qvpn -c "$VPN_CLIENT $VPN_OPTIONS"
    ~~~
    
    Change the `VPN_CLIENT` and `VPN_OPTIONS` variables to match your VPN software.
    
    If using an "auth.txt" file, or a similar file containing your login credentials for the VPN service, make sure to reference that file in `VPN_OPTIONS` so that your VPN service will correctly autostart with you logged in. For example, change the third line in the script given above to: `VPN_OPTIONS='--cd /rw/config/vpn/ --config openvpn-client.ovpn --auth-user-pass auth.txt --daemon'`
    
    Now save the script and make it executable:  
    `sudo chmod +x /rw/config/rc.local`
    
6. Restart the new VM! The link should then be established automatically with a popup notification to that effect.


Usage
-----

Configure your AppVMs to use the VPN VM as a NetVM...

![Settings-NetVM.png](/attachment/wiki/VPN/Settings-NetVM.png)


If you want to be able to use the [Qubes firewall](/doc/firewall), create a new FirewallVM (as a ProxyVM) and set it to use the VPN VM as its NetVM.
Then, configure AppVMs to use your new FirewallVM as their NetVM.

If you want to update your TemplateVMs through the VPN, enable the `qubes-updates-proxy` service in your new FirewallVM.
You can do this in the Services tab in Qubes VM Manager or on the command-line:

    $ qvm-service -e <name> qubes-updates-proxy

Then, configure your templates to use your new FirewallVM as their NetVM.

Creating 
-----

Troubleshooting
---------------

* Always test your basic VPN connection before adding scripts.
* Test DNS: Ping a familiar domain name from an appVM. It should print the IP address for the domain.
* For scripting: Ping external IP addresses from inside the VPN VM using `sudo sg qvpn -c 'ping ...'`, then from an appVM using just `ping ...`. Once the firewall rules are in place, you will have to use `sudo sg` to run any IP network commands in the VPN VM.
* Use `iptables -L -v` and `iptables -L -v -t nat` to check firewall rules. The latter shows the critical PR-QBS chain that enables DNS forwarding.
* If having trouble connecting after setting up autostart, make sure to check that `auth-user-pass` references a "auth.txt" file, properly filled with your loging credentials. 
