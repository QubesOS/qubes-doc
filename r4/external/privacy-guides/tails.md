---
layout: doc
title: Running Tails in Qubes
redirect_from:
- /doc/tails/
- /doc/running-tails
---

Running Tails in Qubes
============================

[Tails](https://tails.boum.org) stands for The Amnesic Incognito Live System. 
It is a live operating system that aims to preserve your privacy and anonymity. 
Tails is intended to be booted off of a live CD and leave no trace on the computer it is run on, but using Tails this way requires the user to restart their computer every time they want to switch from their installed OS to Tails. 
Despite this, in case that method becomes cumbersome, Tails can be used inside virtualization software and Qubes.

To run Tails under Qubes:

1.  Read about [creating and using HVM qubes](/doc/hvm/)

2.  Download and verify Tails from [https://tails.boum.org](https://tails.boum.org) in a qube, (saved as `/home/user/Downloads/tails.iso` on qube "isoVM" for purposes of this guide).

3.  Create a HVM

    - In Manager, click "VM menu" and select "Create VM"
    - Name the new qube - "Tails"
    - Select "HVM"
    - Set "initial memory" and "max memory" as the same ([official documentation](https://tails.boum.org/doc/about/requirements/index.en.html) recommends at least 2048 MB)
    - Configure networking
    - Click "OK" to create new HVM.

4.  Open dom0 Konsole and start Tails:

        qvm-start Tails --cdrom=isoVM:/home/user/Downloads/tails.iso

5.  Configure Tails at start up.

6.  Once the Tails qube has started, configure networking in the qube.

    -  Check the IP address allocated to the qube - either from GUI Manager, or ```qvm-ls -n Tails``` in Konsole. (E.g. `10.137.1.101` with gateway `10.137.1.1`)
    -  In the Tails qube, open systems menu in top-right corner. Select "Wired Settings", and change  IPv4 configuration from "Automatic (DHCP)" to "Manual".
    -  Enter the Address:   `10.137.1.101`  in our example.
    -  Enter the Netmask:   `255.255.255.0`
    -  Enter the Gateway:   `10.137.1.1`  in our example.
    -  Enter DNS:           `10.137.1.1`  in our example.
    -  Click "Apply". You should now see "Connected".

7.  Use Tails as normal.

## Usage Notes

### Display issues:
**Black screen on start up.**

This was reported with earlier versions of Tails: The problem should now be fixed.
If you do encounter this problem, you can try to constrain display settings by appending vga codes to the Tails boot parameters.
(If you do not know the codes, append `vga=999`, and a helpful prompt will appear.)

N.B Tails 2.3 does not appear to honour the vga code.

**Window extends beyond the bottom of the screen.**

This seems to arise because Tails sizes to the height of the screen, but there is a title bar at the top of the window.
Either remove the title bar altogether, or move the window upwards using ALT+drag.

### Persistent Volume
The persistence tools will not work because Tails has not been launched from USB.  
The HVM disk(s) can be configured and mounted from within Tails to provide persistent storage.   
If you want to use an existing USB persistent volume: 
 - Interrupt the Tails vm boot process with arrow-up when the grub boot menu appears. 
 - In dom0 attach the USB drive containing the persistent volume to the Tails vm. 
 - Continue booting Tails: Tails-greeter will detect the encrypted partition on the attached USB. 
 - Unlock the persistent volume in Tails-greeter and use it as normal.

### Shutdown
The Tails qube will not shut down cleanly.
Kill it from the GUI Manager or ```qvm-kill Tails``` in Konsole.

### Security
You will probably want to implement [MAC spoofing](/doc/anonymizing-your-mac-address/).

There are added security concerns for Tails users when running it in a virtual machine.
If you intend to do this, you should read [the warnings](https://tails.boum.org/doc/advanced_topics/virtualization/) from the Tails team about it.
While the Qubes security model mitigates most of the risks identified, traces of the Tails session may remain on the disk.
Live booting Tails, though less convenient, is always more secure than using it inside virtualization software or Qubes, because you don't run the added risk of the virtualization software or Host OS being compromised.
Depending on your threat model, this might induce too much risk.
