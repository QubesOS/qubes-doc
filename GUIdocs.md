---
layout: wiki
title: GUIdocs
permalink: /wiki/GUIdocs/
---

Qubes GUI protocol
==================

AppVM -\> dom0 messages
-----------------------

Proper handling of the below messages is security-critical. Observe that beside two messages (`CLIPBOARD` and `MFNDUMP`) the rest have fixed size, so there is no need for error-prone parsing.

Each message starts with the following header

``` {.wiki}
struct msghdr {   
        uint32_t type;
        uint32_t window;
};
```

The header is followed by message-specific data.

|Message name|Structure after header|Action|
|:-----------|:---------------------|:-----|
|MSG\_CLIPBOARD\_DATA|amorphic blob (length determined by the "window" field)|Store the received clipboard content (not parsing in any way)|
|MSG\_CREATE|` struct msg_create { ` 
 ` uint32_t x; ` 
 ` uint32_t y; ` 
 ` uint32_t width; ` 
 ` uint32_t height; ` 
 ` uint32_t parent; ` 
 ` uint32_t override_redirect; ` 
 ` }; `|Create a window with given parameters|
|MSG\_DESTROY|None|Destroy a window|
|MSG\_MAP|` struct msg_map_info { ` 
 ` uint32_t transient_for; ` 
 ` uint32_t override_redirect; ` 
 ` }; `|Map a window with given parameters|
|MSG\_UNMAP|None|Unmap a window|
|MSG\_CONFIGURE|` struct msg_configure { ` 
 ` uint32_t x; ` 
 ` uint32_t y; ` 
 ` uint32_t width; ` 
 ` uint32_t height; ` 
 ` uint32_t override_redirect; ` 
 ` }; `|Change window position/size/type|
|MSG\_MFNDUMP|` struct shm_cmd { ` 
 ` uint32_t shmid; ` 
 ` uint32_t width; ` 
 ` uint32_t height; ` 
 ` uint32_t bpp; ` 
 ` uint32_t off; ` 
 ` uint32_t num_mfn; ` 
 ` uint32_t domid; ` 
 ` uint32_t mfns[0]; ` 
 ` }; `|Retrieve the array of mfns that constitute the composition buffer of a remote window. 
 The "num\_mfn" 32bit integers follow the shm\_cmd structure.|
|MSG\_SHMIMAGE|` struct msg_shmimage { ` 
 `    uint32_t x; ` 
 `    uint32_t y;` 
 `    uint32_t width;` 
 `    uint32_t height;` 
 ` }; `|Repaint the given window fragment|
|MSG\_WMNAME|` struct msg_wmname { ` 
 ` char data[128]; ` 
 ` } ; `|Set the window name; only printable characters are allowed|
|MSG\_DOCK|None|Dock the window in the tray|

Dom0 -\> AppVM messages
-----------------------

Proper handling of the below messages is NOT security-critical.

Each message starts with the following header

``` {.wiki}
struct msghdr {   
        uint32_t type;
        uint32_t window;
};
```

The header is followed by message-specific data.
 ` KEYPRESS, BUTTON, MOTION ` messages pass information extracted from dom0 XEvent; see appropriate event documentation.

|Message name|Structure after header|Action|
|:-----------|:---------------------|:-----|
|MSG\_KEYPRESS|` struct msg_keypress {  ` 
 ` uint32_t type;  ` 
 ` uint32_t x;  ` 
 ` uint32_t y;  ` 
 ` uint32_t state;  ` 
 ` uint32_t keycode;  ` 
 ` }; `|Tell qubes driver to generate a keypress|
|MSG\_BUTTON|` struct msg_button {  ` 
 ` uint32_t type;  ` 
 ` uint32_t x;  ` 
 ` uint32_t y;  ` 
 ` uint32_t state;  ` 
 ` uint32_t button;  ` 
 ` }; `|Tell qubes driver to generate mouseclick|
|MSG\_MOTION|` struct msg_motion {  ` 
 ` uint32_t x;  ` 
 ` uint32_t y;  ` 
 ` uint32_t state;  ` 
 ` uint32_t is_hint;  ` 
 ` }; `|Tell qubes driver to generate motion|
|MSG\_CONFIGURE|` struct msg_configure { ` 
 ` uint32_t x; ` 
 ` uint32_t y; ` 
 ` uint32_t width; ` 
 ` uint32_t height; ` 
 ` uint32_t override_redirect; ` 
 ` }; `|Change window position/size/type|
|MSG\_MAP|` struct msg_map_info { ` 
 ` uint32_t transient_for; ` 
 ` uint32_t override_redirect; ` 
 ` }; `|Map a window with given parameters|
|MSG\_CLOSE|None|send wmDeleteMessage to the window|
|MSG\_CROSSING|Obsolete|Obsolete, unused|
|MSG\_FOCUS|` struct msg_focus {  ` 
 ` uint32_t type;  ` 
 ` uint32_t mode;  ` 
 ` uint32_t detail;  ` 
 `  }; `|Raise a window, XSetInputFocus|
|MSG\_CLIPBOARD\_REQ|None|Retrieve the local clipboard, pass contents to gui-daemon|
|MSG\_CLIPBOARD\_DATA|amorphic blob|Insert the received data into local clipboard|
|MSG\_EXECUTE|Obsolete|Obsolete, unused|
|MSG\_KEYMAP\_NOTIFY|` unsigned char remote_keys[32]; `|Synchronize the keyboard state (key pressed/depressed) with dom0|


