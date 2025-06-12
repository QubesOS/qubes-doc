---
lang: en
layout: doc
permalink: /doc/certified-hardware/nitropc-pro/
title: NitroPC Pro
image: /attachment/posts/nitropc-pro.jpg
ref: 356
---

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Note:</b> When configuring your NitroPC Pro 2 on the Nitrokey website, there is an option for a discrete graphics card (e.g., Nvidia GeForce RTX 4070 or 4090) in addition to integrated graphics (e.g., Intel UHD 770, which is always included because it is physically built into the CPU). NitroPC Pro 2 configurations that include discrete graphics cards are <em>not</em> Qubes-certified. The only NitroPC Pro 2 configurations that are Qubes-certified are those that contain <em>only</em> integrated graphics.
</div>

<div class="alert alert-warning" role="alert">
  <i class="fa fa-exclamation-circle"></i>
  <b>Note:</b> Only the "Dasharo TianoCore UEFI without Measured Boot, without Nitrokey" firmware option is certified. The "HEADS with Measured Boot, requires Nitrokey!" firmware option is <em>not</em> certified.
</div>

The [NitroPC Pro](https://web.archive.org/web/20231027112856/https://shop.nitrokey.com/shop/product/nitropc-pro-523) is [officially certified](/doc/certified-hardware/) for Qubes OS Release 4.

[![Photo of NitroPC Pro](/attachment/posts/nitropc-pro.jpg)](https://shop.nitrokey.com/shop/product/nitropc-pro-523)

Here's a summary of the main component options available for this mid-tower desktop PC:

| Component                    | Options                                                  |
|----------------------------- | -------------------------------------------------------- |
| Motherboard                  | MSI PRO Z690-A DDR5 (Wi-Fi optional)                     |
| Processor                    | 12th Generation Intel Core i5-12600K or i9-12900K        |
| Memory                       | 16 GB to 128 GB DDR5                                     |
| NVMe storage (optional)      | Up to two NVMe PCIe 4.0 x4 SSDs, up to 2 TB each         |
| SATA storage (optional)      | Up to two SATA SSDs, up to 7.68 TB each                  |
| Wireless (optional)          | Wi-Fi 6E, 2400 Mbps, 802.11/a/b/g/n/ac/ax, Bluetooth 5.2 |
| Operating system (optional)  | Qubes OS 4.1 or Ubuntu 22.04 LTS                         |

Of special note for Qubes users, the NitroPC Pro features a combined PS/2 port that supports both a PS/2 keyboard and a PS/2 mouse simultaneously with a Y-cable (not included). This allows for full control of dom0 without the need for USB keyboard or mouse passthrough. Nitrokey also offers a special tamper-evident shipping method for an additional fee. With this option, the case screws will be individually sealed and photographed, and the NitroPC Pro will be packed inside a sealed bag. Photographs of the seals will be sent to you by email, which you can use to determine whether the case was opened during transit.

The NitroPC Pro also comes with a "Dasharo Entry Subscription," which includes the following:

- Accesses to the latest firmware releases
- Exclusive newsletter
- Special firmware updates, including early access to updates enhancing privacy, security, performance, and compatibility
- Early access to new firmware releases for [newly-supported desktop platforms](https://docs.dasharo.com/variants/overview/#desktop) (please see the [roadmap](https://github.com/Dasharo/presentations/blob/main/archive/dug_2/dug2_dasharo_roadmap.md#dasharo-desktop-roadmap))
- Access to the Dasharo Premier Support invite-only live chat channel on the Matrix network, allowing direct access to the Dasharo Team and fellow subscribers with personalized and priority assistance
- Insider's view and influence on the Dasharo feature roadmap for a real impact on Dasharo development
- [Dasharo Tools Suite Entry Subscription](https://docs.dasharo.com/osf-trivia-list/dts/#what-is-dasharo-tools-suite-supporters-entrance) keys

For further product details, please see the official [NitroPC Pro](https://shop.nitrokey.com/shop/product/nitropc-pro-523) page.
