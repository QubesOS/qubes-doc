---
layout: doc
title: HTTP Filtering Proxy
permalink: /doc/config/http-filtering-proxy/
---

How to run an HTTP filtering proxy in a FirewallVM
=================================================

Introduction
------------

By default Qubes uses a special firewall VM that sits between the
networking VM and each AppVM. This VM controls the traffic for AppVMs
and can be used to restrict what AppVMs can send or receive. The
traffic rules can be setup using filtering rules GUI in Qubes VM
manager. The manager translates user-defined setup into iptables rules
for the kernel of firewall VM.

The primary goal of the filtering rule setup in firewall VM is to
allow for the user to protect either from own mistakes (like accessing
an arbitrary website from a browser running in a banking VM) or from
mistakes of websites (like a banking website that loads JS code from a
social network operator when the user logs in into the bank).

As the rules in the firewall are IP-based, it has drawbacks. First the
rules cannot be used if one has to use a HTTP proxy to connect for
websites (a common setup on corporate networks). Second the Qubes
resolves DNS names from the firewall rules when the AppVM loads. This
prevents websites that use DNS-based load balancers from working
unless the user reloads the firewall rules (which re-resolve the DNS
names) whenever the balancer transfer her session to another IP. Third
the initial setup of the rules is complicated as the firewall drops
the connection silently. As a workaround one can use browser's network
console to see what is blocked, but this is time-consuming and one can
trivially miss some important cases like including in the firewall
white-list sites for OCSP SSL certificate verification.

These drawbacks can be mitigated if one replaces iptable-based rules
with a filtering HTTP proxy. The following describes how to setup
tinyproxy-based proxy in the firewall VM to archive such filtering.


Warning
-------

Running a HTTP proxy in your firewall VM increases the attack surface
against that VM from a compromised AppVM. tinyproxy has a relatively
simple code and a reasonable track record to allow to certain level of
trust. But one cannot exclude bugs especially in the case of a hostile
proxy clients as this is less tested scenario. So it is not advisable
to use the proxy in a shared firewall VM against untrusted AppVM to
black-list some unwanted connection like advertisement sites.

Less problematic setup is to white-list possible connections for
several trusted and semi-trusted AppVMs within one firewall VM. Still
for maximum safety one should consider running a separated firewall VM
per each important AppVMs and run the proxy there.

As a counterweight to this warning it is important to point out that
HTTP proxy decreases attack surface against AppVM. For example, with a
proxy the AppVM does not need DNS connections so a bug in the kernel
or in the browser in that area would not affect the AppVM. Also
browsers typically avoid many latest and greatest HTTP features when
connection through proxies minimizing exposure of new and unproven
networking code.


Setup
-----

1. Copy this [archive] with the proxy control script, default
   tinyproxy config and a sample firewall filtering file into the
   firewall VM and unpack it in `/rw/config` folder there as root:

        cd /rw/config
        sudo tar xzf .../proxy.tar.xz

2. If necessary adjust `/rw/config/tinyproxy/config` according to the
   man page for `tinyproxy.conf`. The included config file refuses the
   connection unless the host is white-listed in the filtering file, so
   this can be altered if one wants rather to black-list connection. One
   may also specify upstream proxies there. The file is a template file
   and the control script will replace `{name}` constructs in the file with
   actual parameters. In general lines with `{}` should be preserved as is.

3. For each AppVM that one wants to run through the proxy create an
   the corresponding filtering file in the `/rw/config/tinyproxy`
   directory. With the default config the filtering file should contain
   regular expressions to match white-listed hosts with one regular
   expression per line, see the man page for tinyproxy.conf for details.
   The file should be named:

        name.ip-address-of-app-vm

   The name part before the dot can be arbitrary. For convenience one can
   use AppVM name here, but this is not required. It is important to get
   ip address part right as this is what the control script uses to
   determine for which AppVM to apply the proxy rules. One can check the
   IP address of AppVM in Qubes VM manager in the VM settings dialog, see
   the Networking session under the Basic tab.

   The attached archive includes `tinyproxy/social.10.137.2.13` file with a
   rules for a AppVM allowing connection to google, facebook, linkedin,
   livejournal, youtube and few other other sites. One can use it as an
   example after changing the the IP address accordingly.

   When editing the rules remember to include `$` at the end of the host
   name and to prefix each dot in the host name with the backslash. This
   way the pattern matches the whole host and not just some prefix and
   the dot is not interpreted as an instruction to match an arbitrary
   character according to regular expression syntax.

4. Check that `proxyctl.py` script can properly recognize the rule
   files. For that run:

        sudo /rw/config/tinyproxy/proxyctl.py show

   For each rule file it should print the name, ip address, network
   interface of the running AppVM if AppVM runs and the id of the
   tinyproxy process that proxies that AppVM. The first time each pid
   should be `--`.

5. Now run some AppVM with proxy and then run:

        sudo /rw/config/tinyproxy/proxyctl.py update

   The update command starts proxy processes and adjusts the iptable
   rules to allow for proxy traffic for each running AppVM from the
   filtering files list. For each stopped AppVM the proxy is killed.

   Check that proxy is started so the `pid` field of the show command is a
   number:

        sudo /rw/config/tinyproxy/proxyctl.py show

6. Run the browser in the started AppVM and configure it to use the
   proxy on the port 8100 running at the IP address of the firewall VM
   gateway interface. In Qubes VM manager the address is given after the
   Gateway label in the Setting dialog for the firewall VM.

   In Firefox go to the Preferences dialog, select Advanced->Network,
   click Settings for the Connection section. In the Connection Settings
   dialog select Manual proxy configuration. For HTTP Proxy field use the
   IP address of the firewall gateway interface.  Enter 8100 as the port
   and the select the checkbox "Use this proxy server for all protocols".

   Go to some site. The browser should either load it if it was
   white-listed in the filtering file or show a page generated by
   tinyproxy that the page was filtered out.

   In the firewall VM see `/run/tinyproxy/name/log` file. For each filtered
   out website it contains an entry and one can adjust the filtering file
   to include the corresponding host. After changing the file run either:

        sudo /rw/config/tinyproxy/proxyctl.py restart name

   to restart proxy with the updated rules file only for the given VM or

        sudo /rw/config/tinyproxy/proxyctl.py kill-all-and-restart

   to restart all proxy processes.

7. To make sure that the proxy is started automatically when the AppVM
   starts change `/rw/config/qubes-firewall-user-script` to include the
   following line:

        /rw/config/tinyproxy/proxyctl.py update

   If the file does not exist, create it so it looks like this:

        #!/usr/bin/bash
        /rw/config/tinyproxy/proxyctl.py update

   Make sure that the script is owned by root and executable:

        sudo chown root:root /rw/config/qubes-firewall-user-script
        sudo chmod 755 /rw/config/qubes-firewall-user-script

8. In Qubes VM manager adjust Firewall rules for each AppVM with a
   proxy. In a typical case when only HTTP proxy should be used for
   outside connections, simply select "Deny network access except...," make
   sure that the address list is empty and then unselect "Allow ICMP," "DNS"
   and "Update proxy" checkboxes.

   There is no need to add any special entries for the proxy in the GUI
   as `proxyctl.py` adds rules for the proxy traffic itself. 

--------------------------------------------------------------------------------

This guide was initially written by Igor Bukanov in a [message] to the
`qubes-devel` [mailing list].

[archive]: https://groups.google.com/group/qubes-devel/attach/39c95d63fccca12b/proxy.tar.gz?part=0.1
[message]: https://groups.google.com/d/msg/qubes-devel/UlK8P27UtD4/K6HM_GNdyTkJ
[mailing list]: /mailing-lists/
