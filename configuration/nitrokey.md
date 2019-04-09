---
layout: doc
title: Nitrokey
permalink: /doc/nitrokey/
---

# Nitrokey #

To use a nitrokey on QubeOS, a USB passhrough is required.

This means, you need to have a sys-usb VM.

This is mentioned in the Qubes Documentation [USB](/doc/usb-devices/#installation-of-qubes-usb-proxy).

```
Note, you cannot pass through devices from dom0
(in other words: a USB VM is required).
```

If you are using a USB keyboard, the sys-usb VM is not installed by default.

If you are using a USB keyboard, you have 2 options:

- Create a sys-usb VM and assign a USB Controller to it.
- If you can't assign a USB Controller (ex: You only have 1 on your computer and can’t buy another), then buy and use a PS/2 Keyboard.
