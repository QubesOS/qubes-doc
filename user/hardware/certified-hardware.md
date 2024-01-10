---
lang: en
layout: doc
permalink: /doc/certified-hardware/
redirect_from:
- /doc/hardware/
- /doc/certified-laptops/
- /hardware-certification/
ref: 144
title: Certified hardware
---

The Qubes OS Project aims to partner with a select few computer vendors to ensure that Qubes users have reliable hardware purchasing options. We aim for these vendors to be as diverse as possible in terms of geography, cost, and availability.

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> The Qubes OS Project certifies only that a particular hardware <em>configuration</em> is <em>supported</em> by Qubes OS and is available to purchase with Qubes OS preinstalled. We take no responsibility for any vendor's manufacturing, shipping, payment, or other practices; nor can we control whether physical hardware is modified (whether maliciously or otherwise) <i>en route</i> to the user.
</div>

You may also be interested in the [community-recommended hardware](https://forum.qubes-os.org/t/5560) list and the [hardware compatibility list (HCL)](/hcl/).

## Qubes-certified computers

Qubes-certified computers are certified for a [major release](/doc/version-scheme/) and regularly tested by the Qubes developers to ensure compatibility with all of Qubes' features within that major release. The developers test all new updates within that major release to ensure that no regressions are introduced.

The current Qubes-certified models are listed below in chronological order of certification.

### Insurgo PrivacyBeast X230

[![Photo of the Insurgo PrivacyBeast X230](/attachment/site/insurgo-privacybeast-x230.png)](https://insurgo.ca/produit/qubesos-certified-privacybeast_x230-reasonably-secured-laptop/)

The [Insurgo PrivacyBeast X230](https://insurgo.ca/produit/qubesos-certified-privacybeast_x230-reasonably-secured-laptop/) is a laptop based on the ThinkPad X230. It is certified for Qubes OS 4.X.

### NitroPad X230

[![Photo of the NitroPad X230](/attachment/site/nitropad-x230.jpg)](https://shop.nitrokey.com/shop/product/nitropad-x230-67)

The [NitroPad X230](https://shop.nitrokey.com/shop/product/nitropad-x230-67) is a laptop based on the ThinkPad X230. It is certified for Qubes OS 4.X.

### NitroPad T430

[![Photo of the NitroPad T430](/attachment/site/nitropad-t430.jpg)](https://shop.nitrokey.com/shop/product/nitropad-t430-119)

The [NitroPad T430](https://shop.nitrokey.com/shop/product/nitropad-t430-119) is a laptop based on the ThinkPad T430. It is certified for Qubes OS 4.X.

### Dasharo FidelisGuard Z690

[![Photo of the Dasharo FidelisGuard Z690](/attachment/site/dasharo-fidelisguard-z690.jpg)](https://3mdeb.com/shop/open-source-hardware/dasharo-fidelisguard-z690-qubes-os-certified/)

The [Dasharo FidelisGuard Z690](https://3mdeb.com/shop/open-source-hardware/dasharo-fidelisguard-z690-qubes-os-certified/) is a desktop based on the MSI PRO Z690-A DDR4 motherboard. It is certified for Qubes OS 4.X.

### NovaCustom NV41 Series

[![Photo of the NovaCustom NV41 Series](/attachment/site/novacustom-nv41-series.png)](https://novacustom.com/product/nv41-series/)

The [NovaCustom NV41 Series](https://novacustom.com/product/nv41-series/) is a 14-inch custom laptop. It is certified for Qubes OS 4.X.

### NitroPC Pro

[![Photo of the NitroPC Pro](/attachment/posts/nitropc-pro.jpg)](https://shop.nitrokey.com/shop/product/nitropc-pro-523)

The [NitroPC Pro](https://shop.nitrokey.com/shop/product/nitropc-pro-523) is a desktop based on the MSI PRO Z690-A DDR5 motherboard. It is certified for Qubes OS 4.X.

### Star Labs StarBook

[![Photo of the Star Labs StarBook](/attachment/site/starlabs-starbook.png)](https://starlabs.systems/pages/starbook)

The [Star Labs StarBook](https://starlabs.systems/pages/starbook) is a 14-inch laptop. It is certified for Qubes OS 4.X. Read our [announcement](TODO) for details.

## Become hardware certified

If you are a hardware vendor, you can have your hardware certified as compatible with Qubes OS. The benefits of hardware certification include:

- Your customers can purchase with confidence, knowing that they can take full advantage of Qubes OS on your hardware for a specific major version.
- We will continue testing your hardware to ensure compatibility with the supported major version. In the course of this testing, we will also test your hardware against upcoming versions, which can help with future planning.
- Your hardware will continue to be compatible with Qubes OS as it further develops within that major version, and we will work with you toward preserving compatibility and certification in future releases.
- You can support the development of Qubes OS.

## Hardware certification requirements

**Note:** This section describes the requirements for hardware *certification*, *not* the requirements for *running* Qubes OS. For the latter, please see the [system requirements](/doc/system-requirements/). A brief list of the requirements described in this section is available [here](/doc/system-requirements/#qubes-certified-hardware).

A basic requirement is that all Qubes-certified devices must be be available for purchase with Qubes OS preinstalled. Customers may be offered the option to select from a list of various operating systems (or no operating system at all) to be preinstalled, but Qubes OS must be on that list in order to maintain Qubes hardware certification.

One of the most important security improvements introduced with the release of Qubes 4.0 was to replace paravirtualization (PV) technology with **hardware-enforced memory virtualization**, which recent processors have made possible thanks to so-called Second Level Address Translation ([SLAT](https://en.wikipedia.org/wiki/Second_Level_Address_Translation)), also known as [EPT](https://ark.intel.com/Search/FeatureFilter?productType=processors&ExtendedPageTables=true&MarketSegment=Mobile) in Intel parlance. SLAT (EPT) is an extension to Intel VT-x virtualization, which originally was capable of only CPU virtualization but not memory virtualization and hence required a complex Shadow Page Tables approach. We hope that embracing SLAT-based memory virtualization will allow us to prevent disastrous security bugs, such as the infamous [XSA-148](https://xenbits.xen.org/xsa/advisory-148.html), which --- unlike many other major Xen bugs --- regrettably did [affect](https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-022-2015.txt) Qubes OS. Consequently, we require SLAT support of all certified hardware beginning with Qubes OS 4.0.

Another important requirement is that Qubes-certified hardware should run only **open-source boot firmware** (aka "the BIOS"), such as [coreboot](https://www.coreboot.org/). The only exception is the use of (properly authenticated) CPU-vendor-provided blobs for silicon and memory initialization (see [Intel FSP](https://firmware.intel.com/learn/fsp/about-intel-fsp)) as well as other internal operations (see [Intel ME](https://www.apress.com/9781430265719)). However, we specifically require all code used for and dealing with the System Management Mode (SMM) to be open-source.

While we [recognize](https://blog.invisiblethings.org/papers/2015/x86_harmful.pdf) the potential problems that proprietary CPU-vendor code can cause, we are also pragmatic enough to realize that we need to take smaller steps first, before we can implement even stronger countermeasures such as a [stateless laptop](https://blog.invisiblethings.org/papers/2015/state_harmful.pdf). A switch to open source boot firmware is one such important step. To be compatible with Qubes OS, the BIOS must properly expose all the VT-x, VT-d, and SLAT functionality that the underlying hardware offers (and which we require). Among other things, this implies **proper DMAR ACPI table** construction.

Most laptops use PS/2 connections internally for their input devices (i.e., keyboard and touchpad). On most desktops, however, USB-connected keyboards and mice have become standard. This presents a dilemma when the computer has only one USB controller. If that single USB controller is dedicated solely to the input devices, then no untrusted USB devices can be used. Conversely, if the sole USB controller is completely untrusted, then there is no way for the user to physically control the system in a secure way. In practice, Qubes users on such hardware systems are generally forced to use a single USB controller for both trusted and untrusted purposes --- [an unfortunate security trade-off](/doc/device-handling-security/#security-warning-on-usb-input-devices). For this reason, we require that every Qubes-certified non-laptop device **either** (1) supports non-USB input devices (e.g., via PS/2) **or** (2) has a separate USB controller that is only for input devices.

Finally, we require that Qubes-certified hardware does not have any built-in _USB-connected_ microphones (e.g. as part of a USB-connected built-in camera) that cannot be easily physically disabled by the user, e.g. via a convenient mechanical switch. Thankfully, the majority of laptops on the market that we have seen already satisfy this condition out-of-the-box, because their built-in microphones are typically connected to the internal audio device, which itself is a type of PCIe device. This is important, because such PCIe audio devices are --- by default --- assigned to Qubes' (trusted) dom0 and exposed through our carefully designed protocol only to select app qubes when the user explicitly chooses to do so. The rest of the time, they should be outside the reach of malware.

While we also recommend a physical kill switch on the built-in camera (or, if possible, not to have a built-in camera), we also recognize this isn't a critical requirement, because users who are concerned about it can easily cover it a piece of tape (something that, regrettably, is far less effective on a microphone).

Similarly, we don't consider physical kill switches on Wi-Fi and Bluetooth devices to be mandatory. Users who plan on using Qubes in an air-gap scenario would do best if they manually remove all such devices persistently (as well as the builtin [speakers](https://github.com/romanz/amodem/)!), rather than rely on easy-to-flip-by-mistake switches, while others should benefit from the Qubes default sandboxing of all networking devices in dedicated VMs.

We hope these hardware requirements will encourage the development of more secure and trustworthy devices.

## Hardware certification process

To have hardware certified, the vendor must:

1. Send the Qubes team two (2) units for testing (non-returnable) for each configuration the vendor wishes to be offering.
2. Offer to customers the very same configuration (same motherboard, same screen, same BIOS version, same Wi-Fi module, etc.) for at least one year.
3. Pay the Qubes team a flat monthly rate, to be agreed upon between the hardware vendor and the Qubes team.

It is the vendor's responsibility to ensure the hardware they wish to have certified can run Qubes OS, at the very least the latest stable version. This could be done by consulting the [Hardware Compatibility List](/hcl/) or trying to install it themselves before shipping any units to us. While we are willing to troubleshoot simple issues, we will need to charge a consulting fee for more in-depth work.

If you are interested in having your hardware certified, please [contact us](mailto:business@qubes-os.org).
