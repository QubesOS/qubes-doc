---
layout: doc
title: Running Tails in Qubes
redirect_to: https://github.com/Qubes-Community/Contents/blob/master/docs/privacy/tails.md
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

## Security
You will probably want to implement [MAC spoofing](/doc/anonymizing-your-mac-address/).

There are added security concerns for Tails users when running it in a virtual machine.
If you intend to do this, you should read [the warnings](https://tails.boum.org/doc/advanced_topics/virtualization/) from the Tails team about it.
While the Qubes security model mitigates most of the risks identified, traces of the Tails session may remain on the disk.
Live booting Tails, though less convenient, is always more secure than using it inside virtualization software or Qubes, because you don't run the added risk of the virtualization software or Host OS being compromised.
Depending on your threat model, this might induce too much risk.

## Troubleshooting

See the [Tails Troubleshooting guide](/doc/tails-troubleshooting/).

