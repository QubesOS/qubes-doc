---
layout: doc
title: GUI
permalink: /doc/gui/
redirect_from:
- /en/doc/gui/
- /en/doc/gui-docs/
- /doc/GUIdocs/
- /wiki/GUIdocs/
---

Qubes GUI protocol
==================

qubes_gui and qubes_guid processes
------------------------------------

All AppVM X applications connect to local (running in AppVM) Xorg server, that uses the following "hardware" drivers:

-   *dummy_drv* - video driver, that paints onto a framebuffer located in RAM, not connected to real hardware
-   *qubes_drv* - it provides a virtual keyboard and mouse (in fact, more, see below)

For each AppVM, there is a pair of *qubes_gui* (running in AppVM) and *qubes_guid* (running in dom0) processes, connected over vchan. Main responsibilities of *qubes_gui* are:

-   call XCompositeRedirectSubwindows on the root window, so that each window has its own composition buffer
-   instruct the local Xorg server to notify it about window creation, configuration and damage events; pass information on these events to dom0
-   receive information about keyboard and mouse events from dom0, tell *qubes_drv* to fake appropriate events
-   receive information about window size/position change, apply them to the local window

Main responsibilities of *qubes_guid* are:

-   create a window in dom0 whenever an information on window creation in AppVM is received from *qubes_gui*
-   whenever the local window receives XEvent, pass information on it to AppVM (particularly, mouse and keyboard data)
-   whenever AppVM signals damage event, tell local Xorg server to repaint a given window fragment
-   receive information about window size/position change, apply them to the local window

Note that keyboard and mouse events are passed to AppVM only if a window belonging to this AppVM has focus. AppVM has no way to get information on keystrokes fed to other AppVMs (e.g. XTEST extension will report the status of local AppVM keyboard only), nor synthesize and pass events to other AppVMs.

Window content updates implementation
-------------------------------------

Typical remote desktop applications, like *vnc*, pass the information on all changed window content in-band (say, over tcp). As the channel has limited throughput, this impacts video performance. In case of Qubes, *qubes_gui* does not transfer all changed pixels via vchan. Instead, for each window, upon its creation or size change, *qubes_gui*

-   asks *qubes_drv* driver for the list of physical memory frames that hold the composition buffer of a window
-   pass this information via `MFNDUMP` message to *qubes_guid* in dom0

Now, *qubes_guid* has to tell dom0 Xorg server about the location of the buffer. There is no supported way (e.g. Xorg extension) to do this zero-copy style. The following method is used in Qubes:

-   in dom0, the Xorg server is started with *LD_PRELOAD*-ed library named *shmoverride.so*. This library hooks all function calls related to shared memory.
-   *qubes_guid* creates a shared memory segment, and then tells Xorg to attach it via *MIT-SHM* extension
-   when Xorg tries to attach the segment (via glibc *shmat*) *shmoverride.so* intercepts this call and instead maps AppVM memory via *xc_map_foreign_range*
-   since then, we can use MIT-SHM functions, e.g. *XShmPutImage* to draw onto a dom0 window. *XShmPutImage* will paint with DRAM speed; actually, many drivers use DMA for this.

The important detail is that *xc_map_foreign_range* verifies that a given mfn range actually belongs to a given domain id (and the latter is provided by trusted *qubes_guid*). Therefore, rogue AppVM cannot gain anything by passing crafted mnfs in the `MFNDUMP` message.

To sum up, this solution has the following benefits:

-   window updates at DRAM speed
-   no changes to Xorg code
-   minimal size of the supporting code

![gui.png](/attachment/wiki/GUIdocs/gui.png)

Security markers on dom0 windows
--------------------------------

It is important that user knows which AppVM a given window belongs to. This prevents an attack when a rogue AppVM paints a window pretending to belong to other AppVM or dom0, and tries to steal e.g. passwords.

In Qubes, the custom window decorator is used, that paints a colourful frame (the colour is determined during AppVM creation) around decorated windows. Additionally, window title always starts with **[name of the AppVM]**. If a window has a *override_redirect* attribute, meaning that it should not be treated by a window manager (typical case is menu windows), *qubes_guid* draws a two-pixel colourful frame around it manually.

Clipboard sharing implementation
--------------------------------

Certainly, it would be insecure to allow AppVM to read/write clipboard of other AppVMs unconditionally. Therefore, the following mechanism is used:

-   there is a "qubes clipboard" in dom0 - its contents is stored in a regular file in dom0.
-   if user wants to copy local AppVM clipboard to qubes clipboard, she must focus on any window belonging to this AppVM, and press **Ctrl-Shift-C**. This combination is trapped by *qubes-guid*, and `CLIPBOARD_REQ` message is sent to AppVM. *qubes-gui* responds with *CLIPBOARD_DATA* message followed by clipboard contents.
-   user focuses on other AppVM window, presses **Ctrl-Shift-V**. This combination is trapped by *qubes-guid*, and `CLIPBOARD_DATA` message followed by qubes clipboard contents is sent to AppVM; *qubes_gui* copies data to the local clipboard, and then user can paste its contents to local applications normally.

This way, user can quickly copy clipboards between AppVMs. This action is fully controlled by the user, it cannot be triggered/forced by any AppVM.

*qubes_gui* and *qubes_guid* code notes
-----------------------------------------

Both applications are structures similarly. They use *select* function to wait for any of the two event sources

-   messages from the local X server
-   messages from the vchan connecting to the remote party

The XEvents are handled by *handle_xevent_eventname* function, messages are handled by *handle_messagename* function. One should be very careful when altering the actual *select* loop - e.g. both XEvents and vchan messages are buffered, meaning that *select* will not wake for each message.

If one changes the number/order/signature of messages, one should increase the *QUBES_GUID_PROTOCOL_VERSION* constant in *messages.h* include file.

*qubes_guid* writes debugging information to */var/log/qubes/qubes.domain_id.log* file; *qubes_gui* writes debugging information to */var/log/qubes/gui_agent.log*. Include these files when reporting a bug.

AppVM -> dom0 messages
-----------------------

Proper handling of the below messages is security-critical. Observe that beside two messages (`CLIPBOARD` and `MFNDUMP`) the rest have fixed size, so the parsing code can be small.

The *override_redirect* window attribute is explained at [Override Redirect Flag](http://tronche.com/gui/x/xlib/window/attributes/override-redirect.html). The *transient_for* attribute is explained at [Transient_for attribute](http://tronche.com/gui/x/icccm/sec-4.html#WM_TRANSIENT_FOR).

Window manager hints and flags are described at [http://standards.freedesktop.org/wm-spec/latest/](http://standards.freedesktop.org/wm-spec/latest/), especially part about `_NET_WM_STATE`.

Each message starts with the following header

~~~
struct msghdr {   
        uint32_t type;
        uint32_t window;
        /* This field is intended for use by gui_agents to skip unknown
         * messages from the (trusted) guid. Guid, on the other hand,
         * should never rely on this field to calculate the actual len of
         * message to be read, as the (untrusted) agent can put here
         * whatever it wants! */
        uint32_t untrusted_len;
};
~~~

The header is followed by message-specific data.

<table class="table">
  <tr>
    <th>Message name</th>
    <th>Structure after header</th>
    <th>Action</th>
  </tr>
  <tr>
    <td>MSG_CLIPBOARD_DATA</td>
    <td>amorphic blob (length determined by the "window" field)</td>
    <td>Store the received clipboard content (not parsing in any way)</td>
  </tr>
<tr>
  <td>MSG_CREATE</td>
  <td><pre>
struct msg_create {
  uint32_t x;
  uint32_t y;
  uint32_t width;
  uint32_t height;
  uint32_t parent;
  uint32_t override_redirect;
};
</pre>
</td>
 <td>Create a window with given parameters</td>
</tr>
<tr>
  <td>MSG_DESTROY</td>
  <td>None</td>
  <td>Destroy a window</td>
 </tr>
<tr>
  <td>MSG_MAP</td>
  <td><pre>
struct msg_map_info { 
  uint32_t transient_for; 
  uint32_t override_redirect; 
};
</pre></td>
 <td>Map a window with given parameters</td>
</tr>
<tr>
  <td>MSG_UNMAP</td>
  <td>None</td>
  <td>Unmap a window</td>
 </tr>
<tr>
  <td>MSG_CONFIGURE</td>
  <td><pre>
struct msg_configure { 
  uint32_t x; 
  uint32_t y; 
  uint32_t width; 
  uint32_t height; 
  uint32_t override_redirect; 
};
</pre></td>
 <td>Change window position/size/type</td>
</tr>
<tr>
  <td>MSG_MFNDUMP</td>
  <td><pre>
struct shm_cmd { 
  uint32_t shmid; 
  uint32_t width; 
  uint32_t height; 
  uint32_t bpp; 
  uint32_t off; 
  uint32_t num_mfn; 
  uint32_t domid; 
  uint32_t mfns[0]; 
};
</pre></td>
 <td>Retrieve the array of mfns that constitute the composition buffer of a remote window.

 The "num_mfn" 32bit integers follow the shm_cmd structure; "off" is the offset of the composite buffer start in the first frame; "shmid" and "domid" parameters are just placeholders (to be filled by *qubes_guid*), so that we can use the same structure when talking to *shmoverride.so*|
 </td>
</tr>
<tr>
  <td>MSG_SHMIMAGE</td>
  <td><pre>
struct msg_shmimage { 
     uint32_t x; 
     uint32_t y;
     uint32_t width;
     uint32_t height;
};
</pre> </td>
 <td>Repaint the given window fragment</td>
</tr>
<tr>
  <td>MSG_WMNAME</td>
  <td><pre>
struct msg_wmname { 
  char data[128]; 
};
</pre></td>
 <td>Set the window name; only printable characters are allowed</td>
</tr>
<tr>
  <td>MSG_DOCK</td>
  <td>None</td>
  <td>Dock the window in the tray</td>
 </tr>
<tr>
  <td>MSG_WINDOW_HINTS</td>
  <td><pre>
struct msg_window_hints { 
     uint32_t flags; 
     uint32_t min_width; 
     uint32_t min_height; 
     uint32_t max_width; 
     uint32_t max_height; 
     uint32_t width_inc; 
     uint32_t height_inc; 
     uint32_t base_width; 
     uint32_t base_height; 
};
</pre> </td>
 <td>Size hints for window manager</td>
</tr>
<tr>
  <td>MSG_WINDOW_FLAGS</td>
  <td><pre>
struct msg_window_flags { 
      uint32_t flags_set; 
     uint32_t flags_unset;
};
</pre> </td>
 <td>Change window state request; fields contains bitmask which flags request to be set and which unset</td>
</tr>
</table>

Dom0 -> AppVM messages
-----------------------

Proper handling of the below messages is NOT security-critical.

Each message starts with the following header

~~~
struct msghdr {   
        uint32_t type;
        uint32_t window;
};
~~~

The header is followed by message-specific data.
 `KEYPRESS`, `BUTTON`, `MOTION`, `FOCUS` messages pass information extracted from dom0 XEvent; see appropriate event documentation.

<table class="table">
  <tr>
    <th>Message name</th>
    <th>Structure after header</th>
    <th>Action</th>
  </tr>
<tr>
  <td>MSG_KEYPRESS</td>
  <td><pre>
struct msg_keypress {  
  uint32_t type;  
  uint32_t x;  
  uint32_t y;  
  uint32_t state;  
  uint32_t keycode;  
};
</pre> </td>
 <td>Tell *qubes_drv* driver to generate a keypress</td>
</tr>
<tr>
  <td>MSG_BUTTON</td>
  <td><pre>
struct msg_button {  
  uint32_t type;  
  uint32_t x;  
  uint32_t y;  
  uint32_t state;  
  uint32_t button;  
};
</pre> </td>
 <td>Tell *qubes_drv* driver to generate mouseclick</td>
</tr>
<tr>
  <td>MSG_MOTION</td>
  <td><pre>
struct msg_motion {  
  uint32_t x;  
  uint32_t y;  
  uint32_t state;  
  uint32_t is_hint;  
};
</pre> </td>
 <td>Tell *qubes_drv* driver to generate motion event</td>
</tr>
<tr>
  <td>MSG_CONFIGURE</td>
  <td><pre>
struct msg_configure { 
  uint32_t x; 
  uint32_t y; 
  uint32_t width; 
  uint32_t height; 
  uint32_t override_redirect; 
};
</pre> </td>
 <td>Change window position/size/type</td>
</tr>
<tr>
  <td>MSG_MAP</td>
  <td><pre>
struct msg_map_info { 
  uint32_t transient_for; 
  uint32_t override_redirect; 
};
</pre> </td>
 <td>Map a window with given parameters</td>
</tr>
<tr>
  <td>MSG_CLOSE</td>
  <td>None</td>
  <td>send wmDeleteMessage to the window</td>
 </tr>
<tr>
  <td>MSG_CROSSING</td>
  <td><pre>
struct msg_crossing { 
  uint32_t type; 
  uint32_t x; 
  uint32_t y; 
  uint32_t state; 
  uint32_t mode; 
  uint32_t detail; 
  uint32_t focus; 
};
</pre> </td>
 <td>Notify window about enter/leave event</td>
</tr>
<tr>
  <td>MSG_FOCUS</td>
  <td><pre>
struct msg_focus {  
  uint32_t type;  
  uint32_t mode;  
  uint32_t detail;  
};
</pre> </td>
 <td>Raise a window, XSetInputFocus</td>
</tr>
<tr>
  <td>MSG_CLIPBOARD_REQ</td>
  <td>None</td>
  <td>Retrieve the local clipboard, pass contents to gui-daemon</td>
 </tr>
<tr>
  <td>MSG_CLIPBOARD_DATA</td>
  <td>amorphic blob</td>
  <td>Insert the received data into local clipboard</td>
 </tr>
<tr>
  <td>MSG_EXECUTE</td>
  <td>Obsolete</td>
  <td>Obsolete, unused</td>
 </tr>
<tr>
  <td>MSG_KEYMAP_NOTIFY</td>
  <td> unsigned char remote_keys[32]; </td>
  <td>Synchronize the keyboard state (key pressed/released) with dom0</td>
 </tr>
<tr>
  <td>MSG_WINDOW_FLAGS</td>
  <td><pre>
struct msg_window_flags { 
      uint32_t flags_set; 
     uint32_t flags_unset;
};
</pre> </td>
 <td>Window state change confirmation</td>
</tr>
</table>
