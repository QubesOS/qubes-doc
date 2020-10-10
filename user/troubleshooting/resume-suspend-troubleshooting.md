---
layout: doc
title: Suspend/Resume Troubleshooting
permalink: /doc/suspend-resume-troubleshooting/
redirect_from:
- /en/doc/wireless-troubleshooting/
- /doc/wireless-troubleshooting/
---

# Troubleshooting problems relating to suspend/resume #

## Network-Manager says “Device not ready” after suspend/resume ##

These instructions may help with suspend/resume issues for more devices than just wireless cards, that is just the (unfortunately not uncommon) example used here.

If your wireless card works, but after suspending and resuming your computer, the Network-Manager applet just says "Device not ready", then try un-loading and re-loading the driver.

### Determining your wireless card driver ###

First, determine which kernel module corresponds to your wireless card. There are several ways to do this.

The easiest is via the output of `lspci -k` in your sys-net VM:

~~~
[user@sys-net ~]$ lspci -k
00:00.0 Network controller: Intel Corporation Wireless 8260 (rev 3a)
	Subsystem: Intel Corporation Device 0130
	Kernel driver in use: iwlwifi
	Kernel modules: iwlwifi
~~~

Here we see that the machine in question has an Intel wireless card, being used by the `iwlwifi` kernel module.


### Checking logs for relevant messages ###

View the output of `dmesg` in sys-net, and check if you see a bunch of wireless related errors. Depending on your hardware, they may look like the following (or not):

~~~
iwlwifi 0000:00:00.0: loaded firmware version 16.242414.0 op_mode iwlmvm
iwlwifi 0000:00:00.0: Detected Intel(R) Dual Band Wireless AC 8260, REV=0x208
...
IPv6: ADDRCONF(NETDEV_UP): wlp0s0: link is not ready
iwlwifi 0000:00:00.0: L1 Enabled - LTR Enabled
iwlwifi 0000:00:00.0: L1 Enabled - LTR Enabled
iwlwifi 0000:00:00.0: Failed to load firmware chunk!
iwlwifi 0000:00:00.0: Could not load the [0] uCode section
iwlwifi 0000:00:00.0: Failed to start INIT ucode: -110
iwlwifi 0000:00:00.0: Failed to run INIT ucode: -110
...
iwlwifi 0000:00:00.0: Direct firmware load for iwlwifi-8000C-18.ucode failed with error -2
~~~

### Seeing what modules you have loaded ###

You can check which drivers are currently loaded with `lsmod`, and view details about a module with `modinfo <module_name>`.

For example, we list what modules we have loaded:

~~~
[user@sys-net ~]$ lsmod
Module                  Size  Used by
iwlmvm                315392  0
iwlwifi               155648  1 iwlmvm
mac80211              708608  1 iwlmvm
cfg80211              557056  3 iwlwifi,mac80211,iwlmvm
...
~~~

and check one:

~~~
[user@sys-net ~]$ modinfo iwlmvm | grep -E '^(description|author|depends):'
author:         Copyright(c) 2003- 2015 Intel Corporation <ilw@linux.intel.com>
description:    The new Intel(R) wireless AGN driver for Linux
depends:        iwlwifi,mac80211,cfg80211
~~~

Hey, it's our wireless driver!

Now, check if reloading the module makes wireless work again:

~~~
[user@sys-net ~]$ sudo rmmod iwlmvm
[user@sys-net ~]$ sudo modprobe iwlmvm
~~~

and try reconnecting to a network that is known to work.

If that is successful, see below about having Qubes automatically reload the driver for you. If not, try also reloading some dependent modules, in our example we must also reload iwlwifi:

~~~
[user@sys-net ~]$ modinfo iwlwifi | grep -E '^(description|author|depends):'
author:         Copyright(c) 2003- 2015 Intel Corporation <ilw@linux.intel.com>
description:    Intel(R) Wireless WiFi driver for Linux
depends:        cfg80211
~~~

~~~
[user@sys-net ~]$ sudo rmmod iwlmvm
[user@sys-net ~]$ sudo rmmod iwlwifi
[user@sys-net ~]$ sudo modprobe iwlwifi # note the reverse order of loading/unloading
[user@sys-net ~]$ sudo modprobe iwlmvm
~~~

## Drivers do not reload automatically on suspend/resume ##

If reloading the driver (which resets the hardware into a known-state) resolves your issue when done manually, you can have Qubes automatically un/reload them on suspend & resume by listing the relevant modules in `/rw/config/suspend-module-blacklist`.

In the above example, it would look like this:

~~~
[user@sys-net config]$ cat /rw/config/suspend-module-blacklist
# You can list here modules you want to be unloaded before going to sleep. This
# file is used only if the VM has any PCI device assigned. Modules will be
# automatically loaded after resume.
iwlmvm
iwlwifi
~~~

## Power consumption increases after suspend/resume ##

This problem is related to the software method used to disable sibling threads and how it interacts with suspend/resume. 
To solve the problem, disable hyperthreading in the BIOS. This [external guide](https://www.pcmag.com/news/how-to-disable-hyperthreading) explains how to disable hyperthreading. 
Since Qubes does disable hyperthreading by default (by not using secondary threads), you won't pay any performance cost.
