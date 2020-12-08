---
layout: doc
title: Network Bridge Support
redirect_to: https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/network-bridge-support.md
redirect_from:
- /doc/network-bridge-support/
- /en/doc/network-bridge-support/
- /doc/NetworkBridgeSupport/
- /wiki/NetworkBridgeSupport/
---

Network Bridge Support (EXPERIMENTAL and UNSUPPORTED)
=====================================================

The Qubes development team does not support bridging the network interfaces found in NetVM and don't plan to support it at all. Several reasons for that:

-   Using a bridged VM is almost only necessary for developers testing or working on OSI layer 2 or layer 3 tools (MAC or routing protocols). If not for testing, such tools are almost only used directly on routers ...).
-   Most of these tools can be anyway used directly inside the NetVM, which has direct access to the network card.
-   It is also possible to use a secondary network card plugged into a specific development VM.
-   Such a setup could break security features of Qubes such as AppVM firewalling.

Now if you really want to work with OSI layer2 / layer 3 tools, that you don't have a secondary network card, or that you want to completely expose services of a given AppVM (at your own risk), a bridged setup may help you.

Qubes manager patch (Qubes R2B2)
--------------------------------

The following patches can be applied to the Qubes Manager GUI in order to add an option to easily bridge a VM. Use it at your own risk. If the patch breaks the Qubes Manager, you can try to restore the Qubes packages:

~~~
# qubes-dom-update qubes-core-dom0 qubes-manager
# yum reinstall qubes-core-dom0
# yum reinstall qubes-manager
~~~

First, retrieve the attachment of this Wifi article in dom0. Then apply the three patches the following way after installing the patch tool :

~~~
# qubes-dom0-update patch
# patch /usr/lib64/python2.7/site-package/qubes/qubes.py < qubes.py-bridge.diff
# patch /usr/lib64/python2.7/site-package/qubesmanager/settings.py < settings.py-bridge.diff
# patch /usr/lib64/python2.7/site-package/qubesmanager/ui_settingsdlg.py < ui_settingsdlg.py-bridge.diff
~~~

Finally restart the qubes manager GUI.

An option is available in the AppVM Settings to enable setting the NetVM in bridge mode. For a bridged AppVM, you should then select a NetVM instead of a FirewallVM/  ProxyVM, enable the Bridge option, and restart your AppVM.

NetVM patch (Qubes R2B2)
------------------------

You need to modify manually the NetVM iptable script inside the NetVM. The reason is that by default the NetVM only accepts traffic coming from network interfaces called vif\* (in our case, we will use an additional interface called bridge0. The second reason is that all traffic is NATed by default. In our case, we want to forward traffic from the bridge interface without modifying it, while NATing traffic coming from vif\* interfaces.

Modify manually the Template you use for your NetVM (not the NetVM itself). This is by default fedora-x86\_64. Edit the file /etc/sysconfig/iptables. You need to modify two parts of the file.

-   Starting from the line -A POSTROUTING -j MASQUERADE that you need to comment :

    ~~~
    # Bridge support
    # Comment the following line
    #-A POSTROUTING -j MASQUERADE
    # Ensure packets coming from firewallVMs or AppVMs use NAT
    -A POSTROUTING -m iprange --src-range 10.137.1.0-10.137.2.255 -j MASQUERADE
    # Allow redirection of bridge packets (optional as POSTROUTING default is ACCEPT)
    #-A POSTROUTING -o bridge+ -j ACCEPT
    # End Bridge support
    ~~~

-   Starting from the line -A FORWARD -i vif+ -j ACCEPT:

    ~~~
    -A FORWARD -i vif+ -o vif+ -j DROP
    -A FORWARD -i vif+ -j ACCEPT
    # Bridge Support
    -A FORWARD -i bridge+ -j ACCEPT
    # End Bridge Support
    -A FORWARD -j DROP
    ~~~

Ensure that the IP addresses used by default in Qubes are in the form 10.137.1.\* or 10.137.2.\* by running ifconfig. Of course, this setup won't work with IPv6.

Now you need to restart the NetVM and FirewallVM or only iptables in both VMs if you prefer:

~~~
# systemctl restart iptables
~~~

Create a Bridge inside the NetVM
--------------------------------

A bridge can be created inside the standard network manager (the network icon in the taskbar).

This requires:

-   creating a bridge that will be your main IP (ex: setup the bridge with DHCP)
-   attach eth0 to your bridge

Note: A wireless interface cannot be bridged.

The bridge edition GUI is somewhat buggy as it does not remember all the parameters you set up. You can fix it by editing manually the files in /etc/NetworkManager/system-connections/. Here is one example for these files:

-   Bridge-DHCP

    ~~~
    [connection]
    id=Bridge-DHCP
    uuid=fd68198b-313a-47cb-9155-52e95cdc67f3
    type=bridge
    autoconnect=false
    timestamp=1363938302

    [ipv6]
    method=auto

    [ipv4]
    method=auto

    [bridge]
    interface-name=bridge0
    stp=false
    ~~~

Note: Do not forget to put stp=false if you bridge only eth0 because sending BPDUs could make your admins angry :)

-   bridge0-eth0

    ~~~
    [802-3-ethernet]
    duplex=full
    mac-address=88:AE:1D:AE:30:31

    [connection]
    id=bridge0-eth0
    uuid=38320e5b-226c-409e-9fd6-0fbf4d0460a0
    type=802-3-ethernet
    autoconnect=false
    timestamp=1363601650
    master=fd68198b-313a-47cb-9155-52e95cdc67f3
    slave-type=bridge
    ~~~

If you do not manage to start your bridge, you can start it manually from a NetVM terminal:

~~~
$ nmcli con up id bridge0-eth0
~~~

Now that the bridge is ready, the bridged AppVM can be started...
