---
lang: en
layout: doc
permalink: /doc/certified-hardware/novacustom-nv41-series/
title: NovaCustom NV41 Series
image: /attachment/site/novacustom-nv41-series.png
ref: 357
---

The [NovaCustom NV41 Series](https://novacustom.com/product/nv41-series/) is [officially certified](/doc/certified-hardware/) for Qubes OS Release 4.

[![Photo of the NovaCustom NV41 Series](/attachment/site/novacustom-nv41-series.png)](https://novacustom.com/product/nv41-series/)

## Qubes-certified configurations

The following configuration options are certified for Qubes OS Release 4:

Processor:
- Intel Core i5-1240P processor
- Intel Core i7-1260P processor

Memory:
- 2 x 16 GB Kingston DDR4 SODIMM 3200 MHz (32 GB total)
- 1 x 32 GB Kingston DDR4 SODIMM 3200 MHz (32 GB total)
- 2 x 32 GB Kingston DDR4 SODIMM 3200 MHz (64 GB total)

M.2 storage chip:
- Samsung 980 SSD (all capacities)
- Samsung 980 Pro SSD (all capacities)

Wi-Fi and Bluetooth:
- Intel AX-200/201 Wi-Fi module 2976 Mbps, 802.11ax/Wi-Fi 6 + Bluetooth 5.2
- Killer (Intel) Wireless-AX 1675x M.2 Wi-Fi module 802.11ax/Wi-Fi 6E + Bluetooth 5.3
- Blob-free: Qualcomm Atheros QCNFA222 Wi-Fi 802.11a/b/g/n + Bluetooth 4.0
- No Wi-Fi/Bluetooth chip

### Notes on Wi-Fi and Bluetooth options

- When viewed in a Linux environment with `lspci`, the "Killer (Intel) Wireless-AX 1675x M.2 Wi-Fi module 802.11ax/Wi-Fi 6E + Bluetooth 5.3" device displays the model number "AX210." However, according to its [Intel Ark entry](https://ark.intel.com/content/www/us/en/ark/products/211485/intel-killer-wifi-6e-ax1675-xw.html) (in the "Product Brief" file), they are actually the same Wi-Fi module.

- Similarly, when viewed in a Linux environment with `lspci`, the "Blob-free: Qualcomm Atheros QCNFA222 Wi-Fi 802.11a/b/g/n + Bluetooth 4.0" device displays the model number "AR9462," which seems to be just the Wi-Fi chip model number, whereas "QCNFA222" seems to be the model number of the whole device (which include Bluetooth). Meanwhile, the Bluetooth device presents itself as "IMC Networks Device 3487."

- The term "blob-free" is used in different ways. In practice, being "blob-free" generally does *not* mean that the device does not use any closed-source firmware "blobs." Rather, it means that the device comes with firmware *preinstalled* so that it does not have to be loaded from the operating system. In theory, the preinstalled firmware could be open-source, but as far as we know, that is not the case with this particular Atheros Wi-Fi/Bluetooth module. (Qualcomm has published firmware source code in the past, but only for other device models, as far as we are aware.) Meanwhile, the Free Software Foundation (FSF) [considers](https://www.gnu.org/philosophy/free-hardware-designs.en.html#boundary) unmodifiable preinstalled firmware to be part of the hardware, hence they regard such hardware as "blob-free" from a software perspective. While common usage of the term "blob-free" often follows the FSF's interpretation, it is worthwhile for Qubes users who are concerned about closed-source firmware to understand the nuance.
