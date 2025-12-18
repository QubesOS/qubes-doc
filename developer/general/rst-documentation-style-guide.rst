===========================================
reStructuredText documentation style guide
===========================================

*Also see* :doc:`How to edit the documentation </developer/general/how-to-edit-the-rst-documentation/>`.

This page explains the standards we follow for writing, formatting, and organizing the documentation.
Please follow these guidelines and conventions when editing the rST documentation.
For the standards governing the website (as opposed to the rST documentation hosted on `https://doc.qubes-os.org <https://doc.qubes-os.org>`__),
please see the :doc:`Website style guide </developer/general/website-style-guide>`.
If you wish to submit a pull request regarding content hosted on the website, please refer to
:doc:`How to edit the website </developer/general/how-to-edit-the-website/>`.

reStructuredText conventions
----------------------------

All the documentation is written in `reStructuredText (rST) <https://docutils.sourceforge.io/rst.html>`__. When making contributions, please observe the following style conventions.
If you’re not familiar with reStructuredText syntax, `the Sphinx primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`__
is a great resource, as well as `this quick reStructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`__.
Please always be mindful that rST syntax is sensitive to indentation!


Directives
^^^^^^^^^^

A `directive <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`__ is a generic block of explicit markup,
provided by `Docutils <https://www.docutils.org/>`__ and extended by `Sphinx <https://www.sphinx-doc.org/>`__.
Directives are used to insert non-paragraph content, such as images, tables, and code blocks.
Example directives are:

.. code:: rst

   .. image::
   .. code::
   .. figure::

Directives start with ``..``, followed by directive name, arguments, options, and indented content.

Images
""""""

To include images (without a caption), use the ``image`` directive.
You need to specify the path to the image and an alt text.

.. code:: rst

  .. image:: path/to/image.png
     :alt: Alternative text
     :width: 200px
     :align: center

Read The Docs and the HTML `sphinx-rtd-theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`__ in use
have a responsive design, which allows the documentation to render appropriately across all screen sizes.

Make sure to link only to images in the :file:`attachment/doc` folder of the `qubes-doc <https://github.com/QubesOS/qubes-doc>`__ repository.
**Do not attempt to link to images hosted on other websites**.

See also :ref:`how_to_add_images` for the further information and about using the ``figure`` directive.

Lists
"""""

`Lists <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#lists-and-quote-like-blocks>`__ can be bullet lists (\*, +, -), enumerated lists (1., 2., etc.), definition lists, field lists.

Nested lists must be separated from the parent list items by blank lines:

.. code:: rst

  - Item 1
  - Item 2

    - Subitem 2.1
    - Subitem 2.2

  - Item 3

Numbered lists can be autonumbered using the ``#`` sign.

.. code:: rst

  #. Item 1
  #. Item 2

    #. Subitem 2.1
    #. Subitem 2.2

  #. Item 3

Item 3 will start at 1.

Code blocks
"""""""""""

When writing code blocks, use syntax highlighting within the `code <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code>`__
or `code-block <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`__.

By specifying the language, you enable pygments, which show syntax color coding for that code sample (see `here <https://pygments.org/languages/>`__ for a list of supported languages).

.. code:: rst

   .. code:: language

      code



Use ``[...]`` for anything omitted.

For inlining small code snippets you can use the `code role <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-code>`__ as in

.. code:: rst

   :code:`:term:`qube``

You can add line numbers to code examples with the ``:linenos:`` parameter.

.. code:: rst

    .. code:: python
      :linenos:

       def hello_world():
         print("Hello, world!")


You can have certain lines with the ``:emphasize-lines:`` parameter.

.. code:: rst

 .. code:: python
   :emphasize-lines: 1,3,4



For Python use ``python``.

.. code:: rst

    .. code:: python

      string_var = 'python'

For Bash use ``bash``.

.. code:: rst

    .. code:: bash

       #!/bin/bash

For a terminal session use ``console``.

.. code:: rst

    .. code:: console

       $ echo "Hello"

For text output use ``output``.

.. code:: rst

    .. code:: output

       some output

For text use ``text``.

.. code:: rst

    .. code:: text

       some text


Tables
""""""

We adhere to the list tables directive by docutils as described `here <https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table-1>`__.

A simple example would be:

    .. code:: rst

        .. list-table::
           :widths: 15 10
           :align: center
           :header-rows: 1

           * - Header 1
             - Header 2
           * - Cell 1
             - Cell 2
           * - Cell 3
             - Cell 4

Admonitions, messages, and warnings
"""""""""""""""""""""""""""""""""""

`Admonitions, messages, and warnings <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#admonitions-messages-and-warnings>`__ are used to draw the reader’s attention to important information, such as warnings, and for stylistic purposes.
They are typically styled as colored text boxes, usually accompanied by icons provided out of the box by Sphinx and rST.

**Alerts should generally be used somewhat sparingly**, so as not to cause `alert fatigue <https://en.wikipedia.org/wiki/Alarm_fatigue>`__.

Here are examples of several types of alerts:

.. code:: rst

     .. hint::
        If you would like to avoid prefixing commands with [...]

     .. note::
       Using Rufus to create the installation medium means that you [...]

     .. warning::
       Qubes OS is not meant to be installed inside a virtual machine as [...]

     .. danger::
       Qubes has no control over what happens on your computer before [...]

These render as:

.. hint::
   If you would like to avoid prefixing commands with [...]

.. note::
   Using Rufus to create the installation medium means that you [...]

.. warning::
   Qubes OS is not meant to be installed inside a virtual machine as [...]

.. danger::
   Qubes has no control over what happens on your computer before [...]


You can also provide a `custom title to the admonition <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-admonition>`_:

.. code:: rst

   .. admonition:: Did you know?

      The Qubes OS installer is completely offline. It doesn't even load [...]

Rendering as:

.. admonition:: Did you know?

   The Qubes OS installer is completely offline. It doesn't even load [...]

Glossary
""""""""

Most of the `glossaries <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#glossary>`__ are present in :file:`/user/reference/glossary.rst`, like:

.. code:: rst

   .. glossary::

      qube
         A secure compartment in Qubes OS.

Anywhere else in the documentation you can link to a term using the `term role <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-term>`__: which automatically generates a hyperlink to the glossary entry. :code:`:term:`qube`` produces the following link: :term:`qube`.

.. admonition:: See also

   :ref:`customizing-text-link`

.. _rst-roles:

Roles
^^^^^

Sphinx uses interpreted text `roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`__ to insert semantic markup into documents
and thus enhance the readability and consistency of the documentation.

Syntax is as follows:

.. code:: rst

   :rolename:`content`

In Qubes OS documentation the `doc <https://www.sphinx-doc.org/en/master/usage/referencing.html#role-doc>`__ and
`ref <https://www.sphinx-doc.org/en/master/usage/referencing.html#role-ref>`__ roles are used extensively
as described in :ref:`cross-referencing`.

.. admonition:: See also

   :ref:`list-roles-used-documentation`

.. _cross-referencing:

Cross-referencing
^^^^^^^^^^^^^^^^^

You can reference other parts of the documentation such as:

* :ref:`a whole page <developer/general/rst-documentation-style-guide:Cross-referencing a page>`, using `doc role <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-doc>`__ and a path
* :ref:`specific sections <developer/general/rst-documentation-style-guide:Cross-referencing a section with a header>` such as headers, using `ref <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-ref>`__ with a path and the header content
* :ref:`unique labels <developer/general/rst-documentation-style-guide:Cross-referencing a custom label>`, created for this purpose
* :ref:`glossary terms <developer/general/rst-documentation-style-guide:Glossary>`, using `term <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-term>`__
* :ref:`external documentation <developer/general/rst-documentation-style-guide:External cross-referencing>` like :doc:`core-admin's documentation <core-admin:index>`
* a lot of :ref:`other items <developer/general/rst-documentation-style-guide:Cross-referencing code>`: python objects, C constructs, program options

Cross-referencing a page
""""""""""""""""""""""""

To cross-reference a page, use the `doc role <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-doc>`__ with a path. To get a link to the file called :file:`intro.rst` in the :file:`introduction/` directory, use:

  .. code:: rst

   :doc:`/introduction/intro`

The path could be relative to the current document, or absolute. In that case, the path starts from the root of the ``qubes-doc`` repository, **with a leading slash** (``/``). You have to **remove the file extension** (``.rst``).

Cross-referencing a section with a header
"""""""""""""""""""""""""""""""""""""""""

To cross-reference a section with a header, use the `ref role <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-ref>`__ with a path and the reStructuredText content of the header, separated by a colon:

  .. code:: rst

   :ref:`introduction/intro:What is Qubes OS?`

Note that with the `ref role <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-ref>`__ the path starts **without a leading slash** (``/``). You might also encounter the normalized header content: in lowercase, with normalized spaces. This is another way to achieve the same result.

You can get a list of the generated labels after building the documentation. If your build directory is :file:`_build/html`, run the following:

.. code:: console

   [~/qubes-doc] $ python3 -m sphinx.ext.intersphinx _build/html/objects.inv

You can also run that command against the current online version of the docs:

.. code:: console

   $ python3 -m sphinx.ext.intersphinx https://doc.qubes-os.org/en/latest/objects.inv

.. note::

   Make sure to **use the reStructuredText content**, and not the built output.

   You can copy-paste headers from the HTML build but it might fail in some situations (i.e.: with quotation marks or any markup).

Cross-referencing a custom label
""""""""""""""""""""""""""""""""

.. note:: No need to create a custom label if you don't reference it somewhere else

Frequently linked sections, especially when they have a long name can be referenced using a custom label.

First, you have to create a custom label, **only use lowercase alphanumeric characters and hyphens**:

.. code:: rst

   .. _disposable-with-pci-devices:

   Named disposable for service qubes without PCI devices via GUI
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, to reference this label, use the custom label instead of the path and the header separated by a colon.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - reStructuredText markup
     - output
   * - .. code:: rst

          :ref:`disposable-with-pci-devices`

     - :ref:`disposable-with-pci-devices`

You can create an arbitrary label anywhere, but make sure to reference it with an explicit title.

.. hint:: For further options and use cases please refer to `Cross-references in the Sphinx project <https://www.sphinx-doc.org/en/master/usage/referencing.html>`__.

.. _customizing-text-link:

Customizing the text content of a link
""""""""""""""""""""""""""""""""""""""

Most cross-references can generate an automatic title. If it doesn't fit the sentence where it is placed, you can `change the text content of the link <https://www.sphinx-doc.org/en/master/usage/referencing.html#xref-syntax>`__ with the following markup. **Avoid doing this if it only duplicates the automatic title.**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - reStructuredText markup
     - output
   * - .. code:: rst

          :ref:`without PCI devices <disposable-with-pci-devices>`

     - :ref:`without PCI devices <disposable-with-pci-devices>`

External cross-referencing
""""""""""""""""""""""""""

You can make a cross-reference to any of the projects of the external developer's documentation (hosted on `https://dev.qubes-os.org <https://dev.qubes-os.org/en/latest/>`__):

* :doc:`core-admin <core-admin:index>`
* :doc:`core-admin-client <core-admin-client:index>`
* :doc:`core-qrexec <core-qrexec:index>`

To do such a cross-reference, use the usual cross-reference syntax but with the following prefix: :samp:`{PROJECT_NAME}:` (replace :samp:`{PROJECT_NAME}` by the name of the project). As an example, if you want to link to the index of the core-admin documentation, use this:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - reStructuredText markup
     - output
   * - .. code:: rst

          :doc:`core-admin:index`

     - :doc:`core-admin:index`

This is equivalent to using ``:doc:`index``` inside the core-admin documentation. This works with any role like `ref <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-ref>`__, `option <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-option>`__, etc. Write the role like you would normally do inside the target documentation, then prefix it with the name of the target (``core-admin`` in the previous example). Something working as :code:`:ref:`some-title`` inside ``core-admin``'s documentation will become :samp:`:ref:`core-admin:some-title``. The only exception concerns the `doc role <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-doc>`__: **do not prepend the file path with a slash** (``/``).

Even if it works without it, **always prefix the external cross-references** with the name of the project, to help other contributors and maintainers figuring out what the target is while reading the reStructuredText source.

.. note::

   Intersphinx `can list all the available links <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#showing-all-links-of-an-intersphinx-mapping-file>`__ to another project with the following command:

   .. code:: console

       python3 -m sphinx.ext.intersphinx https://dev.qubes-os.org/projects/core-admin/en/latest/objects.inv

   You can replace ``core-admin`` by any of the projects listed above.

Cross-referencing code
""""""""""""""""""""""

You can create a reference to `any documented python objects <https://www.sphinx-doc.org/en/master/usage/domains/python.html#python-xref-roles>`__ as well as `configuration values <https://www.sphinx-doc.org/en/master/usage/referencing.html#role-confval>`__, `command-line options <https://www.sphinx-doc.org/en/master/usage/referencing.html#role-option>`__ or `C language constructs <https://www.sphinx-doc.org/en/master/usage/domains/c.html#c-xref-roles>`__.

**To link to the option** called :option:`--help <core-admin-client:qubes-prefs.--help>` in :program:`qvm-prefs` described in core-admin-client documentation, use:


.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - reStructuredText markup
     - output
   * - .. code:: rst

          :option:`core-admin-client:qubes-prefs --help`
     - :option:`core-admin-client:qubes-prefs --help`

**To link to the python class** :py:class:`core-admin:qubes.vm.dispvm.DispVM` in the core-admin documentation use:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - reStructuredText markup
     - output
   * - .. code:: rst

          :py:class:`core-admin:qubes.vm.dispvm.DispVM`

     - :py:class:`core-admin:qubes.vm.dispvm.DispVM`

Do not use a :ref:`custom title <customizing-text-link>` to shorten the link label. **Use the tilde modifier** (``~``) instead:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - reStructuredText markup
     - output
   * - .. code:: rst

          :py:class:`~core-admin:qubes.vm.dispvm.DispVM`

     - :py:class:`~core-admin:qubes.vm.dispvm.DispVM`

**If a cross-reference points to a missing reference** (i.e.: reference to a removed component), prefix the reference with an exclamation mark (``!``). If the function :py:func:`!old_function` has been removed but is still referenced, to discuss the old implementation use:

.. code:: rst

   :py:func:`!old_function`

Hyperlink to other websites syntax
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use `embedded links <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#external-links>`__ like

.. code:: rst

    `website <https://example.com/>`__

**Do not use reference-style links** like

.. code:: rst

   Some text link_

    :: _link:: https://example.org

This facilitates the localization process.

.. warning::

   Always use :ref:`cross-references <cross-referencing>` rather than hyperlinks to link to the documentation (``doc.qubes-os.org`` and ``dev.qubes-os.org`` domains), because using those hyperlinks breaks:

   - Serving the documentation offline
   - Documentation localization
   - Generating offline documentation

HTML and CSS
^^^^^^^^^^^^

**Do not write HTML inside rST documents.** In particular, never include HTML or CSS for styling, formatting, or white space control.
That belongs to the Sphinx theme instead.


Headings
^^^^^^^^

To create a section header use an underline filled with punctuation characters. The length of the underlining should be as long as the text of the header.

Each punctuation character correspond to a header level. Qubes OS uses the convention in `Python Developer’s Guide for documenting <https://devguide.python.org/documentation/markup/#sections>`__ which are as follows:

* ``#`` with overline, for parts
* ``*`` with overline, for chapters
* ``=`` for sections, corresponding to the main title of a HTML page
* ``-`` for subsections
* ``^`` for subsubsections
* ``"`` for paragraphs

Although possible, using a level under the paragraph level should be avoided.

Here is a simple example of a page with a title and three nested levels of heading:

.. code:: rst

  ==========
  Main Title
  ==========

  Subsection
  ----------

  Sub-subsection
  ^^^^^^^^^^^^^^

  Paragraph
  """""""""



Text decorations
^^^^^^^^^^^^^^^^

Emphasis and Italics


- *Italics*: Use single asterisks

 .. code:: rst

    *italics*

- **Bold**: Use double asterisks.

 .. code:: rst

    **bold**

- ``Monospace``: Use backticks.

 .. code:: rst

    ``monospace``


Paragraph
^^^^^^^^^

Paragraphs are plain texts where indentation matters. Separate paragraphs by leaving a blank line between them.


Indentation
^^^^^^^^^^^

**Use spaces instead of tabs.** Use hanging indentations where appropriate.
rST is an indentation sensitive markup language, similar to Python, please maintain consistent indentation (3 spaces) for readability.


Line wrapping
^^^^^^^^^^^^^

**Do not hard wrap text**, except where necessary (e.g., inside code blocks).

Writing guidelines
------------------

Correct use of terminology
^^^^^^^^^^^^^^^^^^^^^^^^^^

Familiarize yourself with the terms defined in the :doc:`glossary </user/reference/glossary>`. Use these terms consistently and accurately throughout your writing.

Sentence case in headings
^^^^^^^^^^^^^^^^^^^^^^^^^

**Use sentence case** (rather than title case) in headings for the reasons explained `here <https://www.sallybagshaw.com.au/articles/sentence-case-v-title-case/>`__. In particular, since the authorship of the Qubes documentation is decentralized and widely distributed among users from around the world, many contributors come from regions with different conventions for implementing title case, not to mention that there are often differing style guide recommendations even within a single region. It is much easier for all of us to implement sentence case consistently across our growing body of pages, which is very important for managing the ongoing maintenance burden and sustainability of the documentation.

Writing command-line examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Tell the reader where to open a terminal** (dom0 or a specific domU), and show the command along with its output (if any) in a code block, e.g.:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - reStructuredText markup
     - output
   * - .. code:: rst

          Open a terminal in dom0 and run:

          .. code:: console

             [user@dom0] $ cd test
             [user@dom0 ~/test] $ echo Hello
             Hello

     - Open a terminal in dom0 and run:

       .. code:: console

          [user@dom0] $ cd test
          [user@dom0 ~/test] $ echo Hello
          Hello

**Precede each command with the appropriate command prompt**:

- at a minimum, the prompt should contain a trailing ``#`` (for the user ``root``) or ``$`` (for other users) on Linux systems and ``>`` on Windows systems, respectively.
- if possible, **indicate the qube used** (i.e.: ``dom0``)
- if relevant, **indicate the path** where the command should occur.
- following all the previous recommendations and **adding the username** could provide a familiar prompt to the user.

  .. list-table::
     :widths: 10 50 50
     :header-rows: 1

     * - style
       - reStructuredText markup
       - output

     * - minimal
       - .. code:: rst

            .. code:: console

               $ cd test

       - .. code:: console

            $ cd test

     * - qube name
       - .. code:: rst

            .. code:: console

               [dom0] $ cd test

       - .. code:: console

            [dom0] $ cd test

     * - with path
       - .. code:: rst

            .. code:: console

               [dom0 /tmp] $ cd test

       - .. code:: console

            [dom0 /tmp] $ cd test

     * - full
       - .. code:: rst

            .. code:: console

               [user@dom0 /tmp] $ cd test

       - .. code:: console

            [user@dom0 /tmp] $ cd test

.. warning::

   **Don’t try to add comments inside the code block**. For example, *don’t* do this:

   .. code:: console

      # Navigate to the new directory
      $ cd test
      # Generate a greeting
      $ echo Hello

   The ``#`` symbol preceding each comment is ambiguous with a root command prompt. Instead, put your comments *outside* of the code block in normal prose.


Variable names in commands
^^^^^^^^^^^^^^^^^^^^^^^^^^


**Syntactically distinguish variables in commands**. For example, this is ambiguous:

.. code:: console

     $ qvm-run --dispvm=disposable-template --service qubes.StartApp+xterm



It should instead be:

.. code:: console

     $ qvm-run --dispvm=<DISPOSABLE_TEMPLATE> --service qubes.StartApp+xterm



Note that we syntactically distinguish variables in three ways:

1. **Surrounding them in angled brackets** (``< >``)

2. **Using underscores** (``_``) instead of spaces between words

3. **Using all capital letters**



We have observed that many novices make the mistake of typing the surrounding angled brackets (``< >``) on the command line, even after substituting the desired real value between them. Therefore, in documentation aimed at novices, we also recommend clarifying that the angled brackets should not be typed. This can be accomplished in one of several ways:

- **Explicitly say something like "without the angled brackets".**

- **Provide an example command using real values** that excludes the angled brackets.

- If you know that almost all users will want to use (or should use) a specific command containing all real values and no variables, you might consider **providing exactly that command** and forgoing the version with variables. Novices may not realize which parts of the command they can substitute with different values, but if you’ve correctly judged that they should use the command you’ve provided as is, then this shouldn’t matter.



Capitalization of "qube"
^^^^^^^^^^^^^^^^^^^^^^^^


We introduced the term :term:`qube` as a user-friendly alternative to the term :term:`vm` in the context of Qubes OS. Nonetheless, “qube” is a common noun like the words “compartment” and “container.” Therefore, in English, “qube” follows the standard capitalization rules for common nouns. For example, “I have three qubes” is correct, while “I have three Qubes” is incorrect. Like other common nouns, “qube” should still be capitalized at the beginnings of sentences, the beginnings of sentence-case headings, and in title-case headings. Note, however, that starting a sentence with the plural of “qube” (e.g., “Qubes can be shut down…”) can be ambiguous, since it may not be clear whether the referent is a plurality of qubes, :term:`qubes os`, or even the Qubes OS Project itself. Hence, it is generally a good idea to rephrase such sentences in order to avoid this ambiguity.

Many people feel a strong temptation to capitalize the word “qube” all the time, like a proper noun, perhaps because it’s a new and unfamiliar term that’s closely associated with a particular piece of software (namely, Qubes OS). However, these factors are not relevant to the capitalization rules of English. In fact, it’s not unusual for new common nouns to be introduced into English, especially in the context of technology. For example, “blockchain” is a relatively recent technical term that’s a common noun. Why is it a common noun rather than a proper noun? Because proper nouns refer to *particular* people, places, things, and ideas. There are many different blockchains. However, even when there was just one, the word still denoted a collection of things rather than a particular thing. It happened to be the case that there was only one member in that collection at the time. For example, if there happened to be only one tree in the world, that wouldn’t change the way we capitalize sentences like, “John sat under a tree.” Intuitively, it makes sense that the addition and removal of objects from the world shouldn’t cause published books to become orthographically incorrect while sitting on their shelves.

Accordingly, the reason “qube” is a common noun rather than a proper noun is because it doesn’t refer to any one specific thing (in this case, any one specific virtual machine). Rather, it’s the term for any virtual machine in a Qubes OS installation. (Technically, while qubes are currently implemented as virtual machines, Qubes OS is independent of its underlying compartmentalization technology. Virtual machines could be replaced with a different technology, and qubes would still be called “qubes.”)

I have several qubes in my Qubes OS installation, and you have several in yours. Every Qubes OS user has their own set of qubes, just as each of us lives in some neighborhood on some street. Yet we aren’t tempted to treat words like “neighborhood” or “street” as proper nouns (unless, of course, they’re part of a name, like “Acorn Street”). Again, while this might seem odd because “qube” is a new word that we invented, that doesn’t change how English works. After all, *every* word was a new word that someone invented at some point (otherwise we wouldn’t have any words at all). We treat “telephone,” “computer,” “network,” “program,” and so on as common nouns, even though those were all new technological inventions in the not-too-distant past (on a historical scale, at least). So, we shouldn’t allow ourselves to be confused by irrelevant factors, like the fact that the inventors happened to be *us* or that the invention was *recent* or is not in widespread use among humanity.

English language conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


For the sake of consistency and uniformity, the Qubes documentation aims to follow the conventions of American English, where applicable. (Please note that this is an arbitrary convention for the sake consistency and not a value judgment about the relative merits of British versus American English.)

Organizational guidelines
-------------------------


Do not duplicate documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Duplicating documentation is almost always a bad idea**. There are many reasons for this. The main one is that almost all documentation has to be updated as some point. When similar documentation appears in more than one place, it is very easy for it to get updated in one place but not the others (perhaps because the person updating it doesn’t realize it’s in more than once place). When this happens, the documentation as a whole is now inconsistent, and the outdated documentation becomes a trap, especially for novice users. Such traps are often more harmful than if the documentation never existed in the first place. The solution is to **link** to existing documentation rather than duplicating it. There are some exceptions to this policy (e.g., information that is certain not to change for a very long time), but they are rare.

.. _core-vs-external-documentation:

Core vs. external documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: See also

   :doc:`/introduction/external-documentation`

If you’ve written a piece of documentation that is not appropriate for `qubes-doc <https://github.com/QubesOS/qubes-doc>`__, we encourage you to submit it to the `Qubes Forum <https://forum.qubes-os.org/docs>`__ instead. However, *linking* to external documentation from `qubes-doc <https://github.com/QubesOS/qubes-doc>`__ is perfectly fine. Indeed, the maintainers of the `Qubes Forum <https://forum.qubes-os.org/>`__ should regularly submit PRs against the :ref:`external-documentation` index (see :ref:`edit_doc_index`) to add and update external links.

Many contributors do not realize that there is a significant amount of work involved in *maintaining* documentation after it has been written. They may wish to write documentation and submit it to the core docs, but they see only their own writing process and fail to consider that it will have to be kept up-to-date and consistent with the rest of the docs for years afterward. Submissions to the core docs also have to :ref:`undergo a review process <developer/general/how-to-edit-the-rst-documentation:security>` to ensure accuracy before being merged, which takes up valuable time from the team. We aim to maintain high quality standards for the core docs (style and mechanics, formatting), which also takes up a lot of time.

**If the documentation involves anything external to the Qubes OS Project** (such as a website, platform, program, protocol, framework, practice, or even a reference to a version number), the documentation is likely to become outdated when that external thing changes. It’s also important to periodically review and update this documentation, especially when a new Qubes release comes out. Periodically, there may be technical or policy changes that affect all the core documentation. The more documentation there is relative to maintainers, the harder all of this will be. Since there are many more people who are willing to write documentation than to maintain it, these individually small incremental additions amount to a significant maintenance burden for the project.

On the positive side, **we consider the existence of community documentation to be a sign of a healthy ecosystem**, and this is quite common in the software world. The community is better positioned to write and maintain documentation that applies, combines, and simplifies the official documentation, e.g., tutorials that explain how to install and use various programs in Qubes, how to create custom VM setups, and introductory tutorials that teach basic Linux concepts and commands in the context of Qubes. In addition, just because the Qubes OS Project has officially written and maintains some flexible framework, such as ``qrexec``, it does not make sense to include every tutorial that says “here’s how to do something cool with ``qrexec`` in the core docs. **Such tutorials generally also belong in the community documentation.**

See `#4693 <https://github.com/QubesOS/qubes-issues/issues/4693>`__ for more background information.


Release-specific documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We maintain one set of documentation for each Qubes OS release, with source files in a named branch (eg Source for r4.3 documentation is in the r4.3 branch of qubes-doc). Documentation is updated on a continual, rolling basis. Our first priority is to document the **current, stable releases** of Qubes. Our second priority is to document the next, upcoming release (if any) that is currently in the beta or release candidate stage.

Each version is available at Read The Docs. Documentation for the current release is loaded by default, but other versions can be accessed from the flyout version menu.

In general, you do not need to mention the version in the body text of documentation for any release. Make sure that any PR you submit is relevant to the version you are targeting, and is a PR against the correct branch: if the change is relevant to more than one release, create a PR against one branch - the documentation maintainers should ensure that the PR is appropriately handled.


Git conventions
---------------


Please follow our :ref:`Git commit message guidelines <developer/code/coding-style:commit message guidelines>`.



Cheatsheet: Markdown vs. reStructuredText
-----------------------------------------

For the documentation contributors more familiar with Markdown, here is a small cheatsheet
highlighting essential differences.

Cheatsheet: Headings
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Markdown markup
     - reStructuredText markup
   * - .. code:: markdown

          [...]
          # Title
          [...]

          ## Subsection
          [...]

          ### Subsubsection
          [...]

          #### Paragraph
          [...]

     - .. code:: rst

        =====
        Title
        =====

        Subsection
        ----------

        Subsubsection
        ^^^^^^^^^^^^^

        Paragraph
        """""""""

Cheatsheet: Hyperlinks and cross-references
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Markdown markup
     - reStructuredText markup

   * - .. code:: markdown

          [Link Text](/doc/path/to/some-file)

     - .. code:: rst

          :doc:`/path/to/some-file`

   * - .. code:: markdown

          [Link Text](/doc/path/to/some-file#some-title)

     - .. code:: rst

          :ref:`/path/to/some-file:Some title`

   * - .. code:: markdown

          a [qube](/doc/glossary#qube)

     - .. code:: rst

          :term:`qube`

   * - .. code:: markdown

          [Link Text](http://example.com)

     - .. code:: rst

          `Link Text <http://example.com>`__

Cheatsheet: Text Decorations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Markdown markup
     - reStructuredText markup

   * - .. code:: markdown

         *Italic* or _Italic_

     - .. code:: rst

        *Italic*

   * - .. code:: markdown

          **Bold** or __Bold__

     - .. code:: rst

          **Bold**

   * - .. code:: markdown

          ~~Strikethrough~~

     - .. code:: rst

          :strike:`Strikethrough`

   * - .. code:: markdown

          ***Bold and italic***

     - .. warning::

          Impossible!

.. admonition:: See also

   :ref:`developer/general/rst-documentation-style-guide:Text decorations`

Cheatsheet: Lists
^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Markdown markup
     - reStructuredText markup

   * - .. code:: markdown

          - Item 1
          - Item 2
            - Subitem 1
            - Subitem 2

          1. Item 1
          2. Item 2
             a. Subitem 1
             b. Subitem 2

     - .. code:: rst

          - Item 1
          - Item 2
            - Subitem 1
            - Subitem 2

          1. Item 1
          2. Item 2
             a. Subitem 1
             b. Subitem 2

.. admonition:: See also

   * :ref:`developer/general/rst-documentation-style-guide:Lists`

Cheatsheet: Tables
^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Markdown markup
     - reStructuredText markup

   * - .. code:: markdown

          | Header 1 | Header 2 |
          |----------|----------|
          | Cell 1   | Cell 2   |
          | Cell 3   | Cell 4   |

     - .. code:: rst

          .. list-table::
             :widths: 10 10
             :header-rows: 1

             * - Header 1
               - Header 2
             * - Cell 1
               - Cell 2
             * - Cell 3
               - Cell 4

.. admonition:: See also

   :ref:`developer/general/rst-documentation-style-guide:Tables`

Cheatsheet: Code Blocks
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Markdown markup
     - reStructuredText markup

   * - .. code:: markdown

          ```python
          print("Hello, world!")
          ```
     - .. code:: rst

          .. code:: python

              print("Hello, world!")

.. admonition:: See also

   :ref:`developer/general/rst-documentation-style-guide:Code blocks`

Alerts and Warnings
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Markdown markup
     - reStructuredText markup

   * - .. code:: markdown

          <div class="alert alert-info" role="alert">
            <i class="fa fa-info-circle"></i>
            <b>Note:</b> This is a note
          </div>

     - .. code:: rst

          .. note::

             This is a note.

.. admonition:: See also

   :ref:`developer/general/rst-documentation-style-guide:Admonitions, messages, and warnings`


.. _list-roles-used-documentation:

List of the roles used in documentation
---------------------------------------

.. list-table::
   :widths: 10 50 50
   :header-rows: 1

   * - name
     - reStructuredText markup
     - output


   * - `:guilabel: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-guilabel>`__

     - .. code:: rst

        :guilabel:`&Apply`

     - :guilabel:`&Apply`

   * - `:file: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-file>`__

     - .. code:: rst

        :file:`~/QubesIncoming/disp{XXXX}`

     - :file:`~/QubesIncoming/disp{XXXX}`

   * - `:program: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-program>`__

     - .. code:: rst

        :program:`qvm-copy`

     - :program:`qvm-copy`

   * - `:menuselection: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-menuselection>`__

     - .. code:: rst

        :menuselection:`Settings --> &Advanced`

     - :menuselection:`Settings --> &Advanced`

   * - `:samp: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-samp>`__

     - .. code:: rst

        :samp:`disp{XXXX}`

     - :samp:`disp{XXXX}`

   * - `:kbd: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-kbd>`__

     - .. code:: rst

        :kbd:`Ctrl`

     - :kbd:`Ctrl`

   * - `:abbr: <https://www.sphinx-doc.org/en/master/usage/referencing.html#role-abbr>`__

     - .. code:: rst

        :abbr:`OCR (Optical Character Recognition)`

     -  :abbr:`OCR (Optical Character Recognition)`

   * - `:code: <https://www.sphinx-doc.org/en/master/usage/referencing.html#role-code>`__

     - .. code:: rst

          :code:`qvm-ls --help`

     - :code:`qvm-ls --help`

   * - `:mimetype: <https://www.sphinx-doc.org/en/master/usage/referencing.html#role-mimetype>`__

     - .. code:: rst

        :mimetype:`application/pdf`

     - :mimetype:`application/pdf`

Please continue using the above or new ones where appropriate.

.. admonition:: See also

   :ref:`rst-roles`

