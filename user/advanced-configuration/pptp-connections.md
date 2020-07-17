---
layout: doc
title: PPTP Connections
permalink: /doc/pptp-connections/
---

# How to allow PPTP Connections in Qubes

Point to Point Tunneling Protocol (PPTP), an protocol initiated by Microsoft is used to establish connections to PPTP based Virtual Private Networks (VPN). In order to establish PPTP connections, you will need to download the pptp-linux package, preferably from your linux version or download the PPTP client, both of which will run a tunnel from your local system to connect to any PPTP-based VPN.

**Warning: The PPTP protocol is inherently insecure and flawed. See [PPTP protocol security](http://poptop.sourceforge.net/dox/protocol-security.phtml).**

## Configuring Firewall settings

To allow PPTP connections, you will need to follow the following steps:
1. Configure your ProxyVM using iptables on the netvm upstream:
       - On ProxyVM, run the following command -

          $ iptables -I INPUT -p 47 -s <vpn server> -j ACCEPT


2. Enable inbound routing from the internet to the VPN ProxyVM:
       - Check that your ProxyVM is attached directly to sys-net.
       - Allow INBOUND protocol 47 by running the following commands on sys-net:

           $ modprobe ip_conntrack_pptp
           $ modprobe ip_nat_pptp
           $ iptables -I FORWARD -p 47 -s <vpn server> -j ACCEPT   

3. Zero the iptables counters, (using -Z), then start the VPN.

You should now see the counters incrementing both in sys-net and on the VPN proxy. If the connection fails, look to see if any DROP rules are being triggered.

To automatically set up the necessary rules, place them in `rc.local` and/or qubes-firewall-script at `/rw/config`.                                                             If you don't routinely use the VPN connection, you may alternatively put them in a simple script and trigger the rules when you want to start the VPN.                      
If you don't routinely use the VPN connection, you may alternatively put them in a simple script and trigger the rules when you want to start the VPN.

Note: By default PPTP connections use TCP port 1723. To log the traffic, put in a rule by running the following command:

          $ iptables -I FORWARD -p tcp --dport 1723 -j LOG

## Installation:

**NOTE: It is strongly recommended to use a ProxyVM for downloading and setting up the PPTP VPN.**

### Pre-installation Checks:

- Check your Linux kernel version.
   If it is below 2.6.15, upgrade it to the most recent version to add MPPE support.
- Check if your Linux kernel has the pptp_mppe module installed. If the module is missing, rebuild your Linux kernel to add MPPE support and enable the CONFIG_PPE_MPPE kernel build
option.

### Obtaining your credentials:

To configure your PPTP VPN, you will need to obtain the following details from your PPTP server administrator:

- Username
- Password
- The IP address or host name of the server
- The domain name used for authentication
- The name you wish to use to refer to the tunnel

### Installation Steps:

1. Follow the steps outlined in the Qubes [VPN documentation](https://www.qubes-os.org/doc/vpn/#set-up-a-proxyvm-as-a-vpn-gateway-using-iptables-and-cli-scripts) to set up a PPTP VPN by installing the `pptp-linux` package. Replace the values used for Username and Password with your credentials.

2. Alternatively, you can also install a [PPTP client](http://pptpclient.sourceforge.net/).

For Qubes guest OS, follow the instructions listed below to install and set up the PPTP client:  

#### Fedora (Qubes default guest OS) -

1. Run the following commands:

    `$ rpm -Uvh http://pptpclient.sourceforge.net/yum/stable/fc6/pptp-release-current.noarch.rpm`

    `$ yum --enablerepo=pptp-stable install pptpconfig`

    You can now configure the PPTP client using the Network Manager[^networkmanager].                                
    Alternatively, you can also configure by hand[^configbyhand].

#### Archlinux -

1. Download the pptp client [here.](https://www.archlinux.org/packages/?name=pptpclient) Run the pptpsetup tool as root with the following command (Replace the values used with your credentials):

    `$ pptpsetup --create my_tunnel --server vpn.example.com --username alice --password foo --encrypt`

2. Run the following command as root to check for successful configuration. The `pon` command should not terminate if the configuration was successful:

    `$ pon <my_tunnel> debug dump logfd 2 nodetach`

     Alternatively, you can also configure by hand[^configbyhand].

#### Debian -

1. Run the following command to install and auto-configure the PPTP client:

    `$ apt install pptp-linux`

2. For the KDE desktop, run the folowing command to install the Plasma  Network  Management widget which supports PPTP:

    `$ apt install plasma-nm`

3. For the GNOME or MATE desktop, run the following command to install the Network  Manager PPTP plugin for GNOME:

    `$ apt install network-manager-pptpgnome`

    You can now configure the PPTP client using the Network Manager[^networkmanager].                                
    Alternatively, you can also configure by hand[^configbyhand].

#### Ubuntu -

1. Run the following command:

    `$ apt-get install pptp-linux`

2. Add the following lines to the source list file '/etc/apt/sources.list' under #user-name's PPTP GUI packaging -

   `deb http://quozl.netrek.org/pptp/pptpconfig ./`

3. Update the list of packages. TO do this, run:

    `$ apt-get update `

4. Install the PPTP GUI client (You may get a warning stating that the package cannot be authenticated. Choose to continue the installation anyway):

    `$ apt-get install pptpconfig `

    You can now configure the PPTP client using the Network Manager[^networkmanager].                                                                                         
    Alternatively, you can also configure by hand[^configbyhand].

#### Whonix -

1. Run the following command:

   `$ apt-get install pptp-linux`

    You can now configure the PPTP client using the Network Manager[^networkmanager].                                                                                        
    Alternatively, you can also configure by hand[^configbyhand].

2. VPN Firewall -
To allow PPTP connections in the Qubes guest OS (Whonix), another fool-proof way is to install a VPN Firewall. In case a VPN breaks down, data traffic is sent without the VPN, thus causing potential data leaks.
A VPN firewall simply makes sure that your VPN is actually working, thus ensuring the safe transfer of your data.

- Enable netfilter-persistent Qubes qvm-service:

`Qubes VM Manager → right click on VM → services → enter (without the single quotes) 'netfilter-persistent' → click on + → OK`

- Then, follow these [steps](https://www.whonix.org/wiki/VPN-Firewall#VPN_Setup) to set up a VPN firewall.
- Follow these [steps](https://www.whonix.org/wiki/VPN-Firewall#Test_VPN-Firewall) to check if your VPN firewall has installed successfully.
- Refer to the [whonix wiki](https://www.whonix.org/wiki/VPN-Firewall) for troubleshooting.

**Tips:**

- To enable forwarding for VM's:

1. Create a new directory `vpn-firewall.d` inside your config directory.
2. Create a new file `50_user.conf` at `/rw/config/vpn-firewall.d/50_user.conf` and add `FORWARDING=true`.

- To allow the VPN firewall to start on boot, run:

1. Create a new 'netfilter-persistent' status file:

     `$ sudo touch /run/qubes-service/netfilter-persistent`

2. Restart the status file:

     `$ sudo service netfilter-persistent restart`

3. Check the netfilter-persistent status:

     `$ sudo service netfilter-persistent status`


#### CentOS -

1. Run the following command to install the PPTP client:

   `$ yum -y pptp-linux`

    You can now configure the PPTP client using the Network Manager[^networkmanager].                                                                                      
    Alternatively, you can also configure by hand[^configbyhand].

2.  Alternatively, you may also set up your CentOS box as a PPTP client:

    - Run the following command:

      `$ yum -y pptp`

    - Add the following line to the `/etc/ppp/chap-secrets` file (Replace username and password with your  personal credentials):
     `username PPTP password`

    - Create a profile file (referred to as `myVPNfile` here) at the following  path: `/etc/ppp/peers/myVPNfile`.
    - Test  the connection with:

      `$ pppd call myVPN`

    - By default, ppp0 connections do not use any specific route. If you do not wish to add any specific routes, you may skip  this step.  To add/edit default routes, you may run:

      `$ route add default dev ppp0`

      To start the PPTP connection on boot, add `pppd call myVPNfile` in the rc.local file.

**You should now be able to connect and route PPTP connections inside your ProxyVM.**


#### Footnotes

[^networkmanager]: Configuring the PPTP client using Network Manager
      - In the Network widget, go to `VPN connections > Add a VPN connection > Point-to-Point Tunneling Protocol(PPTP) > Create`
      - Choose a name for the connection.
      - Set the `Gateway` to your IP address or host name.
      - Input your username and password.
      - Save your choices.
      - Start the new connection.

[^configbyhand]: Configuring the PPTP client by hand:
      - Create or edit the `/etc/ppp/options` file to include the following options - `lock`, `noauth`, `nobsdcomp` and `nodeflate`. This will allow you to set security options for your VPN connection.
      - Create or edit the `/etc/ppp/chap-secrets` file. Replace the values of the `USERNAME` and `PASSWORD` with your credentials. If your password contains any special characters, quote them.
         Make sure to only allow root to have access to this file as it will contain your password in plain text. The original format of the file is as follows:

         ```sh
         /etc/ppp/chap-secrets

         DOMAIN\\USERNAME PPTP PASSWORD
         ```
      - Create a `/etc/ppp/peers/$TUNNEL` file. This will allow you to name your <TUNNEL> and configure it. Replace the DOMAIN, USERNAME and TUNNEL values with your credentials and the name you wish to use for your tunnel.
      - Omit `DOMAIN` if your connection does not require a domain name.
      - You may also remove `require-mppe-128` from this file if you do not require MPPE support.

         ```sh
          /etc/ppp/peers/TUNNEL

          pty "pptp <SERVER> --nolaunchpppd"
          name DOMAIN\\USERNAME
          remotename PPTP
          require-mppe-128
          file /etc/ppp/options
          ipparam TUNNEL
         ```
      - Start the tunnel by running the following command (This will also allow you to see a crash log and diagnose any failures that might occur):

         `$ pon <TUNNEL> debug dump logfd 2 nodetach`

      - Stop the tunnel by running the following command:

         `$ poff <TUNNEL>`
