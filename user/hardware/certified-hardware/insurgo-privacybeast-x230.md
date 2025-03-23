---
lang: en
layout: doc
permalink: /doc/certified-hardware/insurgo-privacybeast-x230/
title: Insurgo PrivacyBeast X230
image: /attachment/site/insurgo-privacybeast-x230.png
---

<div class="alert alert-danger" role="alert">
  <i class="fa fa-exclamation-triangle"></i>
  <b>Warning:</b> The CPU in this computer no longer receives microcode updates from Intel. Without microcode updates, Qubes OS cannot ensure that this computer is secure against CPU vulnerabilities. While this computer remains certified for Qubes OS Release 4, we recommend that prospective buyers consider a newer Qubes-certified computer instead.
</div>

The [Insurgo PrivacyBeast X230](https://insurgo.ca/produit/qubesos-certified-privacybeast_x230-reasonably-secured-laptop/) is [officially certified](/doc/certified-hardware/) for Qubes OS Release 4.

[![Photo of the Insurgo PrivacyBeast X230](/attachment/site/insurgo-privacybeast-x230.png)](https://insurgo.ca/produit/qubesos-certified-privacybeast_x230-reasonably-secured-laptop/)

The [Insurgo PrivacyBeast X230](https://insurgo.ca/produit/qubesos-certified-privacybeast_x230-reasonably-secured-laptop/) is a custom refurbished [ThinkPad X230](https://www.thinkwiki.org/wiki/Category:X230) that includes the following features:

- [Coreboot](https://www.coreboot.org/) initialization for the x230 is binary-blob-free, including native graphic initialization. Built with the [Heads](https://github.com/osresearch/heads/) payload, it delivers an [Anti Evil Maid (AEM)](/doc/anti-evil-maid/)-like solution built into the firmware. (Even though our [requirements](/doc/certified-hardware/#hardware-certification-requirements) provide an exception for CPU-vendor-provided blobs for silicon and memory initialization, Insurgo exceeds our requirements by insisting that these be absent from its machines.)

- [Intel ME](https://libreboot.org/faq.html#intelme) is neutered through the AltMeDisable bit, while all modules other than ROMP and BUP, which are required to initialize main CPU, have been [deleted](https://github.com/osresearch/heads-wiki/blob/master/Clean-the-ME-firmware.md#how-to-disabledeactive-most-of-it).

- A re-ownership process that allows it to ship pre-installed with Qubes OS, including full-disk encryption already in place, but where the final disk encryption key is regenerated only when the machine is first powered on by the user, so that the OEM doesn't know it.

- [Heads](https://github.com/osresearch/heads/) provisioned pre-delivery to protect against malicious [interdiction](https://en.wikipedia.org/wiki/Interdiction).
