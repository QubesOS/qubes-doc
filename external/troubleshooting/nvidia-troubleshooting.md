---
layout: doc
title: Nvidia Troubleshooting
permalink: /doc/nvidia-troubleshooting/
redirect_from:
- /en/doc/nvidia-troubleshooting/
- /doc/NvidiaTroubleshooting/
- /wiki/NvidiaTroubleshooting/
---

# Nvidia Troubleshooting Guide

## System freezes during boot / Graphical login manager is not visible

If you have an NVidia graphics card it will probably not work under Xen out of the box. If your system freezes during boot and you don't see the graphical login manager after you installed Xen, then this problem most likely affects you. The following steps should provide a workaround so that you should be able to use your NVidia with X under Xen, however without any fancy "desktop effects".

### Boot in failsafe

Boot your system using the "failsafe" boot menu, that should have been automatically added to your `grub.conf` when you installed the Dom0 kernel.

If the X Window System doesn't start now, this is probably a non-Xen related issue and this guide will probably not help you.


### Configure X with nouveau

Assuming your X Window System works fine now when you booted from the "failsafe" configuration, do the next steps...

 1. Do not log into X, but instead switch to a text console (press Ctrl-Alt-F2)

 2. Log in as root

 3. Switch to runlevel 3 (this should kill your X server):

    ~~~
    init 3
    ~~~

 4. Run X-autoconfiguration:

    ~~~
    Xorg -configure
    ~~~

    This should generate a file `xorg.conf.new` in the `/root` directory.

    In most cases you can ignore any warning or error messages displayed by the X server, assuming it generated the xorg.conf.new file.

 5. Edit this newly generated `xorg.conf.new` file and introduce the following two modifications:

    First, uncomment the ShadowFB option, so that you should now have something like this:

    ~~~
    Option     "ShadowFB"                   # [<bool>]
    ~~~

    Second, change the driver name to `nouveau` (you will probably have `nv` written there):

    ~~~
    Driver      "nouveau"
    ~~~

    Save the modification, exit the editor.

 6. Move the file to `/etc/X11` and rename it as `xorg.conf`:

    ~~~
    mv /root/xorg.conf.new /etc/X11/xorg.conf
    ~~~

 7. Verify that X will work with those new settings:

    ~~~
    xinit
    ~~~

    If you see a terminal window in the top left corner, it means you most likely succeeded, even if your keyboard or mouse do not work now (don't worry about them).

 8. Reboot and let the system boot from the normal boot configuration. You should be able to use X under Xen now.

## Boot failure after GRUB menu / System freezes followed by reboot

If Qubes fails to properly boot after the GRUB Boot menu and you are stuck on a black screen that displays messages starting with `nouveau` then it means that the nouveau driver failed to launch properly.

One way to get rid of this for now is to disable nouveau.

### Disabling Nouveau

Example error:

~~~
nouveau E[ PGRAPH][0000:01:00.0] grctx template channel unload timeout
nouveau E[ PGRAPH][0000:01:00.0] failed to construct context
nouveau E[ PGRAPH][0000:01:00.0] init failed, -16
~~~

Tip: In case you only have an external monitor it is advised to attach it directly to a connector of the motherboard if it is present, this should ensure that you're using the integrated graphics card instead of the nvidia graphics card.

If you're seeing this error then that means another graphics card (most likely an integrated one) acted as failsafe. Disabling nouveau has the consequences of disabling nvidia support altogether.

#### EFI

 1. Open a terminal in dom0.

 2. To edit the `xen.cfg` file using the `nano` editor:

    ~~~ 
    sudo nano /boot/efi/EFI/qubes/xen.cfg
    ~~~

 3. Locate the three `kernel=` lines. Press the left/right arrow keys to position the cursor at the end of the lines, after `rhgb quiet`.

 4. Add the following:

    ~~~
    nouveau.modeset=0 rd.driver.blacklist=nouveau video=vesa:off
    ~~~

    This will disable nouveau until the option is manually edited back to its original state.

 5. Press the `Ctrl+X` keys, then `y` to save changes. 
   
 6. Reboot 

#### GRUB

 1. Verify that that GRUB Boot Menu is displaying, you should be presented with two options and a progressbar/timer than goes rather fast.

    ~~~
    Qubes
    Qubes with advanced Xen options
    ~~~

 2. Quickly press the "E" key before the time is up.

 3. An editor will open up that allows you to temporarily change the grub options for the next boot.

 4. Press the down arrow key and move the cursor to the line after the line with the kernel options. The line with the kernel options will look like this:

    ~~~
    module /vmlinux-4.1.13-9.pvops.qubes.x86_64 placeholder root=/dev/mapper/qubes_dom0-root ro ... rhgb quiet
    ~~~
    
    It is not an exact copy as it may differ from system to system.

    Please note: choose the module that starts with `vmlinux`!

 5. Press the left/right arrow keys to position the cursor at the end of kernel options line, after `rhgb quiet` in this case.

 6. Add the following:

    ~~~
    nouveau.modeset=0 rd.driver.blacklist=nouveau video=vesa:off
    ~~~

    This will temporarily disable nouveau until next boot.

 7. Press either the F10 key or Ctrl+X to start the boot process.

    Qubes should now boot properly, if that's the case then we should make this change permanent such that the GRUB config knows to not run nouveau.

You'll have to do the following to make this change persistent, so that it will work properly on every boot :

 1. Open a terminal (do this by clicking on Q > 'run command' > type 'terminal' and hit enter)

 2. type following commands:

    ~~~
    cd /etc/default/
    sudo nano grub
    ~~~

 3. Edit `GRUB_CMDLINE_LINUX`, add the following to it at the end:

    ~~~
    nouveau.modeset=0 rd.driver.blacklist=nouveau video=vesa:off
    ~~~

 4. ctrl + X and then y to save the file.

 5. The final step is to compile the configuration file to something the bootloader can read.

    ~~~
    sudo grub2-mkconfig -o /boot/grub2/grub.cfg
    ~~~

## Lack of video output during Nvidia driver installation

Specifically, the notes below are aimed to help when during Nvidia driver installation, the GRUB menu shows up fine, the installation environment starts loading, and then the display(s) go into standby mode. This is, typically, related to some sort of an issue with the kernel's KMS/video card modules.

### Initial setup.
*Note*: The steps below do *not* produce a fully-functional Qubes OS install. Rather, only a dom0 instance is functional, and there is no networking there. However, they can be used to gather data in order to troubleshoot video card issues and/or possible other basic kernel module issues.

1. Append `nomodeset ip=dhcp inst.nokill inst.vnc` to the kernel command line. Remove `rhgb` and `quiet` to see the kernel messages scroll by, which may help in further diagnostics.
   * If DHCP is not available on the installation network, the syntax becomes a bit more involved. The full list of variants is documented in the [Dracut Command-line parameters] (http://man7.org/linux/man-pages/man7/dracut.cmdline.7.html)
2. The VGA console should switch into the installer's multi-virtual-terminal display. VNC may take a number of minutes to start, please be patient.
   * Using the anaconda installer interface, switch to the "shell" TTY (ALT-F2), and use `ip a` command to display the IP addresses.
3. Using the Connect to the IP (remember the :1) using a VNC viewer.
4. Follow the installation UI. 
   * Since this won't be a usable install, skipping LUKS encryption is an option which will simplify this troubleshooting process.
   * Do *not* reboot at the end of the installation.
5. Once the installation completes, use the local VGA console switch to TTY2 via ALT-F2
   * Switch to the chroot of the newly-installed system via `chroot /mnt/sysinstall`
   * Set the root password (this will also enable the root account login)
   * Double-check that `/boot/grub2/grub.cfg` contains a `nomodeset` kernel parameter.
   * Exit out of the chroot environment (`exit` or CTRL-D)
6. Reboot

*Note* If the kernel parameters do *not* include `quiet` and `rhgb`, the kernel messages can easily obscure the LUKS passphrase prompt. Additionally, each character entered will cause the LUKS passphrase prompt to repeat onto next line. Both of these are cosmetic. The trade-off between kernel messages and the easy-to-spot LUKS passphrase prompt is left as an exercise to the user.

### Gather initial `dmesg` output
If all is well, the newly-installed Qubes OS instance should allow for user root to log in. 
Run `dmesg > dmesg.nomodeset.out` to gather an initial dmesg output.

### Gather the 'video no worky' `dmesg` output
1. Reboot and interrupt the Grub2's process, modifying the kernel parameters to no longer contain `nomodeset`.
   * If the LUKS passphrase was set, blindly enter it.
2. Wait for the system to finish booting (about 5 minutes, typically).
3. Blindly switch to a TTY via CTRL-ALT-F2.
4. Blindly log in as user root
5. Blindly run `dmesg > dmesg.out`
6. Blindly run `reboot` (this will also serve to confirm that logging in as root, and running commands blindly is possible rather than, say, the kernel having hung or some such).
   * Should this step fail, perhaps by the time step #3 was undertaken, the OS hasn't finished coming up yet. Please retry, possibly with a different TTY (say, 3 or 4 - so CTRL-ALT-F3?)

### Exfiltrate the dmesg outputs
Allow the system to boot normally, log in as user root, and sneakernet the files off the system for analysis, review, bug logging, et cetera.
