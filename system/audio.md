---
layout: doc
title: Audio virtualization
permalink: /doc/audio-virtualization/
---

Qubes audio virtualization - internals
======================================

VMs on Qubes OS have access to virtualized audio through Pulseaudio module.
It consists of two parts:

 - `pacat-simple-vchan` running in a dom0/Audio VM (standalone application, one per VM, connected to PulseAudio daemon)
 - `module-vchan-sink` running in a VM (loaded into PulseAudio process)

Protocol
--------

The protocol between those two is designed to be as simple as possible.
Specifically, there is no audio format negotiation, no compression etc. All the audio data is transferred as raw 44.1kHz samples in S16LE format, 2 channels.

Those two parts are connected with two vchan links:

1. Connection on vchan port 4713 used to transfer audio from VM to Dom0/Audio VM. There is no negotiation, headers etc - raw samples are sent over this channel.
2. Connection on vchan port 4714 used to transfer audio from Dom0/Audio VM to VM. Similar to previous one, audio data is sent as raw samples.

Additionally, the second vchan connection (on port 4714) is used in the opposite direction (VM->dom0) to send simple notifications/commands about audio state. Each such notification is a 4-bytes number in little-endian format.

List of defined codes:

 - `0x00010001` - VM want to receive audio input (some process is listening); prior to this message, `pacat-simple-vchan` will not send any audio samples to the VM
 - `0x00010000` - VM do not want to receive audio input (no process is listening anymore); after this message, `pacat-simple-vchan` will not send any audio samples to the VM
 - `0x00020000` - VM do not want to send audio output; informational for dom0, to avoid buffer under runs (may affect pulseaudio calculated delays)
 - `0x00020001` - VM do want to send audio output

pacat-simple-vchan
------------------

Dom0 (or Audio VM) part of the audio virtualization. It is responsible for transferring audio samples between pulseaudio daemon in Dom0/Audio VM (having access to actual audio hardware) and a VM playing/recording.
For each VM, matching `pacat-simple-vchan` process is running. Each of them open a separate input and output streams to local pulseaudio, which allows to control volume of each VM separately (using `pavucontrol` tool for example).

Audio input to the VM is not sent by default. It needs to be both requested by the VM part and explicitly enabled in `pacat-simple-vchan`. Mechanism to do that differs between Qubes versions.
In Qubes before R4.1, `pacat-simple-vchan` is controlled over system D-Bus:

  - destination: `org.qubesos.Audio.VMNAME` (with `VMNAME` replaces with actual VM name)
  - object path: `/org/qubesos/audio`
  - interface: `org.qubesos.Audio`
  - property: `RecAllowed` (settable using `org.freedesktop.DBus.Properties` interface)

In Qubes R4.1 or later, `pacat-simple-vchan` is controlled over a UNIX socket at `/var/run/qubes/audio-control.VMNAME` (with `VMNAME` replaces with actual VM name). Supported commands:

  - `audio-input 1\n` - enable audio input
  - `audio-input 0\n` - disable audio input

Those commands can be send using `qubes.AudioInputEnable+VMNAME` and `qubes.AudioInputDisable+VMNAME` qrexec services respectively.
The current status is written into QubesDB at `/audio-input/VMNAME` (with `VMNAME` replaces with actual VM name) with values either `1` or `0`. Lack of the key means the `pacat-simple-vchan` for given VM is not running.

In either version, it is exposed to the user as device of class `mic`, which can be attached to a VM (for example using `qvm-device mic` command).
