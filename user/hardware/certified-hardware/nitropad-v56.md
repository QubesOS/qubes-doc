---
lang: en
layout: doc
permalink: /doc/certified-hardware/nitropad-v56/
title: NitroPad V56
image: /attachment/site/nitropad-v56.png
---

The [NitroPad V56](https://shop.nitrokey.com/shop/nitropad-v56-684) from [Nitrokey](https://www.nitrokey.com/) is [officially certified](/doc/certified-hardware/) for Qubes OS Release 4.

## Secure working in insecure environments thanks to unique hardware protection

Do you believe that your computer hardware is secure? Can you rule out the possibility that someone has tampered with your computer in your absence? In a world where most users have no real control over their hardware and must blindly trust manufacturers' security promises, NitroPad offers a refreshingly new security experience. The NitroPad is significantly more secure than normal computers. NitroPad gives you more control over your hardware and data than ever before, while making it easy to use.

[![Photo of the NitroPad V56](/attachment/site/nitropad-v56.png)](https://shop.nitrokey.com/shop/nitropad-v56-684)

## Qubes-certified options

The configuration options required for Qubes certification are detailed below.

### Processor and graphics card

- Certified: Intel Core Ultra 5 Processor 125H, Intel Arc iGPU with AI Boost
- Certified: Intel Core Ultra 7 Processor 155H, Intel Arc iGPU with AI Boost
- The Nvidia GPU options are not currently certified.

### Memory (RAM) DDR5, 5600 MHz

- Certified: All options 16 GB (2x8 GB) and higher


### 1st Hard Disk SSD NVMe PCIe 4.0 x4

- Certified: Any of the available options in this section

### 2nd Hard Disk SSD NVMe PCIe 4.0 x4

- Certified: Any of the available options in this section

### Keyboard

- Certified: Any of the available options in this section

### Wireless interfaces

- Certified: Wi-Fi 6E + Bluetooth 5.3, Intel AX-210/211 (non vPro) WLAN module 2.4 Gbps, 802.11ax
- Certified: Wi-Fi 7 + Bluetooth 5.42, Intel BE200 (non vPro) WLAN module 5.8 Gbps, 802.11be
- Certified: No wireless

### Webcam and microphone

- Certified: Any of the available options in this section

### Type

- Certified: Any of the available options in this section

### Firmware

- Certified: Dasharo TianoCore UEFI without Measured boot, without Nitrokey
- The option "Dasharo HEADS with Measured Boot, requires Nitrokey!" is not yet certified.

### Operating system

- Certified: Qubes OS 4.2.3 or newer (within Release 4).
- Releases older than 4.2.3 are not certified.
- You may choose either to have Nitrokey preinstall Qubes OS for you, or you may choose to install Qubes OS yourself. This choice does not affect certification.

### Nitrokey

- Certified: None -- for TianoCore only!
- The Nitrokey options are currently not applicable to Qubes hardware certification. (See the Firmware section above.)

### Shipment of Nitrokey

- This section does not affect Qubes hardware certification.

### Tamper-evident packaging

- This section does not affect Qubes hardware certification.

## Disclaimers

- In order for Wi-Fi to function properly, `sys-net` must currently be based on a Fedora template. The firmware package in Debian templates is currently too old for the certified Wi-Fi cards.
- Currently requires `kernel-latest`: If you install Qubes OS yourself, you must select the `Install Qubes OS RX using kernel-latest` option on the GRUB menu when booting the installer. This non-default kernel option is currently required for the NitroPad V56 to function properly.
- Due to a [known bug](https://github.com/Dasharo/dasharo-issues/issues/976), the bottom-right USB-C port is currently limited to USB 2.0 speeds.
