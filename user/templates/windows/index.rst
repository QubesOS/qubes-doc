=============
Windows qubes
=============

Like any other unmodified OSes, Windows can be installed in Qubes as an :doc:`HVM </user/advanced-topics/standalones-and-hvms>` domain.

:term:`Qubes Windows Tools (QWT)` are then usually installed to provide integration with the rest of the Qubes system; they also include Xen’s paravirtualized (PV) drivers to increase performance compared to qemu emulated devices. Alternatively, only Xen’s PV drivers can be installed if integration with Qubes isn’t required or if the tools aren’t supported on a given version of Windows. In the latter case, one would have to :ref:`enable networking between two qubes <user/security-in-qubes/firewall:enabling networking between two qubes>` to be able to exchange files with HVMs.

.. warning::

   Windows VMs use a netfront driver that is not hardened against attacks by
   a malicious netback driver. This means that the NetVM to which you connect
   your Windows VMs should be as trusted (or as *untrusted*) as the Windows VM
   itself. As such, it's recommended to create a dedicated firewall NetVM for
   Windows VMs, for example a clone of ``sys-firewall`` named
   ``sys-firewall-windows``. This also allows users to work around the
   following issues until they're fixed:
   `qubes-issues#10459 <https://github.com/QubesOS/qubes-issues/issues/10459>`__,
   `qubes-issues#6829 <https://github.com/QubesOS/qubes-issues/issues/6829>`__.


.. toctree::
   :caption: Windows related documentation
   :maxdepth: 2

   qubes-windows
   qubes-windows-tools
   Create a Gaming HVM in Qubes <https://forum.qubes-os.org/t/create-a-gaming-hvm/19000>
   qubes-windows-migrate
