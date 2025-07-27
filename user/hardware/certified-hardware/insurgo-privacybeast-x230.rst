=========================
Insurgo PrivacyBeast X230
=========================


.. DANGER::
      
      **Warning:** The CPU in this computer no longer receives microcode updates from Intel. Without microcode updates, Qubes OS cannot ensure that this computer is secure against CPU vulnerabilities. While this computer remains certified for Qubes OS Release 4, we recommend that prospective buyers consider a newer Qubes-certified computer instead.

The `Insurgo PrivacyBeast X230 <https://insurgo.ca/produit/qubesos-certified-privacybeast_x230-reasonably-secured-laptop/>`__ is :doc:`officially certified </user/hardware/certified-hardware/certified-hardware>` for Qubes OS Release 4.

|Photo of the Insurgo PrivacyBeast X230|

The `Insurgo PrivacyBeast X230 <https://insurgo.ca/produit/qubesos-certified-privacybeast_x230-reasonably-secured-laptop/>`__ is a custom refurbished `ThinkPad X230 <https://www.thinkwiki.org/wiki/Category:X230>`__ that includes the following features:

- `coreboot <https://www.coreboot.org/>`__ initialization for the x230 is binary-blob-free, including native graphic initialization. Built with the `Heads <https://github.com/osresearch/heads/>`__ payload, it delivers an :doc:`Anti Evil Maid (AEM) </user/security-in-qubes/anti-evil-maid>`-like solution built into the firmware. (Even though our :ref:`requirements <user/hardware/certified-hardware/certified-hardware:hardware certification requirements>` provide an exception for CPU-vendor-provided blobs for silicon and memory initialization, Insurgo exceeds our requirements by insisting that these be absent from its machines.)

- `Intel ME <https://libreboot.org/faq.html#intelme>`__ is neutered through the AltMeDisable bit, while all modules other than ROMP and BUP, which are required to initialize main CPU, have been `deleted <https://github.com/linuxboot/heads-wiki/blob/master/Installing-and-Configuring/Flashing-Guides/Clean-the-ME-firmware.md#how-to-disabledeactive-most-of-it>`__.

- A re-ownership process that allows it to ship pre-installed with Qubes OS, including full-disk encryption already in place, but where the final disk encryption key is regenerated only when the machine is first powered on by the user, so that the OEM doesn’t know it.

- `Heads <https://github.com/osresearch/heads/>`__ provisioned pre-delivery to protect against malicious :wikipedia:`interdiction <Interdiction>`.



.. |Photo of the Insurgo PrivacyBeast X230| image:: /attachment/site/insurgo-privacybeast-x230.png
   :target: https://insurgo.ca/produit/qubesos-certified-privacybeast_x230-reasonably-secured-laptop/
