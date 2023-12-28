========
Firewall
========


Introduction
------------

| This page explains use of the firewall in Qubes 4.2, using
  ``nftables``.
| In Qubes 4.1, all firewall components used ``iptables``. For details
  of that usage see `here <../firewall_4.1/>`__


Understanding firewalling in Qubes
----------------------------------


Every qube in Qubes is connected to the network via a FirewallVM, which
is used to enforce network-level policies. By default there is one
default FirewallVM, but the user is free to create more, if needed.

For more information, see the following:

- https://groups.google.com/group/qubes-devel/browse_thread/thread/9e231b0e14bf9d62

- https://blog.invisiblethings.org/2011/09/28/playing-with-qubes-networking-for-fun.html



How to edit rules
-----------------


In order to edit rules for a given qube, select it in the Qube Manager
and press the “firewall” button.

.. figure:: /attachment/doc/r4.0-manager-firewall.png
   :alt: r4.0-manager-firewall.png

   r4.0-manager-firewall.png

If the qube is running, you can open Settings from the Qube Popup Menu.

ICMP and DNS are not accessible in the GUI, but can be changed via
``qvm-firewall`` described below. Connections to Updates Proxy are not
made over a network so can not be allowed or blocked with firewall
rules, but are controlled using the relevant policy file (see :doc:`R4.x Updates proxy </user/how-to-guides/how-to-install-software>` for more detail).

Note that if you specify a rule by DNS name it will be resolved to IP(s)
*at the moment of applying the rules*, and not on the fly for each new
connection. This means it will not work for servers using load
balancing, and traffic to complex web sites which draw from many servers
will be difficult to control.

Instead of using the firewall GUI, you can use the ``qvm-firewall``
command in Dom0 to edit the firewall rules by hand. This gives you
greater control than by using the GUI.

The firewall rules for each qube are saved in an XML file in that qube’s
directory in dom0:

.. code:: bash

      /var/lib/qubes/appvms/<vm-name>/firewall.xml



Rules are implemented on the netvm.

You can also manually create rules in the qube itself using standard
firewalling controls. See `Where to put firewall rules <#where-to-put-firewall-rules>`__. In complex cases, it might be
appropriate to load a ruleset using ``nft -f /path/to/ruleset`` called
from ``/rw/config/rc.local``, the ruleset file can be populated from the
current ruleset using ``nft list ruleset > /path/to/ruleset``, you
should add ``flush ruleset`` at the top of the file to remove all
existing rules before loading them. if you do this, be aware that
``rc.local`` is called *after* the network is up, so local rules should
not be relied upon to block leaks.

Reconnecting qubes after a NetVM reboot
---------------------------------------


Normally Qubes doesn’t let the user stop a NetVM if there are other
qubes running which use it as their own NetVM. But in case the NetVM
stops for whatever reason (e.g. it crashes, or the user forces its
shutdown via qvm-kill via terminal in Dom0), Qubes R4.x will often
automatically repair the connection. If it does not, then there is an
easy way to restore the connection to the NetVM by issuing in dom0:

.. code:: bash

      qvm-prefs <vm> netvm <netvm>



Normally qubes do not connect directly to the actual NetVM (sys-net by
default) which has networking devices, but rather to the default
sys-firewall first, and in most cases it would be the NetVM that will
crash, e.g. in response to S3 sleep/restore or other issues with WiFi
drivers. In that case it is only necessary to issue the above command
once, for the sys-firewall (this assumes default VM-naming used by the
default Qubes installation):

.. code:: bash

      qvm-prefs sys-firewall netvm sys-net



Network service qubes
---------------------


Qubes does not support running any networking services (e.g. VPN, local
DNS server, IPS, …) directly in a qube that is used to run the Qubes
firewall service (usually sys-firewall) for good reasons. In particular,
if you want to ensure proper functioning of the Qubes firewall, you
should not tinker with nftables rules in such qubes.

Instead, you should deploy a network infrastructure such as

.. code:: bash

      sys-net <--> sys-firewall-1 <--> network service qube <--> sys-firewall-2 <--> [client qubes]



Thereby sys-firewall-1 is only needed if you have other client qubes
connected there, or you want to manage the traffic of the local network
service qube. The sys-firewall-2 proxy ensures that:

1. Firewall changes done in the network service qube cannot render the
   Qubes firewall ineffective.

2. Changes to the Qubes firewall by the Qubes maintainers cannot lead to
   unwanted information leakage in combination with user rules deployed
   in the network service qube.

3. A compromise of the network service qube does not compromise the
   Qubes firewall.



If you adopt this model, you should be aware that all traffic will
arrive at the ``network service qube`` appearing to originate from the
IP address of ``sys-firewall-2``.

For the VPN service please also look at the `VPN documentation <https://forum.qubes-os.org/t/19061>`__.

Enabling networking between two qubes
-------------------------------------


Normally any networking traffic between qubes is prohibited for security
reasons. However, in special situations, you might want to selectively
allow specific qubes to establish networking connectivity between each
other. For example, this might be useful in some development work, when
you want to test networking code, or to allow file exchange between HVM
domains (which do not have Qubes tools installed) via SMB/SSH/NFS
protocols.

In order to allow networking from qube A (client) to qube B (server)
follow these steps:

- Make sure both A and B are connected to the same firewall vm (by
  default all VMs use the same firewall VM).

- Note the Qubes IP addresses assigned to both qubes. This can be done
  using the ``qvm-ls -n`` command, or via the Qubes Manager using the
  IP column.

- Start both qubes, and also open a terminal in the firewall VM

- In the firewall VM’s terminal enter the following nftables rule:



.. code:: bash

      sudo nft add rule ip qubes custom-forward ip saddr <IP address of A> ip daddr <IP address of B> ct state new,established,related counter accept



- In qube B’s terminal enter the following nftables rule:



.. code:: bash

      sudo nft add rule qubes custom-input ip saddr <IP address of A> ct state new,established,related counter accept



- Now you should be able to reach B from A – test it using e.g. ping
  issued from A. Note however, that this doesn’t allow you to reach A
  from B – for this you would need two more rules, with A and B
  swapped.

- If everything works as expected, then you should write the above
  nftables rules into firewallVM’s ``qubes-firewall-user-script``
  script. This script is run when the netvm starts up. You should also
  write relevant rules in A and B’s ``rc.local`` script which is run
  when the qube is launched. Here’s an example how to update the
  script:



.. code:: bash

      [user@sys-firewall ~]$ sudo -i
      [root@sys-firewall user]# echo "nft add rule ip qubes custom-forward ip saddr 10.137.2.25 ip daddr 10.137.2.6 ct state new,established,related counter accept" >> /rw/config/qubes-firewall-user-script



- Here is an example how to update ``rc.local``:



.. code:: bash

      [user@B ~]$ sudo -i
      [root@B user]# echo "nft add rule qubes custom-input ip saddr 10.137.2.25 accept" >> /rw/config/rc.local



Opening a single TCP port to other network-isolated qube
--------------------------------------------------------


In the case where a specific TCP port needs to be exposed from a qubes
to another one, you do not need to enable networking between them but
you can use the qubes RPC service ``qubes.ConnectTCP``.

**1. Simple port binding**

Consider the following example. ``mytcp-service`` qube has a TCP service
running on port ``444`` and ``untrusted`` qube needs to access this
service.

- In dom0, add the following to
  ``/etc/qubes/policy.d/30-user-networking.policy``: (it could be
  ``another-other-name.policy`` – just remember to keep it consistent)

  .. code:: bash

        qubes.ConnectTCP * untrusted @default allow target=mytcp-service



- In untrusted, use the Qubes tool ``qvm-connect-tcp``:

  .. code:: bash

        [user@untrusted #]$ qvm-connect-tcp 444:@default:444





   Note: The syntax is the same as SSH tunnel handler. The first ``444``
   correspond to the localport destination of ``untrusted``,
   ``@default`` the remote machine and the second ``444`` to the remote
   machine port.

The service of ``mytcp-service`` running on port ``444`` is now
accessible in ``untrusted`` as ``localhost:444``.

Here ``@default`` is used to hide the destination qube which is
specified in the Qubes RPC policy by ``target=mytcp-service``.
Equivalent call is to use the tool as follow:

.. code:: bash

      [user@untrusted #]$ qvm-connect-tcp ::444



which means to use default local port of ``unstrusted`` as the same of
the remote port and unspecified destination qube is ``@default`` by
default in ``qrexec`` call.

**2. Binding remote port on another local port**

Consider now the case where someone prefers to specify the destination
qube and use another port in untrusted, for example ``10044``. Instead
of previous case, add

.. code:: bash

      qubes.ConnectTCP * untrusted mytcp-service allow



in ``/etc/qubes/policy.d/30-user-networking.policy`` and in untrusted,
use the tool as follow:

.. code:: bash

      [user@untrusted #]$ qvm-connect-tcp 10444:mytcp-service:444



The service of ``mytcp-service`` running on port ``444`` is now
accessible in ``untrusted`` as ``localhost:10444``.

**3. Binding to different qubes using RPC policies**

One can go further than the previous examples by redirecting different
ports to different qubes. For example, let assume that another qube
``mytcp-service-bis`` with a TCP service is running on port ``445``. If
someone wants ``untrusted`` to be able to reach this service but port
``445`` is reserved to ``mytcp-service-bis`` then, in dom0, add the
following to ``/etc/qubes/policy.d/30-user-networking.policy``:

.. code:: bash

      qubes.ConnectTCP +445 untrusted @default allow target=mytcp-service-bis



In that case, calling ``qvm-connect-tcp`` like previous examples, will
still bind TCP port ``444`` of ``mytcp-service`` to ``untrusted`` but
now, calling it with port ``445``

.. code:: bash

      [user@untrusted #]$ qvm-connect-tcp ::445



will restrict the binding to only the corresponding TCP port of
``mytcp-service-bis``.

**4. Permanent port binding**

For creating a permanent port bind between two qubes, ``systemd`` can be
used. We use the case of the first example. In ``/rw/config`` (or any
place you find suitable) of qube ``untrusted``, create
``my-tcp-service.socket`` with content:

.. code:: bash

      [Unit]
      Description=my-tcp-service
      
      [Socket]
      ListenStream=127.0.0.1:444
      Accept=true
      
      [Install]
      WantedBy=sockets.target



and ``my-tcp-service@.service`` with content:

.. code:: bash

      [Unit]
      Description=my-tcp-service
      
      [Service]
      ExecStart=qrexec-client-vm '' qubes.ConnectTCP+444
      StandardInput=socket
      StandardOutput=inherit



In ``/rw/config/rc.local``, append the lines:

.. code:: bash

      cp -r /rw/config/my-tcp-service.socket /rw/config/my-tcp-service@.service /lib/systemd/system/
      systemctl daemon-reload
      systemctl start my-tcp-service.socket



When the qube ``unstrusted`` has started (after a first reboot), you can
directly access the service of ``mytcp-service`` running on port ``444``
as ``localhost:444``.

Port forwarding to a qube from the outside world
------------------------------------------------


In order to allow a service present in a qube to be exposed to the
outside world in the default setup (where the qube has ``sys-firewall``
as network VM, which in turn has ``sys-net`` as network VM) the
following needs to be done:

- In the sys-net VM:

  - Route packets from the outside world to the sys-firewall VM

  - Allow packets through the sys-net VM firewall



- In the sys-firewall VM:

  - Route packets from the sys-net VM to the VM

  - Allow packets through the sys-firewall VM firewall



- In the qube QubeDest:

  - Allow packets through the qube firewall to reach the service





As an example we can take the use case of qube QubeDest running a web
server listening on port 443 that we want to expose on our physical
interface ens6, but only to our local network 192.168.x.y/24.

   Note: To have all interfaces available and configured, make sure the
   3 qubes are up and running

   Note: `Issue #4028 <https://github.com/QubesOS/qubes-issues/issues/4028>`__
   discusses adding a command to automate exposing the port.

**1. Identify the IP addresses you will need to use for sys-net, sys-firewall and the destination qube.**

You can get this information using various methods, but only the first
one can be used for ``sys-net`` outside world IP:

- by running this command in each qube: ``ip -4 -br a | grep UP``

- using ``qvm-ls -n``

- in the Qubes Manager window using the column IP

- from the Settings Window for the qube



Note the IP addresses you will need, they will be required in the next
steps.

   Note: The vifx.0 interface is the one used by qubes connected to this
   netvm so it is *not* an outside world interface.

**2. Route packets from the outside world to the FirewallVM**

For the following example, we assume that the physical interface ens6 in
sys-net is on the local network 192.168.x.y with the IP 192.168.x.n, and
that the IP address of sys-firewall is 10.137.1.z.

In the sys-net VM’s Terminal, the first step is to define an ntables
chain that will receive DNAT rules to relay the network traffic on a
given port to the qube NetVM, we recommend to define a new chain for
each destination qube to ease rules management:

.. code:: bash

   nft add chain qubes custom-dnat-qubeDEST '{ type nat hook prerouting priority filter +1 ; policy accept; }'

.. note:: the name ``custom-dnat-qubeDST`` is arbitrary

.. note::

   while we use a DNAT chain for a single qube, it’s totally
   possible to have a single DNAT chain for multiple qubes

Second step, code a natting firewall rule to route traffic on the
outside interface for the service to the sys-firewall VM

.. code:: bash

   nft add rule qubes custom-dnat-qubeDEST iif == "ens6" ip saddr 192.168.x.y/24 tcp dport 443 ct state new,established,related counter dnat 10.137.1.z

Third step, code the appropriate new filtering firewall rule to allow
new connections for the service

.. code:: bash

   nft add rule qubes custom-forward iif == "ens6" ip saddr 192.168.x.y/24 ip daddr 10.137.1.z tcp dport 443 ct state new,established,related counter accept



.. note:: If you do not wish to limit the IP addresses connecting to the
   service, remove ``ip saddr 192.168.x.y/24`` from the rules

If you want to expose the service on multiple interfaces, repeat the
steps 2 and 3 described above, for each interface. Alternatively, you
can leave out the interface completely.

Verify the rules on sys-net firewall correctly match the packets you
want by looking at its counters, check for the counter lines in the
chains ``custom-forward`` and ``custom-dnat-qubeDEST``:

.. code:: bash

   nft list table ip qubes



In this example, we can see 7 packets in the forward rule, and 3 packets
in the dnat rule:

.. code:: bash

   chain custom-forward {
     iif "ens6" ip saddr 192.168.x.y/24 ip daddr 10.137.1.z tcp dport 443 ct state new,established,related counter packets 7 bytes 448 accept
   }

   chain custom-dnat-qubeDEST {
     type nat hook prerouting priority filter + 1; policy accept;
     iif "ens6" ip saddr 192.168.x.y/24 tcp dport 443 ct state new,established,related counter packets 3 bytes 192 dnat to 10.138.33.59
   }



(Optional) You can send a test packet by trying to connect to the
service from an external device using the following command:

.. code:: bash

   telnet 192.168.x.n 443



Once you have confirmed that the counters increase, store the commands
used in the previous steps in ``/rw/config/qubes-firewall-user-script``
so they get set on sys-net start-up:

.. code:: bash

   [user@sys-net user]$ sudo -i
   [root@sys-net user]# nano /rw/config/qubes-firewall-user-script



Content of ``/rw/config/qubes-firewall-user-script`` in ``sys-net``:

.. code:: bash

   #!/bin/sh

   # create the dnat chain for qubeDEST if it doesn't already exist
   if nft add chain qubes custom-dnat-qubeDEST '{ type nat hook prerouting priority filter +1 ; policy accept; }'
   then
     # create the dnat rule
     nft add rule qubes custom-dnat-qubeDEST iif == "ens6" saddr 192.168.x.y/24 tcp dport 443 ct state new,established,related counter dnat 10.137.1.z

     # allow forwarded traffic
     nft add rule qubes custom-forward iif == "ens6" ip saddr 192.168.x.y/24 ip daddr 10.137.1.z tcp dport 443 ct state new,established,related counter accept
   fi



**3. Route packets from the FirewallVM to the VM**

For the following example, we use the fact that the physical interface
of sys-firewall, facing sys-net, is eth0. Furthermore, we assume that
the target VM running the web server has the IP address 10.137.0.xx and
that the IP address of sys-firewall is 10.137.1.z.

In the sys-firewall VM’s Terminal, add a DNAT chain that will contain
routing rules:

.. code:: bash

   nft add chain qubes custom-dnat-qubeDEST '{ type nat hook prerouting priority filter +1 ; policy accept; }'



Second step, code a natting firewall rule to route traffic on the
outside interface for the service to the destination qube

.. code:: bash

   nft add rule qubes custom-dnat-qubeDEST iif == "eth0" ip saddr 192.168.x.y/24 tcp dport 443 ct state new,established,related counter dnat 10.137.0.xx



Third step, code the appropriate new filtering firewall rule to allow
new connections for the service

.. code:: bash

   nft add rule qubes custom-forward iif == "eth0" ip saddr 192.168.x.y/24 ip daddr 10.137.0.xx tcp dport 443 ct state new,established,related counter accept



.. note:: If you do not wish to limit the IP addresses connecting to the
   service, remove ``ip saddr 192.168.x.y/24`` from the rules

Once you have confirmed that the counters increase, store these commands
in the script ``/rw/config/qubes-firewall-user-script``

.. code:: bash

   [user@sys-net user]$ sudo -i
   [root@sys-net user]# nano /rw/config/qubes-firewall-user-script


Content of ``/rw/config/qubes-firewall-user-script`` in
``sys-firewall``:

.. code:: bash

   #!/bin/sh

   # create the dnat chain for qubeDEST if it doesn't already exist
   if nft add chain qubes custom-dnat-qubeDEST '{ type nat hook prerouting priority filter +1 ; policy accept; }'
   then
     # create the dnat rule
     nft add rule qubes custom-dnat-qubeDEST iif == "eth0" tcp dport 443 ct state new,established,related counter dnat 10.137.0.xx

     # allow forwarded traffic
     nft add rule qubes custom-forward iif == "eth0" ip saddr 192.168.x.y/24 ip daddr 10.137.0.xx tcp dport 443 ct state new,established,related counter accept
   fi



If the service should be available to other VMs on the same system, do
not forget to specify the additional rules described earlier in this
guide.

**4. Allow packets into the qube to reach the service**

No routing is required in the destination qube, only filtering.

For the following example, we assume that the target VM running the web
server has the IP address 10.137.0.xx

The according rule to allow the traffic is:

.. code:: bash

   nft add rule qubes custom-input tcp dport 443 ip daddr 10.137.0.xx ct state new,established,related counter accept



To make it persistent, you need to add this command in the script
``/rw/config/rc.local``:

.. code:: bash

   [user@qubeDEST user]$ sudo -i
   [root@qubeDEST user]# echo 'nft add rule qubes custom-input tcp dport 443 ip daddr 10.137.0.xx ct state new,established,related counter accept' >> /rw/config/rc.local



This time testing should allow connectivity to the service as long
qubeDEST is running and the service is up :-)

Where to put firewall rules
---------------------------


Implicit in the above example :doc:`scripts </user/advanced-topics/config-files>`, but
worth calling attention to: for all qubes *except* those supplying
networking, nftables commands should be added to the
``/rw/config/rc.local`` script. For service qubes supplying networking
(``sys-firewall`` and ``sys-net`` inclusive), nftables commands should
be added to ``/rw/config/qubes-firewall-user-script``.

Firewall troubleshooting
------------------------


Firewall logs are stored in the systemd journal of the qube the firewall
is running in (probably ``sys-firewall``). You can view them by running
``sudo journalctl -u qubes-firewall.service`` in the relevant qube.
Sometimes these logs can contain useful information about errors that
are preventing the firewall from behaving as you would expect.

An effective console utility to troubleshoot network is
`tcpdump <https://www.tcpdump.org/>`__, it can be used to display
network packets entering or leaving network interfaces.

For instance, if you want to check if your network interface ``eth0`` is
receiving packets on port TCP 443 from the network 192.168.x.y, you can
run this command:

.. code:: bash

   tcpdump -i eth0 -nn dst port 443 and src net 192.168.x.y/24



This can be used effectively in a destination qube and its Network VM to
see if forwarding / NAT rules are working.

Nftables tips
-------------


A simple way to experiment changes with your ruleset can be achieved by
saving the current working ruleset in two files, one for backup and the
other for making changes.

By adding ``flush ruleset`` at the top of the file, you can achieve
atomic update, which mean the new ruleset would replace the current one
only if it fully succeed to load.

You can dump the ruleset in two files using the following command:

.. code:: bash

   nft list ruleset | tee nft_backup | tee nft_new_ruleset



Then, edit ``nft_new_ruleset``, add ``flush ruleset`` on top and make
changes, load it with ``nft -f nft_new_ruleset``.

You can revert to the original ruleset with the following commands:

.. code:: bash

   nft flush ruleset && nft -f nft_backup
