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

This example assumes use of a Squid proxy for HTTP/HTTPS with the following settings.
These will be different for your environment.
Make sure to use the correct values for your proxy's FQDN, IP address, and ports instead of the examples provided in the below steps.

~~~
HTTP PROXY http://proxy.example.com:8080 or 10.0.0.1:8080
HTTPS PROXY http://proxy.example.com:8443 or 10.0.0.1:8443 (in some proxies, this will be the same port as HTTP)
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
    
    Configure `torrc` so that Whonix can connect through the proxy.
    From the Qubes menu, go to `sys-whonix -> Tor User Config` and edit the `torrc` file to add these lines:
    ~~~
    DisableNetwork 0
    HTTPproxy 10.0.0.1:8080
    HTTPSproxy 10.0.0.1:8443
    FascistFirewall 1
    ~~~
    It's important here to use the IP address instead of the proxy name.

 2. **Set apps to use proxy**

    You can set `http_proxy` and `https_proxy` variables in your template(s) and all AppVMs based on them will automatically pick it up.
    In Fedora based templates, create or edit `/etc/profile.d/proxy.sh`.
    In Debian based templates, create or edit `/etc/environment` instead.
    Then, add the following settings:
    ~~~
    export http_proxy=http://proxy.example.com:8080
    export https_proxy=http://proxy.example.com:8443
    export ftp_proxy=http://proxy.example.com:10021
    export HTTP_PROXY=http://proxy.example.com:8080
    export HTTPS_PROXY=http://proxy.example.com:8443
    export FTP_PROXY=http://proxy.example.com:10021
    ~~~
    Here we use the fully qualified domain names instead of the proxy IP.

 3. **Allow UpdateVM to update via proxy**

    If you receive system updates through Whonix, this step can be skipped and you are done!
    If not, perform the following so updates can be downloaded through the proxy.

    First, determine which template your UpdateVM is using:  
     a. Go to a `dom0` terminal prompt.  
     b. Enter `qubes-prefs` and look for `updatevm`.  
     c. Enter `qvm-prefs <UpdateVMName>` and look for `template`.  
    Perform the following steps from inside that template.

    Add `proxy=http://10.0.0.1:8080` to the bottom of `/etc/apt/apt.conf.d/71proxy` in Debian templates.
    In Fedora, add it to `/etc/dnf/dnf.conf` instead, after the line that says `### QUBES END ###`.
    
    For example,
    ~~~
    [user@fedora-26 ~]$ sudo gedit /etc/dnf/dnf.conf
    .
    .
    ### QUBES END ###
    proxy=http://10.0.0.1:8080
    ~~~
    Again, here we must use the IP of the proxy.
    
*[Credit to pr0xy](https://mail-archive.com/qubes-users@googlegroups.com/msg17994.html)*
