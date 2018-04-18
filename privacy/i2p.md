---
layout: doc
title: transparent-i2p-proxyvm
permalink: /doc/i2p/
---

# I2P #
The Invisible Internet Project[I2P] is an anonymising peer-to-peer network that enables access to hidden I2P services similar to [Tor Hidden Services][hidden-servies].
Though there are outproxies (to access the clearnet), they are rare and the I2P-network isn't built to be used as anonymising network, but much rather an anonymity-by-default secondary network.

# Transparent ProxyVM #
The currently available I2P-software is built to provide a simple http-proxy to route trafic through the network.
This creates problems with software that can't handle proxies or handles them badly.
A transparent proxy allows us to take all trafic and funnle it through the I2P-network to prevent information leakage.  
Furthermore, a transparent proxy allows us to handle traffic to the I2P-network while also handling tor-traffic.

# Theory of operation #
DNS requests from any appVM routed through the I2P-proxyVM are intercepted and answered with a localnet-IP if the domain ends in `.i2p`, otherwise the tor-dns-service is requested.
Any http requests to the localnet-IP again is intercepted and routed to tinyproxy, which repackages the requests into proxy-requests and sends them to the local I2P-server.
All other tcp-requests are routed through TOR.

# Tor #
Torifying traffic allows access to tor hidden nodes.
Assuming you want to access all kind of hidden services, not just the I2P network, it's a good idea to handle tor traffic parrell to I2P

# DISCLAIMER #
Assume I have no idea what I'm doing.
The result of this guide should be seen more adding access to I2P Hidden Services more than protecting your privacy with the I2P network.

## Quick Note on I2P-Over-Tor ##
There is an excellent guide on how to use [I2P over TOR via whonix][whonix-I2P].
However, this adds load to the tor-network.
Since the main purpose of this guide is to access the I2P-network, the performance cost overshadowed the security benifits.

## Qubes 3.2 ##
### TemplateVM setup ###
This guide builds a proxyVM based on a Debian template.

* **(Optional)** If you want to use a seperate vm template for your I2P-proxyVM, clone your Debian template: (run in dom0)*

    qvm-clone debian-8 debian-8-gate

### Install the necessarry tools in the templateVM ###
I2P install instructions can be found [here][i2p-debian-instructions].
This guide assumes debian-8, other versions please reference the according instructions.
TOR can be installed from default debian-repos.
tinyproxy and dnsmasq can be installed from debian-repos, but are already installed by default in qubes' debian-8.

1. Add the repo-key for I2P's Debian repository to apt:
  Download:

      wget https://geti2p.net/_static/i2p-debian-repo.key.asc

  Confirm fingerprint:

      gpg --with-fingerprint i2p-debian-repo.key.asc

  (this needs no keyring, so qubes-gpg-client is unnecessarry)
  Command should yield:

      pub  4096R/5BCF1346 2013-10-10 I2P Debian Package Repository <killyourtv@i2pmail.org>
          Key fingerprint = 7840 E761 0F28 B904 7535  49D7 67EC E560 5BCF 1346

  Add key to apt:

      sudo apt-key add i2p-debian-repo.key.asc
      rm i2p-debian-repo.key.asc


2. Add repo to your sources via or nano:

      nano /etc/apt/sources.lists.d/i2p.list

  content:

      deb https://deb.i2p2.de/ jessie main
      deb-src https://deb.i2p2.de/ jessie main

3. Install I2P, tor, tinyproxy and dnsmasq:

      sudo apt-get update
      sudo apt-get install i2p i2p-keyring tinyproxy dnsmasq-base


4. Configure I2P service:
  Generally speaking, you don't want I2P to start in every VM since it will try to open up connections with other pears and keep them alive. This will add network load and, if traffic is monitored, makes your traffic look more suspicious. So disabeling I2P globally is a good idea!

  There are two ways to turn it on again; using a qubes-service or using `/rw/config/rc.local`.
  If you want to use I2P exclusively in the gate, I recomand startup-scripts.  
  Otherwise create a qubes-service in order to control the service from dom0's VM-configuration.
  To disable I2P generally, in the templateVM run: (needed for both ways)

      sudo systemctl disable i2p


  To enable I2P in one specific VM, add the following line to its `/rw/config/rc.local` script:

      sudo systemctl start i2p


  To create a qubes-service controlling i2p, in the templateVM create a similarly named service:

      sudo nano /etc/systemd/system/i2p.service

  File content:

      .include /lib/systemd/system/i2p.service
      [Unit]
      ConditionPathExists=/var/run/qubes-service/i2p

  Lastly, configure I2P to start automatically:

      sudo systemctl enable i2p

  This will try to start the service in every VM, but fail to do so since the condition of an existing `/var/run/qubes-service/i2p` won't be met unless you configure a qubes-service.

  To enable the i2p-service, open VM-settings in the Qubes VM Manager.
  Switch to tab `Services`. Write `i2p` and click the green plus.  

### Configure everything! ###

*  I2P config
  Sadly, no config can be passed to the I2P-command, so the easyest way to configure I2P is to edit the config-files in the templateVM.

  If you do not want to do that but rather have VM specific configs, save a copy of your config in `/rw/config` and copy them back to their designated folders on startup:

      sudo cp /usr/share/i2p/clients.config /rw/config

  Add the following lines to your `/rw/config/rc.local` script:

      cp /rw/config/clients.config /usr/share/i2p/clients.config
      cp /rw/config/clients.config /var/lib/i2p/i2p-config/clients.config

  (For some reason, sometimes one file is used and sometimes the other, I have not figured out why.)

  To allow the i2p-console to be reachable from another VM, in your config (`/usr/share/i2p/clients.config` in templateVM or `/rw/config/clients.config` in appVM/proxyVM) change the following two lines:

      clientApp.0.args=7657 127.0.0.1 ./webapps/
      [...]
      #clientApp.0.args=7657 0.0.0.0 ./webapps/

  to:

      #clientApp.0.args=7657 127.0.0.1 ./webapps/
      [...]
      clientApp.0.args=7657 0.0.0.0 ./webapps/

  If you change the config in your templateVM, don't forget to copy it over the second config-file:

      sudo cp /usr/share/i2p/clients.config /var/lib/i2p/i2p-config/clients.config


* tinyproxy config
  In the proxyVM, copy the default config:

      sudo cp /etc/tyinproxy.conf /rw/config

  The important settings to add are:

      upstream 127.0.0.1:4444
      [...]
      Allow 10.0.0.0/8

  The first line tells tinyproxy to send proxy-requests to the I2P-server. The second line allows all requests from localnet-IPs.
  If you want to be able to view some proxy stats, add the following line:

      StatHost "tinyproxy.i2p"


* dnsmasq config
  dnsmasq is configured via commandline-options in the next step.

* tor config
  tor is used as is.
  Configuration may be edited to suit your needs, please refere to the [TOR guide][tor-guide].
  (But be advised to adapt the routing according to your port configuration!)

### Startup scripts ###
There are two startup scripts that need modifications:
* `rc.local` is called on VM startup, which is where tinyproxy, dnsmasq and tor (and depending on your setup i2p) are started.
* `qubes-firewall-user-script` is called whenever routing changes, which is always when the connected VMs change.

Since the routing and startup need to use the same ports, it's a good idea to create a single config-file to define all relevant variables.
You would need to change the shell-scripts to bash-scripts by changing the first line, though: `#!/bin/sh` to `#!/bin/bash` (since bash knows the source-command and shell does not.)
Otherwise, all required environment variable have to be defined in the respective file.
But when you change one of the variables, you have to manually change the variable in the other file as well!

code of `/rw/config/config.sh`:

    #!/bin/bash
    export QUBES_IP=$(qubesdb-read /qubes-ip)
    if [ X$QUBES_IP == X ]; then
      QUBES_IP="127.0.0.1"
    fi

    export TINY_PORT=8888            #tinyproxy listen port

    export TARGET_IP=10.100.100.100  #virtual IP for i2p-requests

    export TOR_TRANS_PORT=9049       #tor transparent proxy port
    export TOR_DNS_PORT=8053         #tor's DNS server

    export I2P_HTTP=4444             #I2P HTTP-Proxy port
    export I2P_PORTS=7650            #I2P control-port

The varibale I2P_PORTS exists for future expansion.
Want to use I2P-IRC? add port 6668.
Want to use I2CP? add port 7654.
A complete list can be found [here][i2p-ports].
Some changes to the i2p-config may be required as well.
Seperate ports by comma (`,`), define ranges with colon (`:`, e.g. `7560:7668`).

Relevant code of `/rw/config/rc.local`:

    #!/bin/bash

    source /rw/config/config.sh

    if [ "$QUBES_IP" != "127.0.0.1" ]; then
        killall tor
        /usr/bin/tor \
        --SocksPort 0 \        #disable socks
        --TransListenAddress $QUBES_IP \
        --TransPort $TOR_TRANS_PORT \
        --DNSListenAddress $QUBES_IP \
        --DNSPort $TOR_DNS_PORT \
        --RunAsDaemon 1 \
        --ControlPort $TOR_CTRL_PORT \
        || (echo "Error starting TOR!", QUBES_IP="127.0.0.1")

        #I have no idea what tinyproxy is used for.
        #Killing it may be a bad idea.
        systemctl stop tinyproxy
        killall tinyproxy
        #start tinyproxy with custom config-file
        tinyproxy -c /rw/config/tinyproxy.conf

        systemctl stop dnsmasq
        killall dnsmasq
        dnsmasq --address=/.i2p/$TARGET_IP --server 127.0.0.1#$TOR_DNS_PORT

    else
      echo "$QUBES_IP is localhost. Not starting!"
    fi

The dnsmasq commandline-options tell it to resolve any `.i2p` toplevel domain to `$TARGET_IP` and query TOR's DNS server for other domains.

Relevant code of `/rw/config/qubes-firewall-user-script`:

    !#/bin/bash

    source /rw/config/config.sh
    
    #stop accidential forwards
    iptables -F FOWARD
    iptables -t nat -F

    if [ "$QUBES_IP" == "127.0.0.1" ]; then
      exit 1
    fi

    #allow local redirect
    sysctl net.ipv4.ip_forward=1
    sysctl net.ipv4.conf.all.route_localnet=1

    #accept TOR, I2P and tinyproxy
    iptables -I INPUT -i vif+ -p tcp -m multiport --dport $TOR_TRANS_PORT,$TOR_CTRL_PORT,$I2P_HTTP,$I2P_PORTS,$TINY_PORT -j ACCEPT
    iptables -I INPUT -i vif+ -p udp -m multiport --dport 53,$TOR_DNS_PORT -j ACCEPT

    #routing
    #I2P IS FOR ME!
    iptables -t nat -A PREROUTING -i vif+ -p tcp -d $TARGET_IP -m multiport --dport $I2P_HTTP,$I2P_PORTS -j REDIRECT

    #HTTP is for tinyproxy!
    iptables -t nat -A PREROUTING -i vif+ -p tcp -d $TARGET_IP --dport 80 -j REDIRECT --to-port $TINY_PORT

    #ALL TCP IS FOR TOR!
    iptables -t nat -A PREROUTING -i vif+ -p tcp -j REDIRECT --to-port $TOR_TRANS_PORT

    #local DNS resolution
    iptables -t nat -I PREROUTING -i vif+ -p udp --dport 53 -j REDIRECT --to-port 53


# Usage #
Pick any AppVM to access the I2P network or TOR hidden services. Set it's net-vm to the I2P proxyVM.
Access the router-console by opening a browser and visiting `router.i2p:7567`.
(Or, truely, any `.i2p`-domain at port :7657)  
Check I2P is up and has enough connections.
Click on one of the common pages on the routers home screen, e.g. i2pwiki.i2p!

# Final thoughts #

## Troubleshooting ##
Generally, most Problems can be resolved by waiting long enogh for I2P to gether enough connections or restarting I2P.

#### 404 - tinyproxy can't reach upstream proxy ####
I2P refuses connections.
Either it doesn't have enough connections to answer comfortably (in which case, just wait!), or I2P stopped for some reason.
In which case, open a shell in your proxyVM and type:

    sudo systemctl start i2p

#### I2P won't start! ####
Check your qubes-service settings. If those are in order, check 

## Personal notes ##

Tor may be replaced with qubes-tor, I did not try that.

Getting I2P to run in a whonix-gw whould be great, but I have had no time to get into the whonix routing and didn't find a simple, comprehensive explanation.

[I2P]:https://geti2p.net/en/about/intro
[hidden-servies]:https://geti2p.net/en/about/intro
[whonix-I2P]:https://www.whonix.org/wiki/I2p
[i2p-debian-instructions]:https://geti2p.net/en/download/debian
[tor-guide]:https://www.torproject.org/docs/tor-manual.html.en
[i2p-ports]:https://geti2p.net/uk/docs/ports