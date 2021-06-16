---
lang: en
layout: doc
redirect_from:
- /doc/gui-troubleshooting/
ref: 233
title: GUI Troubleshooting
---


## Can't click on anything after connecting 4k external display

When you connect a 4K external display, you may be unable to click on anything but a small area in the upper-right corner.

When a qube starts, a fixed amount of RAM is allocated to the graphics buffer called video RAM.
This buffer needs to be at least as big as the whole desktop, accounting for all displays that are or will be connected to the machine.
By default, it is as much as needed for the current display and an additional full HD (FHD) display (1920×1080 8 bit/channel RGBA).
This logic fails when the machine has primary display in FHD resolution and, after starting some qubes, a 4K display is connected.
If the buffer is too small, and internal desktop resize fails.

The solution to this problem is to increase the minimum size of the video RAM buffer, as explained in [GUI Configuration](/doc/gui-configuration/#video-ram-adjustment-for-high-resolution-displays).

## Screen blanks / Weird computer glitches like turning partially black or black boxes

You may encountering seemingly random screen blanking while using Qubes, where the screen will black and shows the logon screen, yet, only the active window will show when you move the mouse or use the keyboard. Sometimes, you will get random black screens or black boxes.

Similarly, while working, the XScreenSaver dialog may pop up (indicating the screen is locked) and the screen goes black. However, the screen is not locked, and you have to move a window to redraw the screen.

If you are experiencing the any of the above symptoms, try disabling the window compositor:

`
    Q → System Tools → Window Manager Tweaks → Compositor → uncheck “Enable display compositing”
`

## Post installation, screen goes black and freezes following LUKS decryption

After installing Qubes, you may experience a black screen after entering your LUKS decryption password.
To fix the problem, use your preferred text editor (`nano` works) to edit `/mnt/sysimage/boot/efi/EFI/qubes/xen.cfg`, adding the `efi=no-rs` option to the end of the `options= line`. For example:

~~~
[4.14.18-1.pvops.qubes.x86_64]
options=loglvl=all dom0_mem=min:1024M dom0_mem=max:4096M iommu=no-igfx ucode=scan efi=no-rs
~~~

Note that the `/mnt/sysimage/boot/efi/EFI/qubes/xen.cfg` path applies when running from the installer (either directly after installation, before the reboot, or by starting the installer again in recovery mode). On the actual installed system, the file to edit is `/boot/efi/EFI/qubes/xen.cfg` -- but it may be hard to access directly when your system won't boot.

## Can start VM, but can't launch any applications

If you can start your VM, but can't launch any applications, then you need to fix the issues from the `VM console`, accessible from xen through:

```sh
qvm-start <VMname> # Make sure the VM is started
qvm-console-dispvm <VMname>
```

After launching a VM console using `qvm-console-dispvm`, you may look at the `qubes-gui-agent` service state with:

~~~
systemctl status -l qubes-gui-agent
~~~

If the service is in a failed state, you should see some messages on why it failed.

Another helpful place to look into is `/home/user/.xsession-errors`, which may also contain some hints what is wrong.

### Disable audited messages

During troubleshooting, you may be getting a lot of 'audit' messages which make the log very noisy.
To disable audited messages, you need to edit your VM kernel parameters:

```sh
previous_kernel_parameters=$(qvm-prefs --get <VMname> kernelopts) # Get current kernel parameters
qvm-prefs --set <VMname> kernelopts "<previous_kernel_parameters> audit=0"
```

Then, restart your VM.

Once your troubleshooting is done, don't forget to remove this kernel parameters, it makes troubleshooting VMs not starting easier.
