---
layout: doc
title: Qubes-Certified Laptops
permalink: /doc/certified-laptops/
--- 

Qubes-certified Laptops
============================================

Qubes-certified laptops are laptops that have been tested by the Qubes developers to ensure compatibility with all of Qubes' features.

We aim to partner with a few select computer makers to ensure that Qubes is compatible with them, so that new users have clear path towards getting started with Qubes if they desire. We aim for these makers to be as diverse as possible in terms of geography, cost, and availability. 


Purism Librem 13
----------------------------
[![image of Librem 13](https://puri.sm/wp-content/uploads/2015/07/librem-13-700x490-20150721.png)](https://puri.sm/librem-13/)

For users now who seek to buy a Librem 13, there will be an option to have Qubes pre-installed on their Librem 13. This will include all the necessary tweaks for maximum compatibility with Qubes. 

In addition, the Qubes team will receive a small portion of the revenue from any Librem 13 sale that come with Qubes pre-installed.

For existing Librem 13 users, please follow the instructions to ensure maximum compatibility with Qubes:

1. In `dom0`, open a terminal and type:

       sudo qubes-dom0-update --releasever=3.1 xorg-x11-drivers xorg-x11-drv-intel

2. (optional) Enable newer kernel:

       sudo qubes-dom0-update --enablerepo=qubes-dom0-unstable kernel
