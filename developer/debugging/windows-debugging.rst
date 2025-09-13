=================
Windows debugging
=================


Debugging Windows code can be tricky in a virtualized environment. The guide below assumes Qubes 4.2 and Windows 7 or later VMs.

User-mode debugging is usually straightforward if it can be done on one machine. Just duplicate your normal debugging environment in the VM.

Things get complicated if you need to perform kernel debugging or troubleshoot problems that only manifest on system boot, user logoff or similar. For that you need two Windows VMs: the *host* and the *target*. The *host* will contain the debugger, your source code and private symbols. The *target* will run the code being debugged. We will use kernel debugging over network which is supported from Windows 7 onwards. The main caveat is that Windows kernel supports only specific network adapters for this, and the default one in Qubes won’t work.

Important note
--------------


- Do not install Xen network PV drivers in the target VM. Network kernel debugging needs a specific type of NIC or it won’t work, the network PV drivers interfere with that.

- If you have kernel debugging active when the Xen PV drivers are being installed, make sure to disable it before rebooting (``bcdedit /set debug off``). You can re-enable debugging after the reboot. The OS won’t boot otherwise. I’m not sure what’s the exact cause. I know that busparams for the debugging NIC change when PV drivers are installed (see later), but even changing that accordingly in the debug settings doesn’t help – so it’s best to disable debug for this one reboot.



Modifying the NIC of the target VM
----------------------------------


You will need to create a :external:doc:`custom libvirt config <libvirt>` for the target VM. The following assumes the target VM is named ``target-vm``.

- Edit ``/usr/share/qubes/templates/libvirt/xen.xml`` to prepare our custom config to override just the NIC part of the global template:

  - add ``{% block network %}`` before ``{% if vm.netvm %}``

  - add ``{% endblock %}`` after the matching ``{% endif %}``



- Copy ``/usr/share/qubes/templates/libvirt/devices/net.xml`` to ``/etc/qubes/templates/libvirt/xen/by-name/target-vm.xml``.

- Add ``<model type='e1000'/>`` to the ``<interface>`` section.

- Enclose everything within ``{% block network %}`` + ``{% endblock %}``.

- Add ``{% extends 'libvirt/xen.xml' %}`` at the start.

- The final ``target-vm.xml`` should look something like this:



.. code:: xml+jinja


      {% extends 'libvirt/xen.xml' %}
      {% block network %}
         <interface type='ethernet'>
            <mac address="{{ vm.mac }}" />
            <ip address="{{ vm.ip }}" />
            <backenddomain name="{{ vm.netvm.name }}" />
            <script path='vif-route-qubes' />
            <model type='e1000' />
         </interface>
      {% endblock %}




- Start ``target-vm`` and verify in the device manager that a “Intel PRO/1000 MT” adapter is present.



Host and target preparation
---------------------------


- On ``host-vm`` you will need WinDbg, which is a part of the `Windows SDK <https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/>`__.

- Copy the ``Debuggers`` directory from Windows SDK to ``target-vm``.

- In both ``host-vm`` and ``target-vm`` switch the windows network to private (it tends to be public by default).

- Either turn off the windows firewall or enable all ICMP-in rules in both VMs.

- In ``firewall-vm`` edit ``/rw/config/qubes-firewall-user-script`` to connect both Windows VMs, add:

  - ``iptables -I FORWARD 2 -s <target-vm-ip> -d <host-vm-ip> -j ACCEPT``

  - ``iptables -I FORWARD 2 -s <host-vm-ip> -d <target-vm-ip> -j ACCEPT``

  - run ``/rw/config/qubes-firewall-user-script`` so the changes take effect immediately



- Make sure both VMs can ping each other.

- In ``target-vm``:

  - start elevated ``cmd`` session

  - ``cd sdk\Debuggers\x64``

  - ``kdnet`` should show that the NIC is supported, note the busparams:

    .. code:: text

          Network debugging is supported on the following NICs:
          busparams=0.6.0, Intel(R) PRO/1000 MT Network Connection, KDNET is running on this NIC.



  - ``bcdedit /debug on``

  - ``bcdedit /dbgsettings net hostip:<host-vm-ip> port:50000 key:1.1.1.1`` (you can customize the key)

  - ``bcdedit /set "{dbgsettings}" busparams x.y.z`` (use the busparams ``kdnet`` has shown earlier)



- In ``host-vm`` start WinDbg: ``windbg -k net:port=50000,key=1.1.1.1``. It will listen for target’s connection.

- Reboot ``target-vm``, debugging should start:

  .. code:: text

        Waiting to reconnect...
        Connected to target 10.137.0.19 on port 50000 on local IP 10.137.0.20.
        You can get the target MAC address by running .kdtargetmac command.
        Connected to Windows 10 19041 x64 target at (Thu Aug  3 14:05:48.069 2023 (UTC + 2:00)), ptr64 TRUE





Happy debugging!
