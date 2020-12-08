---
layout: doc
title: External Audio
redirect_to: https://github.com/Qubes-Community/Contents/blob/master/docs/configuration/external-audio.md
redirect_from:
- /doc/external-audio/
- /en/doc/external-audio/
- /doc/ExternalAudio/
- /wiki/ExternalAudio/
---

Using External Audio Devices
============================

Why you want to use external audio devices
------------------------------------------

Qubes audio virtualization protocol does not implement latency reporting for security reasons, keeping the protocol as simple as possible.
Also, in a compromise between low latency and low CPU usage, latency may be around 200 ms.
So applications demanding higher audio quality (even Skype) need a better environment.
But Qubes flexibility fully allows that using external audio devices. 
These are mostly USB audio cards, but firewire devices also might be used.

Implementing external audio devices
-----------------------------------

First you need to identify an user VM dedicated to audio and [assign a device](/doc/AssigningDevices) to it.
In the most common case the assigned device is the USB controller to which your USB audio card will be connected.

### Fedora VMs

In a terminal of the template from which you user VM depends, install pavucontrol with:

~~~
sudo dnf install pavucontrol
~~~

Close the template and start or restart your user VM, insert your external audio device, open a terminal and prepare pulseaudio to use it with:

~~~
sudo chmod a+rw /dev/snd/*
pactl load-module module-udev-detect
~~~

Start the audio application that is going to use the external audio device.

Launch pavucontrol, for example using "run command in VM" of Qubes Manager and select your external audio card in pavucontrol.
You need to do that only the first time you use a new external audio device, then pulse audio will remember your selection.

If you detach your external audio device, then want to insert it again (or want to change it with another one), you need to repeat the previous commands in terminal adding another line at the beginning:

~~~
pactl unload-module module-udev-detect
sudo chmod a+rw /dev/snd/*
pactl load-module module-udev-detect
~~~
