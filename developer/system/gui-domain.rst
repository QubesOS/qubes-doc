=========================
GUI domain implementation
=========================

This page describes how a GUI domain works under the hood.
To set one up, see :doc:`GUI domain </user/advanced-topics/gui-domain>`.

A GUI domain is a qube with the ``guivm`` service.
It shows the qubes whose ``guivm`` property names it.

Backlight and power supply
--------------------------

dom0 owns the backlight and the power supplies of the computer, its battery and charger.
The GUI domain gets a copy of each as a device of its own, so its desktop tools use them as on any computer.
Two components do it, ``dummy-backlight`` for the backlight and ``dummy-psu`` for the power supplies, each with a dom0 part, a GUI domain part and a kernel module that comes with the Qubes kernel.

Backlight
^^^^^^^^^

1. With the ``dummy-backlight`` service on, ``module-load-dummy-backlight.service`` loads the ``dummy_backlight`` module in the GUI domain, a backlight device whose maximum brightness is 100.
2. The desktop changes its brightness as for a real backlight, for example ``xfce4-power-manager`` or the brightness keys.
3. At each change, a udev rule runs ``qubes-set-backlight.sh``, which calls ``qubes.SetBrightness+<value>`` in dom0 with the new brightness in percent.
4. In dom0, ``qubes.SetBrightness`` checks that the value is a number up to 100, then writes the same share of ``max_brightness`` to the device in ``/sys/class/backlight``.

dom0 runs qrexec services as the first member of group ``qubes``, not as root.
So a udev rule of the dom0 part gives the ``brightness`` file to group ``qubes``, writable, when the device appears.

The brightness only goes from the GUI domain to dom0: a change made in dom0 does not show in the GUI domain.
``xfce4-power-manager`` looks for a backlight when it starts, so a module loaded during a session is used from the next one.

Power supply
^^^^^^^^^^^^

1. With the ``dummy-psu`` service on, ``module-load-dummy-psu.service`` loads the ``dummy_psu`` module in the GUI domain, which provides ``/dev/dummy_psu``.
2. ``qubes-psu-client@default.service`` calls ``qubes.PowerSupply`` in dom0 and keeps the call open.
3. In dom0, ``qubes.PowerSupply`` writes the properties of each device in ``/sys/class/power_supply`` as one JSON line, again at least every 10 seconds and at each udev ``change`` event of the ``power_supply`` subsystem.
4. The client creates and updates the same devices in the GUI domain through ``ioctl`` calls on ``/dev/dummy_psu``, so ``upower`` and the panel show the battery and the charger of the computer.

Packages and setup
^^^^^^^^^^^^^^^^^^

- dom0: ``dummy-backlight-dom0`` and ``dummy-psu-sender``.
- Template of the GUI domain: ``dummy-backlight-vm`` and ``dummy-psu-receiver``. A GUI domain with a kernel of its own also needs ``dummy-backlight-module`` and ``dummy-psu-module``, which build the modules with DKMS.

The GUI domain also needs its ``dummy-backlight`` and ``dummy-psu`` services on, and a qrexec policy that allows ``qubes.SetBrightness`` and ``qubes.PowerSupply`` from it to dom0.
A qube reads its services when it starts, so a change to them applies at the GUI domain's next start.

System shutdown
---------------

A person in a GUI domain shuts down, restarts or suspends the computer from the desktop session, as in dom0.
On its own, the session would only stop or suspend the GUI domain: systemd-logind runs in the GUI domain, not in dom0.
So the GUI domain forwards these requests to dom0, and dom0 marks the shutdowns it starts itself, so that the GUI domain does not forward them back.

It has three parts:

- ``qubes-guivm-power-forward`` in the GUI domain (``qubes-desktop-linux-common-guivm``), a service started when the ``guivm`` service is on.
- The dom0 services ``qubes.PowerShutdown``, ``qubes.PowerReboot`` and ``qubes.PowerSuspend`` (``qubes-core-dom0-linux``), which run ``systemctl poweroff``, ``systemctl reboot`` and ``systemctl suspend`` in dom0.
- The GUI extension of qubesd (``qubes-core-dom0``), which writes ``/qubes-shutdown-requested`` in the QubesDB of a GUI domain that dom0 shuts down.

Shutdown or restart from the session
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. ``qubes-guivm-power-forward`` holds a logind ``delay`` inhibitor on ``shutdown``.
2. The person chooses to shut down or restart, and logind emits ``PrepareForShutdownWithMetadata`` with the type ``poweroff``, ``halt`` or ``reboot``.
3. If ``/qubes-shutdown-requested`` is not in the GUI domain's QubesDB, the forwarder calls ``qubes.PowerShutdown`` (for ``poweroff`` and ``halt``) or ``qubes.PowerReboot`` (for ``reboot``) in dom0.
4. The forwarder releases the inhibitor and the GUI domain goes on with its own shutdown.
5. If the qrexec policy allows the call, dom0 shuts down or restarts the computer, which stops the remaining qubes.

The forwarder waits at most 3 seconds for the call, below the 5 seconds logind waits for a delay inhibitor (``InhibitDelayMaxSec``).
If logind cancels the shutdown, the forwarder takes the inhibitor again for the next one.

Shutdown started by dom0
^^^^^^^^^^^^^^^^^^^^^^^^

dom0 shuts down a GUI domain with ``qvm-shutdown``, or while dom0 itself shuts down.
The GUI domain then stops as any other qube, and logind emits the same signal.
Without a mark, the forwarder would take it for a request of the person, and stopping ``sys-gui`` would power off the computer.

1. On ``domain-pre-shutdown``, the GUI extension refuses to shut down a GUI domain while qubes it shows are running, unless the shutdown is forced.
2. Once it accepts the shutdown of a qube with the ``guivm`` service, it writes ``/qubes-shutdown-requested`` in that qube's QubesDB.
3. The forwarder reads it and calls nothing in dom0.
4. On ``domain-shutdown-failed``, the extension removes the mark, so that a later shutdown from the session is forwarded again.

The mark is in the GUI domain's own QubesDB, and it only decides whether that GUI domain skips its own forwarding.

Suspend from the session
^^^^^^^^^^^^^^^^^^^^^^^^

In a GUI domain, ``systemd-suspend.service`` would suspend the GUI domain alone and freeze its session.
A drop-in replaces its command with ``qubes-guivm-suspend``, which calls ``qubes.PowerSuspend`` in dom0 instead.

When dom0 suspends, it calls ``qubes.SuspendPreAll`` and ``qubes.SuspendPre`` in each running qube, then suspends or pauses the qube through libvirt.
The qube's own ``systemd-suspend.service`` is not on that path, so the GUI domain sends nothing back.
In case it runs anyway, a script in ``/etc/qubes/suspend-pre.d`` creates ``/var/run/qubes-suspend-requested`` in the GUI domain, and while that file exists, ``qubes-guivm-suspend`` suspends the GUI domain itself.
``qubes.SuspendPostAll`` removes the file after the resume.

Policy
^^^^^^

``90-sys-gui-power.policy`` denies the three services to every qube.
A GUI domain that may power the computer needs rules that allow them from it to dom0, in a policy file read before this one.

A GUI domain without such rules only stops itself on a shutdown or restart from its session, and a suspend from its session fails and leaves it running.

Cases
^^^^^

The forwarder only sees what goes through logind, so a command that bypasses logind stops the GUI domain alone.

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Action
     - Result
   * - Shut down, restart or suspend in the session menu (logind ``PowerOff``, ``Reboot``, ``Suspend``)
     - ``qubes.PowerShutdown``, ``qubes.PowerReboot`` or ``qubes.PowerSuspend`` in dom0
   * - ``poweroff`` or ``halt`` in the GUI domain
     - ``qubes.PowerShutdown``
   * - ``reboot``, ``systemctl reboot`` or ``shutdown -r now`` in the GUI domain
     - ``qubes.PowerReboot``
   * - ``shutdown -r +1`` in the GUI domain
     - ``qubes.PowerReboot`` when the scheduled shutdown starts, not when it is scheduled
   * - ``systemctl suspend`` in the GUI domain
     - ``qubes.PowerSuspend``, the GUI domain keeps running
   * - ``reboot -f``, ``reboot -ff`` or ``systemctl start reboot.target`` in the GUI domain
     - Nothing in dom0, only the GUI domain stops
   * - ``qvm-shutdown`` of the GUI domain in dom0, or dom0 shutting down
     - Nothing forwarded, the mark is set
   * - dom0 suspending
     - Nothing forwarded
   * - Any of the above in a GUI domain without the grant
     - Shutdown or restart stops the GUI domain alone, suspend fails and leaves it running
   * - Any of the above in a qube without the ``guivm`` service
     - Nothing forwarded, the qube handles it alone as before

For now, dom0 does not start a qube again when it restarts itself (`#8196 <https://github.com/QubesOS/qubes-issues/issues/8196>`__), so after a forwarded restart, the GUI domain stays halted until the computer has restarted.
Without the drop-in, a suspend from the session suspended the GUI domain alone and left it frozen, with no way back from the screen (`#9384 <https://github.com/QubesOS/qubes-issues/issues/9384>`__).
