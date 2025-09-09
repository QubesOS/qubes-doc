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


*Also see* :doc:`how to edit the website </developer/general/how-to-edit-the-website>`.

Some of the Qubes OS website pages are stored as plain text Markdown files in the `qubesos.github.io <https://github.com/QubesOS/qubesos.github.io>`__ repository.


Markdown conventions
^^^^^^^^^^^^^^^^^^^^

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


Do not write HTML inside Markdown documents (except in rare, unavoidable cases, such as `alerts <#alerts>`__). In particular, never include HTML or CSS for styling, formatting, or white space control. That belongs in the (S)CSS files instead.

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

.. code:: bash

      > **Note:** This is an important note!



This renders as:

   **Note:** This is an important note!

There are two problems with this:

1. It is a violation of the `separation of content and presentation <https://en.wikipedia.org/wiki/Separation_of_content_and_presentation>`__, since it abuses markup syntax in order to achieve unintended stylistic results. The Markdown (and HTML, if any) should embody the *content* of the documentation, while the *presentation* is handled by (S)CSS.

2. It is an abuse of quotation syntax for text that is not actually a quotation. (You are not quoting anyone here. You’re just telling the reader to note something and trying to draw their attention to your note visually.)



Instead, an example of an appropriate way to stylistically distinguish a portion of text is by using `alerts <#alerts>`__. Consider also that extra styling and visual distinction may not even be necessary. In most cases, traditional writing methods are perfectly sufficient, e.g.,:

.. code:: bash

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

Correct use of terminology
^^^^^^^^^^^^^^^^^^^^^^^^^^

Familiarize yourself with the terms defined in the :doc:`glossary </user/reference/glossary>`. Use these terms consistently and accurately throughout your writing.

Sentence case in headings
^^^^^^^^^^^^^^^^^^^^^^^^^

Use sentence case (rather than title case) in headings for the reasons explained `here <https://www.sallybagshaw.com.au/articles/sentence-case-v-title-case/>`__. In particular, since the authorship of the Qubes documentation is decentralized and widely distributed among users from around the world, many contributors come from regions with different conventions for implementing title case, not to mention that there are often differing style guide recommendations even within a single region. It is much easier for all of us to implement sentence case consistently across our growing body of pages, which is very important for managing the ongoing maintenance burden and sustainability of the documentation.

Writing command-line examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When providing command-line examples:

- Tell the reader where to open a terminal (dom0 or a specific domU), and show the command along with its output (if any) in a code block, e.g.:

  .. code:: bash

        Open a terminal in dom0 and run:
        ```
        $ cd test
        $ echo Hello
        Hello
        ```

- Precede each command with the appropriate command prompt: At a minimum, the prompt should contain a trailing ``#`` (for the user ``root``) or ``$`` (for other users) on Linux systems and ``>`` on Windows systems, respectively.
- Don’t try to add comments inside the code block. For example, *don’t* do this:

  .. code:: bash

        Open a terminal in dom0 and run:
        ```
        # Navigate to the new directory
        $ cd test
        # Generate a greeting
        $ echo Hello
        Hello
        ```

  The ``#`` symbol preceding each comment is ambiguous with a root command prompt. Instead, put your comments *outside* of the code block in normal prose.



Variable names in commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

Syntactically distinguish variables in commands. For example, this is ambiguous:

.. code:: bash

      $ qvm-run --dispvm=disposable-template --service qubes.StartApp+xterm

It should instead be:

.. code:: bash

      $ qvm-run --dispvm=<DISPOSABLE_TEMPLATE> --service qubes.StartApp+xterm

Note that we syntactically distinguish variables in three ways:

1. Surrounding them in angled brackets (``< >``)

2. Using underscores (``_``) instead of spaces between words

3. Using all capital letters



We have observed that many novices make the mistake of typing the surrounding angled brackets (``< >``) on the command line, even after substituting the desired real value between them. Therefore, in documentation aimed at novices, we also recommend clarifying that the angled brackets should not be typed. This can be accomplished in one of several ways:

- Explicitly say something like “without the angled brackets.”
- Provide an example command using real values that excludes the angled brackets.
- If you know that almost all users will want to use (or should use) a specific command containing all real values and no variables, you might consider providing exactly that command and forgoing the version with variables. Novices may not realize which parts of the command they can substitute with different values, but if you’ve correctly judged that they should use the command you’ve provided as is, then this shouldn’t matter.


Capitalization of "qube"
^^^^^^^^^^^^^^^^^^^^^^^^

We introduced the term :term:`qube` as a user-friendly alternative to the term :term:`vm` in the context of Qubes OS. Nonetheless, “qube” is a common noun like the words “compartment” and “container.” Therefore, in English, “qube” follows the standard capitalization rules for common nouns. For example, “I have three qubes” is correct, while “I have three Qubes” is incorrect. Like other common nouns, “qube” should still be capitalized at the beginnings of sentences, the beginnings of sentence-case headings, and in title-case headings. Note, however, that starting a sentence with the plural of “qube” (e.g., “Qubes can be shut down…”) can be ambiguous, since it may not be clear whether the referent is a plurality of qubes, :term:`qubes os`, or even the Qubes OS Project itself. Hence, it is generally a good idea to rephrase such sentences in order to avoid this ambiguity.

Many people feel a strong temptation to capitalize the word “qube” all the time, like a proper noun, perhaps because it’s a new and unfamiliar term that’s closely associated with a particular piece of software (namely, Qubes OS). However, these factors are not relevant to the capitalization rules of English. In fact, it’s not unusual for new common nouns to be introduced into English, especially in the context of technology. For example, “blockchain” is a relatively recent technical term that’s a common noun. Why is it a common noun rather than a proper noun? Because proper nouns refer to *particular* people, places, things, and ideas. There are many different blockchains. However, even when there was just one, the word still denoted a collection of things rather than a particular thing. It happened to be the case that there was only one member in that collection at the time. For example, if there happened to be only one tree in the world, that wouldn’t change the way we capitalize sentences like, “John sat under a tree.” Intuitively, it makes sense that the addition and removal of objects from the world shouldn’t cause published books to become orthographicallly incorrect while sitting on their shelves.

Accordingly, the reason “qube” is a common noun rather than a proper noun is because it doesn’t refer to any one specific thing (in this case, any one specific virtual machine). Rather, it’s the term for any virtual machine in a Qubes OS installation. (Technically, while qubes are currently implemented as virtual machines, Qubes OS is independent of its underlying compartmentalization technology. Virtual machines could be replaced with a different technology, and qubes would still be called “qubes.”)

I have several qubes in my Qubes OS installation, and you have several in yours. Every Qubes OS user has their own set of qubes, just as each of us lives in some neighborhood on some street. Yet we aren’t tempted to treat words like “neighborhood” or “street” as proper nouns (unless, of course, they’re part of a name, like “Acorn Street”). Again, while this might seem odd because “qube” is a new word that we invented, that doesn’t change how English works. After all, *every* word was a new word that someone invented at some point (otherwise we wouldn’t have any words at all). We treat “telephone,” “computer,” “network,” “program,” and so on as common nouns, even though those were all new technological inventions in the not-too-distant past (on a historical scale, at least). So, we shouldn’t allow ourselves to be confused by irrelevant factors, like the fact that the inventors happened to be *us* or that the invention was *recent* or is not in widespread use among humanity.

English language conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the sake of consistency and uniformity, the Qubes documentation aims to follow the conventions of American English, where applicable. (Please note that this is an arbitrary convention for the sake consistency and not a value judgment about the relative merits of British versus American English.)


Incorrect Example
^^^^^^^^^^^^^^^^^

.. code:: bash

      ## How to Foo

      Fooing is the process by which one foos. There are both general and specific
      versions of fooing, which vary in usefulness depending on your goals, but for
      the most part, all fooing is fooing.

      To foo in Qubes 3.2:

         $ qvm-foo <foo-bar>

      Note that this does not work in Qubes 4.0, where there is a special widget
      for fooing, which you can find in the lower-right corner of the screen in
      the Foo Manager. Alternatively, you can use the more general `qubes-baz`
      command introduced in 4.0:

         $ qubes-baz --foo <bar>

      Once you foo, make sure to close the baz before fooing the next bar.


Correct Example
^^^^^^^^^^^^^^^

.. code:: bash

      ## Qubes 3.2

      ### How to Foo

      Fooing is the process by which one foos. There are both general and specific
      versions of fooing, which vary in usefulness depending on your goals, but for
      the most part, all fooing is fooing.

      To foo:

         $ qvm-foo <foo-bar>

      Once you foo, make sure to close the baz before fooing the next bar.

      ## Qubes 4.0

      ### How to Foo

      Fooing is the process by which one foos. There are both general and specific
      versions of fooing, which vary in usefulness depending on your goals, but for
      the most part, all fooing is fooing.

      There is a special widget for fooing, which you can find in the lower-right
      corner of the screen in the Foo Manager. Alternatively, you can use the
      general `qubes-baz` command:

         $ qubes-baz --foo <bar>

      Once you foo, make sure to close the baz before fooing the next bar.


Subdividing the page into clearly-labeled sections for each release has several benefits:

- It preserves good content for older (but still supported) releases. Many documentation contributors are also people who prefer to use the latest release. Many of them are tempted to *replace* existing content that applies to an older, supported release with content that applies only to the latest release. This is somewhat understandable. Since they only use the latest release, they may be focused on their own experience, and they may even regard the older release as deprecated, even when it’s actually still supported. However, allowing this replacement of content would do a great disservice to those who still rely on the older, supported release. In many cases, these users value the stability and reliability of the older, supported release. With the older, supported release, there has been more time to fix bugs and make improvements in both the software and the documentation. Consequently, much of the documentation content for this release may have gone through several rounds of editing, review, and revision. It would be a tragedy for this content to vanish while the very set of users who most prize stability and reliability are depending on it.
- It’s easy for readers to quickly find the information they’re looking for, since they can go directly to the section that applies to their release.
- It’s hard for readers to miss information they need, since it’s all in one place. In the incorrect example, information that the reader needs could be in any paragraph in the entire document, and there’s no way to tell without reading the entire page. In the correct example, the reader can simply skim the headings in order to know which parts of the page need to be read and which can be safely ignored. The fact that some content is repeated in the two release-specific sections is not a problem, since no reader has to read the same thing twice. Moreover, as one release gets updated, it’s likely that the documentation for that release will also be updated. Therefore, content that is initially duplicated between release-specific sections will not necessarily stay that way, and this is a good thing: We want the documentation for a release that *doesn’t* change to stay the same, and we want the documentation for a release that *does* change to change along with the software.
- It’s easy for documentation contributors and maintainers to know which file to edit and update, since there’s only one page for all Qubes OS releases. Initially creating the new headings and duplicating content that applies to both is only a one-time cost for each page, and many pages don’t even require this treatment, since they apply to all currently-supported Qubes OS releases.


By contrast, an alternative approach, such as segregating the documentation into two different branches, would mean that contributions that apply to both Qubes releases would only end up in one branch, unless someone remembered to manually submit the same thing to the other branch and actually made the effort to do so. Most of the time, this wouldn’t happen. When it did, it would mean a second pull request that would have to be reviewed. Over time, the different branches would diverge in non-release-specific content. Good general content that was submitted only to one branch would effectively disappear once that release was deprecated. (Even if it were still on the website, no one would look at it, since it would explicitly be in the subdirectory of a deprecated release, and there would be a motivation to remove it from the website so that search results wouldn’t be populated with out-of-date information.)

For further discussion about release-specific documentation in Qubes, see `here <https://groups.google.com/d/topic/qubes-users/H9BZX4K9Ptk/discussion>`__.

Git conventions
---------------

Please follow our :ref:`Git commit message guidelines <developer/code/coding-style:commit message guidelines>`.

.. |alerts| image:: /attachment/doc/website_alerts.png
