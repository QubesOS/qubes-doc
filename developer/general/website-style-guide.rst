===================
Website style guide
===================


This page explains the standards we follow for building and maintaining the website. Please follow these guidelines and conventions when modifying the website. For the standards governing the documentation in particular, please see the :doc:`documentation style guide </developer/general/rst-documentation-style-guide>`.


Coding conventions
------------------

The following conventions apply to the website as a whole, including everything written in HTML, CSS, YAML, and Liquid. These conventions are intended to keep the codebase consistent when multiple collaborators are working on it. They should be understood as a practical set of rules for maintaining order in this specific codebase rather than as a statement of what is objectively right or good.

General practices
^^^^^^^^^^^^^^^^^


- Use comments to indicate the purposes of different blocks of code. This makes the file easier to understand and navigate.

- Use descriptive variable names. Never use one or two letter variable names. Avoid obscure abbreviations and made-up words.

- In general, make it easy for others to read your code. Your future self will thank you, and so will your collaborators!

- `Don’t Repeat Yourself (DRY)! <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`__ Instead of repeating the same block of code multiple times, abstract it out into a separate file and ``include`` that file where you need it.

Whitespace
^^^^^^^^^^

- Always use spaces. Never use tabs.
- Each indentation step should be exactly two (2) spaces.
- Whenever you add an opening tag, indent the following line. (Exception: If you open and close the tag on the same line, do not indent the following line.)
- Indent Liquid the same way as HTML.
- In general, the starting columns of every adjacent pair of lines should be no more than two spaces apart (example below).
- No blank or empty lines. (Hint: When you feel you need one, add a comment on that line instead.)


Indentation example
^^^^^^^^^^^^^^^^^^^

Here’s an example that follows the indentation rules:

.. code:: html

      <table>
        <tr>
          <th title="Anchor Link"><span class="fa fa-link"></span></th>
          {% for item in secs.htmlsections[0].columns %}
            <th>{{ item.title }}</th>
          {% endfor %}
        </tr>
        {% for canary in site.data.sec-canary reversed %}
          <tr id="{{ canary.canary }}">
            <td><a href="#{{ canary.canary }}" class="fa fa-link black-icon" title="Anchor link to Qubes Canary row: Qubes Canary #{{ canary.canary }}"></a></td>
            <td>{{ canary.date }}</td>
            <td><a href="https://github.com/QubesOS/qubes-secpack/blob/master/canaries/canary-{{ canary.canary }}-{{ canary.date | date: '%Y' }}.txt">Qubes Canary #{{ canary.canary }}</a></td>
          </tr>
        {% endfor %}
      </table>


Markdown style guide and conventions
------------------------------------


*Also see* :doc:`How to edit the website </developer/general/how-to-edit-the-website>`.

Some of the Qubes OS website pages are stored as plain text Markdown files in the `qubesos.github.io <https://github.com/QubesOS/qubesos.github.io>`__ repository.
When making contributions to Markdown files, please observe the following style conventions. If you’re not familiar with Markdown syntax, `this <https://daringfireball.net/projects/markdown/>`__ is a great resource.

Hyperlink syntax
^^^^^^^^^^^^^^^^

Use non-reference-style links like :code:`[website](https://example.com/)`. Do *not* use reference-style links like ``[website][example]``, ``[website][]`` or ``[website]``. This facilitates the localization process.

Relative vs. absolute links
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Always use relative rather than absolute paths for internal website links. For example, use ``/donate/`` instead of ``https://www.qubes-os.org/donate/``.

You may use absolute URLs in the following cases:

- External links
- URLs that appear inside code blocks (e.g., in comments and document templates, and the plain text reproductions of `QSBs <https://www.qubes-os.org/security/qsb/>`__ and `Canaries <https://www.qubes-os.org/security/canary/>`__), since they’re not hyperlinks
- Git repo files like ``README.md`` and ``CONTRIBUTING.md``, since they’re not part of the website itself but rather of the auxiliary infrastructure supporting the website


This rule is important because using absolute URLs for internal website links breaks:

- Serving the website offline
- Website localization
- Generating offline documentation
- Automatically redirecting Tor Browser visitors to the correct page on the onion service mirror


Image linking
^^^^^^^^^^^^^

To add an image to a page, use the following syntax in the main document.

.. code:: markdown

  [![Image Title](/attachment/doc/image.png)](/attachment/doc/image.png)

This will make the image a hyperlink to the image file, allowing the reader to click on the image in order to view the full image by itself. This is important. Following best practices, our website has a responsive design, which allows the website to render appropriately across all screen sizes. When viewing this page on a smaller screen, such as on a mobile device, the image will automatically shrink down to fit the screen. If visitors cannot click on the image to view it in full size, then, depending on their device, they may have no way see the details in the image clearly.

In addition, make sure to link only to images in the `qubes-attachment <https://github.com/QubesOS/qubes-attachment>`__ repository. Do not attempt to link to images hosted on other websites.

HTML and CSS
^^^^^^^^^^^^


Do not write HTML inside Markdown documents (except in rare, unavoidable cases, such as :ref:`developer/general/website-style-guide:alerts`). In particular, never include HTML or CSS for styling, formatting, or white space control. That belongs in the (S)CSS files instead.

Headings
^^^^^^^^

Do not use ``h1`` headings (single ``#`` or ``======`` underline). These are automatically generated from the ``title:`` line in the YAML front matter.

Use Atx-style syntax for headings: ``##h2``, ``### h3``, etc. Do not use underlining syntax (``-----``).

Indentation
^^^^^^^^^^^

Use spaces instead of tabs. Use hanging indentations where appropriate.

Lists
^^^^^

If appropriate, make numerals in numbered lists match between Markdown source and HTML output. Some users read the Markdown source directly, and this makes numbered lists easier to follow.

Code blocks
^^^^^^^^^^^

When writing code blocks, use `syntax highlighting <https://github.github.com/gfm/#info-string>`__ where possible (see `here <https://github.com/jneen/rouge/wiki/List-of-supported-languages-and-lexers>`__ for a list of supported languages). Use ``[...]`` for anything omitted.

Line wrapping
^^^^^^^^^^^^^

Do not hard wrap text, except where necessary (e.g., inside code blocks).

Do not use Markdown syntax for styling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, there is a common temptation to use block quotations (created by beginning lines with the ``>`` character) in order to stylistically distinguish some portion of text from the rest of the document, e.g.:

.. code:: markdown

      > **Note:** This is an important note!



This renders as:

   **Note:** This is an important note!

There are two problems with this:

1. It is a violation of the `separation of content and presentation <https://en.wikipedia.org/wiki/Separation_of_content_and_presentation>`__, since it abuses markup syntax in order to achieve unintended stylistic results. The Markdown (and HTML, if any) should embody the *content* of the documentation, while the *presentation* is handled by (S)CSS.

2. It is an abuse of quotation syntax for text that is not actually a quotation. (You are not quoting anyone here. You’re just telling the reader to note something and trying to draw their attention to your note visually.)



Instead, an example of an appropriate way to stylistically distinguish a portion of text is by using :ref:`developer/general/website-style-guide:alerts`. Consider also that extra styling and visual distinction may not even be necessary. In most cases, traditional writing methods are perfectly sufficient, e.g.,:

.. code:: markdown

      **Note:** This is an important note.


This renders as:

**Note:** This is an important note.

Alerts
^^^^^^

Alerts are sections of HTML used to draw the reader’s attention to important information, such as warnings, and for stylistic purposes. They are typically styled as colored text boxes, usually accompanied by icons. Alerts should generally be used somewhat sparingly, so as not to cause `alert fatigue <https://en.wikipedia.org/wiki/Alarm_fatigue>`__ and since they must be written in HTML instead of Markdown, which makes the source less readable and more difficult to work with for localization and automation purposes. Here are examples of several types of alerts and their recommended icons:

.. code:: html

      <div class="alert alert-success" role="alert">
        <i class="fa fa-check-circle"></i>
        <b>Did you know?</b> The Qubes OS installer is completely offline. It doesn't
        even load any networking drivers, so there is no possibility of
        internet-based data leaks or attacks during the installation process.
      </div>

      <div class="alert alert-info" role="alert">
        <i class="fa fa-info-circle"></i>
        <b>Note:</b> Using Rufus to create the installation medium means that you <a
        href="https://github.com/QubesOS/qubes-issues/issues/2051">won't be able</a>
        to choose the "Test this media and install Qubes OS" option mentioned in the
        example below. Instead, choose the "Install Qubes OS" option.
      </div>

      <div class="alert alert-warning" role="alert">
        <i class="fa fa-exclamation-circle"></i>
        <b>Note:</b> Qubes OS is not meant to be installed inside a virtual machine
        as a guest hypervisor. In other words, <b>nested virtualization</b> is not
        supported. In order for a strict compartmentalization to be enforced, Qubes
        OS needs to be able to manage the hardware directly.
      </div>

      <div class="alert alert-danger" role="alert">
        <i class="fa fa-exclamation-triangle"></i>
        <b>Warning:</b> Qubes has no control over what happens on your computer
        before you install it. No software can provide security if it is installed on
        compromised hardware. Do not install Qubes on a computer you don't trust. See
        [installation security](/doc/install-security/) for more
        information.
      </div>



These render as:

|alerts|

Writing guidelines
^^^^^^^^^^^^^^^^^^

For writing guidelines please refer to the :ref:`appropriate section <developer/general/rst-documentation-style-guide:writing guidelines>` in the rST documentation style guide
with the exemption of the following:

Writing command-line examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When providing command-line examples:

- Tell the reader where to open a terminal (dom0 or a specific domU), and show the command along with its output (if any) in a code block, e.g.:

  .. code:: markdown

        Open a terminal in dom0 and run:
        ```
        $ cd test
        $ echo Hello
        Hello
        ```

- Precede each command with the appropriate command prompt: At a minimum, the prompt should contain a trailing ``#`` (for the user ``root``) or ``$`` (for other users) on Linux systems and ``>`` on Windows systems, respectively.
- Don’t try to add comments inside the code block. For example, *don’t* do this:

  .. code:: markdown

        Open a terminal in dom0 and run:
        ```
        # Navigate to the new directory
        $ cd test
        # Generate a greeting
        $ echo Hello
        Hello
        ```

  The ``#`` symbol preceding each comment is ambiguous with a root command prompt. Instead, put your comments *outside* of the code block in normal prose.


Git conventions
---------------

Please follow our :ref:`Git commit message guidelines <developer/code/coding-style:commit message guidelines>`.

.. |alerts| image:: /attachment/doc/website_alerts.png
   :alt: Depicts different alerts and messages: note, warning, danger and how they are rendered on the website
