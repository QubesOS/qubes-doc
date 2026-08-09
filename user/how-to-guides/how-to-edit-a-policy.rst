====================
How to edit a policy
====================

There are three ways to edit a :term:`policy <policies>`:

* with :program:`Qubes OS Global Config`, the **recommended way** for the most common policies

* with :program:`Qubes Policy Editor`, a graphical text editor dedicated to this task

* with :program:`qubes-policy-editor`, a command-line text editor that will validate the file
  before saving it.

In this how-to, we will restrict the clipboard policy to prevent an *untrusted* qube from pasting something in a *vault* qube, **as an example**.

.. _edit-a-policy-with-qubes-os-global-config:

Edit a policy with :program:`Qubes OS Global Config`
----------------------------------------------------

:program:`Qubes OS Global Config` allows you to edit the most common policies. Following our clipboard example:

1. you need to go to the :guilabel:`Clipboard` tab.

2. Under :guilabel:`Custom policy`, select :guilabel:`Add`

3. Change the drop-down items to get this: ":guilabel:`untrusted` will :guilabel:`never` be allowed to paste into the clipboard of :guilabel:`vault`"

   .. note:: if there is any inconsistency, a pop-up will warn you about that

4. Click on :guilabel:`Accept` and at the bottom of the window, select either :guilabel:`OK` or :guilabel:`Apply`.

Edit a policy with :program:`Qubes Policy Editor`
-------------------------------------------------

1. Open :program:`Qubes Policy Editor`:

   .. image:: /attachment/doc/r4.3/qubes-policy-editor.png
      :alt:
      :width: 100%

2. You have to either:

   * open an existing file using :menuselection:`&File --> &Open`  or :kbd:`Ctrl` + :kbd:`O`
   * or create a new file using :menuselection:`&File --> &New` or :kbd:`Ctrl` + :kbd:`N`

     In that case, you need to choose a filename. The filename can only contain alphanumeric characters, underscores and hyphens. The common practice is to use a name like :file:`{30}-{user}.policy` where:

     * :samp:`{30}` indicates the priority (i.e. the default policies start with ``90`` while the policies from :program:`Qubes OS Global Config` start with ``50``)
     * :samp:`{user}` could be any name

    In order to override some clipboard policy, :file:`30-clipboard` could be a good name. Starting with ``30`` makes sure that the file will be read before any file starting with ``31`` or more, especially :file:`50-config-clipboard.policy` (this file is automatically created if you :ref:`edit-a-policy-with-qubes-os-global-config`). If you want to create a policy that will never override the policies from :program:`Qubes OS Global Config`, use a name starting with a number between ``51`` and ``89``. The default policies from Qubes OS start with ``90``, so using a number equal or superior might be useless.

3. Add a line to the file. In order to prevent the *untrusted* qube from pasting to the *vault* qube, the line should be:

   .. code:: text

      qubes.ClipboardPaste *       untrusted       vault   deny

4. If you have made any edits and if the format is correct, you will be able to select :guilabel:`Save Changes` and :guilabel:`Save and Exit`, or to press :kbd:`Ctrl` + :kbd:`S`.

Edit a policy with :program:`qubes-policy-editor`
-------------------------------------------------

:program:`qubes-policy-editor` is a command-line tool that ensures that the syntax of the policy is valid. You have to run it as root:

.. code:: console

   [root@dom0] # qubes-policy-editor

An editor will open; it will be your default editor if you have set the environment variable ``$EDITOR`` or ``$VISUAL``, otherwise it will fall back to :program:`vi`. After saving the file, :program:`qubes-policy-editor` will check the content and tell you if there is something wrong with the syntax.

It will open :file:`30-user.policy` by default but you can invoke the program with any valid filename (only alphanumeric characters, underscores and hyphens), without the ``.policy`` extension:

.. code:: console

   [root@dom0] # qubes-policy-editor 30-clipboard

In that case, :program:`qubes-policy-editor` will also check that the filename of the policy is correct.

.. _manage-file-operations-policies:

Examples: how to manage the file operations policies between qubes
------------------------------------------------------------------

.. note::

   This section assumes that you are familiar with :doc:`/user/how-to-guides/how-to-copy-and-move-files` and :doc:`/user/how-to-guides/how-to-use-disposables`.

You might want to control how your qubes can operate file exchanges between them. The default behavior is to ``ask`` for operations involving existing qubes and to ``allow`` file operations using a new disposable.

Control access for moving and copying files with :program:`Qubes OS Global Config`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to restrict the possibility to copy or move files from your `personal` to your `work` qube with :program:`Qubes OS Global Config`, follow :ref:`edit-a-policy-with-qubes-os-global-config` but use the :guilabel:`File Access` tab instead. Set this exception:

   :guilabel:`personal` will :guilabel:`never` be allowed to copy files to :guilabel:`work`

This will create the file :file:`/etc/qubes/policy.d/50-config-filecopy.policy`.

Using :program:`Qubes Policy Editor` or :program:`qubes-policy-editor`, you can achieve the same result with this policy:

.. code-block::

   qubes.Filecopy * personal work deny

.. note:: Make sure to name it with a number lower than ``50`` if you want to override the settings of :program:`Qubes OS Global Config`.

.. container:: two-columns

   .. graphviz::
      :caption: Before (default policy)
      :alt: personal and work can exchange files
      :align: center

      digraph base {
        personal, work [penwidth=3 fontname="Open Sans"]
        personal [color="#e7e532"]
        work [color="#3874d8"]

        personal -> work [xlabel=ask]
        work -> personal [label=ask]
      }

   .. graphviz::
      :caption: After
      :alt: only personal can send files to work
      :align: center

      digraph base {
        personal, work [penwidth=3 fontname="Open Sans"]
        personal [color="#e7e532"]
        work [color="#3874d8"]

        work -> personal [label=ask]
        personal -> work [color="#bd2727" arrowhead=none style=dotted label=deny fontcolor="#bd2727"]

      }

Deny action to any qube
"""""""""""""""""""""""

You can also deny the :ref:`qubes.Filecopy <qubes.Filecopy>` operation from personal to any other qube:

With :program:`Qubes OS Global Config`
   :guilabel:`personal` will :guilabel:`never` be allowed to copy files to :guilabel:`ALL QUBES`

Or with a policy editor
   .. code-block::

      qubes.Filecopy * personal @anyvm deny

.. graphviz::
   :caption: No file operations between qubes
   :alt: personal can't copy or move files to the other qubes
   :align: center

   digraph base {
     personal, work, untrusted, vault [penwidth=3 fontname="Open Sans"]
     personal [color="#e7e532"]
     work [color="#3874d8"]
     vault [color="#bfbfbf"]
     untrusted [color="#bd2727"]

     personal -> vault [color="#bd2727" arrowhead=none style=dotted label=deny]
     personal -> work [color="#bd2727" arrowhead=none style=dotted xlabel=deny]
     personal -> untrusted [color="#bd2727" arrowhead=none style=dotted label=deny]
   }

Mixing ``deny``, ``allow`` and ``ask`` in a policy
""""""""""""""""""""""""""""""""""""""""""""""""""

You can also allow only a limited set of qubes. When you trigger a copy or move operation, no target qube is specified. So, even if you allow the operation, the confirmation dialog from dom0 will still open and ask you to choose, but only between *work* or *vault*.

With :program:`Qubes OS Global Config`
   * :guilabel:`personal` will :guilabel:`always` allow files to be copied to :guilabel:`work`
   * :guilabel:`personal` will :guilabel:`always` allow files to be copied to :guilabel:`vault`
   * :guilabel:`personal` will :guilabel:`never` be allowed to copy files to :guilabel:`ALL QUBES`

   .. warning::

      You will still have to manually edit one line because this tool doesn't allow you to do it so, after completing the previous instructions, open :guilabel:`View or edit raw policy file for: qubes.Filecopy` and append the first line in the raw policy example below.

Or with a policy editor
   .. code-block::
      :linenos:
      :emphasize-lines: 1

      qubes.Filecopy * personal @default ask
      qubes.Filecopy * personal work allow
      qubes.Filecopy * personal vault allow
      qubes.Filecopy * personal @anyvm deny

.. graphviz::
   :caption: Limited operations between qubes
   :alt: personal can copy or move files to vault and work, but not untrusted
   :align: center

   digraph base {
     personal, work, untrusted, vault [penwidth=3 fontname="Open Sans"]
     personal [color="#e7e532"]
     work [color="#3874d8"]
     vault [color="#bfbfbf"]
     untrusted [color="#bd2727"]

     personal -> untrusted [color="#bd2727" arrowhead=none style=dotted label=deny]
     personal -> work [xlabel=ask]
     personal -> vault [label=ask]
   }

.. _set-default-target:

Set the default target qube
"""""""""""""""""""""""""""

.. hint::

   This customization is not possible in :program:`Qubes OS Global Config`, use a policy editor instead.

Using the previous example, each time you trigger a :ref:`qubes.Filecopy <qubes.Filecopy>` action, the dom0 dialog asks you to explicitly choose a qube. If you want the `work` qube to be the pre-selected target of this dialog, append ``default_target=work`` at the end of the third line in our previous example:

.. code-block::
   :linenos:
   :emphasize-lines: 1

   qubes.Filecopy * personal @default ask default_target=work
   qubes.Filecopy * personal work allow
   qubes.Filecopy * personal vault allow
   qubes.Filecopy * personal @anyvm deny

Control access for converting or opening files and URLs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are more actions that can be managed by policies:

:ref:`qubes.OpenInVM <qubes.OpenInVM>`
   Used by: :guilabel:`Open in other qube`, :guilabel:`Edit in disposable qube`, :guilabel:`View in disposable qube`, :guilabel:`QubesOS Edit In Disposable VM`, :ref:`qvm-open-in-vm <qvm-open-in-vm>` and  :ref:`qvm-open-in-dvm <qvm-open-in-dvm>`

_`qubes.OpenURL`
   Used by :ref:`qvm-open-in-vm <qvm-open-in-vm>` and  :ref:`qvm-open-in-dvm <qvm-open-in-dvm>`

_`qubes.PdfConvert`
   Used by :guilabel:`Convert in disposable qube` on a PDF file and :ref:`qvm-convert-pdf <qvm-convert-pdf>`

_`qubes.GetImageRGBA`
   Used by :guilabel:`Convert in disposable qube` on a picture file and :ref:`qvm-convert-img <qvm-convert-img>`

.. hint::

   Before continuing, make sure to have read:

   * :ref:`open-link-non-default-disposable`
   * :ref:`open-file-type-in-disposable`

Opening and converting files in an offline disposable
"""""""""""""""""""""""""""""""""""""""""""""""""""""

If you have created :ref:`a new disposable template <create-new-disposable-template>` and :ref:`changed its net qube <change-disposable-template-settings>` to none, making it offline, you might want to use this disposable template instead of your default disposable template for opening or converting files.

In :program:`Qubes OS Global Config`, in the :guilabel:`Disposables` tab and :guilabel:`Open in Disposable Qube` section:
   :guilabel:`ALL QUBES` will :guilabel:`always` use :guilabel:`offline-dvm`

   Where *offline-dvm* is the name of your disposable template.

Or in a policy editor:
   .. code-block::

      qubes.OpenInVM * @anyvm @dispvm allow target=@dispvm:offline-dvm

   Where *offline-dvm* is the name of you disposable template.

Opening links when the default disposable is offline
""""""""""""""""""""""""""""""""""""""""""""""""""""

The default policy allows links to be opened in the default disposable, without any confirmation dialog. If your default disposable is offline (because you changed the :term:`net qube`), this behavior is not convenient. You have several options:

1. In :program:`Qubes OS Global Config`, in the :guilabel:`Disposables` tab and :guilabel:`Open URL in Disposable` section:
      :guilabel:`ALL QUBES` will :guilabel:`ask` and default to :guilabel:`Default Disposable Template`

   Or in a policy editor:
      .. code-block::

        qubes.OpenURL * @anyvm @dispvm ask default_target=@dispvm

   You can change :guilabel:`Default Disposable Template` or ``@dispvm`` by an online qube if you want.

2. If you don't want to confirm the action, assuming you have an online disposable template called *online-dvm*, you can use this policy:

   .. code-block::

      qubes.OpenURL * @anyvm @dispvm allow target=@dispvm:online-dvm

   Using the :ref:`target <target>` argument will replace your default qube by *online-dvm* when opening URLs. This is useful if you want to keep the default disposable offline (i.e.: to open files) while being able to conveniently follow links.

3. Following the example in :ref:`set-default-target`, you can allow a limited set of qubes and combine it with the first option in this list so that you are prompted each time you want to open a link. I.e.:

   .. code-block::
      :linenos:

      qubes.OpenURL * @anyvm @dispvm                           ask default_target=@dispvm
      qubes.OpenURL * @anyvm @dispvm                           allow
      qubes.OpenURL * @anyvm @dispvm:online-dvm                allow
      qubes.OpenURL * @anyvm @dispvm:whonix-workstation-18-dvm allow
      qubes.OpenURL * @anyvm @tag:sys-disposable               deny
      qubes.OpenURL * @anyvm @type:DispVM                      allow
      qubes.OpenURL * @anyvm @anyvm deny

   When opening a URL in a disposable, you will be prompted (line 1) to choose between:

   * the default disposable (line 2)
   * a disposable based on *online-dvm* (line 3)
   * a disposable based on *whonix-workstation-18-dvm* (line 4)
   * any existing disposable (line 6) **except** the ones tagged with ``sys-disposable`` (line 5). If you use disposable :term:`service qubes <service qube>` you can tag them so it won't be possible to use them.

.. seealso::

   :doc:`/developer/services/qrexec`
      Introduction to qrexec
   :doc:`core-qrexec:index`
      The whole document of the core-qrexec module: python code, RPC Policies format and manpages
