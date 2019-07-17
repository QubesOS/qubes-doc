---
layout: doc
title: TorVM
permalink: /doc/torvm/
redirect_from:
- /doc/privacy/torvm/
- /en/doc/torvm/
- /doc/TorVM/
- /doc/UserDoc/TorVM/
- /wiki/UserDoc/TorVM/
---

Known issues:
-------------

-   [Service doesn't start without (even empty) user torrc](https://groups.google.com/d/msg/qubes-users/fyBVmxIpbSs/R5mxUcIEZAQJ)

Qubes TorVM (qubes-tor)
==========================

Qubes TorVM is a deprecated ProxyVM service that provides torified networking to
all its clients. **If you are interested in TorVM, you will find the
[Whonix implementation in Qubes](/doc/privacy/whonix/) a
more usable and robust solution for creating a torifying traffic proxy.**

By default, any AppVM using the TorVM as its NetVM will be fully torified, so
even applications that are not Tor aware will be unable to access the outside
network directly.

Moreover, AppVMs running behind a TorVM are not able to access globally
identifying information (IP address and MAC address).

Due to the nature of the Tor network, only IPv4 TCP and DNS traffic is allowed.
All non-DNS UDP and IPv6 traffic is silently dropped.

See [this article](https://blog.invisiblethings.org/2011/09/28/playing-with-qubes-networking-for-fun.html) for a description of the concept, architecture, and the original implementation.

## Warning + Disclaimer

1. Qubes TorVM is produced independently from the Tor(R) anonymity software and
   carries no guarantee from The Tor Project about quality, suitability or
   anything else.

2. Qubes TorVM is not a magic anonymizing solution. Protecting your identity
   requires a change in behavior. Read the "Protecting Anonymity" section
   below.

3. Traffic originating from the TorVM itself **IS NOT** routed through Tor.
   This includes system updates to the TorVM. Only traffic from VMs using TorVM
   as their NetVM is torified.

Installation
============


0. *(Optional)* If you want to use a separate vm template for your TorVM

        qvm-clone fedora-23 fedora-23-tor

1. In dom0, create a proxy vm and disable unnecessary services and enable qubes-tor


        qvm-create -p torvm
        qvm-service torvm -d qubes-netwatcher
        qvm-service torvm -d qubes-firewall
        qvm-service torvm -e qubes-tor

        # if you  created a new template in the previous step
        qvm-prefs torvm -s template fedora-23-tor

2. From your TemplateVM, install the torproject Fedora repo

        sudo yum install qubes-tor-repo

3. Then, in the template, install the TorVM init scripts

        sudo yum install qubes-tor

5. Configure an AppVM to use TorVM as its NetVM (for example a vm named anon-web)

        qvm-prefs -s anon-web netvm torvm
        ... repeat for any other AppVMs you want torified...

6. Shutdown the TemplateVM.
7. Set the prefs of your TorVM to use the default sys-net or sys-firewall as its NetVM

        qvm-prefs -s torvm netvm sys-net

8. Start the TorVM and any AppVM you have configured to be route through the TorVM
9. From the AppVMs, verify torified connectivity, e.g. by visiting
   `https://check.torproject.org`.


### Troubleshooting ###


1. Check if the qubes-tor service is running (on the torvm)

        [user@torvm] $ sudo service qubes-tor status

2. Tor logs to syslog, so to view messages use

        [user@torvm] $ sudo grep Tor /var/log/messages

3. Restart the qubes-tor service (and repeat 1-2)

        [user@torvm] $ sudo service qubes-tor restart

4. You may need to manually create the private data directory and set its permissions:

        [user@torvm] $ sudo mkdir /rw/usrlocal/lib/qubes-tor
        [user@torvm] $ sudo chown user:user /rw/usrlocal/lib/qubes-tor

Usage
=====

Applications should "just work" behind a TorVM, however there are some steps
you can take to protect anonymity and increase performance.

## Protecting Anonymity

The TorVM only purports to prevent the leaking of two identifiers:

1. WAN IP Address
2. NIC MAC Address

This is accomplished through transparent TCP and transparent DNS proxying by
the TorVM.

The TorVM cannot anonymize information stored or transmitted from your AppVMs
behind the TorVM.

*Non-comprehensive* list of identifiers TorVM does not protect:

* Time zone
* User names and real name
* Name+version of any client (e.g. IRC leaks name+version through CTCP)
* Metadata in files (e.g., exif data in images, author name in PDFs)
* License keys of non-free software

### Further Reading

* [Information on protocol leaks](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO#Protocolleaks)
* [Official Tor Usage Warning](https://www.torproject.org/download/download-easy.html.en#warning)
* [Tor Browser Design](https://www.torproject.org/projects/torbrowser/design/)

## How to use Tor Browser behind TorVM

1. In a clean VM, [download Tor Browser from the Tor Project][tor-browser].
2. [Verify the PGP signature][tor-verify-sig].
3. Copy/move the Tor Browser archive into your AnonVM (i.e., the AppVM which has your TorVM as its netvm).
4. Unpack the Tor Browser archive into your home directory.
5. In dom0, right click the KDE Application Launcher Menu (AKA "Start Menu") and left click "Edit Applications..."
6. In the KDE Menu Editor, find your AnonVM's group and create a new item (or make a copy of an existing item).
7. Edit the following fields on the "General" tab:
   * Name: `my-new-anonvm: Tor Browser`
   * Command: `qvm-run -q --tray -a my-new-anonvm 'TOR_SKIP_LAUNCH=1 TOR_SKIP_CONTROLPORTTEST=1 TOR_SOCKS_PORT=9050 TOR_SOCKS_HOST=1.2.3.4 ./tor-browser_en-US/Browser/start-tor-browser'`
     * Replace `my-new-anonvm` with the name of your AnonVM.
     * Replace `1.2.3.4` with your TorVM's internal Qubes IP address, which can be viewed in Qubes VM Manager by clicking "View" --> "IP" or by running `qvm-ls -n` in dom0.
     * Replace `en-US` with your locale ID, if different.
8. Click "Save" in the KDE Menu Editor.

Tor Browser should now work correctly in your AnonVM when launched via the shortcut you just created.

**Note:** If you want to use Tor Browser in a [DispVM][dispvm], the steps are the same as above, except you should copy the Tor Browser directory into your DVM template, [regenerate the DVM template][dispvm-customization], then use the following command in your KDE menu entry:

`sh -c 'echo TOR_SKIP_LAUNCH=1 TOR_SKIP_CONTROLPORTTEST=1 TOR_SOCKS_PORT=9050 TOR_SOCKS_HOST=1.2.3.4 ./tor-browser_en-US/Browser/start-tor-browser | /usr/lib/qubes/qfile-daemon-dvm qubes.VMShell dom0 DEFAULT red'`

(Replace `1.2.3.4` and `en-US` as indicated above.)

## Performance

In order to mitigate identity correlation TorVM makes use of Tor's new [stream
isolation feature][stream-isolation]. Read "Threat Model" below for more
information.

However, this isn't desirable in all situations, particularly web browsing.
These days loading a single web page requires fetching resources (images,
javascript, css) from a dozen or more remote sources. Moreover, the use of
IsolateDestAddr in a modern web browser may create very uncommon HTTP behavior
patterns, that could ease fingerprinting.

Additionally, you might have some apps that you want to ensure always share a
Tor circuit or always get their own.

For these reasons TorVM ships with two open SOCKS5 ports that provide Tor
access with different stream isolation settings:

* Port 9050 - Isolates by SOCKS Auth and client address only  
              Each AppVM gets its own circuit, and each app using a unique SOCKS
              user/pass gets its own circuit
* Port 9049 - Isolates client + destination port, address, and by SOCKS Auth
              Same as default settings listed above, but additionally traffic
              is isolated based on destination port and destination address.


## Custom Tor Configuration

Default tor settings are found in the following file and are the same across
all TorVMs.

      /usr/lib/qubes-tor/torrc

You can override these settings in your TorVM, or provide your own custom
settings by appending them to:

      /rw/config/qubes-tor/torrc

For information on tor configuration settings `man tor`

Threat Model
============

TorVM assumes the same Adversary Model as [TorBrowser][tor-threats], but does
not, by itself, have the same security and privacy requirements.

## Proxy Obedience

The primary security requirement of TorVM is *Proxy Obedience*.

Client AppVMs MUST NOT bypass the Tor network and access the local physical
network, internal Qubes network, or the external physical network.

Proxy Obedience is assured through the following:

1. All TCP traffic from client VMs is routed through Tor
2. All DNS traffic from client VMs is routed through Tor
3. All non-DNS UDP traffic from client VMs is dropped
4. Reliance on the [Qubes OS network model][qubes-net] to enforce isolation

## Mitigate Identity Correlation

TorVM SHOULD prevent identity correlation among network services.

Without stream isolation, all traffic from different activities or "identities"
in different applications (e.g., web browser, IRC, email) end up being routed
through the same tor circuit. An adversary could correlate this activity to a
single pseudonym.

TorVM uses the default stream isolation settings for transparently torified
traffic. While more paranoid options are available, they are not enabled by
default because they decrease performance and in most cases don't help
anonymity (see [this tor-talk thread][stream-isolation-explained])

By default TorVM does not use the most paranoid stream isolation settings for
transparently torified traffic due to performance concerns. By default TorVM
ensures that each AppVM will use a separate tor circuit (`IsolateClientAddr`).

For more paranoid use cases the SOCKS proxy port 9049 is provided that has all
stream isolation options enabled. User applications will require manual
configuration to use this socks port.


Future Work
===========
* Integrate Vidalia
* Create Tor Browser packages w/out bundled tor
* Use local DNS cache to speedup queries (pdnsd)
* Support arbitrary [DNS queries][dns]
* Fix Tor's openssl complaint
* Support custom firewall rules (to support running a relay)

Acknowledgements
================

Qubes TorVM is inspired by much of the previous work done in this area of
transparent torified solutions. Notably the following:

* [Patrick Schleizer](mailto:adrelanos@riseup.net) for his work on [Whonix](https://www.whonix.org)
* The [Tor Project wiki](https://trac.torproject.org/projects/tor/wiki/doc/TorifyHOWTO)
* And the many people who contributed to discussions on [tor-talk](https://lists.torproject.org/pipermail/tor-talk/)

[stream-isolation]: https://gitweb.torproject.org/torspec.git/blob/HEAD:/proposals/171-separate-streams.txt
[stream-isolation-explained]: https://lists.torproject.org/pipermail/tor-talk/2012-May/024403.html
[tor-threats]: https://www.torproject.org/projects/torbrowser/design/#adversary
[qubes-net]: /doc/QubesNet/
[dns]: https://tails.boum.org/todo/support_arbitrary_dns_queries/
[tor-browser]: https://www.torproject.org/download/download-easy.html
[tor-verify-sig]: https://www.torproject.org/docs/verifying-signatures.html
[dispvm]: /doc/DisposableVms/
[dispvm-customization]: /doc/UserDoc/DispVMCustomization/
