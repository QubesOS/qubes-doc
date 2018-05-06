---
layout: doc
title: Setup Behind Proxy
permalink: /doc/behind-proxy/
redirect_from:
- /en/doc/behind-proxy/
---

How to run Qubes behind a proxy
=================================================

If you are running Qubes behind a proxy (such as inside a corporate environment), there are some additional configuration steps that will need to be done in order for it access Internet resources.

This document has been tested with Qubes R4.0, but should also work with R3.2.
It assumes use of a Squid proxy for HTTP/HTTPS with the following settings.
These will be different for your environment.
Make sure to use the correct values for your proxy's FQDN, IP address, and ports instead of the examples provided in the below steps.

~~~
HTTP PROXY http://proxy.example.com:8080 or 10.0.0.1:8080
HTTPS PROXY http://proxy.example.com:8443 or 10.0.0.1:8443 (in many proxies, this will be the same port as HTTP)
FTP PROXY http://proxy.example.com:10021 or 10.0.0.1:10021 (this one too)
~~~

You can also use an authenticating proxy by adding a username and password in front, like:

~~~
HTTP PROXY http://username:password@proxy.example.com:8080 or username:password@10.0.0.1:8080
HTTPS PROXY http://username:password@proxy.example.com:8443 or username:password@10.0.0.1:8443
FTP PROXY http://username:password@proxy.example.com:10021 or username:password@10.0.0.1:10021
~~~

If you use special characters in your username or password, they need to be replaced with their `%` equivalent.
See this [table](https://grox.net/utils/encoding.html).

 1. **Whonix**

    If you are not using Whonix, skip to the next step.
    
    **Note** Running Tor through a proxy server reduces diversity of entry nodes because it restricts the set it can select from to only the ones running on 80 or 443.
    This may have security impacts.
    
    Configure `/etc/tor/torrc` (`/usr/local/etc/torrc.d/50_user.conf` in Whonix 14+) so that Whonix can connect through the proxy.
    From the Qubes menu, go to `sys-whonix -> Tor User Config` and edit the file to add these lines:
    ~~~
    DisableNetwork 0
    HTTPproxy 10.0.0.1:8080
    HTTPSproxy 10.0.0.1:8443
    FascistFirewall 1
    ~~~
    It's important here to use the IP address instead of the proxy name.

 2. **Set apps to use proxy**

    You can set proxy variables in your template(s) and all AppVMs based on them will automatically pick it up.
    In Fedora based templates, create or edit `/etc/profile.d/proxy.sh`.
    In Debian based templates, create or edit `/etc/environment` instead.
    Then, add the following settings:
    ~~~
    export http_proxy=http://proxy.example.com:8080
    export https_proxy=http://proxy.example.com:8443
    export ftp_proxy=http://proxy.example.com:10021
    ~~~
    Here we may use the fully qualified domain names instead of the proxy IP.

 3. **Allow UpdateVM to update via proxy**

    If you receive system updates through Whonix, this step can be skipped and you are done!
    If not, perform the following so updates can be downloaded through the proxy.

    First, determine your UpdateVM:  
     a. Go to a `dom0` terminal prompt.  
     b. Enter `qubes-prefs` and look for `updatevm`.  
    Perform the following steps from a terminal inside that UpdateVM (it will typically be `sys-net`).

    Enter `sudo gedit /rw/config/rc.local`.
    Add the following to the bottom, replacing the example IP address:port with your proxy's.
    Here we must use the IP of the proxy, not the FQDN.
    
    ~~~
    echo "Upstream 10.0.0.1:8080" >> /etc/tinyproxy/tinyproxy-updates.conf
    ~~~
    
    Make sure `rc.local` is set to executable with `sudo chmod 755 /rw/config/rc.local`.
    

    
*[Credit to pr0xy](https://mail-archive.com/qubes-users@googlegroups.com/msg17994.html)*
