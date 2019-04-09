---
layout: doc
title: Windows gaming hvm
permalink: /doc/windows-gaming-hvm/
---

# Windows gaming HVM

Some information to configure a windows HVM for gaming. 
This is not officially supported, just some community trial & errors

## References

Everythings needed is referenced here

- [Usefull technical details](https://paste.debian.net/1043341/)
- [Reddit thread of what is needed for GPU passthrough](https://www.reddit.com/r/Qubes/comments/9hp3e7/gpu_passthrough_howto/)
- [Solution to have more than 3Go of RAM in the Windows HVM](https://github.com/QubesOS/qubes-issues/issues/4321#issuecomment-423011787)
- [Some old references](https://www.reddit.com/r/Qubes/comments/66wk4q/gpu_passthrough/)

## Prerequise

You have a functional Windows 7 HVM.

The "how to" for this part can be found on the Qubes OS documentation and here: [Usefull github comment](https://github.com/QubesOS/qubes-issues/issues/3585#issuecomment-453200971).

However, few tips:

- Do a backup (clone VM) of the Windows HVM BEFORE starting to install QWT
- The Windows user MUST BE "user"
- Windows 7 Only, do not use Windows 10 or others.

## Hardware

To have a Windows HVM for gaming, you must have:

- A dedicated AMD GPU. By dedicated, it means: it is a secondary GPU, not the GPU used to display dom0. Nvidia GPU are not supported (or maybe with a lot of trick).
- A really fast disk (M.2 disk)
- A lot of RAM
- A dedicated screen

In my case, I use:

- Secondary GPU: AMD RX580
- Primary GPU: Some Nvidia trash, used for dom0
- 32Go of RAM. 16Go of RAM will be dedicated for the Windows HVM
- A fast M.2 disk


## Checklist

Short list of things to do to make the GPU passthrough work:

- In dom0, you edited the file /etc/default/grub to allow PCI hidding for your secondary GPU, and regenerated the grub
- You patched your stubdom-linux-rootfs.gz to allow to have more than 3Go of RAMfor your Windows HVM

## GRUB modification

You must hide your secondary GPU from dom0.
To do that, you have to edit the GRUB.

In a dom0 Terminal, type:

```bash
qvm-pci
```

Then find the devices id for your secondary gpu.

In my case, it is "dom0:0a_00.0" and "dom0:0a_00.1".

Edit /etc/default/grub, and add the PCI hiding 

```
GRUB_CMDLINE_LINUX="....rd.qubes.hide_pci=0a:00.0,0a:00.1 modprobe=xen-pciback.passthrough=1 xen-pciback.permissive"
```

then regenerate the grub 

```bash
grub2-mkconfig -o /boot/grub2/grub.cfg
```

## Patching stubdom-linux-rootfs.gz

Follow the instructions here: [https://github.com/QubesOS/qubes-issues/issues/4321#issuecomment-423011787](https://github.com/QubesOS/qubes-issues/issues/4321#issuecomment-423011787)

Copy-paste of the comment:

```
This is caused by the default TOLUD (Top of Low Usable DRAM) of 3.75G provided by qemu not being large enough to accommodate the larger BARs that a graphics card typically has.
The code to pass a custom max-ram-below-4g value to the qemu commandline does exist in the libxl_dm.c file of xen, but there is no functionality in libvirt to addthis parameter.
It is possible to manually add this parameter to the qemu commandline by doing the following in a dom0 terminal:

```bash
mkdir stubroot
cp /usr/lib/xen/boot/stubdom-linux-rootfs stubroot/stubdom-linux-rootfs.gz
cd stubroot
gunzip stubdom-linux-rootfs.gz
cpio -i -d -H newc --no-absolute-filenames < stubdom-linux-rootfs
rm stubdom-linux-rootfs
nano init3
```

Before the line "# $dm_args and $kernel are separated withx1b to allow for spaces in arguments." add:

```bash
SP=$'\x1b'
dm_args=$(echo "$dm_args"\
sed"s/-machine\\${SP}xenfv/-machine\
\\${SP}xenfv,max-ram-below-4g=3.5G/g")
```
Then execute:

```bash
find . -print0 | cpio --null -ov\
--format=newc | gzip -9 > ../stubdom-linux-rootfs
sudo mv ../stubdom-linux-rootfs /usr/lib/xen/boot/
```


Note that this will apply the change to all HVMs, so if you have any other HVM with more than 3.5G ram assigned,
they will not start without the adapter being passed through.
Ideally to fix this libvirt should be extended to pass the max-ram-below-4g parameter through to xen,
and then a calculation added to determine the correct TOLUD based on the total BAR size of the PCI devices
are being passed through to the vm.

## Pass the GPU

In qubes settings for the windows HVM, go to the "devices" tab, pass the ID corresponding to your AMD GPU.
(in my case, it was 0a:00.0 and 0a:00.1)

And check the option for "nostrictreset" for those 

##  Conclusion

Don’t forget to install the GPU drivers, you can install the official one from AMD website, no modification or trick to do.

Nothing else is required to make it work (in my case at least, once I finish to fight to find those informations).

If you have issues, you can refer to the links in the first sections. 

If it doesn’t work and you need to debug more things, you can go deeper.

- Virsh (start, define, ...)
- /etc/libvirt/libxl/
- xl
- /etc/qubes/templates/libvirt/xen/by-name/
- /usr/lib/xen/boot/
- virsh -c xen:/// domxml-to-native xen-xm /etc/libvirt/libxl/...

I am able to play games on my windows HVM with very good performances. And safely.

## Bugs

The AMD GPUs have a bug when used in HVM: each time you will reboot your windows HVM, it will get slower and slower.
It is because the AMD GPUs is not correctly resetted when you restart your windows HVM.

Two solutions for that:
- Reboot your computer
- In the windows HVM, use to windows option in the system tray to "safely remove devices", remove your GPU. Restart the HVM.

This bug is referenced somewhere, but lost the link TODO
