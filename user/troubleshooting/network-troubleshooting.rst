=======================
Network troubleshooting
=======================


A qube reaches the network through a chain of other qubes:

::

   your qube  →  sys-firewall  →  sys-net  →  outside


``sys-net`` holds the network card and ``sys-firewall`` applies the firewall
rules. Check each hop in turn, starting from your qube.

Run the commands inside the qube being checked, except where marked "in dom0".


Find the chain
--------------


In dom0, ``qvm-ls --format network`` shows every qube with its net qube, IP, and
gateway. A qube with no net qube (shown as ``-``) has no network. If it should
be online, give it one:

.. code:: console

      $ qvm-prefs <qube> netvm sys-firewall


Check the affected qube
-----------------------


.. code:: console

      $ ip -4 addr
      $ ip route


Expect an address in ``10.137.0.0/16`` and a default route through the gateway.
Then test routing and DNS:

.. code:: console

      $ ping -c3 9.9.9.9
      $ host qubes-os.org


Ping working but ``host`` failing means a DNS problem. If both fail, check the
next qube in the chain.

The qube's address, gateway, and DNS servers come from QubesDB:

.. code:: console

      $ qubesdb-read /qubes-ip
      $ qubesdb-read /qubes-gateway
      $ qubesdb-read /qubes-primary-dns


Empty values mean the net qube gave this qube no configuration; check that net
qube. ``/etc/resolv.conf`` comes from the DNS values unless you have listed it
in ``/etc/qubes/protected-files.d``, where a stale entry can break DNS.


Check sys-firewall
------------------


.. code:: console

      $ sudo systemctl status qubes-firewall
      $ sudo nft list ruleset


The firewall and NAT rules are in the nftables ruleset, not ``iptables``.
Forwarding must be on (``cat /proc/sys/net/ipv4/ip_forward`` prints ``1``). List
a qube's own rules in dom0 with ``qvm-firewall <qube> list``.


Check sys-net
-------------


.. code:: console

      $ sudo systemctl status qubes-network-uplink@eth0
      $ ip -4 addr
      $ ping -c3 9.9.9.9


``sys-net`` should have an address from your router or modem. The uplink
interface is usually ``eth0``; use the name from ``ip addr`` if it differs.
NetworkManager manages Wi-Fi and most wired links:

.. code:: console

      $ nmcli device
      $ nmcli device wifi list


If ``sys-net`` cannot reach the outside, the cause is usually the network card,
its driver, or its firmware. See
:ref:`PCI troubleshooting <user/troubleshooting/pci-troubleshooting:network adapter does not work>`
and :doc:`hardware troubleshooting </user/troubleshooting/hardware-troubleshooting>`.


Reporting a problem
-------------------


Include the Qubes version (``cat /etc/qubes-release`` in dom0), the templates of
the qubes in the chain (``qvm-prefs <qube> template``), and the output of the
checks above for each qube.

.. warning::

   This output can contain your public IP address, Wi-Fi network name, MAC
   addresses, and qube names. Remove anything sensitive before posting it
   publicly.
