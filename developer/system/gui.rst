==================
GUI virtualization
==================
``qubes-gui`` and ``qubes-guid`` processes
------------------------------------------

All AppVM X applications connect to local (running in AppVM) Xorg
servers that use the following “hardware” drivers:

-  *``dummyqsb_drv``* - video driver, that paints onto a framebuffer
   located in RAM, not connected to real hardware
-  *``qubes_drv``* - it provides a virtual keyboard and mouse (in fact,
   more, see below)

For each AppVM, there is a pair of ``qubes-gui`` (running in AppVM) and
``qubes-guid`` (running in the AppVM’s GuiVM, dom0 by default) processes
connected over vchan. The main responsibilities of ``qubes-gui`` are:

-  call XCompositeRedirectSubwindows on the root window, so that each
   window has its own composition buffer
-  instruct the local Xorg server to notify it about window creation,
   configuration and damage events; pass information on these events to
   dom0
-  receive information about keyboard and mouse events from dom0, tell
   ``qubes-drv`` to fake appropriate events
-  receive information about window size/position change, apply them to
   the local window

The main responsibilities of ``qubes-guid`` are:

-  create a window in dom0 whenever an information on window creation in
   AppVM is received from ``qubes-gui``
-  whenever the local window receives XEvent, pass information on it to
   AppVM (particularly, mouse and keyboard data)
-  whenever AppVM signals damage event, tell local Xorg server to
   repaint a given window fragment
-  receive information about window size/position change, apply them to
   the local window

Note that keyboard and mouse events are passed to AppVM only if a window
belonging to this AppVM has focus. AppVM has no way to get information
on keystrokes fed to other AppVMs (e.g. XTEST extension will report the
status of local AppVM keyboard only) or synthesize and pass events to
other AppVMs.

Window content updates implementation
-------------------------------------

Typical remote desktop applications, like VNC, pass information on all
changed window content in-band (say, over tcp). As that channel has
limited throughput, this impacts video performance. In the case of
Qubes, ``qubes-gui`` does not transfer all changed pixels via vchan.
Instead, for each window, upon its creation or size change:

-  Old ``qubes-gui`` versions will ask ``qubes-drv`` driver for the list
   of physical memory frames that hold the composition buffer of a
   window, and pass this to dom0 via the deprecated ``MFNDUMP`` message.
-  New ``qubes-gui`` versions will rely on ``qubes-drv`` having
   allocated memory using gntalloc, and then pass the grant table
   indexes gntalloc has chosen to the GUI daemon using the
   ``WINDOW_DUMP`` message.

Now, ``qubes-guid`` has to tell the dom0 Xorg server about the location
of the buffer. There is no supported way (e.g. Xorg extension) to do
this zero-copy style. The following method is used in Qubes:

-  in dom0, the Xorg server is started with ``LD_PRELOAD``-ed library
   named ``shmoverride.so``. This library hooks all function calls
   related to shared memory.
-  ``qubes-guid`` creates a shared memory segment, and then tells Xorg
   to attach it via ``MIT-SHM`` extension
-  when Xorg tries to attach the segment (via glibc ``shmat``)
   ``shmoverride.so`` intercepts this call and instead maps AppVM memory
   via ``xc_map_foreign_pages`` for the deprecated ``MFNDUMP`` message,
   or ``xengnttab_map_domain_grant_refs`` for the ``WINDOW_DUMP``
   message.
-  afterwards, we can use MIT-SHM functions, such as ``XShmPutImage``,
   to draw onto a dom0 window. ``XShmPutImage`` will paint with DRAM
   speed, and many drivers use DMA to make this even faster.

The important detail is that ``xc_map_foreign_pages`` verifies that a
given mfn range actually belongs to a given domain id (and the latter is
provided by trusted ``qubes-guid``). Therefore, rogue AppVM cannot gain
anything by passing crafted mnfs in the ``MFNDUMP`` message. Similarly,
``xengnttab_map_domain_grant_refs`` will only map grants from the
specific domain ID specified by qubes-guid, so crafted ``WINDOW_DUMP``
messages are not helpful to an attacker.

To sum up, this solution has the following benefits:

-  window updates at DRAM speed
-  no changes to Xorg code
-  minimal size of the supporting code

There are two reasons that ``WINDOW_DUMP`` is preferred over
``MFNDUMP``:

1. ``xc_map_foreign_pages`` can only be used by dom0, as it allows
   accessing all memory of any VM. Allowing any VM other than dom0 to do
   this would be a security vulnerability.
2. ``xc_map_foreign_pages`` requires the guest physical address of the
   pages to map, but normal userspace processes (such as ``qubes-gui``
   or Xorg) do not have access to that information. Therefore, the
   translation is done via the ``u2mfn`` out-of-tree kernel module.

Currently, using ``WINDOW_DUMP`` does come at a performance cost,
because the AppVM’s X server must copy the pages from the application to
the gntalloc-allocated memory. This will be solved by future
improvements to gntalloc, which will allow exporting *any* page via
gntalloc, including memory shared by another process.

.. figure:: /attachment/doc/gui.png
   :alt: gui.png

   gui.png

Security markers on dom0 windows
--------------------------------

It is important that the user knows which AppVM a given window belongs
to. This prevents a rogue AppVM from painting a window pretending to
belong to other AppVM or dom0 and trying to steal, for example,
passwords.

In Qubes, a custom window decorator is used that paints a colourful
frame (the colour is determined during AppVM creation) around decorated
windows. Additionally, the window title always starts with **[name of
the AppVM]**. If a window has an ``override_redirect`` attribute,
meaning that it should not be treated by a window manager (typical case
is menu windows), ``qubes-guid`` draws a two-pixel colourful frame
inside it manually.

Clipboard sharing implementation
--------------------------------

Certainly, it would be insecure to allow AppVM to read/write the
clipboards of other AppVMs unconditionally. Therefore, the following
mechanism is used:

-  there is a “qubes clipboard” in dom0 - its contents are stored in a
   regular file in dom0.
-  if the user wants to copy local AppVM clipboard to qubes clipboard,
   she must focus on any window belonging to this AppVM, and press
   **Ctrl-Shift-C**. This combination is trapped by ``qubes-guid``, and
   ``CLIPBOARD_REQ`` message is sent to AppVM. ``qubes-gui`` responds
   with ``CLIPBOARD_DATA`` message followed by clipboard contents.
-  the user focuses on other AppVM window, presses **Ctrl-Shift-V**.
   This combination is trapped by ``qubes-guid``, and ``CLIPBOARD_DATA``
   message followed by qubes clipboard contents is sent to AppVM;
   ``qubes-gui`` copies data to the local clipboard, and then user can
   paste its contents to local applications normally.

This way, the user can quickly copy clipboards between AppVMs. This
action is fully controlled by the user, it cannot be triggered/forced by
any AppVM.

``qubes-gui`` and ``qubes-guid`` code notes
-------------------------------------------

Both applications are structured similarly. They use ``select`` function
to wait for any of these two event sources:

-  messages from the local X server
-  messages from the vchan connecting to the remote party

The XEvents are handled by the ``handle_xevent_eventname`` function, and
messages are handled by ``handle_messagename`` function. One should be
very careful when altering the actual ``select`` loop, because both
XEvents and vchan messages are buffered, and ``select`` will not wake
for each message.

If one changes the number/order/signature of messages, one should
increase the ``QUBES_GUID_PROTOCOL_VERSION`` constant in ``messages.h``
include file.

``qubes-guid`` writes debugging information to
``/var/log/qubes/qubes.domain_id.log`` file; ``qubes-gui`` writes
debugging information to ``/var/log/qubes/gui_agent.log``. Include these
files when reporting a bug.

AppVM -> GuiVM messages
-----------------------

Proper handling of the below messages is security-critical. Note that
all messages except for ``CLIPBOARD``, ``MFNDUMP``, and ``WINDOW_DUMP``
have fixed size, so the parsing code can be small.

The ``override_redirect`` window attribute is explained at `Override
Redirect
Flag <https://tronche.com/gui/x/xlib/window/attributes/override-redirect.html>`__.
The ``transient_for`` attribute is explained at `transient_for
attribute <https://tronche.com/gui/x/icccm/sec-4.html#WM_TRANSIENT_FOR>`__.

Window manager hints and flags are described in the `Extended Window
Manager Hints (EWMH)
spec <https://standards.freedesktop.org/wm-spec/latest/>`__, especially
under the ``_NET_WM_STATE`` section.

Each message starts with the following header:

.. code:: c

   struct msghdr {
       uint32_t type;
       uint32_t window;
       /* This field is intended for use by GUI agents to skip unknown
        * messages from the (trusted) GUI daemon. GUI daemon, on the other
        * hand, should never rely on this field to calculate the actual len
        * of message to be read, as the (untrusted) agent can put whatever
        * it wants here! */
       uint32_t untrusted_len;
   };

This header is followed by message-specific data:

.. raw:: html

   <table class="table">

.. raw:: html

   <tr>

.. raw:: html

   <th>

Message name

.. raw:: html

   </th>

.. raw:: html

   <th>

Structure after header

.. raw:: html

   </th>

.. raw:: html

   <th>

Action

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_CLIPBOARD_DATA

.. raw:: html

   </td>

.. raw:: html

   <td>

amorphic blob (in protocol before 1.2, length determined by the “window”
field, in 1.2 and later - by untrusted_len in the header)

.. raw:: html

   </td>

.. raw:: html

   <td>

Store the received clipboard content (not parsed in any way)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_CREATE

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_create {
     uint32_t x;
     uint32_t y;
     uint32_t width;
     uint32_t height;
     uint32_t parent;
     uint32_t override_redirect;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Create a window with given parameters

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_DESTROY

.. raw:: html

   </td>

.. raw:: html

   <td>

None

.. raw:: html

   </td>

.. raw:: html

   <td>

Destroy a window

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_MAP

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_map_info {
     uint32_t transient_for;
     uint32_t override_redirect;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Map a window with given parameters

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_UNMAP

.. raw:: html

   </td>

.. raw:: html

   <td>

None

.. raw:: html

   </td>

.. raw:: html

   <td>

Unmap a window

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_CONFIGURE

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_configure {
     uint32_t x;
     uint32_t y;
     uint32_t width;
     uint32_t height;
     uint32_t override_redirect;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Change window position/size/type

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_MFNDUMP

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
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
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Retrieve the array of mfns that constitute the composition buffer of a
remote window.

The “num_mfn” 32bit integers follow the shm_cmd structure; “off” is the
offset of the composite buffer start in the first frame; “shmid” and
“domid” parameters are just placeholders (to be filled by
``qubes-guid``), so that we can use the same structure when talking to
``shmoverride.so``.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_SHMIMAGE

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_shmimage {
        uint32_t x;
        uint32_t y;
        uint32_t width;
        uint32_t height;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Repaint the given window fragment

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_WMNAME

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_wmname {
     char data[128];
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Set the window name. Only printable characters are allowed, and by
default non-ASCII characters are not allowed.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_DOCK

.. raw:: html

   </td>

.. raw:: html

   <td>

None

.. raw:: html

   </td>

.. raw:: html

   <td>

Dock the window in the tray

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_WINDOW_HINTS

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
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
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Size hints for window manager

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_WINDOW_FLAGS

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_window_flags {
        uint32_t flags_set;
        uint32_t flags_unset;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Change window state request; fields contains bitmask which flags request
to be set and which unset

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_CURSOR

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_cursor {
        uint32_t cursor;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Update cursor pointer for a window. Supported cursor IDs are default
cursor (0) and X Font cursors (with 0x100 bit set).

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_WMCLASS

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_wmclass {
       char res_class[64];
       char res_name[64];
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Set the WM_CLASS property of a window.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_WINDOW_DUMP

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_window_dump_hdr {
       uint32_t type;
       uint32_t width;
       uint32_t height;
       uint32_t bpp;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Header for shared memory dump command of type hdr.type. Currently only

.. raw:: html

   <pre>WINDOW_DUMP_TYPE_GRANT_REFS</pre>

(0) is supported.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       <tr>

    .. raw:: html

       <td>

    WINDOW_DUMP_TYPE_GRANT_REFS

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    .. raw:: html

       <pre>
       struct msg_window_dump_grant_refs {
           uint32_t refs[0];
       };
       </pre>

    .. raw:: html

       </td>

    .. raw:: html

       <td>

    Grant references that should be mapped into the compositing buffer.

    .. raw:: html

       </td>

    .. raw:: html

       </tr>

    .. raw:: html

       </tr>

    .. raw:: html

       </table>

GuiVM -> AppVM messages
-----------------------

Proper handling of the below messages is NOT security-critical.

Each message starts with the following header

.. code:: c

   struct msghdr {
           uint32_t type;
           uint32_t window;
   };

The header is followed by message-specific data:

.. raw:: html

   <table class="table">

.. raw:: html

   <tr>

.. raw:: html

   <th>

Message name

.. raw:: html

   </th>

.. raw:: html

   <th>

Structure after header

.. raw:: html

   </th>

.. raw:: html

   <th>

Action

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_KEYPRESS

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_keypress {
     uint32_t type;
     uint32_t x;
     uint32_t y;
     uint32_t state;
     uint32_t keycode;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Tell

.. raw:: html

   <pre>qubes_drv</pre>

driver to generate a keypress

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_BUTTON

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_button {
     uint32_t type;
     uint32_t x;
     uint32_t y;
     uint32_t state;
     uint32_t button;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Tell

.. raw:: html

   <pre>qubes_drv</pre>

driver to generate mouseclick

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_MOTION

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_motion {
     uint32_t x;
     uint32_t y;
     uint32_t state;
     uint32_t is_hint;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Tell

.. raw:: html

   <pre>qubes_drv</pre>

driver to generate motion event

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_CONFIGURE

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_configure {
     uint32_t x;
     uint32_t y;
     uint32_t width;
     uint32_t height;
     uint32_t override_redirect;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Change window position/size/type

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_MAP

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_map_info {
     uint32_t transient_for;
     uint32_t override_redirect;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Map a window with given parameters

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_CLOSE

.. raw:: html

   </td>

.. raw:: html

   <td>

None

.. raw:: html

   </td>

.. raw:: html

   <td>

send wmDeleteMessage to the window

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_CROSSING

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_crossing {
     uint32_t type;
     uint32_t x;
     uint32_t y;
     uint32_t state;
     uint32_t mode;
     uint32_t detail;
     uint32_t focus;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Notify window about enter/leave event

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_FOCUS

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_focus {
     uint32_t type;
     uint32_t mode;
     uint32_t detail;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Raise a window, XSetInputFocus

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_CLIPBOARD_REQ

.. raw:: html

   </td>

.. raw:: html

   <td>

None

.. raw:: html

   </td>

.. raw:: html

   <td>

Retrieve the local clipboard, pass contents to gui-daemon

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_CLIPBOARD_DATA

.. raw:: html

   </td>

.. raw:: html

   <td>

amorphic blob

.. raw:: html

   </td>

.. raw:: html

   <td>

Insert the received data into local clipboard

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_EXECUTE

.. raw:: html

   </td>

.. raw:: html

   <td>

Obsolete

.. raw:: html

   </td>

.. raw:: html

   <td>

Obsolete, unused

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_KEYMAP_NOTIFY

.. raw:: html

   </td>

.. raw:: html

   <td>

unsigned char remote_keys[32];

.. raw:: html

   </td>

.. raw:: html

   <td>

Synchronize the keyboard state (key pressed/released) with dom0

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

MSG_WINDOW_FLAGS

.. raw:: html

   </td>

.. raw:: html

   <td>

.. raw:: html

   <pre>
   struct msg_window_flags {
     uint32_t flags_set;
     uint32_t flags_unset;
   };
   </pre>

.. raw:: html

   </td>

.. raw:: html

   <td>

Window state change confirmation

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

``KEYPRESS``, ``BUTTON``, ``MOTION``, ``FOCUS`` messages pass
information extracted from dom0 XEvent; see appropriate event
documentation.
