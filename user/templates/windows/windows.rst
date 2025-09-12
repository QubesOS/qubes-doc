=============
Windows qubes
=============


Like any other unmodified OSes, Windows can be installed in Qubes as an :doc:`HVM </user/advanced-topics/standalones-and-hvms>` domain.

Qubes Windows Tools (QWT) are then usually installed to provide integration with the rest of the Qubes system; they also include Xen’s paravirtualized (PV) drivers to increase performance compared to qemu emulated devices. Alternatively, only Xen’s PV drivers can be installed if integration with Qubes isn’t required or if the tools aren’t supported on a given version of Windows. In the latter case, one would have to :ref:`enable inter-VM networking <user/security-in-qubes/firewall:enabling networking between two qubes>` to be able to exchange files with HVMs.

For more information about Windows VMs in Qubes OS, please see the following external resources:

- :doc:`Installing and Using Windows-based VMs </user/templates/windows/qubes-windows>`

- :doc:`Installing and Using Qubes Windows Tools </user/templates/windows/qubes-windows-tools>`

- `Create a Gaming HVM in Qubes <https://forum.qubes-os.org/t/create-a-gaming-hvm/19000>`__

- :doc:`Migrate Windows qubes from old Qubes versions </user/templates/windows/qubes-windows-migrate>`
