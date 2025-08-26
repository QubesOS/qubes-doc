===================
VPN troubleshooting
===================


Tips
----


- If using qubes-vpn, check the VPN service’s log in the VPN VM by running:

  .. code:: console

        $ sudo journalctl -u qubes-vpn-handler



- Always test your basic VPN connection before adding scripts.

- Test DNS: Ping a familiar domain name from an appVM. It should print the IP address for the domain.

- Use ``iptables -L -v`` and ``iptables -L -v -t nat`` to check firewall rules. The latter shows the critical PR-QBS chain that enables DNS forwarding.



VPN does not reconnect after suspend
------------------------------------


This applies when using OpenVPN.

After suspend/resume, OpenVPN may not automatically reconnect. In order to get it to work, you must kill the OpenVPN process and restart it.

VPN stuck at "Ready to start link"
----------------------------------


After setting up OpenVPN and restarting the VM, you may be repeatedly getting the popup “Ready to start link”, but the VPN isn’t connected.

To figure out the root of the problem, check the VPN logs in ``/var/log/syslog`` or use ``journalctl``. The logs may reveal issues like missing OpenVPN libraries, which you can then install.

``notify-send`` induced failure
-------------------------------


`Some VPN guides <https://forum.qubes-os.org/t/configuring-a-proxyvm-vpn-gateway/19061>`__ use complex scripts that include a call to ``notify-send``, yet some images may not contain this tool or may not have it working properly. For instance calling ``notify-send`` on a ``fedora-36`` template VM gives:

.. code:: output

      Failed to execute child process “dbus-launch” (No such file or directory)



To check this tool is working properly run:

.. code:: console

      $ sudo notify-send "$(hostname): Test notify-send OK" --icon=network-idle


You should see the ``info`` message appear on the top of your screen. If that is the case then ``notify-send`` is not the issue. If it is not, and you have an error of some sort you can:

1. Remove all calls to ``notify-send`` from scripts you are using to start VPN

2. Use another template qube that has a working ``notify-send`` or find proper guide and make your current template run ``notify-send`` work properly.


