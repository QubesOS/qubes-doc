====================
How to edit a policy
====================

There are three ways to edit a policy:

* with :program:`Qubes OS Global Config`, the **recommended way** for the most common policies

* with :program:`Qubes Policy Editor`, a graphical text editor dedicated to this task

* with :program:`qubes-policy-editor`, a command-line text editor that will validate the file
  before saving it.

In this how-to, we will restrict the clipboard policy to prevent an *untrusted* qube from pasting something in a *vault* qube.

Edit a policy with :program:`Qubes OS Global Config`
----------------------------------------------------

1. You need to go to the :guilabel:`Clipboard` tab.

2. Under :guilabel:`Custom policy`, select :guilabel:`Add`

3. Change the dropdown items to get this: ":guilabel:`untrusted` will :guilabel:`never` be allowed to paste into the clipboard of :guilabel:`vault`"

   .. note:: if there is any inconsistency, a pop-up will warn you about that

4. Click on :guilabel:`Accept` and at the bottom of the window, select either :guilabel:`OK` or :guilabel:`Apply`.

Edit a policy with :program:`Qubes Policy Editor`
-------------------------------------------------

1. Open :program:`Qubes Policy Editor`

2. You have to:

   * either open an existing file using :menuselection:`&File --> &Open`  or :kbd:`Ctrl` + :kbd:`O`
   * or create a new file using :menuselection:`&File --> &New` or :kbd:`Ctrl` + :kbd:`N`

     In that case, you need to choose a filename. The filename can only contain alphanumeric characters, underscores and hyphens. The common practice is to use a name like :file:`{30}-{user}.policy` where:

     * :samp:`{30}` indicates the priority (i.e. the default policies start with ``90`` while the policies from :program:`Qubes OS Global Config` start with ``50``)
     * :samp:`{user}` could be any name

     In order to change some clipboard policy, :file:`20-clipboard` could be a good name.

3. Add a line to the file. In order to prevent the *untrusted* qube from pasting to the *vault* qube, the line should be:

   .. code: text
        
      qubes.ClipboardPaste *       untrusted       vault   deny

4. If you have made any edits and if the format is correct, you will be able to select :guilabel:`Save Changes` and :guilabel:`Save and Exit`, or to press :kbd:`Ctrl` + :kbd:`S`. 

Edit a policy with :program:`qubes-policy-editor`
-------------------------------------------------

`qubes-policy-editor` is a command-line tool that ensures that the filename of the policy is correct and that the syntax is valid.

You can invoke the program with any valid filename (only alphanumeric characters, underscores and hyphens), with or without the ``.policy`` extension:

.. code: console

   [root@dom0] # qubes-policy-editor 20-clipboard

Your default editor will open. After saving the file, `qubes-policy-editor` will check the file and tell you if there is something wrong with the syntax.

See also
--------

* :doc:`/developer/services/qrexec`
* `qubes-core-qrexec's documentation <https://dev.qubes-os.org/projects/qubes-core-qrexec/en/latest/>`__
