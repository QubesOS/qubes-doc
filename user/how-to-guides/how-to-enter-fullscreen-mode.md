---
lang: en
layout: doc
permalink: /doc/how-to-enter-fullscreen-mode/
redirect_from:
- /doc/full-screen-mode/
- /en/doc/full-screen-mode/
- /doc/FullScreenMode/
- /wiki/FullScreenMode/
ref: 205
title: How to Enter Fullscreen Mode
---


What is fullscreen mode?
-------------------------

Normally, the Qubes GUI virtualization daemon restricts the VM from "owning" the full screen, ensuring that there are always clearly marked decorations drawn by the trusted Window Manager around each of the VMs window.
This allows the user to easily realize to which domain a specific window belongs.
See the [screenshots](/doc/QubesScreenshots/) page for examples.

Why is fullscreen mode potentially dangerous?
----------------------------------------------

If one allowed one of the VMs to "own" the full screen, e.g. to show a movie on a full screen, it might not be possible for the user to know if the applications/VM really "released" the full screen, or if it has started emulating the whole desktop and is pretending to be the trusted Window Manager, drawing shapes on the screen that look e.g. like other windows, belonging to other domains (e.g. to trick the user into entering a secret passphrase into a window that looks like belonging to some trusted domain).

Secure use of fullscreen mode
------------------------------

However, it is possible to deal with fullscreen mode in a secure way assuming there are mechanisms that can be used at any time to switch between windows or show the full desktop and that cannot be intercepted by the VM.
The simplest example is the use of Alt+Tab for switching between windows, which is a shortcut handled by dom0.

Other examples such mechanisms are the KDE "Present Windows" and "Desktop Grid" effects, which are similar to Mac's "Expose" effect, and which can be used to immediately detect potential "GUI forgery", as they cannot be intercepted by any of the VM (as the GUID never passes down the key combinations that got consumed by KDE Window Manager), and so the VM cannot emulate those.
Those effects are enabled by default in KDE once Compositing gets enabled in KDE (System Settings -\> Desktop -\> Enable Desktop Effects), which is recommended anyway.
By default, they are triggered by Ctrl-F8 and Ctrl-F9 key combinations, but can also be reassigned to other shortcuts.

Enabling fullscreen mode for select VMs
----------------------------------------

You can always put a window into fullscreen mode in Xfce4 using the trusted window manager by right-clicking on a window's title bar and selecting "Fullscreen" or pressing `alt` + `f11`.
This functionality should still be considered safe, since a VM window still can't voluntarily enter fullscreen mode.
The user must select this option from the trusted window manager in dom0.
To exit fullscreen mode from here, press `alt` + `space` to bring up the title bar menu again, then select "Leave Fullscreen" or simply press `alt` + `f11`.
For StandaloneHVMs, you should set the screen resolution in the qube to that of the host, (or larger), *before* setting fullscreen mode in Xfce4.

As an alternative to the Xfce4 method, you can enable fullscreen mode for select VMs by creating the following entry in the `/etc/qubes/guid.conf` file in dom0:

~~~
VM: {
  personal: {
    allow_fullscreen = true;
  };
};
~~~

The string 'personal' above is an example only and should be replaced by the actual name of the VM for which you want to enable this functionality.

**Note:** There should be only one `VM: {}` block in the file (or you will [get into problems](https://groups.google.com/d/msg/qubes-users/-Yf9yNvTsVI/xXsEm8y2lrYJ)).

One can also enable this functionality for all the VMs globally in the same file, by modifying the 'global' section:

~~~
global: {
  # default values
  allow_fullscreen = true;
  #allow_utf8_titles = false;
  #secure_copy_sequence = "Ctrl-Shift-c";
  #secure_paste_sequence = "Ctrl-Shift-v";
  #windows_count_limit = 500;
};
~~~

Be sure to restart the VM(s) after modifying this file, for the changes to take effect.
