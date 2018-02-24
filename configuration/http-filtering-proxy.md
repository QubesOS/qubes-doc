---
layout: doc
title: HTTP Filtering Proxy
permalink: /doc/config/http-filtering-proxy/
---

How to run an HTTP filtering proxy in a FirewallVM
=================================================

Introduction
------------

By default, Qubes uses a special firewall VM that sits between the networking VM and each AppVM.
This VM controls the traffic for AppVMs and can be used to restrict what AppVMs can send or receive.
The traffic rules can be setup using the filtering rules GUI in Qubes VM manager.
The manager translates user-defined setup into iptables rules for the firewall VM's kernel.

The primary goal of the filtering rule setup in the firewall VM is to allow for the user to protect either from his own mistakes (like accessing an arbitrary website from a browser running in a banking VM) or from the mistakes of websites (like a banking website that loads JS code from a social network operator when the user logs into the bank).

As the rules in the firewall are IP-based, it has drawbacks.
First, the rules cannot be used if one has to use an HTTP proxy to connect to websites (a common setup on corporate networks).
Second, Qubes resolves DNS names from the firewall rules when the AppVM loads.
This prevents websites that use DNS-based load balancers from working unless the user reloads the firewall rules (which re-resolve the DNS names) whenever the balancer transfers her session to another IP.
Third, the initial setup of the rules is complicated as the firewall drops the connection silently.
As a workaround, one can use a browser's network console to see what is blocked, but this is time-consuming and one can easily miss some important cases like including sites for OCSP SSL certificate verification in the firewall white-list.

These drawbacks can be mitigated if one replaces iptable-based rules with a filtering HTTP proxy.
The following describes how to setup a tinyproxy-based proxy in the firewall VM to achieve such filtering.

**Note** This content only describes setup of an HTTP proxy.
This will handle web browsing using HTTP and HTTPS, but this type of proxy does not support other protocols such as IMAP used in Thunderbird.
For that, you need a fully featured SOCKS proxy such as Squid which is beyond the scope of this article.

Warning
-------

Running an HTTP proxy in your firewall VM increases the attack surface against that VM from a compromised AppVM.
Tinyproxy has relatively simple code and a reasonable track record to allow to certain level of trust, but one cannot exclude bugs especially in the case of hostile proxy clients as this is a less tested scenario.
It is not advisable to use the proxy in a shared firewall VM against untrusted AppVMs to black-list some unwanted connections such as advertisement sites.

A less problematic setup is to white-list possible connections for several trusted and semi-trusted AppVMs within one firewall VM.
Still, for maximum safety, one should consider running a separate ProxyVM for each important AppVM.

In Qubes R4.0, one no longer creates ProxyVMs as such. However, the same is accomplished by choosing the `provides network` checkbox when creating an AppVM that will be used as a proxy.

As a counterpoint to this warning, it is important to note that an HTTP proxy decreases the attack surface of AppVMs.
For example, with a proxy the AppVM does not need to make direct DNS connections, so a bug in the kernel or in the browser in that area would not affect the AppVM.
Also, browsers typically avoid many of the latest and greatest HTTP features when connecting through proxies, minimizing exposure of new and unproven networking code.


Setup
-----

1. After reading through the Warning section above, determine if you want to proceed with the following steps in either your default `sys-firewall` VM or in a newly created proxy VM.
   If you decide to create a separate proxy VM,
    * In R4.0, create a new AppVM with the `provides network` checkbox set.
    * In R3.2, create a new ProxyVM.
   
   Then, proceed with the following.

2. Copy this [archive] with the proxy control script, default tinyproxy config, and a sample filtering file into the proxy VM and unpack it in the `/rw/config` folder there as root:

        cd /rw/config
        sudo tar xzf .../proxy.tar.xz

3. If necessary, adjust `/rw/config/tinyproxy/config` according to the man page for `tinyproxy.conf`.
   The included config file refuses the connection unless the host is white-listed in the filtering file, so this can be altered if one prefers to black-list connections.
   One may also specify upstream proxies here.
   The file is a template file and the control script will replace `{name}` constructs in the file with actual parameters.
   In general, lines with `{}` should be preserved as is.

4. For each AppVM that one wants to run through the proxy, create a corresponding filtering file in the `/rw/config/tinyproxy` directory.
   With the default config, the filtering file should contain regular expressions to match white-listed hosts with one regular expression per line.
   See the man page for tinyproxy.conf for details.
   The file should be named:

        name.ip-address-of-app-vm

   The name before the dot is arbitrary.
   For convenience, one can use an AppVM name here, but this is not required.
   
   It is important to get the ip address part right, as this is what the control script uses to determine to which AppVM it will apply the proxy rules.
   If you have created a separate proxy VM, change the `NetVM` of each AppVM that will be using it to the proxy VM.
   That can be done in Qubes VM manager in the VM settings dialog under the Basic tab.
   Next, see the Networking settings on the same tab to check the IP address of an AppVM.

   The attached archive includes a `social.10.137.2.13` file with rules for an AppVM allowing connections to Google, Facebook, Linkedin, Livejournal, Youtube, and few other other sites.
   One can use it as an example after changing the IP address accordingly.

   When editing the rules, remember to include a `$` at the end of the host name, and to prefix each dot in the host name with a backslash (like `\.`).
   This way, the pattern matches the whole host and not just a prefix, and the dot is not interpreted as an instruction to match an arbitrary character according to regular expression syntax.

5. Check that the `proxyctl.py` script can properly recognize the rule files.
   For that, run:

        sudo /rw/config/tinyproxy/proxyctl.py show

   For each rule file it should print the name, ip address, and network interface of the running AppVMs.
   It will also display the id of the tinyproxy process that proxies that AppVM.
   Each pid will be `--` because we have no running proxies yet.

6. Now, start the AppVM for which you created a rule file, and then run:

        sudo /rw/config/tinyproxy/proxyctl.py update

   The update command starts proxy processes and adjusts the iptable rules to allow for proxy traffic for each running AppVM from the filtering files list.
   For each stopped AppVM, the proxy is killed.

   Check that proxy is started and the `pid` field of the show command is a number:

        sudo /rw/config/tinyproxy/proxyctl.py show

7. Run the browser in the active AppVM and configure it to use the proxy on port 8100 of the proxy VM interface's IP address.
   In Qubes VM manager, the IP address is displayed in the Gateway field in the Settings dialog for the AppVM.

   In Firefox, go to the Preferences dialog, select Advanced->Network, and click Settings for the Connection section.
   In the Connection Settings dialog, select Manual proxy configuration. For the HTTP Proxy field use the IP address of the AppVM's gateway.
   Enter 8100 as the port, and select the checkbox "Use this proxy server for all protocols".

   Go to a test web site.
   The browser should either load it (if it was white-listed in the filtering file), or show a page generated by tinyproxy that the page was filtered out.

   In the proxy VM, see the `/run/tinyproxy/<name>/log` file.
   For each filtered out website it contains an entry, and one can adjust the filtering file to include the corresponding host.
   After changing the file, run either:
   
        sudo /rw/config/tinyproxy/proxyctl.py restart <name>

   to restart the proxy with an updated rules file only for the given VM, or

        sudo /rw/config/tinyproxy/proxyctl.py kill-all-and-restart

   to restart all proxy processes.

8. To make sure that the proxy is started automatically when the AppVM starts, change `/rw/config/qubes-firewall-user-script` to include the following line:

        /rw/config/tinyproxy/proxyctl.py update

   If the file does not exist, create it so it looks like this:

        #!/bin/sh
        /rw/config/tinyproxy/proxyctl.py update

   Make sure that the script is owned by root and executable:

        sudo chown root:root /rw/config/qubes-firewall-user-script
        sudo chmod 755 /rw/config/qubes-firewall-user-script

9. In Qubes VM manager, adjust the Firewall rules for each AppVM using a proxy.
   In a typical case, when only the HTTP proxy should be permitted for outside connections:
    * In R4.0, select "Limit outgoing Internet connections to..." and make sure the address list is empty.
    * In R3.2, select "Deny network access except...", make sure the address list is empty, and then unselect the "Allow ICMP," "DNS", and "Update proxy" checkboxes.

   There is no need to add any special entries for the proxy in the GUI as `proxyctl.py` adds rules for the proxy traffic itself. 

--------------------------------------------------------------------------------

This guide was initially written by Igor Bukanov in a [message] to the `qubes-devel` [mailing list].

[archive]: https://groups.google.com/group/qubes-devel/attach/39c95d63fccca12b/proxy.tar.gz?part=0.1
[message]: https://groups.google.com/d/msg/qubes-devel/UlK8P27UtD4/K6HM_GNdyTkJ
[mailing list]: /mailing-lists/
