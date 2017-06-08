---
layout: sidebar
title: Hardware
permalink: /doc/hardware/
redirect_from:
 - /hardware-certification/
 - /doc/certified-laptops/
---

# Hardware #

## Important Information ##

There is currently **no** specific hardware (e.g., a specific laptop model) that the Qubes team recommends for individual (as opposed to enterprise) users.
However, we're working hard to make a "reasonably secure laptop" a reality, and we look forward to sharing more information about this when the time is right.
(Note that this will be distinct from a [stateless laptop], which no one has implemented yet.)
In the meantime, users are encouraged to make use of the [Hardware Compatibility List] and [System Requirements] as sources of information in making hardware selection decisions.

Some users may wish to consider [Qubes-certified laptops].
However, it is important to note that such laptops are certified only for *compatibility* with Qubes OS.
In particular, the [Purism Librem 13] is certified only for compatibility with Qubes R3.x, and it is not likely to be certified for compatibility with Qubes R4.x.
Aside from compatibility, we do not believe that it should be considered any safer than other laptops.

Serious prospective business customers should [contact us] for more information.

## Hardware Certification ##

### Become Hardware Certified ###

If you are a hardware vendor, you can have your hardware certified as
compatible with Qubes OS. To view currently certified hardware, please see
the [Qubes-certified Laptops] page.

The benefits of hardware certification include:

* your customers can buy with confidence
- *your customers know they can take advantage of the full functionality
of Qubes OS on your hardware*

* ensure continued compatibility
- *your hardware will continue to be compatible with Qubes OS as it
further develops*

* support the development of Qubes OS
- *support the continued development of everyone's favorite "reasonably
secure" OS*

### Hardware Certification Requirements ###

Please see the [updated requirements] for Qubes 4.x certification.

**Note:** These are the requirements for hardware certification, *not* the
requirements for *running* Qubes 4.x. For the latter, please see the
[system requirements for Qubes 4.x].

### Hardware Certification Process ###

To have hardware certified, the vendor must:

1. send the Qubes team two (2) units for testing (non-returnable) for
each configuration the vendor wishes to be offering,

2. offer to customers the very same configuration -- same motherboard,
same screen, same BIOS version, same WiFi module, etc. -- for some
sufficiently long period of time (currently approximately a year),

3. pay the Qubes team a portion of the sales of each unit, to be agreed
upon between the hardware vendor and the Qubes team.

It is the vendor's responsibility to ensure the hardware they wish to
have certified can run Qubes OS, at the very least the last stable
version. This could be done by consulting the [hardware compatibility
list](https://www.qubes-os.org/doc/hcl/) or trying to install it
themselves before shipping to us. While we are willing to troubleshoot
simple issues, we will need to charge a consulting fee for more engaging
work.

If you are interested in having your hardware certified, please [contact us].


## Qubes-certified Laptops ##

Qubes-certified laptops are regularly tested by the Qubes
developers to ensure compatibility with all of Qubes' features. The developers
test all new major versions and updates to ensure that no regressions are introduced.
To learn more about the certification process, or if you're interested in
getting your company's hardware Qubes-certified, please see the [Hardware
Certification] page.

We aim to partner with a few select computer makers to ensure that Qubes is
compatible with them and new users have clear path towards getting started
with Qubes if they desire. We look for these makers to be as diverse as possible
in terms of geography, cost, and availability.

Note that we certify only that a particular configuration is supported by Qubes.
We take no responsibility for our partners' shipping process -- including that
the hardware will not be modified in any way (malicious or not).

For more general information about choosing hardware for Qubes, please see the
[System Requirements] and the [Hardware Compatibility List].


### Certified for Qubes R3.x ###

#### Purism Librem 13 ####

[![image of Librem 13](/attachment/site/qubes-plus-purism.png)](https://puri.sm/librem-13/)

For users now who seek to buy a Librem 13, there is an option to have Qubes
pre-installed. This will include all the necessary tweaks for
maximum compatibility with Qubes. 

In addition, the Qubes team will receive a small portion of the revenue from any
Librem 13 sale that comes with Qubes pre-installed.

For existing Librem 13 users, please follow the instructions to ensure maximum
compatibility with Qubes:

1. In `dom0`, open a terminal and type:

       sudo qubes-dom0-update --releasever=3.1 xorg-x11-drivers xorg-x11-drv-intel

2. (optional) Enable newer kernel:

       sudo qubes-dom0-update --enablerepo=qubes-dom0-unstable kernel


### Certified for Qubes R4.x ###

There are [updated requirements] for Qubes R4.x certification. Currently, no
laptops are certified for Qubes R4.x. This page will be updated once
R4.x-certified laptops are available.

[Qubes-certified laptops]: #qubes-certified-laptops
[stateless laptop]: https://blog.invisiblethings.org/2015/12/23/state_harmful.html
[System Requirements]: /doc/system-requirements/
[Hardware Compatibility List]: /hcl/
[Purism Librem 13]: #purism-librem-13
[updated requirements]: /news/2016/07/21/new-hw-certification-for-q4/
[system requirements for Qubes 4.x]: /doc/system-requirements/#qubes-release-4x
[contact us]: mailto:business@qubes-os.org


