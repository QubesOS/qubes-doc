Contributing to `qubes-doc`
===========================

Thank you for your interest in contributing to `qubes-doc`, the Qubes OS
Project's dedicated documentation repository! Please take a moment to
familiarize yourself with the terms defined in the [glossary], and try to use
these terms consistently and accurately throughout your writing and editing.

Please report all documentation issues in [qubes-issues]. 


Markdown Conventions
--------------------

All the documentation is written in Markdown for maximum accessibility. When
making contributions, please try to observe the following style conventions:

 * Use spaces instead of tabs.
 * Hard wrap Markdown lines at 80 characters.
 * If appropriate, make numerals in numbered lists match between Markdown
   source and HTML output.
   * Rationale: In the event that a user is required to read the Markdown source
     directly, this will make it easier to follow, e.g., numbered steps in a set
     of instructions.
 * Use hanging indentations  
   where appropriate.
 * Use underline headings (`=====` and `-----`) if possible. If this is not
   possible, use Atx-style headings on both the left and right sides
   (`### H3 ###`).
 * Use `[reference-style][ref]` links.  
 
`[ref]: https://daringfireball.net/projects/markdown/syntax#link`

([This][md] is a great source for learning about Markdown.)


Git Conventions
---------------

Please attempt to follow these conventions when writing your Git commit
messages:

 * Separate the subject line from the body with a blank line.
 * Limit the subject line to approximately 50 characters.
 * Capitalize the subject line.
 * Do not end the subject line with a period.
 * Use the imperative mood in the subject line.
 * Wrap the body at 72 characters.
 * Use the body to explain *what* and *why* rather than *how*.

For details, examples, and the rationale behind each of these conventions,
please see [this blog post][git-commit], which is the source of this list.


[glossary]: https://www.qubes-os.org/doc/glossary/
[qubes-issues]: https://github.com/QubesOS/qubes-issues/issues
[md]: https://daringfireball.net/projects/markdown/
[git-commit]: http://chris.beams.io/posts/git-commit/

