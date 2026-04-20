==========================
How to copy and paste text
==========================

Qubes OS features a secure inter-qube clipboard, the global clipboard, that allows you **to copy and paste plain text** between qubes.

.. note:: If you wish to copy more complex data, such as rich text or images, or copy from dom0, see:

   * :doc:`/user/how-to-guides/how-to-copy-and-move-files`
   * :doc:`/user/how-to-guides/how-to-copy-from-dom0`

In order to copy text from qube A to qube B:

1. Select text from the source app in qube A, then copy it normally (e.g., by pressing :kbd:`Ctrl` + :kbd:`C`).

2. With the source app in qube A still in focus, press :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`C`. This copies the text from qube A’s clipboard to the global clipboard. You will see a notification that the content has been copied *to* the global clipboard, showing the number of bytes copied.

3. Select the target app in qube B and press :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`V`. This copies the text from the global clipboard to qube B’s clipboard and clears the global clipboard, ensuring that only qube B will have access to the copied text. You will see a notification that this has happened.

4. Paste the text in the target app in qube B normally (e.g., by pressing :kbd:`Ctrl` + :kbd:`V`).

This process might look complicated at first glance, but in practice it is actually very easy and fast once you get used to it. At the same time, it provides you with full control over exactly which qube receives the content of the global clipboard every time.

.. note:: You cannot use the global clipboard to paste back to the same qube where you copied text. If you try to do this you will see a warning that this is prohibited.

   Some applications, like xterm and uxterm, require configuration to ensure that the copy process places data on to the local clipboard.

Security
--------

The global clipboard system is secure because it doesn’t allow any qube other than your selected target to steal contents from the global clipboard. Without such a system in place, if you copied a password from the password manager in your vault qube to another qube, for example, it would immediately be leaked to every other running qube in the system, including qubes that are untrusted by default, such as ``sys-net``. By giving you precise control over exactly which qube receives the global clipboard content, then immediately wiping the global clipboard afterward, Qubes OS protects the confidentiality of the text being copied.

However, you should keep in mind that performing a copy and paste operation from a *less trusted* to a *more trusted* qube is always potentially insecure, since the data that you copy could exploit some hypothetical bug in the target qube. For example, the seemingly-innocent link that you copy from an untrusted qube could turn out to be a large buffer of junk that, when pasted into the target qube’s word processor, could exploit a hypothetical bug in the undo buffer. This is a general problem and applies to any data transfer from *less trusted* to *more trusted* qubes. It even applies to copying files between physically separate (air-gapped) machines. Therefore, you should always copy clipboard data only from *more trusted* to *less trusted* qubes.

See also `this article <https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html>`__ for more information on this topic, and some ideas of how we might solve this problem in some future version of Qubes, as well as `this message <https://groups.google.com/group/qubes-devel/msg/48b4b532cee06e01>`__ from qubes-devel.

Focus stealing
^^^^^^^^^^^^^^

The above discussion assumes that you control which window is focused in dom0 at the time of the paste. However, the default install of the Xfce window manager is configured to give focus to newly created windows. This means that a malicious qube could potentially “steal the focus” by creating a window just before you press :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`V`, and so would receive the data instead of your intended target. (Focus stealing is a risk any time you are typing confidential data, but a Qubes clipboard paste probably presents the greatest risk of leaking an entire password before you have time to react). You may be able to mitigate this risk by changing the window manager configuration. For example, in Xfce, you could run ``xfwm4-settings`` in dom0, go to the :guilabel:`Focus` tab, and un-check :guilabel:`Automatically give focus to newly created windows`. However, we have not confirmed whether such settings are sufficient to prevent a malicious qube from stealing the focus in all cases.

Clipboard automatic policy enforcement
--------------------------------------

The global clipboard is configurable like any other policy, see: :doc:`/user/how-to-guides/how-to-edit-a-policy`.

Automatic clipboard wiping
--------------------------

By default data pasted into a qube will remain there until you copy something else or restart the qube. It’s possible to make the ``qubes-gui`` process inside a qube wipe the clipboard automatically a minute after the last paste operation. This helps protect you from accidentally pasting the old content of the clipboard like a password in the wrong place (like a browser search bar). Since qubes don’t share the same clipboard, software like KeePassXC isn’t able to automatically wipe the clipboard of other qubes.

To enable automatic wiping of the clipboard after a minute :doc:`enable the service </user/how-to-guides/how-to-enable-a-service>` called `gui-agent-clipboard-wipe`.

Shortcut configuration
----------------------

The copy/paste shortcuts are configurable via :program:`Qubes OS Global Config`, in the :guilabel:`Clipboard` tab.

.. image:: /attachment/doc/qubes-clipboard-config.png
   :alt:

You can also change them using :doc:`qvm-features <core-admin-client:manpages/qvm-features>`.
The following commands would change the *copy/paste to global clipboard* shortcuts to :kbd:`Win` + :kbd:`c` for copy, and :kbd:`Win` + :kbd:`v` for paste:

.. code:: console

      [user@dom0] $ qvm-features dom0 gui-default-secure-copy-sequence 'Mod4-c'
      [user@dom0] $ qvm-features dom0 gui-default-secure-paste-sequence 'Mod4-v'

.. note:: For the changes to take effect in a qube, you need to restart the qube after changing the shortcuts.
