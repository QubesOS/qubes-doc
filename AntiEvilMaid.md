---
layout: doc
title: AntiEvilMaid
permalink: /doc/AntiEvilMaid/
redirect_from: /wiki/AntiEvilMaid/
---

Installing and Using Anti Evil Maid (AEM) with Qubes OS
=======================================================

Background
----------

Please read [this blog article](http://theinvisiblethings.blogspot.com/2011/09/anti-evil-maid.html).

Installing
----------

In Dom0 install anti-evil-maid:

{% highlight trac-wiki %}
sudo qubes-dom0-update anti-evil-maid
{% endhighlight %}

More information regarding configuration in the [README](http://git.qubes-os.org/?p=joanna/antievilmaid.git;a=blob_plain;f=README;hb=HEAD) file.

Security Considerations
-----------------------

[Qubes security guidelines](/wiki/SecurityGuidelines) dictate that USB devices should never be attached directly to dom0, since this can result in the entire system being compromised. However, in its default configuration, installing and using AEM requires attaching a USB drive (i.e., [mass storage device](https://en.wikipedia.org/wiki/USB_mass_storage_device_class)) directly to dom0. (The other option is to install AEM to an internal disk. However, this carries significant security implications, as explained [here](http://theinvisiblethings.blogspot.com/2011/09/anti-evil-maid.html).) This presents us with a classic security trade-off: each Qubes user must make a choice between protecting dom0 from a potentially malicious USB drive, on the one hand, and protecting the system from Evil Maid attacks, on the other hand. Given the practical feasibility of attacks like [BadUSB](https://srlabs.de/badusb/) and revelations regarding pervasive government hardware backdoors, this is no longer a straightforward decision. New, factory-sealed USB drives cannot simply be assumed to be "clean" (e.g., to have non-malicious microcontroller firmware). Therefore, it is up to each individual Qubes user to evaluate the relative risk of each attack vector against his or her security model.

For example, a user who frequently travels with a Qubes laptop holding sensitive data may be at a much higher risk of Evil Maid attacks than a home user with a stationary Qubes desktop. If the frequent traveler judges her risk of an Evil Maid attack to be higher than the risk of a malicious USB device, she might reasonably opt to install and use AEM. On the other hand, the home user might deem the probability of an Evil Maid attack occurring in her own home to be so low that there is a higher probability that any USB drive she purchases is already compromised, in which case she might reasonably opt never to attach any USB devices directly to dom0. (In either case, users can--and should--secure dom0 against further USB-related attacks through the use of a [USBVM](/wiki/SecurityGuidelines#CreatingandUsingaUSBVM).)

For more information, please see [this discussion thread](https://groups.google.com/d/msg/qubes-devel/EBc4to5IBdg/n1hfsHSfbqsJ).

Known issues
------------

-   USB 3.0 isn't supported yet

