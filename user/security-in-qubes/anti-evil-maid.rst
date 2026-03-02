====================
Anti evil maid (AEM)
====================


Background
----------


Please read `this blog article <https://blog.invisiblethings.org/2011/09/07/anti-evil-maid.html>`__.

Requirements
------------


The current package requires a TPM 1.2 interface and a working Intel TXT engine. If you cleaned your Intel Management Engine with e.g. `me_cleaner <https://github.com/corna/me_cleaner>`__ while installing `coreboot <https://www.coreboot.org/>`__ then you are out of luck. For now you have to choose between cleaning your BIOS and deploying Anti Evil Maid.

`Discussion <https://groups.google.com/d/msg/qubes-users/sEmZfOZqYXM/j5rHeex1BAAJ>`__

Installing
----------


In Dom0 install ``anti-evil-maid``:

.. code:: console

      $ sudo qubes-dom0-update anti-evil-maid



For more information, see the `qubes-antievilmaid <https://github.com/QubesOS/qubes-antievilmaid>`__ repository, which includes a ``README``.

Security Considerations
-----------------------


`Qubes security guidelines <https://forum.qubes-os.org/t/19075>`__ dictate that USB devices should never be attached directly to dom0, since this can result in the entire system being compromised. However, in its default configuration, installing and using AEM requires attaching a USB drive (i.e., `mass storage device <https://en.wikipedia.org/wiki/USB_mass_storage_device_class>`__) directly to dom0. (The other option is to install AEM to an internal disk. However, this carries significant security implications, as explained `here <https://blog.invisiblethings.org/2011/09/07/anti-evil-maid.html>`__.) This presents us with a classic security trade-off: each Qubes user must make a choice between protecting dom0 from a potentially malicious USB drive, on the one hand, and protecting the system from Evil Maid attacks, on the other hand. Given the practical feasibility of attacks like `BadUSB <https://web.archive.org/web/20160304013434/https://srlabs.de/badusb/>`__ and revelations regarding pervasive government hardware backdoors, this is no longer a straightforward decision. New, factory-sealed USB drives cannot simply be assumed to be “clean” (e.g., to have non-malicious microcontroller firmware). Therefore, it is up to each individual Qubes user to evaluate the relative risk of each attack vector against his or her security model.

For example, a user who frequently travels with a Qubes laptop holding sensitive data may be at a much higher risk of Evil Maid attacks than a home user with a stationary Qubes desktop. If the frequent traveler judges her risk of an Evil Maid attack to be higher than the risk of a malicious USB device, she might reasonably opt to install and use AEM. On the other hand, the home user might deem the probability of an Evil Maid attack occurring in her own home to be so low that there is a higher probability that any USB drive she purchases is already compromised, in which case she might reasonably opt never to attach any USB devices directly to dom0. (In either case, users can–and should–secure dom0 against further USB-related attacks through the use of a `USB VM <https://forum.qubes-os.org/t/19075#creating-and-using-a-usbvm>`__.)

For more information, please see `this discussion thread <https://groups.google.com/d/msg/qubes-devel/EBc4to5IBdg/n1hfsHSfbqsJ>`__.

Known issues
------------


- USB 3.0 isn’t supported yet

- `AEM is not compatible with having an SSD cache <https://groups.google.com/d/msgid/qubes-users/70021590-fb3a-4f95-9ce5-4b340530ddbf%40petaramesh.org>`__


