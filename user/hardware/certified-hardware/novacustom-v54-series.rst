=====================
NovaCustom V54 Series
=====================


The `NovaCustom V54 Series 14.0 inch coreboot laptop <https://novacustom.com/product/v54-series/>`__ is :doc:`officially certified </user/hardware/certified-hardware/certified-hardware>` for Qubes OS Release 4.

|Photo of the NovaCustom V54 Series 14.0 inch coreboot laptop|

Qubes-certified options
-----------------------


The configuration options required for Qubes certification are detailed below.

Screen size
^^^^^^^^^^^


- Certified: 14 inch



**Note:** The 14-inch model (V540TU) and the 16-inch model (V560TU) are two separate products. :doc:`The 16-inch model is also certified. </user/hardware/certified-hardware/novacustom-v56-series>`

Screen resolution
^^^^^^^^^^^^^^^^^


- Certified: Full HD+ (1920 x 1200)

- Certified: 2.8K (2880 x 1800)



Processor and graphics
^^^^^^^^^^^^^^^^^^^^^^


- Certified: Intel Core Ultra 5 Processor 125H, Intel Arc iGPU with AI Boost

- Certified: Intel Core Ultra 7 Processor 155H, Intel Arc iGPU with AI Boost

- The Nvidia discrete GPU options are not currently certified.



Memory
^^^^^^


- Certified: Any configuration with at least 16 GB of memory



Storage
^^^^^^^


- Certified: All of the available options in these sections



Personalization
^^^^^^^^^^^^^^^


- This section is merely cosmetic and therefore does not affect certification.



Firmware options
^^^^^^^^^^^^^^^^


- Qubes OS does not currently support UEFI secure boot.

- The option to be kept up to date with firmware updates is merely an email notification service and therefore does not affect certification.

- Certified: coreboot+EDK-II

- Certified: coreboot+Heads

- Disabling Intel Management Engine (HAP disabling) does not affect certification.



Operating system
^^^^^^^^^^^^^^^^


- Certified: Qubes OS 4.2.4 or newer (within Release 4).

- Releases older than 4.2.4 are not certified.

- You may choose either to have NovaCustom preinstall Qubes OS for you, or you may choose to install Qubes OS yourself. This choice does not affect certification.



Wi-Fi and Bluetooth
^^^^^^^^^^^^^^^^^^^


- Certified: Intel AX-210/211 (non vPro) Wi-Fi module 2.4 Gbps, 802.11AX/Wi-Fi6E + Bluetooth 5.3

- Certified: Intel BE200 (non vPro) Wi-Fi module 5.8 Gbps, 802.11BE/Wi-Fi7 + Bluetooth 5.42

- Certified: No Wi-Fi chip – no Bluetooth and Wi-Fi connection possible (only with USB adapter)



Disclaimers
-----------


- In order for Wi-Fi to function properly, ``sys-net`` must currently be based on a Fedora template. The firmware package in Debian templates is currently too old for the certified Wi-Fi cards.

- Currently requires ``kernel-latest``: If you install Qubes OS yourself, you must select the ``Install Qubes OS RX using kernel-latest`` option on the GRUB menu when booting the installer. This non-default kernel option is currently required for the NovaCustom V54 Series to function properly.

- Due to a `known bug <https://github.com/Dasharo/dasharo-issues/issues/976>`__, the bottom-right USB-C port is currently limited to USB 2.0 speeds.



.. |Photo of the NovaCustom V54 Series 14.0 inch coreboot laptop| image:: /attachment/site/novacustom-v54-series.png
   :target: https://novacustom.com/product/v54-series/
