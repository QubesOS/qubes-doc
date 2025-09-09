=========================
Autostart troubleshooting
=========================


The following instructions are valid for **Qubes OS R4.0 legacy mode** and **Qubes OS R4.1 legacy and UEFI modes**. For **Qubes OS R4.0 in UEFI mode**, there is no GRUB, so manual boot from another operating system is needed.

In several cases, there is a need to prevent ``autostart=True`` for qubes on boot. For example:

- ``sys-usb`` was enabled, but the only keyboard is attached via USB, and the ``qubes.InputKeyboard`` service is disabled.

- A PCI device assigned to an autostarting qube crashes the system (e.g., a GPU or RAID controller card).



To address this, there is a ``qubes.skip_autostart`` option for the kernel command line. You can use it at the grub boot menu.

|grub1.png|

Press the ``E`` key on the first prompt (or your custom prompt). Then, press the down arrow key multiple times to reach the line starting with ``module2``.

|grub2.png|

Append ``qubes.skip_autostart`` to the end of this line (generally after the ``rhgb quiet`` options).

|grub3.png|

Press ``Ctrl+X`` to boot with the edited GRUB entry. The boot will proceed as usual from here, except that no qube will be autostarted.

.. |grub1.png| image:: /attachment/doc/grub1.png
.. |grub2.png| image:: /attachment/doc/grub2.png
.. |grub3.png| image:: /attachment/doc/grub3.png
