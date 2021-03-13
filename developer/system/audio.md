---
layout: doc
title: Audio Virtualization
permalink: /doc/audio-virtualization/
---

Audio Virtualization
====================

VMs on Qubes OS have access to virtualized audio through the PulseAudio module.
It consists of two parts:

- `pacat-simple-vchan` running in a dom0/Audio VM (standalone application, one per VM, connected to the PulseAudio daemon)
- `module-vchan-sink` running in a VM (loaded into the PulseAudio process)

Protocol
--------

The protocol between these two parts is designed to be as simple as possible.
Specifically, there is no audio format negotiation, no compression, etc.
All the audio data is transferred as raw 44.1kHz samples in S16LE format, 2 channels.

These two parts are connected with two vchan links:

1. Connection on vchan port 4713 used to transfer audio from VM to dom0/Audio VM.
   There is no negotiation, no headers, etc.
   Only raw samples are sent over this channel.
2. Connection on vchan port 4714 used to transfer audio from dom0/Audio VM to VM.
   Like the previous one, audio data is sent as raw samples.

Additionally, the second vchan connection (on port 4714) is used in the opposite direction (VM to dom0) to send simple notifications/commands about the audio state.
Each such notification is a 4-byte number in little-endian format.

List of defined codes:

- `0x00010001` -- VM wants to receive audio input (some process is listening); prior to this message, `pacat-simple-vchan` will not send any audio samples to the VM.
- `0x00010000` -- VM does not want to receive audio input (no process is listening anymore); after this message, `pacat-simple-vchan` will not send any audio samples to the VM.
- `0x00020000` -- VM does not want to send audio output; informational for dom0, to avoid buffer under runs (may affect PulseAudio calculated delays).
- `0x00020001` -- VM does want to send audio output.

pacat-simple-vchan
------------------

This is the dom0 (or Audio VM) part of the audio virtualization.
It is responsible for transferring audio samples between the PulseAudio daemon in dom0/Audio VM (which has access to the actual audio hardware) and a VM playing/recording sounds.
A separate `pacat-simple-vchan` process runs in dom0 for each VM with audio.
Each of them opens separate input and output streams to their local PulseAudio, which allows for controlling the volume of each VM separately (using the `pavucontrol` tool, for example).
In order to (re)create a stream for a VM in dom0, `pacat-simple-vchan` can be used. In order to find the needed parameters, domid and domain name, the command `xl list` can be used.

Audio input to the VM is not sent by default.
It needs to be both requested by the VM part and explicitly enabled in `pacat-simple-vchan`.
The mechanism to do this differs between Qubes versions.
In Qubes before R4.1, `pacat-simple-vchan` is controlled over system D-Bus:

- destination: `org.qubesos.Audio.VMNAME` (where `VMNAME` is the VM's name)
- object path: `/org/qubesos/audio`
- interface: `org.qubesos.Audio`
- property: `RecAllowed` (which can be set using the `org.freedesktop.DBus.Properties` interface)

In Qubes R4.1 and later, `pacat-simple-vchan` is controlled over a UNIX socket at `/var/run/qubes/audio-control.VMNAME` (where `VMNAME` is the VM's name).
Supported commands:

- `audio-input 1\n` - enable audio input
- `audio-input 0\n` - disable audio input

These commands can be sent using the `qubes.AudioInputEnable+VMNAME` and `qubes.AudioInputDisable+VMNAME` qrexec services, respectively.
The current status is written into QubesDB at `/audio-input/VMNAME` (where `VMNAME` is the VM's name) with either `1` or `0` values.
The lack of a key means that the `pacat-simple-vchan` for a given VM is not running.

In either version, it is exposed to the user as device of class `mic`, which can be attached to a VM (for example, using the `qvm-device mic` command).
