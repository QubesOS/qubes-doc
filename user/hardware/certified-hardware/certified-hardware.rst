==================
Certified hardware
==================


The Qubes OS Project aims to partner with a select few computer vendors to ensure that Qubes users have reliable hardware purchasing options. We aim for these vendors to be as diverse as possible in terms of geography, cost, and availability.

.. DANGER::

      **Warning:** The Qubes OS Project certifies only that a particular hardware *configuration* is *supported* by Qubes OS and is available to purchase with Qubes OS preinstalled. We take no responsibility for any vendor’s manufacturing, shipping, payment, or other practices; nor can we control whether physical hardware is modified (whether maliciously or otherwise) *en route* to the user.

You may also be interested in the `community-recommended hardware <https://forum.qubes-os.org/t/5560>`__ list and the `hardware compatibility list (HCL) <https://www.qubes-os.org/hcl/>`__.

Qubes-certified computers
-------------------------


Qubes-certified computers are certified for a :doc:`major release </developer/releases/version-scheme>` and regularly tested by the Qubes developers to ensure compatibility with all of Qubes’ features within that major release. The developers test all new updates within that major release to ensure that no regressions are introduced.

The current Qubes-certified models are listed below in reverse chronological order of certification.

.. list-table::
   :widths: 43 43 43
   :align: center
   :header-rows: 1

   * - Brand
     - Model
     - Certification details
   * - `NovaCustom <https://novacustom.com/>`__
     - `V54 Series <https://novacustom.com/product/v54-series/>`__
     - :doc:`Certification details </user/hardware/certified-hardware/novacustom-v54-series/>`
   * - `Nitrokey <https://www.nitrokey.com/>`__
     - `NitroPad V56 <https://shop.nitrokey.com/shop/nitropad-v56-684>`__
     - :doc:`Certification details </user/hardware/certified-hardware/nitropad-v56/>`
   * - `NovaCustom <https://novacustom.com/>`__
     - `V56 Series <https://novacustom.com/product/v56-series/>`__
     - :doc:`Certification details </user/hardware/certified-hardware/novacustom-v56-series/>`
   * - `Nitrokey <https://www.nitrokey.com/>`__
     - `NitroPC Pro 2 <https://shop.nitrokey.com/shop/nitropc-pro-2-523>`__
     - :doc:`Certification details </user/hardware/certified-hardware/nitropc-pro-2/>`
   * - `Star Labs <https://starlabs.systems/>`__
     - `StarBook <https://starlabs.systems/pages/starbook>`__
     - :doc:`Certification details </user/hardware/certified-hardware/starlabs-starbook/>`
   * - `Nitrokey <https://www.nitrokey.com/>`__
     - `NitroPC Pro <https://web.archive.org/web/20231027112856/https://shop.nitrokey.com/shop/product/nitropc-pro-523>`__
     - :doc:`Certification details </user/hardware/certified-hardware/nitropc-pro/>`
   * - `NovaCustom <https://novacustom.com/>`__
     - `NV41 Series <https://novacustom.com/product/nv41-series/>`__
     - :doc:`Certification details </user/hardware/certified-hardware/novacustom-nv41-series/>`
   * - `3mdeb <https://3mdeb.com/>`__
     - `Dasharo FidelisGuard Z690 <https://web.archive.org/web/20240917145232/https://shop.3mdeb.com/shop/open-source-hardware/dasharo-fidelisguard-z690-qubes-os-certified/>`__
     - :doc:`Certification details </user/hardware/certified-hardware/dasharo-fidelisguard-z690/>`
   * - `Nitrokey <https://www.nitrokey.com/>`__
     - `NitroPad T430 <https://shop.nitrokey.com/shop/nitropad-t430-119>`__
     - :doc:`Certification details </user/hardware/certified-hardware/nitropad-t430/>`
   * - `Nitrokey <https://www.nitrokey.com/>`__
     - `NitroPad X230 <https://shop.nitrokey.com/shop/product/nitropad-x230-67>`__
     - :doc:`Certification details </user/hardware/certified-hardware/nitropad-x230/>`
   * - `Insurgo <https://insurgo.ca/>`__
     - `PrivacyBeast X230 <https://insurgo.ca/produit/qubesos-certified-privacybeast_x230-reasonably-secured-laptop/>`__
     - :doc:`Certification details </user/hardware/certified-hardware/insurgo-privacybeast-x230/>`


Become hardware certified
-------------------------


If you are a hardware vendor, you can have your hardware certified as compatible with Qubes OS. The benefits of hardware certification include:

- Your customers can purchase with confidence, knowing that they can take full advantage of Qubes OS on your hardware for a specific major version.

- We will continue testing your hardware to ensure compatibility with the supported major version. In the course of this testing, we will also test your hardware against upcoming versions, which can help with future planning.

- Your hardware will continue to be compatible with Qubes OS as it further develops within that major version, and we will work with you toward preserving compatibility and certification in future releases.

- You can support the development of Qubes OS.



Hardware certification requirements
-----------------------------------


**Note:** This section describes the requirements for hardware *certification*, *not* the requirements for *running* Qubes OS. For the latter, please see the :doc:`system requirements </user/hardware/system-requirements>`. A brief list of the requirements described in this section is available :ref:`here <user/hardware/system-requirements:qubes-certified hardware>`.

A basic requirement is that all Qubes-certified devices must be available for purchase with Qubes OS preinstalled. Customers may be offered the option to select from a list of various operating systems (or no operating system at all) to be preinstalled, but Qubes OS must be on that list in order to maintain Qubes hardware certification.

One of the most important security improvements introduced with the release of Qubes 4.0 was to replace paravirtualization (PV) technology with **hardware-enforced memory virtualization**, which recent processors have made possible thanks to so-called Second Level Address Translation (`SLAT <https://en.wikipedia.org/wiki/Second_Level_Address_Translation>`__), also known as `EPT <https://ark.intel.com/Search/FeatureFilter?productType=processors&ExtendedPageTables=true&MarketSegment=Mobile>`__ in Intel parlance. SLAT (EPT) is an extension to Intel VT-x virtualization, which originally was capable of only CPU virtualization but not memory virtualization and hence required a complex Shadow Page Tables approach. We hope that embracing SLAT-based memory virtualization will allow us to prevent disastrous security bugs, such as the infamous `XSA-148 <https://xenbits.xen.org/xsa/advisory-148.html>`__, which — unlike many other major Xen bugs — regrettably did `affect <https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-022-2015.txt>`__ Qubes OS. Consequently, we require SLAT support of all certified hardware beginning with Qubes OS 4.0.

Another important requirement is that Qubes-certified hardware should run only **open-source boot firmware** (aka “the BIOS”), such as `coreboot <https://www.coreboot.org/>`__. The only exception is the use of (properly authenticated) CPU-vendor-provided blobs for silicon and memory initialization (see `Intel FSP <https://firmware.intel.com/learn/fsp/about-intel-fsp>`__) as well as other internal operations (see `Intel ME <https://www.apress.com/9781430265719>`__). However, we specifically require all code used for and dealing with the System Management Mode (SMM) to be open-source.

While we `recognize <https://blog.invisiblethings.org/papers/2015/x86_harmful.pdf>`__ the potential problems that proprietary CPU-vendor code can cause, we are also pragmatic enough to realize that we need to take smaller steps first, before we can implement even stronger countermeasures such as a `stateless laptop <https://blog.invisiblethings.org/papers/2015/state_harmful.pdf>`__. A switch to open source boot firmware is one such important step. To be compatible with Qubes OS, the BIOS must properly expose all the VT-x, VT-d, and SLAT functionality that the underlying hardware offers (and which we require). Among other things, this implies **proper DMAR ACPI table** construction.

Most laptops use PS/2 connections internally for their input devices (i.e., keyboard and touchpad). On most desktops, however, USB-connected keyboards and mice have become standard. This presents a dilemma when the computer has only one USB controller. If that single USB controller is dedicated solely to the input devices, then no untrusted USB devices can be used. Conversely, if the sole USB controller is completely untrusted, then there is no way for the user to physically control the system in a secure way. In practice, Qubes users on such hardware systems are generally forced to use a single USB controller for both trusted and untrusted purposes — :ref:`an unfortunate security trade-off <user/security-in-qubes/device-handling-security:security warning on usb input devices>`. For this reason, we require that every Qubes-certified non-laptop device **either** (1) supports non-USB input devices (e.g., via PS/2) **or** (2) has a separate USB controller that is only for input devices.

Finally, we require that Qubes-certified hardware does not have any built-in *USB-connected* microphones (e.g. as part of a USB-connected built-in camera) that cannot be easily physically disabled by the user, e.g. via a convenient mechanical switch. Thankfully, the majority of laptops on the market that we have seen already satisfy this condition out-of-the-box, because their built-in microphones are typically connected to the internal audio device, which itself is a type of PCIe device. This is important, because such PCIe audio devices are — by default — assigned to Qubes’ (trusted) dom0 and exposed through our carefully designed protocol only to select app qubes when the user explicitly chooses to do so. The rest of the time, they should be outside the reach of malware.

While we also recommend a physical kill switch on the built-in camera (or, if possible, not to have a built-in camera), we also recognize this isn’t a critical requirement, because users who are concerned about it can easily cover it a piece of tape (something that, regrettably, is far less effective on a microphone).

Similarly, we don’t consider physical kill switches on Wi-Fi and Bluetooth devices to be mandatory. Users who plan on using Qubes in an air-gap scenario would do best if they manually remove all such devices persistently (as well as the builtin `speakers <https://github.com/romanz/amodem/>`__!), rather than rely on easy-to-flip-by-mistake switches, while others should benefit from the Qubes default sandboxing of all networking devices in dedicated VMs.

We hope these hardware requirements will encourage the development of more secure and trustworthy devices.

Hardware certification process
------------------------------


To have hardware certified, the vendor must:

1. Send the Qubes team two (2) units for testing (non-returnable) for each configuration the vendor wishes to be offering.

2. Offer to customers the very same configuration (same motherboard, same screen, same BIOS version, same Wi-Fi module, etc.) for at least one year.

3. Pay the Qubes team a flat monthly rate, to be agreed upon between the hardware vendor and the Qubes team.



It is the vendor’s responsibility to ensure the hardware they wish to have certified can run Qubes OS, at the very least the latest stable version. This could be done by consulting the `Hardware Compatibility List <https://www.qubes-os.org/hcl/>`__ or trying to install it themselves before shipping any units to us. While we are willing to troubleshoot simple issues, we will need to charge a consulting fee for more in-depth work.

If you are interested in having your hardware certified, please `contact us <mailto:business@qubes-os.org>`__.
