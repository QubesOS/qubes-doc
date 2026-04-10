=============
Windows qubes
=============

Like any other unmodified OSes, Windows can be installed in Qubes as an :doc:`HVM </user/advanced-topics/standalones-and-hvms>` domain.

:term:`Qubes Windows Tools (QWT)` are then usually installed to provide integration with the rest of the Qubes system; they also include Xen’s paravirtualized (PV) drivers to increase performance compared to qemu emulated devices. Alternatively, only Xen’s PV drivers can be installed if integration with Qubes isn’t required or if the tools aren’t supported on a given version of Windows. In the latter case, one would have to :ref:`enable networking between two qubes <user/security-in-qubes/firewall:enabling networking between two qubes>` to be able to exchange files with HVMs.

.. warning::

   Windows VMs use a netfront driver that is not hardened against attacks by
   a malicious netback driver. This means that the net qube to which you connect
   your Windows VMs should be as trusted (or as *untrusted*) as the Windows VM
   itself.

   It is recommended that you create a dedicated firewall qube for
   Windows VMs, for example a clone of ``sys-firewall`` named
   ``sys-firewall-windows``. This also allows you to work around this
   issues until it is fixed:
   `qubes-issues#6829 <https://github.com/QubesOS/qubes-issues/issues/6829>`__.
   The workaround is to disconnect ``sys-firewall-windows`` from its net qube or
   use the Qubes Firewall to block traffic.

   If you use the Qubes Firewall then it is recommended that you use the
   `qvm-firewall <https://doc.qubes-os.org/en/latest/user/security-in-qubes/firewall.html#how-to-edit-rules-using-qvm-firewall>`__
   utility for this purpose, as it allows you to block ICMP and DNS
   traffic. By default the firewall rules contain an ``accept`` rule at position 0.
   You can delete this rule using ``qvm-firewall QUBE_NAME del --rule-no 0`` , or
   insert a new ``drop`` all rule as rule number 0, using ``qvm-firewall
   QUBE_NAME add --before 0 drop``. If you have customised the firewall
   settings, insert the ``drop`` rule as above.


.. toctree::
   :caption: Windows related documentation
   :maxdepth: 2

   qubes-windows
   qubes-windows-tools
   Create a Gaming HVM in Qubes <https://forum.qubes-os.org/t/create-a-gaming-hvm/19000>
   qubes-windows-migrate
