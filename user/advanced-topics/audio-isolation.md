---
lang: en
layout: doc
permalink: /doc/sys-audio/
ref: 179
title: Dedicated VM for audio-isolation (sys-audio)
---

# Introduction

## General Concept
In Qubes, all VMs output sound to a virtual stream. By default, dom0 collects all these streams and relays them to the sound-device. This has the advantage of a very simple, robust setup. However, it requires dom0 to handle the sound card (a pci-device) and disables any additional sound devices. Since bluetooth-headsets are common or a broken sound-card requires using a USB-sound-device, a more flexible solution may be desirable.

## Setup Goals
A successful setup with this guide will provide a dedicated VM for sound processing. All VMs will output their sound through the new VM instead of dom0. New audio-devices can be added (e.g. via `qvm-usb`) and used as physical output. Microphone capability will be available as before.

## Caveats
Qubes 4.2 switched from pipewire to pulseaudio. Apart from some details (installed packages, required permissions), this doesn't seem to affect user experience at all.

The volume-tray-icon doesn't work for audio-VMs at the moment.

Some systems integrate a sound-card with the graphics card. There is usually another, normal sound card available. If for any reason you want to use the sound-card integrated in your graphics card, see whether the sound-card is a dedicated PCI-device. This would result in a partial PCI-device passed through to your audio-VM, which may result in unstable behaviour. However, if this isn't possible for you and using the sound-card on your GPU is necessary, you may have to stick with dom0 as audio-VM.

Keyboard-shortcuts won't work, as the keyboard is attached to dom0 and not your audio-VM. However, the most important shortcuts can be replicated with commandline-bindings.

# Setup
## Choosing A Template
Generally speaking there is no reason to choose any particular template, as long as it's up to date. The only real choice here is whether a minimal-template is more to your liking. All commands will assume a minimal-template, so you will install all required packages.

The guide is written with/for a `fedora-38-minimal` template in particular.

### Install Required Packages
In your template-VM run:

```
dnf install qubes-audio-daemon pulseaudio-utils notification-daemon pavucontrol qubes-core-admin-client qubes-gui-daemon pipewire
```

**optional**  
for bluetooth-support: `blueman qubes-usb-proxy`  
for audio-USB-support: `qubes-usb-proxy`  

Additionally, `pulseaudio-utils` is technically optional, but a great help in debugging and used to implement volume-change keyboard shortcuts.

## Create An Audio-VM Based On The Template
Nothing special, use the `Create New Qube` gui or create a new VM from commandline. Just make sure it's based on the template of the previous step!

This guide will assume the audio-VM is called `sys-audio`.

### Add Service
In the new VM's settings, **add a new service called `audiovm`**. Missing this step will cause hard-to-debug problems!

## Create Permissions
Open the Qubes Policy Editor. Click `File` -> `New` -> choose a name, but start with `50-`, e.g. `50-sys-audio`. It will contain all audio-service related rules.

In the new file, enter these rules:
```
admin.Events                        *                            sys-audio    sys-audio              allow target=dom0
admin.Events                        *                            sys-audio    @adminvm               allow target=dom0
admin.Events                        *                            sys-audio    @tag:audiovm-sys-audio allow target=dom0
admin.vm.CurrentState               *                            sys-audio    sys-audio              allow target=dom0
admin.vm.CurrentState               *                            sys-audio    @adminvm               allow target=dom0
admin.vm.CurrentState               *                            sys-audio    @tag:audiovm-sys-audio allow target=dom0
admin.vm.listening                  *                            sys-audio    sys-audio              allow target=dom0
admin.vm.List                       *                            sys-audio    @adminvm               allow target=dom0
admin.vm.List                       *                            sys-audio    @tag:audiovm-sys-audio allow target=dom0
admin.vm.property.Get               +audiovm                     sys-audio    @tag:audiovm-sys-audio allow target=dom0
admin.vm.property.Get               +xid                         sys-audio    @tag:audiovm-sys-audio allow target=dom0
admin.vm.property.Get               +stubdom_xid                 sys-audio    @tag:audiovm-sys-audio allow target=dom0
#admin.vm.feature.CheckWithTemplate *                            sys-audio    @tag:audiovm-sys-audio allow target=dom0
admin.vm.feature.CheckWithTemplate  +audio-model                 sys-audio    @tag:audiovm-sys-audio allow target=dom0
admin.vm.feature.CheckWithTemplate  +audio                       sys-audio    @tag:audiovm-sys-audio allow target=dom0
admin.vm.feature.CheckWithTemplate  +supported-service.pipewire  sys-audio    @tag:audiovm-sys-audio allow target=dom0
admin.vm.feature.CheckWithTemplate  +audio-low-latency           sys-audio    @tag:audiovm-sys-audio allow target=dom0
admin.vm.property.GetAll            *                            sys-audio    sys-audio              allow target=dom0
admin.vm.property.GetAll            *                            sys-audio    @adminvm               allow target=dom0
admin.vm.property.GetAll            *                            sys-audio    @tag:audiovm-sys-audio allow target=dom0
```
Make sure to adapt all permissions to your chosen audio-VM-name, including all `@tag:audiovm-sys-audio` to `@tag:audiovm-[your audio-VM name]`

### Attach Devices
You need to attach some physical output device. This is most likely a pci-device, but feel free to already attach you bluetooth-device!

Identify your sound-card by executing in **dom0**:

```
qvm-pci | grep -i audio
```
It should yield something like:
```
dom0:00_2f.1  Audio device: Intel Corporation Raptor Lake-N/V/K
```
Make sure it's not already attached to a VM!

Attach the device persistently to the audio-VM:
```
qvm-pci a sys-audio dom0:00_2f.1 --persistent -o no-strict-reset=true
```
If you were listening to music, it should stop now.

## Test Setup With Powered-Down Qube!
Choose a VM to test the audio-VM. It should be able to play some kind of sound, so make sure it contains some kind of media-file or can access youtube or similar.

**Make sure the audio-VM has started!**

Before starting, set the `audiovm`-preference of this VM! In dom0 run:
```
qvm-prefs [test-VM name] audiovm sys-audio
```
Now start the VM and play some sound. If you can't hear anything or the stream won't start, jump to troubleshooting!



If it works, go ahead and set sys-audio as the default audio-vm for your system:
```
qubes-prefs default_audiovm sys-audio
```

At this point, every VM that starts will connect to your audio-VM, but all VMs already running will still try to reach dom0, which should not accept any audio anymore. So make sure to either restart all VMs with relevant audio-streams or do a full reboot.

# Caveats / Improvements
At the moment, there is no working implementation of the small volume tray-icon. The icon you still see in your panel's tray area is dom0's PulseAudio Plugin. I recommend removing it to avoid confusion.

### Getting Mouse-Control For Volume
The easiest method is to run pavucontrol form sys-audio and keep the window around. The 'Output Devices'-tab allows easy control by hovering over the (active) volume control bar and using the mouse-wheel.

You can make this a lot easier by adding 'PulseAudio Volume Control' to your audio-VM in the Applications-settings.

### Getting Keyboard-Control For Volume
Since the keyboard is attached to dom0, you need to build a solution in dom0. The approach chosen is to run a command in the audio-VM and bind those to shortcuts in xfce.

The basic commands to use use the `pactl`-interface, so make sure you have the `pulseaudio-utils`-package installed!

Test basic functionality first:

 1. Open PulseAudio Volume Control (`pavucontrol`) and have the 'Output Devices'-tab visible to see any changes on the volume-control.
 2. In dom0, run `qvm-run sys-audio 'pactl set-sink-volume @DEFAULT_SINK@ -10%'`
 3. Confirm the volume decreased. If it didn't, make sure your default audio-device is visible (you may have to scroll).
 4. Troubleshooting: Try the command in your audio-VM `pactl set-sink-volume @DEFAULT_SINK@ -10%` and if it didn't work, read the error-message carefully.

Once this works, open up your keyboard settings in dom0, navigate to the 'Application Shortcuts' - tab.

 1. Click '+ Add'
 2. Set the command to `qvm-run sys-audio 'pactl set-sink-volume @DEFAULT_SINK@ -3%'` (3% is a nice value for me, set to your own taste)
 3. After clicking 'OK', hit whatever key-combo you'd like to use. You CAN use volume-down media keys!
 4. Repeat for volume-up. Here is the command: `qvm-run sys-audio 'pactl set-sink-volume @DEFAULT_SINK@ +3%'` (it's just `+` instead of `-`)
 5. Don't forget the `+`/`-`!
 6. If you want to do mute, the command is `qvm-run sys-audio 'pactl set-sink-mute @DEFAULT_SINK@ toggle'`
 7. If any of the commands don't immediately work, try to run `killall pulseaudio` in dom0. There seems to be some race between pulse and xfce to resolve media-keys.

### USB Audio Devices
Should be supported out of the box, as long as `qubes-usb-proxy` is installed in the audio-VM's template. Use the device-manager to attach the USB-device to the audio-VM and select it in the PulseAudio Volume Control.

### Bluetooth Devices
Generally speaking, bluetooth audio devices are supported without any unexpected difficulty. But there may be some expected difficulties.

 1. In the audio-VM's template both these packages need to be installed: `qubes-usb-proxy` and `blueman`.
 2. You need to identify your bluetooth-device. It is usually registered as a USB-device with a number instead of a name. Run `qvm-usb` in dom0 and if you can't see any device obviously doing bluetooth, check the numbered devices with a web-search. One should turn out to be the device-identifier of a bluetooth device.
 3. Attach that device to the audio-VM. Persistently attaching is an option: it allows auto-starting blueman after boot but can cause problems if the USB-devices get different numbers when starting the USB-proxy and disables attaching the bluetooth-device to another VM. (while the audio-VM is running, which should be most of the time.)
 4. With an attached bluetooth-device, run `blueman-manager` in your audio-VM. This should start a simple window to search for, pair, and use your bluetooth-devices. If this doesn't appear, make sure the bluetooth-device is correctly attached to the audio-VM. Run `lsusb` in the audio-VM to see whether it exists.

# Troubleshooting
### Streams Don't Start
If streams don't move, that means pulseaudio doesn't see an intact sink. This is hard to debug, but has some common causes to check:

 * Make sure the VM's `audiovm` property (or global `qubes-prefs default_audiovm`) is set correctly, check for typos!
 * Make sure all mentioned packages are installed in the audio-vm. Try using a non-minimal fedora-template!
 * Ensure audio-vm is started and running BEFORE starting the VM with a stream. If some VMs can play streams and others don't, restart the VMs that can't play.
 * If the `pavucontrol` command fails in the audio-vm, there may be a pulseaudio-issue. It may even be a driver issue, in which case reverting to dom0 as audiovm is your best bet.

### Streams Seem To Play, But No Audio
If streams play but there is no sound (e.g. all videos are a silent movie), most likely it's just a slight misconfiguration.

To debug:

 1. In your audio-VM, run `pavucontrol`.
 2. The top shows several tabs. Navigate to the left most: "Playback"
 3. You should see some streams here with the names of currently running (and connected) VMs. If there aren't any, start a VM that has it's `audiovm`-property set to this audio-VM. It should show up in the "Playback"-tab shortly after booting. If it doesn't, check you have installed all relevant packages. If that didn't help, try using a non-minimal fedora template.
 4. Check the streams aren't muted! (The audio-control-bar should be blue and the mute-icon have no / white background.)
 5. If everything checked out, navigate to the right most tab: "Configuration"
 6. Make sure the devices are not "Off". Several profiles may be valid / should work depending on device, but if you are unsure: "Analog Stereo Duplex" is a safe bet for your sound-card.
 7. If there is still no audio (check by starting a stream in a VM), navigate to the "Output Devices"-Tab.
 8. Start a stream that outputs audio. You should see one horizontal line flickering. (you might have to scroll!)
 9. The blue line is a volume-indicator. It means this device is active as output-device. Make sure it's not muted. If it's active and you can't use it for other reasons, activate a different device you know should work by clicking the check mark to the right of the device name.
 10. Make sure the volume-control (the static horizontal line with 'Silence' and '100%(0 dB)' indicator) is not set to the very left and move it a bit to the right.

### Sound card / Build-in Audio Is Missing
Reboot your audio-VM until it shows up. The easiest way is to boot by selecting 'pavucontrol' (of your audio-VM) from the application finder. You should see the device in the 'Output Device'-tab.

### Revert To dom0 As Audio-VM
This is rather simple:

 * Shutdown your audio-VM
 * Remove all PCI-devices from that VM
 * Set the global audio-VM to dom0: `qubes-prefs default_audiovm dom0`
 * Maybe check for VMs that had their `audiovm`-preference set manually and set it to dom0!
 * For convenience, remove autostart form your audio-VM!
 * Reboot your real machine!