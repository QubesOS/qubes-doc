### Updating System Firmware

Keeping system firmware up to date is a vital part of system maintenance.
On AMD CPUs, firmware updates are the only way to update the CPU microcode on non-server systems.
On all systems, firmware can have vulnerabilities that must be addressed.

Qubes OS supports updating system firmware in three different ways.
Which one to use depends on the device whose firmware is being updated.

- If a device is attached to a non-dom0 VM, it should be updated using **fwupd**.
  fwupd is included in both Debian and Fedora repositories.
  It requires Internet access to use, but you can use the updates proxy if you
  need to update firmware from an offline VM.

- If a device is attached to dom0, you can also use **fwupd**.  Qubes OS ships
  a modified version of fwupd that does not require Internet access to use.
  Instead, firmware is fetched via qrexec.

- System76 systems use a special update tool which is simpler than fwupd.
  Use the **system76-firmware-cli** command-line tool to update the firmware.

Unfortunately, graphical tools are currently not supported.
