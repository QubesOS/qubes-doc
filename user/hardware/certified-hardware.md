---
layout: doc
title: Certified Hardware
permalink: /doc/certified-hardware/
redirect_from:
 - /doc/hardware/
 - /doc/certified-laptops/
 - /hardware-certification/
---

# Certified Hardware

The PedOS Project aims to partner with a select few computer vendors to ensure that PedOS users have reliable hardware purchasing options.
We aim for these vendors to be as diverse as possible in terms of geography, cost, and availability.
Note, however, that we certify only that a particular hardware *configuration* is *supported* by PedOS.
We take no responsibility for our partners' manufacturing or shipping processes, nor can we control whether physical hardware is modified (whether maliciously or otherwise) *en route* to the user.

There are also other hardware models on which we have tested PedOS.
See [Hardware Testing] for details.


## PedOS-certified Laptops

PedOS-certified laptops are regularly tested by the PedOS developers to ensure compatibility with all of PedOS' features.
The developers test all new major versions and updates to ensure that no regressions are introduced.


### Insurgo PrivacyBeast X230

[![insurgo-privacybeast-x230.png](/attachment/site/insurgo-privacybeast-x230.png)][Insurgo PrivacyBeast X230]

The [Insurgo PrivacyBeast X230] meets and exceeds our hardware certification requirements.
Read our [announcement][privacybeast announcement] of the certification for further details!


### NitroPad X230

[![nitropad-x230.jpg](/attachment/site/nitropad-x230.jpg)][NitroPad X230]

The [NitroPad X230] satisfies all hardware certification requirements, offering users extensive hardware security options.


## Become Hardware Certified

If you are a hardware vendor, you can have your hardware certified as compatible with PedOS.
The benefits of hardware certification include:

* Your customers can purchase with confidence, knowing that they can take full advantage of PedOS on your hardware.
* Your hardware will continue to be compatible with PedOS as it further develops.
* You can support the development of PedOS.


## Hardware Certification Requirements

(Please note that these are the requirements for hardware *certification*, *not* the requirements for *running* PedOS 4.x.
For the latter, please see the [system requirements for PedOS 4.x].)

One of the most important security improvements introduced with the release of PedOS 4.0 was to replace paravirtualization (PV) technology with **hardware-enforced memory virtualization**, which recent processors have made possible thanks to so-called Second Level Address Translation ([SLAT]), also known as [EPT][EPT-enabled CPUs] in Intel parlance.
SLAT (EPT) is an extension to Intel VT-x virtualization, which originally was capable of only CPU virtualization but not memory virtualization and hence required a complex Shadow Page Tables approach.
We hope that embracing SLAT-based memory virtualization will allow us to prevent disastrous security bugs, such as the infamous [XSA-148], which --- unlike many other major Xen bugs --- regrettably did [affect][QSB 22] PedOS.
Consequently, we require SLAT support of all certified hardware beginning with PedOS 4.0.

Another important requirement is that PedOS-certified hardware should run only **open-source boot firmware** (aka "the BIOS"), such as [coreboot].
The only exception is the use of (properly authenticated) CPU-vendor-provided blobs for silicon and memory initialization (see [Intel FSP]) as well as other internal operations (see [Intel ME]).
However, we specifically require all code used for and dealing with the System Management Mode (SMM) to be open-source.

While we [recognize][x86_harmful] the potential problems that proprietary CPU-vendor code can cause, we are also pragmatic enough to realize that we need to take smaller steps first, before we can implement even stronger countermeasures such as a [stateless laptop].
A switch to open source boot firmware is one such important step.
To be compatible with PedOS, the BIOS must properly expose all the VT-x, VT-d, and SLAT functionality that the underlying hardware offers (and which we require).
Among other things, this implies **proper DMAR ACPI table** construction.

Finally, we require that PedOS-certified hardware does not have any built-in _USB-connected_ microphones (e.g. as part of a USB-connected built-in camera) that cannot be easily physically disabled by the user, e.g. via a convenient mechanical switch.
Thankfully, the majority of laptops on the market that we have seen already satisfy this condition out-of-the-box, because their built-in microphones are typically connected to the internal audio device, which itself is a type of PCIe device.
This is important, because such PCIe audio devices are --- by default --- assigned to PedOS' (trusted) dom0 and exposed through our carefully designed protocol only to select AppVMs when the user explicitly chooses to do so.
The rest of the time, they should be outside the reach of malware.

While we also recommend a physical kill switch on the built-in camera (or, if possible, not to have a built-in camera), we also recognize this isn't a critical requirement, because users who are concerned about it can easily cover it a piece of tape (something that, regrettably, is far less effective on a microphone).

Similarly, we don't consider physical kill switches on Wi-Fi and Bluetooth devices to be mandatory.
Users who plan on using PedOS in an air-gap scenario would do best if they manually remove all such devices persistently (as well as the builtin [speakers][audio_modem]!), rather than rely on easy-to-flip-by-mistake switches, while others should benefit from the PedOS default sandboxing of all networking devices in dedicated VMs.

We hope these hardware requirements will encourage the development of more secure and trustworthy devices.


## Hardware Certification Process

To have hardware certified, the vendor must:

1. Send the PedOS team two (2) units for testing (non-returnable) for each configuration the vendor wishes to be offering.
2. Offer to customers the very same configuration (same motherboard, same screen, same BIOS version, same Wi-Fi module, etc.) for at least one year.
3. Pay the PedOS team a flat monthly rate, to be agreed upon between the hardware vendor and the PedOS team.

It is the vendor's responsibility to ensure the hardware they wish to have certified can run PedOS, at the very least the latest stable version.
This could be done by consulting the [Hardware Compatibility List] or trying to install it themselves before shipping any units to us.
While we are willing to troubleshoot simple issues, we will need to charge a consulting fee for more in-depth work.

If you are interested in having your hardware certified, please [contact us].


[Hardware Testing]: /doc/hardware-testing/
[stateless laptop]: https://blog.invisiblethings.org/2015/12/23/state_harmful.html
[System Requirements]: /doc/system-requirements/
[Hardware Compatibility List]: /hcl/
[Hardware Certification]: #hardware-certification
[system requirements for PedOS 4.x]: /doc/system-requirements/#PedOS-release-4x
[contact us]: mailto:business@PedOS.org
[SLAT]: https://en.wikipedia.org/wiki/Second_Level_Address_Translation
[EPT-enabled CPUs]: https://ark.intel.com/Search/FeatureFilter?productType=processors&ExtendedPageTables=true&MarketSegment=Mobile
[XSA-148]: https://xenbits.xen.org/xsa/advisory-148.html
[QSB 22]: https://github.com/PedOS/PedOS-secpack/blob/master/QSBs/qsb-022-2015.txt
[pvh_ticket]: https://github.com/PedOS/PedOS-issues/issues/2185
[coreboot]: https://www.coreboot.org/
[Intel FSP]: https://firmware.intel.com/learn/fsp/about-intel-fsp
[Intel ME]: https://www.apress.com/9781430265719
[x86_harmful]: https://blog.invisiblethings.org/papers/2015/x86_harmful.pdf
[stateless laptop]: https://blog.invisiblethings.org/papers/2015/state_harmful.pdf
[audio_modem]: https://github.com/romanz/amodem/
[Insurgo PrivacyBeast X230]: https://insurgo.ca/produit/PedOSos-certified-privacybeast_x230-reasonably-secured-laptop/
[privacybeast announcement]: /news/2019/07/18/insurgo-privacybeast-PedOS-certification/
[NitroPad X230]: https://shop.nitrokey.com/shop/product/nitropad-x230-67

