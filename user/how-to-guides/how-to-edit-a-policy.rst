====================
How to edit a policy
====================

There are three ways to edit a :ref:`policy <user/reference/glossary:policies>`:

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

1. Open :program:`Qubes Policy Editor`

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

See also
--------

* :doc:`/developer/services/qrexec`
* `qubes-core-qrexec's documentation <https://dev.qubes-os.org/projects/qubes-core-qrexec/en/latest/>`__
