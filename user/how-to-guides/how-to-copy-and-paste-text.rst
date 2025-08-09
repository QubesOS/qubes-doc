==========================
How to copy and paste text
==========================


*This page is about copying and pasting plain text. If you wish to copy more complex data, such as rich text or images, see* :doc:`copying and moving files between qubes </user/how-to-guides/how-to-copy-and-move-files>` *. For dom0, see* :doc:`copying from (and to) dom0 </user/how-to-guides/how-to-copy-from-dom0>` *.*

Qubes OS features a secure inter-qube clipboard that allows you to copy and paste text between qubes.

In order to copy text from qube A to qube B:

1. Select text from the source app in qube A, then copy it normally (e.g., by pressing Ctrl+C).

2. With the source app in qube A still in focus, press Ctrl+Shift+C. This copies the text from qube A’s clipboard to the inter-qube clipboard.

3. Select the target app in qube B and press Ctrl+Shift+V. This copies the text from the inter-qube clipboard to qube B’s clipboard and clears the inter-qube clipboard, ensuring that only qube B will have access to the copied text.

4. Paste the text in the target app in qube B normally (e.g., by pressing Ctrl+V).



This process might look complicated at first glance, but in practice it is actually very easy and fast once you get used to it. At the same time, it provides you with full control over exactly which qube receives the content of the inter-qube clipboard every time.

Security
--------


The inter-qube clipboard system is secure because it doesn’t allow any qube other than your selected target to steal any contents from the inter-qube clipboard. Without such a system in place, any password you were to copy from the password manager in your vault qube to another qube, for example, would immediately be leaked to every other running qube in the system, including qubes that are untrusted by default, such as ``sys-net``. By giving you precise control over exactly which qube receives the inter-qube clipboard content, then immediately wiping the inter-qube clipboard afterward, Qubes OS protects the confidentiality of the text being copied.

However, one should keep in mind that performing a copy and paste operation from *less trusted* to *more trusted* qube is always potentially insecure, since the data that we copy could exploit some hypothetical bug in the target qube. For example, the seemingly-innocent link that we copy from an untrusted qube could turn out to be a large buffer of junk that, when pasted into the target qube’s word processor, could exploit a hypothetical bug in the undo buffer. This is a general problem and applies to any data transfer from *less trusted* to *more trusted* qubes. It even applies to copying files between physically separate (air-gapped) machines. Therefore, you should always copy clipboard data only from *more trusted* to *less trusted* qubes.

See also `this article <https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html>`__ for more information on this topic, and some ideas of how we might solve this problem in some future version of Qubes, as well as `this message <https://groups.google.com/group/qubes-devel/msg/48b4b532cee06e01>`__ from qubes-devel.

Focus stealing
^^^^^^^^^^^^^^


The above discussion assumes that you control which window is focused in dom0 at the time of the paste. However, if your dom0 window manager is configured to give focus to newly created windows (which, as of Qubes 4.0, is true in the default install with Xfce), then a malicious qube could “steal the focus” by creating a window just before you press Ctrl+Shift+V, and it would receive the data instead of your intended target. (Focus stealing is a risk any time you are typing confidential data, but a Qubes clipboard paste probably presents the greatest risk of leaking an entire password before you have time to react.) You may be able to mitigate this risk by changing the window manager configuration. For example, with Xfce, you could run ``xfwm4-settings`` in dom0, go to the “Focus” tab, and un-check “Automatically give focus to newly created windows”. However, we have not confirmed whether such settings are sufficient to prevent a malicious qube from stealing the focus in all cases.

Clipboard automatic policy enforcement
--------------------------------------


The Qubes clipboard :doc:`RPC policy </user/advanced-topics/rpc-policy>` is configurable in:

.. code:: text

      /etc/qubes-rpc/policy/qubes.ClipboardPaste



You may wish to configure this policy in order to prevent user error. For example, if you are certain that you never wish to paste *into* your “vault” app qube (and it is highly recommended that you do not), then you should edit the policy as follows:

.. code:: text

      @anyvm  vault   deny
      @anyvm  @anyvm  ask



Automatic clipboard wiping
--------------------------


By default data pasted into a qube will remain there until user copies something else or restarts the qube. It’s possible to make the ``qubes-gui`` process inside a qube wipe the clipboard automatically after a minute from the last paste operation. This helps protect users from accidentally pasting the old content of the clipboard like a password in the wrong place like a browser search bar. Since qubes don’t share the same clipboard, software like KeePassXC isn’t able to automatically wipe the clipboard of other qubes.

To enable automatic wiping of the clipboard after a minute use ``qvm-service``:

.. code:: console

      qvm-service --enable VMNAME gui-agent-clipboard-wipe



Shortcut configuration
----------------------


The copy/paste shortcuts are configurable via ``qvm-features``, e.g.

.. code:: console

      qvm-features dom0 gui-default-secure-copy-sequence 'Mod4-c'
      qvm-features dom0 gui-default-secure-paste-sequence 'Mod4-v'



would change the *copy/paste to global clipboard* to the Win key plus c for copy, or v for paste.

You need to restart Qubes for the changes to take effect.
